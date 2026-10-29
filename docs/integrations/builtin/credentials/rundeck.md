---
title: Rundeck 凭据
description: Rundeck 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Rundeck 的身份验证。
contentType:
- integration
- reference
nodeTitle: Rundeck 凭据
originalFilePath: integrations/builtin/credentials/rundeck.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/rundeck
url: https://docs.n8n.io/integrations/builtin/credentials/rundeck
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Rundeck 凭据 <a href="#rundeck-credentials" id="rundeck-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Rundeck](../app-nodes/n8n-nodes-base.rundeck.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在 [Rundeck](https://www.rundeck.com/) 服务器上创建用户账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Rundeck API 文档](https://docs.rundeck.com/docs/api/)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要：

- 你的 **URL**：输入 Rundeck 服务器的基础 URL，例如 `http://myserver:4440`。更多信息请参阅 [URL](https://docs.rundeck.com/docs/api/#urls)。
- 一个用户 API **Token（令牌）**：进入 **Profile > User API Tokens（个人资料 > 用户 API 令牌）**，生成令牌。更多信息请参阅[用户 API 令牌](https://docs.rundeck.com/docs/manual/10-user.html#user-api-tokens)。

