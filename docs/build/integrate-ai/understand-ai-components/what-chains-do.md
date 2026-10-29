---
title: 什么是 AI 链？
description: 了解 AI 中的链，以及 n8n 中的链。
contentType: explanation
nodeTitle: 链的作用
originalFilePath: advanced-ai/examples/understand-chains.md
originalUrl: https://docs.n8n.io/advanced-ai/examples/understand-chains
url: https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-chains-do
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 什么是 AI 链？ <a href="#whats-a-chain-in-ai" id="whats-a-chain-in-ai"></a>

链[^1]将不同的 AI 组件组合成一个协同工作的系统，在组件之间建立调用顺序。这些组件可以包括模型和记忆[^2]，但请注意，n8n 中的链无法使用记忆。


## n8n 中的链 <a href="#chains-in-n8n" id="chains-in-n8n"></a>

n8n 提供三个链节点：

* [Basic LLM Chain](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm.md)：用于与 LLM 交互，不包含额外组件。
* [Question and Answer Chain](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/README.md)：可以通过检索器连接到[向量存储](#user-content-fn-3)[^3]，或通过 Workflow Retriever 节点连接到 n8n 工作流。需要构建支持针对特定文档提问的工作流时，可使用此节点。
* [Summarization Chain](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization.md)：接收输入并返回摘要。

n8n 中的链与 LangChain 等其他工具中的链有一个重要区别：n8n 的所有链节点均不支持记忆，无法记住用户之前的查询。如果使用 LangChain 编程构建 AI 应用，可以为应用添加记忆。在 n8n 中，如果工作流需要记忆，请使用智能体。要让用户与应用进行自然、持续的对话，记忆至关重要。

[^1]: AI 链通过按顺序调用组件，让你与大语言模型（LLM）和其他资源交互。n8n 中的 AI 链不使用持久记忆，因此无法引用先前的上下文；如有此需求，请使用 AI 智能体。
[^2]: 在 AI 场景中，记忆让 AI 工具能够在多次交互之间保留消息上下文。例如，你可以与 AI 智能体持续对话，而无需在每条消息中重新提供上下文。在 n8n 中，AI 智能体节点可以使用记忆，AI 链则不能。
<a id="user-content-fn-3"></a>
[^3]: 向量存储，也称向量数据库，用数学形式表示并存储信息。将其与嵌入模型和检索器配合使用，可以创建供 AI 回答问题时访问的数据库。

## 相关资源 <a id="related-resources"></a>

* [理解 AI 组件](./)
* [智能体的作用](what-agents-do.md)
* [记忆的工作原理](how-memory-works.md)
* [工具的工作原理](how-tools-work.md)
* [使用向量存储和搜索数据](store-and-search-data-with-vectors.md)
* [检索相关上下文](retrieve-relevant-context.md)
* [智能体与链的对比](agents-vs-chains.md)
