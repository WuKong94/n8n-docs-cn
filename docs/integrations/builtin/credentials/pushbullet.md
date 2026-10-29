---
title: Pushbullet 凭据
description: Pushbullet 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Pushbullet 的身份验证。
contentType:
- integration
- reference
nodeTitle: Pushbullet 凭据
originalFilePath: integrations/builtin/credentials/pushbullet.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/pushbullet
url: https://docs.n8n.io/integrations/builtin/credentials/pushbullet
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Pushbullet 凭据 <a href="#pushbullet-credentials" id="pushbullet-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Pushbullet](../app-nodes/n8n-nodes-base.pushbullet.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Pushbullet](https://www.pushbullet.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Pushbullet API 文档](https://docs.pushbullet.com/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- **Client ID**（客户端 ID）：创建 Pushbullet 应用时生成，该应用也称 OAuth 客户端。
- **Client Secret**（客户端密钥）：创建 Pushbullet 应用时生成，该应用也称 OAuth 客户端。

要生成 **Client ID** 和 **Client Secret**，进入[创建客户端](https://www.pushbullet.com/create-client)页面。从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），将其设置为应用或客户端的 **redirect_uri**。将 OAuth 客户端中的 **client_id** 和 **client_secret** 填入 n8n 凭据。

更多信息请参阅 Pushbullet [OAuth2 指南](https://docs.pushbullet.com/#oauth2)。

{% hint style="info" %}
**Pushbullet OAuth 测试链接**

Pushbullet 在上述客户端创建流程中提供测试链接，但此链接与 n8n 不兼容。要验证身份验证是否有效，请使用 n8n 中的 **Connect my account**（连接我的账户）按钮。
{% endhint %}

