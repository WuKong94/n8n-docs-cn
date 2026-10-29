---
title: Contentful 凭据
description: Contentful 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Contentful 的身份验证。
contentType:
- integration
- reference
nodeTitle: Contentful 凭据
originalFilePath: integrations/builtin/credentials/contentful.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/contentful
url: https://docs.n8n.io/integrations/builtin/credentials/contentful
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Contentful 凭据 <a href="#contentful-credentials" id="contentful-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Contentful](../app-nodes/n8n-nodes-base.contentful.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Contentful](https://www.contentful.com/) 账号。
- 创建一个 [Contentful 空间](https://www.contentful.com/help/getting-started/contentful-101/#step-2-create-a-space)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Contentful API 文档](https://www.contentful.com/developers/docs/references/)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要：

- Contentful **Space ID**（空间 ID）：生成令牌时会显示 Space ID，也可以按照 [Contentful 的 Find space ID 文档](https://www.contentful.com/help/spaces/find-space-id/)查看。
- **Content Delivery API Access Token**（内容交付 API 访问令牌）：使用 [Content Delivery API](https://www.contentful.com/developers/docs/references/content-delivery-api/) 时必填，不使用此 API 时留空。
- **Content Preview API Access Token**（内容预览 API 访问令牌）：使用 [Content Preview API](https://www.contentful.com/developers/docs/references/content-preview-api/) 时必填，不使用此 API 时留空。

在 Contentful 的 **Settings > API keys**（设置 > API 密钥）中查看和生成访问令牌。创建一个密钥时，Contentful 会同时生成 Content Delivery API 和 Content Preview API 的令牌。详细步骤请参阅 [Contentful API 身份验证文档](https://www.contentful.com/developers/docs/references/authentication/)。

