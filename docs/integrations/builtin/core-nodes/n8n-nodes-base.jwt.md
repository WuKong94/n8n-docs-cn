---
title: JWT 节点
description: 了解 n8n 中 JWT 节点的用法，并查看相关示例。
contentType:
- integration
- reference
priority: medium
nodeTitle: JWT 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.jwt.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# JWT <a href="#jwt" id="jwt"></a>

在 n8n 工作流中处理 JSON Web Token（JWT）。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [JWT 凭据文档](../credentials/jwt.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Decode（解码）
* Sign（签名）
* Verify（验证）

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

* **Credential to connect with**（连接凭据）：选择或创建用于连接的 [JWT 凭据](../credentials/jwt.md)。
* **Token**（令牌）：输入要 **Verify**（验证）或 **Decode**（解码）的令牌。
* 选择 **Sign**（签名）操作后，还会有以下参数：
    * **Use JSON to Build Payload**（使用 JSON 构建载荷）：开启时，节点使用 JSON 构建声明。此选项决定 Payload Claims（载荷声明）部分显示的内容。

## Payload Claims（载荷声明） <a href="#payload-claims" id="payload-claims"></a>

只有选择 **Sign**（签名）操作时，节点才显示载荷声明。具体内容取决于 **Use JSON to Build Payload**（使用 JSON 构建载荷）的设置：

* 开启 **Use JSON to Build Payload**（使用 JSON 构建载荷）时，此处显示 JSON 编辑器，可在其中构建声明。
* 未开启 **Use JSON to Build Payload**（使用 JSON 构建载荷）时，此处提示 **Add Claim**（添加声明）。

可以添加以下声明。

### Audience（受众） <a href="#audience" id="audience"></a>

**Audience**（受众）或 `aud` 声明用于标识 JWT 的预期接收方。

更多信息，请参阅 [aud（受众）声明](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3)。

### Expires In（过期时间） <a href="#expires-in" id="expires-in"></a>

**Expires In**（过期时间）或 `exp` 声明标识 JWT 过期的时间，在此时间之后不得再接受该 JWT 进行处理。

更多信息，请参阅 [exp（过期时间）声明](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4)。

### Issuer（签发者） <a href="#issuer" id="issuer"></a>

**Issuer**（签发者）或 `iss` 声明用于标识签发 JWT 的主体。

更多信息，请参阅 [iss（签发者）声明](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.1)。

### JWT ID <a href="#jwt-id" id="jwt-id"></a>

**JWT ID** 或 `jti` 声明为 JWT 提供唯一标识。

更多信息，请参阅 [jti（JWT ID）声明](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.7)。

### Not Before（生效时间） <a href="#not-before" id="not-before"></a>

**Not Before**（生效时间）或 `nbf` 声明标识 JWT 的生效时间，在此时间之前不得接受该 JWT 进行处理。

更多信息，请参阅 [nbf（生效时间）声明](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.5)。

### Subject（主题） <a href="#subject" id="subject"></a>

**Subject**（主题）或 `sub` 声明标识 JWT 所涉及的主体。

更多信息，请参阅 [sub（主题）声明](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.2)。

## 节点选项 <a href="#node-options" id="node-options"></a>

### Decode（解码）节点选项 <a href="#decode-node-options" id="decode-node-options"></a>

**Return Additional Info**（返回额外信息）开关控制节点返回的信息量。

开启时，节点返回完整的解码后令牌，包含头部和签名信息；关闭时，仅返回载荷。

### Sign（签名）节点选项 <a href="#sign-node-options" id="sign-node-options"></a>

使用 **Override Algorithm**（覆盖算法）选择签名令牌所用的算法，此设置覆盖凭据中选择的算法。

### Verify（验证）节点选项 <a href="#verify-node-options" id="verify-node-options"></a>

此操作包含以下节点选项：

* **Return Additional Info**（返回额外信息）：控制节点返回的信息量。开启时返回完整的解码后令牌，包含头部和签名信息；关闭时，仅返回载荷。
* **Ignore Expiration**（忽略过期时间）：控制是否忽略令牌的过期时间声明（`exp`）。更多信息，请参阅 [exp（过期时间）声明](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4)。
* **Ignore Not Before Claim**（忽略生效时间声明）：控制是否忽略令牌的生效时间声明（`nbf`）。更多信息，请参阅 [nbf（生效时间）声明](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.5)。
* **Clock Tolerance**（时钟容差）：输入检查 `nbf` 和 `exp` 声明时可容忍的秒数，用于应对不同服务器间的微小时钟差异。更多信息，请参阅 [exp（过期时间）声明](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4)。
* **Override Algorithm**（覆盖算法）：验证令牌所用的算法，此设置覆盖凭据中选择的算法。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 JWT 集成模板](https://n8n.io/integrations/jwt)，或[搜索所有模板](https://n8n.io/workflows/)
