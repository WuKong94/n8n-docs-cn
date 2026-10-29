---
title: Taiga 凭据
description: Taiga 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Taiga 的身份验证。
contentType:
- integration
- reference
nodeTitle: Taiga 凭据
originalFilePath: integrations/builtin/credentials/taiga.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/taiga
url: https://docs.n8n.io/integrations/builtin/credentials/taiga
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Taiga 凭据 <a href="#taiga-credentials" id="taiga-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Taiga](../app-nodes/n8n-nodes-base.taiga.md)
- [Taiga Trigger（触发器）](../trigger-nodes/n8n-nodes-base.taigatrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Taiga](https://taiga.io/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Taiga API 文档](https://docs.taiga.io/api.html)。

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

配置此凭据需要：

- **Username**（用户名）：输入用户名或用户邮箱地址。更多信息请参阅[普通登录](https://docs.taiga.io/api.html#auth-normal-login)。
- **Password**（密码）：输入密码。
- **Environment**（环境）：选择 **Cloud**（云端）或 **Self-Hosted**（自托管）。自托管实例还需要添加：
    - **URL**：输入 Taiga URL。

