---
title: Philips Hue 凭据
description: Philips Hue 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Philips Hue 的身份验证。
contentType:
- integration
- reference
nodeTitle: Philips Hue 凭据
originalFilePath: integrations/builtin/credentials/philipshue.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/philipshue
url: https://docs.n8n.io/integrations/builtin/credentials/philipshue
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Philips Hue 凭据 <a href="#philips-hue-credentials" id="philips-hue-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Philips Hue](../app-nodes/n8n-nodes-base.philipshue.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Philips Hue](https://www.philips-hue.com/en-us) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Philips Hue CLIP API 文档](https://developers.meethue.com/develop/hue-api-v2/api-reference/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

使用内置 OAuth 连接时，无需填写 **APP ID**。

如果需要从头配置 OAuth2，则需要一个 [Philips Hue 开发者](https://developers.meethue.com/)账户。

在 [Add new Hue Remote API app](https://developers.meethue.com/add-new-hue-remote-api-app/)（添加新的 Hue Remote API 应用）页面创建远程应用。

为应用采用以下设置：

- 从 n8n 复制 **OAuth Callback URL**（OAuth 回调 URL），填为 **Callback URL**（回调 URL）。
- 复制 **AppId**、**ClientId** 和 **ClientSecret**，填入 n8n 对应字段。
