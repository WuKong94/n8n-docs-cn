---
title: Chargebee 凭据
description: Chargebee 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Chargebee 的身份验证。
contentType:
- integration
- reference
nodeTitle: Chargebee 凭据
originalFilePath: integrations/builtin/credentials/chargebee.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/chargebee
url: https://docs.n8n.io/integrations/builtin/credentials/chargebee
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Chargebee 凭据 <a href="#chargebee-credentials" id="chargebee-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Chargebee](../app-nodes/n8n-nodes-base.chargebee.md)
- [Chargebee Trigger（触发器）](../trigger-nodes/n8n-nodes-base.chargebeetrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Chargebee](https://www.chargebee.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Chargebee API 文档](https://apidocs.chargebee.com/docs/api/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **Account Name（账号名称）**：即 Chargebee 站点名称或子域名。例如，完整站点名称为 `https://n8n.chargebee.com` 时，Account Name 为 `n8n`。
- 一个 **API Key（API 密钥）**：生成步骤请参阅 [Chargebee 的创建 API 密钥文档](https://www.chargebee.com/docs/api_keys.html#creating-an-api-key)。

如需进一步了解，请参阅其通用 [API 身份验证文档](https://apidocs.chargebee.com/docs/api/auth?lang=curl)。

