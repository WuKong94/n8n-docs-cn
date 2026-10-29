---
title: Eventbrite 凭据
description: Eventbrite 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Eventbrite 的身份验证。
contentType:
- integration
- reference
nodeTitle: Eventbrite 凭据
originalFilePath: integrations/builtin/credentials/eventbrite.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/eventbrite
url: https://docs.n8n.io/integrations/builtin/credentials/eventbrite
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Eventbrite 凭据 <a href="#eventbrite-credentials" id="eventbrite-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Eventbrite Trigger（触发器）](../trigger-nodes/n8n-nodes-base.eventbritetrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Eventbrite](https://www.eventbrite.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API private key（API 私钥）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Eventbrite API 文档](https://www.eventbrite.com/platform/new/api)。

## 使用 API 私钥 <a href="#using-api-private-key" id="using-api-private-key"></a>

配置此凭据需要：

- **Private Key**（私钥）：生成私有令牌的详细步骤，请参阅 [Eventbrite API 身份验证文档中的 Get a Private Token](https://www.eventbrite.com/platform/new/api#/introduction/authentication/1.-get-a-private-token)。将该私有令牌填入 n8n 凭据的 **Private Key** 字段。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果需要从头配置 OAuth2，或了解 OAuth 网页流程的更多细节，请按照 [Eventbrite API 身份验证文档中的 For App Partners](https://www.eventbrite.com/platform/new/api#/introduction/authentication/2.-(for-app-partners)-authorize-your-users) 配置 OAuth。
