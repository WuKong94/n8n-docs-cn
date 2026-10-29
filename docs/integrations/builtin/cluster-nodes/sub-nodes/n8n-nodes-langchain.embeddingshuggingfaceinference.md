---
title: Embeddings HuggingFace Inference（HuggingFace Inference 嵌入模型） 节点文档
description: 了解如何在 n8n 中使用 Embeddings HuggingFace Inference（HuggingFace Inference
  嵌入模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Embeddings HuggingFace Inference（HuggingFace Inference 嵌入模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Embeddings HuggingFace Inference（HuggingFace Inference 嵌入模型） 节点 <a href="#embeddings-huggingface-inference-node" id="embeddings-huggingface-inference-node"></a>

使用 Embeddings HuggingFace Inference 节点，为指定文本生成嵌入向量[^1]。

本页列出了 Embeddings HuggingFace Inference 的节点参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Hugging Face 凭据文档](../../credentials/huggingface.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**（模型）：选择用于生成嵌入向量的模型。

可用模型请参阅 [Hugging Face 模型文档](https://huggingface.co/models?other=embeddings)。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Custom Inference Endpoint**（自定义推理端点）：输入部署在 HuggingFace 上的模型 URL。设置后，n8n 会忽略 **Model Name**（模型名称）。

更多信息请参阅 [HuggingFace 推理指南](https://huggingface.co/inference-endpoints)。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Embeddings HuggingFace Inference（HuggingFace Inference 嵌入模型） 集成模板](https://n8n.io/integrations/embeddings-hugging-face-inference)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: 嵌入是使用向量对数据进行数值化表示。AI 通过将值映射到多个维度，利用嵌入理解复杂数据及其关系。向量数据库或向量存储是专门用于存储和访问嵌入的数据库。
