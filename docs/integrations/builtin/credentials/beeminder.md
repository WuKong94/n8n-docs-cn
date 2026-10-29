---
title: Beeminder 凭据
description: Beeminder 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Beeminder 的身份验证。
contentType:
- integration
- reference
nodeTitle: Beeminder 凭据
originalFilePath: integrations/builtin/credentials/beeminder.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/beeminder
url: https://docs.n8n.io/integrations/builtin/credentials/beeminder
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Beeminder 凭据 <a href="#beeminder-credentials" id="beeminder-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Beeminder](../app-nodes/n8n-nodes-base.beeminder.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Beeminder](https://www.beeminder.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API user token（API 用户令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Beeminder API 文档](https://api.beeminder.com/#beeminder-api-reference)。

## 使用 API 用户令牌 <a href="#using-api-user-token" id="using-api-user-token"></a>

配置此凭据需要：

- **User**（用户名）：应与生成 Auth Token 的用户一致。
- 该用户的个人 **Auth Token**（身份验证令牌），可通过以下任一方式生成：
    - 在图形界面中：进入 **Account Settings**（账户设置）中的 [Apps & API](https://help.beeminder.com/article/110-apps-and-api#API-token)。
    - 在 API 中：调用 [`auth_token` API 端点](https://api.beeminder.com/#auth)。

