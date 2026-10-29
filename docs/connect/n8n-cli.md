---
description: n8n CLI 是一个轻量级客户端，通过公共 API 以编程方式与 n8n 交互。
contentType: guide
status: beta
nodeTitle: n8n CLI
originalFilePath: api/n8n-cli/index.md
originalUrl: https://docs.n8n.io/api/n8n-cli
url: https://docs.n8n.io/connect/
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# n8n CLI 入门 <a href="#getting-started-with-n8n-cli" id="getting-started-with-n8n-cli"></a>

**n8n CLI** 是轻量级命令行客户端，通过 [n8n API](n8n-api/README.md) 与正在运行的 n8n 实例通信。它可在任何能通过网络访问实例的机器上运行，并使用 API 密钥进行身份验证。

使用此 API CLI 可以：

- 列出和查看工作流。
- 从 JSON 创建工作流。
- 查看最近的执行。
- 创建凭据。
- 管理项目。

所有操作均遵循用户权限和 API 密钥的作用域。

## n8n CLI 与服务器 CLI <a href="#n8n-cli-versus-server-cli" id="n8n-cli-versus-server-cli"></a>

如需管理 n8n 实例（备份、许可证管理、紧急重置），请参阅[服务器 CLI](../deploy/host-n8n/configure-n8n/use-the-command-line.md)。它是内置工具，在与 n8n 相同的机器上运行。

| 对比项 | n8n CLI | 服务器 CLI |
|--------|---------|-----------|
| **运行位置** | 任何能通过网络访问实例的机器 | 与 n8n 相同的机器 |
| **身份验证** | API 密钥 | 直接访问数据库 |
| **是否要求 n8n 正在运行** | 是 | 否（大多数操作不要求） |
| **适用场景** | 开发者、集成、AI 智能体 | 实例运维、备份、紧急处理 |
| **权限** | 遵循用户角色和 API 密钥作用域 | 绕过访问控制 |

## 安装 n8n-cli <a href="#install-n8n-cli" id="install-n8n-cli"></a>

```bash
# Use directly with npx (zero install) <a href="#use-directly-with-npx-zero-install" id="use-directly-with-npx-zero-install"></a>
npx @n8n/cli workflow list

# Or install globally <a href="#or-install-globally" id="or-install-globally"></a>
npm install -g @n8n/cli
```

## 连接到实例 <a href="#connect-to-your-instance" id="connect-to-your-instance"></a>

```bash
n8n-cli config set-url https://your-instance.n8n.cloud
n8n-cli config set-api-key YOUR_API_KEY
n8n-cli config show
```

* 配置保存在 `~/.n8n-cli/config.json`，文件权限限制为 `0600`。
* 在 **n8n > Settings > n8n API**（n8n > 设置 > n8n API）中获取 API 密钥。

也可以不使用配置文件，改为使用环境变量：

```bash
export N8N_URL=https://your-instance.n8n.cloud
export N8N_API_KEY=your_api_key
```

## 命令行选项 <a href="#inline-flags" id="inline-flags"></a>

``` bash
n8n-cli --url=https://my-n8n.app.n8n.cloud --api-key=n8n_api_xxxxx workflow list
```

### 配置解析顺序 <a href="#resolution-order" id="resolution-order"></a>

1. 命令行选项（`--url`、`--api-key`）。
2. 环境变量（`N8N_URL`、`N8N_API_KEY`）。
3. 配置文件（`~/.n8n-cli/config.json`）。

## 命令 <a href="#commands" id="commands"></a>

每个命令都支持使用 `--help` 查看详细用法。

| 主题 | 命令 |
|---|---|
| `workflow` | `list`, `get`, `create`, `update`, `delete`, `activate`, `deactivate`, `tags`, `transfer` |
| `execution` | `list`, `get`, `retry`, `stop`, `delete` |
| `credential` | `list`, `get`, `schema`, `create`, `delete`, `transfer` |
| `project` | `list`, `get`, `create`, `update`, `delete`, `members`, `add-member`, `remove-member` |
| `tag` | `list`, `create`, `update`, `delete` |
| `variable` | `list`, `create`, `update`, `delete` |
| `data-table` | `list`, `get`, `create`, `delete`, `rows`, `add-rows`, `update-rows`, `upsert-rows`, `delete-rows` |
| `user` | `list`, `get` |
| `config` | `set-url`, `set-api-key`, `show` |
| `source-control` | `pull` |
| `package (preview)` | `export`, `import` |
| `skill` | `install` |
| `audit` | 顶层命令 |
| `login` / `logout` | 顶层命令 |


