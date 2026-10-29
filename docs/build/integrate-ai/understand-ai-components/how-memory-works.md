---
title: AI 中的记忆是什么？
description: 了解 AI 中的记忆，以及 n8n 记忆功能的特点。
contentType: explanation
nodeTitle: 记忆的工作原理
originalFilePath: advanced-ai/examples/understand-memory.md
originalUrl: https://docs.n8n.io/advanced-ai/examples/understand-memory
url: https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-memory-works
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# AI 中的记忆是什么？ <a href="#whats-memory-in-ai" id="whats-memory-in-ai"></a>

记忆是 AI 聊天服务的重要组成部分。记忆[^1]保留先前消息的历史，让你可以与 AI 持续对话，而不是每次交互都重新开始。

## n8n 中的 AI 记忆 <a href="#ai-memory-in-n8n" id="ai-memory-in-n8n"></a>

要为 AI 工作流添加记忆，可以使用：

* [Simple Memory](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/README.md)：保存当前会话的聊天历史，长度可以自定义。这是最容易入门的方式。
* n8n 提供了对应节点的记忆服务，包括：
	* [Motorhead](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead.md)
	* [Redis Chat Memory](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat.md)
	* [Postgres Chat Memory](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat.md)
	* [Xata](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryxata.md)
	* [Zep](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep.md)

如果需要在工作流中进行高级 AI 记忆管理，请使用 [Chat Memory Manager](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager.md) 节点。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-sub-nodes/chat-memory-manager-purpose.md" %}

[^1]: 在 AI 场景中，记忆让 AI 工具能够在多次交互之间保留消息上下文。例如，你可以与 AI 智能体持续对话，而无需在每条消息中重新提供上下文。在 n8n 中，AI 智能体节点可以使用记忆，AI 链则不能。

## 相关资源 <a id="related-resources"></a>

* [理解 AI 组件](./)
* [链的作用](what-chains-do.md)
* [智能体的作用](what-agents-do.md)
* [工具的工作原理](how-tools-work.md)
* [使用向量存储和搜索数据](store-and-search-data-with-vectors.md)
* [检索相关上下文](retrieve-relevant-context.md)
* [智能体与链的对比](agents-vs-chains.md)
