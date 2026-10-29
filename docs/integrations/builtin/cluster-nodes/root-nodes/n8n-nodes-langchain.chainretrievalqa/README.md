---
title: Question and Answer Chain（问答链） 节点文档
description: 了解如何在 n8n 中使用 Question and Answer Chain（问答链） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: n8n-nodes-langchain.chainretrievalqa
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Question and Answer Chain（问答链） 节点 <a href="#question-and-answer-chain-node" id="question-and-answer-chain-node"></a>

使用 Question and Answer Chain 节点，将[向量存储](#user-content-fn-1)[^1]用作检索器。

本页列出了 Question and Answer Chain 节点的参数，并提供更多资源的链接。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

### Query（查询） <a href="#query" id="query"></a>

你要提出的问题。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Question and Answer Chain（问答链）集成模板](https://n8n.io/integrations/retrieval-qanda-chain)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

LangChain 将向量存储用作检索器的示例，请参阅 [LangChain 语义搜索教程](https://docs.langchain.com/oss/javascript/langchain/knowledge-base)。

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误和问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。

<a id="user-content-fn-1"></a>
[^1]: 向量存储或向量数据库用于存储信息的数学表示。将其与嵌入模型和检索器配合使用，可创建供 AI 在回答问题时访问的数据库。
