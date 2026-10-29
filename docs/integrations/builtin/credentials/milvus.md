---
title: Milvus 凭据
description: Milvus 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Milvus 的身份验证。
contentType:
- integration
- reference
priority: high
nodeTitle: Milvus 凭据
originalFilePath: integrations/builtin/credentials/milvus.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/milvus
url: https://docs.n8n.io/integrations/builtin/credentials/milvus
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Milvus 凭据 <a href="#milvus-credentials" id="milvus-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Milvus Vector Store（向量存储）](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建并运行一个 [Milvus](https://milvus.io/) 实例。更多信息请参阅[安装 Milvus](https://milvus.io/docs/install-overview.md)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

身份验证设置的更多信息，请参阅 [Milvus 身份验证文档](https://milvus.io/docs/authenticate.md?tab=docker#Authenticate-User-Access)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

配置此凭据需要：

* **Base URL**（基础 URL）：Milvus 实例的基础 URL，默认值为 `http://localhost:19530`。
* **Username**（用户名）：向 Milvus 实例进行身份验证的用户名，默认值为 `root`。
* **Password**（密码）：向 Milvus 实例进行身份验证的密码，默认值为 `Milvus`。
