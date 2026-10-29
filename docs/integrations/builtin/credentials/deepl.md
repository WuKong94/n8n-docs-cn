---
title: DeepL 凭据
description: DeepL 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 DeepL 的身份验证。
contentType:
- integration
- reference
nodeTitle: DeepL 凭据
originalFilePath: integrations/builtin/credentials/deepl.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/deepl
url: https://docs.n8n.io/integrations/builtin/credentials/deepl
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# DeepL 凭据 <a href="#deepl-credentials" id="deepl-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [DeepL](../app-nodes/n8n-nodes-base.deepl.md)


## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [DeepL 开发者](https://www.deepl.com/pro-api)账户。n8n 同时支持 Free 和 Pro API 方案。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [DeepL API 文档](https://developers.deepl.com/docs)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **API Key**（API 密钥）：获取密钥的更多信息，请参阅 [DeepL 身份验证文档](https://developers.deepl.com/docs/getting-started/auth#authentication)。
- 确认当前的 **API Plan**（API 方案）。DeepL 为各方案提供不同的 API 端点，因此请务必选择正确方案：
    - Pro Plan（Pro 方案）
    - Free Plan（Free 方案）

