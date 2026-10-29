---
title: ServiceNow 凭据
description: ServiceNow 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 ServiceNow 的身份验证。
contentType:
- integration
- reference
nodeTitle: ServiceNow 凭据
originalFilePath: integrations/builtin/credentials/servicenow.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/servicenow
url: https://docs.n8n.io/integrations/builtin/credentials/servicenow
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# ServiceNow 凭据 <a href="#servicenow-credentials" id="servicenow-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [ServiceNow](../app-nodes/n8n-nodes-base.servicenow.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [ServiceNow](https://developer.servicenow.com/dev.do#!/reference) 开发者账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [ServiceNow API 文档](https://developer.servicenow.com/dev.do#!/reference/api/washingtondc/rest/)。

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

配置此凭据需要：

- 一个 **User**（用户名）：输入你的 ServiceNow 用户名。
- 一个 **Password（密码）**：输入 ServiceNow 密码。
- 一个 **Subdomain**（子域名）：ServiceNow 实例的子域名位于实例 URL 中：`https://<subdomain>.service-now.com/`。例如，完整 URL 为 `https://dev99890.service-now.com` 时，子域名为 `dev99890`。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- 一个 **Client ID**（客户端 ID）：注册新应用时生成。
- 一个 **Client Secret**（客户端密钥）：注册新应用时生成。
- 一个 **Subdomain**（子域名）：ServiceNow 实例的子域名位于实例 URL 中：`https://<subdomain>.service-now.com/`。例如，完整 URL 为 `https://dev99890.service-now.com` 时，子域名为 `dev99890`。

要生成 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥），请在 **System OAuth > Application Registry > New > Create an OAuth API endpoint for external clients**（系统 OAuth > 应用注册表 > 新建 > 为外部客户端创建 OAuth API 端点）中注册新应用，并使用以下设置：

- 复制 **Client ID**（客户端 ID），添加到 n8n 凭据。
- 输入 **Client Secret**（客户端密钥），或留空以自动生成随机密钥。将此密钥添加到 n8n 凭据。
- 从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），将其添加为 **Redirect URL**（重定向 URL）。

更多信息请参阅[如何为 RESTMessageV2 集成设置 OAuth2 身份验证](https://www.servicenow.com/community/in-other-news/how-to-setup-oauth2-authentication-for-restmessagev2/ba-p/2271823)。

