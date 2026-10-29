---
title: Spotify 凭据
description: Spotify 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Spotify 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Spotify 凭据
originalFilePath: integrations/builtin/credentials/spotify.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/spotify
url: https://docs.n8n.io/integrations/builtin/credentials/spotify
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Spotify 凭据 <a href="#spotify-credentials" id="spotify-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Spotify](../app-nodes/n8n-nodes-base.spotify.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Spotify Web API 文档](https://developer.spotify.com/documentation/web-api)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果[自行托管](../../../deploy/host-n8n/README.md) n8n，需要一个 [Spotify Developer（开发者）](https://developer.spotify.com/)账户，以便创建 Spotify 应用：

1. 打开 [Spotify 开发者控制台](https://developer.spotify.com/dashboard)。
2. 选择 **Create an app**（创建应用）。
3. 输入 **App name**（应用名称），例如 `n8n integration`。
4. 输入 **App description**（应用描述）。
5. 从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），将其填入 Spotify 应用的 **Redirect URI**（重定向 URI）。
6. 勾选复选框，同意 Spotify 的服务条款和品牌规范。
7. 选择 **Create**（创建），随后打开 **App overview**（应用概览）页面。
8. 复制 **Client ID**（客户端 ID），填入 n8n 凭据。
9. 复制 **Client Secret**（客户端密钥），填入 n8n 凭据。
10. 选择 **Connect my account**（连接我的账户），按照屏幕提示完成凭据授权。

更多信息请参阅 [Spotify Apps（应用）](https://developer.spotify.com/documentation/web-api/concepts/apps)。
