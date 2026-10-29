---
title: Mailgun 凭据
description: Mailgun 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Mailgun 的身份验证。
contentType:
- integration
- reference
nodeTitle: Mailgun 凭据
originalFilePath: integrations/builtin/credentials/mailgun.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/mailgun
url: https://docs.n8n.io/integrations/builtin/credentials/mailgun
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Mailgun 凭据 <a href="#mailgun-credentials" id="mailgun-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Mailgun](../app-nodes/n8n-nodes-base.mailgun.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Mailgun](https://www.mailgun.com/) 账号。
- 在 Mailgun 中[添加并验证域名](https://help.mailgun.com/hc/en-us/articles/360026833053-Domain-Verification-Setup-Guide)，或使用提供的沙盒域名测试。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Mailgun API 文档](https://documentation.mailgun.com/docs/mailgun/api-reference/api-overview)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **API Domain**（API 域名）：如果 Mailgun 账户位于欧洲，选择 **api.eu.mailgun.net**；否则选择 **api.mailgun.net**。更多信息请参阅 [Mailgun 基础 URL](https://documentation.mailgun.com/docs/mailgun/api-reference/api-overview#base-url)。
- **Email Domain**（邮件域名）：输入当前使用的邮件发送域名。如果有多个发送域名，请参阅[使用多个邮件域名](#working-with-multiple-email-domains)。
- **API Key**（API 密钥）：在 **Settings > API Keys**（设置 > API 密钥）中查看。详细步骤请参阅 [Mailgun API 身份验证文档](https://documentation.mailgun.com/docs/mailgun/api-reference/mg-auth)。

## 使用多个邮件域名 <a href="#working-with-multiple-email-domains" id="working-with-multiple-email-domains"></a>

如果 Mailgun 账户包含多个发送域名，请为每个需要使用的邮件域名单独创建凭据。
