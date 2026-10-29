---
title: Jira 凭据
description: Jira 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Jira 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Jira 凭据
originalFilePath: integrations/builtin/credentials/jira.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/jira
url: https://docs.n8n.io/integrations/builtin/credentials/jira
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Jira 凭据 <a href="#jira-credentials" id="jira-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Jira](../app-nodes/n8n-nodes-base.jira.md)
- [Jira Trigger（触发器）](../trigger-nodes/n8n-nodes-base.jiratrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建 [Jira](https://www.atlassian.com/software/jira) Software Cloud 或 Server 账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- [SW Cloud OAuth2](#using-sw-cloud-oauth2)：使用 [Jira Software Cloud](https://www.atlassian.com/software/jira) 进行 OAuth2 身份验证时，使用此方式。
- [SW Cloud API token](#using-sw-cloud-api-token)：使用 [Jira Software Cloud](https://www.atlassian.com/software/jira) 时，使用此方式。
- [SW Server account](#using-sw-server-account)：使用 [Jira Software Server](https://www.atlassian.com/software/jira/download.) 时，使用此方式。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Jira API 文档](https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/#about)。

## 使用 SW Cloud OAuth2 <a href="#using-sw-cloud-oauth2" id="using-sw-cloud-oauth2"></a>

配置此凭据需要一个 [Jira Software Cloud](https://www.atlassian.com/software/jira) 账户，以及 [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/) 的访问权限。

然后：

1. 打开 [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/)，选择 **Create**（创建）> **OAuth 2.0 integration**（OAuth 2.0 集成）。
2. 输入应用的 **Name**（名称），同意条款，再选择 **Create**（创建）。
3. 在左侧边栏选择 **Authorization**（授权）。
4. 在 **OAuth 2.0 (3LO)** 旁选择 **Add**（添加）。
5. 在 n8n 中复制 **OAuth Redirect URL**（OAuth 重定向 URL）。
6. 将该 URL 粘贴到 Atlassian Developer Console 的 **Callback URL**（回调 URL）字段。
7. 选择 **Save changes**（保存更改）。
8. 在左侧边栏选择 **Permissions**（权限），再选择 **Jira API** 旁的 **Add**（添加）。
9. 在 **Jira API** 旁选择 **Configure**（配置）> **Edit Scopes**（编辑作用域）。至少启用以下作用域，再保存修改：
	- `read:jira-user`
	- `read:jira-work`
	- `write:jira-work`
	- `manage:jira-webhook`
10. 在左侧边栏选择 **Settings**（设置）。
11. 复制 **Client ID**（客户端 ID），粘贴到 n8n。
12. 复制 **Secret**（秘密值），粘贴到 n8n 的 **Client Secret**（客户端密钥）。
13. 输入访问 Jira 的 **Site URL**（站点 URL），例如 `https://example.atlassian.net`。
14. 选择 **Connect to Jira SW Cloud**（连接到 Jira SW Cloud），按照提示完成 OAuth2 流程。

{% hint style="info" %}
**创建和删除用户需要额外作用域**

Jira 节点的 **User > Create**（用户 > 创建）和 **User > Delete**（用户 > 删除）操作调用的端点要求 `manage:jira-configuration` 作用域，它不在默认作用域中。如需使用这两个操作，请在 Atlassian Developer Console 的 OAuth 应用中启用 `manage:jira-configuration`，在凭据中开启 **Custom Scopes**（自定义作用域），将该作用域添加到列表中，然后重新连接。Jira 节点的其余操作均可使用默认作用域。
{% endhint %}

{% hint style="warning" %}
**在应用中启用每个请求的作用域**

如果凭据请求了 OAuth 应用未启用的作用域，Atlassian 会拒绝授权请求。请确保在 Atlassian Developer Console 中启用上述全部作用域。凭据还会请求 `offline_access`，Atlassian 会在请求时自动授予它。此作用域用于刷新令牌，让连接无需你再次登录即可持续工作。
{% endhint %}

更多信息，请参阅 Atlassian 文档中的 [OAuth 2.0（3LO）应用](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/)。

## 使用 SW Cloud API 令牌 <a href="#using-sw-cloud-api-token" id="using-sw-cloud-api-token"></a>

配置此凭据需要一个 [Jira Software Cloud](https://www.atlassian.com/software/jira) 账户。

然后：

1. 登录 Atlassian 个人资料，进入 **Security > API tokens**（安全 > API 令牌）页面，或通过此[链接](https://id.atlassian.com/manage-profile/security/api-tokens)直接打开。
2. 选择 **Create API Token**（创建 API 令牌）。
3. 输入令牌的 **Name**（名称），例如 `n8n integration`。
4. 设置 **Expires on**（到期日期），或保留默认日期。
5. 选择 **Create**（创建）。
6. 复制 API 令牌。
7. 在 n8n 中输入 Jira 账户关联的 **Email**（电子邮箱）地址。
8. 将复制的 API 令牌粘贴到 **API Token**（API 令牌）。
9. 输入访问 Jira 的 **Domain**（域名），例如 `https://example.atlassian.net`。

更多信息，请参阅[管理 Atlassian 账户的 API 令牌](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/)。

{% hint style="info" %}
**新令牌**

新令牌最长可能需要一分钟才会生效。如果首次凭据验证失败，请等待一分钟后重试。
{% endhint %}

## 使用 SW Server 账户 <a href="#using-sw-server-account" id="using-sw-server-account"></a>

配置此凭据需要一个 [Jira Software Server](https://www.atlassian.com/software/jira/download.) 账户。

然后：

1. 输入 Jira 账户关联的 **Email**（电子邮箱）地址。
2. 输入 Jira 账户的 **Password**（密码）。
3. 输入访问 Jira 的 **Domain**（域名）。

