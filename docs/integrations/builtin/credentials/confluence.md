---
title: Confluence 凭据
description: Confluence 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Confluence 的身份验证。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Confluence 凭据 <a id="confluence-credentials"></a>

使用 **Confluence Cloud OAuth2 API** 凭据，在 n8n 中完成 [Confluence Cloud](https://www.atlassian.com/software/confluence) 的身份验证。

## 前置条件 <a id="prerequisites"></a>

- [Confluence Cloud](https://www.atlassian.com/software/confluence) 站点。
- [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/) 的访问权限。

## 支持的身份验证方式 <a id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a id="related-resources"></a>

有关该服务的更多信息，请参阅 Atlassian 文档中的 [OAuth 2.0（3LO）应用](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/)和[适用于 OAuth 2.0（3LO）与 Forge 应用的 Confluence 作用域](https://developer.atlassian.com/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/)。

## 使用 OAuth2 <a id="using-oauth2"></a>

配置此凭据需要一个 [Confluence Cloud](https://www.atlassian.com/software/confluence) 站点，以及 [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/) 的访问权限。

然后：

1. 打开 [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/)，选择 **Create**（创建）> **OAuth 2.0 integration**（OAuth 2.0 集成）。
2. 输入应用的 **Name**（名称），同意条款，再选择 **Create**（创建）。
3. 在左侧边栏选择 **Authorization**（授权）。
4. 在 **OAuth 2.0 (3LO)** 旁选择 **Add**（添加）。
5. 在 n8n 中复制 **OAuth Redirect URL**（OAuth 重定向 URL）。
6. 将该 URL 粘贴到 Atlassian Developer Console 的 **Callback URL**（回调 URL）字段。
7. 选择 **Save changes**（保存更改）。
8. 在左侧边栏选择 **Permissions**（权限），再选择 **Confluence API** 旁的 **Add**（添加）。
9. 在 **Confluence API** 旁选择 **Configure**（配置）> **Edit Scopes**（编辑作用域）。在细粒度作用域中启用以下作用域，再保存修改：
	- `read:page:confluence`
	- `write:page:confluence`
	- `read:hierarchical-content:confluence`
	- `read:space:confluence`
	- `read:attachment:confluence`
	- `read:comment:confluence`
	- `read:label:confluence`
	- `read:content-details:confluence`
	- `write:attachment:confluence`
	- `delete:attachment:confluence`
	- `write:comment:confluence`
	- `delete:comment:confluence`
	- `write:label:confluence`
	- `delete:page:confluence`
10. 在左侧边栏选择 **Settings**（设置）。
11. 复制 **Client ID**（客户端 ID），粘贴到 n8n。
12. 复制 **Secret**（秘密值），粘贴到 n8n 的 **Client Secret**（客户端密钥）。
13. 选择 **Connect my account**（连接我的账户），按照提示完成 OAuth2 流程。

{% hint style="info" %}
**选择站点**

凭据不存储 Confluence 站点。请在 Confluence 节点的 **Site**（站点）参数中选择站点：从连接可访问的站点列表中选择，或粘贴站点 URL。如果连接只可访问一个站点，可将 **Site** 留空，节点会自动使用该站点。
{% endhint %}

{% hint style="warning" %}
**在应用中启用每个请求的作用域**

如果凭据请求了 OAuth 应用未启用的作用域，Atlassian 会拒绝授权请求。请确保在 Atlassian Developer Console 中启用上述全部作用域。凭据还会请求 `offline_access`，Atlassian 会在请求时自动授予它。此作用域用于刷新令牌，让连接无需你再次登录即可持续工作。
{% endhint %}

### Custom Scopes（自定义作用域） <a id="custom-scopes"></a>

默认情况下，凭据请求上述作用域。如需修改，开启 **Custom Scopes**（自定义作用域），编辑以空格分隔的作用域列表。必须在 Atlassian Developer Console 的 OAuth 应用中，启用每个请求的作用域。

更多信息，请参阅 Atlassian 文档中的 [OAuth 2.0（3LO）应用](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/)。
