---
title: Cohere 凭据
description: Cohere 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Cohere 的身份验证。
contentType:
- integration
- reference
nodeTitle: Cohere 凭据
originalFilePath: integrations/builtin/credentials/cohere.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/cohere
url: https://docs.n8n.io/integrations/builtin/credentials/cohere
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Cohere 凭据 <a href="#cohere-credentials" id="cohere-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Cohere](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere.md)
* [Cohere Chat（聊天）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatcohere.md)
* [Reranker Cohere（重排序器）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere.md)
* [Embeddings Cohere（嵌入模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Cohere 账户](https://cohere.com/)。

账户需要具备以下访问权限：

- 使用 Trial API 时，需要 User（用户）或 Owner（所有者）权限。
- 使用 Production API 时，需要 Owner（所有者）权限。

更多信息请参阅 [Cohere Teams and Roles 文档](https://docs.cohere.com/reference/teams-and-roles)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Cohere 文档](https://docs.cohere.com/reference/about)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **API Key**（API 密钥）：在 [Cohere 控制台的 API Keys 部分](https://dashboard.cohere.com/api-keys)生成 Cohere API 密钥。
