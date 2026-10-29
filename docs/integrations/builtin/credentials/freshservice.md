---
title: Freshservice 凭据
description: Freshservice 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Freshservice 的身份验证。
contentType:
- integration
- reference
nodeTitle: Freshservice 凭据
originalFilePath: integrations/builtin/credentials/freshservice.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/freshservice
url: https://docs.n8n.io/integrations/builtin/credentials/freshservice
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Freshservice 凭据 <a href="#freshservice-credentials" id="freshservice-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Freshservice](../app-nodes/n8n-nodes-base.freshservice.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Freshservice](https://freshservice.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Freshservice API 文档](https://api.freshservice.com/v2/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**：获取密钥的详细步骤，请参阅 [Freshservice API 身份验证文档](https://api.freshservice.com/v2/#authentication)。
- 你的 Freshservice **Domain（域名）**：使用账号的子域名，即 URL 中的一部分，例如 `https://<subdomain>.freshservice.com`。如果通过 `https://n8n.freshservice.com` 访问 Freshservice，请将 **Domain** 填为 `n8n`。

