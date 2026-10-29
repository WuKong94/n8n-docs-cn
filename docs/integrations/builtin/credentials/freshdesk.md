---
title: Freshdesk 凭据
description: Freshdesk 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Freshdesk 的身份验证。
contentType:
- integration
- reference
nodeTitle: Freshdesk 凭据
originalFilePath: integrations/builtin/credentials/freshdesk.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/freshdesk
url: https://docs.n8n.io/integrations/builtin/credentials/freshdesk
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Freshdesk 凭据 <a href="#freshdesk-credentials" id="freshdesk-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Freshdesk](../app-nodes/n8n-nodes-base.freshdesk.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Freshdesk](https://freshdesk.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Freshdesk API 文档](https://developers.freshdesk.com/api/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**：获取密钥的详细步骤，请参阅 [Freshdesk API 身份验证文档](https://developers.freshdesk.com/api/#authentication)。
- 一个 Freshdesk **Domain（域名）**：使用账号的子域名，即 URL 中的一部分，例如 `https://<subdomain>.freshdesk.com`。如果通过 `https://n8n.freshdesk.com` 访问 Freshdesk，请将 **Domain** 填为 `n8n`。

