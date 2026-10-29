---
title: Quick Base 凭据
description: Quick Base 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Quick Base 的身份验证。
contentType:
- integration
- reference
nodeTitle: Quick Base 凭据
originalFilePath: integrations/builtin/credentials/quickbase.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/quickbase
url: https://docs.n8n.io/integrations/builtin/credentials/quickbase
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Quick Base 凭据 <a href="#quick-base-credentials" id="quick-base-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Quick Base](../app-nodes/n8n-nodes-base.quickbase.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Quick Base](https://www.quickbase.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Quick Base API 文档](https://developer.quickbase.com/auth/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **Hostname（主机名）**：即 Quick Base URL 中位于 `https://` 与 `/db` 之间的字符串。
- 一个 **User Token（用户令牌）**：选择 **Profile > My preferences > My User Information > Manage my user tokens（个人资料 > 我的偏好设置 > 我的用户信息 > 管理我的用户令牌）**，生成令牌。详细说明请参阅[创建和使用用户令牌](https://help.quickbase.com/docs/create-and-use-user-tokens)。

