---
title: IMAP 凭据
description: IMAP 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 IMAP 的身份验证。
contentType:
- integration
- reference
priority: high
nodeTitle: IMAP
originalFilePath: integrations/builtin/credentials/imap/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/imap
url: https://docs.n8n.io/integrations/builtin/credentials/imap
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# IMAP 凭据 <a href="#imap-credentials" id="imap-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [IMAP Email（邮件）](../../core-nodes/n8n-nodes-base.emailimap.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在支持 IMAP 的服务上创建邮箱账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- 用户账户

## 相关资源 <a href="#related-resources" id="related-resources"></a>

Internet Message Access Protocol（IMAP，互联网消息访问协议）是接收电子邮件的标准协议。大多数邮件提供商都提供通过 IMAP 设置其服务的说明，请参阅提供商的 IMAP 说明。

## 使用用户账户 <a href="#using-user-account" id="using-user-account"></a>

配置此凭据需要：

- **User**（用户）名：要从中获取邮件的邮箱地址。
- **Password**（密码）：登录邮箱所用的密码或应用密码。邮件提供商会说明应使用账户密码还是生成应用密码。
- **Host**（主机）：邮件提供商的 IMAP 主机地址，通常采用 `imap.<provider>.com` 格式。请向提供商确认。
- **Port**（端口）号：默认为 `993`。除非提供商或邮件管理员要求使用其他端口，否则请使用此端口。

选择是否使用 **SSL/TLS**，以及是否 **Allow Self-Signed Certificates**（允许自签名证书）。

### 提供商说明 <a href="#provider-instructions" id="provider-instructions"></a>

请参阅以下常见邮件提供商的快速入门指南。

#### Gmail <a href="#gmail" id="gmail"></a>

请参阅 [Gmail](gmail.md)。

#### Outlook.com <a href="#outlookcom" id="outlookcom"></a>

请参阅 [Outlook.com](outlook.md)。

#### Yahoo <a href="#yahoo" id="yahoo"></a>

请参阅 [Yahoo](yahoo.md)。

### 未列出我使用的提供商 <a href="#my-provider-isnt-listed" id="my-provider-isnt-listed"></a>

如果此处未列出你的邮件提供商，请搜索其 `IMAP settings` 或 `IMAP instructions`。
