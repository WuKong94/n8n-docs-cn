---
description: 一键将 AI 智能体连接到 MCP 注册表中的服务器。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MCP 服务器 <a id="mcp-servers"></a>

n8n 的节点面板提供 [Model Context Protocol（MCP，模型上下文协议）](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro)服务器注册表，可以一键连接到智能体。选择服务器并登录后，智能体即可使用其工具。

你也可以将注册表中的 MCP 服务器连接到 [n8n Assistant](../ways-of-building-workflows/n8n-assistant.md)。

## 将注册表中的服务器添加到智能体 <a id="add-a-registry-server-to-an-agent"></a>

1. 在画布上的 [AI Agent](../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/README.md) 节点中点击“Tool +”，打开工具面板；或者在[构建和管理智能体](../build-and-manage-agents/README.md#add-tools)中点击“Add Tool”。
2. 在搜索栏中搜索要连接的服务，例如 Notion 或 Linear；也可以点击“MCP Servers”部分，查看所有可用服务器。
3. 选择服务器，然后按提示登录。
4. 通过“Tools to include（包含的工具）”选择向智能体提供哪些工具：全部、指定列表，或排除指定列表后的全部工具。

从面板登录时，n8n 会自动创建 [MCP 凭据](../../integrations/builtin/credentials/mcp.md)。

## 查找可用服务器 <a id="find-available-servers"></a>

注册表中的服务器列表经常变化，请在节点面板中查看当前列表，不要依赖此处的静态清单。

有些服务器需要先在提供商侧完成设置，并提供专门的说明页。对于 Databricks Genie，请参阅 [Databricks Genie One MCP 服务器](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-mcp-registry.databricksgenie.md)，了解管理员必须添加的 OAuth 作用域及 Genie 所需的智能体设置。对于 Supabase，请按 [Supabase OAuth2 凭据设置](../../integrations/builtin/credentials/supabase.md#using-oauth2)操作，包括 Supabase MCP 服务器所需的应用权限。

如果所需服务器尚未加入注册表，可以使用 [MCP Client Tool](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp.md) 节点，通过连接 URL 和凭据手动连接任意 MCP 服务器。

## 如何选择内置工具（节点）或 MCP 服务器作为智能体工具 <a id="how-to-choose-between-a-built-in-tool-node-and-an-mcp-server-as-an-agent-tool"></a>

两者都能让智能体访问服务。内置工具提供更精细的控制：你可以固定操作和部分参数，让模型只填写你开放的字段。MCP 服务器给予智能体更大的操作空间，但相应地减少控制，并在每次调用时使用更多上下文。

| | 内置工具（n8n 集成） | MCP 服务器 |
| --- | --- | --- |
| **适用场景** | 已知智能体需要执行的操作，希望严格限定范围 | 智能体需要执行多种操作，或无法预先确定所需操作 |
| **范围** | 单个节点操作，例如发送 Slack 消息 | 通过单个连接访问服务器提供的所有工具 |
| **你配置的内容** | 需要固定的参数，例如频道、消息类型或消息文本 | 允许或排除的工具 |
| **智能体提供的内容** | 仅填写你选择[向模型开放的字段](ai-examples/use-ai-for-parameters.md) | 从允许的工具中选择调用哪个工具，并提供全部参数 |

## 相关资源 <a id="related-resources"></a>

* [集成 AI](./)
* [理解 AI 组件](understand-ai-components/README.md)
* [n8n 中的 LangChain](langchain-in-n8n.md)
* [测试和改进 AI 工作流](test-and-improve-ai-workflows/README.md)
* [AI 示例](ai-examples.md)
