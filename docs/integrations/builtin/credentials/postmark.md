---
title: Postmark 凭据
description: Postmark 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Postmark 的身份验证。
contentType:
- integration
- reference
nodeTitle: Postmark 凭据
originalFilePath: integrations/builtin/credentials/postmark.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/postmark
url: https://docs.n8n.io/integrations/builtin/credentials/postmark
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Postmark 凭据 <a href="#postmark-credentials" id="postmark-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Postmark Trigger（触发器）](../trigger-nodes/n8n-nodes-base.postmarktrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在 Postmark 服务器上创建一个 [Postmark](https://postmarkapp.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Postmark API 文档](https://postmarkapp.com/developer/api/overview)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要：

- 一个 **Server API Token（服务器 API 令牌）**：账号所有者、账号管理员，以及拥有该服务器管理权限的用户可以访问此令牌。在 Postmark 服务器下的 [**API Tokens（API 令牌）**](https://account.postmarkapp.com/api_tokens) 标签页获取。更多信息请参阅 [API 身份验证](https://postmarkapp.com/developer/api/overview#authentication)。
