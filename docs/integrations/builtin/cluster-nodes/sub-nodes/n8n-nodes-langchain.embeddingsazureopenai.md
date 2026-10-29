---
title: Microsoft Foundry Embeddings（Microsoft Foundry 嵌入模型） 节点文档
description: 了解如何在 n8n 中使用 Microsoft Foundry Embeddings（Microsoft Foundry 嵌入模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Microsoft Foundry Embeddings（Microsoft Foundry 嵌入模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Foundry Embeddings（Microsoft Foundry 嵌入模型） 节点 <a href="#embeddings-azure-openai-node" id="embeddings-azure-openai-node"></a>

使用 Microsoft Foundry Embeddings 节点，为指定文本生成嵌入向量[^1]。

此节点此前名为 **Embeddings Azure OpenAI**。

本页列出了 Microsoft Foundry Embeddings 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Microsoft Foundry 凭据文档](../../credentials/azureopenai.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}


## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Authentication**（身份验证）：选择节点登录 Azure 的方式，每个选项使用独立凭据。
    * **API Key**（API 密钥）：使用已保存的 API 密钥，为默认选项。请参阅[使用 API 密钥](../../credentials/azureopenai.md#using-api-key)。
    * **Azure Entra ID (OAuth2)**：使用客户端 ID 和密钥，以 Entra 应用身份登录。组织不允许存储 API 密钥时，使用此项。n8n 中不会保存 API 密钥。请参阅[使用 Microsoft Foundry（Entra ID）](../../credentials/azureopenai.md#using-azure-entra-id-oauth2)。

两种方式均支持 **Classic**（经典）和 **Microsoft Foundry** 端点类型。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Model (Deployment) Name**（模型或部署名称）：选择用于生成嵌入向量的模型（部署）。
* **Batch Size**（批次大小）：输入每次请求发送的最大文档数量。
* **Strip New Lines**（移除换行符）：开启时移除输入文本中的换行符，关闭时不移除。n8n 默认启用此项。
* **Timeout**（超时）：输入请求的最长耗时，单位为秒。设为 `-1` 表示不设置超时。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Microsoft Foundry Embeddings（Microsoft Foundry 嵌入模型） 集成模板](https://n8n.io/integrations/embeddings-azure-openai)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 的 Azure OpenAI 嵌入文档](https://docs.langchain.com/oss/javascript/integrations/embeddings/azure_openai)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: 嵌入是使用向量对数据进行数值化表示。AI 通过将值映射到多个维度，利用嵌入理解复杂数据及其关系。向量数据库或向量存储是专门用于存储和访问嵌入的数据库。
