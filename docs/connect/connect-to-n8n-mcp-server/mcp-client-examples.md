---
title: MCP 客户端连接示例
description: Lovable、Claude Desktop、Claude Code、Codex、Gemini CLI、Cursor、VS Code、Windsurf
  和 Google ADK 智能体可直接复制使用的连接命令与配置。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MCP 客户端连接示例 <a href="#mcp-client-connection-examples" id="mcp-client-connection-examples"></a>

以下示例提供将特定客户端连接到 n8n MCP 服务器的准确命令和配置。使用前，请先在实例上[启用 MCP 访问](../connect-to-n8n-mcp-server.md#enabling-mcp-access)并选择身份验证方式，参阅[连接 MCP 客户端](../connect-to-n8n-mcp-server.md#setting-up-mcp-authentication)。

{% hint style="info" %}
自 n8n 2.33.0 起提供的 **Connect a client**（连接客户端）对话框，支持一键连接 Claude.ai、Cursor 和 VS Code，也为 Claude Code、Codex、Gemini CLI、ChatGPT 和 Windsurf 提供交互式设置步骤。如何打开对话框并选择客户端，请参阅[使用 OAuth（推荐）](../connect-to-n8n-mcp-server.md#using-oauth2)。

如果 n8n 未为所选客户端显示交互式步骤，或需要查阅、手动配置，可以使用以下示例。
{% endhint %}

以下示例均使用 `https://`。如果实例通过普通 HTTP 提供服务，例如本地安装地址为 `http://localhost:5678`，请改用 `http://`。从 n8n 复制完整的 **Server URL**（服务器 URL），即可获得正确前缀。

## 将 Lovable 连接到 n8n MCP 服务器 <a href="#connecting-lovable-to-n8n-mcp-server" id="connecting-lovable-to-n8n-mcp-server"></a>

1. 在 Lovable 中配置 MCP 服务器（OAuth）。
   * 前往工作区的 **Settings > Integrations**（设置 > 集成）。
   * 在 **MCP Servers**（MCP 服务器）部分找到 **n8n**，点击 **Connect**（连接）。
   * 输入 n8n 服务器 URL，即 **Connect a client**（连接客户端）对话框中的 **Server URL**（服务器 URL）值。
   * 保存连接。成功后，n8n 会重定向到授权页面，请批准 Lovable 的访问。
2. 验证连接。
   * 连接后，Lovable 可以查询已启用 MCP 访问的工作流。
   * **示例：**让 Lovable 构建一个列出用户并允许删除用户的工作流界面。

## 将 Claude Desktop 连接到 n8n MCP 服务器 <a href="#connecting-claude-desktop-to-n8n-mcp-server" id="connecting-claude-desktop-to-n8n-mcp-server"></a>

**使用 OAuth（推荐）**

1. 在 Claude Desktop 中，前往 **Settings**（设置）> **Connectors**（连接器）。
2. 点击 **Add custom connector**（添加自定义连接器）。
3. 填写以下信息：
   * **Name**（名称）：n8n MCP
   * **Remote MCP Server URL**（远程 MCP 服务器 URL）：**Connect a client**（连接客户端）对话框中显示的 **Server URL**（服务器 URL）值。它以 `/mcp-server/http` 结尾，形如 `https://<your-n8n-domain>/mcp-server/http`。这与 n8n 编辑器地址不同，不要粘贴浏览器地址栏中的 URL。
4. 保存连接器。
5. 按提示批准 Claude Desktop 的访问。

**使用 API 密钥**

将以下条目添加到 `claude_desktop_config.json` 文件：

```json
"mcpServers": {
  "n8n-mcp": {
    "command": "npx",
    "args": [
    "-y",
    "supergateway",
    "--streamableHttp",
    "https://<your-n8n-domain>/mcp-server/http",
    "--header",
    "Authorization:Bearer <YOUR_N8N_MCP_TOKEN>"
    ]
  }
}
```

请替换以下值：

* `<your-n8n-domain>`：n8n 域名，不包含 `https://` 前缀。在 n8n Cloud 中为 `your-instance.app.n8n.cloud`；自托管时，为 n8n 编辑器使用的域名，例如 `n8n.example.com`。完整服务器 URL 可在 n8n 的 **Settings**（设置）> **Instance-level MCP > Connect a client > Server URL**（实例级 MCP > 连接客户端 > 服务器 URL）中找到。

## 将 Claude Code 连接到 n8n MCP 服务器 <a href="#connecting-claude-code-to-n8n-mcp-server" id="connecting-claude-code-to-n8n-mcp-server"></a>

**方式一：使用 OAuth 进行身份验证（推荐）**

使用以下 CLI 命令：

```bash
claude mcp add --transport http n8n https://<your-n8n-domain>/mcp-server/http
```

或者将以下条目添加到 `claude.json` 文件：

```json
{
    "mcpServers": {
        "n8n": {
            "type": "http",
            "url": "https://<your-n8n-domain>/mcp-server/http"
        }
    }
}
```

请替换以下值：

* `<your-n8n-domain>`：n8n 域名，不包含 `https://` 前缀。在 n8n Cloud 中为 `your-instance.app.n8n.cloud`；自托管时，为 n8n 编辑器使用的域名，例如 `n8n.example.com`。完整服务器 URL 可在 n8n 的 **Settings**（设置）> **Instance-level MCP > Connect a client > Server URL**（实例级 MCP > 连接客户端 > 服务器 URL）中找到。

在 Claude Code 中运行 `/mcp`，选择 **n8n**，完成 OAuth 授权。

**方式二：使用 API 密钥进行身份验证**

使用以下 CLI 命令：

```bash
claude mcp add --transport http n8n-mcp https://<your-n8n-domain>/mcp-server/http \
  --header "Authorization: Bearer <YOUR_N8N_MCP_TOKEN>"
```

或者将以下条目添加到 `claude.json` 文件：

```json
{
    "mcpServers": {
        "n8n-mcp": {
            "type": "http",
            "url": "https://<your-n8n-domain>/mcp-server/http",
            "headers": {
                "Authorization": "Bearer <YOUR_N8N_MCP_TOKEN>"
            }
        }
    }
}
```

请替换以下值：

* `<your-n8n-domain>`：n8n 域名，不包含 `https://` 前缀。在 n8n Cloud 中为 `your-instance.app.n8n.cloud`；自托管时，为 n8n 编辑器使用的域名，例如 `n8n.example.com`。完整服务器 URL 可在 n8n 的 **Settings**（设置）> **Instance-level MCP > Connect a client > Server URL**（实例级 MCP > 连接客户端 > 服务器 URL）中找到。
* `<YOUR_N8N_MCP_TOKEN>`：生成的令牌。

## 将 Codex CLI 连接到 n8n MCP 服务器 <a href="#connecting-codex-cli-to-n8n-mcp-server" id="connecting-codex-cli-to-n8n-mcp-server"></a>

**方式一：使用 OAuth 进行身份验证（推荐）**

使用以下 CLI 命令：

```bash
codex mcp add n8n --url "https://<your-n8n-domain>/mcp-server/http"
```

或者将以下条目添加到 `~/.codex/config.toml` 文件：

```toml
[features]
experimental_use_rmcp_client = true

[mcp_servers.n8n]
url = "https://<your-n8n-domain>/mcp-server/http"
```

{% hint style="info" %}
`[features]` 块用于启用 Codex 的 HTTP MCP 客户端。较旧的 Codex 版本需要此配置，较新版本会忽略它。
{% endhint %}

请替换以下值：

* `<your-n8n-domain>`：n8n 域名，不包含 `https://` 前缀。在 n8n Cloud 中为 `your-instance.app.n8n.cloud`；自托管时，为 n8n 编辑器使用的域名，例如 `n8n.example.com`。完整服务器 URL 可在 n8n 的 **Settings**（设置）> **Instance-level MCP > Connect a client > Server URL**（实例级 MCP > 连接客户端 > 服务器 URL）中找到。

运行 `codex mcp login n8n` 完成 OAuth 授权。

**方式二：使用 API 密钥进行身份验证**

将以下条目添加到 `~/.codex/config.toml` 文件：

```toml
[features]
experimental_use_rmcp_client = true

[mcp_servers.n8n-mcp]
url = "https://<your-n8n-domain>/mcp-server/http"
http_headers = { "authorization" = "Bearer <YOUR_N8N_MCP_TOKEN>" }
```

请替换以下值：

* `<your-n8n-domain>`：n8n 域名，不包含 `https://` 前缀。在 n8n Cloud 中为 `your-instance.app.n8n.cloud`；自托管时，为 n8n 编辑器使用的域名，例如 `n8n.example.com`。完整服务器 URL 可在 n8n 的 **Settings**（设置）> **Instance-level MCP > Connect a client > Server URL**（实例级 MCP > 连接客户端 > 服务器 URL）中找到。
* `<YOUR_N8N_MCP_TOKEN>`：生成的令牌。

## 将 Gemini CLI 连接到 n8n MCP 服务器 <a href="#connecting-gemini-cli-to-n8n-mcp-server" id="connecting-gemini-cli-to-n8n-mcp-server"></a>

使用以下 CLI 命令：

```bash
gemini mcp add --transport http n8n https://<your-n8n-domain>/mcp-server/http
```

或者将以下条目添加到 `~/.gemini/settings.json` 文件：

```json
{
    "mcpServers": {
        "n8n": {
            "httpUrl": "https://<your-n8n-domain>/mcp-server/http"
        }
    }
}
```

请替换以下值：

* `<your-n8n-domain>`：n8n 域名，不包含 `https://` 前缀。在 n8n Cloud 中为 `your-instance.app.n8n.cloud`；自托管时，为 n8n 编辑器使用的域名，例如 `n8n.example.com`。完整服务器 URL 可在 n8n 的 **Settings**（设置）> **Instance-level MCP > Connect a client > Server URL**（实例级 MCP > 连接客户端 > 服务器 URL）中找到。

在 Gemini CLI 中运行 `/mcp`，选择 **n8n**，完成 OAuth 授权。

## 将 Cursor 连接到 n8n MCP 服务器 <a href="#connecting-cursor-to-n8n-mcp-server" id="connecting-cursor-to-n8n-mcp-server"></a>

在 **Connect a client**（连接客户端）对话框中，从 **Your client**（你的客户端）选择 **Cursor**，再选择 **One-click setup**（一键设置），即可打开 Cursor 并自动添加 n8n 服务器。Cursor 重定向回 n8n 时，请批准访问。

或者将以下条目添加到 `~/.cursor/mcp.json` 文件（或项目中的 `.cursor/mcp.json`）：

```json
{
  "mcpServers": {
    "n8n": {
      "type": "streamable-http",
      "url": "https://<your-n8n-domain>/mcp-server/http"
    }
  }
}
```

请替换以下值：

* `<your-n8n-domain>`：n8n 域名，不包含 `https://` 前缀。在 n8n Cloud 中为 `your-instance.app.n8n.cloud`；自托管时，为 n8n 编辑器使用的域名，例如 `n8n.example.com`。完整服务器 URL 可在 n8n 的 **Settings**（设置）> **Instance-level MCP > Connect a client > Server URL**（实例级 MCP > 连接客户端 > 服务器 URL）中找到。

## 将 VS Code 连接到 n8n MCP 服务器 <a href="#connecting-vs-code-to-n8n-mcp-server" id="connecting-vs-code-to-n8n-mcp-server"></a>

在 **Connect a client**（连接客户端）对话框中，从 **Your client**（你的客户端）选择 **VS Code**，再选择 **One-click setup**（一键设置），即可打开 VS Code 并自动添加 n8n 服务器。VS Code 重定向回 n8n 时，请批准访问。

或者将以下条目添加到工作区的 `.vscode/mcp.json` 文件：

```json
{
  "servers": {
    "n8n": {
      "type": "http",
      "url": "https://<your-n8n-domain>/mcp-server/http"
    }
  }
}
```

请替换以下值：

* `<your-n8n-domain>`：n8n 域名，不包含 `https://` 前缀。在 n8n Cloud 中为 `your-instance.app.n8n.cloud`；自托管时，为 n8n 编辑器使用的域名，例如 `n8n.example.com`。完整服务器 URL 可在 n8n 的 **Settings**（设置）> **Instance-level MCP > Connect a client > Server URL**（实例级 MCP > 连接客户端 > 服务器 URL）中找到。

## 将 Windsurf 连接到 n8n MCP 服务器 <a href="#connecting-windsurf-to-n8n-mcp-server" id="connecting-windsurf-to-n8n-mcp-server"></a>

将以下条目添加到 `~/.codeium/windsurf/mcp_config.json` 文件：

```json
{
  "mcpServers": {
    "n8n": {
      "serverUrl": "https://<your-n8n-domain>/mcp-server/http"
    }
  }
}
```

请替换以下值：

* `<your-n8n-domain>`：n8n 域名，不包含 `https://` 前缀。在 n8n Cloud 中为 `your-instance.app.n8n.cloud`；自托管时，为 n8n 编辑器使用的域名，例如 `n8n.example.com`。完整服务器 URL 可在 n8n 的 **Settings**（设置）> **Instance-level MCP > Connect a client > Server URL**（实例级 MCP > 连接客户端 > 服务器 URL）中找到。

Windsurf 首次尝试连接并重定向到 n8n 时，请批准访问。

## 将 Google ADK 智能体连接到 n8n MCP 服务器 <a href="#connecting-google-adk-agent-to-n8n-mcp-server" id="connecting-google-adk-agent-to-n8n-mcp-server"></a>

以下示例代码创建一个连接到远程 n8n MCP 服务器的智能体：

```python
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams

N8N_INSTANCE_URL = "https://n8n.example.com"
N8N_MCP_TOKEN = "YOUR_N8N_MCP_TOKEN"

root_agent = Agent(
    model="gemini-2.5-pro",
    name="n8n_agent",
    instruction="Help users manage and execute workflows in n8n",
    tools=[
        McpToolset(
            connection_params=StreamableHTTPServerParams(
                url=f"{N8N_INSTANCE_URL}/mcp-server/http",
                headers={
                    "Authorization": f"Bearer {N8N_MCP_TOKEN}",
                },
            ),
        )
    ],
)
```

请替换以下值：

* `N8N_INSTANCE_URL`：n8n 实例的基础 URL。在 n8n Cloud 中为 `https://your-instance.app.n8n.cloud`；自托管时为自己的 URL，例如 `https://n8n.example.com`。完整服务器 URL 可在 n8n 的 **Settings**（设置）> **Instance-level MCP > Connect a client > Server URL**（实例级 MCP > 连接客户端 > 服务器 URL）中找到。
* `YOUR_N8N_MCP_TOKEN`：生成的访问令牌。

更多详情请参阅[将 ADK 智能体连接到 n8n](https://google.github.io/adk-docs/tools/third-party/n8n/)。

## 故障排查 <a id="troubleshooting"></a>

如果客户端无法按上述步骤连接，请参阅 MCP 服务器主页面中的[故障排查](../connect-to-n8n-mcp-server.md#troubleshooting)。

## 相关资源 <a id="related-resources"></a>

* [连接 n8n MCP 服务器](../connect-to-n8n-mcp-server.md)
* [MCP 服务器工具参考](mcp-server-tools-reference.md)
