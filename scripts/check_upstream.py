#!/usr/bin/env python3
"""Compare accepted translations with a fixed upstream snapshot; write reports only."""
import argparse
import concurrent.futures
import hashlib
import json
import os
import posixpath
import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
HOST = 'https://docs.n8n.io'
NS = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], stderr=subprocess.PIPE)


def fetch(url):
    if urlsplit(url).scheme != 'https' or urlsplit(url).netloc != 'docs.n8n.io':
        raise ValueError('Unexpected official document URL')
    return subprocess.check_output(
        ['curl', '--fail', '--silent', '--show-error', '--location', '--retry', '2',
         '--max-time', '60', '--max-filesize', '10485760', url], stderr=subprocess.PIPE)


def changed_files(upstream, base, head):
    parts = git(upstream, 'diff', '--name-status', '-z', '--find-renames', base, head).decode().split('\0')
    rows, index = [], 0
    while index < len(parts) and parts[index]:
        status, path = parts[index:index + 2]
        index += 2
        previous = None
        if status.startswith(('R', 'C')):
            previous, path = path, parts[index]
            index += 1
        relevant = lambda value: value.startswith('docs/') or value in {'SPACE_INDEX.md', 'REUSABLE_CONTENT_INDEX.md'}
        if relevant(path) or (previous and relevant(previous)):
            kind = ('更新记录' if path.startswith('docs/changelog/') else
                    '共享片段' if path.startswith('docs/reusable-content/') else
                    '目录' if path.endswith('/SUMMARY.md') else
                    '正文' if path.endswith('.md') and path.startswith('docs/') else
                    '索引' if not path.startswith('docs/') else '资源')
            rows.append({'status': status[0], 'path': path, 'previous_path': previous, 'kind': kind})
    return rows


def translation_backlog(upstream, chinese, registry):
    pending = []
    for file in sorted((upstream / 'docs').rglob('*.md')):
        path = file.relative_to(upstream / 'docs').as_posix()
        if path.startswith('changelog/'):
            continue
        entry = registry.get(path, {})
        translated = chinese / 'docs' / path
        reason = None
        if not translated.is_file() or not entry:
            reason = '新增待翻译'
        elif entry.get('status') != 'translated':
            reason = '翻译未完成'
        elif entry.get('source_sha256') != digest(file.read_bytes()):
            reason = '原文已更新'
        elif entry.get('translation_sha256') != digest(translated.read_bytes()):
            reason = '译文修改尚未登记'
        if reason:
            pending.append({'path': 'docs/' + path, 'reason': reason})
    return pending


def affected_pages(upstream, changes):
    """Resolve file references and reusable IDs, then walk reverse dependencies."""
    files = list((upstream / 'docs').rglob('*.md'))
    reusable = defaultdict(list)
    for file in files:
        if 'reusable-content' in file.parts:
            reusable[file.stem].append(file.relative_to(upstream).as_posix())
    ids = {}
    index_file = upstream / 'REUSABLE_CONTENT_INDEX.md'
    if index_file.exists():
        for identifier, name in re.findall(r'^\| `([^`]+)` \| ([^|]+) \|', index_file.read_text(), re.M):
            candidates = reusable[name.strip()]
            if len(candidates) == 1:
                ids[identifier] = candidates[0]
    reverse = defaultdict(set)
    for file in files:
        path = file.relative_to(upstream).as_posix()
        text = re.sub(r'(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$', '', file.read_text())
        for identifier in re.findall(r'/~/reusable/([^/\s"\']+)', text):
            if identifier in ids:
                reverse[ids[identifier]].add(path)
        refs = re.findall(r'\]\(([^)\n]+)\)|\b(?:src|href)=["\']([^"\']+)["\']', text)
        for pair in refs:
            dest = urlsplit(next(value for value in pair if value))
            if dest.scheme or dest.netloc or not dest.path or dest.path.startswith('/'):
                continue
            target = posixpath.normpath(posixpath.join(posixpath.dirname(path), unquote(dest.path)))
            reverse[target].add(path)
    changed = {row['path'] for row in changes}
    changed.update(row['previous_path'] for row in changes if row['previous_path'])
    queue, affected = list(changed), set()
    while queue:
        for referrer in reverse[queue.pop()]:
            if referrer not in affected and referrer not in changed:
                affected.add(referrer)
                queue.append(referrer)
    return sorted(affected)


