---
title: Embeddings Google Gemini（Google Gemini 嵌入模型） 节点文档
description: 了解如何在 n8n 中使用 Embeddings Google Gemini（Google Gemini 嵌入模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Embeddings Google Gemini（Google Gemini 嵌入模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Embeddings Google Gemini（Google Gemini 嵌入模型） 节点 <a href="#embeddings-google-gemini-node" id="embeddings-google-gemini-node"></a>

使用 Embeddings Google Gemini 节点，为指定文本生成嵌入向量[^1]。

本页列出了 Embeddings Google Gemini 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Google Gemini(PaLM) 凭据文档](../../credentials/googleai.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**（模型）：选择用于生成嵌入向量的模型。

可用模型的更多信息，请参阅 [Google Gemini 模型文档](https://ai.google.dev/models/gemini)。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Embeddings Google Gemini（Google Gemini 嵌入模型） 集成模板](https://n8n.io/integrations/embeddings-google-gemini)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 的 Google Generative AI 嵌入文档](https://docs.langchain.com/oss/javascript/integrations/embeddings/google_generative_ai)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: 嵌入是使用向量对数据进行数值化表示。AI 通过将值映射到多个维度，利用嵌入理解复杂数据及其关系。向量数据库或向量存储是专门用于存储和访问嵌入的数据库。
