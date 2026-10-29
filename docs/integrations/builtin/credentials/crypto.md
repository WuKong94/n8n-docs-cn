---
title: Crypto 凭据
description: Crypto 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Crypto 的身份验证。
contentType:
- integration
- reference
priority: medium
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Crypto 凭据 <a id="crypto-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Crypto](../core-nodes/n8n-nodes-base.crypto.md)

## 凭据字段 <a id="credential-fields"></a>

只配置所用操作需要的字段，所有字段均为可选。

* **Hmac Secret**（HMAC 密钥）：供 **Hmac** 操作使用的密钥。
* **Private Key**（私钥）：供 **Sign**（签名）操作使用的私钥。
* **Encryption Passphrase**（加密口令）：对称模式下，供 **Encrypt**（加密）和 **Decrypt**（解密）操作使用。使用至少 16 个随机字符，或由密码管理器生成的强口令。
* **Encryption Public Key**（加密公钥）：非对称模式下，供 **Encrypt** 操作使用的 RSA 公钥，采用 PEM、SPKI 格式。
* **Encryption Private Key**（加密私钥）：非对称模式下，供 **Decrypt** 操作使用的 RSA 私钥，采用 PEM、PKCS#8 格式。

## 相关资源 <a id="related-resources"></a>

各操作的详细信息，请参阅 [Crypto 节点文档](../core-nodes/n8n-nodes-base.crypto.md)。