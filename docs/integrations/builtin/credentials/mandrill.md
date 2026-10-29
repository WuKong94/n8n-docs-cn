---
title: Mandrill 凭据
description: Mandrill 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Mandrill 的身份验证。
contentType:
- integration
- reference
nodeTitle: Mandrill 凭据
originalFilePath: integrations/builtin/credentials/mandrill.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/mandrill
url: https://docs.n8n.io/integrations/builtin/credentials/mandrill
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Mandrill 凭据 <a href="#mandrill-credentials" id="mandrill-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Mandrill](../app-nodes/n8n-nodes-base.mandrill.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建 Mailchimp [事务性邮件账户](https://mailchimp.com/features/transactional-email-infrastructure/)。
- 使用 Mailchimp 账户登录 [Mandrill](https://mandrillapp.com/login/)。

如果已经拥有 Standard 或更高级别的 Mailchimp 账户，请在该账户中启用 [Transactional Emails](https://mailchimp.com/help/add-or-remove-transactional-email)（事务性邮件），以使用 Mandrill。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Mailchimp Transactional API 文档](https://mailchimp.com/developer/transactional/api/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **API Key**（API 密钥）：在 Mandrill 的[设置](https://mandrillapp.com/settings)中生成。详细步骤请参阅 Mailchimp 的[生成 API 密钥文档](https://mailchimp.com/developer/transactional/guides/quick-start/#generate-your-api-key)。

