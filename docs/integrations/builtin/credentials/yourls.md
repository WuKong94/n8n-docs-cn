---
title: Yourls 凭据
description: Yourls 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Yourls 的身份验证。
contentType:
- integration
- reference
nodeTitle: Yourls 凭据
originalFilePath: integrations/builtin/credentials/yourls.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/yourls
url: https://docs.n8n.io/integrations/builtin/credentials/yourls
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Yourls 凭据 <a href="#yourls-credentials" id="yourls-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Yourls](../app-nodes/n8n-nodes-base.yourls.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在服务器上安装 [Yourls](https://github.com/YOURLS/YOURLS)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Yourls 文档](https://yourls.org/docs)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **Signature（签名）** 令牌：进入 **Tools > Secure passwordless API call（工具 > 安全的无密码 API 调用）**，获取 **Signature** 令牌。更多信息请参阅 [Yourls 无密码 API 文档](https://yourls.org/docs/guide/advanced/passwordless-api)。
- 一个 **URL**：输入 Yourls 实例的 URL。

