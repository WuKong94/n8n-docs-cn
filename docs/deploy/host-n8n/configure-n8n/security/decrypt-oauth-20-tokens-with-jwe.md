---
title: OAuth 2.0 凭据的 JWE 令牌解密
description: 在 n8n 实例上启用 JWE 加密的 OAuth 2.0 令牌，让身份提供商加密访问令牌和 ID 令牌，仅允许你的实例解密。
contentType: howto
nodeTitle: 使用 JWE 解密 OAuth 2.0 令牌
originalFilePath: hosting/securing/oauth2-jwe-token-decryption.md
originalUrl: https://docs.n8n.io/hosting/securing/oauth2-jwe-token-decryption
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/decrypt-oauth-20-tokens-with-jwe
layout:
  description:
    visible: false
status: preview
tags:
- tag: preview
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# OAuth 2.0 凭据的 JWE 令牌解密 <a href="#jwe-token-decryption-for-oauth-20-credentials" id="jwe-token-decryption-for-oauth-20-credentials"></a>

{% hint style="info" %}
**功能可用范围**

* 自 n8n 2.21.0 起提供 JWE 令牌解密。
* 可用于将 `N8N_ENV_FEAT_OAUTH2_JWE` 环境变量设为 `true` 的任何 n8n 实例。自托管实例可直接设置；Cloud 用户请联系 n8n 支持团队申请启用。
* 需要身份提供商（IdP）支持以 JWE 格式加密令牌。
{% endhint %}

{% hint style="info" %}
**预览状态**

JWE 令牌解密处于预览阶段，通过环境变量开关控制。正式发布前，字段名、环境变量、JWKS 端点路径和支持的算法都可能更改。请固定 n8n 版本，并在每次升级后重新测试 OAuth 2.0 凭据。
{% endhint %}

