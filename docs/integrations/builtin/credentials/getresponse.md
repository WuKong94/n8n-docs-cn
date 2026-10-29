---
title: GetResponse 凭据
description: GetResponse 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 GetResponse 的身份验证。
contentType:
- integration
- reference
nodeTitle: GetResponse 凭据
originalFilePath: integrations/builtin/credentials/getresponse.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/getresponse
url: https://docs.n8n.io/integrations/builtin/credentials/getresponse
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# GetResponse 凭据 <a href="#getresponse-credentials" id="getresponse-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [GetResponse](../app-nodes/n8n-nodes-base.getresponse.md)
- [GetResponse Trigger（触发器）](../trigger-nodes/n8n-nodes-base.getresponsetrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [GetResponse](https://www.getresponse.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [GetResponse API 文档](https://apidocs.getresponse.com/v3)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key**（API 密钥）：在 **Integrations and API > API**（集成与 API > API）中查看或生成 API 密钥。详细步骤请参阅 [GetResponse 帮助中心](https://www.getresponse.com/help/where-do-i-find-the-api-key.html)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- 一个 **Client ID**（客户端 ID）：[注册应用](https://apidocs.getresponse.com/v3/authentication/oauth2)时生成。
- 一个 **Client Secret**（客户端密钥）：[注册应用](https://apidocs.getresponse.com/v3/authentication/oauth2)时生成，名为 **Client Secret Key**（客户端密钥）。

注册应用时，从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），将其添加为 GetResponse 中的 **Redirect URL**（重定向 URL）。

{% hint style="info" %}
**使用 localhost 的重定向 URL**

重定向 URL 应使用你的域名，例如 `https://mytemplatemaker.example.com/gr_callback`。GetResponse 不接受 localhost 回调 URL。在本地环境配置凭据的方法，请参阅[常见问题](#configure-oauth2-credentials-for-a-local-environment)。
{% endhint %}

## 为本地环境配置 OAuth2 凭据 <a href="#configure-oauth2-credentials-for-a-local-environment" id="configure-oauth2-credentials-for-a-local-environment"></a>

GetResponse 不接受 localhost 回调 URL。请按以下步骤为本地环境配置 OAuth 凭据：
1. 使用 [ngrok](https://ngrok.com/) 将运行在 `5678` 端口的本地服务器暴露到互联网。在终端运行以下命令：
```sh
ngrok http 5678
```
2. 在新终端运行以下命令。将 `<YOUR-NGROK-URL>` 替换为上一步获取的 URL。`N8N_WEBHOOK_URL` 从 n8n 2.30.0 起可用；更早版本请使用 `WEBHOOK_URL`。
```sh
export N8N_WEBHOOK_URL=<YOUR-NGROK-URL>
```
3. 按照[使用 OAuth2](#using-oauth2) 中的说明配置凭据，将此 URL 用作 **Redirect URL**（重定向 URL）。

