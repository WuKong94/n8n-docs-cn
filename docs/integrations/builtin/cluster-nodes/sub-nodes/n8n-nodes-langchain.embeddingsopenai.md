---
title: Embeddings OpenAI（OpenAI 嵌入模型） 节点文档
description: 了解如何在 n8n 中使用 Embeddings OpenAI（OpenAI 嵌入模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Embeddings OpenAI（OpenAI 嵌入模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Embeddings OpenAI（OpenAI 嵌入模型） 节点 <a href="#embeddings-openai-node" id="embeddings-openai-node"></a>

使用 Embeddings OpenAI 节点，为指定文本生成嵌入向量[^1]。

本页列出了 Embeddings OpenAI 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [OpenAI 凭据文档](../../credentials/openai.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}


## 节点选项 <a href="#node-options" id="node-options"></a>

* **Model**（模型）：选择用于生成嵌入向量的模型。
* **Base URL**（基础 URL）：输入请求发送到的 URL。使用自行托管、兼容 OpenAI 的模型时，可设置此项。
* **Batch Size**（批次大小）：输入每次请求发送的最大文档数量。
* **Strip New Lines**（移除换行符）：开启时移除输入文本中的换行符，关闭时不移除。n8n 默认启用此项。
* **Timeout**（超时）：输入请求的最长耗时，单位为秒。设为 `-1` 表示不设置超时。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Embeddings OpenAI（OpenAI 嵌入模型） 集成模板](https://n8n.io/integrations/embeddings-openai)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 的 OpenAI 嵌入文档](https://docs.langchain.com/oss/javascript/integrations/embeddings/openai)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: 嵌入是使用向量对数据进行数值化表示。AI 通过将值映射到多个维度，利用嵌入理解复杂数据及其关系。向量数据库或向量存储是专门用于存储和访问嵌入的数据库。