JWE 令牌解密允许身份提供商返回以 [JWE](https://datatracker.ietf.org/doc/html/rfc7516) 格式加密的 OAuth 2.0 访问令牌和 ID 令牌。n8n 实例在 OAuth 回调时，使用始终保留在实例内部的私钥解密令牌。这样可以保护令牌内容，防止处于 IdP 和 n8n 之间的反向代理、浏览器、日志等环节读取。

## JWE 令牌解密的工作原理 <a href="#how-jwe-token-decryption-works" id="how-jwe-token-decryption-works"></a>

启用此功能后，n8n 会：

1. 在启动时生成 RSA 密钥对，并将使用实例加密密钥加密后的私钥存入数据库。
2. 在实例级 JWKS 端点发布对应公钥，供 IdP 获取。
3. 在 OAuth 回调时，使用与 JWE 标头中 `kid` 匹配的私钥，解密收到的 JWE 令牌。

IdP 使用从 JWKS 端点获取的公钥加密每个令牌，只有你的实例能解密结果。

## 开始之前 <a href="#before-you-begin" id="before-you-begin"></a>

你需要：

* 在 n8n 实例上设置 `N8N_ENV_FEAT_OAUTH2_JWE=true`。自托管实例可直接启用；Cloud 用户请联系 n8n 支持团队申请启用。
* 所有 n8n 实例，包括主实例和工作进程，都使用相同的 `N8N_ENCRYPTION_KEY` 值。n8n 使用此实例密钥加密静态存储的 JWE 私钥。
* IdP 支持使用 `RSA-OAEP-256` 密钥加密算法的 JWE 加密令牌。

## 启用 JWE 令牌解密 <a href="#enable-jwe-token-decryption" id="enable-jwe-token-decryption"></a>

1. 在**所有** n8n 实例上设置以下环境变量，包括主实例和工作进程：

    ```sh
    N8N_ENV_FEAT_OAUTH2_JWE=true
    ```

2. 重启所有实例。n8n 会在启动时生成 RSA 密钥对，并在 JWKS 端点发布公钥。
3. 要确认功能已生效，请请求 JWKS 端点，检查是否返回一个带有 `"alg": "RSA-OAEP-256"` 的密钥：

    ```sh
    curl https://<your-n8n-host>/rest/.well-known/jwks.json
    ```

## 配置身份提供商 <a href="#configure-your-identity-provider" id="configure-your-identity-provider"></a>

在 IdP 的 OAuth 2.0 客户端或应用配置中：

1. 为 n8n 连接的客户端启用令牌加密。
2. 将客户端的 JWKS URI 设为实例的 JWKS 端点。n8n 会在凭据中显示此 URL，创建凭据后即可直接复制，参阅下一节。
3. 选择 `RSA-OAEP-256` 作为密钥加密算法（`alg`），搭配 IdP 支持的任意内容加密算法（`enc`），例如 `A128CBC-HS256` 或 `A256GCM`。

<details>

<summary>示例：Okta</summary>

1. 在 Okta 管理控制台中打开 n8n 使用的 OAuth 2.0 应用，或新建一个 Web 应用。
2. 在应用的 OpenID Connect 设置中启用令牌加密。
3. 将 **Key management algorithm**（密钥管理算法）设为 `RSA-OAEP-256`，并选择内容加密算法，例如 `A256GCM`。
4. 将 **JWKS URI** 设为 n8n 凭据中 **JWKS URI** 字段显示的值。

</details>

## 在 n8n 中配置凭据 <a href="#configure-the-credential-in-n8n" id="configure-the-credential-in-n8n"></a>

1. 创建或编辑 [OAuth 2.0 API 凭据](../../../../integrations/builtin/credentials/httprequest.md#using-oauth2)。
2. 打开 **Encrypted Tokens (JWE)**（加密令牌）开关。
3. 如果尚未配置，请复制 **JWKS URI** 字段的值，粘贴到 IdP 的 JWKS URI 设置中。
4. 保存凭据并连接。n8n 会解密 IdP 返回的令牌，存储解密后的形式，供工作流使用。

IdP 的响应必须至少包含一个 JWE 加密令牌，可以是访问令牌、ID 令牌，或两者都包含。如果响应完全为明文，n8n 会拒绝响应并报错 `Expected at least one JWE-encrypted token but received only plaintext`。

## JWKS 端点参考 <a href="#jwks-endpoint-reference" id="jwks-endpoint-reference"></a>

n8n 在以下地址提供实例的公开加密密钥：

```
<instance-base-url>/<rest-endpoint>/.well-known/jwks.json
```

| 属性 | 值 |
| :------- | :---- |
| 默认路径 | `/rest/.well-known/jwks.json` |
| 身份验证 | 无，按设计公开访问 |
| 速率限制 | 每个 IP 每分钟允许的请求数由 `N8N_OAUTH_JWE_JWKS_PER_MINUTE` 指定，默认 `60` |
| 缓存标头 | `Cache-Control: public, max-age=3600, must-revalidate` |
| 响应格式 | [JWK Set](https://datatracker.ietf.org/doc/html/rfc7517#section-5)（RFC 7517 第 5 节） |

如果自定义了 `N8N_ENDPOINT_REST`，请将路径中的 `rest` 替换为你的值。

## 支持的算法 <a href="#supported-algorithms" id="supported-algorithms"></a>

n8n 支持使用 `RSA-OAEP-256` 加密密钥。请配置 IdP，在加密令牌时使用此 `alg` 值。n8n 不限制内容加密算法（`enc`），可使用 IdP 支持的任意值。

JWKS 架构预留了椭圆曲线算法（`ECDH-ES` 及其变体），但 n8n 尚不生成 EC 密钥。

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

* **凭据中未显示 Encrypted Tokens (JWE) 开关。**确认已在每个 n8n 实例上设置 `N8N_ENV_FEAT_OAUTH2_JWE=true`，并重启所有实例。
* **报错 `Expected at least one JWE-encrypted token but received only plaintext`。**IdP 返回了明文令牌。确认已在 IdP 中为客户端启用令牌加密，且 IdP 已从 JWKS 端点获取密钥。
* **IdP 无法获取 JWKS URI。**检查 IdP 是否能访问 JWKS 端点。反向代理和身份验证中间件有时会阻止 `/rest/.well-known/jwks.json`。该端点必须允许公开访问，无需身份验证。
* **IdP 过于频繁地获取 JWKS，触发速率限制。**提高 n8n 实例上的 `N8N_OAUTH_JWE_JWKS_PER_MINUTE`，或配置 IdP，在完整的 `max-age` 时间窗口内缓存 JWKS 响应。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

* [安全](../security.md)：审计、加固并限制自托管实例。
* [HTTP Request 凭据：使用 OAuth2](../../../../integrations/builtin/credentials/httprequest.md#using-oauth2)：设置通用 OAuth 2.0 凭据。
* [部署环境变量](../basic-configuration/use-environment-variables/deployment.md)：`N8N_ENV_FEAT_OAUTH2_JWE` 和 `N8N_OAUTH_JWE_JWKS_PER_MINUTE` 的参考。
* [加密密钥轮换](rotate-encryption-keys.md)：轮换用于保护静态存储 JWE 私钥的数据加密密钥。
* [JSON Web Encryption（RFC 7516）](https://datatracker.ietf.org/doc/html/rfc7516)：JWE 规范。
