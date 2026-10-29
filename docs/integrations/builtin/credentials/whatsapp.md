---
title: WhatsApp Business Cloud 凭据
contentType:
- integration
- reference
priority: high
nodeTitle: WhatsApp Business Cloud 凭据
originalFilePath: integrations/builtin/credentials/whatsapp.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/whatsapp
url: https://docs.n8n.io/integrations/builtin/credentials/whatsapp
description: WhatsApp Business Cloud 凭据文档。使用这些凭据在 n8n 中完成 WhatsApp Business Cloud
  的身份验证。
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


# WhatsApp Business Cloud 凭据 <a id="whatsapp-business-cloud-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [WhatsApp Business Cloud](../app-nodes/n8n-nodes-base.whatsapp/README.md)
* [WhatsApp Trigger（触发器）](../trigger-nodes/n8n-nodes-base.whatsapptrigger.md)

## 要求 <a href="#requirements" id="requirements"></a>

创建 WhatsApp 凭据需要以下 Meta 资产：

* [Meta 开发者](https://developers.facebook.com/docs/development/register)账户：开发者账户允许创建和管理 Meta 应用，包括 WhatsApp 集成。

<details>

<summary>设置 Meta 开发者账户</summary>

1. 访问 [Facebook Developers 网站](https://developers.facebook.com)。
2. 点击右上角的 **Getting Started**（开始使用）。如果链接显示 **My Apps**（我的应用），则表示已设置开发者账户。
3. 同意条款和条件。
4. 提供电话号码以完成验证。
5. 选择职业或角色。

</details>

* Meta [业务资产组合](https://www.facebook.com/business/help/1710077379203657?id=180505742745347)：WhatsApp 消息服务要求具有 Meta 业务资产组合，其旧称为 Business Manager（商务管理平台）账户。界面中可能仍显示其中任一名称。

<details>

<summary>设置 Meta 业务资产组合</summary>

1. 访问 [Facebook Business 网站](https://business.facebook.com)。
2. 选择 **Create an account**（创建账户）。
   * 如果已有 Facebook Business 账户及业务资产组合，但希望创建新的组合，请打开左侧菜单中的业务资产组合选择器，选择 **Create a business portfolio**（创建业务资产组合）。
3. 输入 **Business portfolio name**（业务资产组合名称）。
4. 输入你的 **name**（姓名）。
5. 输入 **business email**（业务邮箱）。
6. 选择 **Submit**（提交）或 **Create**（创建）。

</details>

* 配置了 WhatsApp 的 Meta [业务应用](https://developers.facebook.com/docs/development/create-an-app/)：取得开发者账户后，需要创建 Meta 业务应用。

<details>

<summary>设置包含 WhatsApp 的 Meta 业务应用</summary>

1. 访问 [Meta for Developers 应用控制台](https://developers.facebook.com/apps/)
2. 选择 **Create app**（创建应用）。
3. 在 **Add products to your app**（为应用添加产品）中，选择 WhatsApp 卡片上的 **Set up**（设置）。详情请参阅[添加 WhatsApp 产品](https://developers.facebook.com/docs/whatsapp/solution-providers/get-started-for-tech-providers#step-3--add-the-whatsapp-product)。
4. 随后打开 WhatsApp **Quickstart**（快速入门）页面，选择业务资产组合。
5. 选择 **Continue**（继续）。
6. 在左侧菜单中进入 **App settings**（应用设置）> **Basic**（基本）。
7. 为应用设置 **Privacy Policy URL**（隐私政策 URL）和 **Terms of Service URL**（服务条款 URL）。
8. 将 **App Mode**（应用模式）切换为 **Live**（上线）。

</details>

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API 密钥：用于 [WhatsApp Business Cloud](../app-nodes/n8n-nodes-base.whatsapp/README.md) 节点。
* OAuth2：用于 [WhatsApp Trigger（触发器）](../trigger-nodes/n8n-nodes-base.whatsapptrigger.md)节点。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [WhatsApp API 文档](https://developers.facebook.com/docs/whatsapp/#platform-apis)。

Meta 将创建 WhatsApp 业务应用的用户归类为 Tech Providers（技术提供商）。更多信息，请参阅 Meta 的[技术提供商入门指南](https://developers.facebook.com/docs/whatsapp/solution-providers/get-started-for-tech-providers)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

使用 [WhatsApp Business Cloud](../app-nodes/n8n-nodes-base.whatsapp/README.md) 节点需要 WhatsApp API 密钥凭据。

配置此凭据需要：

* API **Access Token**（访问令牌）
* **Business Account ID**（业务账户 ID）

按照以下步骤生成访问令牌：

1. 访问 [Meta for Developers 应用控制台](https://developers.facebook.com/apps/)。
2. 选择 Meta 应用。
3. 在左侧菜单中选择 **WhatsApp** > **API Setup**（API 设置）。
4. 选择 **Generate access token**（生成访问令牌），确认希望授予的访问权限。
5. 复制 **Access token**（访问令牌），填入 n8n 的 **Access Token**（访问令牌）。
6. 复制 **WhatsApp Business Account ID**（WhatsApp 业务账户 ID），填入 n8n 的 **Business Account ID**（业务账户 ID）。

上述步骤的更多信息，请参阅[在 WhatsApp 上测试业务消息](https://developers.facebook.com/docs/whatsapp/solution-providers/become-a-tech-provider-legacy-flow#step-4--test-business-messaging-on-whatsapp)。

要完整验证应用并上线，还需进一步配置。更多信息，请参阅 Meta 的[技术提供商入门指南](https://developers.facebook.com/docs/whatsapp/solution-providers/become-a-tech-provider-legacy-flow#step-5--scale-your-solution)中第 5 步及后续步骤。Meta 应用审核流程的更多信息，请参阅[应用审核](https://developers.facebook.com/docs/resp-plat-initiatives/app-review)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

使用 [WhatsApp Trigger（触发器）](../trigger-nodes/n8n-nodes-base.whatsapptrigger.md)节点需要 WhatsApp OAuth2 凭据。

配置此凭据需要：

* **Client ID**（客户端 ID）
* **Client Secret**（客户端密钥）

按照以下步骤获取这些信息：

1. 访问 [Meta for Developers 应用控制台](https://developers.facebook.com/apps/)。
2. 选择 Meta 应用。
3. 在左侧菜单中选择 **App settings**（应用设置）> **Basic**（基本）。
4. 复制 **App ID**（应用 ID），填入 n8n 凭据的 **Client ID**（客户端 ID）。
5. 复制 **App Secret**（应用密钥），填入 n8n 凭据的 **Client Secret**（客户端密钥）。

要完整验证应用并上线，还需进一步配置。更多信息，请参阅 Meta 的[技术提供商入门指南](https://developers.facebook.com/docs/whatsapp/solution-providers/become-a-tech-provider-legacy-flow#step-5--scale-your-solution)中第 5 步及后续步骤。Meta 应用审核流程的更多信息，请参阅[应用审核](https://developers.facebook.com/docs/resp-plat-initiatives/app-review)。
