---
title: Mailchimp 凭据
description: Mailchimp 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Mailchimp 的身份验证。
contentType:
- integration
- reference
nodeTitle: Mailchimp 凭据
originalFilePath: integrations/builtin/credentials/mailchimp.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/mailchimp
url: https://docs.n8n.io/integrations/builtin/credentials/mailchimp
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Mailchimp 凭据 <a href="#mailchimp-credentials" id="mailchimp-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Mailchimp](../app-nodes/n8n-nodes-base.mailchimp.md)
- [Mailchimp Trigger（触发器）](../trigger-nodes/n8n-nodes-base.mailchimptrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Mailchimp](https://www.mailchimp.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）
- OAuth2

如何选择验证方式，请参阅[选择身份验证方式](#selecting-an-authentication-method)。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Mailchimp API 文档](https://mailchimp.com/developer/marketing/api/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **API Key**（API 密钥）：在 Mailchimp 账户的 [API 密钥部分](https://us1.admin.mailchimp.com/account/api/)中生成。详细步骤请参阅 [Mailchimp 生成 API 密钥文档](https://mailchimp.com/developer/marketing/build/get-started/generate-your-api-key)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果需要从头配置 OAuth2，请[注册应用](https://mailchimp.com/developer/marketing/build/start-developing/set-up-an-oauth-app)。更多信息请参阅 [Mailchimp OAuth2 文档](https://mailchimp.com/developer/marketing/api-concepts/authentication/oauth-2)。

## 选择身份验证方式 <a href="#selecting-an-authentication-method" id="selecting-an-authentication-method"></a>

如果只访问自己 Mailchimp 账户的数据，Mailchimp 建议使用 API 密钥：

> 如果编写的代码将 _你的_ 应用数据与 _你的_ Mailchimp 账户数据紧密结合，请使用 API 密钥。如果需要访问 _其他人_ 的 Mailchimp 账户数据，则应使用 OAuth 2（[来源](https://mailchimp.com/developer/marketing/api-concepts/authentication)）。

