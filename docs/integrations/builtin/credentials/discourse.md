---
title: Discourse 凭据
description: Discourse 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Discourse 的身份验证。
contentType:
- integration
- reference
nodeTitle: Discourse 凭据
originalFilePath: integrations/builtin/credentials/discourse.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/discourse
url: https://docs.n8n.io/integrations/builtin/credentials/discourse
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Discourse 凭据 <a href="#discourse-credentials" id="discourse-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Discourse](../app-nodes/n8n-nodes-base.discourse.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 托管一个 [Discourse](https://discourse.org/) 实例。
- 在托管的实例中创建账户，并确保具有管理员身份。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Discourse API 文档](https://docs.discourse.org/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- Discourse 实例的 **URL**，例如 `https://community.n8n.io`。
- **API Key**（API 密钥）：通过 Discourse 管理面板创建。如何创建密钥并指定用户名，请参阅 [Discourse 创建和配置 API 密钥文档](https://meta.discourse.org/t/create-and-configure-an-api-key/230124)。
- **Username**（用户名）：使用你自己的名称、`system` 或其他用户。

示例请参阅 [Discourse API 文档](https://docs.discourse.org/)中的 Authentication（身份验证）部分。


