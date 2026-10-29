---
title: Azure AI Search Vector Store（Azure AI Search 向量存储） 节点文档
contentType:
- integration
- reference
priority: medium
nodeTitle: Azure AI Search Vector Store（Azure AI Search 向量存储） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch
description: 了解如何在 n8n 中使用 Azure AI Search Vector Store（Azure AI Search 向量存储） 节点，并按照技术文档将其集成到工作流中。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Azure AI Search Vector Store（Azure AI Search 向量存储） <a id="azure-ai-search-vector-store"></a>

Azure AI Search（原名 Azure Cognitive Search）是一项云搜索服务，提供适用于 RAG 和语义搜索应用的向量搜索能力。使用此节点，存储、检索和查询嵌入向量及其对应的内容和元数据。

本页列出了 Azure AI Search Vector Store 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Azure AI Search 凭据文档](../../credentials/azureaisearch.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

使用此节点前，需要：

1. [Azure 订阅](https://azure.microsoft.com)
2. [Azure AI Search 服务](https://learn.microsoft.com/azure/search/search-create-service-portal)
3. 已配置 API 密钥身份验证（写入操作使用管理员密钥，只读操作使用查询密钥）

    设置说明，请参阅[凭据文档](../../credentials/azureaisearch.md)。

### 索引配置 <a href="#index-configuration" id="index-configuration"></a>

索引不存在时，节点会自动创建索引。自动创建时，节点会配置：

* 根据嵌入模型设置适当维度的向量字段
* 使用余弦度量的 HNSW 算法，实现高效相似度搜索
* 用于过滤和检索的内容及元数据字段

也可在 Azure Portal 中预先创建索引，使用自定义配置。架构示例：

```json
{
  "name": "n8n-vectorstore",
  "fields": [
    {
      "name": "id",
      "type": "Edm.String",
      "key": true,
      "filterable": true
    },
    {
      "name": "content",
      "type": "Edm.String",
      "searchable": true
    },
    {
      "name": "content_vector",
      "type": "Collection(Edm.Single)",
      "searchable": true,
      "vectorSearchDimensions": 1536,
      "vectorSearchProfileName": "n8n-vector-profile"
    },
    {
      "name": "metadata",
      "type": "Edm.String",
      "filterable": true
    }
  ],
  "vectorSearch": {
    "profiles": [
      {
        "name": "n8n-vector-profile",
        "algorithm": "n8n-vector-algorithm"
      }
    ],
    "algorithms": [
      {
        "name": "n8n-vector-algorithm",
        "kind": "hnsw",
        "hnswParameters": {
          "metric": "cosine",
          "m": 4,
          "efConstruction": 400,
          "efSearch": 500
        }
      }
    ]
  }
}
```

{% hint style="info" %}
**向量维度**

`vectorSearchDimensions` 值必须与嵌入模型的输出匹配。
{% endhint %}

## 节点使用模式 <a href="#node-usage-patterns" id="node-usage-patterns"></a>

### 作为普通节点插入和检索文档 <a href="#use-as-a-regular-node-to-insert-and-retrieve-documents" id="use-as-a-regular-node-to-insert-and-retrieve-documents"></a>

直接在工作流中使用此节点插入或检索文档，无需智能体。模式示例，请参阅[此模板](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/)（使用 Supabase，但模式完全相同）。

### 作为工具直接连接到 AI 智能体 <a href="#connect-directly-to-an-ai-agent-as-a-tool" id="connect-directly-to-an-ai-agent-as-a-tool"></a>

连接到 [AI 智能体](n8n-nodes-langchain.agent/README.md)的工具连接器，将向量存储用作可搜索的知识库：

AI Agent（工具连接器）→ Azure AI Search Vector Store 节点

### 使用检索器获取文档 <a href="#use-a-retriever-to-fetch-documents" id="use-a-retriever-to-fetch-documents"></a>

与 [Vector Store Retriever](../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) 和 [Question and Answer Chain](n8n-nodes-langchain.chainretrievalqa/README.md) 配合使用，实现检索增强生成：

Question and Answer Chain（Retriever）→ Vector Store Retriever（Vector Store）→ Azure AI Search Vector Store

请参阅[此示例工作流](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)。

### 使用 Vector Store Question Answer Tool <a href="#use-the-vector-store-question-answer-tool" id="use-the-vector-store-question-answer-tool"></a>

使用 [Vector Store Question Answer Tool](../sub-nodes/n8n-nodes-langchain.toolvectorstore.md) 汇总信息并回答问题：

AI Agent（工具）→ Vector Store Question Answer Tool（Vector Store）→ Azure AI Search Vector Store

请参阅[此示例](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/vector-store-mode-with-update.md" %}

### Rerank Results（结果重排序） <a href="#rerank-results" id="rerank-results"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/vector-store-rerank-results.md" %}

{% hint style="info" %}
**Azure AI Search 语义重排序**

Azure AI Search 内置[语义重排序](https://learn.microsoft.com/azure/search/semantic-search-overview)，使用 **Semantic Hybrid**（语义混合）查询模式并配置语义设置时可用。使用步骤：

1. 在 Options（选项）中，将 **Query Mode**（查询模式）设为 **Semantic Hybrid**（语义混合）
2. 将 **Semantic Configuration**（语义配置）设为你的配置名称（未指定时默认为 `semantic-search-config`）

内置语义重排序器使用机器学习模型提高相关性。还可在语义重排序之后串联额外的重排序节点，进一步优化结果。

仅当索引定义了语义配置时，[语义重排序](https://learn.microsoft.com/azure/search/semantic-search-overview)才可用。
{% endhint %}

### Get Many（获取多条）参数 <a href="#get-many-parameters" id="get-many-parameters"></a>

* **Endpoint**（端点）：Azure AI Search 端点（格式：`https://your-service.search.windows.net`）
* **Index Name**（索引名称）：要查询的索引
* **Limit**（上限）：返回的最大文档数量（默认值：4）

### Insert Documents（插入文档）参数 <a href="#insert-documents-parameters" id="insert-documents-parameters"></a>

* **Endpoint**（端点）：Azure AI Search 端点
* **Index Name**（索引名称）：要使用的索引（不存在时自动创建）
* **Batch Size**（批次大小）：每批上传到 Azure AI Search 的文档数量。请根据文档大小及服务层级限制调整。此选项仅控制上传批次；生成嵌入的批次在嵌入节点中配置。

### Update Documents（更新文档）参数 <a href="#update-documents-parameters" id="update-documents-parameters"></a>

* **Endpoint**（端点）：Azure AI Search 端点
* **Index Name**（索引名称）：要更新的索引

### Retrieve Documents（作为链或工具的向量存储）参数 <a href="#retrieve-documents-parameters-as-vector-store-for-chaintool" id="retrieve-documents-parameters-as-vector-store-for-chaintool"></a>

* **Endpoint**（端点）：Azure AI Search 端点
* **Index Name**（索引名称）：要查询的索引

### Retrieve Documents（作为 AI 智能体的工具）参数 <a href="#retrieve-documents-as-tool-for-ai-agent-parameters" id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

* **Name**（名称）：向 LLM 显示的工具名称
* **Description**（描述）：向 LLM 说明此工具的用途。描述应具体，帮助 LLM 判断何时使用此工具。
* **Endpoint**（端点）：Azure AI Search 端点
* **Index Name**（索引名称）：要查询的索引
* **Limit**（上限）：检索结果的最大数量（例如，`10` 表示最匹配的十条结果）

## 节点选项 <a href="#node-options" id="node-options"></a>

### Options（选项） <a href="#options" id="options"></a>

* **Filter**（过滤器）：使用 [OData 过滤表达式](https://learn.microsoft.com/azure/search/search-query-odata-filter)，按文档字段或元数据过滤结果。请参阅下方过滤器示例。
* **Query Mode**（查询模式）：使用的搜索策略：
  * **Vector**（向量）：仅使用嵌入进行相似度搜索
  * **Keyword**（关键词）：使用 BM25 排序进行全文搜索
  * **Hybrid**（混合，默认）：使用倒数排名融合（RRF），结合向量搜索和关键词搜索
  * **Semantic Hybrid**（语义混合）：结合[语义重排序](https://learn.microsoft.com/azure/search/semantic-search-overview)的混合搜索，提高相关性
* **Semantic Configuration**（语义配置）：用于[语义排序](https://learn.microsoft.com/azure/search/semantic-search-overview)的语义配置名称。未指定时默认为 `semantic-search-config`。仅当预先创建索引并使用自定义语义配置名称时，才需要填写。

{% hint style="info" %}
**选择查询模式**

语义相似度搜索使用 **Vector**（向量）；精确词项匹配使用 **Keyword**（关键词）；均衡结果使用 **Hybrid**（混合）；如果已在索引中配置语义搜索，希望尽可能提高相关性，则使用 **Semantic Hybrid**（语义混合）。
{% endhint %}

### OData 过滤器示例 <a href="#odata-filter-examples" id="odata-filter-examples"></a>

Azure AI Search 使用 [OData 语法](https://learn.microsoft.com/azure/search/search-query-odata-filter)进行过滤，元数据字段通过 `metadata/fieldName` 格式访问。

**按文档 ID 过滤：**

```
id eq '3da6491a-f930-4a4e-9471-c05dcd450ba0'
```

**按元数据字段过滤：**

```
metadata/source eq 'user-guide'
```

**复杂 AND 过滤器：**

```
metadata/category eq 'technology' and metadata/author eq 'John'
```

**复杂 OR 过滤器：**

```
metadata/source eq 'user-guide' or metadata/rating ge 4
```

**数值比较：**

```
metadata/rating ge 4 and metadata/rating lt 10
```

**使用 NOT 的字符串匹配：**

```
metadata/category eq 'technology' and metadata/title ne 'Deprecated'
```

**支持的 OData 运算符：**

* 比较：`eq`、`ne`、`gt`、`ge`、`lt`、`le`
* 逻辑：`and`、`or`、`not`
* 字符串函数：`startswith()`、`endswith()`、`contains()`
* 集合函数：`any()`、`all()`

{% hint style="info" %}
**过滤器格式**

过滤器适用于所有查询模式（Vector、Keyword、Hybrid、Semantic Hybrid）和所有操作模式（retrieve、load、retrieve-as-tool）。
{% endhint %}

## Azure AI Search 特有功能 <a href="#azure-ai-search-specific-features" id="azure-ai-search-specific-features"></a>

### 使用 RRF 的混合搜索 <a href="#hybrid-search-with-rrf" id="hybrid-search-with-rrf"></a>

Azure AI Search 的混合搜索使用倒数排名融合，合并向量和关键词结果，比单独使用任一方法更准确。

### [语义排序](https://learn.microsoft.com/azure/search/semantic-search-overview) <a href="#semantic-rankinghttpslearnmicrosoftcomazuresearchsemantic-search-overview" id="semantic-rankinghttpslearnmicrosoftcomazuresearchsemantic-search-overview"></a>

Semantic Hybrid（语义混合）模式应用机器学习模型，根据对查询的语义理解重新排序结果。索引中必须具备语义配置。

### OData 过滤器 <a href="#odata-filters" id="odata-filters"></a>

在向量搜索执行之前，使用 OData 语法按文档字段或元数据过滤。需要来自特定来源或具有特定属性的结果时，这有助于提高性能和精度。

### HNSW 算法 <a href="#hnsw-algorithm" id="hnsw-algorithm"></a>

Azure AI Search 使用分层可导航小世界（HNSW）图进行近似最近邻搜索，在大规模数据上快速检索，并可配置准确性与速度之间的取舍。

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

### 索引问题 <a href="#index-issues" id="index-issues"></a>

**找不到索引**：确认索引名称正确（区分大小写），且索引存在于 Azure AI Search 服务中。使用自动创建时，检查索引是否创建成功。

**向量维度不匹配**：确保嵌入模型维度与索引向量字段维度一致。检查索引架构中的 `vectorSearchDimensions` 设置。

**文档插入失败**：

* 验证写入权限（需要管理员 API 密钥）
* 检查文档字段是否与索引架构匹配
* 确保文档提供了所有必需字段
* 大量文档导致超时时，检查批次大小设置

### 过滤器问题 <a href="#filter-issues" id="filter-issues"></a>

**过滤器不生效**：

* 确认 OData 语法正确
* 确保元数据字段使用 `metadata/` 前缀：`metadata/source eq 'value'`
* 检查索引架构中用于过滤的字段是否标记为 `filterable`
* 先测试简单过滤器（`id eq 'value'`），再测试复杂表达式

**OData 语法无效**：

* 字符串值使用单引号：`metadata/source eq 'value'`
* 使用正确的运算符：`eq`、`ne`、`gt`、`ge`、`lt`、`le`、`and`、`or`、`not`
* 语法详情，请参阅 [OData 过滤器文档](https://learn.microsoft.com/azure/search/search-query-odata-filter)

### 连接问题 <a href="#connection-issues" id="connection-issues"></a>

**无法连接**：

* 验证端点 URL 格式：`https://your-service.search.windows.net`
* 确认 Azure AI Search 服务正在运行且可访问
* 检查网络安全组、防火墙规则和专用终结点配置
* 对于托管在 Azure 上的 n8n，如果使用专用终结点，请验证虚拟网络对等互连或服务终结点配置

### 身份验证问题 <a href="#authentication-issues" id="authentication-issues"></a>

包括 API 密钥错误在内的身份验证问题，请参阅[凭据文档的故障排查部分](../../credentials/azureaisearch.md#troubleshooting)。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Azure AI Search Vector Store（Azure AI Search 向量存储） 集成模板](https://n8n.io/integrations/azure-ai-search-vector-store)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

* [Azure AI Search 向量搜索文档](https://learn.microsoft.com/azure/search/vector-search-overview)
* [Azure AI Search REST API 参考](https://learn.microsoft.com/rest/api/searchservice/)
* [Azure AI Search 的 OData 过滤器语法](https://learn.microsoft.com/azure/search/search-query-odata-filter)

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/starter-kits/self-hosted-ai-starter-kit.md" %}
