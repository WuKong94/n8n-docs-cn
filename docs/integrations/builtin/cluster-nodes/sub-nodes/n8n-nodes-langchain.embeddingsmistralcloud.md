---
title: Embeddings Mistral Cloud（Mistral Cloud 嵌入模型） 节点文档
description: 了解如何在 n8n 中使用 Embeddings Mistral Cloud（Mistral Cloud 嵌入模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Embeddings Mistral Cloud（Mistral Cloud 嵌入模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Embeddings Mistral Cloud（Mistral Cloud 嵌入模型） 节点 <a href="#embeddings-mistral-cloud-node" id="embeddings-mistral-cloud-node"></a>

使用 Embeddings Mistral Cloud 节点，为指定文本生成嵌入向量[^1]。

本页列出了 Embeddings Mistral Cloud 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Mistral Cloud 凭据文档](../../credentials/mistral.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**（模型）：选择用于生成嵌入向量的模型。

可用模型的更多信息，请参阅 [Mistral 模型文档](https://docs.mistral.ai/models/)。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Batch Size**（批次大小）：输入每次请求发送的最大文档数量。
* **Strip New Lines**（移除换行符）：开启时移除输入文本中的换行符，关闭时不移除。n8n 默认启用此项。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Embeddings Mistral Cloud（Mistral Cloud 嵌入模型） 集成模板](https://n8n.io/integrations/embeddings-mistral-cloud)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 的 Mistral 嵌入文档](https://docs.langchain.com/oss/javascript/integrations/embeddings/mistralai)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: 嵌入是使用向量对数据进行数值化表示。AI 通过将值映射到多个维度，利用嵌入理解复杂数据及其关系。向量数据库或向量存储是专门用于存储和访问嵌入的数据库。