## 输出格式 <a href="#output-formats" id="output-formats"></a>
所有命令均可通过 `--format` 选择三种输出格式：

| 格式 | 选项 | 适用场景 |
|---|---|---|
| 表格 | -`-format=table`（默认） | 便于阅读的终端输出 |
| JSON | `--format=json` | 通过管道传给 jq，或供程序使用 |
| 仅 ID | `--format=id-only` | 通过管道传给 xargs，或用于脚本 |

### 示例 <a href="#examples" id="examples"></a>
* 便于阅读的表格

   ``` bash
   n8n-cli workflow list
   ```

* 供脚本使用的 JSON

   ``` bash
   n8n-cli workflow list --format=json | jq '.[] | select(.active) | .id'
   ```

* 将 ID 通过管道传给其他命令

   ``` bash
   n8n-cli workflow list --format=id-only | xargs -I{} n8n-cli workflow deactivate {}
   ```

## 在 Claude Code 中作为技能使用 <a href="#use-as-skill-with-claude-code" id="use-as-skill-with-claude-code"></a>

安装技能，让 Claude 知道如何使用 n8n-cli：

```bash
n8n-cli skill install --global
```

然后在 Claude Code 中输入 `/n8n-cli` 加载技能。Claude 随后可代你创建、更新和管理工作流，无需使用 MCP。

## 示例 <a href="#examples" id="examples"></a>

### 列出和查看工作流 <a href="#list-and-inspect-workflows" id="list-and-inspect-workflows"></a>

```bash
n8n-cli workflow list
n8n-cli workflow get <id>
```
    
### 从 JSON 创建工作流 <a href="#create-a-workflow-from-json" id="create-a-workflow-from-json"></a>
    
```bash
cat workflow.json | n8n-cli workflow create --stdin
```
    
### 查看最近的执行 <a href="#check-recent-executions" id="check-recent-executions"></a>

```bash
n8n-cli execution list --status=error --limit=10
```
    
### 创建凭据 <a href="#create-a-credential" id="create-a-credential"></a>
    
```bash
n8n-cli credential schema gmailOAuth2  # see required fields first
n8n-cli credential create --type=gmailOAuth2 --name='My Gmail' --file=cred.json
```
    
### 管理项目 <a href="#manage-projects" id="manage-projects"></a>
    
```bash
n8n-cli project create --name="My Project"
n8n-cli workflow transfer <id> --project=<projectId>
```

### 导出和导入软件包 <a href="#export-and-import-packages" id="export-and-import-packages"></a>

{% hint style="info" %}
**预览状态**

`package` 命令处于预览阶段，未来版本可能更改。
{% endhint %}

```bash
n8n-cli package export --workflow-id=<workflow-id> --output=export.n8np
n8n-cli package export --project-id=<project-id> --output=project.n8np
n8n-cli package import --file=export.n8np --workflow-conflict-policy=fail
n8n-cli package import --file=export.n8np --project-id=<project-id> --workflow-conflict-policy=skip
n8n-cli package import --file=export.n8np --project-id=<project-id> --data-table-schema-conflict-policy=overwrite-non-destructive
```

软件包的组成请参阅 [n8n 软件包](../build/manage-workflows/n8n-packages/README.md)，全部可用选项请参阅[导入软件包](../build/manage-workflows/n8n-packages/import-a-package.md)。

## 相关资源 <a id="related-resources"></a>

* [连接](./)
* [n8n API](n8n-api/README.md)
* [连接 n8n MCP 服务器](connect-to-n8n-mcp-server.md)
* [连接 n8n 文档 MCP 服务器](connect-to-n8n-docs-mcp-server.md)
* [创建节点](create-nodes/README.md)