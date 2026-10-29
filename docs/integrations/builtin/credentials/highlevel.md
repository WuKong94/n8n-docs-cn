---
title: HighLevel 凭据
description: HighLevel 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 HighLevel 的身份验证。
contentType:
- integration
- reference
nodeTitle: HighLevel 凭据
originalFilePath: integrations/builtin/credentials/highlevel.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/highlevel
url: https://docs.n8n.io/integrations/builtin/credentials/highlevel
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# HighLevel 凭据 <a href="#highlevel-credentials" id="highlevel-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [HighLevel 节点](../app-nodes/n8n-nodes-base.highlevel.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [HighLevel 开发者](https://marketplace.gohighlevel.com/)账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）：用于 API v1。
- OAuth2：用于 API v2。

{% hint style="warning" %}
**功能可用范围**

HighLevel 已弃用 API v1.0，并停止维护。新凭据请使用 OAuth2 配置。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [HighLevel API 2.0 文档](https://highlevel.stoplight.io/docs/integrations/0443d7d1a4bd0-overview)。

现有 API v1.0 集成的说明，请参阅 [HighLevel API 1.0 文档](https://help.gohighlevel.com/support/solutions/articles/48001060529-highlevel-api)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key**（API 密钥）：获取 API 密钥的方法，请参阅 [HighLevel API 1.0 欢迎文档](https://help.gohighlevel.com/support/solutions/articles/48001060529-highlevel-api)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- 一个 **Client ID（客户端 ID）**
- 一个 **Client Secret（客户端密钥）**

要生成这两项，请在 **My Apps > Create App**（我的应用 > 创建应用）中创建应用，并使用以下设置：

1. 将 **Distribution Type**（分发类型）设为 **Sub-Account**（子账户）。
2. 添加以下 **Scopes**（作用域）：
    - `locations.readonly`
    - `contacts.readonly`
    - `contacts.write`
    - `opportunities.readonly`
    - `opportunities.write`
    - `users.readonly`
3. 从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），将其添加为 HighLevel 应用中的 **Redirect URL**（重定向 URL）。
4. 从 HighLevel 复制 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥），添加到 n8n 凭据。
5. 将上方添加的相同作用域以空格分隔的列表形式，添加到 n8n 凭据。例如：

    ```locations.readonly contacts.readonly contacts.write opportunities.readonly opportunities.write users.readonly```

更多详情请参阅 HighLevel 的 [API 授权文档](https://highlevel.stoplight.io/docs/integrations/a04191c0fabf9-authorization)。可用作用域的更多信息，请参阅 HighLevel 的 [API 作用域文档](https://highlevel.stoplight.io/docs/integrations/vcctp9t1w8hja-scopes)。

