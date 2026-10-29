---
title: Gotify 凭据
description: Gotify 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Gotify 的身份验证。
contentType:
- integration
- reference
nodeTitle: Gotify 凭据
originalFilePath: integrations/builtin/credentials/gotify.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/gotify
url: https://docs.n8n.io/integrations/builtin/credentials/gotify
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Gotify 凭据 <a href="#gotify-credentials" id="gotify-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Gotify](../app-nodes/n8n-nodes-base.gotify.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在服务器上安装 [Gotify](https://gotify.net/docs/install)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Gotify API 文档](https://gotify.net/api-docs)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要：

- 一个 **App API Token（应用 API 令牌）**：仅在使用此凭据创建消息时需要。在 **Apps（应用）** 菜单中创建应用，即可生成 App API 令牌。更多信息请参阅 [Gotify 推送消息文档](https://gotify.net/docs/pushmsg)。
- 一个 **Client API Token（客户端 API 令牌）**：除创建消息之外的所有操作都需要此令牌，例如删除或获取消息。在 **Clients（客户端）** 菜单中创建客户端，即可生成 Client API 令牌。
- Gotify 主机的 **URL**

