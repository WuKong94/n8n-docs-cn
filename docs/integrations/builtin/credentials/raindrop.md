---
title: Raindrop 凭据
description: Raindrop 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Raindrop 的身份验证。
contentType:
- integration
- reference
nodeTitle: Raindrop 凭据
originalFilePath: integrations/builtin/credentials/raindrop.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/raindrop
url: https://docs.n8n.io/integrations/builtin/credentials/raindrop
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Raindrop 凭据 <a href="#raindrop-credentials" id="raindrop-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Raindrop](../app-nodes/n8n-nodes-base.raindrop.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Raindrop](https://raindrop.io/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Raindrop API 文档](https://developer.raindrop.io/)。

## 使用 OAuth <a href="#using-oauth" id="using-oauth"></a>

配置此凭据需要：

- 一个 **Client ID（客户端 ID）**
- 一个 **Client Secret（客户端密钥）**

创建 Raindrop 应用即可生成这两个值。

进入 **Settings >** [**Integrations**](https://app.raindrop.io/settings/integrations)（设置 > 集成），在 **For Developers**（开发者）部分选择 **+ Create new app**（创建新应用）。

为应用采用以下设置：

- 从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），将其添加为应用的 **Redirect URI**（重定向 URI）。
- 从 Raindrop 应用复制 **Client ID** 和 **Client Secret**，填入 n8n 凭据。

