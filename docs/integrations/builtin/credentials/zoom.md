---
title: Zoom 凭据
description: Zoom 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Zoom 的身份验证。
contentType:
- integration
- reference
nodeTitle: Zoom 凭据
originalFilePath: integrations/builtin/credentials/zoom.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/zoom
url: https://docs.n8n.io/integrations/builtin/credentials/zoom
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Zoom 凭据 <a href="#zoom-credentials" id="zoom-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Zoom](../app-nodes/n8n-nodes-base.zoom.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建 [Zoom](https://zoom.us/) 账户，账户必须具有以下任一权限：

- 账户所有者
- 账户管理员
- Zoom for developers（开发者）角色

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API JWT token（API JWT 令牌）
- OAuth2

{% hint style="warning" %}
**功能可用范围**

Zoom 于 2023 年 6 月移除了对 JWT 访问令牌的支持。所有新凭据都必须使用 OAuth2。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Zoom API 文档](https://developers.zoom.us/docs/api/)。

## 使用 API JWT 令牌 <a href="#using-api-jwt-token" id="using-api-jwt-token"></a>

此身份验证方式已被 Zoom 完全弃用，请勿使用它创建新凭据。

配置此凭据需要：

- **JWT token**（JWT 令牌）：如需创建 JWT 令牌，请在 [Zoom App Marketplace](https://marketplace.zoom.us/) 中创建新的 JWT 应用。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- **Client ID**（客户端 ID）：在 Zoom App Marketplace 创建 OAuth 应用时生成。
- **Client Secret**（客户端密钥）：创建 OAuth 应用时生成。

如需生成 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥），请[创建 OAuth 应用](https://developers.zoom.us/docs/integrations/create/)。

为 OAuth 应用使用以下设置：

- 将 **Select how the app is managed**（选择应用管理方式）设为 **User-managed app**（用户管理的应用）。
- 从 n8n 复制 **OAuth Callback URL**（OAuth 回调 URL），填入 Zoom 的 **OAuth Redirect URL**（OAuth 重定向 URL）。
- 如果 n8n 凭据显示 **Whitelist URL**（白名单 URL），也将该 URL 填入 **OAuth Redirect URL**（OAuth 重定向 URL）。
- 在 **Scopes**（作用域）中输入计划使用的作用域。如需使用 [Zoom](../app-nodes/n8n-nodes-base.zoom.md) 节点的全部功能，请选择：
    - `meeting:read`
    - `meeting:write`
    - 会议作用域的更多信息，请参阅 [OAuth scopes | Meeting scopes（OAuth 作用域 | 会议作用域）](https://developers.zoom.us/docs/integrations/oauth-scopes/#meeting-scopes)。
- 复制 Zoom 应用提供的 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥），填入 n8n 凭据。
