---
title: Facebook Graph API 凭据
contentType:
- integration
- reference
priority: medium
nodeTitle: Facebook Graph API 凭据
originalFilePath: integrations/builtin/credentials/facebookgraph.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/facebookgraph
url: https://docs.n8n.io/integrations/builtin/credentials/facebookgraph
description: Facebook Graph API 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Facebook Graph API 的身份验证。
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


# Facebook Graph API 凭据 <a id="facebook-graph-api-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Facebook Graph API](../app-nodes/n8n-nodes-base.facebookgraphapi.md)

{% hint style="info" %}
**Facebook Trigger 凭据**

如果要为 [Facebook Trigger](../trigger-nodes/n8n-nodes-base.facebooktrigger/README.md) 节点创建凭据，请按照 [Facebook App 凭据](facebookapp.md)文档中的说明操作。
{% endhint %}

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* OAuth2
* App access token（应用访问令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Meta Graph API 文档](https://developers.facebook.com/docs/graph-api/overview)。

## 前置条件 <a id="prerequisites"></a>

无论选择哪种身份验证方式，都需要一个 [Meta for Developers](https://developers.facebook.com/) 账户和 Meta 应用。

## 创建 Meta 应用 <a href="#create-a-meta-app" id="create-a-meta-app"></a>

创建 Meta 应用的步骤如下：

1. 打开 Meta Developer 的[应用控制台](https://developers.facebook.com/apps)，选择 **Create App**（创建应用）。
2. 填写应用详情：
   * 添加 **App name**（应用名称）。
   * 添加 **App contact email**（应用联系邮箱）。
3. 选择符合 Facebook Graph API 用途的 **Use case**（使用场景）。对于 Meta **Business**（业务）套件中的产品，例如 Messenger、Instagram、WhatsApp、Marketing API、App Events、Audience Network、Commerce API、Fundraisers、Jobs、Threat Exchange 和 Webhooks，选择 **Other**（其他），再选择 **Next**（下一步）。
4. 将 **App type**（应用类型）设为 **Business**（业务），再选择 **Next**（下一步）。
5. 如果你有业务资产组合，且已准备好将应用关联到它，请选择该业务资产组合。如果没有或尚未准备好关联，保留 **No business portfolio selected**（未选择业务资产组合）。
6. 选择 **Create app（创建应用）**。
7. 随后打开 **Add products to your app**（为应用添加产品）页面，选择适合应用的产品。

   {% hint style="info" %}
   **Facebook Login for Business**

   如果使用 [OAuth2](facebookgraph.md#using-oauth2) 身份验证类型，必须添加 **Facebook Login for Business**。仅使用应用访问令牌时，不需要添加此产品。
   {% endhint %}

创建应用、填写隐私政策 URL 等必需字段及添加产品的更多信息，请参阅 Meta 的[创建应用](https://developers.facebook.com/docs/development/create-an-app)文档。

### 将 Meta 应用上线 <a id="taking-a-meta-app-live"></a>

{% hint style="info" %}
**何时将应用切换为 Live（正式）模式**

在 **Development**（开发）模式下，只有在应用中具有角色（管理员、开发者或测试者）的人才能进行身份验证或生成令牌。如果仅连接自己的账户，可将应用保持为开发模式。
{% endhint %}

1. 从左侧菜单选择 **App settings > Basic**（应用设置 > 基本）。
2. 输入 **Privacy Policy URL**（隐私政策 URL），这是将应用切换为 Live（正式）模式前的必填项。
3. 选择 **Save changes**（保存更改）。
4. 如果需要没有应用角色的用户进行身份验证，将 **App Mode**（应用模式）从 **Development**（开发）切换为 **Live**（正式）。

应用模式和切换为 **Live**（正式）模式的更多信息，请参阅[应用模式](https://developers.facebook.com/docs/development/build-and-test/app-modes)和[发布 | 应用类型](https://developers.facebook.com/docs/development/release#app-types)。

## 使用 OAuth2 <a id="using-oauth2"></a>

配置此凭据需要一个 [Meta for Developers](https://developers.facebook.com/) 账号，以及：

* **Client ID**（客户端 ID）
* **Client Secret**（客户端密钥）

设置凭据需要两个步骤：

1. [创建 Meta 应用](facebookgraph.md#create-a-meta-app)，添加需要访问的产品。
2. 为该应用[生成 Client ID 和 Client Secret](facebookgraph.md#generate-a-client-id-and-client-secret)。

### 生成 Client ID 和 Client Secret <a id="generate-a-client-id-and-client-secret"></a>

生成 Client ID 和 Client Secret，供 n8n 凭据及已选择的产品使用：

1. 打开 Meta Developer 的[应用控制台](https://developers.facebook.com/apps)。
2. 从左上角的下拉列表中选择已[创建](facebookgraph.md#create-a-meta-app)的 **Meta App**（Meta 应用）。
3. 在左侧菜单选择 **Products**（产品）> **Facebook Login for Business** > **Settings**（设置）。
4. 将 n8n 凭据中的 **OAuth Redirect URL**（OAuth 重定向 URL）复制到 **Valid OAuth Redirect URIs**（有效的 OAuth 重定向 URI）框中，再选择 **Save changes**（保存更改）。
5. 在左侧菜单选择 **App settings**（应用设置）> **Basic**（基本）。
6. 复制 **App ID**（应用 ID），填入 n8n 凭据的 **Client ID**（客户端 ID）。
7. 复制 **App Secret**（应用密钥），填入 n8n 凭据的 **Client Secret**（客户端密钥）。
8. 在 n8n 凭据中选择 **Connect to Facebook Graph (App)**（连接到 Facebook Graph，应用）。

更多信息，请参阅 Meta 的 [Facebook Login for Business](https://developers.facebook.com/docs/facebook-login/facebook-login-for-business) 文档。

## 使用应用访问令牌 <a href="#using-app-access-token" id="using-app-access-token"></a>

配置此凭据需要一个 [Meta for Developers](https://developers.facebook.com/) 账号，以及：

* 应用 **Access Token**（访问令牌）

设置凭据需要两个步骤：

1. [创建 Meta 应用](facebookgraph.md#create-a-meta-app)，添加需要访问的产品。
2. 为该应用[生成应用访问令牌](facebookgraph.md#generate-an-app-access-token)。

### 生成应用访问令牌 <a href="#generate-an-app-access-token" id="generate-an-app-access-token"></a>

创建应用访问令牌，供 n8n 凭据及已选择的产品使用：

1. 打开 [Graph API explorer（Graph API 浏览器）](https://developers.facebook.com/tools/explorer/)。
2. 在 **Access Token**（访问令牌）部分，选择已[创建](facebookgraph.md#create-a-meta-app)的 **Meta App**（Meta 应用）。
3. 在 **User or Page**（用户或公共主页）中，选择 **Get App Token**（获取应用令牌）。
4. 选择 **Generate Access Token**（生成访问令牌）。
5. 页面会提示你登录并授予访问权限，请按照屏幕提示操作。

   {% hint style="warning" %}
   **应用不可用**

   可能收到应用不可用的警告。[将应用上线](facebookgraph.md#taking-a-meta-app-live)后，可能需要等待几分钟才能生成访问令牌。
   {% endhint %}
6. 复制令牌，填入 n8n 凭据的 **Access Token**（访问令牌）。

生成令牌的更多信息，请参阅 Meta 的[首次请求](https://developers.facebook.com/docs/graph-api/get-started#get-started)说明。
