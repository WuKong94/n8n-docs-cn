---
title: Azure Cosmos DB 节点文档
description: 了解如何在 n8n 中使用 Azure Cosmos DB 节点，并按照技术文档将 Azure Cosmos DB 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Azure Cosmos DB 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.azurecosmosdb.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurecosmosdb
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurecosmosdb
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Azure Cosmos DB 节点 <a href="#azure-cosmos-db-node" id="azure-cosmos-db-node"></a>

使用 Azure Cosmos DB 节点自动处理 Azure Cosmos DB 中的工作，并将其与其他应用集成。n8n 内置支持多种 Azure Cosmos DB 功能，包括创建、获取、更新和删除容器及数据项。

本页列出了 Azure Cosmos DB 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

该节点的身份验证信息，请参阅 [Azure Cosmos DB 凭据文档](../credentials/azurecosmosdb.md)。
{% endhint %}


## 操作 <a href="#operations" id="operations"></a>

* **Container**（容器）：
    * **Create**（创建）
    * **Delete**（删除）
    * **Get**（获取）
    * **Get Many**（获取多条）
* **Item**（数据项）：
    * **Create**（创建）
    * **Delete**（删除）
    * **Get**（获取）
    * **Get Many**（获取多条）
    * **Execute Query**（执行查询）
    * **Update**（更新）

## Item: Execute Query（数据项：执行查询） <a href="#item-execute-query" id="item-execute-query"></a>

对容器执行 NoSQL SQL 查询，返回匹配的数据项。

### 参数 <a href="#parameters" id="parameters"></a>

| 参数 | 是否必填 | 说明 |
| --- | --- | --- |
| **Container**（容器） | 是 | 执行查询的容器。可从列表中选择，或直接输入容器 ID。 |
| **Query**（查询） | 是 | 要执行的 SQL 查询。使用 `$1`、`$2`、`$3` 等作为查询参数的位置占位符。向 Azure Cosmos DB 发送请求前，n8n 会自动将其转换为 `@Param1`、`@Param2`、`@Param3`。例如：`SELECT * FROM c WHERE c.status = $1 AND c.startDate = $2`。 |
| **Simplify**（简化） | 否 | 开启时（默认），从返回的数据项中移除 Cosmos DB 内部元数据字段，即以 `_` 开头的字段。关闭可接收完整的原始 API 响应。 |

### 选项 <a href="#options" id="options"></a>

展开 **Options**（选项），配置查询参数。

| 选项 | 说明 |
| --- | --- |
| **Query Parameters**（查询参数） | 以逗号分隔的字符串值列表，按位置映射到查询中的 `$1`、`$2` 等。**所有值始终以字符串发送。**适用于名称或状态值等简单文本筛选。例如：`active,2024`。 |
| **Query Parameters (JSON)**（查询参数，JSON） | JSON 值数组，按位置映射到查询中的 `$1`、`$2` 等。保留原生类型，包括数字、布尔值、`null`，以及带前导零的字符串。当类型精度很重要时，请用它代替 **Query Parameters**（查询参数）。例如：`[1737062400000, "01234", true, null]`。 |

{% hint style="info" %}
**如何选择 Query Parameters 和 Query Parameters (JSON)**

Azure Cosmos DB 的比较对类型敏感。例如，对于以下筛选条件：
`WHERE c.startDate = $1`，如果 `startDate` 在数据库中存储为数字，
而传入的参数是字符串，则不会返回任何结果。

- 当所有筛选值都是文本，例如名称、状态或标识符时，使用 **Query Parameters**（查询参数）。
- 当需要按数字、布尔值、`null` 筛选，或值以数字开头但必须保留为字符串时，例如邮政编码 `"01234"`，使用 **Query Parameters (JSON)**（查询参数，JSON）。

**限制：**JavaScript 的 JSON 解析器无法完整精确表示大于
`Number.MAX_SAFE_INTEGER`（`9007199254740991`）的整数。超过
此限制的值，在使用 **Query Parameters (JSON)** 时可能丢失精度。
{% endhint %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Azure Cosmos DB 集成模板](https://n8n.io/integrations/azure-cosmos-db)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>


有关该服务的更多信息，请参阅 [Azure Cosmos DB 文档](https://learn.microsoft.com/en-us/rest/api/cosmos-db/)。


{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
