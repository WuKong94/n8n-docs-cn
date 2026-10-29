---
title: NocoDB 凭据
description: NocoDB 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 NocoDB 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: NocoDB 凭据
originalFilePath: integrations/builtin/credentials/nocodb.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/nocodb
url: https://docs.n8n.io/integrations/builtin/credentials/nocodb
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# NocoDB 凭据 <a href="#nocodb-credentials" id="nocodb-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [NocoDB](../app-nodes/n8n-nodes-base.nocodb.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌，推荐）
- User auth token（用户身份验证令牌）

{% hint style="warning" %}
**功能可用范围**

NocoDB 从 v0.205.1 起弃用用户身份验证令牌，请改用 [API 令牌](#using-api-token)。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [NocoDB API 文档](https://data-apis-v2.nocodb.com/)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要一个 [NocoDB](https://www.nocodb.com/) 实例，以及：

- 一个 **API Token（API 令牌）**
- 数据库的 **Host**（主机）

生成 API 令牌的步骤如下：

1. 登录 NocoDB，选择左侧边栏底部的 **User menu**（用户菜单）。
2. 选择 **Account Settings**（账户设置）。
3. 打开 **Tokens**（令牌）选项卡。
4. 选择 **Add new API token**（添加新的 API 令牌）。
5. 输入令牌的 **Name**（名称），例如 `n8n integration`。
6. 选择 **Save**（保存）。
7. 复制 **API Token**（API 令牌），填入 n8n 凭据。
8. 将 NocoDB 实例的 **Host**（主机）填入 n8n 凭据，例如 `http://localhost:8080`。

更详细的说明，请参阅 NocoDB 的 [API 令牌文档](https://docs.nocodb.com/account-settings/api-tokens/)。

## 使用用户身份验证令牌 <a href="#using-user-auth-token" id="using-user-auth-token"></a>

在被 NocoDB 弃用前，用户身份验证令牌是一种用于快速试用 API 的临时令牌，在用户注销前的会话期间有效，或有效期为 10 小时。

{% hint style="warning" %}
**功能可用范围**

NocoDB 从 v0.205.1 起弃用用户身份验证令牌，请改用 [API 令牌](#using-api-token)。
{% endhint %}

配置此凭据需要一个 [NocoDB](https://www.nocodb.com/) 实例，以及：

- **User Token**（用户令牌）
- 数据库的 **Host**（主机）

生成用户身份验证令牌的步骤如下：

1. 登录 NocoDB，选择左侧边栏底部的 **User menu**（用户菜单）。
2. 选择 **Copy Auth token**（复制身份验证令牌）。
3. 将该身份验证令牌填入 n8n 的 **User Token**（用户令牌）。
4. 输入 NocoDB 实例的 **Host**（主机），例如 `http://localhost:8080`。

更多信息，请参阅 NocoDB 的 [Auth Tokens（身份验证令牌）文档](https://docs.nocodb.com/account-settings/api-tokens/#auth-tokens)。
