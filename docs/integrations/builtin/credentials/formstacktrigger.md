---
title: Formstack Trigger 凭据
description: Formstack Trigger 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Formstack Trigger 的身份验证。
contentType:
- integration
- reference
nodeTitle: Formstack Trigger 凭据
originalFilePath: integrations/builtin/credentials/formstacktrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/formstacktrigger
url: https://docs.n8n.io/integrations/builtin/credentials/formstacktrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Formstack Trigger 凭据 <a href="#formstack-trigger-credentials" id="formstack-trigger-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Formstack Trigger](../trigger-nodes/n8n-nodes-base.formstacktrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建 [Formstack](https://www.formstack.com/) 账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Formstack API 文档](https://developers.formstack.com/reference/api-overview)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要：

- API **Access Token**（访问令牌）：如需生成访问令牌，请在 Formstack 中使用以下信息[创建新应用](https://www.formstack.com/admin/apiKey/main)：
    * **Redirect URI**（重定向 URI）：n8n 云实例请填写 `https://oauth.n8n.cloud/oauth2/callback`。
        - 自托管 n8n 实例请填写该实例的 OAuth 回调 URL，格式为 `https://<n8n_url>/rest/oauth2-credential/callback`，例如 `https://localhost:5678/rest/oauth2-credential/callback`。
    * **Platform**（平台）：选择 **Website**（网站）。

创建应用后，从应用列表中复制访问令牌，或选择应用并查看详情以复制令牌。

更详细的说明，请参阅 [Formstack API 授权文档](https://developers.formstack.com/reference/api-overview#obtaining-an-api-key-oauth2-access-token)。

{% hint style="info" %}
**访问令牌权限**

Formstack 将访问令牌关联到 Formstack 用户。访问令牌遵循 Formstack 应用内的用户权限。
{% endhint %}

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- 一个 **Client ID（客户端 ID）**
- 一个 **Client Secret（客户端密钥）**

如需生成这两项，请在 Formstack 中使用以下信息[创建新应用](https://www.formstack.com/admin/apiKey/main)：

- **Redirect URI**（重定向 URI）：从 n8n 凭据中复制 **OAuth Redirect URL**（OAuth 重定向 URL），填入此处。
    - 自托管 n8n 实例请填写该实例的 OAuth 回调 URL，格式为 `https://<n8n_url>/rest/oauth2-credential/callback`，例如 `https://localhost:5678/rest/oauth2-credential/callback`。
- **Platform**（平台）：选择 **Website**（网站）。

创建应用后，在应用列表中选择该应用，查看 **Application Details**（应用详情）。复制 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥），填入 n8n。添加两项信息后，选择 **Connect my account**（连接我的账户）按钮，开始 OAuth2 流程和授权过程。

更详细的说明，请参阅 [Formstack API 授权文档](https://developers.formstack.com/reference/api-overview#obtaining-an-api-key-oauth2-access-token)。

{% hint style="info" %}
**访问令牌权限**

Formstack 将访问令牌关联到 Formstack 用户。访问令牌遵循 Formstack 应用内的用户权限。
{% endhint %}

