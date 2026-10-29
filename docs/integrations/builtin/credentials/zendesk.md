---
title: Zendesk 凭据
description: Zendesk 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Zendesk 的身份验证。
contentType:
- integration
- reference
nodeTitle: Zendesk 凭据
originalFilePath: integrations/builtin/credentials/zendesk.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/zendesk
url: https://docs.n8n.io/integrations/builtin/credentials/zendesk
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Zendesk 凭据 <a href="#zendesk-credentials" id="zendesk-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Zendesk](../app-nodes/n8n-nodes-base.zendesk.md)
- [Zendesk Trigger（触发器）](../trigger-nodes/n8n-nodes-base.zendesktrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Zendesk](https://zendesk.com/) 账号。
- 使用 API 令牌身份验证时，请在 Admin Center（管理中心）的 **Apps and integrations > APIs > Zendesk APIs**（应用与集成 > API > Zendesk API）中启用 API 令牌访问。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Zendesk API 文档](https://developer.zendesk.com/api-reference/)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要：

- 你的 **Subdomain**（子域名）：Zendesk 子域名是 URL 中 `https://` 和 `.zendesk.com` 之间的部分。例如，Zendesk URL 为 `https://n8n-example.zendesk.com/agent/dashboard` 时，子域名为 `n8n-example`。
- 一个 **Email（电子邮件）** 地址：输入用于登录 Zendesk 的邮箱地址。
- 一个 **API Token**（API 令牌）：在 **Apps and integrations > APIs > Zendesk API**（应用与集成 > API > Zendesk API）中生成 API 令牌。更多信息请参阅 [API 令牌](https://developer.zendesk.com/api-reference/introduction/security-and-auth/#api-token)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- 一个 **Client ID**（客户端 ID）：创建新的 OAuth 客户端时生成。
- 一个 **Client Secret**（客户端密钥）：创建新的 OAuth 客户端时生成。
- 你的 **Subdomain**（子域名）：Zendesk 子域名是 URL 中 `https://` 和 `.zendesk.com` 之间的部分。例如，Zendesk URL 为 `https://n8n-example.zendesk.com/agent/dashboard` 时，子域名为 `n8n-example`。

要创建新的 OAuth 客户端，请进入 **Apps and integrations > APIs > Zendesk API > OAuth Clients**（应用与集成 > API > Zendesk API > OAuth 客户端）。

使用以下设置：

 - 从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），将其填入 OAuth 客户端的 **Redirect URL**（重定向 URL）。
 - 复制 Zendesk 客户端的 **Unique identifier**（唯一标识符），填入 n8n 的 **Client ID**（客户端 ID）。
 - 从 Zendesk 复制 **Secret**（密钥），填入 n8n 的 **Client Secret**（客户端密钥）。
 
 
 更多信息请参阅[在 Zendesk 中注册应用](https://support.zendesk.com/hc/en-us/articles/4408845965210-Using-OAuth-authentication-with-your-application#topic_s21_lfs_qk)。

