---
title: Cockpit 凭据
description: Cockpit 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Cockpit 的身份验证。
contentType:
- integration
- reference
nodeTitle: Cockpit 凭据
originalFilePath: integrations/builtin/credentials/cockpit.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/cockpit
url: https://docs.n8n.io/integrations/builtin/credentials/cockpit
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Cockpit 凭据 <a href="#cockpit-credentials" id="cockpit-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Cockpit](../app-nodes/n8n-nodes-base.cockpit.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Cockpit](https://getcockpit.com/) 账号。
- 设置一个[自托管的 Cockpit 实例](https://getcockpit.com/documentation/core/quickstart/installation)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Cockpit API 文档](https://getcockpit.com/documentation/core/api/introduction)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要：

- 你的 **Cockpit URL**：用于访问 Cockpit 实例的 URL
- 一个 **Access Token（访问令牌）**：创建 API 令牌的方法，请参阅 [Cockpit 令牌管理文档](https://getcockpit.com/documentation/core/api/authentication/#managing-tokens)。将 **API token** 填入 n8n 的 **Access Token** 字段。

