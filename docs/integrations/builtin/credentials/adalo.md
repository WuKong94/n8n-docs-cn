---
title: Adalo 凭据
description: Adalo 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Adalo 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Adalo 凭据
originalFilePath: integrations/builtin/credentials/adalo.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/adalo
url: https://docs.n8n.io/integrations/builtin/credentials/adalo
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Adalo 凭据 <a href="#adalo-credentials" id="adalo-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Adalo](../app-nodes/n8n-nodes-base.adalo.md)

{% hint style="info" %}
**API 访问**

使用 Adalo API 需要 Team 或 Business 方案。
{% endhint %}

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务使用方法的更多信息，请参阅 [Adalo API 集合文档](https://help.adalo.com/integrations/the-adalo-api/collections)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个 [Adalo](https://www.adalo.com/) 账号，以及：

- 一个 **API Key（API 密钥）**
- **App ID**（应用 ID）

如需获取这些信息，请创建 Adalo 应用：

1. 从顶部导航栏的应用下拉列表中，选择 **CREATE NEW APP**（创建新应用）。
1. 选择适合你的 App Layout（应用布局）类型，再选择 **Next**（下一步）。
    - 初次使用此产品时，Adalo 建议选择 **Mobile Only**（仅移动端）。
1. 选择一个模板作为起点，或选择 **Blank**（空白），再选择 **Next**（下一步）。
1. 输入 **App Name**（应用名称），例如 `n8n integration`。
1. 如适用，选择应用所属的 **Team**（团队）。
1. 选择品牌颜色。
1. 选择 **Create**（创建），随后打开应用编辑器。
1. 在左侧菜单选择 **Settings**（设置，齿轮图标）。
1. 选择 **App Access**（应用访问）。
1. 在 **API Key**（API 密钥）部分，选择 **Generate Key**（生成密钥）。
    - 如果方案级别不满足要求，则会显示升级提示。
1. 复制密钥，填入 n8n 凭据的 **API Key**（API 密钥）。
1. URL 中的 **App ID**（应用 ID）位于 `https://app.adalo.com/apps/` 之后。例如，应用 URL 为 `https://app.adalo.com/apps/b78bdfcf-48dc-4550-a474-dd52c19fc371/app-settings` 时，`b78bdfcf-48dc-4550-a474-dd52c19fc371` 即为 App ID。复制此值，填入 n8n 凭据。

在 Adalo 中创建应用的更多信息，请参阅[创建应用](https://help.adalo.com/design/designing-your-app/creating-an-app)。生成 API 密钥的更多信息，请参阅 [Adalo API](https://help.adalo.com/integrations/the-adalo-api)。
