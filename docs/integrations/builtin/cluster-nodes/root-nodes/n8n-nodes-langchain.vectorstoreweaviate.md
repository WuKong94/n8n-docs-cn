---
title: Weaviate Vector Store（Weaviate 向量存储） 节点文档
contentType:
- integration
- reference
priority: medium
nodeTitle: Weaviate Vector Store（Weaviate 向量存储） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate
description: 了解如何在 n8n 中使用 Weaviate Vector Store（Weaviate 向量存储） 节点，并按照技术文档将其集成到工作流中。
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


# Weaviate Vector Store（Weaviate 向量存储） <a id="weaviate-vector-store"></a>

使用 Weaviate 节点，将 Weaviate 集合作为[向量存储](#user-content-fn-1)[^1]进行交互。可向向量数据库插入文档或从中检索文档，也可检索文档并提供给连接到链[^2]的检索器，或将此节点直接连接到智能体[^3]作为工具[^4]使用。本页列出了 Weaviate 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Weaviate 凭据文档](../../credentials/weaviate.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点使用模式 <a href="#node-usage-patterns" id="node-usage-patterns"></a>

可按以下方式使用 Weaviate Vector Store 节点。

### 作为普通节点插入和检索文档 <a href="#use-as-a-regular-node-to-insert-and-retrieve-documents" id="use-as-a-regular-node-to-insert-and-retrieve-documents"></a>

可将 Weaviate Vector Store 用作普通节点，插入或获取文档。此模式将 Weaviate Vector Store 放在常规连接流程中，无需使用智能体。

### 作为工具直接连接到 AI 智能体 <a href="#connect-directly-to-an-ai-agent-as-a-tool" id="connect-directly-to-an-ai-agent-as-a-tool"></a>

可将 Weaviate Vector Store 节点直接连接到 [AI 智能体](n8n-nodes-langchain.agent/README.md)的工具连接器，让智能体在回答查询时使用向量存储作为资源。

此时连接方式为：AI Agent（工具连接器）→ Weaviate Vector Store 节点。

### 使用检索器获取文档 <a href="#use-a-retriever-to-fetch-documents" id="use-a-retriever-to-fetch-documents"></a>

可将 [Vector Store Retriever](../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) 节点与 Weaviate Vector Store 节点配合使用，从 Weaviate Vector Store 节点获取文档。这通常与 [Question and Answer Chain](n8n-nodes-langchain.chainretrievalqa/README.md) 节点配合，从向量存储获取与给定聊天输入匹配的文档。

### 使用 Vector Store Question Answer Tool 回答问题 <a href="#use-the-vector-store-question-answer-tool-to-answer-questions" id="use-the-vector-store-question-answer-tool-to-answer-questions"></a>

另一种模式使用 [Vector Store Question Answer Tool](../sub-nodes/n8n-nodes-langchain.toolvectorstore.md)，汇总 Weaviate Vector Store 节点的结果并回答问题。此模式通过专门用于汇总向量存储数据的工具工作，无需将 Weaviate Vector Store 直接作为工具连接。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

{% hint style="info" %}
**多租户**

可将同一集合中的数据划分到相互隔离的租户中（例如供不同客户使用）。为此，插入和检索对象时都必须始终提供 [Tenant Name（租户名称）](n8n-nodes-langchain.vectorstoreweaviate.md#tenant-name)。[在 Weaviate 文档中了解多租户的更多信息](https://docs.weaviate.io/weaviate/manage-collections/multi-tenancy)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/vector-store-mode.md" %}

### Get Many（获取多条）参数 <a href="#get-many-parameters" id="get-many-parameters"></a>

* **Weaviate Collection**（Weaviate 集合）：输入要使用的 Weaviate 集合名称。
* **Prompt**（提示词）：输入搜索查询。
* **Limit**（上限）：输入从向量存储检索的结果数量。例如，设为 `10` 可获取最匹配的十条结果。

### Insert Documents（插入文档）参数 <a href="#insert-documents-parameters" id="insert-documents-parameters"></a>

* **Weaviate Collection**（Weaviate 集合）：输入要使用的 Weaviate 集合名称。
* **Embedding Batch Size**（嵌入批次大小）：单个批次中生成嵌入的文档数量，默认为 200 个文档。

### Retrieve Documents（作为链或工具的向量存储）参数 <a href="#retrieve-documents-as-vector-store-for-chaintool-parameters" id="retrieve-documents-as-vector-store-for-chaintool-parameters"></a>

* **Weaviate Collection**（Weaviate 集合）：输入要使用的 Weaviate 集合名称。

### Retrieve Documents（作为 AI 智能体的工具）参数 <a href="#retrieve-documents-as-tool-for-ai-agent-parameters" id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

* **Weaviate Collection**（Weaviate 集合）：向量存储的名称。
* **Description**（描述）：向 LLM 说明此工具的用途。清晰、具体的描述有助于 LLM 更经常地生成预期结果。
* **Weaviate Collection**（Weaviate 集合）：输入要使用的 Weaviate 集合名称。
* **Limit**（上限）：输入从向量存储检索的结果数量。例如，设为 `10` 可获取最匹配的十条结果。

### Include Metadata（包含元数据） <a href="#include-metadata" id="include-metadata"></a>

是否包含文档元数据。

可与 [Get Many（获取多条）](n8n-nodes-langchain.vectorstoreweaviate.md#get-many-parameters)和 [Retrieve Documents（作为 AI 智能体的工具）](n8n-nodes-langchain.vectorstoreweaviate.md#retrieve-documents-as-tool-for-ai-agent-parameters)模式配合使用。

### Rerank Results（结果重排序） <a href="#rerank-results" id="rerank-results"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/vector-store-rerank-results.md" %}

## 节点选项 <a href="#node-options" id="node-options"></a>

### Search Filters（搜索过滤器） <a href="#search-filters" id="search-filters"></a>

适用于 [Get Many（获取多条）](n8n-nodes-langchain.vectorstoreweaviate.md#get-many-parameters)、[Retrieve Documents（作为链或工具的向量存储）](n8n-nodes-langchain.vectorstoreweaviate.md#retrieve-documents-as-vector-store-for-chaintool-parameters)和 [Retrieve Documents（作为 AI 智能体的工具）](n8n-nodes-langchain.vectorstoreweaviate.md#retrieve-documents-as-tool-for-ai-agent-parameters)操作模式。

搜索数据时，用于匹配文档关联的元数据。运算符和查询结构的更多信息，请参阅 [Weaviate 条件过滤器文档](https://docs.weaviate.io/weaviate/api/graphql/filters)。

可使用 `AND` 和 `OR` 搭配不同运算符。运算符不区分大小写：

```json
{
  "OR": [
    {
        "path": ["source"],
        "operator": "Equal",
        "valueString": "source1"
    },
    {
        "path": ["source"],
        "operator": "Equal",
        "valueString": "source1"
    }
  ]
}
```

支持的运算符：

| 运算符 | 必需字段 | 描述 |
| ------------------ | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `'equal'` | `valueString` 或 `valueNumber` | 检查属性是否等于给定字符串或数字。 |
| `'like'` | `valueString` | 检查字符串属性是否匹配模式（例如子字符串匹配）。 |
| `'containsAny'` | `valueTextArray`（字符串数组） | 检查属性是否包含给定值中的**任意一个**。 |
| `'containsAll'` | `valueTextArray`（字符串数组） | 检查属性是否包含给定的**全部**值。 |
| `'greaterThan'` | `valueNumber` | 检查属性值是否大于给定数字。 |
| `'lessThan'` | `valueNumber` | 检查属性值是否小于给定数字。 |
| `'isNull'` | `valueBoolean`（true/false） | 检查属性是否为 null。（[必须在导入数据前启用](https://docs.weaviate.io/weaviate/manage-collections/collection-operations#set-inverted-index-parameters)） |
| `'withinGeoRange'` | `valueGeoCoordinates`（包含地理位置数据的对象） | 按与地理坐标的距离进行过滤。 |

插入数据时，由文档加载器设置元数据。加载文档的更多信息，请参阅 [Default Data Loader](../sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md)。

### Metadata Keys（元数据键） <a href="#metadata-keys" id="metadata-keys"></a>

可定义希望 Weaviate 在查询时返回哪些元数据键。这样只获取已指定的属性，可减少网络负载。默认返回服务器中的所有属性。

适用于 [Get Many（获取多条）](n8n-nodes-langchain.vectorstoreweaviate.md#get-many-parameters)、[Retrieve Documents（作为链或工具的向量存储）](n8n-nodes-langchain.vectorstoreweaviate.md#retrieve-documents-as-vector-store-for-chaintool-parameters)和 [Retrieve Documents（作为 AI 智能体的工具）](n8n-nodes-langchain.vectorstoreweaviate.md#retrieve-documents-as-tool-for-ai-agent-parameters)操作模式。

### Hybrid: Query Text（混合搜索：查询文本） <a href="#hybrid-query-text" id="hybrid-query-text"></a>

提供查询文本，将向量搜索与关键词或文本搜索结合。

### Hybrid: Explain Score（混合搜索：解释分数） <a href="#hybrid-explain-score" id="hybrid-explain-score"></a>

是否显示混合搜索融合分数及向量搜索解释。

### Hybrid: Fusion Type（混合搜索：融合类型） <a href="#hybrid-fusion-type" id="hybrid-fusion-type"></a>

选择合并向量搜索和关键词搜索结果的融合类型。[了解融合算法的更多信息](https://weaviate.io/learn/knowledgecards/fusion-algorithm)。

选项：

* **Relative Score**（相对分数）：使用相对分数融合
* **Ranked**（排名）：使用排名融合

### Hybrid: Auto Cut Limit（混合搜索：自动截断上限） <a href="#hybrid-auto-cut-limit" id="hybrid-auto-cut-limit"></a>

通过检测分数的突然跳变，限制结果组。[了解 autocut 的更多信息](https://docs.weaviate.io/weaviate/api/graphql/additional-operators#autocut)。

### Hybrid: Alpha（混合搜索：Alpha） <a href="#hybrid-alpha" id="hybrid-alpha"></a>

调整关键词和向量部分的相对权重。1.0 = 纯向量，0.0 = 纯关键词，默认值为 0.5。[了解 alpha 参数的更多信息](https://weaviate.io/learn/knowledgecards/alpha-parameter)。

### Hybrid: Query Properties（混合搜索：查询属性） <a href="#hybrid-query-properties" id="hybrid-query-properties"></a>

以逗号分隔的查询属性列表，可选择为属性值设置权重，例如“question^2,answer”。[了解属性值权重设置的更多信息](https://docs.weaviate.io/weaviate/search/hybrid#set-weights-on-property-values)。

### Hybrid: Max Vector Distance（混合搜索：最大向量距离） <a href="#hybrid-max-vector-distance" id="hybrid-max-vector-distance"></a>

设置向量搜索部分允许的最大距离。

### Tenant Name（租户名称） <a href="#tenant-name" id="tenant-name"></a>

要为其存储或检索文档的具体租户。[了解多租户的更多信息](https://weaviate.io/learn/knowledgecards/multi-tenancy)。

{% hint style="info" %}
**必须在创建时启用**

首次导入数据时必须传入租户名称，才能为集合启用多租户。创建后无法启用或禁用多租户。
{% endhint %}

### Text Key（文本键） <a href="#text-key" id="text-key"></a>

文档中包含用于生成嵌入的文本的键。

### Skip Init Checks（跳过初始化检查） <a href="#skip-init-checks" id="skip-init-checks"></a>

实例化客户端时，是否[跳过初始化检查](https://docs.weaviate.io/weaviate/client-libraries/typescript/notes-best-practices#initial-connection-checks)。

### Init Timeout（初始化超时） <a href="#init-timeout" id="init-timeout"></a>

初始检查中[超时](https://docs.weaviate.io/weaviate/client-libraries/typescript/notes-best-practices#timeout-values)前等待的秒数。

### Insert Timeout（插入超时） <a href="#insert-timeout" id="insert-timeout"></a>

插入时[超时](https://docs.weaviate.io/weaviate/client-libraries/typescript/notes-best-practices#timeout-values)前等待的秒数。

### Query Timeout（查询超时） <a href="#query-timeout" id="query-timeout"></a>

查询时[超时](https://docs.weaviate.io/weaviate/client-libraries/typescript/notes-best-practices#timeout-values)前等待的秒数。

### GRPC Proxy（gRPC 代理） <a href="#grpc-proxy" id="grpc-proxy"></a>

用于 gRPC 请求的代理。

### Clear Data（清空数据） <a href="#clear-data" id="clear-data"></a>

适用于 [Insert Documents（插入文档）](n8n-nodes-langchain.vectorstoreweaviate.md#insert-documents-parameters)操作模式。

是否在插入新数据之前清空集合或租户。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Weaviate Vector Store（Weaviate 向量存储） 集成模板](https://n8n.io/integrations/weaviate-vector-store)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain Weaviate 文档](https://docs.langchain.com/oss/javascript/integrations/vectorstores/weaviate)。

关于自托管 Weaviate 集群，请参阅 [Weaviate 安装](https://docs.weaviate.io/deploy)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

<a id="user-content-fn-1"></a>
[^1]: 向量存储或向量数据库用于存储信息的数学表示。将其与嵌入模型和检索器配合使用，可创建供 AI 在回答问题时访问的数据库。
[^2]: AI 链通过对组件的一系列调用，让你与大语言模型（LLM）及其他资源交互。n8n 中的 AI 链不使用持久记忆，因此不能通过它引用先前的上下文（此用途请使用 AI 智能体）。
[^3]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大语言模型（LLM）理解用户输入，利用可用的信息和资源，决定如何最好地处理请求。
[^4]: 在 AI 场景中，工具是附加资源，AI 可在响应请求时调用它获取特定信息或功能。AI 模型可以通过工具与外部系统交互，或完成具体、专门的任务。
