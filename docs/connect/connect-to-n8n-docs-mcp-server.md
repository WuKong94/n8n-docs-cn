---
description: >-
  将 AI 工具连接到 n8n 文档的模型上下文协议（MCP）服务器，以搜索文档和更广泛的知识库并回答问题。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 连接 n8n 文档 MCP 服务器 <a id="connect-to-the-n8n-docs-mcp-server"></a>

n8n 文档提供两个[模型上下文协议（MCP）](https://modelcontextprotocol.io/)服务器。将 AI 工具连接到服务器后，它就可以在你工作时搜索 n8n 知识并回答问题。

两个服务器使用不同的信息来源，请根据希望 AI 工具如何回答问题来选择：

| 服务器 | 信息来源 | 适合用途 |
|--------|---------|----------|
| **GitBook 文档服务器** | 仅包含已发布的 n8n 文档 | 搜索和阅读具体文档页面，以文档作为唯一权威来源。 |
| **Kapa.ai 服务器** | 文档、[社区论坛](https://community.n8n.io/)和 [n8n 博客](https://blog.n8n.io/) | 文档之外更广泛的问题，例如故障排查和实际案例。文档站的 AI Assistant 也使用同一引擎。 |

你可以同时连接两者。希望答案以文档为依据时，使用 GitBook 服务器；希望从 n8n 更广泛的知识库中获取答案时，使用 Kapa.ai 服务器。

两个服务器均使用 HTTP 传输，因此 AI 工具需要支持通过 HTTP 连接远程 MCP 服务器。两者都不支持 stdio 或 SSE。

## MCP 服务器地址 <a id="mcp-server-urls"></a>

使用所需服务器对应的端点：

| 服务器 | URL |
|--------|-----|
| GitBook 文档服务器 | `https://docs.n8n.io/~gitbook/mcp` |
| Kapa.ai 服务器 | `https://n8n.mcp.kapa.ai` |

## 连接 AI 工具 <a id="connect-your-ai-tool"></a>

不同工具的操作步骤有所不同，但都需要上面的服务器地址。下面的示例会配置两个服务器。如果只需要连接一个，保留所需条目并删除另一个即可。

{% hint style="info" %}
Kapa.ai 服务器需要身份验证。首次连接或首次使用时，AI 工具会打开基于浏览器的登录流程。请按照提示批准连接。
{% endhint %}

### Claude Code <a id="claude-code"></a>

在终端中运行以下命令：

```bash
claude mcp add --transport http n8n-docs https://docs.n8n.io/~gitbook/mcp
claude mcp add --transport http n8n-kapa https://n8n.mcp.kapa.ai
```

### Cursor <a id="cursor"></a>

将服务器添加到 `mcp.json` 文件：

```json
{
	"mcpServers": {
		"n8n-docs": {
			"url": "https://docs.n8n.io/~gitbook/mcp"
		},
		"n8n-kapa": {
			"url": "https://n8n.mcp.kapa.ai"
		}
	}
}
```

### VS Code <a id="vs-code"></a>

将服务器添加到 `mcp.json` 文件：

```json
{
	"servers": {
		"n8n-docs": {
			"type": "http",
			"url": "https://docs.n8n.io/~gitbook/mcp"
		},
		"n8n-kapa": {
			"type": "http",
			"url": "https://n8n.mcp.kapa.ai"
		}
	}
}
```

### 其他工具 <a id="other-tools"></a>

对于其他 MCP 客户端，请在其 MCP 设置中添加远程（HTTP）服务器，并输入服务器地址：

```
https://docs.n8n.io/~gitbook/mcp
https://n8n.mcp.kapa.ai
```

连接后，工具即可在你工作时搜索 n8n 知识。

{% hint style="info" %}
具体配置步骤和文件位置因工具及版本而异。如何添加远程 MCP 服务器，请参阅对应工具的文档。有关 Kapa.ai 服务器的更多信息，请参阅 [Kapa.ai MCP 文档](https://docs.kapa.ai/overview/build-with-ai)。
{% endhint %}

## 相关资源 <a id="related-resources"></a>

* [连接](./)
* [n8n API](n8n-api/README.md)
* [n8n CLI](n8n-cli.md)
* [连接 n8n MCP 服务器](connect-to-n8n-mcp-server.md)
* [创建节点](create-nodes/README.md)
