---
title: Sentry.io 凭据
description: Sentry.io 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Sentry.io 的身份验证。
contentType:
- integration
- reference
nodeTitle: Sentry.io 凭据
originalFilePath: integrations/builtin/credentials/sentryio.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/sentryio
url: https://docs.n8n.io/integrations/builtin/credentials/sentryio
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Sentry.io 凭据 <a href="#sentryio-credentials" id="sentryio-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Sentry.io](../app-nodes/n8n-nodes-base.sentryio.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Sentry.io](https://sentry.io/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）
- OAuth2
- Server API token（服务器 API 令牌）：用于[自托管 Sentry](https://develop.sentry.dev/self-hosted/)。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Sentry.io API 文档](https://docs.sentry.io/api/)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要：

- API **Token**（API 令牌）：在 **Account > Settings > User Auth Tokens**（账户 > 设置 > 用户身份验证令牌）中生成 [**User Auth Token**](https://sentry.io/settings/account/api/auth-tokens/)。更多信息请参阅 [User Auth Tokens](https://docs.sentry.io/account/auth-tokens/#user-auth-tokens)。

## 使用 OAuth <a href="#using-oauth" id="using-oauth"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果需要从头配置 OAuth2，请[创建集成](https://docs.sentry.io/organization/integrations/integration-platform/#creating-an-integration)，并采用以下设置：

- 复制 n8n 的 **OAuth Callback URL**（OAuth 回调 URL），将其添加为 **Authorized Redirect URI**（授权重定向 URI）。
- 复制 **Client ID** 和 **Client Secret**，填入 n8n 凭据。

创建集成的更多信息，请参阅[公开集成](https://docs.sentry.io/organization/integrations/integration-platform/public-integration/)。

## 使用服务器 API 令牌 <a href="#using-server-api-token" id="using-server-api-token"></a>

配置此凭据需要：

- API **Token**（API 令牌）：在 **Account > Settings > User Auth Tokens**（账户 > 设置 > 用户身份验证令牌）中生成 [**User Auth Token**](https://sentry.io/settings/account/api/auth-tokens/)。更多信息请参阅 [User Auth Tokens](https://docs.sentry.io/account/auth-tokens/#user-auth-tokens)。
- 自托管 Sentry 实例的 **URL**。
