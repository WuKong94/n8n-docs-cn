---
title: Azure AI Search 凭据
description: Azure AI Search 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Azure AI Search 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Azure AI Search 凭据
originalFilePath: integrations/builtin/credentials/azureaisearch.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/azureaisearch
url: https://docs.n8n.io/integrations/builtin/credentials/azureaisearch
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Azure AI Search 凭据 <a href="#azure-ai-search-credentials" id="azure-ai-search-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Azure AI Search Vector Store（向量存储）](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- [Azure 订阅](https://azure.microsoft.com)
- 在 [Azure Portal](https://portal.azure.com/) 中创建的 Azure AI Search 服务

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

此节点使用 API 密钥身份验证。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Azure AI Search 文档](https://learn.microsoft.com/azure/search/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **Endpoint**（端点）：Azure AI Search 服务的 URL（格式：`https://your-service.search.windows.net`）
- **API Key**（API 密钥）：管理员密钥（读写）或查询密钥（只读）

获取这些值的步骤如下：

1. 在 [Azure Portal](https://portal.azure.com/) 中打开 Azure AI Search 服务。
2. 从 **Overview**（概览）部分复制 **URL**。
3. 进入 **Settings**（设置）> **Keys**（密钥），复制以下任一密钥：
   - **Admin key**（管理员密钥）：提供完整读写权限，或
   - **Query key**（查询密钥）：仅用于只读查询
4. 将这些值填入 n8n。

{% hint style="info" %}
**API 密钥权限**

管理员密钥提供完整访问权限，包括创建和删除索引；查询密钥提供只读权限。请根据工作流需求选择。
{% endhint %}

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

### 身份验证错误 <a href="#authentication-errors" id="authentication-errors"></a>

**API 密钥身份验证失败**：
- 确认 API 密钥正确，且未在 Azure Portal 中重新生成
- 确认写入操作（插入或更新）使用管理员密钥
- 检查密钥是否已过期或轮换

### 连接问题 <a href="#connection-issues" id="connection-issues"></a>

- 验证端点 URL 格式：`https://your-service.search.windows.net`
- 确认 Azure AI Search 服务正在运行
- 检查网络安全规则和防火墙设置是否允许 n8n 实例访问
