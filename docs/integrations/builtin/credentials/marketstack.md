---
title: Marketstack 凭据
description: Marketstack 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Marketstack 的身份验证。
contentType:
- integration
- reference
nodeTitle: Marketstack 凭据
originalFilePath: integrations/builtin/credentials/marketstack.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/marketstack
url: https://docs.n8n.io/integrations/builtin/credentials/marketstack
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Marketstack 凭据 <a href="#marketstack-credentials" id="marketstack-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Marketstack](../app-nodes/n8n-nodes-base.marketstack.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Marketstack](https://marketstack.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Marketstack API 文档](https://marketstack.com/documentation)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **API Key**（API 密钥）：在 Marketstack 的[账户控制台](https://marketstack.com/dashboard)中查看和生成 API 密钥。
- 选择是否 **Use HTTPS**（使用 HTTPS）：根据 Marketstack 账户的方案层级选择：
    - Free 方案：关闭 **Use HTTPS**。
    - 其他所有方案：开启 **Use HTTPS**。

