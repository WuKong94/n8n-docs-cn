---
title: Embeddings Google Vertex（Google Vertex 嵌入模型） 节点文档
description: 了解如何在 n8n 中使用 Google Vertex 嵌入模型节点，并将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Embeddings Google Vertex（Google Vertex 嵌入模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglevertex.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglevertex
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglevertex
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Embeddings Google Vertex（Google Vertex 嵌入模型） 节点 <a href="#embeddings-google-vertex-node" id="embeddings-google-vertex-node"></a>

使用 Embeddings Google Vertex 节点，为指定文本生成嵌入向量[^1]。

本页列出了 Embeddings Google Vertex 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

使用 [Google Vertex AI 凭据](../../credentials/googlevertexai.md)，将项目、区域和服务账户详情一并存储。此节点也支持 [Google 服务账户凭据](../../credentials/google/service-account.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

- **Authentication**（身份验证）：选择 **Google Service Account**（Google 服务账户，默认）或 **Google Vertex AI**。
- **Project ID**（项目 ID）：使用 **Google Service Account** 身份验证时，n8n 根据服务账户的访问权限加载项目列表。可选择列表中的项目，也可手动输入项目 ID。使用 **Google Vertex AI** 身份验证时，在凭据中配置项目。
- **Model Name**（模型名称）：输入用于生成嵌入向量的模型名称。
- **Region**（区域）：选择 **Default (Use Credential Region)**（默认，使用凭据区域），使用凭据中设置的区域。要覆盖此值，选择 **Global**（全球）、**EU (Multi-Region)**（欧盟，多区域）或 **US (Multi-Region)**（美国，多区域）。

可用嵌入模型的更多信息，请参阅 [Google Vertex AI 嵌入 API 文档](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api)。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>



[浏览 Embeddings Google Vertex（Google Vertex 嵌入模型） 集成模板](https://n8n.io/integrations/embeddings-google-vertex)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 的 Google Vertex AI 嵌入文档](https://docs.langchain.com/oss/javascript/integrations/embeddings/google_vertex_ai)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: 嵌入是使用向量对数据进行数值化表示。AI 通过将值映射到多个维度，利用嵌入理解复杂数据及其关系。向量数据库或向量存储是专门用于存储和访问嵌入的数据库。
