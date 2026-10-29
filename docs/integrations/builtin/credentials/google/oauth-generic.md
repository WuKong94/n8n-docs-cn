---
title: Google OAuth2（通用）
contentType:
- integration
- reference
nodeTitle: Google OAuth2（通用）
originalFilePath: integrations/builtin/credentials/google/oauth-generic.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic
url: https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic
description: 通用 Google OAuth2 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Google 服务的身份验证。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google OAuth2（通用） <a id="google-oauth2-generic"></a>

本文说明如何创建通用 Google OAuth2 API 凭据，以用于[自定义操作](../../custom-api-actions-for-existing-nodes.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/managed-google-oauth.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建 [Google Cloud](https://cloud.google.com/) 账户。

## 设置 OAuth <a href="#set-up-oauth" id="set-up-oauth"></a>

将 n8n 凭据连接到 Google 服务需要五个步骤：

1. [创建 Google Cloud Console 项目](oauth-generic.md#create-a-google-cloud-console-project)。
2. [启用 API](oauth-generic.md#enable-apis)。
3. [配置 OAuth 授权同意页面](oauth-generic.md#configure-your-oauth-consent-screen)。
4. [创建 Google OAuth 客户端凭据](oauth-generic.md#create-your-google-oauth-client-credentials)。
5. [完成 n8n 凭据设置](oauth-generic.md#finish-your-n8n-credential)。

### 创建 Google Cloud Console 项目 <a href="#create-a-google-cloud-console-project" id="create-a-google-cloud-console-project"></a>

首先创建 Google Cloud Console 项目。如果已有项目，请跳到[下一节](oauth-generic.md#enable-apis)：

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/google/create-google-cloud-project.md" %}

### 启用 API <a href="#enable-apis" id="enable-apis"></a>

创建项目后，启用需要访问的 API：

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/google/enable-apis.md" %}

### 配置 OAuth 授权同意页面 <a href="#configure-your-oauth-consent-screen" id="configure-your-oauth-consent-screen"></a>

如果之前未在 Google Cloud 项目中使用 OAuth，需要[配置 OAuth 授权同意页面](https://developers.google.com/workspace/guides/configure-oauth-consent)：

1. 进入 [Google Cloud Console - Library（库）](https://console.cloud.google.com/apis/library)，确认当前位于正确的项目中。

    <figure><img src="../../../.gitbook/assets/google-cloud-project-dropdown (1).png" alt=""><figcaption><p>检查 Google Cloud 顶部导航栏中的项目下拉菜单</p></figcaption></figure>
2. 打开左侧导航菜单，进入 **APIs & Services > OAuth consent screen**（API 和服务 > OAuth 授权同意页面）。Google 会将你重定向到 Google Auth Platform 概览页面。
3. 在 **Overview**（概览）选项卡中选择 **Get started**（开始使用），开始配置 OAuth 授权同意。
4. 输入授权页面中显示的 **App name**（应用名称）和 **User support email**（用户支持邮箱）。选择 **Next**（下一步）继续。
5. 对于 **Audience**（受众），如果只允许组织内 Google Workspace 用户访问，请选择 **Internal**（内部）；如果允许任何具有 Google 账户的用户访问，请选择 **External**（外部）。用户类型的更多信息，请参阅 Google 的[用户类型文档](https://support.google.com/cloud/answer/15549945?sjid=17061891731152303663-EU#user-type)。选择 **Next**（下一步）继续。<br>

    {% hint style="info" %}
    **测试模式和测试用户**

    如果选择 **External**（外部），应用默认处于 Testing（测试）模式。在此模式下，只有手动添加为测试用户的 Google 账户才能完成 OAuth 流程，其他人都会看到“access denied”（访问被拒绝）页面。添加方法请参阅 [Google 尚未验证此应用](oauth-generic.md#google-hasnt-verified-this-app)。
    {% endhint %}
6. 选择 Google 用于联系你、通知项目变更的 **Email addresses**（电子邮件地址）。选择 **Next**（下一步）继续。
7. 阅读并接受 Google 用户数据政策。选择 **Continue**（继续），再选择 **Create**（创建）。
8. 在左侧菜单中选择 **Branding**（品牌信息）。
9. 在 **Authorized domains**（已获授权的网域）部分选择 **Add domain**（添加网域）：
   * 如果使用 n8n Cloud 服务，请添加 `n8n.cloud`
   * 如果[自托管](../../../../deploy/host-n8n/README.md)，请添加 n8n 实例的域名。
10. 在页面底部选择 **Save**（保存）。

### 创建 Google OAuth 客户端凭据 <a href="#create-your-google-oauth-client-credentials" id="create-your-google-oauth-client-credentials"></a>

接下来，在 Google 中创建 OAuth 客户端凭据：

1. 进入 [Google Cloud Console](https://console.cloud.google.com/)，确认当前位于正确的项目中。
2. 在 **APIs & Services**（API 和服务）部分选择 [**Credentials**（凭据）](https://console.cloud.google.com/apis/credentials)。
3. 选择 **+ Create credentials**（+ 创建凭据）> **OAuth client ID**（OAuth 客户端 ID）。
4. 在 **Application type**（应用类型）下拉菜单中选择 **Web application**（Web 应用）。
5. Google 会自动生成 **Name**（名称）。请将其改为能在控制台中辨认的名称。
6. 从 n8n 凭据中复制 **OAuth Redirect URL**（OAuth 重定向 URL），粘贴到 Google Console 的 **Authorized redirect URIs**（已获授权的重定向 URI）中。<br>

    {% hint style="info" %}
    **自托管时的 OAuth 重定向 URL**

    如果在本地计算机上运行 n8n，使用 Google OAuth 无需公共域名、SSL 证书或端口转发。Google 允许在开发时将 localhost 用作有效重定向 URI。n8n 的 OAuth 重定向 URL 类似于 `http://localhost:5678/rest/oauth2-credential/callback`。可接受的重定向 URI 的更多详情，请参阅 [Google 重定向 URI 文档](https://support.google.com/cloud/answer/15549257?hl=en#zippy=%2Cweb-applications)。
    {% endhint %}
7. 选择 **Create**（创建）。

### 完成 n8n 凭据设置 <a href="#finish-your-n8n-credential" id="finish-your-n8n-credential"></a>

Google 项目和凭据配置完成后，完成 n8n 凭据设置：

1. 在 Google 的 **OAuth client created**（已创建 OAuth 客户端）弹窗中复制 **Client ID**（客户端 ID），填入 n8n 凭据。
2. 在同一个 Google 弹窗中复制 **Client Secret**（客户端密钥），填入 n8n 凭据。
3. 必须为此凭据提供作用域。更多信息，请参阅[作用域](oauth-generic.md#scopes)。多个作用域以空格分隔，例如：

    ```
    https://www.googleapis.com/auth/gmail.labels https://www.googleapis.com/auth/gmail.addons.current.action.compose
    ```
4. 在 n8n 中选择 **Sign in with Google**（使用 Google 登录），完成 Google 身份验证。
5. **Save**（保存）新凭据。

## 视频 <a href="#video" id="video"></a>

以下视频演示上述步骤：

{% embed url="https://www.youtube.com/embed/FBGtpWMTppw" %}

## 作用域 <a href="#scopes" id="scopes"></a>

Google 服务具有一个或多个可用访问作用域。作用域会限制用户能够执行的操作。所有服务的作用域列表，请参阅 [Google API 的 OAuth 2.0 作用域](https://developers.google.com/identity/protocols/oauth2/scopes)。

n8n 不支持全部作用域。创建通用 Google OAuth2 API 凭据时，可填写下方**支持的作用域**列表中的作用域。如果输入 n8n 尚未支持的作用域，将无法正常工作。

<details>

<summary>支持的作用域</summary>

| 服务 | 可用作用域 |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Gmail                                       | <ul><li><code>https://www.googleapis.com/auth/gmail.labels</code></li><li><code>https://www.googleapis.com/auth/gmail.addons.current.action.compose</code></li><li><code>https://www.googleapis.com/auth/gmail.addons.current.message.action</code></li><li><code>https://mail.google.com/</code></li><li><code>https://www.googleapis.com/auth/gmail.modify</code></li><li><code>https://www.googleapis.com/auth/gmail.compose</code></li></ul> |
| Google Ads                                  | <ul><li><code>https://www.googleapis.com/auth/adwords</code></li></ul>                                                                                                                                                                                                                                                                                                                                                                           |
| Google Analytics                            | <ul><li><code>https://www.googleapis.com/auth/analytics</code></li><li><code>https://www.googleapis.com/auth/analytics.readonly</code></li></ul>                                                                                                                                                                                                                                                                                                 |
| Google BigQuery                             | <ul><li><code>https://www.googleapis.com/auth/bigquery</code></li></ul>                                                                                                                                                                                                                                                                                                                                                                          |
| Google Books                                | <ul><li><code>https://www.googleapis.com/auth/books</code></li></ul>                                                                                                                                                                                                                                                                                                                                                                             |
| Google Calendar                             | <ul><li><code>https://www.googleapis.com/auth/calendar</code></li><li><code>https://www.googleapis.com/auth/calendar.events</code></li></ul>                                                                                                                                                                                                                                                                                                     |
| <p>Google Cloud<br>Natural Language</p>     | <ul><li><code>https://www.googleapis.com/auth/cloud-language</code></li><li><code>https://www.googleapis.com/auth/cloud-platform</code></li></ul>                                                                                                                                                                                                                                                                                                |
| <p>Google Cloud<br>Storage</p>              | <ul><li><code>https://www.googleapis.com/auth/cloud-platform</code></li><li><code>https://www.googleapis.com/auth/cloud-platform.read-only</code></li><li><code>https://www.googleapis.com/auth/devstorage.full_control</code></li><li><code>https://www.googleapis.com/auth/devstorage.read_only</code></li><li><code>https://www.googleapis.com/auth/devstorage.read_write</code></li></ul>                                                    |
| Google Contacts                             | <ul><li><code>https://www.googleapis.com/auth/contacts</code></li></ul>                                                                                                                                                                                                                                                                                                                                                                          |
| Google Docs                                 | <ul><li><code>https://www.googleapis.com/auth/documents</code></li><li><code>https://www.googleapis.com/auth/drive</code></li><li><code>https://www.googleapis.com/auth/drive.file</code></li></ul>                                                                                                                                                                                                                                              |
| Google Drive                                | <ul><li><code>https://www.googleapis.com/auth/drive</code></li><li><code>https://www.googleapis.com/auth/drive.appdata</code></li><li><code>https://www.googleapis.com/auth/drive.photos.readonly</code></li></ul>                                                                                                                                                                                                                               |
| <p>Google Firebase<br>Cloud Firestore</p>   | <ul><li><code>https://www.googleapis.com/auth/datastore</code></li><li><code>https://www.googleapis.com/auth/firebase</code></li></ul>                                                                                                                                                                                                                                                                                                           |
| <p>Google Firebase<br>Realtime Database</p> | <ul><li><code>https://www.googleapis.com/auth/userinfo.email</code></li><li><code>https://www.googleapis.com/auth/firebase.database</code></li><li><code>https://www.googleapis.com/auth/firebase</code></li></ul>                                                                                                                                                                                                                               |
| Google Perspective                          | <ul><li><code>https://www.googleapis.com/auth/userinfo.email</code></li></ul>                                                                                                                                                                                                                                                                                                                                                                    |
| Google Sheets                               | <ul><li><code>https://www.googleapis.com/auth/drive.file</code></li><li><code>https://www.googleapis.com/auth/spreadsheets</code></li></ul>                                                                                                                                                                                                                                                                                                      |
| Google Slide                                | <ul><li><code>https://www.googleapis.com/auth/drive.file</code></li><li><code>https://www.googleapis.com/auth/presentations</code></li></ul>                                                                                                                                                                                                                                                                                                     |
| Google Tasks                                | <ul><li><code>https://www.googleapis.com/auth/tasks</code></li></ul>                                                                                                                                                                                                                                                                                                                                                                             |
| Google Translate                            | <ul><li><code>https://www.googleapis.com/auth/cloud-translation</code></li></ul>                                                                                                                                                                                                                                                                                                                                                                 |
| GSuite Admin                                | <ul><li><code>https://www.googleapis.com/auth/admin.directory.group</code></li><li><code>https://www.googleapis.com/auth/admin.directory.user</code></li><li><code>https://www.googleapis.com/auth/admin.directory.domain.readonly</code></li><li><code>https://www.googleapis.com/auth/admin.directory.userschema.readonly</code></li></ul>                                                                                                     |

</details>

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

### Google 尚未验证此应用 <a href="#google-hasnt-verified-this-app" id="google-hasnt-verified-this-app"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/google/unverified-app.md" %}

### Google Cloud 应用授权失效 <a href="#google-cloud-app-becoming-unauthorized" id="google-cloud-app-becoming-unauthorized"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/google/app-becoming-unauthorized.md" %}

### redirect\_uri\_mismatch <a href="#redirecturimismatch" id="redirecturimismatch"></a>

此错误表示 n8n 发送的重定向 URI 与 Google Cloud Console OAuth 客户端中登记的所有 URI 均不匹配。

**解决方法：**从 n8n 凭据面板复制 **OAuth Redirect URL**（OAuth 重定向 URL），将其完整粘贴到 Google OAuth 客户端的 **Authorized redirect URIs**（已获授权的重定向 URI）字段，包括协议（`http` 或 `https`）和端口号。

### 访问被拒绝 / “应用未验证” <a href="#access-denied-app-not-verified" id="access-denied-app-not-verified"></a>

这通常是因为应用仍处于 Testing（测试）模式，而用于身份验证的 Google 账户尚未添加为测试用户。

**解决方法：**进入 **APIs & Services**（API 和服务）> **OAuth consent screen**（OAuth 授权同意页面）> **Test users**（测试用户），添加要使用的账户。

### invalid\_client <a href="#invalidclient" id="invalidclient"></a>

此错误通常表示 n8n 凭据中的 Client ID 或 Client Secret 与 Google Cloud Console 中的值不匹配。

**解决方法：**返回 Google Cloud Console 中的 OAuth 客户端，重新复制这两个值并填入 n8n。复制时注意避免意外带入空格。
