---
title: Splunk 凭据
description: Splunk 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Splunk 的身份验证。
contentType:
- integration
- reference
nodeTitle: Splunk 凭据
originalFilePath: integrations/builtin/credentials/splunk.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/splunk
url: https://docs.n8n.io/integrations/builtin/credentials/splunk
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Splunk 凭据 <a href="#splunk-credentials" id="splunk-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Splunk](../app-nodes/n8n-nodes-base.splunk.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- [下载并安装](https://www.splunk.com/en_us/download/splunk-enterprise.html) Splunk Enterprise。
- 在 **Settings > Tokens**（设置 > 令牌）中[启用令牌身份验证](https://docs.splunk.com/Documentation/Splunk/9.2.1/Security/EnableTokenAuth)。

{% hint style="info" %}
**免费试用的 Splunk Cloud Platform 账户无法访问 REST API**

免费试用的 Splunk Cloud Platform 账户没有 REST API 访问权限。请确保拥有必要权限。更多详情请参阅 [Splunk Cloud Platform REST API 的访问要求与限制](https://docs.splunk.com/Documentation/SplunkCloud/8.2.2203/RESTTUT/RESTandCloud)。
{% endhint %}

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API auth token（API 身份验证令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Splunk Enterprise API 文档](https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTprolog)。

## 使用 API 身份验证令牌 <a href="#using-api-auth-token" id="using-api-auth-token"></a>

配置此凭据需要：

- 一个 **Auth Token**（身份验证令牌）：启用令牌身份验证后，在 **Settings > Tokens**（设置 > 令牌）中创建身份验证令牌。更多信息请参阅[创建身份验证令牌](https://docs.splunk.com/Documentation/Splunk/9.2.1/Security/CreateAuthTokens)。
- 一个 **Base URL**（基础 URL）：你的 Splunk 实例地址，应包含协议、域名和端口，例如 `https://localhost:8089`。
- **Allow Self-Signed Certificates**（允许自签名证书）：开启后，即使 SSL 验证失败，n8n 仍会连接。

## 所需能力权限 <a href="#required-capabilities" id="required-capabilities"></a>

创建身份验证令牌时，你的 Splunk 平台账户及角色必须具有特定的能力权限：

- `edit_tokens_own`：为自己创建令牌时需要。
- `edit_tokens_all`：为实例上的任意用户创建令牌时需要。

更多信息请参阅[使用能力权限定义 Splunk 平台角色](https://docs.splunk.com/Documentation/Splunk/9.2.1/Security/Rolesandcapabilities)。
