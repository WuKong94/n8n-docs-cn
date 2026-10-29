---
title: Line 凭据
description: Line 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Line 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Line 凭据
originalFilePath: integrations/builtin/credentials/line.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/line
url: https://docs.n8n.io/integrations/builtin/credentials/line
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Line 凭据 <a href="#line-credentials" id="line-credentials"></a>


{% hint style="warning" %}
**功能可用范围**

Line 节点从 n8n 1.64.0 起弃用。LINE Notify 于 2025 年 4 月 1 日终止服务，此后该节点不再工作。更多信息，请查看 LINE Notify 的[服务终止公告](https://notify-bot.line.me/closing-announce)。
{% endhint %}


这些凭据可用于以下节点的身份验证：

- [Line](../app-nodes/n8n-nodes-base.line.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Notify OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Line Notify API 文档](https://notify-bot.line.me/doc/en/)。

## 使用 Notify OAuth2 <a href="#using-notify-oauth2" id="using-notify-oauth2"></a>

配置此凭据需要一个 [Line](https://line.me/en/) 账号，以及：

- 一个 **Client ID（客户端 ID）**
- 一个 **Client Secret（客户端密钥）**

如需生成这两项，请将 Line 连接到 [Line Notify](https://notify-bot.line.me/en/)，然后：

1. 打开 Line Notify 的[添加新服务](https://notify-bot.line.me/my/services/new)页面。
1. 输入 **Service name**（服务名称），其他人尝试连接该服务时会显示此名称。
1. 输入 **Service description**（服务描述）。
1. 输入 **Service URL**（服务 URL）。
1. 输入 **Company/Enterprise**（公司或企业）。
1. 选择 **Country/region**（国家或地区）。
1. 将你的姓名或团队名称填入 **Representative**（代表）。
1. 输入有效的 **Email address**（电子邮箱地址）。服务完成注册之前，Line 会验证此邮箱。请使用你能随时访问的邮箱地址。
1. 从 n8n 凭据复制 **OAuth Redirect URL**（OAuth 重定向 URL），填入 Line Notify 的 **Callback URL**（回调 URL）。
1. 选择 **Agree and continue**（同意并继续），同意服务条款。
1. 确认输入的信息正确，再选择 **Add**（添加）。
1. 检查邮件，打开 Line Notify 注册 URL，验证电子邮箱地址。
1. 完成验证后，打开 [**My services**（我的服务）](https://notify-bot.line.me/my/services/)。
1. 选择刚添加的服务。
1. 复制 **Client ID**（客户端 ID），填入 n8n 凭据。
1. 选择 **Display**（显示）**Client Secret**（客户端密钥）的选项，复制该值并填入 n8n 凭据。
1. 在 n8n 中选择 **Connect my account**（连接我的账户），按照屏幕提示完成凭据配置。

更多信息，请参阅 [Line Notify API 文档](https://notify-bot.line.me/doc/en/)中的身份验证部分。
