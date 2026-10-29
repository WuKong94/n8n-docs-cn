---
title: Storyblok 凭据
description: Storyblok 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Storyblok 的身份验证。
contentType:
- integration
- reference
nodeTitle: Storyblok 凭据
originalFilePath: integrations/builtin/credentials/storyblok.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/storyblok
url: https://docs.n8n.io/integrations/builtin/credentials/storyblok
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Storyblok 凭据 <a href="#storyblok-credentials" id="storyblok-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Storyblok](../app-nodes/n8n-nodes-base.storyblok.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Storyblok](https://www.storyblok.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Content API key（内容 API 密钥）：用于只读访问。
- Management API key（管理 API 密钥）：用于完整的创建、读取、更新和删除操作。

{% hint style="info" %}
**Content API 支持**

n8n 仅支持 Content API v1。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

这些服务的更多信息，请参阅 Storyblok 的 [Content v1 API 文档](https://www.storyblok.com/docs/api/content-delivery/v1)和 [Management API 文档](https://www.storyblok.com/docs/api/management)。

## 使用 Content API 密钥 <a href="#using-content-api-key" id="using-content-api-key"></a>

配置此凭据需要：

- 一个内容 **API Key**（API 密钥）：在 Storyblok 工作区的 **Settings > Access Tokens**（设置 > 访问令牌）中获取 API 密钥。将 **Access Level**（访问级别）设为 **Public**（公开，`version=published`）或 **Preview**（预览，`version-published` 和 `version=draft`），并将此访问令牌填入 **API Key**。详细步骤请参阅[获取和生成访问令牌的方法](https://www.storyblok.com/faq/retrieve-and-generate-access-tokens)。

各访问级别支持的操作，请参阅 [Content v1 API 身份验证](https://www.storyblok.com/docs/api/content-delivery/v1#topics/authentication)。

## 使用 Management API 密钥 <a href="#using-management-api-key" id="using-management-api-key"></a>

配置此凭据需要：

- 一个 **Personal Access Token**（个人访问令牌）：进入 [**My Account**](https://app.storyblok.com/#!/me/account) **> Personal access tokens**（我的账户 > 个人访问令牌）生成新的访问令牌，将其填入 **Personal Access Token**。

