---
contentType: overview
title: 高级 AI 示例与概念
description: 通过 n8n 构建 AI 功能的工作流示例和使用场景。
hide:
- toc
nodeTitle: AI 示例
originalFilePath: advanced-ai/examples/introduction.md
originalUrl: https://docs.n8n.io/advanced-ai/examples/introduction
url: https://docs.n8n.io/build/integrate-ai/ai-examples
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 高级 AI 示例与概念 <a href="#advanced-ai-examples-and-concepts" id="advanced-ai-examples-and-concepts"></a>

本节解释重要的 AI 概念，并提供展示这些概念的工作流模板、说明及配置指南。示例涵盖常见使用场景，展示 n8n 高级 AI 的不同功能。

<div class="grid cards" markdown>

-   __智能体与链__

	了解 AI 中的智能体[^1]和链[^2]，并通过工作流示例探索两者的主要区别。

	[→ 什么是 AI 链？](understand-ai-components/what-chains-do.md)\
    [→ 什么是 AI 智能体？](understand-ai-components/what-agents-do.md)\
	[→ 演示智能体与链的主要区别](understand-ai-components/agents-vs-chains.md)

-   __Call n8n Workflow Tool__

    了解 AI 中的工具[^3]，再探索将 n8n 工作流用作自定义工具的示例，让 AI 工作流能够访问更多数据。

	[→ AI 中的工具是什么？](understand-ai-components/how-tools-work.md)\
    [→ 与 Google Sheets 对话](ai-examples/use-google-sheets-as-a-data-source.md)\
	[→ 调用 API 获取数据](ai-examples/call-apis.md)\
	[→ 设置人工兜底](ai-examples/set-a-human-fallback-for-ai-workflows.md)\
	[→ 通过 `$fromAI()` 让 AI 指定工具参数](ai-examples/use-ai-for-parameters.md)

-   __向量数据库__

    了解 AI 中的[向量数据库](#user-content-fn-4)[^4]，以及嵌入[^5]和检索器等相关概念。

	[→ 什么是向量数据库？](understand-ai-components/store-and-search-data-with-vectors.md)\
    [→ 将网站内容写入 Pinecone 向量数据库](ai-examples/use-website-content.md)\

-   __记忆__

    了解 AI 中的记忆[^6]。

	[→ AI 中的记忆是什么？](understand-ai-components/how-memory-works.md)\

-   __AI 工作流模板__

	你可以在 n8n 网站浏览 AI 模板，包括社区贡献的模板。

    [→ 浏览所有 AI 模板](https://n8n.io/workflows/?categories=25)


   
</div>

[^1]: AI 智能体是能够响应请求、做出决策并为用户执行现实任务的人工智能系统。它们使用大语言模型（LLM）理解用户输入，并根据可用信息和资源，决定如何更好地处理请求。
[^2]: AI 链通过按顺序调用组件，让你与大语言模型（LLM）和其他资源交互。n8n 中的 AI 链不使用持久记忆，因此无法引用先前的上下文；如有此需求，请使用 AI 智能体。
[^3]: 在 AI 场景中，工具是一种附加资源，AI 响应请求时可以利用它获取特定信息或功能。AI 模型可以通过工具与外部系统交互，或完成具体、专门的任务。
<a id="user-content-fn-4"></a>
[^4]: 向量存储，也称向量数据库，用数学形式表示并存储信息。将其与嵌入模型和检索器配合使用，可以创建供 AI 回答问题时访问的数据库。
[^5]: 嵌入（embedding）是使用向量对数据进行的数值表示。AI 通过将数值映射到多个维度来理解复杂数据及其关系。向量数据库，也称向量存储，是专门用于存储和访问嵌入的数据库。
[^6]: 在 AI 场景中，记忆让 AI 工具能够在多次交互之间保留消息上下文。例如，你可以与 AI 智能体持续对话，而无需在每条消息中重新提供上下文。在 n8n 中，AI 智能体节点可以使用记忆，AI 链则不能。

## 本节内容 <a id="in-this-section"></a>

* [使用 Google Sheets 作为数据源](ai-examples/use-google-sheets-as-a-data-source.md)：通过 n8n 工作流工具，将 Google Sheets 数据加载到 AI 工作流中。
* [调用 API](ai-examples/call-apis.md)：通过 n8n 工作流工具，使用 HTTP Request 节点从 API 加载数据。
* [使用网站内容](ai-examples/use-website-content.md)：抓取网站，将数据加载到 Pinecone，再通过聊天工作流查询。
* [为工具添加人工审核](ai-examples/human-in-the-loop-for-tools.md)：要求 AI Agent 在运行工具前获得人工批准。
* [为 AI 工作流设置人工兜底](ai-examples/set-a-human-fallback-for-ai-workflows.md)：AI 无法提供帮助时，触发人工回答。
* [使用 AI 填写参数](ai-examples/use-ai-for-parameters.md)：通过 `$fromAI()` 动态填写 AI 应用工具的参数。

## 相关资源 <a id="related-resources"></a>

* [集成 AI](./)
* [MCP 服务器](mcp-servers.md)
* [理解 AI 组件](understand-ai-components/README.md)
* [n8n 中的 LangChain](langchain-in-n8n.md)
* [测试和改进 AI 工作流](test-and-improve-ai-workflows/README.md)
