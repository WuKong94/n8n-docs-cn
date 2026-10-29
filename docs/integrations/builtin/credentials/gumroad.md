---
title: Gumroad 凭据
description: Gumroad 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Gumroad 的身份验证。
contentType:
- integration
- reference
nodeTitle: Gumroad 凭据
originalFilePath: integrations/builtin/credentials/gumroad.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/gumroad
url: https://docs.n8n.io/integrations/builtin/credentials/gumroad
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Gumroad 凭据 <a href="#gumroad-credentials" id="gumroad-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Gumroad Trigger（触发器）](../trigger-nodes/n8n-nodes-base.gumroadtrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Gumroad](https://gumroad.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Gumroad API 文档](https://app.gumroad.com/api)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要：

- 一个 API **Access Token**（访问令牌）：创建应用以生成访问令牌。创建新应用并生成访问令牌的详细步骤，请参阅 [Gumroad 创建 API 应用的文档](https://gumroad.com/help/article/280-create-application-api)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果[自行托管 n8n](../../../deploy/host-n8n/README.md)，你需要：

- 一个 **OAuth Redirect URL**（OAuth 重定向 URL）
- 一个 **Client ID（客户端 ID）**
- 一个 **Client Secret（客户端密钥）**

要获取这些信息，请创建 Gumroad 应用：

1. 在 Gumroad 中进入 **Settings > Advanced**（设置 > 高级）。详细步骤请参阅 [Gumroad 创建 API 应用的文档](https://gumroad.com/help/article/280-create-application-api)。
2. 从 n8n 凭据中复制 **OAuth Redirect URL**（OAuth 重定向 URL），在 Gumroad 中创建应用时将其填入 **Redirect URI**（重定向 URI）。
3. 创建应用。Gumroad 会生成 **Application ID**（应用 ID）和 **Application Secret**（应用密钥）。
4. 复制 **Application ID**（应用 ID），粘贴到 n8n 凭据的 **Client ID**（客户端 ID）字段。
5. 复制 **Application Secret**（应用密钥），粘贴到 n8n 凭据的 **Client Secret**（客户端密钥）字段。
6. 如果要请求默认 `view_sales` 以外的作用域，请在 n8n 凭据中启用 **Custom Scopes**（自定义作用域），并输入所需作用域；否则保持关闭。

