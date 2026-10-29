---
title: X（原 Twitter）凭据
description: X 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 X 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: X（原 Twitter）凭据
originalFilePath: integrations/builtin/credentials/twitter.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/twitter
url: https://docs.n8n.io/integrations/builtin/credentials/twitter
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# X（原 Twitter） 凭据 <a href="#x-formerly-twitter-credentials" id="x-formerly-twitter-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [X（原 Twitter）](../app-nodes/n8n-nodes-base.twitter.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建 [X 开发者](https://developer.x.com)账户。
- 创建 [Twitter 应用](https://docs.x.com/fundamentals/developer-apps)，或使用注册开发者门户时创建的默认项目和应用。应用配置的更多详情，请参阅下文各支持身份验证方式的说明。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

{% hint style="warning" %}
**功能可用范围**

n8n 以前支持 **OAuth** 身份验证方式，使用 X 的 [OAuth 1.0a](https://docs.x.com/fundamentals/authentication/oauth-1-0a/overview) 身份验证。从 n8n 0.236.0 发布 X 节点 V2 版本起，n8n 已弃用此方式。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [X API 文档](https://docs.x.com/x-api/introduction)。服务身份验证的更多信息，请参阅 [X API 身份验证文档](https://docs.x.com/fundamentals/authentication/overview)。

仅应用身份验证的更多信息，请参阅 [Application-only Authentication（仅应用身份验证）](https://docs.x.com/fundamentals/authentication/oauth-2-0/application-only)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

此 OAuth2 方式从 n8n 0.236.0 起可用。

配置此凭据需要：

- 一个 **Client ID（客户端 ID）**
- 一个 **Client Secret（客户端密钥）**

生成 Client ID 和 Client Secret 的步骤如下：

1. 在 Twitter [开发者门户](https://developer.x.com/en/portal/dashboard)中打开项目。
2. 在项目的 **Overview**（概览）选项卡中，找到 **Apps**（应用）部分，选择 **Add App**（添加应用）。
3. 为应用设置 **Name**（名称），再选择 **Next**（下一步）。
1. 进入 **App Settings**（应用设置）。
4. 在 **User authentication settings**（用户身份验证设置）中选择 **Set Up**（设置）。
1. 设置 **App permissions**（应用权限）。如果希望使用 n8n X 节点的全部功能，请选择 **Read and write and Direct message**（读取、写入和私信）。
5. 在 **Type of app**（应用类型）部分选择 **Web App, Automated App or Bot**（Web 应用、自动化应用或机器人）。
1. 在 n8n 中复制 **OAuth Redirect URL**（OAuth 重定向 URL）。
7. 在 X 应用中找到 **App Info**（应用信息）部分，将该 URL 粘贴到 **Callback URI / Redirect URL**（回调 URI / 重定向 URL）。
7. 添加 **Website URL**（网站 URL）。
8. 保存更改。
1. 复制 X 中显示的 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥），填入 n8n 凭据的对应字段。

此身份验证方式的更多用法，请参阅 X 的 [OAuth 2.0 身份验证文档](https://docs.x.com/fundamentals/authentication/oauth-2-0/overview)。

{% hint style="info" %}
**X 速率限制**

此凭据使用 OAuth 2.0 Bearer Token 身份验证，因此受应用速率限制约束。更多信息，请参阅下文的 [X 速率限制](#x-rate-limits)。
{% endhint %}

## X 速率限制 <a href="#x-rate-limits" id="x-rate-limits"></a>

X 根据开发者访问套餐等级，对各端点实施基于时间的速率限制。X 分别计算应用速率限制和用户速率限制。各访问套餐等级的速率限制以及避免触及限制的指引，请参阅[速率限制](https://docs.x.com/fundamentals/rate-limits)。

计算速率限制时，请遵循以下指引：

- 如果使用已弃用的 OAuth 方式，则适用用户速率限制。每组用户访问令牌在每个时间窗口内各有一个限额。
- 如果[使用 OAuth2](#using-oauth2)，则适用应用速率限制。应用发出的请求在每个时间窗口内有一个限额。

X 分别计算用户速率限制和应用速率限制。

这些速率限制类型的更多信息，请参阅 X 的[速率限制与身份验证方式](https://docs.x.com/fundamentals/rate-limits)。
