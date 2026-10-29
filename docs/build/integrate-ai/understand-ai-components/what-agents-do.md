---
title: 什么是 AI 智能体？
description: 了解 AI 中的智能体，以及 n8n 如何提供智能体。
contentType: explanation
nodeTitle: 智能体的作用
originalFilePath: advanced-ai/examples/understand-agents.md
originalUrl: https://docs.n8n.io/advanced-ai/examples/understand-agents
url: https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-agents-do
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 什么是 AI 智能体？ <a href="#whats-an-agent-in-ai" id="whats-an-agent-in-ai"></a>

可以将智能体[^1]理解为能够做决策的[链](what-chains-do.md)。链按照预定顺序调用不同的 AI 组件，而智能体会通过语言模型判断应采取哪些行动。

智能体是 AI 中负责决策的部分，可以与其他智能体和工具[^2]交互。向智能体发送查询时，它会尝试选择最合适的工具来回答。智能体会根据具体查询，以及用于配置其行为的提示词调整行动。

## n8n 中的智能体 <a href="#agents-in-n8n" id="agents-in-n8n"></a>

n8n 提供一个 Agent 节点，可根据所选设置充当不同类型的智能体。可用智能体类型的详情请参阅 [Agent 节点文档](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/README.md)。

执行包含智能体的工作流时，智能体会运行多次。例如，先进行初始准备，再运行一次以调用工具，然后再次运行以评估工具响应并回复用户。

[^1]: AI 智能体是能够响应请求、做出决策并为用户执行现实任务的人工智能系统。它们使用大语言模型（LLM）理解用户输入，并根据可用信息和资源，决定如何更好地处理请求。
[^2]: 在 AI 场景中，工具是一种附加资源，AI 响应请求时可以利用它获取特定信息或功能。AI 模型可以通过工具与外部系统交互，或完成具体、专门的任务。

## 相关资源 <a id="related-resources"></a>

* [理解 AI 组件](./)
* [链的作用](what-chains-do.md)
* [记忆的工作原理](how-memory-works.md)
* [工具的工作原理](how-tools-work.md)
* [使用向量存储和搜索数据](store-and-search-data-with-vectors.md)
* [检索相关上下文](retrieve-relevant-context.md)
* [智能体与链的对比](agents-vs-chains.md)
