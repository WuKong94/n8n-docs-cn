---
title: AI 中的工具是什么？
description: 了解 AI 中的工具，以及 n8n 工具功能的特点。
contentType: explanation
nodeTitle: 工具的工作原理
originalFilePath: advanced-ai/examples/understand-tools.md
originalUrl: https://docs.n8n.io/advanced-ai/examples/understand-tools
url: https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-tools-work
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# AI 中的工具是什么？ <a href="#whats-a-tool-in-ai" id="whats-a-tool-in-ai"></a>

在 AI 中，“工具”具有特定含义。工具类似于附加组件，AI 可以通过它们访问更多上下文或资源。

也可以用以下两种方式理解：

> 工具是智能体与外部世界交互所使用的接口（[来源](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/)）。



> 可以将工具理解为 AI 模型能够调用的函数（[来源](https://www.udemy.com/course/chatgpt-and-langchain-the-complete-developers-masterclass/)）。

## n8n 中的 AI 工具 <a href="#ai-tools-in-n8n" id="ai-tools-in-n8n"></a>

n8n 提供内置节点[^1]和 [MCP 服务器](../mcp-servers.md)注册表，可以将它们作为工具连接到 [AI 智能体](#user-content-fn-2)[^2]。内置节点包括 [Wikipedia](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwikipedia.md) 和 [SerpAPI](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi.md) 等常用服务。
此外，n8n 还提供三个功能强大的工具：

* [Call n8n Workflow Tool](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md)：将任意 n8n 工作流加载为工具。
* [Custom Code Tool](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode.md)：编写智能体可以运行的代码。
* [HTTP Request Tool](../../../integrations/builtin/core-nodes/n8n-nodes-base.httprequest/README.md)：通过请求获取网页或 API 数据。

以下三个示例重点展示 Call n8n Workflow Tool：

- [与 Google Sheets 对话](../ai-examples/use-google-sheets-as-a-data-source.md)
- [调用 API 获取数据](../ai-examples/call-apis.md)
- [设置人工兜底](../ai-examples/set-a-human-fallback-for-ai-workflows.md)

还可以学习如何[通过 `$fromAI()` 函数让 AI 动态指定工具参数](../ai-examples/use-ai-for-parameters.md)。

[^1]: n8n 集群节点由一个根节点及连接到它的一个或多个子节点组成。子节点扩展根节点的功能，提供特定服务或资源的访问能力，或提供计算器等专门处理能力。
<a id="user-content-fn-2"></a>
[^2]: AI 智能体是能够响应请求、做出决策并为用户执行现实任务的人工智能系统。它们使用大语言模型（LLM）理解用户输入，并根据可用信息和资源，决定如何更好地处理请求。

## 相关资源 <a id="related-resources"></a>

* [理解 AI 组件](./)
* [链的作用](what-chains-do.md)
* [智能体的作用](what-agents-do.md)
* [记忆的工作原理](how-memory-works.md)
* [使用向量存储和搜索数据](store-and-search-data-with-vectors.md)
* [检索相关上下文](retrieve-relevant-context.md)
* [智能体与链的对比](agents-vs-chains.md)
