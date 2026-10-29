---
title: Mindee 凭据
description: Mindee 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Mindee 的身份验证。
contentType:
- integration
- reference
nodeTitle: Mindee 凭据
originalFilePath: integrations/builtin/credentials/mindee.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/mindee
url: https://docs.n8n.io/integrations/builtin/credentials/mindee
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Mindee 凭据 <a href="#mindee-credentials" id="mindee-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Mindee](../app-nodes/n8n-nodes-base.mindee.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Mindee](https://mindee.com) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Invoice API key（发票 API 密钥）：用于 [Invoice OCR API](https://www.mindee.com/product/invoice-ocr-api)。
- Receipt API key（收据 API 密钥）：用于 [Receipt OCR API](https://www.mindee.com/product/receipt-ocr-api)。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

各服务的更多信息，请参阅 [Mindee Invoice OCR API 文档](https://developers.mindee.com/docs/invoice-ocr)和 [Mindee Receipt OCR API 文档](https://developers.mindee.com/docs/receipt-ocr)。

## 使用发票 API 密钥 <a href="#using-invoice-api-key" id="using-invoice-api-key"></a>

配置此凭据需要：

- **API Key**（API 密钥）：创建步骤请参阅 Mindee [Create & Manage API Keys 文档](https://developers.mindee.com/docs/create-api-key)。

## 使用收据 API 密钥 <a href="#using-receipt-api-key" id="using-receipt-api-key"></a>

配置此凭据需要：

- **API Key**（API 密钥）：创建步骤请参阅 Mindee [Create & Manage API Keys 文档](https://developers.mindee.com/docs/create-api-key)。

