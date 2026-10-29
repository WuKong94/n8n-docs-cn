---
title: Mautic 凭据
description: Mautic 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Mautic 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Mautic 凭据
originalFilePath: integrations/builtin/credentials/mautic.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/mautic
url: https://docs.n8n.io/integrations/builtin/credentials/mautic
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Mautic 凭据 <a href="#mautic-credentials" id="mautic-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Mautic](../app-nodes/n8n-nodes-base.mautic.md)
- [Mautic Trigger（触发器）](../trigger-nodes/n8n-nodes-base.mautictrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Mautic API 文档](https://developer.mautic.org/#rest-api)。

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

{% hint style="info" %}
**已启用 API**

配置此凭据前，Mautic 实例必须启用 API。操作说明，请参阅[启用 API](#enable-the-api)。
{% endhint %}

配置此凭据需要 [Mautic](https://www.mautic.org/) 实例上的账户，以及：

- **URL**
- 一个 **Username（用户名）**
- 一个 **Password（密码）**

设置步骤如下：

1. 在 Mautic 中进入 **Configuration > API Settings**（配置 > API 设置）。
2. 如果 **Enable HTTP basic auth?**（启用 HTTP 基本身份验证？）设为 **No**（否），将其改为 **Yes**（是）并保存。更多信息，请参阅 [API 设置文档](https://docs.mautic.org/en/5.x/configuration/settings.html#api-settings)。
1. 在 n8n 中输入 Mautic 实例的基础 **URL**。
2. 输入 Mautic **Username（用户名）**。
3. 输入 Mautic 的 **Password**（密码）。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% hint style="info" %}
**已启用 API**

配置此凭据前，Mautic 实例必须启用 API。操作说明，请参阅[启用 API](#enable-the-api)。
{% endhint %}

配置此凭据需要 [Mautic](https://www.mautic.org/) 实例上的账户，以及：

- **Client ID**（客户端 ID）：创建新 API 凭据时生成。
- **Client Secret**（客户端密钥）：创建新 API 凭据时生成。
- **URL**

设置步骤如下：

1. 在 Mautic 中进入 **Configuration > Settings**（配置 > 设置）。
2. 选择 **API Credentials**（API 凭据）。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>没有 API Credentials 菜单</strong></p><p>如果未看到 <strong>API Credentials（API 凭据）</strong> 选项（位于 <strong>Configuration &gt; Settings（配置 > 设置）</strong>），请确保已<a href="#enable-the-api">启用 API</a>。如果启用后仍未显示，请尝试<a href="https://forum.mautic.org/t/cant-find-api-credentials-menu/10689">手动清理缓存</a>。</p></div>

2. 选择 **Create new client**（创建新客户端）。
3. 将 **Authorization Protocol**（授权协议）设为 **OAuth 2**。
4. 输入凭据的 **Name**（名称），例如 `n8n integration`。
5. 在 n8n 中复制 **OAuth Callback URL**（OAuth 回调 URL），填入 Mautic 的 **Redirect URI**（重定向 URI）。
6. 选择 **Apply**（应用）。
7. 从 Mautic 复制 **Client ID**（客户端 ID），填入 n8n 凭据。
8. 从 Mautic 复制 **Client Secret**（客户端密钥），填入 n8n 凭据。
9. 输入 Mautic 实例的基础 **URL**。

更多信息，请参阅[什么是 Mautic API？](https://kb.mautic.org/article/what-is-mautic-039%3bs-api.html#mcetoc_1g7n1bgoo0)

## 启用 API <a href="#enable-the-api" id="enable-the-api"></a>

在 Mautic 实例中启用 API 的步骤如下：

1. 进入 **Settings > Configuration**（设置 > 配置）。
2. 选择 **API Settings**（API 设置）。
3. 将 **API enabled?**（启用 API？）设为 **Yes**（是）。
4. **Save**（保存）更改。

更多信息，请参阅[如何使用 Mautic API](https://kb.mautic.org/article/what-is-mautic-039;s-api.html)。
