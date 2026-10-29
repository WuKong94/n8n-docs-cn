---
title: HTTP Request 凭据
contentType:
- integration
- reference
priority: critical
nodeTitle: HTTP Request 凭据
originalFilePath: integrations/builtin/credentials/httprequest.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/httprequest
url: https://docs.n8n.io/integrations/builtin/credentials/httprequest
description: HTTP Request 凭据文档。使用这些凭据在 n8n 中完成 HTTP Request 节点的身份验证。
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


# HTTP Request 凭据 <a id="http-request-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [HTTP Request](../core-nodes/n8n-nodes-base.httprequest/README.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

必须使用要查询的应用或服务所要求的身份验证方式。

如果需要使用 SSL 证书保护身份验证，请参阅[提供 SSL 证书](httprequest.md#provide-an-ssl-certificate)，了解所需信息。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* 预定义凭据类型
* Basic auth（基本身份验证，通用凭据类型）
* Custom auth（自定义身份验证，通用凭据类型）
* Digest auth（摘要身份验证，通用凭据类型）
* Header auth（请求头身份验证，通用凭据类型）
* Bearer auth（持有者令牌身份验证，通用凭据类型）
* OAuth1（通用凭据类型）
* OAuth2（通用凭据类型）
* Query auth（查询参数身份验证，通用凭据类型）
* Simplified Custom Auth（简化自定义身份验证，通用凭据类型）

通用凭据类型的更多相关信息，请参阅 [HTTP 身份验证](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)。

{% hint style="info" %}
**预定义凭据类型**

只要所连接的服务有对应凭据类型，n8n 就建议使用预定义凭据类型。与配置通用凭据相比，它能更方便地设置和管理凭据。

对于 n8n 已提供平台节点的部分 API，可使用[预定义凭据类型](../custom-api-actions-for-existing-nodes.md#predefined-credential-types)执行自定义操作。例如，n8n 有 Asana 节点，也支持在 HTTP Request 节点中使用 Asana 凭据。更多信息，请参阅[自定义操作](../custom-api-actions-for-existing-nodes.md)。
{% endhint %}

## 使用预定义凭据类型 <a href="#using-predefined-credential-type" id="using-predefined-credential-type"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/predefined-credential-type-how-to.md" %}

更多信息，请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/generic-auth/basic-auth.md" %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/generic-auth/digest-auth.md" %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/generic-auth/header-auth.md" %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/generic-auth/bearer-auth.md" %}

## 使用 OAuth1 <a href="#using-oauth1" id="using-oauth1"></a>

如果应用或服务支持 OAuth1 身份验证，请使用此通用身份验证方式。

配置此凭据时，请输入：

* **Authorization URL**（授权 URL）：也称为 Resource Owner Authorization URI（资源所有者授权 URI）。此 URL 通常以 `/oauth1/authorize` 结尾。n8n 将临时凭据发送到此处，提示用户完成授权。
* **Access Token URL**（访问令牌 URL）：用于首次请求临时凭据的 URI。此 URL 通常以 `/oauth1/request` 或 `/oauth1/token` 结尾。
* **Consumer Key**（消费者密钥）：也称为客户端键，类似用户名，用于指定调用所使用的 `oauth_consumer_key`。
* **Consumer Secret**（消费者秘密值）：也称为客户端密钥，类似密码。
* **Request Token URL**（请求令牌 URL）：授权完成后，将临时凭据交换为长期凭据的 URI。此 URL 通常以 `/oauth1/access` 结尾。

> 译注：原文将 Access Token URL 和 Request Token URL 的流程说明及示例路径对调了。按 OAuth 1.0 的流程，Request Token URL 用于获取临时凭据，Access Token URL 用于在授权后用临时凭据交换访问令牌。实际端点请以服务商文档为准，勿直接套用上面的示例路径。

* 选择身份验证握手使用的 **Signature Method**（签名方法），用于指定调用所使用的 `oauth_signature_method`。选项包括：
  * **HMAC-SHA1**
  * **HMAC-SHA256**
  * **HMAC-SHA512**

对于大多数 OAuth1 集成，需要配置应用、服务或集成，生成上述大部分字段的值。请将 n8n 中的 **OAuth Redirect URL**（OAuth 重定向 URL）用作该服务的重定向 URL 或重定向 URI。

进一步了解 [OAuth1](https://oauth.net/1/) 和 [OAuth1 授权流程](https://oauth1.wp-api.org/docs/basics/Auth-Flow.html)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

如果应用或服务支持 OAuth2 身份验证，请使用此通用身份验证方式。

配置此凭据的要求取决于所选的 **Grant Type**（授权类型）。各授权类型的更多信息，请参阅 [OAuth 授权类型](https://oauth.net/2/grant-types/)。

对于大多数 OAuth2 集成，需要配置应用、服务或集成。请将 n8n 中的 **OAuth Redirect URL**（OAuth 重定向 URL）用作该服务的重定向 URL 或重定向 URI。

进一步了解 [OAuth2](https://oauth.net/2/)。

### Authorization Code（授权码）授权类型 <a href="#authorization-code-grant-type" id="authorization-code-grant-type"></a>

使用 Authorization Code 授权类型，将授权码交换为访问令牌。身份验证流程通过重定向 URL 将用户返回到客户端，随后应用从 URL 中获取授权码，并用它请求访问令牌。更多信息，请参阅[授权码请求](https://www.oauth.com/oauth2-servers/access-tokens/authorization-code-request/)。

配置此凭据时，请将 **Grant Type**（授权类型）设为 **Authorization Code**（授权码）。

然后输入：

* **Authorization URL**（授权 URL）
* **Access Token URL**（访问令牌 URL）
* **Client ID**（客户端 ID）：用于登录的 ID 或用户名。
* **Client Secret**（客户端密钥）：用于登录的密钥或密码。
* _可选：_为凭据输入一个或多个 **Scope**（作用域）。如果未指定，凭据将请求客户端可用的所有作用域。
* _可选：_某些服务要求额外查询参数。如果所用服务有此要求，请将其添加为 **Auth URI Query Parameters**（身份验证 URI 查询参数）。
* **Authentication**（身份验证）类型：选择最适合使用场景的选项，包括：
  * **Header**（请求头）：以基本身份验证请求头发送凭据。
  * **Body**（请求体）：在请求体中发送凭据。
* _可选：_选择是否 **Ignore SSL Issues**（忽略 SSL 问题）。开启后，即使 SSL 验证失败，n8n 仍会连接。

### Client Credentials（客户端凭据）授权类型 <a href="#client-credentials-grant-type" id="client-credentials-grant-type"></a>

当应用请求访问令牌以访问自身资源，而不是代表用户访问资源时，使用 Client Credentials 授权类型。更多信息，请参阅[客户端凭据](https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/)。

配置此凭据时，请将 **Grant Type**（授权类型）设为 **Client Credentials**（客户端凭据）。

然后输入：

* **Access Token URL**（访问令牌 URL）：用于启动 OAuth2 流程的请求 URL，通常以 `/token` 结尾。
* **Client ID**（客户端 ID）：用于登录客户端的 ID 或用户名。
* **Client Secret**（客户端密钥）：用于登录客户端的密钥或密码。
* _可选：_为凭据输入一个或多个 **Scope**（作用域）。大多数服务不支持为 Client Credentials 授权类型设置作用域；仅当所用服务支持时才填写。
* **Authentication**（身份验证）类型：选择最适合使用场景的选项，包括：
  * **Header**（请求头）：以基本身份验证请求头发送凭据。
  * **Body**（请求体）：在请求体中发送凭据。
* _可选：_选择是否 **Ignore SSL Issues**（忽略 SSL 问题）。开启后，即使 SSL 验证失败，n8n 仍会连接。

### PKCE 授权类型 <a href="#pkce-grant-type" id="pkce-grant-type"></a>

Proof Key for Code Exchange（PKCE，代码交换证明密钥）授权类型是 Authorization Code 流程的扩展，用于防止 CSRF 和授权码注入攻击。

配置此凭据时，请将 **Grant Type**（授权类型）设为 **PKCE**。

然后输入：

* **Authorization URL**（授权 URL）
* **Access Token URL**（访问令牌 URL）
* **Client ID**（客户端 ID）：用于登录的 ID 或用户名。
* **Client Secret**（客户端密钥）：用于登录的密钥或密码。
* _可选：_为凭据输入一个或多个 **Scope**（作用域）。如果未指定，凭据将请求客户端可用的所有作用域。
* _可选：_某些服务要求额外查询参数。如果所用服务有此要求，请将其添加为 **Auth URI Query Parameters**（身份验证 URI 查询参数）。
* **Authentication**（身份验证）类型：选择最适合使用场景的选项，包括：
  * **Header**（请求头）：以基本身份验证请求头发送凭据。
  * **Body**（请求体）：在请求体中发送凭据。
* _可选：_选择是否 **Ignore SSL Issues**（忽略 SSL 问题）。开启后，即使 SSL 验证失败，n8n 仍会连接。

## 使用查询参数身份验证 <a href="#using-query-auth" id="using-query-auth"></a>

如果应用或服务支持通过单个键值查询参数传递身份验证信息，请使用此通用身份验证方式。多个查询参数请使用[自定义身份验证](httprequest.md#using-custom-auth)。

配置此凭据时，请输入：

* 查询参数键，即 **Name**（名称）
* 查询参数 **Value**（值）

## 使用自定义身份验证 <a href="#using-custom-auth" id="using-custom-auth"></a>

如果应用或服务支持通过多个键值查询参数传递身份验证信息，或需要比其他通用身份验证选项更灵活的配置，请使用此方式。

**Custom Auth**（自定义身份验证）凭据使用 JSON 数据定义凭据，可使用 `headers`、`qs`、`body`，或混合使用。请从下方示例开始了解。

### 发送两个请求头 <a href="#sending-two-headers" id="sending-two-headers"></a>

```
{
	"headers": {
		"X-AUTH-USERNAME": "username",
		"X-AUTH-PASSWORD": "password"
	}
}
```

### 请求体 <a href="#body" id="body"></a>

```
{
	 "body" : {
		"user": "username",
		"pass": "password"
	}
}
```

### 查询字符串 <a href="#query-string" id="query-string"></a>

```
{
	"qs": { 
		"appid": "123456",
		"apikey": "my-api-key"
	}
}
```

### 发送请求头和查询字符串 <a href="#sending-header-and-query-string" id="sending-header-and-query-string"></a>

```
{
	"headers": {
		"api-version": "202404"
	},
	"qs": {
		"apikey": "my-api-key"
	}
}
```

## 使用简化自定义身份验证 <a id="using-simplified-custom-auth"></a>

{% hint style="info" %}
**功能可用范围**

Simplified Custom Auth（简化自定义身份验证）从 n8n 2.35.0 起可用。较早版本请改用[自定义身份验证](httprequest.md#using-custom-auth)。
{% endhint %}

如果应用或服务要求在请求头、查询参数或请求体中提供静态身份验证值，并且希望将秘密值与请求定义分开保存，请使用此通用身份验证方式。

简化自定义身份验证与[自定义身份验证](httprequest.md#using-custom-auth)类似，均使用 JSON，n8n 会将其合并到使用该凭据的每个请求中。区别在于，该 JSON 是模板，包含 `{{placeholder}}` 标记而非秘密值本身。凭据表单为每个占位符显示一个字段，n8n 在发送请求时用字段值替换各标记。

这样拆分是为了让 n8n Assistant 代为准备设置部分。[n8n Assistant](../../../build/ways-of-building-workflows/n8n-assistant.md) 为没有专用 n8n 凭据的服务构建工作流时，会创建此凭据类型：依据服务 API 文档准备模板、字段和测试 URL，你只需将秘密值粘贴到表单中。它还会记录服务的 API 主机，使 n8n 仅向调用同一服务的节点提供此凭据。

也可自行设置凭据。在凭据弹窗中选择 **Edit setup**（编辑设置），输入：

* **Auth template**（身份验证模板）：n8n 会将此 JSON 合并到使用该凭据的每个请求中。可使用 `headers`、`qs`、`body`，或混合使用，在秘密值或账户特定值的位置放置 `{{placeholder}}` 标记。不要将真实值填入模板。
* 每个占位符的 **Fields**（字段）设置：包括 **Label**（标签）、值是 **Secret**（秘密值，遮罩显示）还是 **Plain text**（纯文本）、是否 **Required**（必填），以及可选的 **Hint**（提示），用于说明预期值，例如其格式。
* _可选：_**Test URL**（测试 URL）：保存凭据时，n8n 会携带身份验证信息调用此 GET 端点，检查凭据是否可用。请选择没有副作用、不会触发计费工作的端点，例如账户或个人资料端点。
* _可选：_**Accepted status codes**（接受的状态码）：测试凭据时，除 2xx 响应外也视为成功的状态码。例如，对于有效但作用域有限的密钥返回 403 的服务，可填写 `403`。
* _可选：_**Documentation URL**（文档 URL）：在提供商处创建或复制秘密值的页面。此字段不会出现在凭据表单中，n8n Assistant 会用它引导你前往准确页面。

然后返回表单，为每个字段填入值。保存后，n8n 会隐藏这些值。

### 在请求头中发送 API 密钥 <a id="sending-an-api-key-in-a-header"></a>

发送 Bearer 令牌的模板：

```
{
	"headers": {
		"Authorization": "Bearer {{api_key}}"
	}
}
```

凭据表单为 `api_key` 显示一个字段。节点发送请求时，n8n 用字段值替换标记，得到请求头 `Authorization: Bearer <your-api-key>`。

如果必填字段为空，请求会报错，不会将标记原样发送给服务。如果可选字段为空，n8n 会从请求中移除使用该字段的模板条目。

## 提供 SSL 证书 <a href="#provide-an-ssl-certificate" id="provide-an-ssl-certificate"></a>

可在 HTTP 请求中发送 SSL 证书。请将 SSL 证书创建为单独的凭据，供节点使用：

1. 在 HTTP Request 节点的 **Settings**（设置）中开启 **SSL Certificates**（SSL 证书）。
2. 在 **Parameters**（参数）选项卡中，将现有 SSL Certificate 凭据添加到 **Credential for SSL Certificates**（SSL 证书凭据），或创建新凭据。

配置 SSL Certificates 凭据需要添加：

* 证书颁发机构 **CA** 证书包
* **Certificate**（证书，CRT）：根据签发 CA 及其证书格式，也可能显示为 Public Key（公钥）
* **Private Key**（私钥，KEY）
* _可选：_如果 **Private Key**（私钥）已加密，请输入私钥的 **Passphrase**（口令）。

如果 SSL 证书保存在单个文件中，例如 `.pfx` 文件，需要打开文件，复制其中的信息并粘贴到相应字段：

* 将 Public Key/CRT 填入 **Certificate**（证书）
* 将 **Private Key**（私钥）/KEY 填入对应字段
