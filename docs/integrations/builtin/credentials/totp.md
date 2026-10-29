---
title: TOTP 凭据
description: TOTP 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 TOTP 的身份验证。
contentType:
- integration
- reference
nodeTitle: TOTP 凭据
originalFilePath: integrations/builtin/credentials/totp.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/totp
url: https://docs.n8n.io/integrations/builtin/credentials/totp
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# TOTP 凭据 <a href="#totp-credentials" id="totp-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [TOTP](../core-nodes/n8n-nodes-base.totp.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

生成 TOTP **Secret**（密钥）和 **Label**（标签）。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Secret and label（密钥和标签）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

基于时间的一次性密码（TOTP）是一种利用当前时间生成一次性密码（OTP）的算法。更多信息请参阅 [Google Authenticator | Key URI format](https://github.com/google/google-authenticator/wiki/Key-Uri-Format)。

## 使用密钥和标签 <a href="#using-secret-and-label" id="using-secret-and-label"></a>

配置此凭据需要：

- **Secret**（密钥）：设置身份验证器时编码在二维码中的密钥，使用 Base32 编码的任意密钥值，例如 `BVDRSBXQB2ZEL5HE`。更多信息请参阅 [Google Authenticator Secret](https://github.com/google/google-authenticator/wiki/Key-Uri-Format#secret)。
- **Label**（标签）：账户标识符，包含以 URI 编码字符串表示的账户名称。可添加前缀，用于标识管理账户的提供商或服务。使用前缀时，以字面冒号或 URL 编码的冒号分隔签发者前缀与账户名称，例如 `GitHub:john-doe`。更多信息请参阅 [Google Authenticator Label](https://github.com/google/google-authenticator/wiki/Key-Uri-Format#label)。
