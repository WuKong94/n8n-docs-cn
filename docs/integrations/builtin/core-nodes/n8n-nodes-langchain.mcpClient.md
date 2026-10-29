---
title: MCP Client 节点
description: 了解如何在 n8n 工作流中配置和使用 MCP Client 节点。
contentType:
- integration
- reference
nodeTitle: MCP Client 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-langchain.mcpClient.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcpClient
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcpClient
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MCP Client（MCP 客户端）节点 <a href="#mcp-client-node" id="mcp-client-node"></a>

MCP Client 是[模型上下文协议（MCP）](https://modelcontextprotocol.io/introduction)客户端，用于调用外部 MCP 服务器提供的工具。

可将 MCP 工具作为工作流中的普通步骤使用。

若要将 MCP 工具作为 AI Agent 的工具，请改用 [MCP Client Tool 节点](../cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp.md)。

{% hint style="info" %}
**凭据**

MCP Client 支持 [Bearer](../credentials/httprequest.md#using-bearer-auth)、通用[请求头](../credentials/httprequest.md#using-header-auth)、多请求头和 [OAuth2](../credentials/mcp.md#using-oauth2) 身份验证。
{% endhint %}


## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置节点。

* **Server Transport**（服务器传输方式）：目标 MCP 端点使用的传输协议。
* **MCP Endpoint URL**（MCP 端点 URL）：外部 MCP 服务器的 URL，例如 `https://mcp.notion.com/mcp`。
* **Authentication**（身份验证）：连接服务器的认证方式，支持 [bearer](../credentials/httprequest.md#using-bearer-auth)、通用[请求头](../credentials/httprequest.md#using-header-auth)、多请求头及 [OAuth2](../credentials/mcp.md#using-oauth2)。选择 **None**（无）可尝试无认证连接。
    * **Multiple Headers Auth**（多请求头认证）：服务器要求多个请求头，例如 API 密钥和用户名时使用。在凭据中以 **Name**（名称）/**Value**（值）对添加各请求头，数量不限。
* **Tool**（工具）：选择要调用的工具，列表会从外部 MCP 服务器自动获取。
* **Input Mode**（输入模式）：
    * **Manual**（手动）：逐个指定工具参数。
    * **JSON**：以 JSON 对象指定参数，适用于含嵌套参数的工具。

## 选项 <a href="#options" id="options"></a>

* **Convert to Binary**（转换为二进制）：选择是否将图片和音频转换为二进制数据。关闭时，以 base64 编码字符串返回。
* **Timeout**（超时）：等待工具调用完成的时长，单位为毫秒。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 MCP Client 节点集成模板](https://n8n.io/integrations/mcp-client)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

要在 AI Agent 中使用 MCP 工具，请使用 [MCP Client Tool 节点](../cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp.md)。

n8n 还提供 [MCP Server Trigger](n8n-nodes-langchain.mcptrigger.md) 节点，用于向外部 AI Agent 提供 n8n 工具。

协议、服务器和客户端的更多信息，请参阅 [MCP 文档](https://modelcontextprotocol.io/introduction)及 [MCP 规范](https://modelcontextprotocol.io/specification/)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/tools-link.md" %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

