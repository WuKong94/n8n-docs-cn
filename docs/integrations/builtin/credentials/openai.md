---
title: OpenAI 凭据
contentType:
- integration
- reference
priority: critical
nodeTitle: OpenAI 凭据
originalFilePath: integrations/builtin/credentials/openai.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/openai
url: https://docs.n8n.io/integrations/builtin/credentials/openai
description: OpenAI 凭据文档。使用这些凭据在 n8n 中完成 OpenAI 的身份验证。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# OpenAI 凭据 <a id="openai-credentials"></a>

{% hint style="info" %}
在 n8n Cloud 上，可以在支持此功能的节点凭据字段中选择 **Use Gateway credits（使用 Gateway 额度）**，无需另行设置 OpenAI 凭据。详情请参阅 [Gateway 额度](../../../deploy/use-n8n-cloud/gateway-credits/README.md)。
{% endhint %}

这些凭据可用于以下节点的身份验证：

* [OpenAI](../app-nodes/n8n-nodes-langchain.openai/README.md)
* [Chat OpenAI（聊天模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/README.md)
* [Embeddings OpenAI（嵌入模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai.md)
* [LM OpenAI](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/README.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [OpenAI](https://platform.openai.com/signup/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [OpenAI API 文档](https://platform.openai.com/docs/introduction)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

* 一个 **API Key**（API 密钥）
* **Organization ID**（组织 ID）：属于多个组织时必填，否则留空。

生成 API 密钥：

1. 登录 OpenAI 账户，或[创建](https://platform.openai.com/signup/)账户。
2. 打开 [API 密钥](https://platform.openai.com/api-keys)页面。
3. 选择 **Create new secret key**（创建新密钥），创建 API 密钥，也可以为密钥命名。
4. 复制密钥，填入 n8n 的 **API Key** 字段。

更多信息，请参阅 [API 快速入门的账户设置文档](https://platform.openai.com/docs/quickstart/account-setup)。

查找 Organization ID 的步骤如下：

1. 进入 [Organization Settings（组织设置）](https://platform.openai.com/account/organization)页面。
2. 复制组织 ID，填入 n8n 的 **Organization ID**（组织 ID）。

更多信息，请参阅[设置组织](https://platform.openai.com/docs/guides/production-best-practices/setting-up-your-organization)。请注意，使用组织 ID 发起的 API 请求会计入该组织的订阅配额。
