---
title: Google Gemini(PaLM) 凭据
description: Google Gemini(PaLM) 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Google Gemini 和 Google
  PaLM AI 节点的身份验证。
contentType:
- integration
- reference
priority: high
nodeTitle: Google Gemini(PaLM) 凭据
originalFilePath: integrations/builtin/credentials/googleai.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/googleai
url: https://docs.n8n.io/integrations/builtin/credentials/googleai
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Gemini(PaLM) 凭据 <a href="#google-geminipalm-credentials" id="google-geminipalm-credentials"></a>

{% hint style="info" %}
在 n8n Cloud 上，对于支持此功能的节点，可在凭据字段中选择 **Use Gateway credits**（使用 Gateway 额度），跳过 Google Gemini 凭据设置。详情请参阅 [Gateway 额度](../../../deploy/use-n8n-cloud/gateway-credits/README.md)。
{% endhint %}

这些凭据可用于以下节点的身份验证：

* [Embeddings Google Gemini（向量嵌入）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini.md)
* [Google Gemini](../app-nodes/n8n-nodes-langchain.googlegemini.md)
* [Google Gemini Chat Model（聊天模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini.md)
* [Embeddings Google PaLM（向量嵌入）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建 [Google Cloud](https://cloud.google.com/) 账户。
* 创建 [Google Cloud Platform 项目](https://developers.google.com/workspace/marketplace/create-gcp-project)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Gemini(PaLM) API 密钥

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Google Gemini API 文档](https://ai.google.dev/gemini-api/docs)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 Gemini(PaLM) API 密钥 <a href="#using-geminipalm-api-key" id="using-geminipalm-api-key"></a>

配置此凭据需要：

- API **Host**（主机）URL：PaLM 和 Gemini 均使用默认值 `https://generativelanguage.googleapis.com`。
- **API Key**（API 密钥）：在 [Google AI Studio](https://aistudio.google.com/apikey) 中创建密钥。

{% hint style="warning" %}
**不支持自定义主机**

相关节点尚不支持为 API 主机设置自定义主机或代理，必须使用 `https://generativelanguage.googleapis.com`。
{% endhint %}

创建 API 密钥：

1. 进入 Google AI Studio 的 API Key 页面：[https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)。
2. 选择 **Create API Key**（创建 API 密钥）。
3. 可选择 **Create API key in new project**（在新项目中创建 API 密钥），也可搜索现有 Google Cloud 项目并选择 **Create API key in existing project**（在现有项目中创建 API 密钥）。
4. 复制生成的 API 密钥，添加到 n8n 凭据。
