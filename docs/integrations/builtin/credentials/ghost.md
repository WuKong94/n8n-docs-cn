---
title: Ghost 凭据
description: Ghost 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Ghost 的身份验证。
contentType:
- integration
- reference
nodeTitle: Ghost 凭据
originalFilePath: integrations/builtin/credentials/ghost.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/ghost
url: https://docs.n8n.io/integrations/builtin/credentials/ghost
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Ghost 凭据 <a href="#ghost-credentials" id="ghost-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Ghost](../app-nodes/n8n-nodes-base.ghost.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Ghost](https://ghost.org/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Admin API key（管理 API 密钥）
- Content API key（内容 API 密钥）

两种密钥的生成步骤相同，但授权流程和密钥格式不同，因此 n8n 将凭据分别存储。Content API 使用 API 密钥；Admin API 使用 API 密钥生成用于身份验证的令牌。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

Admin API 服务的更多信息，请参阅 Ghost 的 [Admin API 文档](https://ghost.org/docs/admin-api/)。Content API 服务的更多信息，请参阅 Ghost 的 [Content API 文档](https://ghost.org/docs/content-api/)。

## 使用 Admin API 密钥 <a href="#using-admin-api-key" id="using-admin-api-key"></a>

配置此凭据需要：

- Ghost 管理域名的 **URL**。你的[管理域名](https://ghost.org/docs/admin-api/#base-url)可能与主域名不同，也可能包含子目录。所有 Ghost(Pro) 博客都以 `*.ghost.io` 域名作为管理域名，并要求使用 HTTPS。
- 一个 **API Key**（API 密钥）：创建新的 Custom Integration（自定义集成）以生成新 API 密钥。详细步骤请参阅 [Ghost Admin API 令牌身份验证密钥文档](https://ghost.org/docs/admin-api/#token-authentication)。复制 **Admin API Key**，将其填入 n8n 的 Ghost Admin 凭据的 **API Key** 字段。

## 使用 Content API 密钥 <a href="#using-content-api-key" id="using-content-api-key"></a>

配置此凭据需要：

- Ghost 管理域名的 **URL**。你的[管理域名](https://ghost.org/docs/content-api/#url)可能与主域名不同，也可能包含子目录。所有 Ghost(Pro) 博客都以 `*.ghost.io` 域名作为管理域名，并要求使用 HTTPS。
- 一个 **API Key**（API 密钥）：创建新的 Custom Integration（自定义集成）以生成新 API 密钥。详细步骤请参阅 [Ghost Content API 密钥文档](https://ghost.org/docs/content-api/#key)。复制 **Content API Key**，将其填入 n8n 的 Ghost Content 凭据的 **API Key** 字段。

