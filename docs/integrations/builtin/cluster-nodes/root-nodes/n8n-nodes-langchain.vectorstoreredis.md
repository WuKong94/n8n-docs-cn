---
title: Redis Vector Store（Redis 向量存储） 节点文档
contentType:
- integration
- reference
priority: medium
nodeTitle: Redis Vector Store（Redis 向量存储） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreredis.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreredis
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreredis
description: 了解如何在 n8n 中使用 Redis Vector Store（Redis 向量存储） 节点，并按照技术文档将其集成到工作流中。
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


# Redis Vector Store（Redis 向量存储） <a id="redis-vector-store"></a>

使用 Redis Vector Store 节点，将 Redis 数据库作为[向量存储](#user-content-fn-1)[^1]进行交互。可向向量数据库插入文档、从中获取文档、通过连接到链[^2]的检索器检索文档，或直接连接到智能体[^3]作为工具[^4]使用。

本页列出了 Redis Vector Store 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Redis 凭据文档](../../credentials/redis.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

{% hint style="info" %}
**功能可用性**

Redis 查询过滤器和 **Metadata Schema**（元数据架构）选项从 Redis Vector Store 节点版本 1.4 起可用。更早的节点版本，请参阅 [Metadata Filter（元数据过滤器）](#metadata-filter)。

现有 Redis Vector Store 节点会保留其节点版本，原有索引仍可使用。如需使用节点版本 1.4，请添加新的 Redis Vector Store 节点并使用新索引，然后重新导入文档。请勿将节点版本 1.4 的节点指向早期节点版本创建的索引，否则元数据会缺失，过滤器将返回错误结果。
{% endhint %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

使用此节点前，需要一个启用了 [Redis Query Engine](https://redis.io/docs/latest/develop/ai/search-and-query/?utm_source=n8n\&utm_medium=docs) 的 Redis 数据库。可使用以下任一选项：

* **Redis Open Source（v8.0 及更高版本）**：默认包含 Redis Query Engine
* [**Redis Cloud**](https://cloud.redis.io/?utm_source=n8n\&utm_medium=docs)：全托管服务
* [**Redis Software**](https://redis.io/software/?utm_source=n8n\&utm_medium=docs)：自行管理的部署

{% hint style="info" %}
**如果没有索引，将创建新索引。**

只有需要自定义索引架构或复用现有索引时，才需要提前创建索引。否则可跳过此步骤，让节点根据你指定的选项创建新索引。
{% endhint %}

## 节点使用模式 <a href="#node-usage-patterns" id="node-usage-patterns"></a>

可按以下方式使用 Redis Vector Store 节点：

### 作为普通节点插入和检索文档 <a href="#use-as-a-regular-node-to-insert-and-retrieve-documents" id="use-as-a-regular-node-to-insert-and-retrieve-documents"></a>

可将 Redis Vector Store 用作普通节点，插入或获取文档。此模式将 Redis Vector Store 放在常规连接流程中，无需使用智能体。

示例请参阅[此模板](https://n8n.io/workflows/10887-reduce-llm-costs-with-semantic-caching-using-redis-vector-store-and-huggingface/)，其中将语义缓存存储在 Redis 中，并在工作流开头使用 Redis Vector Store 节点检索。

### 作为工具直接连接到 AI 智能体 <a href="#connect-directly-to-an-ai-agent-as-a-tool" id="connect-directly-to-an-ai-agent-as-a-tool"></a>

可将 Redis Vector Store 节点直接连接到 [AI 智能体](n8n-nodes-langchain.agent/README.md)的工具[^4]连接器，让智能体在回答查询时将向量存储用作资源。

此时连接方式为：AI Agent（工具连接器）→ Redis Vector Store 节点。

### 使用检索器获取文档 <a href="#use-a-retriever-to-fetch-documents" id="use-a-retriever-to-fetch-documents"></a>

可将 [Vector Store Retriever](../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) 节点与 Redis Vector Store 节点配合使用，从 Redis Vector Store 节点获取文档。这通常与 [Question and Answer Chain](n8n-nodes-langchain.chainretrievalqa/README.md) 节点配合，从向量存储获取与给定聊天输入匹配的文档。

[连接流程示例](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)如下（链接示例使用 Pinecone，但模式相同）：Question and Answer Chain（Retriever 连接器）→ Vector Store Retriever（Vector Store 连接器）→ Redis Vector Store。

### 使用 Vector Store Question Answer Tool 回答问题 <a href="#use-the-vector-store-question-answer-tool-to-answer-questions" id="use-the-vector-store-question-answer-tool-to-answer-questions"></a>

另一种模式使用 [Vector Store Question Answer Tool](../sub-nodes/n8n-nodes-langchain.toolvectorstore.md)，汇总 Redis Vector Store 节点的结果并回答问题。此模式通过专门用于汇总向量存储数据的工具工作，无需将 Redis Vector Store 直接作为工具连接。

此[模板](https://n8n.io/workflows/10837-chat-with-github-issues-using-openai-and-redis-vector-search/)展示了如何将 Vector Store Question Answer Tool 与 Redis Vector Store 节点配合使用。此时的连接流程为：AI Agent（工具连接器）→ Vector Store Question Answer Tool（Vector Store 连接器）→ Redis Vector Store。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/vector-store-mode.md" %}

### Rerank Results（结果重排序） <a href="#rerank-results" id="rerank-results"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/vector-store-rerank-results.md" %}

### Get Many（获取多条）参数 <a href="#get-many-parameters" id="get-many-parameters"></a>

* **Redis Index**（Redis 索引）：输入要使用的 Redis 向量搜索索引名称，也可从列表中选择现有索引。
* **Prompt**（提示词）：输入搜索查询。
* **Limit**（上限）：输入从向量存储检索的结果数量。例如，设为 `10` 可获取最匹配的十条结果。

此操作模式包含 [Metadata Filter（元数据过滤器）](#metadata-filter)**节点选项**。从节点版本 1.4 起，还包含 [Metadata Schema（元数据架构）](#metadata-schema)**节点选项**。

### Insert Documents（插入文档）参数 <a href="#insert-documents-parameters" id="insert-documents-parameters"></a>

* **Redis Index**（Redis 索引）：输入要使用的 Redis 向量搜索索引名称，也可从列表中选择现有索引。

从节点版本 1.4 起，此操作模式包含 [Metadata Schema（元数据架构）](#metadata-schema)**节点选项**。

### Retrieve Documents（作为链或工具的向量存储）参数 <a href="#retrieve-documents-as-vector-store-for-chaintool-parameters" id="retrieve-documents-as-vector-store-for-chaintool-parameters"></a>

* **Redis Index**（Redis 索引）：输入要使用的 Redis 向量搜索索引名称，也可从列表中选择现有索引。

此操作模式包含 [Metadata Filter（元数据过滤器）](#metadata-filter)**节点选项**。从节点版本 1.4 起，还包含 [Metadata Schema（元数据架构）](#metadata-schema)**节点选项**。

### Retrieve Documents（作为 AI 智能体的工具）参数 <a href="#retrieve-documents-as-tool-for-ai-agent-parameters" id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

* **Name**（名称）：向量存储的名称。
* **Description**（描述）：向 LLM 说明此工具的用途。清晰、具体的描述有助于 LLM 更经常地生成预期结果。
* **Redis Index**（Redis 索引）：输入要使用的 Redis 向量搜索索引名称，也可从列表中选择现有索引。
* **Limit**（上限）：输入从向量存储检索的结果数量。例如，设为 `10` 可获取最匹配的十条结果。

此操作模式包含 [Metadata Filter（元数据过滤器）](#metadata-filter)**节点选项**。从节点版本 1.4 起，还包含 [Metadata Schema（元数据架构）](#metadata-schema)**节点选项**。

### Include Metadata（包含元数据） <a href="#include-metadata" id="include-metadata"></a>

是否包含文档元数据。

可与 [Get Many（获取多条）](n8n-nodes-langchain.vectorstoreredis.md#get-many-parameters)和 [Retrieve Documents（作为 AI 智能体的工具）](n8n-nodes-langchain.vectorstoreredis.md#retrieve-documents-as-tool-for-ai-agent-parameters)模式配合使用。

## 节点选项 <a href="#node-options" id="node-options"></a>

### Metadata Filter（元数据过滤器） <a href="#metadata-filter" id="metadata-filter"></a>

**Metadata Filter**（元数据过滤器）选项将结果限定为元数据匹配过滤器的文档，适用于 [Get Many（获取多条）](#get-many-parameters)、[Retrieve Documents（作为链或工具的向量存储）](#retrieve-documents-as-vector-store-for-chaintool-parameters)和 [Retrieve Documents（作为 AI 智能体的工具）](#retrieve-documents-as-tool-for-ai-agent-parameters)操作模式。过滤器语法取决于节点版本。

插入数据时，由文档加载器设置元数据。加载文档的更多信息，请参阅 [Default Data Loader](../sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md)。

#### 节点版本 1.4 中的 Redis 查询过滤器 <a id="redis-query-filters-in-node-version-14"></a>

从节点版本 1.4 起，**Metadata Filter**（元数据过滤器）接受 Redis 查询表达式。可对标签、数值、文本和地理位置字段进行过滤，并用 AND 和 OR 逻辑组合条件。过滤器仅对索引中以匹配类型存储的字段有效。字段类型设置方法，请参阅 [Metadata Schema（元数据架构）](#metadata-schema)。

| 过滤类型 | 示例 | 匹配文档的条件 |
|-------------|---------|-------------------------|
| 标签 | `@category:{electronics}` | `category` 为 `electronics` |
| 多个标签 | `@category:{electronics\|books}` | `category` 为 `electronics` 或 `books` |
| 数值范围 | `@price:[0 100]` | `price` 在 0 到 100 之间 |
| 组合 | `@category:{electronics} @price:[0 100]` | 两个条件都匹配 |
| 文本 | `@description:laptop` | `description` 包含单词 `laptop` |

完整语法，请参阅 [LangChain Redis Vector Store 高级功能文档](https://docs.langchain.com/oss/javascript/integrations/vectorstores/redis#advanced-features)和 [Redis Query Engine 文档](https://redis.io/docs/latest/develop/ai/search-and-query/query/)。

#### 节点版本 1.3 及更早版本中以逗号分隔的过滤器 <a id="comma-separated-filters-in-node-version-13-and-earlier"></a>

在节点版本 1.3 及更早版本中，**Metadata Filter**（元数据过滤器）接受以逗号分隔的词列表，例如 `Item1,Item2,Item3`。节点执行 `OR` 查询，只要至少一个词匹配，文档即匹配。

### Metadata Schema（元数据架构） <a id="metadata-schema"></a>

**Metadata Schema**（元数据架构）选项设置索引中各个元数据字段的类型。从节点版本 1.4 起，适用于 [Insert Documents（插入文档）](#insert-documents-parameters)、[Get Many（获取多条）](#get-many-parameters)、[Retrieve Documents（作为链或工具的向量存储）](#retrieve-documents-as-vector-store-for-chaintool-parameters)和 [Retrieve Documents（作为 AI 智能体的工具）](#retrieve-documents-as-tool-for-ai-agent-parameters)操作模式。

输入 JSON 数组，每个元数据字段对应一个对象。每个对象必须包含 `name` 和 `type`，还可包含 `options` 对象：

```json
[
	{"name": "category", "type": "tag"},
	{"name": "price", "type": "numeric", "options": {"sortable": true}},
	{"name": "description", "type": "text"},
	{"name": "location", "type": "geo"}
]
```

如果 JSON 无效、字段缺少名称或类型未知，节点将报错停止，索引保持不变。

| 类型 | 用途 | 过滤器示例 |
|------|------------|----------------|
| `tag` | 精确匹配类别、标签和状态值 | `@category:{electronics}` |
| `text` | 对描述和内容进行全文搜索 | `@description:laptop` |
| `numeric` | 价格、分数和日期范围（日期以 Unix 时间戳存储） | `@price:[0 100]` |
| `geo` | 地理位置，以 `"<longitude>,<latitude>"` 格式存储 | `@location:[-73.98 40.75 5 km]` |

| 选项 | 字段类型 | 描述 |
|--------|-------------|-------------|
| `sortable` | `numeric`、`text` | 允许 Redis 按该字段对结果排序。默认值：`false`。 |
| `separator` | `tag` | 同一个值中分隔多个标签的字符。默认值：`,`。 |
| `caseSensitive` | `tag` | 区分大小写匹配标签。默认值：`false`。 |
| `weight` | `text` | Redis 对文本匹配评分时，该字段的权重。默认值：`1.0`。 |
| `noStem` | `text` | 关闭词干提取，使 `laptops` 不匹配 `laptop`。默认值：`false`。 |
| `noindex` | 所有类型 | 存储字段但不为其建立索引，因此无法按此字段过滤。默认值：`false`。 |

如果将 **Metadata Schema**（元数据架构）留空，节点会根据插入的所有文档推断各字段的类型：

| 元数据值 | 推断类型 |
|-----------------|---------------|
| 数值或日期 | `numeric` |
| 数组 | `tag` |
| 格式为 `"<longitude>,<latitude>"` 的字符串 | `geo` |
| 其他字符串 | `text` |

普通字符串字段会成为 `text` 类型，因此 `@category:{electronics}` 等标签过滤器无法匹配。要对字符串字段使用标签过滤器，请在 **Metadata Schema**（元数据架构）中将该字段声明为 `tag`。

更多详情，请参阅 [LangChain Redis Vector Store 文档](https://docs.langchain.com/oss/javascript/integrations/vectorstores/redis#advanced-features)。

### Redis 配置选项 <a href="#redis-configuration-options" id="redis-configuration-options"></a>

适用于所有操作模式：

* **Metadata Key**（元数据键）：输入 Redis 哈希中元数据字段的键（默认值：`metadata`）。
* **Key Prefix**（键前缀）：输入存储文档使用的键前缀（默认值：`doc:`）。
* **Content Key**（内容键）：输入 Redis 哈希中内容字段的键（默认值：`content`）。
* **Embedding Key**（嵌入键）：输入 Redis 哈希中嵌入字段的键（默认值：`embedding`）。

### 插入选项 <a href="#insert-options" id="insert-options"></a>

适用于 [Insert Documents（插入文档）](n8n-nodes-langchain.vectorstoreredis.md#insert-documents-parameters)操作模式：

* **Overwrite Documents**（覆盖文档）：开启时覆盖现有文档，关闭时不覆盖。此操作还会删除索引。
* **Time-to-Live**（存活时间）：输入文档的存活时间，单位为秒。不会使索引过期。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Redis Vector Store（Redis 向量存储） 集成模板](https://n8n.io/integrations/redis-vector-store)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

请参阅：

* [Redis Vector Search 文档](https://redis.io/docs/latest/develop/ai/search-and-query/vectors/)，了解 Redis 向量功能的更多信息。
* [RediSearch 文档](https://redis.io/docs/latest/develop/ai/search-and-query/query/)，了解详细查询语法和过滤表达式。
* [LangChain Redis Vector Store 文档](https://docs.langchain.com/oss/javascript/integrations/vectorstores/redis)，了解该服务的更多信息，包括[高级过滤与自定义架构功能](https://docs.langchain.com/oss/javascript/integrations/vectorstores/redis#advanced-features)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/starter-kits/self-hosted-ai-starter-kit.md" %}

<a id="user-content-fn-1"></a>
[^1]: 向量存储或向量数据库用于存储信息的数学表示。将其与嵌入模型和检索器配合使用，可创建供 AI 在回答问题时访问的数据库。
[^2]: AI 链通过对组件的一系列调用，让你与大语言模型（LLM）及其他资源交互。n8n 中的 AI 链不使用持久记忆，因此不能通过它引用先前的上下文（此用途请使用 AI 智能体）。
[^3]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大语言模型（LLM）理解用户输入，利用可用的信息和资源，决定如何最好地处理请求。
[^4]: 在 AI 场景中，工具是附加资源，AI 可在响应请求时调用它获取特定信息或功能。AI 模型可以通过工具与外部系统交互，或完成具体、专门的任务。
