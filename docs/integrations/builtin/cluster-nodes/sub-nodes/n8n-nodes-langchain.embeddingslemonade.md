---
title: Embeddings Lemonade（Lemonade 嵌入模型） 节点文档
description: 了解如何在 n8n 中使用 Embeddings Lemonade（Lemonade 嵌入模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Embeddings Lemonade（Lemonade 嵌入模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Embeddings Lemonade（Lemonade 嵌入模型） 节点 <a href="#embeddings-lemonade-node" id="embeddings-lemonade-node"></a>

使用 Embeddings Lemonade 节点，通过 Lemonade 服务器托管和管理的模型生成嵌入向量。此节点适用于语义搜索、聚类、相似度匹配，以及其他需要将文本表示为数值向量的工作流。

本页列出了 Embeddings Lemonade 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Lemonade 凭据文档](../../credentials/lemonade.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置节点。

### 模型 <a href="#model" id="model"></a>

用于生成嵌入向量的模型。模型通过为此节点配置的 Lemonade 服务器加载和管理。请从 Lemonade 实例提供的可用模型列表中选择所需模型。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Embeddings Lemonade（Lemonade 嵌入模型） 集成模板](https://n8n.io/integrations/embeddings-lemonade)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Lemonade Server 文档](https://lemonade-server.ai/docs/)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}
