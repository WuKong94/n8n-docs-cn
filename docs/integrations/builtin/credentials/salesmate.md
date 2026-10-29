---
title: Salesmate 凭据
description: Salesmate 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Salesmate 的身份验证。
contentType:
- integration
- reference
nodeTitle: Salesmate 凭据
originalFilePath: integrations/builtin/credentials/salesmate.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/salesmate
url: https://docs.n8n.io/integrations/builtin/credentials/salesmate
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Salesmate 凭据 <a href="#salesmate-credentials" id="salesmate-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Salesmate](../app-nodes/n8n-nodes-base.salesmate.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Salesmate](https://salesmate.io/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Salesmate API 文档](https://apidocs.salesmate.io/?version=latest)。


## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要：

- 一个 **Session Token（会话令牌）**，即 **Access Key（访问密钥）**。在 **My Account > Access Key（我的账号 > 访问密钥）** 中生成。更多信息请参阅[访问权限和密钥](https://apidocs.salesmate.io/?version=latest#ac8296ec-cb44-4937-a860-5ae032397ca0)。
- 一个 **URL**：即 Salesmate 的域名／基础 URL，例如 `n8n.salesmate.io`。

