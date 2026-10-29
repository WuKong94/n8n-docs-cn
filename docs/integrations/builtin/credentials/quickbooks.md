---
title: QuickBooks 凭据
description: QuickBooks 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 QuickBooks 的身份验证。
contentType:
- integration
- reference
nodeTitle: QuickBooks 凭据
originalFilePath: integrations/builtin/credentials/quickbooks.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/quickbooks
url: https://docs.n8n.io/integrations/builtin/credentials/quickbooks
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# QuickBooks 凭据 <a href="#quickbooks-credentials" id="quickbooks-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [QuickBooks](../app-nodes/n8n-nodes-base.quickbooks.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建 [Intuit 开发者](https://developer.intuit.com/)账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Intuit API 文档](https://developer.intuit.com/app/developer/qbo/docs/develop)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- **Client ID**（客户端 ID）：创建应用时生成。
- 一个 **Client Secret**（客户端密钥）：创建应用时生成。
- 一个 **Environment**（环境）：选择此凭据访问 **Production**（生产）还是 **Sandbox**（沙箱）环境。

要生成 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥），请[创建应用](https://developer.intuit.com/app/developer/qbo/docs/get-started/start-developing-your-app#create-an-app)。

创建应用时使用以下设置：

- 为应用选择适当的作用域。更多信息请参阅[了解作用域](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)。
- 将 n8n 的 **OAuth Redirect URL**（OAuth 重定向 URL）填入应用 **Development > Keys & OAuth**（开发 > 密钥与 OAuth）部分的 **Redirect URI**（重定向 URI）。
- 从应用的 **Development > Keys & OAuth**（开发 > 密钥与 OAuth）部分复制 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥），填入 n8n。更多信息请参阅[获取应用的客户端 ID 和客户端密钥](https://developer.intuit.com/app/developer/qbo/docs/get-started/get-client-id-and-client-secret)。

完整流程的更多信息，请参阅 Intuit 的[设置 OAuth 2.0 文档](https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0)。

{% hint style="info" %}
**环境选择**

如果从头创建新应用，请先使用 **Sandbox**（沙箱）环境。生产应用必须满足 Intuit 的所有要求，更多信息请参阅 Intuit 的[发布应用文档](https://developer.intuit.com/app/developer/qbo/docs/go-live/publish-app)。
{% endhint %}
