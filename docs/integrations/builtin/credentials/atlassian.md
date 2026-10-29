---
title: Atlassian 凭据
description: Atlassian 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Atlassian 的身份验证。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Atlassian 凭据 <a id="atlassian-credentials"></a>

**Atlassian OAuth2 API** 凭据是适用于 [Atlassian Cloud](https://www.atlassian.com/) 的通用 OAuth2 凭据。

{% hint style="info" %}
**选择凭据类型**

产品专用凭据 [Jira SW Cloud OAuth2 API](jira.md) 和 [Confluence Cloud OAuth2 API](confluence.md) 基于此凭据构建，适合 Jira 和 Confluence 节点，会请求这些节点所需的作用域。通用 **Atlassian OAuth2 API** 凭据适用于高级场景，例如在 HTTP Request 节点中自行定义作用域。
{% endhint %}

## 前置条件 <a id="prerequisites"></a>

- 要访问的产品（例如 Jira 或 Confluence）的 [Atlassian Cloud](https://www.atlassian.com/) 站点。
- [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/) 的访问权限。

## 支持的身份验证方式 <a id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a id="related-resources"></a>

有关该服务的更多信息，请参阅 Atlassian 文档中的 [OAuth 2.0（3LO）应用](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/)。

## 使用 OAuth2 <a id="using-oauth2"></a>

配置此凭据需要一个 [Atlassian Cloud](https://www.atlassian.com/) 站点，以及 [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/) 的访问权限。

然后：

1. 打开 [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/)，选择 **Create**（创建）> **OAuth 2.0 integration**（OAuth 2.0 集成）。
2. 输入应用的 **Name**（名称），同意条款，再选择 **Create**（创建）。
3. 在左侧边栏选择 **Authorization**（授权）。
4. 在 **OAuth 2.0 (3LO)** 旁选择 **Add**（添加）。
5. 在 n8n 中复制 **OAuth Redirect URL**（OAuth 重定向 URL）。
6. 将该 URL 粘贴到 Atlassian Developer Console 的 **Callback URL**（回调 URL）字段。
7. 选择 **Save changes**（保存更改）。
8. 在左侧边栏选择 **Permissions**（权限），再选择要访问的各产品 API（例如 **Jira API** 或 **Confluence API**）旁的 **Add**（添加）。
9. 在每个已添加的 API 旁选择 **Configure**（配置），再选择 **Edit Scopes**（编辑作用域），启用计划请求的作用域。
10. 在左侧边栏选择 **Settings**（设置）。
11. 复制 **Client ID**（客户端 ID），粘贴到 n8n。
12. 复制 **Secret**（秘密值），粘贴到 n8n 的 **Client Secret**（客户端密钥）。
13. 在 **Scope**（作用域）中输入以空格分隔的待请求作用域列表，例如 `read:jira-work read:page:confluence offline_access`。
14. 选择 **Connect my account**（连接我的账户），按照提示完成 OAuth2 流程。

{% hint style="warning" %}
**在应用中启用每个请求的作用域**

如果凭据请求了 OAuth 应用未启用的作用域，Atlassian 会拒绝授权请求。必须在 Atlassian Developer Console 的 **Permissions**（权限）> **Edit Scopes**（编辑作用域）中，同样启用你在 n8n 的 **Scope**（作用域）字段填写的每个作用域。`offline_access` 是例外：Atlassian 会在请求时自动授予它，因此只需填入 **Scope** 字段。此作用域用于刷新令牌，让连接无需你再次登录即可持续工作。
{% endhint %}

可用作用域，请参阅 Atlassian 文档中的 [Jira 作用域](https://developer.atlassian.com/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/)和 [Confluence 作用域](https://developer.atlassian.com/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/)。
