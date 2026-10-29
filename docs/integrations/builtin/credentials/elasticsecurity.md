---
title: Elastic Security 凭据
description: Elastic Security 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Elastic Security 的身份验证。
contentType:
- integration
- reference
nodeTitle: Elastic Security 凭据
originalFilePath: integrations/builtin/credentials/elasticsecurity.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/elasticsecurity
url: https://docs.n8n.io/integrations/builtin/credentials/elasticsecurity
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Elastic Security 凭据 <a href="#elastic-security-credentials" id="elastic-security-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Elastic Security](../app-nodes/n8n-nodes-base.elasticsecurity.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Elastic Security](https://www.elastic.co/security) 账户。
- [部署](https://www.elastic.co/guide/en/cloud/current/ec-create-deployment.html)应用。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）
- API Key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Elastic Security 文档](https://www.elastic.co/guide/en/security/current/es-overview.html)。

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

配置此凭据需要：

- **Username**（用户名）：登录 Elasticsearch 所用用户账户的用户名。
- **Password**（密码）：登录 Elasticsearch 所用用户账户的密码。
- Elasticsearch 应用的 **Base URL**（基础 URL，也称为 Elasticsearch 应用端点）：

    1. 在 Elasticsearch 中选择 **Manage this deployment**（管理此部署）。
    2. 在 **Applications**（应用）部分，复制 **Elasticsearch** 应用的端点。
    3. 在 n8n 中，将其填入 **Base URL**（基础 URL）。

{% hint style="info" %}
**自定义端点别名**

如果为部署添加了[自定义端点别名](https://www.elastic.co/guide/en/cloud/current/ec-regional-deployment-aliases.html)，请将 n8n 凭据的 **Base URL**（基础 URL）更新为新端点。
{% endhint %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **API Key**（API 密钥）：用于登录 Elasticsearch 的用户账户。更多信息，请参阅 Elasticsearch 的[创建 API 密钥文档](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-create-api-key.html)。
- Elasticsearch 应用的 **Base URL**（基础 URL，也称为 Elasticsearch 应用端点）：

    1. 在 Elasticsearch 中选择 **Manage this deployment**（管理此部署）。
    2. 在 **Applications**（应用）部分，复制 **Elasticsearch** 应用的端点。
    3. 在 n8n 中，将其填入 **Base URL**（基础 URL）。
