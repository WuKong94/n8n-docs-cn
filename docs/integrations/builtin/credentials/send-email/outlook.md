---
title: Outlook.com
description: Outlook.com Send Email 凭据文档。使用这些凭据在工作流自动化平台 n8n 中通过 Outlook.com 完成 Send
  Email 的身份验证。
contentType:
- integration
- reference
priority: high
nodeTitle: Outlook.com
originalFilePath: integrations/builtin/credentials/sendemail/outlook.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/sendemail/outlook
url: https://docs.n8n.io/integrations/builtin/credentials/send-email/outlook
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->



# Outlook.com Send Email 凭据 <a href="#outlookcom-send-email-credentials" id="outlookcom-send-email-credentials"></a>

{% hint style="warning" %}
**功能可用范围**

Microsoft 已弃用 Exchange Online 和 Outlook.com 中 SMTP 的基本身份验证及应用密码。因此，Send Email 节点**无法通过用户名/密码或应用密码身份验证连接 Outlook.com 或 Microsoft 365 账户**。

**要从 Outlook.com 或 Microsoft 365 账户发送邮件，请使用 [Microsoft Outlook 节点](../../app-nodes/n8n-nodes-base.microsoftoutlook.md)，它采用 Microsoft 要求的 OAuth 2.0。**

更多信息，请参阅 [Microsoft 的弃用公告](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-basic-authentication-exchange-online#what-we-are-changing)。
{% endhint %}
