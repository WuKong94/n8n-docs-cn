import hashlib
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from check_upstream import affected_pages, api_changes, changed_files, translation_backlog


def sha(value):
    return hashlib.sha256(value).hexdigest()


class UpstreamChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.up = self.root / 'upstream'
        self.cn = self.root / 'chinese'
        (self.up / 'docs').mkdir(parents=True)
        (self.cn / 'docs').mkdir(parents=True)

    def test_pending_translation_is_not_lost_after_repeated_checks(self):
        (self.up / 'docs/page.md').write_text('New English text')
        (self.cn / 'docs/page.md').write_text('原有译文')
        registry = {'page.md': {'status': 'translated', 'source_sha256': sha(b'Old English text'),
                                 'translation_sha256': sha('原有译文'.encode())}}
        for _ in range(2):
            self.assertEqual(translation_backlog(self.up, self.cn, registry),
                             [{'path': 'docs/page.md', 'reason': '原文已更新'}])

    def test_changelog_is_excluded_but_missing_translation_is_pending(self):
        (self.up / 'docs/changelog').mkdir()
        (self.up / 'docs/changelog/release.md').write_text('Release notes')
        (self.up / 'docs/new.md').write_text('New guide')
        self.assertEqual(translation_backlog(self.up, self.cn, {}),
                         [{'path': 'docs/new.md', 'reason': '新增待翻译'}])

    def test_unregistered_chinese_edit_is_reported(self):
        (self.up / 'docs/page.md').write_bytes(b'English')
        (self.cn / 'docs/page.md').write_text('修改后的译文')
        registry = {'page.md': {'status': 'translated', 'source_sha256': sha(b'English'),
                                 'translation_sha256': sha('旧译文'.encode())}}
        self.assertEqual(translation_backlog(self.up, self.cn, registry)[0]['reason'], '译文修改尚未登记')

    def test_git_reports_renames_binary_assets_and_deletions(self):
        def git(*args):
            return subprocess.check_output(['git', '-C', str(self.up), *args], stderr=subprocess.PIPE).decode().strip()
        git('init', '--quiet')
        git('config', 'user.name', 'Test')
        git('config', 'user.email', 'test@example.com')
        (self.up / 'docs/old.md').write_text('A long unchanged paragraph.\n' * 10)
        (self.up / 'docs/remove.md').write_text('Remove')
        git('add', '.'); git('commit', '--quiet', '-m', 'base')
        base = git('rev-parse', 'HEAD')
        (self.up / 'docs/old.md').rename(self.up / 'docs/new.md')
        (self.up / 'docs/remove.md').unlink()
        (self.up / 'docs/image.png').write_bytes(b'\x00\x01\x02')
        git('add', '.'); git('commit', '--quiet', '-m', 'changes')
        rows = changed_files(self.up, base, git('rev-parse', 'HEAD'))
        self.assertEqual({r['status'] for r in rows}, {'A', 'R', 'D'})
        renamed = next(r for r in rows if r['status'] == 'R')
        self.assertEqual(renamed['previous_path'], 'docs/old.md')
        self.assertEqual(next(r for r in rows if r['path'].endswith('.png'))['kind'], '资源')

    def test_shared_fragment_changes_propagate_through_references(self):
        fragment = self.up / 'docs/reusable-content/example.md'
        fragment.parent.mkdir()
        fragment.write_text('---\ntitle: Operation Mode\n---\nA shared paragraph')
        (self.up / 'REUSABLE_CONTENT_INDEX.md').write_text('| `fragment-id` | Operation Mode |\n')
        (self.up / 'docs/one.md').write_text('{% include "https://app.gitbook.com/s/space/~/reusable/fragment-id/" %}')
        (self.up / 'docs/two.md').write_text('[Read](one.md)\n')
        result = affected_pages(self.up, [{'path': 'docs/reusable-content/example.md', 'previous_path': None}])
        self.assertEqual(result, ['docs/one.md', 'docs/two.md'])

    def test_api_fetch_failure_is_not_a_deletion(self):
        folder = self.cn / '.upstream/generated-api'
        folder.mkdir(parents=True)
        (folder / 'manifest.json').write_text(json.dumps([
            {'source': 'docs/api.md', 'source_url': 'https://docs.n8n.io/api.md', 'source_sha256': sha(b'old')}]))
        def failed(_):
            raise RuntimeError('HTTP 403')
        result = api_changes(self.cn, read=failed)
        self.assertEqual(result[0]['status'], 'error')
        result = api_changes(self.cn, read=lambda _: b'# API\n' + b'new content ' * 20)
        self.assertEqual(result[0]['status'], 'changed')


if __name__ == '__main__':
    unittest.main()
