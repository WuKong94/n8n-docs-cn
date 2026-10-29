---
title: AI Agent（AI 智能体） 节点文档
description: 了解如何在 n8n 中使用 AI Agent（AI 智能体） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: critical
nodeTitle: n8n-nodes-langchain.agent
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# AI Agent（AI 智能体） 节点 <a href="#ai-agent-node" id="ai-agent-node"></a>

AI Agent 节点支持在 n8n 中构建 AI 智能体。连接聊天模型及一个或多个工具后，智能体会决定调用哪些工具来完成任务。

[AI 智能体](#user-content-fn-1)[^1]是自主系统，可接收数据、作出合理决策，并在所处环境中采取行动以实现特定目标。环境包含智能体自身以外所有可访问的内容。此智能体通过外部工具[^2]和 API 执行操作、获取信息，能够理解不同工具的能力，并根据任务决定使用哪种工具。

{% hint style="info" %}
**连接工具**

必须为 AI Agent 节点连接至少一个工具[子节点](../../sub-nodes/README.md)。
{% endhint %}

{% hint style="warning" %}
**功能可用性**

AI Agent 节点的智能体类型设置从 n8n 1.82.0 起弃用。现在所有 AI Agent 节点都作为 `Tools Agent` 工作，这是此前推荐且最常使用的设置。使用旧版 AI Agent 节点并设为 `Tools Agent` 的工作流或模板，仍会按预期运行。

包含智能体类型设置的节点版本 v1 **将在 n8n 3.0 中移除**。如果使用 AI Agent 节点 v1，请更新至最新版本。对于 SQL Agent 等场景，请改用较新的 Agent 节点，并连接 Postgres/MySQL 工具子节点。
{% endhint %}


## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 AI Agent（AI 智能体）集成模板](https://n8n.io/integrations/agent)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 智能体文档](https://docs.langchain.com/oss/javascript/langchain/agents)。

初次接触 AI 智能体？请阅读 [n8n 博客中的 AI 智能体介绍](https://blog.n8n.io/ai-agents/)。

一键将注册表中的 MCP 服务器作为工具连接的方法，请参阅 [MCP 服务器](../../../../../build/integrate-ai/mcp-servers.md)。

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误和问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。

<a id="user-content-fn-1"></a>
[^1]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大型语言模型（LLM）理解用户输入，并根据可用的信息和资源，决定如何最好地处理请求。
[^2]: 在 AI 场景中，工具是附加资源，AI 可在响应请求时调用它获取特定信息或功能。AI 模型可以通过工具与外部系统交互，或完成具体、专门的任务。
