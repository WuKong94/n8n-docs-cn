---
title: Zammad 凭据
description: Zammad 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Zammad 的身份验证。
contentType:
- integration
- reference
nodeTitle: Zammad 凭据
originalFilePath: integrations/builtin/credentials/zammad.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/zammad
url: https://docs.n8n.io/integrations/builtin/credentials/zammad
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Zammad 凭据 <a href="#zammad-credentials" id="zammad-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Zammad](../app-nodes/n8n-nodes-base.zammad.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建托管的 [Zammad](https://zammad.com/) 账户，或部署自己的 Zammad 实例。
- 使用令牌身份验证时，请在 **Settings > System > API**（设置 > 系统 > API）中启用 **API Token Access**（API 令牌访问）。更多信息请参阅 [Zammad API 简介](https://docs.zammad.org/en/latest/api/intro.html)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）
- Token auth（令牌身份验证）：Zammad 推荐使用此身份验证方式。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的身份验证详情，请参阅 [Zammad API 身份验证文档](https://docs.zammad.org/en/latest/api/intro.html?#authentication)。

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

配置此凭据需要：

- 一个 **Base URL**（基础 URL）：输入 Zammad 实例的 URL。
- 一个 **Email（电子邮件）** 地址：输入用于登录 Zammad 的邮箱地址。
- 一个 **Password（密码）**：输入 Zammad 密码。
- **Ignore SSL Issues**（忽略 SSL 问题）：开启后，即使 SSL 证书验证失败，n8n 仍会连接。

## 使用令牌身份验证 <a href="#using-token-auth" id="using-token-auth"></a>

配置此凭据需要：

- 一个 **Base URL**（基础 URL）：输入 Zammad 实例的 URL。
- 一个 **Access Token**（访问令牌）：为 Zammad 实例启用 **API Token Access**（API 令牌访问）后，任何具有 `user_preferences.access_token` 权限的用户，都可进入**头像 > Profile > Token Access**（个人资料 > 令牌访问），选择 **Create**（创建）来生成新的 **Access Token**。
    - 访问令牌的权限取决于你希望通过此凭据完成哪些操作。要使用 [Zammad](../app-nodes/n8n-nodes-base.zammad.md) 节点的全部功能，请选择：
        - `admin.group`
        - `admin.organization`
        - `admin.user`
        - `ticket.agent`
        - `ticket.customer`
- **Ignore SSL Issues**（忽略 SSL 问题）：开启后，即使 SSL 证书验证失败，n8n 仍会连接。

