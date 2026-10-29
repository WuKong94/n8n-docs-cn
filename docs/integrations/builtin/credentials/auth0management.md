---
title: Auth0 Management 凭据
description: Auth0 Management 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Auth0 Management 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Auth0 Management 凭据
originalFilePath: integrations/builtin/credentials/auth0management.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/auth0management
url: https://docs.n8n.io/integrations/builtin/credentials/auth0management
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Auth0 Management 凭据 <a href="#auth0-management-credentials" id="auth0-management-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Auth0](https://auth0.com) 账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API client secret（API 客户端密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Auth0 Management 文档](https://auth0.com/docs/api/management/v2)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/auth0-management-api/)。

## 使用 API 客户端密钥 <a href="#using-api-client-secret" id="using-api-client-secret"></a>

配置此凭据需要：

- Auth0 **Domain**（域名）
- 一个 **Client ID（客户端 ID）**
- 一个 **Client Secret（客户端密钥）**

如何从应用的 **Settings**（设置）标签页获取 Client ID 和 Client Secret，请参阅 [Auth0 Management API 的 Get Access Tokens 文档](https://auth0.com/docs/secure/tokens/access-tokens/get-access-tokens)。
