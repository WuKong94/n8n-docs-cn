---
title: Chroma 凭据
description: Chroma 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Chroma 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Chroma 凭据
originalFilePath: integrations/builtin/credentials/chroma.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/chroma
url: https://docs.n8n.io/integrations/builtin/credentials/chroma
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Chroma 凭据 <a href="#chroma-credentials" id="chroma-credentials"></a>

这些凭据可用于以下节点的身份验证：

- Chroma Vector Store（向量存储）

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>
创建并运行 [Chroma](https://www.trychroma.com/home) 实例。更多信息，请参阅[以客户端与服务器模式运行 Chroma](https://docs.trychroma.com/docs/run-chroma/client-server)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>
- API key（API 密钥）
- Instance URL（实例 URL）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Chroma 文档](https://docs.trychroma.com/docs/overview/getting-started)。云实例的使用方法，还可参阅 [Chroma Cloud](https://docs.trychroma.com/cloud/getting-started)。

查看 n8n 的[高级 AI](../../../build/integrate-ai/README.md) 文档。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个 [Chroma](https://www.trychroma.com/) 账户，以及：

- 一个 **API Key（API 密钥）**
- **Tenant ID**（租户 ID）
- **Database Name**（数据库名称）

设置步骤如下：

1. 进入 **Cloud Dashboard**（云控制台）。
2. 创建 **Database**（数据库）。
3. 点击要访问的数据库的 **Settings**（设置）。
4. 点击 **Create API key and copy code**（创建 API 密钥并复制代码）。
5. 将 **API Key**（API 密钥）、**Tenant ID**（租户 ID）和 **Database Name**（数据库名称）填入 n8n 凭据。
## 使用实例 URL <a href="#using-instance-url" id="using-instance-url"></a>

配置此凭据需要：

- **Base URL:**（基础 URL）：Chroma 实例的基础 URL，默认值为 `http://localhost:8000`。
