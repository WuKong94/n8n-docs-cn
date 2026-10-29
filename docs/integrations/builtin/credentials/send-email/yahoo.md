---
title: Yahoo
description: Yahoo Send Email 凭据文档。使用这些凭据在工作流自动化平台 n8n 中通过 Yahoo 完成 Send Email 的身份验证。
contentType:
- integration
- reference
priority: high
nodeTitle: Yahoo
originalFilePath: integrations/builtin/credentials/sendemail/yahoo.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/sendemail/yahoo
url: https://docs.n8n.io/integrations/builtin/credentials/send-email/yahoo
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Yahoo Send Email 凭据 <a href="#yahoo-send-email-credentials" id="yahoo-send-email-credentials"></a>

按照以下步骤，使用 Yahoo 账户配置 Send Email 凭据。

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

执行以下说明前，必须先生成应用密码：

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/email/yahoo-app-password.md" %}

## 设置凭据 <a href="#set-up-the-credential" id="set-up-the-credential"></a>

使用 Yahoo Mail 配置 Send Email 凭据时：

1. 将 Yahoo 邮箱地址填入 **User**（用户）。
2. 将上面生成的应用密码填入 **Password**（密码）。
3. 将 `smtp.mail.yahoo.com` 填入 **Host**（主机）。
4. 对于 **Port**（端口）：
    - 使用 SSL 或不确定应使用哪种方式时，保留默认值 `465`。
    - 使用 TLS 时，填写 `587`。
5. 开启 **SSL/TLS**。

> 译注：此步原文统一要求开启 SSL/TLS，但同版本 Send Email 凭据总览将端口 465 对应为开启 SSL/TLS，将端口 587 对应为关闭 SSL/TLS、使用 STARTTLS。若上一步选择 587，请按总览中的加密方式配置。

更多信息，请参阅 [Yahoo Mail 的 IMAP 服务器设置](https://help.yahoo.com/kb/sln4075.html)。如果上述设置不适用，请联系邮件管理员。
