---
title: PagerDuty 凭据
description: PagerDuty 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 PagerDuty 的身份验证。
contentType:
- integration
- reference
nodeTitle: PagerDuty 凭据
originalFilePath: integrations/builtin/credentials/pagerduty.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/pagerduty
url: https://docs.n8n.io/integrations/builtin/credentials/pagerduty
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# PagerDuty 凭据 <a href="#pagerduty-credentials" id="pagerduty-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [PagerDuty](../app-nodes/n8n-nodes-base.pagerduty.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [PagerDuty](https://pagerduty.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [PagerDuty API 文档](https://developer.pagerduty.com/docs/531092d4c6658-rest-api-v2-overview)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要：

- 一个通用访问 **API Token**（API 令牌）：在 **Integrations > Developer Tools > API Access Keys > Create New API Key**（集成 > 开发者工具 > API 访问密钥 > 创建新 API 密钥）中生成 API 令牌。更多信息请参阅[生成通用访问 REST API 密钥](https://support.pagerduty.com/docs/api-access-keys#generate-a-general-access-rest-api-key)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果需要从头配置 OAuth2，请[注册新的 PagerDuty 应用](https://developer.pagerduty.com/docs/dd91fbd09a1a1-register-an-app)。

注册应用时使用以下设置：

- 在 **Category**（类别）下拉菜单中选择 **Infrastructure Automation**（基础设施自动化）。
- 在 **Functionality**（功能）部分选择 **OAuth 2.0**。

**Save**（保存）应用后，打开应用详情，[编辑应用配置](https://developer.pagerduty.com/docs/dd91fbd09a1a1-register-an-app#editing-your-app-configuration)并使用以下设置：

- 在 **OAuth 2.0** 部分选择 **Add**（添加）。
- 从 n8n 复制 **OAuth Callback URL**（OAuth 回调 URL），粘贴到 **Redirect URL**（重定向 URL）字段。
- 从 PagerDuty 复制 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥），添加到 n8n 凭据。
- 在 **Set Permission Scopes**（设置权限作用域）下拉菜单中选择 **Read/Write**（读写）。

可用功能的更多信息，请参阅[应用功能](https://developer.pagerduty.com/docs/b25fd1b8acb1b-app-functionality)中的说明。OAuth 流程的更多信息，请参阅 PagerDuty 的 [OAuth 功能文档](https://developer.pagerduty.com/docs/f59fdbd94ceab-o-auth-functionality)。


