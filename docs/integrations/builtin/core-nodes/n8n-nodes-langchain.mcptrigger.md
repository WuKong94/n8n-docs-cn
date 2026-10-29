---
title: MCP Server Trigger 节点
description: 了解如何在 n8n 工作流中配置和使用 MCP Server Trigger 节点。
contentType:
- integration
- reference
nodeTitle: MCP Server Trigger 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MCP Server Trigger（MCP 服务器触发器）节点 <a href="#mcp-server-trigger-node" id="mcp-server-trigger-node"></a>

使用 MCP Server Trigger 让 n8n 作为[模型上下文协议（MCP）](https://modelcontextprotocol.io/introduction)服务器，向 MCP 客户端提供 n8n 工具和工作流。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [HTTP Request 凭据文档](../credentials/httprequest.md)。
{% endhint %}

## MCP Server Trigger 如何工作 <a href="#how-the-mcp-server-trigger-node-works" id="how-the-mcp-server-trigger-node-works"></a>

此节点是 MCP 客户端访问 n8n 的入口，通过公开 URL 让客户端访问工具。

传统[触发器节点](#user-content-fn-1)[^1]响应事件并将输出传给后续[已连接节点](../../../build/understand-workflows/workflow-components/connect-nodes-together.md)；MCP Server Trigger 则只连接和执行[工具](../../../build/integrate-ai/understand-ai-components/how-tools-work.md)节点。客户端可列出工具并逐个调用。

通过 [Custom n8n Workflow Tool](../cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md) 节点连接工作流，可将其提供给客户端。

{% hint style="info" %}
**支持服务器发送事件（SSE）和流式 HTTP**

节点支持基于 HTTP 长连接的[服务器发送事件（SSE）](https://modelcontextprotocol.io/docs/concepts/transports#server-sent-events-sse)，以及[流式 HTTP](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http)传输，用于客户端与服务器之间的连接。目前不支持[标准输入／输出（stdio）](https://modelcontextprotocol.io/docs/concepts/transports#standard-input%2Foutput-stdio)传输。
{% endhint %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置节点。

### MCP URL <a href="#mcp-url" id="mcp-url"></a>

节点有测试和生产两个 **MCP URLs**（MCP URL），显示在节点面板顶部。

选择 **Test URL**（测试 URL）或 **Production URL**（生产 URL）切换显示的地址。

* **Test**（测试）：工作流尚未激活时，选择 **Listen for Test Event**（监听测试事件）或 **Execute workflow**（执行工作流），会注册测试 MCP URL。调用该 URL 后，n8n 在工作流中显示数据。
* **Production**（生产）：发布工作流时注册生产 MCP URL。使用生产地址时，数据不会直接显示在工作流界面中；仍可在 **Executions**（执行记录）标签页选择相应执行，查看生产数据。

### Authentication（身份验证） <a href="#authentication" id="authentication"></a>

可要求连接 MCP URL 的客户端进行身份验证，可选：

- None（无）
- Bearer auth（Bearer 认证）
- Header auth（请求头认证）

各凭据类型的设置说明，请参阅 [HTTP Request 凭据](../credentials/httprequest.md)。

### Path（路径） <a href="#path" id="path"></a>

默认随机生成 MCP URL 路径，避免与其他 MCP Server Trigger 冲突。

也可手动指定路径并添加路由参数。例如，使用 n8n 构建 API 原型、需要一致的端点 URL 时，可采用此方式。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 MCP Server Trigger 节点集成模板](https://n8n.io/integrations/mcp-server-trigger)，或[搜索所有模板](https://n8n.io/workflows/)

### 与 Claude Desktop 集成 <a href="#integrating-with-claude-desktop" id="integrating-with-claude-desktop"></a>

可通过运行网关，在远程 SSE 端点与 stdio 连接之间转发消息，从 [Claude Desktop](https://claude.ai/download) 连接此节点。

将以下内容添加到 Claude Desktop 配置：

```json
{
  "mcpServers": {
    "n8n": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "<MCP_URL>",
        "--header",
        "Authorization: Bearer ${AUTH_TOKEN}"
      ],
      "env": {
        "AUTH_TOKEN": "<MCP_BEARER_TOKEN>"
      }
    }
  }
}
```

将 `<MCP_URL>` 和 `<MCP_BEARER_TOKEN>` 占位符替换为 MCP Server Trigger 参数和凭据中的值。

## 限制 <a href="#limitations" id="limitations"></a>

### 配置 webhook 副本 <a href="#configuring-the-mcp-server-trigger-node-with-webhook-replicas" id="configuring-the-mcp-server-trigger-node-with-webhook-replicas"></a>

节点依赖 SSE 或流式 HTTP，要求由同一个服务器实例处理持久连接。在[队列模式](../../../deploy/host-n8n/configure-n8n/scaling/enable-queue-mode.md)下，某些 [webhook 处理进程](../../../deploy/host-n8n/configure-n8n/scaling/enable-queue-mode.md#webhook-processors)配置可能因此出现问题：

* 使用队列模式且只有**一个 webhook 副本**时，节点可正常工作。
* 使用**多个 webhook 副本**时，必须将所有 `/mcp*` 请求路由到同一个专用副本。为 MCP 请求创建仅含一个 webhook 容器的独立副本集，再调整入口或负载均衡配置，将所有 `/mcp*` 流量指向该实例。

{% hint style="warning" %}
**多个 webhook 副本的注意事项**

使用多个副本却没有将所有 `/mcp*` 请求路由到同一个专用副本时，SSE 和流式 HTTP 连接会频繁中断，或无法可靠投递事件。
{% endhint %}

### Authentication 为 None 时，claude.ai 仍要求登录 <a href="#claudeai-asks-users-to-sign-in-when-authentication-is-none" id="claudeai-asks-users-to-sign-in-when-authentication-is-none"></a>

即使将 **Authentication**（身份验证）设为 **None**（无），claude.ai 自定义连接器仍要求登录 n8n。claude.ai 是目前已知唯一有此行为的客户端。

实例会为其他触发器提供 n8n 用户认证，claude.ai 因此假定该域名下的所有 MCP 端点都使用该认证。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 还提供 [MCP Client Tool](../cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp.md) 节点，用于将 n8n AI Agent 连接到外部工具。

协议、服务器和客户端的更多信息，请参阅 [MCP 文档](https://modelcontextprotocol.io/introduction)及 [MCP 规范](https://modelcontextprotocol.io/specification/)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下是 MCP Server Trigger 的常见错误和问题，以及解决或排查步骤。

### 配合反向代理运行 <a href="#running-the-mcp-server-trigger-node-with-a-reverse-proxy" id="running-the-mcp-server-trigger-node-with-a-reverse-proxy"></a>

n8n 位于 nginx 等反向代理之后时，如果未为 MCP 端点配置 SSE 或流式 HTTP，可能出现问题。

必须为该端点禁用代理缓冲。还可禁用 gzip 压缩（由 n8n 自行处理）、禁用分块传输编码，并将 `Connection` 设为空字符串，从转发请求头中移除此项。在 MCP 端点显式禁用，能避免继承 nginx 其他配置中的值。

用于处理 MCP 流量的 nginx location 配置示例如下：

```
location /mcp/ {
    proxy_http_version          1.1;
    proxy_buffering             off;
    gzip                        off;
    chunked_transfer_encoding   off;

    proxy_set_header            Connection '';

    # The rest of your proxy headers and settings
    # . . .
}
```

<a id="user-content-fn-1"></a>
[^1]: 触发器节点负责在指定条件下执行工作流，所有生产工作流至少需要一个触发器，以决定何时运行。
