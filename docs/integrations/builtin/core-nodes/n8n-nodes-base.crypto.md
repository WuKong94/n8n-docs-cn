---
title: Crypto（加密）
description: 了解 n8n 工作流自动化平台中的 Crypto 节点，包括用法说明和示例链接。
contentType:
- integration
- reference
priority: medium
nodeTitle: Crypto（加密）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.crypto.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Crypto（加密） <a href="#crypto" id="crypto"></a>

使用 Crypto 节点在工作流中执行密码学操作。

{% hint style="info" %}
**凭据**

有关此节点的身份验证信息，请参阅 [Crypto 凭据文档](../credentials/crypto.md)。
{% endhint %}

## 动作 <a href="#actions" id="actions"></a>

* 使用口令或私钥[**Decrypt**（解密）字符串](#decrypt-parameters)。
* 使用口令或公钥[**Encrypt**（加密）字符串](#encrypt-parameters)。
* [**Generate**（生成）随机字符串](#generate-parameters)。
* 按指定格式对文本或文件计算[**Hash**（哈希）](#hash-parameters)。
* 按指定格式对文本或文件计算[**Hmac**](#hmac-parameters)。
* 使用私钥对字符串进行[**Sign**（签名）](#sign-parameters)。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

节点参数取决于所选动作。

**Hmac**、**Sign**（签名）、**Encrypt**（加密）和 **Decrypt**（解密）动作需要 [Crypto 凭据](../credentials/crypto.md)。每种动作使用相应的凭据字段：

* **Hmac** 使用 **Hmac Secret**（Hmac 密钥）。
* **Sign**（签名）使用 **Private Key**（私钥）。
* **Encrypt**（加密）和 **Decrypt**（解密）在对称模式下使用 **Encryption Passphrase**（加密口令），在非对称模式下分别使用 **Encryption Public Key**（加密公钥）和 **Encryption Private Key**（加密私钥）。

### Decrypt（解密）参数 <a href="#decrypt-parameters" id="decrypt-parameters"></a>

* **Mode**（模式）：选择要使用的模式，必须与加密时使用的模式一致。可选：
    * **Symmetric (Passphrase)**（对称：口令）：使用口令和认证加密算法解密。
    * **Asymmetric (RSA)**（非对称：RSA）：使用 RSA 私钥解密。
* **Cipher**（加密算法）：选择 **Symmetric (Passphrase)**（对称：口令）时，选择要使用的认证加密算法，必须与加密时一致。可选：
    * **AES-256-GCM**
    * **AES-192-GCM**
    * **AES-128-GCM**
    * **ChaCha20-Poly1305**
* **Value**（值）：输入 **Encrypt**（加密）动作生成的 base64 字符串。
* **Property Name**（属性名称）：输入用于写入解密结果的属性名称。

### Encrypt（加密）参数 <a href="#encrypt-parameters" id="encrypt-parameters"></a>

* **Mode**（模式）：选择要使用的模式，可选：
    * **Symmetric (Passphrase)**（对称：口令）：使用口令和认证加密算法加密。
    * **Asymmetric (RSA)**（非对称：RSA）：使用 RSA 公钥加密。
* **Cipher**（加密算法）：选择 **Symmetric (Passphrase)**（对称：口令）时，选择要使用的认证加密算法，解密时必须选择同一算法。可选：
    * **AES-256-GCM**
    * **AES-192-GCM**
    * **AES-128-GCM**
    * **ChaCha20-Poly1305**
* **Value**（值）：输入要加密的值。
* **Property Name**（属性名称）：输入用于写入加密结果的属性名称。节点将结果写为 base64 字符串。

{% hint style="info" %}
**RSA 载荷大小**

非对称（RSA）模式只能加密少量数据，使用 2048 位密钥时约为 190 字节。较大的数据请使用对称模式。
{% endhint %}

### Generate（生成）参数 <a href="#generate-parameters" id="generate-parameters"></a>

* **Property Name**（属性名称）：输入用于写入随机字符串的属性名称。
* **Type**（类型）：选择用于生成字符串的编码类型，可选：
    * **ASCII**
    * **BASE64**
    * **HEX**
    * **UUID**
* **Length**（长度）：选择 **ASCII**、**BASE64** 或 **HEX** 时，输入要生成的字符串长度，默认值为 `32`。

### Hash（哈希）参数 <a href="#hash-parameters" id="hash-parameters"></a>

* **Type**（类型）：选择要使用的哈希类型，可选：
    * **MD5**
    * **SHA256**
    * **SHA3-256**
    * **SHA3-384**
    * **SHA3-512**
    * **SHA384**
    * **SHA512**
* **Binary File**（二进制文件）：如果要计算哈希的数据来自二进制文件，开启此参数。
    * **Value**（值）：关闭 **Binary File**（二进制文件）时，输入要计算哈希的值。
    * **Binary Property Name**（二进制属性名称）：开启 **Binary File**（二进制文件）时，输入包含待计算哈希数据的二进制属性名称。
* **Property Name**（属性名称）：输入用于写入哈希结果的属性名称。
* **Encoding**（编码）：选择要使用的编码类型，可选：
    * **BASE64**
    * **HEX**

### Hmac 参数 <a href="#hmac-parameters" id="hmac-parameters"></a>

* **Binary File**（二进制文件）：如果要计算 Hmac 的数据来自二进制文件，开启此参数。
    * **Value**（值）：关闭 **Binary File**（二进制文件）时，输入要计算 Hmac 的值。
    * **Binary Property Name**（二进制属性名称）：开启 **Binary File**（二进制文件）时，输入包含待计算 Hmac 数据的二进制属性名称。
* **Type**（类型）：选择要使用的哈希类型，可选：
    * **MD5**
    * **SHA256**
    * **SHA3-256**
    * **SHA3-384**
    * **SHA3-512**
    * **SHA384**
    * **SHA512**
* **Property Name**（属性名称）：输入用于写入 Hmac 结果的属性名称。
* **Encoding**（编码）：选择要使用的编码类型，可选：
    * **BASE64**
    * **HEX**

此动作使用 [Crypto 凭据](../credentials/crypto.md)中的 **Hmac Secret**（Hmac 密钥）。

### Sign（签名）参数 <a href="#sign-parameters" id="sign-parameters"></a>

* **Value**（值）：输入要签名的值。
* **Property Name**（属性名称）：输入用于写入签名结果的属性名称。
* **Algorithm Name or ID**（算法名称或 ID）：从列表中选择算法名称，或通过[表达式](../../../build/work-with-data/expressions-versus-data-nodes.md)指定 ID。
* **Encoding**（编码）：选择要使用的编码类型，可选：
    * **BASE64**
    * **HEX**

此动作使用 [Crypto 凭据](../credentials/crypto.md)中的 **Private Key**（私钥）。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Crypto 集成模板](https://n8n.io/integrations/crypto)，或[搜索所有模板](https://n8n.io/workflows/)
