---
title: Grist 凭据
description: Grist 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Grist 的身份验证。
contentType:
- integration
- reference
nodeTitle: Grist 凭据
originalFilePath: integrations/builtin/credentials/grist.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/grist
url: https://docs.n8n.io/integrations/builtin/credentials/grist
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Grist 凭据 <a href="#grist-credentials" id="grist-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Grist](../app-nodes/n8n-nodes-base.grist.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Grist](https://getgrist.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Grist API 文档](https://support.getgrist.com/api/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **API Key**（API 密钥）：在 Grist 中打开右上角的账户菜单，进入 **Account settings**（账户设置）> **Developer**（开发者），创建或复制 API 密钥。更多信息，请参阅 [Grist API 身份验证文档](https://support.getgrist.com/rest-api/#authentication)。
- **Grist URL**：让 n8n 连接到指定的 Grist 服务器：
    - 默认值 `https://api.getgrist.com` 适用于托管版 Grist（getgrist.com）上的任何账户。
    - 如需将连接限定到单个团队，请使用 `https://YOUR_TEAM.getgrist.com`。
    - 自行管理的实例请使用其实例 URL（例如 `https://grist.example.com`）。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

自行管理的 Grist 中，OAuth 应用属于[完整 Grist 版本](https://support.getgrist.com/self-managed/#how-do-i-enable-the-full-edition-of-grist)的功能。如果实例不提供此功能，请使用 API 密钥。

配置此凭据需要：

- **Client ID**（客户端 ID）：注册 OAuth 应用时，由 Grist 提供。
- **Client Secret**（客户端密钥）：注册 OAuth 应用时，由 Grist 提供。
- **Grist URL**：让 n8n 连接到指定的 Grist 服务器：
    - 默认值 `https://api.getgrist.com` 适用于托管版 Grist（getgrist.com）上的任何账户。
    - 如需将连接限定到单个团队，请使用 `https://YOUR_TEAM.getgrist.com`。
    - 自行管理的实例请使用其实例 URL（例如 `https://grist.example.com`）。

注册应用并连接的步骤如下：

1. 在 n8n 中开始创建 **Grist OAuth2 API** 凭据，并复制 **OAuth Redirect URL**（OAuth 重定向 URL）。
2. 在 Grist 中打开右上角的账户菜单，进入 **Account settings**（账户设置）> **Developer**（开发者）。
3. 在 **OAuth apps**（OAuth 应用）部分，选择 **Register app**（注册应用）。输入 **Application name**（应用名称），例如 `n8n`，并将 n8n 重定向 URL 粘贴为 **Redirect URI**（重定向 URI）。
4. 选择以下作用域：`offline_access`、`doc:read` 和 `doc:write`。
5. 选择 **Register**（注册），再复制 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）。Grist 只显示一次密钥。
6. 返回 n8n，输入 Client ID 和 Client Secret，再选择 **Connect my account**（连接我的账户）。
7. 在 Grist 授权页面，选择凭据可访问的资源范围：**All documents (now and in the future)**（当前及未来的所有文档），或通过 **Selected resources**（选定资源）选择具体文档、工作区或站点。然后选择 **Authorize**（授权）。

步骤 7 的选择会在作用域限制之外进一步缩小凭据权限。Grist 在每次调用时强制执行此限制：即使你本人可以打开某文档，请求授权范围外的该文档仍会失败。将凭据限定到单个文档，是让工作流仅访问所需数据的好方法。如需之后修改选择，或单独撤销某凭据的访问权限，进入 Grist 的 **Account settings**（账户设置）> **Authorized apps**（已授权应用）。

授权的工作方式及管理方法，请参阅 [Grist 已连接应用文档](https://support.getgrist.com/connected-apps/)；注册应用的详情，请参阅 [Grist OAuth 应用文档](https://support.getgrist.com/oauth-apps/)。

{% hint style="info" %}
**注册应用时包含凭据请求的每个作用域**

Grist 会拒绝请求未在应用注册时声明的作用域的授权，连接会失败并返回 `invalid_scope` 错误。如果注册应用时仅选择了较少作用域，请使用[自定义作用域](#setting-custom-scopes)，仅请求这些作用域。
{% endhint %}

{% hint style="info" %}
**至少每月使用一次凭据**

Grist 的刷新令牌在 60 天后过期。至少每 30 天运行一次工作流，可使凭据持续有效。如果凭据闲置时间更长，请通过 **Connect my account**（连接我的账户）重新连接。API 密钥凭据不会过期。
{% endhint %}

## 设置自定义权限范围 <a href="#setting-custom-scopes" id="setting-custom-scopes"></a>

Grist OAuth2 凭据默认使用以下作用域：

* `offline_access`
* `doc:read`
* `doc:write`

如需为凭据选择其他作用域，请启用 **Custom Scopes**（自定义作用域）开关，编辑 **Enabled Scopes**（已启用的作用域）列表。使用更严格的作用域时，部分功能可能无法正常运行。例如，没有 `doc:write` 的凭据可以读取记录，但无法创建、更新或删除。全部可用作用域，请参阅 [Grist OAuth 作用域](https://support.getgrist.com/oauth-apps/#scopes)。

