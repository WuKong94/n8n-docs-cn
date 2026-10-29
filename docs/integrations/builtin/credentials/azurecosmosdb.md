---
title: Azure Cosmos DB 凭据
description: Azure Cosmos DB 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Azure Cosmos DB 的身份验证。
contentType:
- integration
- reference
nodeTitle: Azure Cosmos DB 凭据
originalFilePath: integrations/builtin/credentials/azurecosmosdb.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/azurecosmosdb
url: https://docs.n8n.io/integrations/builtin/credentials/azurecosmosdb
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Azure Cosmos DB 凭据 <a href="#azure-cosmos-db-credentials" id="azure-cosmos-db-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Azure Cosmos DB](../app-nodes/n8n-nodes-base.azurecosmosdb.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建一个 [Azure](https://azure.microsoft.com) 订阅。
* 创建一个 [Azure Cosmos DB 账户](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-manage-database-account)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API Key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>


有关该服务的更多信息，请参阅 [Azure Cosmos DB API 文档](https://learn.microsoft.com/en-us/rest/api/cosmos-db/)。


## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

* **Account**（账户）：Azure Cosmos DB 账户的名称。
* **Key**（密钥）：Azure Cosmos DB 账户的密钥。在 Azure 门户中打开对应的 Azure Cosmos DB，选择 **Overview**（概览）> **Keys**（密钥）。两个账户密钥任选其一即可。
* **Database**（数据库）：要连接的 Azure Cosmos DB 数据库名称。

详细步骤请参阅 [Get your primary key | Microsoft](https://learn.microsoft.com/en-us/previous-versions/azure/cosmos-db/how-to-obtain-keys?tabs=azure-portal)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下列出 Azure Cosmos DB 凭据的已知常见错误和问题。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/microsoft-need-admin-approval.md" %}
