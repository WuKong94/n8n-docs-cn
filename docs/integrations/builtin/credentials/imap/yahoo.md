---
title: Yahoo
description: Yahoo IMAP 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Yahoo IMAP 的身份验证。
contentType:
- integration
- reference
priority: high
nodeTitle: Yahoo
originalFilePath: integrations/builtin/credentials/imap/yahoo.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/imap/yahoo
url: https://docs.n8n.io/integrations/builtin/credentials/imap/yahoo
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Yahoo IMAP 凭据 <a href="#yahoo-imap-credentials" id="yahoo-imap-credentials"></a>

按照以下步骤，使用 Yahoo 账户配置 IMAP 凭据。

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

执行以下说明前，必须先生成应用密码：

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/email/yahoo-app-password.md" %}

## 设置凭据 <a href="#set-up-the-credential" id="set-up-the-credential"></a>

使用 Yahoo Mail 账户设置 IMAP 凭据时，请采用以下设置：

1. 将 Yahoo 邮箱地址填入 **User**（用户）。
2. 将上面生成的应用密码填入 **Password**（密码）。
3. 将 `imap.mail.yahoo.com` 填入 **Host**（主机）。
4. **Port**（端口）保留默认值 `993`。如果此端口无法使用，请联系邮件管理员。
5. 开启 **SSL/TLS**。
6. 请向邮件管理员确认是否 **Allow Self-Signed Certificates**（允许自签名证书）。

更多信息，请参阅[为 Yahoo 邮箱账户设置 IMAP](https://help.yahoo.com/kb/sln4075.html)。
