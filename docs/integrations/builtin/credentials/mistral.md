---
title: Mistral Cloud 凭据
description: Mistral Cloud 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Mistral Cloud 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Mistral Cloud 凭据
originalFilePath: integrations/builtin/credentials/mistral.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/mistral
url: https://docs.n8n.io/integrations/builtin/credentials/mistral
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Mistral Cloud 凭据 <a href="#mistral-cloud-credentials" id="mistral-cloud-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Mistral AI](../app-nodes/n8n-nodes-base.mistralai.md)
* [Mistral Cloud](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud.md)
* [Embeddings Mistral Cloud（嵌入模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>


- 创建 [Mistral](https://mistral.ai/) La Plateforme 账户。
- 必须在 **Workspace >** [**Billing**](https://admin.mistral.ai/organization/billing)（工作区 > 账单）中添加付款信息并启用付款，才能启用 API 密钥。更多信息请参阅[账户设置](https://docs.mistral.ai/getting-started/quickstart/#account-setup)。


## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关这些 API 的更多信息，请参阅 [Mistral API 文档](https://docs.mistral.ai/api/)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**

为 Mistral Cloud 账户添加付款信息后：

1. 登录你的 [Mistral 账户](https://console.mistral.ai/home)。
2. 进入 **API Keys**（API 密钥）页面。
3. 选择 **Create new key**（创建新密钥）。
4. 复制 API 密钥，填入 n8n 凭据。

更多信息请参阅[账户设置](https://docs.mistral.ai/getting-started/quickstart/#account-setup)。

{% hint style="info" %}
**需要付费账户**

Mistral 要求添加付款信息并启用付款，才能使用 API 密钥。更多信息请参阅上方的[前置条件](#prerequisites)。
{% endhint %}
