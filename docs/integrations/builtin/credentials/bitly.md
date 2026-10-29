---
title: Bitly 凭据
description: Bitly 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Bitly 的身份验证。
contentType:
- integration
- reference
nodeTitle: Bitly 凭据
originalFilePath: integrations/builtin/credentials/bitly.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/bitly
url: https://docs.n8n.io/integrations/builtin/credentials/bitly
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Bitly 凭据 <a href="#bitly-credentials" id="bitly-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Bitly](../app-nodes/n8n-nodes-base.bitly.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Bitly](https://www.bitly.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Bitly API 文档](https://dev.bitly.com/)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要：

- 一个 **Access Token（访问令牌）**：登录后，进入 [Settings > Developer Settings > API（设置 > 开发者设置 > API）](https://app.bitly.com/settings/api/)生成令牌。


## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果需要从头配置 OAuth2，或希望进一步了解 OAuth 网页授权流程，请参阅 [Bitly API 身份验证文档](https://dev.bitly.com/docs/getting-started/authentication/)。

