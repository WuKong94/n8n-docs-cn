---
title: Send Email 凭据
description: Send Email 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Send Email 的身份验证。
contentType:
- integration
- reference
priority: high
nodeTitle: Send Email
originalFilePath: integrations/builtin/credentials/sendemail/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/sendemail
url: https://docs.n8n.io/integrations/builtin/credentials/send-email
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Send Email 凭据 <a href="#send-email-credentials" id="send-email-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Send Email](../../core-nodes/n8n-nodes-base.sendemail.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 在支持 SMTP 的服务上创建邮箱账户。
- 某些邮件提供商要求启用或设置出站 SMTP，或生成应用密码。请查阅提供商文档，确认是否还需完成其他步骤。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- SMTP 账户

## 相关资源 <a href="#related-resources" id="related-resources"></a>

Simple Mail Transfer Protocol（SMTP，简单邮件传输协议）是用于发送和接收电子邮件的标准协议。大多数邮件提供商都提供通过 SMTP 设置其服务的说明，请参阅提供商的 SMTP 说明。

## 使用 SMTP 账户 <a href="#using-smtp-account" id="using-smtp-account"></a>

配置此凭据需要：

- **User**（用户）邮箱地址
- **Password**（密码）：可以是用户密码或应用密码。请参阅邮件提供商的文档。
- **Host**（主机）：邮件提供商的 SMTP 主机地址，通常采用 `smtp.<provider>.com` 格式。请向提供商确认。
- **Port**（端口）号：端口取决于加密方式：
  - 端口 `465` 用于 SSL/TLS（隐式加密）
  - 端口 `587` 用于 STARTTLS（显式加密）
  - 端口 `25` 用于不加密的连接（不推荐）
    请向邮件提供商确认具体要求。
- **SSL/TLS**：此开关控制加密方式：
  - 端口 `465` 应**开启**，使用隐式 SSL/TLS 加密
  - 端口 `587` 应**关闭**，使用 STARTTLS 显式加密
  - 端口 `25` 应**关闭**，不使用加密
- **Disable STARTTLS**（禁用 STARTTLS）：禁用 SSL/TLS 时，SMTP 服务器仍可尝试[使用 STARTTLS 升级 TCP 连接](https://en.wikipedia.org/wiki/Opportunistic_TLS)。开启此选项会阻止该行为。
- **Client Host Name**（客户端主机名）：用于向服务器标识客户端。Gmail、Outlook.com 或 Yahoo 可能不要求填写；除非邮件提供商或管理员明确要求，否则请留空。如果必须提供，请使用完全限定域名（FQDN），例如 `mail.yourdomain.com`，避免使用 `localhost` 等通用值。

### 提供商说明 <a href="#provider-instructions" id="provider-instructions"></a>

请参阅以下常见邮件提供商的快速入门指南。

#### Gmail <a href="#gmail" id="gmail"></a>

请参阅 [Gmail](gmail.md)。

#### Outlook.com <a href="#outlookcom" id="outlookcom"></a>

请参阅 [Outlook.com](outlook.md)。

#### Yahoo <a href="#yahoo" id="yahoo"></a>

请参阅 [Yahoo](yahoo.md)。

### 未列出我使用的提供商 <a href="#my-provider-isnt-listed" id="my-provider-isnt-listed"></a>

如果此处未列出你的邮件提供商，请搜索 `SMTP settings` 以查找其说明。这些说明也可能与 `IMAP settings` 或 `POP settings` 一并提供。
