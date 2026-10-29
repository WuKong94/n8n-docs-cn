---
title: MCP Client Tool（MCP 客户端工具） 节点文档
description: 了解如何在 n8n 中使用 MCP Client Tool（MCP 客户端工具） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: MCP Client Tool（MCP 客户端工具） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MCP Client Tool（MCP 客户端工具） 节点 <a href="#mcp-client-tool-node" id="mcp-client-tool-node"></a>

MCP Client Tool 节点是 [Model Context Protocol（MCP，模型上下文协议）](https://modelcontextprotocol.io/introduction)客户端，支持使用外部 MCP 服务器提供的工具。可将它连接到模型，让 n8n 智能体调用外部工具。

{% hint style="info" %}
**已在注册表中？**

如果所需服务已在 n8n 的 [MCP 服务器](../../../../build/integrate-ai/mcp-servers.md)注册表中，可直接从节点面板连接，无需添加凭据。尚未进入注册表的 MCP 服务器，可使用此节点。
{% endhint %}

## 凭据 <a id="credentials"></a>

MCP Client Tool 节点支持 [Bearer](../../credentials/httprequest.md#using-bearer-auth)、通用[请求头](../../credentials/httprequest.md#using-header-auth)、多个请求头及 [OAuth2](../../credentials/mcp.md#using-oauth2) 身份验证方式。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置节点。

* **SSE Endpoint**（SSE 端点）：要连接的 MCP 服务器的 SSE 端点。
* **Authentication**（身份验证）：连接 MCP 服务器时使用的身份验证方式。MCP 工具支持 [Bearer](../../credentials/httprequest.md#using-bearer-auth)、通用[请求头](../../credentials/httprequest.md#using-header-auth)、多个请求头及 [OAuth2](../../credentials/mcp.md#using-oauth2)。选择 **None**（无），尝试不经身份验证连接。
    * **Multiple Headers Auth**（多个请求头身份验证）：MCP 服务器需要多个请求头时使用，例如 API 密钥和用户名。在凭据中将每个请求头添加为一对 **Name**（名称）和 **Value**（值），可按需添加任意数量。
* **Tools to Include**（要包含的工具）：选择向 AI Agent 提供哪些工具：
    * **All**（全部）：提供 MCP 服务器的所有工具。
    * **Selected**（选定）：显示 **Tools to Include**（要包含的工具）参数，供你选择向 AI Agent 提供的工具。
    * **All Except**（排除选定）：显示 **Tools to Exclude**（要排除的工具）参数，供你选择不向 AI Agent 提供的工具。AI Agent 可访问 MCP 服务器中所有未选中的工具。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 MCP Client Tool（MCP 客户端工具） 集成模板](https://n8n.io/integrations/mcp-client-tool)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 也提供 [MCP Server Trigger](../../core-nodes/n8n-nodes-langchain.mcptrigger.md) 节点，可将 n8n 工具暴露给外部 AI 智能体。

协议、服务器和客户端的更多详情，请参阅 [MCP 文档](https://modelcontextprotocol.io/introduction)和 [MCP 规范](https://modelcontextprotocol.io/specification/)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/tools-link.md" %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

