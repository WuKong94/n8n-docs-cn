---
title: Paddle 凭据
description: Paddle 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Paddle 的身份验证。
contentType:
- integration
- reference
nodeTitle: Paddle 凭据
originalFilePath: integrations/builtin/credentials/paddle.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/paddle
url: https://docs.n8n.io/integrations/builtin/credentials/paddle
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Paddle 凭据 <a href="#paddle-credentials" id="paddle-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Paddle](../app-nodes/n8n-nodes-base.paddle.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Paddle](https://paddle.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token (Classic)（Classic API 访问令牌）

{% hint style="warning" %}
**Paddle Classic API**

此凭据适用于 Paddle Classic API。如果在 2023 年 8 月之后加入 Paddle，则使用的是 [Paddle Billing API](https://developer.paddle.com/api-reference/overview)，此凭据可能不适用。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Paddle Classic API 文档](https://developer.paddle.com/classic/api-reference/1384a288aca7a-api-reference)。

## 使用 API 访问令牌（Classic） <a href="#using-api-access-token-classic" id="using-api-access-token-classic"></a>

配置此凭据需要：

- **Vendor Auth Code**（供应商授权码）：生成 API 密钥时创建。
- **Vendor ID**（供应商 ID）：生成 API 密钥时显示。
- **Use Sandbox Environment API**（使用沙盒环境 API）：开启后，使用此凭据的节点会请求沙盒 API 端点，而非正式 API 端点。

要生成授权码并查看 Vendor ID，进入 **Paddle > Developer Tools > Authentication > Generate Auth Code**（Paddle > 开发者工具 > 身份验证 > 生成授权码）。选择 **Reveal Auth Code**（显示授权码）。更多信息请参阅 [API 身份验证](https://developer.paddle.com/api-reference/about/authentication)。
