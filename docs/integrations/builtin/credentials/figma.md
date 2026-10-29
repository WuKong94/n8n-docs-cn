---
title: Figma 凭据
description: Figma 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Figma 的身份验证。
contentType:
- integration
- reference
nodeTitle: Figma 凭据
originalFilePath: integrations/builtin/credentials/figma.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/figma
url: https://docs.n8n.io/integrations/builtin/credentials/figma
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Figma 凭据 <a href="#figma-credentials" id="figma-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Figma Trigger（Beta 触发器）](../trigger-nodes/n8n-nodes-base.figmatrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建 [Figma](https://www.figma.com/) 账户，需要管理员或所有者级别的账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Access token（访问令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Figma API 文档](https://www.figma.com/developers/api)。

## 使用访问令牌 <a href="#using-access-token" id="using-access-token"></a>

配置此凭据需要：

- 个人 **Access Token**（访问令牌，PAT）：生成步骤，请参阅 [Figma API 访问令牌文档](https://www.figma.com/developers/api#access-tokens)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要一个 [Figma](https://www.figma.com/) 账户。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果[自托管](../../../deploy/host-n8n/README.md) n8n，需要注册应用以设置 OAuth：

1. 打开 Figma 的[开发者应用](https://www.figma.com/developers/apps)页面。
2. 选择 **Create a new app**（创建新应用）。
3. 输入应用的 **Name**（名称），例如 `n8n integration`。
4. 在 n8n 中复制 **OAuth Redirect URL**（OAuth 重定向 URL）。
5. 在 Figma 中选择 **Add a callback**（添加回调），输入从 n8n 复制的 URL。
6. 保存应用。
7. 从 Figma 复制 **Client ID**（客户端 ID），填入 n8n 凭据。
8. 从 Figma 复制 **Client Secret**（客户端密钥），填入 n8n 凭据。

更多信息，请参阅 [Figma OAuth 文档](https://www.figma.com/developers/api#oauth2)。

## 设置自定义权限范围 <a href="#setting-custom-scopes" id="setting-custom-scopes"></a>

Figma OAuth2 凭据默认使用以下作用域：

* `webhooks:read`
* `webhooks:write`

如需为凭据选择其他作用域，请启用 **Custom Scopes**（自定义作用域）开关，并编辑 **Enabled Scopes**（已启用的作用域）列表。使用更严格的作用域时，部分功能可能无法正常运行。全部可用作用域，请参阅 [Figma OAuth 作用域](https://developers.figma.com/docs/rest-api/scopes/)。
