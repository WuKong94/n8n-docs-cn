---
title: Reranker Cohere（Cohere 重排序器）
description: 了解如何在 n8n 中使用 Reranker Cohere 节点，并按照技术文档将 Cohere 重排序集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Reranker Cohere（Cohere 重排序器）
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Reranker Cohere（Cohere 重排序器） <a href="#reranker-cohere" id="reranker-cohere"></a>

Reranker Cohere 节点支持重排序[^1]，可重新排列来自[向量存储](#user-content-fn-2)[^2]的结果块。可将此节点连接到向量存储。

重排序器针对指定查询，将向量存储检索出的文档按相关性从高到低重新排列。

本页列出了 Reranker Cohere 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Cohere 凭据文档](../../credentials/cohere.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

### 模型 <a href="#model" id="model"></a>

选择要使用的重排序模型。可用模型的更多信息，请参阅 [Cohere 模型文档](https://docs.cohere.com/docs/models#rerank)。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Reranker Cohere（Cohere 重排序器） 集成模板](https://n8n.io/integrations/reranker-cohere)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: 重排序是一种优化候选文档列表顺序、提高搜索结果相关性的技术。检索增强生成（RAG）等应用使用重排序，优先选择最相关的信息，用于生成或下游任务。
<a id="user-content-fn-2"></a>
[^2]: 向量存储或向量数据库用于存储信息的数学表示。将其与嵌入模型和检索器配合使用，可创建供 AI 在回答问题时访问的数据库。
