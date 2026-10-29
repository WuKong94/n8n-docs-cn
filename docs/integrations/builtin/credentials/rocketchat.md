---
title: Rocket.Chat 凭据
description: Rocket.Chat 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Rocket.Chat 的身份验证。
contentType:
- integration
- reference
nodeTitle: Rocket.Chat 凭据
originalFilePath: integrations/builtin/credentials/rocketchat.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/rocketchat
url: https://docs.n8n.io/integrations/builtin/credentials/rocketchat
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Rocket.Chat 凭据 <a href="#rocketchat-credentials" id="rocketchat-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Rocket.Chat](../app-nodes/n8n-nodes-base.rocketchat.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Rocket.Chat](https://rocket.chat/) 账号。
- 账户必须拥有 `create-personal-access-tokens` 权限，才能生成个人访问令牌。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>


有关该服务的更多信息，请参阅 [Rocket.Chat API 文档](https://developer.rocket.chat/reference/api/rest-api)。


## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要：

- **User ID**（用户 ID）：生成访问令牌时显示。
- **Auth Key**（身份验证密钥）：即个人访问令牌。进入 **avatar > Account > Personal Access Tokens**（头像 > 账户 > 个人访问令牌）生成令牌，再将其复制到 n8n 的 **Auth Key** 字段。
- Rocket.Chat **Domain**（域名）：也称默认 URL 或工作区 URL。

更多信息请参阅[个人访问令牌](https://docs.rocket.chat/docs/manage-your-account-settings#personal-access-tokens)。

