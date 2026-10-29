---
title: Baserow 凭据
description: Baserow 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Baserow 的身份验证。
contentType:
- integration
- reference
priority: high
nodeTitle: Baserow 凭据
originalFilePath: integrations/builtin/credentials/baserow.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/baserow
url: https://docs.n8n.io/integrations/builtin/credentials/baserow
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Baserow 凭据 <a href="#baserow-credentials" id="baserow-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Baserow](../app-nodes/n8n-nodes-base.baserow.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在任意托管的 Baserow 实例或自托管实例上创建 [Baserow](https://baserow.io/) 账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）
- Token（令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Baserow 文档](https://baserow.io/docs/index)。

有关 API 本身的更多信息，请参阅 [Baserow 自动生成的 API 文档](https://baserow.io/api-docs)。

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

配置此凭据需要：

- Baserow 的 **Host**（主机）
- 用于登录的 **Username**（用户名）和 **Password**（密码）

按以下步骤操作：

1. 输入 Baserow 实例的 **Host**（主机）：
    - Baserow 托管的实例：保留 `https://api.baserow.io`。
    - 自托管实例：设置为自托管实例的 API URL。
2. 输入 n8n 应使用的用户账户的 **Username**（用户名）。
3. 输入该用户账户的 **Password**（密码）。

创建用户账户的相关信息，请参阅 [Baserow API 身份验证文档](https://baserow.io/docs/apis/rest-api#authentication)。

## 使用令牌 <a href="#using-a-token" id="using-a-token"></a>

配置数据库令牌凭据需要：

- Baserow 的 **Host**（主机）
- 在 Baserow.io 上创建的 **Database token**（数据库令牌），创建时需要使用 **Username**（用户名）和 **Password**（密码）登录。

### 创建数据库令牌 <a href="#creating-the-database-token" id="creating-the-database-token"></a>

1. 在 [Baserow](https://baserow.io/login) 中使用用户名和密码登录。
2. 点击左上角的工作区，选择 **My Settings**（我的设置）。
3. 在打开的页面中，点击 **Database tokens**（数据库令牌）。
4. 点击 **Create token**（创建令牌）。
5. 输入令牌的 **Name**（名称）和 **Workspace**（工作区）。
6. 点击 **Create token**（创建令牌），完成创建。

在 n8n 中创建凭据的步骤如下：

1. 输入 Baserow 实例的 **Host**（主机）：
    - Baserow 托管的实例：保留 `https://api.baserow.io`。
    - 自托管实例：设置为自托管实例的 API URL。
2. 输入刚创建的 **Database Token**（数据库令牌）。
