---
title: ConvertKit 凭据
description: ConvertKit 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 ConvertKit 的身份验证。
contentType:
- integration
- reference
nodeTitle: ConvertKit 凭据
originalFilePath: integrations/builtin/credentials/convertkit.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/convertkit
url: https://docs.n8n.io/integrations/builtin/credentials/convertkit
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# ConvertKit 凭据 <a href="#convertkit-credentials" id="convertkit-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [ConvertKit](../app-nodes/n8n-nodes-base.convertkit.md)
- [ConvertKit Trigger（触发器）](../trigger-nodes/n8n-nodes-base.convertkittrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [ConvertKit](https://convertkit.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [ConvertKit API 文档](https://developers.convertkit.com/#overview)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Secret（API 密钥）**：在 [**Account Settings > Advanced（账号设置 > 高级）**](https://app.convertkit.com/account_settings/advanced_settings)中获取 ConvertKit API 密钥，将其填入 n8n 的 **API Secret** 字段。
