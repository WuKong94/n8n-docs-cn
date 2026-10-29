---
title: Webflow 凭据
description: Webflow 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Webflow 的身份验证。
contentType:
- integration
- reference
nodeTitle: Webflow 凭据
originalFilePath: integrations/builtin/credentials/webflow.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/webflow
url: https://docs.n8n.io/integrations/builtin/credentials/webflow
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Webflow 凭据 <a href="#webflow-credentials" id="webflow-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Webflow](../app-nodes/n8n-nodes-base.webflow.md)
- [Webflow Trigger（触发器）](../trigger-nodes/n8n-nodes-base.webflowtrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Webflow](https://webflow.com/) 账号。
- [创建站点](https://developers.webflow.com/data/reference/structure-1#sites)：仅 API 访问令牌身份验证需要此步骤。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Webflow API 文档](https://developers.webflow.com/data/reference/rest-introduction)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要：

- 站点 **Access Token**（访问令牌）：访问令牌专属于具体站点。进入站点的 **Site Settings > Apps & integrations > API access**（站点设置 > 应用与集成 > API 访问），选择 **Generate API token**（生成 API 令牌）。更多信息请参阅[获取站点令牌](https://developers.webflow.com/data/v1.0.0/docs/get-a-site-token)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果需要从头配置 OAuth2，请在工作区中[注册应用](https://developers.webflow.com/data/docs/register-an-app)。

为应用采用以下设置：

- 从 n8n 复制 **OAuth callback URL**（OAuth 回调 URL），将其添加为应用的 **Redirect URI**（重定向 URI）。
- 创建应用后，复制 **Client ID** 和 **Client Secret**，填入 n8n 凭据。
- Webflow Data API V1 已弃用。如果仍在使用，请开启 **Legacy**（旧版）开关；否则保持关闭。

Webflow OAuth 网页流程的更多信息，请参阅 [OAuth](https://developers.webflow.com/data/reference/oauth-app)。
