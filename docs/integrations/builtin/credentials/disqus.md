---
title: Disqus 凭据
description: Disqus 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Disqus 的身份验证。
contentType:
- integration
- reference
nodeTitle: Disqus 凭据
originalFilePath: integrations/builtin/credentials/disqus.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/disqus
url: https://docs.n8n.io/integrations/builtin/credentials/disqus
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Disqus 凭据 <a href="#disqus-credentials" id="disqus-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Disqus](../app-nodes/n8n-nodes-base.disqus.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Disqus](https://www.disqus.com/) 账号。
- 注册一个 [API 应用](https://help.disqus.com/en/articles/1717083-how-to-create-an-api-application)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Disqus API 文档](https://disqus.com/api/docs/)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要：

- 一个 **Access Token（访问令牌）**：注册 API 应用后，复制 **API Key（API 密钥）**，并将其填入 n8n 的 **Access Token** 字段。
