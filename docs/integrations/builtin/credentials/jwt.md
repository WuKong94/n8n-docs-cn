---
title: JWT 凭据
contentType:
- integration
- reference
priority: medium
nodeTitle: JWT 凭据
originalFilePath: integrations/builtin/credentials/jwt.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/jwt
url: https://docs.n8n.io/integrations/builtin/credentials/jwt
description: JWT 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 JWT 的身份验证。
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


# JWT 凭据 <a id="jwt-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [JWT](../core-nodes/n8n-nodes-base.jwt.md)
* [Webhook](../core-nodes/n8n-nodes-base.webhook/README.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Passphrase（口令）：使用 HMAC 算法和秘密值签名
* Private key (PEM key)（私钥，PEM 密钥）：搭配使用 RSA 或 ECDSA 算法的 [Private Key JWT](https://auth0.com/docs/get-started/authentication-and-authorization-flow/authenticate-with-private-key-jwt) 使用

## 相关资源 <a href="#related-resources" id="related-resources"></a>

更多详情，请参阅 [JSON Web Token 规范](https://datatracker.ietf.org/doc/html/rfc7519)。

更详细的介绍，请参阅 [JWT 网站的 JSON Web Token 简介](https://jwt.io/introduction)。如何在这两种类型及相关算法之间选择，请参阅 [JSON Web Token（JWT）签名算法概述](https://auth0.com/blog/json-web-token-signing-algorithms-overview/)。

## 使用口令 <a href="#using-passphrase" id="using-passphrase"></a>

配置此凭据的步骤如下：

1. 将 **Key Type**（密钥类型）设为 **Passphrase**（口令）。
2. 输入口令 **Secret**（秘密值）。
3. 选择用于签署断言的 **Algorithm**（算法）。支持的算法列表，请参阅下方的[可用算法](jwt.md#available-algorithms)。

## 使用私钥（PEM 密钥） <a href="#using-private-key-pem-key" id="using-private-key-pem-key"></a>

配置此凭据的步骤如下：

1. 将 **Key Type**（密钥类型）设为 **PEM Key**（PEM 密钥）。
2. **Private Key**（私钥）：通过生成密钥对获得。示例请参阅[生成 RSA 密钥对](https://auth0.com/docs/secure/application-credentials/generate-rsa-key-pair)。
3. **Public Key**（公钥）：通过生成密钥对获得。示例请参阅[生成 RSA 密钥对](https://auth0.com/docs/secure/application-credentials/generate-rsa-key-pair)。
4. 选择用于签署断言的 **Algorithm**（算法）。支持的算法列表，请参阅下方的[可用算法](jwt.md#available-algorithms)。

## 可用算法 <a href="#available-algorithms" id="available-algorithms"></a>

此 n8n 凭据支持以下算法：

* `HS256`
* `HS384`
* `HS512`
* `RS256`
* `RS384`
* `RS512`
* `ES256`
* `ES384`
* `ES512`
* `PS256`
* `PS384`
* `PS512`
* `none`
