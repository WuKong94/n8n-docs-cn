---
title: Gmail
description: Gmail IMAP 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Gmail IMAP 的身份验证。
contentType:
- integration
- reference
priority: high
nodeTitle: Gmail
originalFilePath: integrations/builtin/credentials/imap/gmail.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/imap/gmail
url: https://docs.n8n.io/integrations/builtin/credentials/imap/gmail
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Gmail IMAP 凭据 <a href="#gmail-imap-credentials" id="gmail-imap-credentials"></a>

按照以下步骤，使用 Gmail 账户配置 IMAP 凭据。

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

执行以下说明前，必须先完成：

1. 为 Gmail 账户[启用两步验证](#enable-2-step-verification)。
2. [生成应用密码](#generate-an-app-password)。

### 启用两步验证 <a href="#enable-2-step-verification" id="enable-2-step-verification"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/email/gmail-two-step-verification.md" %}

### 生成应用密码 <a href="#generate-an-app-password" id="generate-an-app-password"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/email/gmail-app-password.md" %}

## 设置凭据 <a href="#set-up-the-credential" id="set-up-the-credential"></a>

使用 Gmail 账户设置 IMAP 凭据时，请采用以下设置：

1. 将 Gmail 邮箱地址填入 **User**（用户）。
2. 将上面生成的应用密码填入 **Password**（密码）。
3. 将 `imap.gmail.com` 填入 **Host**（主机）。
4. **Port**（端口）保留默认端口号 `993`。如果此端口无法使用，请联系邮件管理员。
5. 开启 **SSL/TLS**。
6. 请向邮件管理员确认是否 **Allow Self-Signed Certificates**（允许自签名证书）。

更多信息，请参阅[将 Gmail 添加到其他客户端](https://support.google.com/mail/answer/7126229?hl=en)。个人 Google 账户始终启用 IMAP 访问，Google 已于 2025 年 1 月移除 **Enable IMAP**（启用 IMAP）/ **Disable IMAP**（禁用 IMAP）开关。如果使用 Google Workspace 账户且 IMAP 无法工作，请向邮件管理员确认是否允许你的账户访问 IMAP。
