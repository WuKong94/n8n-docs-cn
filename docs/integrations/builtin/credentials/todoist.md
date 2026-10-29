---
title: Todoist 凭据
description: Todoist 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Todoist 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Todoist 凭据
originalFilePath: integrations/builtin/credentials/todoist.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/todoist
url: https://docs.n8n.io/integrations/builtin/credentials/todoist
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Todoist 凭据 <a href="#todoist-credentials" id="todoist-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Todoist](../app-nodes/n8n-nodes-base.todoist.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Todoist REST API 文档](https://developer.todoist.com/rest/v2/#overview)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个 [Todoist](https://todoist.com/) 账号，以及：

- 一个 **API Key（API 密钥）**

获取 **API Key**（API 密钥）的步骤如下：

1. 在 Todoist 中打开 [**Settings > Integrations**（设置 > 集成）](https://app.todoist.com/app/settings/integrations)。
2. 选择 **Developer**（开发者）选项卡。
3. 复制 **API token**（API 令牌），填入 n8n 凭据的 **API Key**（API 密钥）。

更多信息，请参阅[查找 API 令牌](https://todoist.com/help/articles/find-your-api-token-Jpzx9IIlB)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果[自托管](../../../deploy/host-n8n/README.md) n8n，需要一个 [Todoist](https://todoist.com/) 账户，以及：

- 一个 **Client ID（客户端 ID）**
- 一个 **Client Secret（客户端密钥）**

创建应用即可获取这两项：

1. 打开 Todoist 的[应用管理控制台](https://developer.todoist.com/appconsole.html)。
2. 选择 **Create a new app**（创建新应用）。
3. 输入应用的 **App name**（应用名称），例如 `n8n integration`。
4. 选择 **Create app**（创建应用）。
5. 从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），填入 Todoist 的 **OAuth redirect URL**（OAuth 重定向 URL）。
6. 从 Todoist 复制 **Client ID**（客户端 ID），填入 n8n 凭据。
7. 从 Todoist 复制 **Client Secret**（客户端密钥），填入 n8n 凭据。
8. 根据具体使用场景，配置 Todoist 应用的其余部分。

更多信息，请参阅 Todoist 的[授权指南](https://developer.todoist.com/guides/#authorization)。
