---
title: Gmail
description: Gmail Send Email 凭据文档。使用这些凭据在工作流自动化平台 n8n 中通过 Gmail 完成 Send Email 的身份验证。
contentType:
- integration
- reference
priority: high
nodeTitle: Gmail
originalFilePath: integrations/builtin/credentials/sendemail/gmail.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/sendemail/gmail
url: https://docs.n8n.io/integrations/builtin/credentials/send-email/gmail
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Gmail Send Email 凭据 <a href="#gmail-send-email-credentials" id="gmail-send-email-credentials"></a>

按照以下步骤，使用 Gmail 账户配置 Send Email 凭据。

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

执行以下说明前，必须先完成：

1. 为 Gmail 账户[启用两步验证](#enable-2-step-verification)。
2. [生成应用密码](#generate-an-app-password)。

### 启用两步验证 <a href="#enable-2-step-verification" id="enable-2-step-verification"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/email/gmail-two-step-verification.md" %}

### 生成应用密码 <a href="#generate-an-app-password" id="generate-an-app-password"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/email/gmail-app-password.md" %}

## 设置凭据 <a href="#set-up-the-credential" id="set-up-the-credential"></a>

使用 Gmail 设置 Send Email 凭据时：

1. 将 Gmail 邮箱地址填入 **User**（用户）。
2. 将上面生成的应用密码填入 **Password**（密码）。
3. 将 `smtp.gmail.com` 填入 **Host**（主机）。
4. 对于 **Port**（端口）：
    - 使用 SSL 或不确定应使用哪种方式时，保留默认值 `465`。
    - 使用 TLS 时，填写 `587`。
5. 开启 **SSL/TLS**。

> 译注：此步原文统一要求开启 SSL/TLS，但同版本 Send Email 凭据总览将端口 465 对应为开启 SSL/TLS，将端口 587 对应为关闭 SSL/TLS、使用 STARTTLS。若上一步选择 587，请按总览中的加密方式配置。

更多信息，请参阅[使用 POP 在其他邮件客户端中读取 Gmail 邮件](https://support.google.com/mail/answer/7104828?hl=en)中的出站邮件（SMTP）服务器设置。如果上述设置不适用，请联系邮件管理员。
