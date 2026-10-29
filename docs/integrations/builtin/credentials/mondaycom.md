---
title: monday.com 凭据
description: monday.com 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 monday.com 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: monday.com 凭据
originalFilePath: integrations/builtin/credentials/mondaycom.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/mondaycom
url: https://docs.n8n.io/integrations/builtin/credentials/mondaycom
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# monday.com 凭据 <a href="#mondaycom-credentials" id="mondaycom-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [monday.com](../app-nodes/n8n-nodes-base.mondaycom.md)

{% hint style="info" %}
**最低版本要求**

monday.com 节点要求 n8n 1.22.6。
{% endhint %}

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务身份验证的更多信息，请参阅 [monday.com API 文档](https://developer.monday.com/api-reference/docs/basics)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要一个 [monday.com](https://monday.com/) 账号，以及：

- API **Token V2**（V2 令牌）

获取令牌的步骤如下：

1. 在 monday.com 账户中，选择右上角的个人头像。
2. 选择 **Developers**（开发者），开发者中心会在新选项卡中打开。
3. 在开发者中心，选择 **My Access Tokens > Show**（我的访问令牌 > 显示）。
4. 复制个人令牌，填入 n8n 凭据的 **Token V2**（V2 令牌）。

更多信息，请参阅 [monday.com API 身份验证](https://developer.monday.com/api-reference/docs/authentication)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要一个 [monday.com](https://monday.com/) 账号，以及：

- 一个 **Client ID（客户端 ID）**
- 一个 **Client Secret（客户端密钥）**

如需生成这两个字段，请注册新的 monday.com 应用：

1. 在 monday.com 账户中，选择右上角的个人头像。
2. 选择 **Developers**（开发者），开发者中心会在新选项卡中打开。
3. 在开发者中心，选择 **Build app**（构建应用），随后打开应用详情。
4. 输入应用的 **Name**（名称），例如 `n8n integration`。
5. 复制 **Client ID**（客户端 ID），填入 n8n 凭据。
6. **Show**（显示）**Client Secret**（客户端密钥），复制后填入 n8n 凭据。
7. 在左侧菜单选择 **OAuth**。
8. 在 **Scopes**（作用域）中选择 `boards:write` 和 `boards:read`。
9. 选择 **Save Scopes**（保存作用域）。
10. 选择 **Redirect URLs**（重定向 URL）选项卡。
11. 从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），填入 **Redirect URL**（重定向 URL）。
12. 在 monday.com 中 **Save**（保存）更改。
13. 在 n8n 中选择 **Connect my account**（连接我的账户），完成设置。

 创建应用的更多信息，请参阅[创建应用](https://developer.monday.com/apps/docs/create-an-app)。
 
 可用作用域及重定向 URL 设置的更多信息，请参阅 [OAuth 与权限](https://developer.monday.com/apps/docs/oauth)。
