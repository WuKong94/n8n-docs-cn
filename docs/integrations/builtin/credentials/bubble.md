---
title: Bubble 凭据
description: Bubble 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Bubble 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Bubble 凭据
originalFilePath: integrations/builtin/credentials/bubble.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/bubble
url: https://docs.n8n.io/integrations/builtin/credentials/bubble
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Bubble 凭据 <a href="#bubble-credentials" id="bubble-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Bubble](../app-nodes/n8n-nodes-base.bubble.md)

{% hint style="info" %}
**API 访问**

访问 Bubble API 需要付费方案。
{% endhint %}

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Bubble API 文档](https://manual.bubble.io/help-guides/integrations/api)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个付费 [Bubble](https://bubble.io) 账户，以及：

- 一个 **API Token（API 令牌）**
- **App Name**（应用名称）
- 如果使用自定义域名，需要提供 **Domain**（域名）

设置此凭据需要先创建应用：

1. 打开 Bubble 的 [**Apps**（应用）](https://bubble.io/home/apps)页面。
1. 选择 **Create an app**（创建应用）。
1. 输入应用的 **Name**（名称），例如 `n8n-integration`。
1. 选择 **Get started**（开始），随后打开应用详情。
1. 在左侧导航栏选择 **Settings**（设置，齿轮图标）。
1. 选择 **API** 选项卡。
1. 在 **Public API Endpoints**（公共 API 端点）部分，勾选 **Enable Data API**（启用 Data API）。
1. 页面会显示 **Data API root URL**（Data API 根 URL），例如：`https://n8n-integration.bubbleapps.io/version-test/api/1.1/obj`。
1. 复制 URL 中位于 `https://` 之后、`.bubbleapps.io` 之前的部分，填入 n8n 的 **App Name**（应用名称）。在上述示例中，应输入 `n8n-integration`。
1. 选择 **Generate a new API token**（生成新的 API 令牌）。
8. 输入 **API Token Label**（API 令牌标签），例如 `n8n integration`。
1. 复制 **Private key**（私有密钥），填入 n8n 凭据的 **API Token**（API 令牌）。
    - 生成 API 令牌的更多信息，请参阅 [Data API | 身份验证](https://manual.bubble.io/core-resources/api/the-bubble-api/the-data-api/authentication)。
1. 在 n8n 中，选择与应用最匹配的 **Environment**（环境）：
    - 尚未部署、通过 `https://appname.bubbleapps.io/version-test` 或 `https://www.mydomain.com/version-test` 访问的应用，选择 **Development**（开发）。
    - 已[部署](https://manual.bubble.io/help-guides/getting-started/navigating-the-bubble-editor/deploying-your-app)、通过 `https://appname.bubbleapps.io` 或 `https://www.mydomain.com` 访问的应用，选择 **Live**（正式）。
1. 在 n8n 中选择 **Hosting**（托管方式）：
    - 未设置自定义域名时，选择 **Bubble Hosting**（Bubble 托管）。
    - 已设置[自定义域名](https://manual.bubble.io/help-guides/getting-started/navigating-the-bubble-editor/tabs-and-sections/settings-tab/web-app/custom-domain-and-dns)时，选择 **Self Hosted**（自行托管），并输入自定义 **Domain**（域名）。

更多信息，请参阅 Bubble 的[创建与管理应用](https://manual.bubble.io/help-guides/getting-started/creating-and-managing-apps)文档。
