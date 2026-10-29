---
title: Calendly 凭据
description: Calendly 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Calendly 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Calendly 凭据
originalFilePath: integrations/builtin/credentials/calendly.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/calendly
url: https://docs.n8n.io/integrations/builtin/credentials/calendly
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Calendly 凭据 <a href="#calendly-credentials" id="calendly-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Calendly Trigger（触发器）](../trigger-nodes/n8n-nodes-base.calendlytrigger.md)

{% hint style="warning" %}
**支持的 Calendly 方案**

Calendly Trigger 节点依赖 Calendly webhook，而 Calendly 仅在付费方案中提供 webhook 访问权限。
{% endhint %}

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Personal Access Token（个人访问令牌）
- OAuth2

## 所需作用域 <a href="#required-scopes" id="required-scopes"></a>

在 n8n 中使用 Calendly 节点和触发器，凭据必须具有以下作用域：

- `users:read`：读取用户信息
- `webhooks:read`：读取 webhook 订阅
- `webhooks:write`：创建和管理 webhook 订阅
- `scheduled_events:read`：读取已安排事件的信息

个人访问令牌也需要相同作用域。在 Calendly 中创建个人访问令牌时，请选择上述作用域。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Calendly API 文档](https://developer.calendly.com/getting-started)。

## 使用个人访问令牌 <a href="#using-personal-access-token" id="using-personal-access-token"></a>

配置此凭据需要一个 [Calendly](https://www.calendly.com/) 账号，以及：

- **Personal Access Token**（个人访问令牌）

获取访问令牌的步骤如下：

1. 打开 Calendly 的 [**Integrations & apps**（集成与应用）](https://calendly.com/integrations)页面。
2. 选择 [**API & Webhooks**](https://calendly.com/integrations/api_webhooks)。
3. 在 **Your Personal Access Tokens**（你的个人访问令牌）中，选择 **Generate new token**（生成新令牌）。
4. 输入访问令牌的 **Name**（名称），例如 `n8n integration`。
5. 选择 **Create token**（创建令牌）。
6. 选择 **Copy token**（复制令牌），填入 n8n 凭据。

更多信息，请参阅 [Calendly API 身份验证文档](https://developer.calendly.com/docs/authentication/how-to-authenticate-with-personal-access-tokens)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要一个 [Calendly developer](https://developer.calendly.com)（开发者）账户，以及：

- 一个 **Client ID（客户端 ID）**
- 一个 **Client Secret（客户端密钥）**

如需获取这两项，请在 Calendly 中创建新的 OAuth 应用：

1. 登录 Calendly 开发者门户，进入 [**My apps**（我的应用）](https://developer.calendly.com/console/apps)。
1. 选择 **Create new app**（创建新应用）。
1. 输入 **Name of app**（应用名称），例如 `n8n integration`。
2. 将 **Kind of app**（应用类型）设为 **Web**。
3. 在 **Environment type**（环境类型）中，选择符合使用场景的 **Sandbox**（沙盒）或 **Production**（生产）。
    - Calendly 建议开发时先使用 **Sandbox**（沙盒），准备上线时再为 **Production**（生产）创建第二个应用。
4. 从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），填入 OAuth 应用的 **Redirect URI**（重定向 URI）。
5. 在 **Scopes**（作用域）部分，添加以下必需作用域：
    - `users:read`
    - `webhooks:read`
    - `webhooks:write`
    - `scheduled_events:read`
6. 选择 **Save & Continue**（保存并继续），随后显示应用详情。
7. 复制 **Client ID**（客户端 ID），填入 n8n 的 **Client ID**（客户端 ID）。
8. 复制 **Client secret**（客户端密钥），填入 n8n 的 **Client Secret**（客户端密钥）。
9. 在 n8n 中选择 **Connect my account**（连接我的账户），按照屏幕提示完成凭据授权。

更多信息请参阅[在 Calendly 中注册应用](https://developer.calendly.com/docs/authentication/creating-an-oauth-app)。

{% hint style="info" %}
**本地 OAuth2 测试**

通过隧道（例如 ngrok 或 Cloudflare Tunnel）测试 OAuth2 时，请使用与 **OAuth Redirect URL**（OAuth 重定向 URL）相同的公共 URL 打开 n8n，否则 OAuth 回调可能因 n8n 会话 cookie 属于不同主机而失败。
{% endhint %}
