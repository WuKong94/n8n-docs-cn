---
title: Mailjet 凭据
description: Mailjet 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Mailjet 的身份验证。
contentType:
- integration
- reference
nodeTitle: Mailjet 凭据
originalFilePath: integrations/builtin/credentials/mailjet.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/mailjet
url: https://docs.n8n.io/integrations/builtin/credentials/mailjet
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Mailjet 凭据 <a href="#mailjet-credentials" id="mailjet-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Mailjet](../app-nodes/n8n-nodes-base.mailjet.md)
- [Mailjet Trigger（触发器）](../trigger-nodes/n8n-nodes-base.mailjettrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Mailjet](https://www.mailjet.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Email API key（邮件 API 密钥）：用于 Mailjet 的 Email API。
- SMS token（短信令牌）：用于 Mailjet 的 SMS API。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

各服务的更多信息，请参阅 [Mailjet Email API 文档](https://dev.mailjet.com/email/guides/)和 [Mailjet SMS API 文档](https://dev.mailjet.com/guides-sms/)。

## 使用 Email API 密钥 <a href="#using-email-api-key" id="using-email-api-key"></a>

配置此凭据需要：

- 一个 **API Key**（API 密钥）：在 Mailjet 的 [API Key Management（API 密钥管理）](https://app.mailjet.com/signin)页面查看和生成 API 密钥。
- 一个 **Secret Key**（密钥）：在 Mailjet 的 [API Key Management（API 密钥管理）](https://app.mailjet.com/signin)页面查看 API Secret Key（API 密钥对应的秘密密钥）。
- _可选：_选择是否为通过此凭据发出的调用启用 **Sandbox Mode**（沙箱模式）。开启后，所有 API 调用都使用沙箱模式：API 仍会验证载荷，但不会实际投递消息，便于在不真正发送消息的情况下排查载荷错误。更多信息请参阅 Mailjet 的[沙箱模式文档](https://dev.mailjet.com/email/guides/send-api-v31/#sandbox-mode)。

此凭据可使用以下任意一种：

- Mailjet 的主 API 密钥及对应的秘密密钥
- 子账户的 API 密钥及对应的秘密密钥

创建更多 API 密钥的详细步骤，请参阅 Mailjet 的[如何创建子账户或附加 API 密钥文档](https://documentation.mailjet.com/hc/en-us/articles/360042561974-How-to-create-a-subaccount-or-additional-API-Key)。Mailjet 子账户的用途和适用场景，请参阅[什么是子账户，有何帮助？](https://documentation.mailjet.com/hc/en-us/articles/360042561854-What-are-subaccounts-and-how-does-it-help-me)

## 使用 SMS 令牌 <a href="#using-sms-token" id="using-sms-token"></a>

配置此凭据需要：

- 一个访问 **Token**（令牌）：在 Mailjet 的 [SMS Dashboard（短信控制台）](https://app.mailjet.com/sms)中生成新令牌。

