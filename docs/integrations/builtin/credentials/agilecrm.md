---
title: Agile CRM 凭据
description: Agile CRM 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Agile CRM 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Agile CRM 凭据
originalFilePath: integrations/builtin/credentials/agilecrm.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/agilecrm
url: https://docs.n8n.io/integrations/builtin/credentials/agilecrm
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Agile CRM 凭据 <a href="#agile-crm-credentials" id="agile-crm-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Agile CRM](../app-nodes/n8n-nodes-base.agilecrm.md)


## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Agile CRM](https://www.agilecrm.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关如何使用该服务的更多信息，请参阅 [Agile CRM API 文档](https://www.agilecrm.com/api)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个已在 AgileCRM 注册的 **Email Address（电子邮件地址）**
- 一个 REST **API Key（API 密钥）**：通过 **Admin Settings > Developers & API（管理设置 > 开发者与 API）>** [**REST API key（REST API 密钥）**](https://github.com/agilecrm/rest-api?tab=readme-ov-file#api-key)获取 Agile CRM API 密钥。
- 一个 Agile CRM **Subdomain（子域名）**，例如 `n8n`
