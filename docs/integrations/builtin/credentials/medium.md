---
title: Medium 凭据
description: Medium 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Medium 的身份验证。
contentType:
- integration
- reference
nodeTitle: Medium 凭据
originalFilePath: integrations/builtin/credentials/medium.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/medium
url: https://docs.n8n.io/integrations/builtin/credentials/medium
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Medium 凭据 <a href="#medium-credentials" id="medium-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Medium](../app-nodes/n8n-nodes-base.medium.md)

{% hint style="warning" %}
**Medium API 已停止支持**

Medium 已停止支持 Medium API。这些凭据仍会出现在 n8n 中，但无法用于配置新的集成。
{% endhint %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 在 [Medium](https://www.medium.com/) 创建账户。
- 使用 OAuth2 时，请发送邮件至 [yourfriends@medium.com](mailto:yourfriends@medium.com)，申请凭据访问权限。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Medium API 文档](https://github.com/Medium/medium-api-docs)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要：

- 一个 API **Access Token**（访问令牌）：在 **Settings >** [**Security and apps**](https://medium.com/me/settings/security) **> Integration tokens**（设置 > 安全与应用 > 集成令牌）中生成令牌。将生成的集成令牌用作 n8n 的 **Access Token**。

更多信息请参阅 Medium API 的[自行签发访问令牌文档](https://github.com/Medium/medium-api-docs?tab=readme-ov-file#21-self-issued-access-tokens)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- 一个 **Client ID（客户端 ID）**
- 一个 **Client Secret（客户端密钥）**

生成 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）需要访问 **Developers**（开发者）菜单，在其中创建新应用即可生成客户端 ID 和密钥。

为新应用使用以下设置：

- 将 **Authorization Protocol**（授权协议）设为 **OAuth 2**。
- 从 n8n 复制 **OAuth Callback URL**（OAuth 回调 URL），将其用作 Medium 中的 **Callback URL**（回调 URL）。
