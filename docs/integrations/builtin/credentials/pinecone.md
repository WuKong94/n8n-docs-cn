---
title: Pinecone 凭据
description: Pinecone 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Pinecone 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Pinecone 凭据
originalFilePath: integrations/builtin/credentials/pinecone.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/pinecone
url: https://docs.n8n.io/integrations/builtin/credentials/pinecone
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Pinecone 凭据 <a href="#pinecone-credentials" id="pinecone-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Pinecone Vector Store（向量存储）](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Pinecone 文档](https://docs.pinecone.io/reference/api/introduction)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个 [Pinecone](https://www.pinecone.io/) 账号，以及：

- 一个 **API Key（API 密钥）**

获取 API 密钥：

1. 打开 [Pinecone 控制台](https://app.pinecone.io/organizations/-/projects)。
2. 选择要为其创建 API 密钥的项目。如果还没有项目，先创建一个。更多信息请参阅 Pinecone [快速入门](https://docs.pinecone.io/guides/get-started/quickstart)。
3. 进入 **API Keys**（API 密钥）。
4. 复制其中显示的 API 密钥，填入 n8n 凭据。

更多信息请参阅 Pinecone API [身份验证文档](https://docs.pinecone.io/guides/get-started/authentication)。
