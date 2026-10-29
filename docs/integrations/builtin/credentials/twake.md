---
title: Twake 凭据
description: Twake 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Twake 的身份验证。
contentType:
- integration
- reference
nodeTitle: Twake 凭据
originalFilePath: integrations/builtin/credentials/twake.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/twake
url: https://docs.n8n.io/integrations/builtin/credentials/twake
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Twake 凭据 <a href="#twake-credentials" id="twake-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Twake](../app-nodes/n8n-nodes-base.twake.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Twake](https://twake.app/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Cloud API key（云 API 密钥）
- Server API key（服务器 API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Twake 文档](https://doc.twake.app/developers-api/api-reference)。

## 使用云 API 密钥 <a href="#using-cloud-api-key" id="using-cloud-api-key"></a>

配置此凭据需要：

- **Workspace Key**（工作区密钥）：在 Twake Cloud 环境中安装 **n8n** 应用并选择 **Configure**（配置）时生成。详细说明，请参阅[如何将 n8n 连接到 Twake](https://help.twake.app/en/latest/applications/connectors/index.html#how-to-connect-n8n-to-twake)。

## 使用服务器 API 密钥 <a href="#using-server-api-key" id="using-server-api-key"></a>

配置此凭据需要：

- **Host URL**（主机 URL）：Twake 自托管实例的 URL。
- **Public ID**（公开 ID）：创建应用时生成。
- **Private API Key**（私有 API 密钥）：创建应用时生成。

如需生成 **Public ID**（公开 ID）和 **Private API Key**（私有 API 密钥），请[创建 Twake 应用](https://doc.twake.app/developers-api/get-started/create-your-first-application)：

1. 进入 **Workspace Settings > Applications and connectors > Access your applications and connectors > Create an application**（工作区设置 > 应用与连接器 > 访问应用与连接器 > 创建应用）。
2. 输入适当的信息。
3. 创建应用后，查看其 **API Details**（API 详情）。
4. 复制 **Public identifier**（公开标识符），填入 n8n 的 **Public ID**（公开 ID）。
5. 复制 **Private key**（私有密钥），填入 n8n 的 **Private API Key**（私有 API 密钥）。

更多信息，请参阅 [API 设置](https://doc.twake.app/developers-api/get-started/create-your-first-application#id-3.-api-settings)。
