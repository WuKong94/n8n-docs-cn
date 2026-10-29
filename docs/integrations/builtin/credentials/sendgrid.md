---
title: SendGrid 凭据
description: SendGrid 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 SendGrid 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: SendGrid 凭据
originalFilePath: integrations/builtin/credentials/sendgrid.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/sendgrid
url: https://docs.n8n.io/integrations/builtin/credentials/sendgrid
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# SendGrid 凭据 <a href="#sendgrid-credentials" id="sendgrid-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [SendGrid](../app-nodes/n8n-nodes-base.sendgrid.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [SendGrid API 文档](https://www.twilio.com/docs/sendgrid/api-reference)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个 [SendGrid](https://sendgrid.com) 账号，以及：

- 一个 **API Key（API 密钥）**

创建 API 密钥：

1. 在 Twilio SendGrid 应用中，进入 **Settings >** [**API Keys**](https://app.sendgrid.com/settings/api_keys)（设置 > API 密钥）。
2. 选择 **Create API Key**（创建 API 密钥）。
3. 为 API 密钥输入 **Name**（名称），例如 `n8n integration`。
4. 选择 **Full Access**（完全访问）。
5. 选择 **Create & View**（创建并查看）。
6. 复制密钥，填入 n8n 凭据。

更多信息请参阅[创建 API 密钥](https://www.twilio.com/docs/sendgrid/api-reference/api-keys/create-api-keys)。
