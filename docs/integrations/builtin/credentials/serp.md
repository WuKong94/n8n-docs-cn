---
title: Serp 凭据
description: Serp 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Serp 的身份验证。
contentType:
- integration
- reference
priority: high
nodeTitle: Serp 凭据
originalFilePath: integrations/builtin/credentials/serp.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/serp
url: https://docs.n8n.io/integrations/builtin/credentials/serp
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Serp 凭据 <a href="#serp-credentials" id="serp-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Serp](../cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [SerpApi](https://serpapi.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Serp API 文档](https://serpapi.com/search-api)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**

获取 API 密钥的步骤如下：

1. 进入 **Your Account（你的账号）>** [**API Key（API 密钥）**](https://serpapi.com/manage-api-key)。
2. 复制 **Your Private API Key（你的私有 API 密钥）**，填入 n8n 凭据的 **API Key** 字段。
