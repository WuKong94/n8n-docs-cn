---
title: Linear 凭据
description: Linear 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Linear 的身份验证。
contentType:
- integration
- reference
nodeTitle: Linear 凭据
originalFilePath: integrations/builtin/credentials/linear.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/linear
url: https://docs.n8n.io/integrations/builtin/credentials/linear
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Linear 凭据 <a href="#linear-credentials" id="linear-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Linear Trigger（触发器）](../trigger-nodes/n8n-nodes-base.lineartrigger.md)
* [Linear](../app-nodes/n8n-nodes-base.linear.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Linear](https://linear.app/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Linear API 文档](https://developers.linear.app/docs/graphql/working-with-the-graphql-api)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：


- 个人 **API Key**（API 密钥）：在 [**Settings** > **Security & access**](https://linear.app/n8n/settings/account/security)（设置 > 安全与访问）中创建专用的个人 API 密钥。更多信息请参阅 [Linear 个人 API 密钥文档](https://linear.app/developers/graphql#personal-api-keys)。


## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- **Client ID**（客户端 ID）：创建新的 OAuth2 应用时生成。
- **Client Secret**（客户端密钥）：创建新的 OAuth2 应用时生成。
- 选择 **Actor**（执行身份）：决定 OAuth2 应用以何种身份创建问题、评论和其他更改，可选项：
    - **User**（用户，Linear 默认选项）：应用以授权用户的身份创建资源。希望每位用户分别完成身份验证时，使用此选项。
    - **Application**（应用）：应用以自身身份创建资源。只有一位用户（例如管理员）为应用授权时，使用此选项。
- 要在 [Linear Trigger](../trigger-nodes/n8n-nodes-base.lineartrigger.md) 节点中使用此凭据，必须开启 **Include Admin Scope**（包含管理员作用域）开关。

详细步骤和解释请参阅 [Linear OAuth2 身份验证文档](https://developers.linear.app/docs/oauth/authentication)。将 n8n 的 **OAuth Redirect URL**（OAuth 重定向 URL）用作 Linear OAuth2 应用的 **Redirect callback URL**（重定向回调 URL）。
