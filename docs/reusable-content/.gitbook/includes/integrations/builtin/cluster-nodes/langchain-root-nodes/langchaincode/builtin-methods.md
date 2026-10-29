---
title: LangChain Code 内置方法
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

| 方法 | 说明 |
| ------ | ----------- |
| `this.addInputData(inputName, data)` | 填充指定非主输入的数据，便于模拟数据。<ul><li>`inputName` 为连接类型，必须是以下之一：`ai_agent`、`ai_chain`、`ai_document`、`ai_embedding`、`ai_languageModel`、`ai_memory`、`ai_outputParser`、`ai_retriever`、`ai_textSplitter`、`ai_tool`、`ai_vectorRetriever`、`ai_vectorStore`</li><li>`data` 包含要添加的数据。n8n 要求的数据结构见[数据结构](../../../../../../../../build/work-with-data/understand-n8ns-data-structure.md)。</li></ul> |
| `this.addOutputData(outputName, data)` | 填充指定非主输出的数据，便于模拟数据。<ul><li>`outputName` 为连接类型，必须是以下之一：`ai_agent`、`ai_chain`、`ai_document`、`ai_embedding`、`ai_languageModel`、`ai_memory`、`ai_outputParser`、`ai_retriever`、`ai_textSplitter`、`ai_tool`、`ai_vectorRetriever`、`ai_vectorStore`</li><li>`data` 包含要添加的数据。n8n 要求的数据结构见[数据结构](../../../../../../../../build/work-with-data/understand-n8ns-data-structure.md)。</li></ul> |
| `this.getInputConnectionData(inputName, itemIndex, inputIndex?)` | 从指定非主输入获取数据。<ul><li>`inputName` 为输入连接类型，必须是以下之一：`ai_agent`、`ai_chain`、`ai_document`、`ai_embedding`、`ai_languageModel`、`ai_memory`、`ai_outputParser`、`ai_retriever`、`ai_textSplitter`、`ai_tool`、`ai_vectorRetriever`、`ai_vectorStore`</li><li>`itemIndex` 应始终设为 `0`（该参数将用于后续功能）。</li><li>同一指定输入连接多个节点时，使用 `inputIndex`。</li></ul> |
| `this.getInputData(inputIndex?, inputName?)` | 获取主输入的数据。 |
| `this.getNode()` | 获取当前节点。 |
| `this.getNodeOutputs()` | 获取当前节点的输出。 |
| `this.getExecutionCancelSignal()` | 工作流停止时，用于停止函数执行。大多数工作流由 n8n 自动处理，但自行构建链或智能体时，可能需要使用。 |
