---
title: Outlook.com
description: Outlook.com IMAP 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Outlook.com IMAP 的身份验证。
contentType:
- integration
- reference
priority: high
nodeTitle: Outlook.com
originalFilePath: integrations/builtin/credentials/imap/outlook.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/imap/outlook
url: https://docs.n8n.io/integrations/builtin/credentials/imap/outlook
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


{% hint style="warning" %}
**功能可用范围**

Microsoft 已弃用 Exchange Online 和
Outlook.com 的 IMAP 基本身份验证，自 2022 年 10 月 1 日起生效。因此，IMAP 节点**无法连接到 Outlook.com 或
Microsoft 365 账户**。应用密码无法绕过这一
限制。

**请改用 [Microsoft Outlook 节点](../../app-nodes/n8n-nodes-base.microsoftoutlook.md)，
它使用 OAuth 2.0**，这是 Microsoft 目前对邮件访问要求的身份验证方式。

更多信息，请参阅 [Microsoft 的弃用公告](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-basic-authentication-exchange-online#what-we-are-changing)
。
{% endhint %}


# Outlook.com IMAP 凭据 <a href="#outlookcom-imap-credentials" id="outlookcom-imap-credentials"></a>

Microsoft 自 2022 年 10 月 1 日起弃用了 Exchange Online 和 Outlook.com 的基本身份验证，因此 n8n 不再支持通过 IMAP 访问 Outlook.com 和 Microsoft 365 账户。无法使用 IMAP 配合普通密码或应用密码连接 Outlook.com 或 Microsoft 365 账户。

如需替代接收邮件的 IMAP 触发器，请使用 [Microsoft Outlook Trigger 节点](../../trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger.md)，它支持 Message Received（收到邮件）事件。

对于常规 Microsoft Outlook 自动化，请使用 [Microsoft Outlook 节点](../../app-nodes/n8n-nodes-base.microsoftoutlook.md)，它采用 Microsoft 要求的 OAuth 2.0。

更多信息，请参阅 [Microsoft 的弃用公告](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-basic-authentication-exchange-online#what-we-are-changing)。
