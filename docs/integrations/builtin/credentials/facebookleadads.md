---
title: Facebook Lead Ads 凭据
description: Facebook Lead Ads 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Facebook Lead Ads 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Facebook Lead Ads 凭据
originalFilePath: integrations/builtin/credentials/facebookleadads.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/facebookleadads
url: https://docs.n8n.io/integrations/builtin/credentials/facebookleadads
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Facebook Lead Ads 凭据 <a href="#facebook-lead-ads-credentials" id="facebook-lead-ads-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Facebook Lead Ads 触发器](../trigger-nodes/n8n-nodes-base.facebookleadadstrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Facebook Lead Ads 文档](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/)。

查看 n8n 网站上的[工作流示例和相关内容](https://n8n.io/integrations/facebook-lead-ads-trigger/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要一个 [Meta for Developers](https://developers.facebook.com/) 账号，以及：

- 一个 **Client ID（客户端 ID）**
- 一个 **Client Secret（客户端密钥）**

如需获取这两项，请[创建 Meta 应用](https://developers.facebook.com/docs/development/create-an-app)，使用 Facebook Login 或 Facebook Login for Business 产品。

使用 **Facebook Login for Business** 创建应用并设置凭据的步骤如下：

1. 打开 Meta Developer 的[应用控制台](https://developers.facebook.com/apps)，选择 **Create App**（创建应用）。
2. 如果你有业务资产组合，且已准备好将应用关联到它，请选择该业务资产组合。如果没有或暂未准备好关联，选择 **I don’t want to connect a business portfolio yet**（暂不关联业务资产组合），再选择 **Next**（下一步）。随后打开 **Use cases**（使用场景）页面。
3. 选择 **Other**（其他），再选择 **Next**（下一步）。
4. 选择 **Business**（业务）和 **Next**（下一步）。
5. 填写必要信息：
    * 添加 **App name**（应用名称）。
    * 添加 **App contact email**（应用联系邮箱）。
    * 此处也可关联业务资产组合，或跳过。
1. 选择 **Create app**（创建应用），随后打开 **Add products to your app**（为应用添加产品）页面。
1. 选择 **Facebook Login for Business**，随后打开该产品的 **Settings**（设置）页面。
1. 从 n8n 凭据复制 **OAuth Redirect URL**（OAuth 重定向 URL）。
1. 在 Meta 应用设置的 **Client OAuth settings**（客户端 OAuth 设置）中，将该 URL 粘贴到 **Valid OAuth Redirect URIs**（有效的 OAuth 重定向 URI）。
1. 从左侧菜单选择 **App settings > Basic**（应用设置 > 基本）。
1. 复制 **App ID**（应用 ID），填入 n8n 凭据的 **Client ID**（客户端 ID）。
1. 复制 **App Secret**（应用密钥），填入 n8n 凭据的 **Client Secret**（客户端密钥）。

此时凭据应能成功连接，但在与 [Facebook Lead Ads 触发器](../trigger-nodes/n8n-nodes-base.facebookleadadstrigger.md)配合使用前，还需要完成 Meta 应用上线步骤，概括如下：

1. 在 Meta 应用的左侧菜单选择 **App settings > Basic**（应用设置 > 基本）。
1. 输入 **Privacy Policy URL**（隐私政策 URL），这是将应用切换为 Live（正式）状态的必填项。
1. 选择 **Save changes**（保存更改）。
1. 在页面顶部，将 **App Mode**（应用模式）从 **Development**（开发）切换为 **Live**（正式）。
1. Facebook Login for Business 要求 `public_profile` 的高级访问权限。添加方法是进入 **App Review > Permissions and Features**（应用审核 > 权限与功能）。
1. 搜索 `public_profile`，选择 **Request advanced access**（申请高级访问权限）。
1. 完成[业务验证](https://www.facebook.com/business/tools/meta-verified-for-business/)步骤。
1. 使用 [Lead Ads Testing Tool](https://developers.facebook.com/tools/lead-ads-testing) 触发一些演示表单提交，测试工作流。

创建应用、填写隐私政策 URL 等必需字段及添加产品的更多信息，请参阅 Meta 的[创建应用](https://developers.facebook.com/docs/development/create-an-app)文档。

应用模式和切换为 **Live**（正式）模式的更多信息，请参阅[应用模式](https://developers.facebook.com/docs/development/build-and-test/app-modes)和[发布 | 应用类型](https://developers.facebook.com/docs/development/release#app-types)。
