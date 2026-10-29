---
title: Asana 凭据
description: Asana 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Asana 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Asana 凭据
originalFilePath: integrations/builtin/credentials/asana.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/asana
url: https://docs.n8n.io/integrations/builtin/credentials/asana
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Asana 凭据 <a href="#asana-credentials" id="asana-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Asana](../app-nodes/n8n-nodes-base.asana.md)
- [Asana Trigger（触发器）](../trigger-nodes/n8n-nodes-base.asanatrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Access token（访问令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务使用方法的更多信息，请参阅 [Asana 开发者指南](https://developers.asana.com/docs/overview)。

## 使用访问令牌 <a href="#using-access-token" id="using-access-token"></a>

配置此凭据需要一个 [Asana](https://asana.com/) 账号，以及：

- 个人 **Access Token**（访问令牌，PAT）

获取 PAT 的步骤如下：

1. 打开 Asana 的[开发者控制台](https://app.asana.com/0/my-apps)。
2. 在 **Personal access tokens**（个人访问令牌）部分，选择 **Create new token**（创建新令牌）。
3. 输入 **Token name**（令牌名称），例如 `n8n integration`。
4. 勾选复选框，同意 **Asana API terms**（Asana API 条款）。
5. 选择 **Create token**（创建令牌）。
6. 复制令牌，填入 n8n 凭据的 **Access Token**（访问令牌）。

更多信息，请参阅 [Asana 快速入门指南](https://developers.asana.com/docs/quick-start#setup)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要一个 [Asana](https://asana.com/) 账户。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果[自托管](../../../deploy/host-n8n/README.md) n8n，需要注册应用以设置 OAuth：

1. 打开 Asana 的[开发者控制台](https://app.asana.com/0/my-apps)。
2. 在 **My apps**（我的应用）部分，选择 **Create new app**（创建新应用）。
3. 输入应用的 **App name**（应用名称），例如 `n8n integration`。
4. 选择应用的用途。
5. 勾选复选框，同意 **Asana API terms**（Asana API 条款）。
6. 选择 **Create app**（创建应用）。页面将打开应用的 **Basic Information**（基本信息）。
7. 从左侧菜单选择 **OAuth**。
8. 在 n8n 中复制 **OAuth Redirect URL**（OAuth 重定向 URL）。
9. 在 Asana 中选择 **Add redirect URL**（添加重定向 URL），输入从 n8n 复制的 URL。
7. 从 Asana 复制 **Client ID**（客户端 ID），填入 n8n 凭据。
8. 从 Asana 复制 **Client Secret**（客户端密钥），填入 n8n 凭据。

更多信息，请参阅 [Asana OAuth 注册应用文档](https://developers.asana.com/docs/oauth#register-an-application)。
