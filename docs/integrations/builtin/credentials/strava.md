---
title: Strava 凭据
description: Strava 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Strava 的身份验证。
contentType:
- integration
- reference
nodeTitle: Strava 凭据
originalFilePath: integrations/builtin/credentials/strava.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/strava
url: https://docs.n8n.io/integrations/builtin/credentials/strava
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Strava 凭据 <a href="#strava-credentials" id="strava-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Strava](../app-nodes/n8n-nodes-base.strava.md)
- [Strava Trigger（触发器）](../trigger-nodes/n8n-nodes-base.stravatrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Strava](https://strava.com) 账号。
- 在 [**Settings > API**](https://www.strava.com/settings/api)（设置 > API）中创建 Strava 应用。更多信息请参阅[使用 OAuth2](#using-oauth2)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Strava API 文档](https://developers.strava.com/docs/reference/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- **Client ID**（客户端 ID）：[创建 Strava 应用](https://developers.strava.com/docs/getting-started/#account)时生成。
- **Client Secret**（客户端密钥）：[创建 Strava 应用](https://developers.strava.com/docs/getting-started/#account)时生成。

为 Strava 应用采用以下设置：

- 在 n8n 中复制 **OAuth Callback URL**（OAuth 回调 URL），粘贴到 Strava 应用的 **Authorization Callback Domain**（授权回调域名）。
- 从 **Authorization Callback Domain** 中移除协议（`https://` 或 `http://`）和相对 URL（`/oauth2/callback` 或 `/rest/oauth2-credential/callback`）。例如，OAuth Redirect URL 原本为 `https://oauth.n8n.cloud/oauth2/callback` 时，**Authorization Callback Domain** 应为 `oauth.n8n.cloud`。
- 从应用复制 **Client ID** 和 **Client Secret**，填入 n8n 凭据。

Strava OAuth 流程的更多信息，请参阅[身份验证](https://developers.strava.com/docs/authentication/)。
