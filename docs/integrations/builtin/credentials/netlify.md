---
title: Netlify 凭据
description: Netlify 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Netlify 的身份验证。
contentType:
- integration
- reference
nodeTitle: Netlify 凭据
originalFilePath: integrations/builtin/credentials/netlify.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/netlify
url: https://docs.n8n.io/integrations/builtin/credentials/netlify
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Netlify 凭据 <a href="#netlify-credentials" id="netlify-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Netlify](../app-nodes/n8n-nodes-base.netlify.md)
- [Netlify Trigger（触发器）](../trigger-nodes/n8n-nodes-base.netlifytrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Netlify](https://netlify.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Netlify API 文档](https://docs.netlify.com/api/get-started/)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要：

- 一个 **Access Token（访问令牌）**：在 **Applications > Personal Access Tokens（应用 > 个人访问令牌）** 中生成令牌。详细说明请参阅 [Netlify API 身份验证](https://docs.netlify.com/api/get-started/#authentication)。

