---
title: Embeddings Google PaLM（Google PaLM 嵌入模型） 节点文档
description: 了解如何在 n8n 中使用 Embeddings Google PaLM（Google PaLM 嵌入模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Embeddings Google PaLM（Google PaLM 嵌入模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Embeddings Google PaLM（Google PaLM 嵌入模型） 节点 <a href="#embeddings-google-palm-node" id="embeddings-google-palm-node"></a>

使用 Embeddings Google PaLM 节点，为指定文本生成嵌入向量[^1]。

本页列出了 Embeddings Google PaLM 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Google Gemini(PaLM) 凭据文档](../../credentials/googleai.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**（模型）：选择用于生成嵌入向量的模型。

n8n 从 Google PaLM API 动态加载模型，你只会看到自己的账户可用的模型。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Embeddings Google PaLM（Google PaLM 嵌入模型） 集成模板](https://n8n.io/integrations/embeddings-google-palm)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: 嵌入是使用向量对数据进行数值化表示。AI 通过将值映射到多个维度，利用嵌入理解复杂数据及其关系。向量数据库或向量存储是专门用于存储和访问嵌入的数据库。
