---
title: WordPress 凭据
description: WordPress 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 WordPress 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: WordPress 凭据
originalFilePath: integrations/builtin/credentials/wordpress.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/wordpress
url: https://docs.n8n.io/integrations/builtin/credentials/wordpress
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# WordPress 凭据 <a href="#wordpress-credentials" id="wordpress-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [WordPress](../app-nodes/n8n-nodes-base.wordpress.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- **Basic auth**（基本身份验证）：创建 [WordPress](https://wordpress.com/) 账户，或在服务器上部署 WordPress。
- **OAuth2**：创建可访问[开发者门户](https://developer.wordpress.com/apps/)的 [WordPress.com](https://wordpress.com/) 账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [WordPress API 文档](https://developer.wordpress.com/docs/api/)。

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

配置此凭据需要：

- WordPress 的 **Username**（用户名）
- WordPress 应用 **Password**（密码）
- 你的 **WordPress URL**
- 决定是否 **Ignore SSL Issues**（忽略 SSL 问题）

使用此凭据需要三个步骤：

1. [启用两步身份验证](#enable-two-step-authentication)。
2. [创建应用密码](#create-an-application-password)。
3. [设置凭据](#set-up-the-credential)。

各步骤的详细说明如下。

### 启用两步身份验证 <a href="#enable-two-step-authentication" id="enable-two-step-authentication"></a>

生成应用密码前，必须先在 WordPress 中启用两步身份验证。如果已完成，可[跳至下一节](#create-an-application-password)。

1. 打开 WordPress 的[个人资料](https://wordpress.com/me)。
2. 从左侧菜单选择 **Security**（安全）。
3. 选择 **Two-Step Authentication**（两步身份验证），随后打开该页面。
4. 如果尚未启用两步身份验证，必须先启用。
5. 选择使用身份验证器应用或短信验证码启用，按照屏幕说明操作。

详细步骤，请参阅 WordPress 的[启用两步身份验证](https://wordpress.com/support/security/two-step-authentication/)。

### 创建应用密码 <a href="#create-an-application-password" id="create-an-application-password"></a>

启用两步身份验证后，即可生成应用密码：

1. 在 WordPress 的 **Security >** [**Two-Step Authentication**](https://wordpress.com/me/security/two-step)（安全 > 两步身份验证）页面，在 **Application passwords**（应用密码）部分选择 **+ Add new application password**（添加新应用密码）。
2. 输入 **Application name**（应用名称），例如 `n8n integration`。
3. 选择 **Generate Password**（生成密码）。
4. 复制生成的密码，稍后填入 n8n 凭据。

### 设置凭据 <a href="#set-up-the-credential" id="set-up-the-credential"></a>

1. 在 n8n 凭据中输入 WordPress 的 **Username**（用户名）。
2. 将上面复制的应用密码填入 n8n 凭据的 **Password**（密码）。
3. 将 WordPress 网站 URL 填入 **WordPress URL**。
4. 可选：使用 **Ignore SSL Issues**（忽略 SSL 问题），选择 n8n 凭据是否在 SSL 证书验证失败时仍连接（开启），或遵循 SSL 证书验证（关闭）。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% hint style="info" %}
**仅适用于 WordPress.com**

OAuth2 身份验证仅适用于 WordPress.com 托管的网站。自托管 WordPress 请改用基本身份验证。
{% endhint %}

配置此凭据需要：

- **Client ID**（客户端 ID）：创建 WordPress.com 开发者应用时生成。
- **Client Secret**（客户端密钥）：创建 WordPress.com 开发者应用时生成。
- **WordPress.com Site**（WordPress.com 站点）：你的 `.wordpress.com` 子域名或自定义域名，例如 `myblog.wordpress.com` 或 `myblog.com`。

创建此凭据需要两个步骤：

1. [创建开发者应用](#create-a-developer-application)。
2. [设置 OAuth2 凭据](#set-up-the-oauth2-credential)。

### 创建开发者应用 <a href="#create-a-developer-application" id="create-a-developer-application"></a>

1. 打开 WordPress.com 的[开发者应用](https://developer.wordpress.com/apps/)页面。
2. 选择 **Create New Application**（创建新应用）。
3. 输入应用的 **Name**（名称），例如 `n8n integration`。
4. 从 n8n 的 **OAuth2 (WordPress.com)** 凭据页面复制 **OAuth Redirect URL**（OAuth 重定向 URL），粘贴到 WordPress 的 **Redirect URLs**（重定向 URL）字段。
5. 根据应用情况，填写 **Description**（描述）、**Website URL**（网站 URL）及其他字段。
6. 选择 **Create**（创建），保存应用。
7. 返回 WordPress.com 的[开发者应用](https://developer.wordpress.com/apps/)页面，点击刚创建的集成。
8. 复制 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）。

### 设置 OAuth2 凭据 <a href="#set-up-the-oauth2-credential" id="set-up-the-oauth2-credential"></a>

1. 在 n8n 的 **OAuth2 (WordPress.com)** 凭据页面中，粘贴上一步获取的 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）。
2. 在 **WordPress.com Site**（WordPress.com 站点）字段中输入站点标识符，例如 `myblog.wordpress.com`。
3. 点击 **Connect to WordPress**（连接到 WordPress）。

更多信息，请参阅 WordPress 的 [OAuth2 身份验证文档](https://developer.wordpress.com/docs/oauth2/)。
