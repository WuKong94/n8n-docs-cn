---
title: MailerLite 凭据
description: MailerLite 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 MailerLite 的身份验证。
contentType:
- integration
- reference
nodeTitle: MailerLite 凭据
originalFilePath: integrations/builtin/credentials/mailerlite.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/mailerlite
url: https://docs.n8n.io/integrations/builtin/credentials/mailerlite
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MailerLite 凭据 <a href="#mailerlite-credentials" id="mailerlite-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [MailerLite](../app-nodes/n8n-nodes-base.mailerlite.md)
- [MailerLite Trigger（触发器）](../trigger-nodes/n8n-nodes-base.mailerlitetrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [MailerLite](https://www.mailerlite.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [MailerLite API 文档](https://developers.mailerlite.com/docs/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**：从 **Integrations（集成）** 菜单生成密钥。详细说明请参阅 [API 身份验证文档](https://developers.mailerlite.com/docs/#authentication)。

如果 API 密钥用于 MailerLite Classic 账号，而非新版 MailerLite，请启用 **Classic API（经典版 API）** 开关。

{% hint style="info" %}
大多数新建的 MailerLite 账号和所有免费账号应禁用 **Classic API（经典版 API）** 开关。你可以查看[正在使用哪个版本的 MailerLite](https://www.mailerlite.com/help/which-version-of-mailerlite-am-i-using)，并通过 [MailerLite 常见问题](https://www.mailerlite.com/help/new-mailerlite-faq)进一步了解两个版本的区别。
{% endhint %}