def official_urls():
    root = ET.fromstring(fetch(HOST + '/sitemap.xml'))
    urls = {x.text.strip() for x in root.findall('s:url/s:loc', NS)}
    children = [x.text.strip() for x in root.findall('s:sitemap/s:loc', NS)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for data in pool.map(fetch, children):
            urls.update(x.text.strip() for x in ET.fromstring(data).findall('s:url/s:loc', NS))
    if not urls:
        raise ValueError('Official sitemap is empty')
    return sorted(urls)


def api_changes(chinese, read=fetch):
    manifest = json.loads((chinese / '.upstream/generated-api/manifest.json').read_text())
    def check(entry):
        try:
            data = read(entry['source_url'])
            if len(data) < 100 or b'# Page Not Found' in data[:500] or data.lstrip().lower().startswith((b'<!doctype', b'<html')):
                raise ValueError('Invalid Markdown export')
            return {'path': entry['source'], 'url': entry['source_url'],
                    'status': 'changed' if digest(data) != entry['source_sha256'] else 'unchanged',
                    'sha256': digest(data)}
        except Exception as error:
            return {'path': entry['source'], 'url': entry['source_url'], 'status': 'error', 'error': str(error)}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        return list(pool.map(check, manifest))


def markdown_report(report):
    rows = report['changes']
    counts = Counter(row['status'] for row in rows)
    api = report['api']
    base, head = report['base'], report.get('head')
    lines = ['# n8n 官方文档月度更新检查', '', '检查时间：' + report['checked_at'], '',
             '- 已接受的翻译基线：`' + base + '`', '- 本次上游版本：`' + (head or '检查失败') + '`',
             f'- Git 内容差异：{len(rows)} 个文件（新增 {counts["A"]}、修改 {counts["M"]}、删除 {counts["D"]}、移动 {counts["R"]}）',
             f'- 待处理译文：{len(report["pending"])} 份；间接受影响页面：{len(report["affected"])} 份',
             f'- 官网 API：已检查 {len(api)} 份，变化 {sum(r["status"] == "changed" for r in api)} 份，失败 {sum(r["status"] == "error" for r in api)} 份',
             f'- 官网 URL：新增 {len(report["published_added"])} 个，移除 {len(report["published_removed"])} 个', '']
    if head:
        lines += [f'[查看英文差异](https://github.com/n8n-io/n8n-docs/compare/{base}...{head})', '']
    if report.get('offline'):
        lines += ['本次为本地离线检查，官网 API 和路径未检查。', '']
    if report['errors']:
        lines += ['## 检查异常', '', *['- ' + error for error in report['errors']], '']
    lines += ['## 待更新清单', '', '| 文件 | 原因 |', '| --- | --- |']
    todo = report['pending'] + [{'path': r['path'], 'reason': '官网 API 参考已更新'} for r in api if r['status'] == 'changed']
    lines += [f'| `{row["path"].replace("|", "&#124;")}` | {row["reason"]} |' for row in todo]
    if not todo:
        lines += ['| — | 本次已成功检查的范围内，无待更新译文 |']
    lines += ['', '## Git 内容差异', '', '| 类型 | 操作 | 文件 |', '| --- | --- | --- |']
    lines += [f'| {r["kind"]} | {r["status"]} | `{r["path"].replace("|", "&#124;")}` |' for r in rows]
    for title, values in [('间接受影响的页面', report['affected']), ('新增官网路径', report['published_added']), ('移除的官网路径', report['published_removed'])]:
        if values:
            lines += ['', '## ' + title, '', *['- `' + value.replace('`', '') + '`' for value in values]]
    lines += ['', '每次检查都以已接受的原文和逐文件哈希为基线，未处理的更新会持续保留。译文更新与网站发布通过审核后的版本提交推进。', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--upstream-dir', type=Path, help='Use an existing upstream checkout without fetching')
    parser.add_argument('--output', type=Path, default=ROOT / 'reports')
    parser.add_argument('--offline', action='store_true', help='Skip website checks for local tests; the scheduled workflow never sets this')
    args = parser.parse_args()
    source = json.loads((ROOT / 'upstream.json').read_text())
    if source['repository'] != 'n8n-io/n8n-docs' or not re.fullmatch(r'[0-9a-f]{40}', source['commit']):
        raise ValueError('Invalid upstream configuration')
    report = {'checked_at': datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds'),
              'base': source['commit'], 'head': None, 'changes': [], 'pending': [], 'affected': [],
              'api': [], 'published_added': [], 'published_removed': [], 'errors': [], 'offline': args.offline}
    with tempfile.TemporaryDirectory(prefix='n8n-upstream-') as temporary:
        upstream = args.upstream_dir or Path(temporary)
        try:
            if not args.upstream_dir:
                git(upstream, 'init', '--quiet')
                url = 'https://github.com/' + source['repository'] + '.git'
                git(upstream, 'fetch', '--quiet', '--depth=1', url, 'HEAD')
                head = git(upstream, 'rev-parse', 'FETCH_HEAD').decode().strip()
                git(upstream, 'fetch', '--quiet', '--depth=1', url, source['commit'])
                git(upstream, 'checkout', '--quiet', '--detach', head)
            head = git(upstream, 'rev-parse', 'HEAD').decode().strip()
            report['head'] = head
            report['changes'] = changed_files(upstream, source['commit'], head)
            report['pending'] = translation_backlog(upstream, ROOT, json.loads((ROOT / 'translation-status.json').read_text()))
            report['affected'] = affected_pages(upstream, report['changes'])
        except Exception as error:
            report['errors'].append('Git 来源检查失败：' + str(error))
        if not args.offline:
            report['api'] = api_changes(ROOT)
            report['errors'] += [r['path'] + '：' + r['error'] for r in report['api'] if r['status'] == 'error']
            try:
                current = set(official_urls())
                accepted = set(json.loads((ROOT / '.upstream/published-urls.json').read_text())['urls'])
                report['published_added'] = sorted(current - accepted)
                report['published_removed'] = sorted(accepted - current)
            except Exception as error:
                report['errors'].append('官网路径检查失败：' + str(error))
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'upstream-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    text = markdown_report(report)
    (args.output / 'upstream-report.md').write_text(text)
    summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary, 'a') as stream:
            stream.write(text[:900000])
    print(text)
    return 1 if report['errors'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
