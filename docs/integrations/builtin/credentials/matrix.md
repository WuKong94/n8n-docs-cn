---
title: Matrix 凭据
description: Matrix 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Matrix 的身份验证。
contentType:
- integration
- reference
nodeTitle: Matrix 凭据
originalFilePath: integrations/builtin/credentials/matrix.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/matrix
url: https://docs.n8n.io/integrations/builtin/credentials/matrix
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Matrix 凭据 <a href="#matrix-credentials" id="matrix-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Matrix](../app-nodes/n8n-nodes-base.matrix.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在 [Matrix](https://matrix.org/) 服务器上创建账户。更多信息请参阅[创建账户](https://matrix.org/docs/chat_basics/matrix-for-im/#creating-a-matrix-account)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Matrix 规范](https://spec.matrix.org/latest/)。

请参阅你用来访问 Matrix 服务器的具体客户端文档。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要：

- **Access Token**（访问令牌）：此令牌与用于登录 Matrix 的账户关联。
- **Homeserver URL**（主服务器 URL）：创建账户时填写的 [homeserver](https://matrix.org/docs/matrix-concepts/elements-of-matrix/#homeserver) 的 URL。n8n 默认填入 matrix.org 自己的服务器地址；如果使用其他托管位置的服务器，请调整该值。

获取这些信息的步骤取决于访问服务器所用的客户端。**Access Token** 和 **Homeserver URL** 通常可在 **Settings > Help & About > Advanced**（设置 > 帮助与关于 > 高级）中找到，详情请参阅客户端文档。

