---
title: GoToWebinar 凭据
description: GoToWebinar 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 GoToWebinar 的身份验证。
contentType:
- integration
- reference
nodeTitle: GoToWebinar 凭据
originalFilePath: integrations/builtin/credentials/gotowebinar.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/gotowebinar
url: https://docs.n8n.io/integrations/builtin/credentials/gotowebinar
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# GoTo Webinar 凭据 <a href="#goto-webinar-credentials" id="goto-webinar-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [GoToWebinar](../app-nodes/n8n-nodes-base.gotowebinar.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [GoToWebinar](https://www.goto.com/webinar) 账户，并确保拥有 [Developer Center](https://developer.goto.com/) 的访问权限。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务身份验证的更多信息，请参阅 [GoToWebinar API 文档](https://developer.goto.com/GoToWebinarV2)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- **Client ID**（客户端 ID）：创建 OAuth 客户端后提供。
- **Client Secret**（客户端密钥）：创建 OAuth 客户端后提供。

创建 OAuth 客户端的详细步骤，请参阅[创建 OAuth 客户端文档](https://developer.goto.com/guides/Get%20Started/02_HOW_createClient/)。从 n8n 复制 **OAuth Callback URL**（OAuth 回调 URL），将其用作 OAuth 客户端的 **Redirect URI**（重定向 URI）。完成客户端设置后，即可获得 Client ID 和 Client Secret。

