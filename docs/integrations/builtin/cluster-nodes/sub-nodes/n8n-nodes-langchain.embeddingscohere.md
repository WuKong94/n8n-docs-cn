---
title: Embeddings Cohere（Cohere 嵌入模型） 节点文档
description: 了解如何在 n8n 中使用 Embeddings Cohere（Cohere 嵌入模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Embeddings Cohere（Cohere 嵌入模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Embeddings Cohere（Cohere 嵌入模型） 节点 <a href="#embeddings-cohere-node" id="embeddings-cohere-node"></a>

使用 Embeddings Cohere 节点，为指定文本生成嵌入向量[^1]。

本页列出了 Embeddings Cohere 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Cohere 凭据文档](../../credentials/cohere.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**（模型）：选择用于生成嵌入向量的模型，可选：
    * **Embed-English-v2.0(4096 Dimensions)**（4096 维）
    * **Embed-English-Light-v2.0(1024 Dimensions)**（1024 维）
    * **Embed-Multilingual-v2.0(768 Dimensions)**（768 维）

可用模型的更多信息，请参阅 [Cohere 模型文档](https://docs.cohere.com/docs/models)。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Embeddings Cohere（Cohere 嵌入模型） 集成模板](https://n8n.io/integrations/embeddings-cohere)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 的 Cohere 嵌入文档](https://docs.langchain.com/oss/javascript/integrations/embeddings/cohere)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: 嵌入是使用向量对数据进行数值化表示。AI 通过将值映射到多个维度，利用嵌入理解复杂数据及其关系。向量数据库或向量存储是专门用于存储和访问嵌入的数据库。
