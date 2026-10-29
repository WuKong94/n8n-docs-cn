---
title: Twist 凭据
description: Twist 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Twist 的身份验证。
contentType:
- integration
- reference
nodeTitle: Twist 凭据
originalFilePath: integrations/builtin/credentials/twist.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/twist
url: https://docs.n8n.io/integrations/builtin/credentials/twist
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Twist 凭据 <a href="#twist-credentials" id="twist-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Twist](../app-nodes/n8n-nodes-base.twist.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Twist](https://twist.com/) 账号。
- [创建通用集成](https://twist.com/app_console/create_app)，并配置有效的 OAuth 重定向 URL。更多信息，请参阅[使用 OAuth2](#using-oauth2)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务身份验证的更多信息，请参阅 [Twist API 文档](https://developer.twist.com/v3/#authorization)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>
配置此凭据需要：

- 一个 **Client ID**（客户端 ID）：创建通用集成后生成。
- 一个 **Client Secret**（客户端密钥）：创建通用集成后生成。

如需生成 Client ID 和 Client Secret，请[创建通用集成](https://twist.com/app_console/create_app)。

为集成的 **OAuth Authentication**（OAuth 身份验证）使用以下设置：

- 从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），将其填入 Twist 的 **OAuth 2 redirect URL**（OAuth 2 重定向 URL）。<br>
    
    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>自托管 n8n 的 OAuth 重定向 URL</strong></p><p>Twist 不接受 <code>localhost</code> 重定向 URL。重定向 URL 应使用你的域名，例如：<code>https://mytemplatemaker.example.com/gr_callback</code>。如果 n8n 的 <strong>OAuth Redirect URL（OAuth 重定向 URL）</strong> 包含 localhost，请参阅下方的<a href="#local-environment-redirect-url">本地环境重定向 URL</a>，生成 Twist 允许使用的 URL。</p></div>

- 选择 **Update OAuth settings**（更新 OAuth 设置），保存更改。
- 从 Twist 复制 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥），填入 n8n 中的对应字段。

### 本地环境重定向 URL <a href="#local-environment-redirect-url" id="local-environment-redirect-url"></a>

Twist 不接受 localhost 回调 URL。可按以下步骤，为本地环境配置 OAuth 凭据：

1. 使用 [ngrok](https://ngrok.com/) 将运行在 `5678` 端口的本地服务器暴露到互联网。在终端运行以下命令：
```sh
ngrok http 5678
```
2. 在新终端运行以下命令。将 `<YOUR-NGROK-URL>` 替换为上一步获取的 URL。`N8N_WEBHOOK_URL` 从 n8n 2.30.0 起可用；更早版本请使用 `WEBHOOK_URL`。
```sh
export N8N_WEBHOOK_URL=<YOUR-NGROK-URL>
```
3. 将生成的 URL 用作 Twist 的 **OAuth 2 redirect URL**（OAuth 2 重定向 URL）。

