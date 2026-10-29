---
title: PayPal 凭据
description: PayPal 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 PayPal 的身份验证。
contentType:
- integration
- reference
nodeTitle: PayPal 凭据
originalFilePath: integrations/builtin/credentials/paypal.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/paypal
url: https://docs.n8n.io/integrations/builtin/credentials/paypal
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# PayPal 凭据 <a href="#paypal-credentials" id="paypal-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [PayPal](../app-nodes/n8n-nodes-base.paypal.md)
- [PayPal Trigger（触发器）](../trigger-nodes/n8n-nodes-base.paypaltrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [PayPal 开发者](https://developer.paypal.com/home)账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API client and secret（API 客户端与密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [PayPal API 文档](https://developer.paypal.com/api/rest/)。

## 使用 API 客户端与密钥 <a href="#using-api-client-and-secret" id="using-api-client-and-secret"></a>

配置此凭据需要：

- **Client ID**（客户端 ID）：创建应用时生成。
- **Secret**（密钥）：创建应用时生成。
- **Environment**（环境）：选择 **Live**（正式环境）或 **Sandbox**（沙盒）。

要生成 **Client ID** 和 **Secret**，登录 PayPal [开发者控制台](https://developer.paypal.com/dashboard/)，选择 **Apps & Credentials > Rest API apps > Create app**（应用与凭据 > REST API 应用 > 创建应用）。更多信息请参阅[获取客户端 ID 和客户端密钥](https://developer.paypal.com/api/rest/#link-getclientidandclientsecret)。


