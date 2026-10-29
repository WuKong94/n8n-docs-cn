---
title: Qdrant 凭据
description: Qdrant 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Qdrant 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Qdrant 凭据
originalFilePath: integrations/builtin/credentials/qdrant.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/qdrant
url: https://docs.n8n.io/integrations/builtin/credentials/qdrant
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Qdrant 凭据 <a href="#qdrant-credentials" id="qdrant-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Qdrant Vector Store（向量存储）](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

更多信息请参阅 [Qdrant 文档](https://qdrant.tech/documentation/)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个 [Qdrant 集群](https://qdrant.tech/documentation/cloud/create-cluster/)，以及：

- 一个 **API Key（API 密钥）**
- 你的 **Qdrant URL**

设置步骤如下：

1. 进入 [Cloud Dashboard（云控制台）](https://qdrant.to/cloud)。
2. 选择 **Access Management**（访问管理）查看可用的 API 密钥，或进入 **Cluster detail**（集群详情）页面的 **API Keys**（API 密钥）部分。
3. 选择 **Create**（创建）。
4. 在下拉菜单中选择该密钥可访问的集群。
5. 选择 **OK**（确定）。
6. 复制 API Key（API 密钥），填入 n8n 凭据。
7. 在 **Qdrant URL** 中输入 Qdrant 集群的 URL。更多信息请参阅 [Qdrant Web UI](https://qdrant.tech/documentation/interfaces/web-ui/)。

创建和使用 API 密钥的更多信息，请参阅 [Qdrant 身份验证文档](https://qdrant.tech/documentation/cloud/authentication/)。
