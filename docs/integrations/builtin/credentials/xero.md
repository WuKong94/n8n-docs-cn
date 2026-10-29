---
title: Xero 凭据
description: Xero 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Xero 的身份验证。
contentType:
- integration
- reference
nodeTitle: Xero 凭据
originalFilePath: integrations/builtin/credentials/xero.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/xero
url: https://docs.n8n.io/integrations/builtin/credentials/xero
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Xero 凭据 <a href="#xero-credentials" id="xero-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Xero](../app-nodes/n8n-nodes-base.xero.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Xero](https://www.xero.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Xero API 文档](https://developer.xero.com/documentation/api/accounting/overview)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- 一个 **Client ID**（客户端 ID）：为自定义连接创建新应用时生成。
- 一个 **Client Secret**（客户端密钥）：为自定义连接创建新应用时生成。

要生成 Client ID（客户端 ID）和 Client Secret（客户端密钥），请在 Xero 开发者门户的 [**My Apps**（我的应用）](https://developer.xero.com/app/manage)中[创建 OAuth2 自定义连接应用](https://developer.xero.com/documentation/guides/oauth2/custom-connections/)。

为应用采用以下设置：

{% hint style="info" %}
**Xero 应用名称**

Xero 不支持在 Xero Developer Centre 中使用名称包含 `n8n` 的应用实例。
{% endhint %}

- 将 **Integration Type**（集成类型）设为 **Web app**（网页应用）。
- 在 **Company or Application URL**（公司或应用 URL）中输入 n8n 服务器或反向代理地址的 URL。例如，云用户可使用 `https://your-username.app.n8n.cloud/`。
- 从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），将其添加为应用中的 **OAuth 2.0 redirect URI**（OAuth 2.0 重定向 URI）。
- 为应用选择适当的 **scopes**（作用域）。更多信息请参阅 [OAuth2 作用域](https://developer.xero.com/documentation/guides/oauth2/scopes/)。
    - 要使用 [Xero](../app-nodes/n8n-nodes-base.xero.md) 节点的全部功能，请添加 `accounting.contacts` 和 `accounting.transactions` 作用域。

更多信息请参阅 Xero 的 [OAuth 自定义连接](https://developer.xero.com/documentation/guides/oauth2/custom-connections)文档。
