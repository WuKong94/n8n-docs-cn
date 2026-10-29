---
title: Oracle Database Vector Store（Oracle 数据库向量存储） 节点文档
description: 了解如何在 n8n 中使用 Oracle Database Vector Store（Oracle 数据库向量存储） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Oracle Database Vector Store（Oracle 数据库向量存储） 节点 <a id="oracle-database-vector-store-node"></a>

使用 Oracle Database Vector Store 节点，将 Oracle Database 作为向量存储[^1]进行交互。可向向量表插入文档、从中获取文档、检索文档并提供给连接到链[^2]的检索器，或作为工具[^4]直接连接到智能体[^3]。

本页列出了 Oracle Database Vector Store 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Oracle Database 凭据文档](../../credentials/oracledb.md)。
{% endhint %}

{% hint style="info" %}
**Oracle Database 向量支持**

Oracle Database 实例必须支持 Oracle AI Vector Search，才能执行向量存储操作。详情请参阅 [Oracle AI Vector Search 指南](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/26/arpls&id=VECSE-GUID-29B9E7E1-5A99-4D95-8614-58CA07D29957)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点使用模式 <a id="node-usage-patterns"></a>

可按以下方式使用 Oracle Database Vector Store 节点。

### 作为普通节点插入和检索文档 <a id="use-as-a-regular-node-to-insert-and-retrieve-documents"></a>

可将 Oracle Database Vector Store 用作普通节点，插入或获取文档。此模式将 Oracle Database Vector Store 放在常规连接流程中，无需使用智能体。

示例请参阅[此模板](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/)的场景 1（该模板使用 Supabase Vector Store，但模式相同）。

### 作为工具直接连接到 AI 智能体 <a id="connect-directly-to-an-ai-agent-as-a-tool"></a>

可将 Oracle Database Vector Store 节点直接连接到 [AI 智能体](n8n-nodes-langchain.agent/README.md)的工具连接器，让智能体在回答查询时使用向量存储作为资源。

此时连接方式为：AI Agent（工具连接器）→ Oracle Database Vector Store 节点。

### 使用检索器获取文档 <a id="use-a-retriever-to-fetch-documents"></a>

可将 [Vector Store Retriever](../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) 节点与 Oracle Database Vector Store 节点配合使用，从 Oracle Database Vector Store 节点获取文档。这通常与 [Question and Answer Chain](n8n-nodes-langchain.chainretrievalqa/README.md) 节点配合，从向量存储获取与给定聊天输入匹配的文档。

[连接流程示例](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)如下（链接示例使用 Pinecone，但模式相同）：Question and Answer Chain（Retriever 连接器）→ Vector Store Retriever（Vector Store 连接器）→ Oracle Database Vector Store。

### 使用 Vector Store Question Answer Tool 回答问题 <a id="use-the-vector-store-question-answer-tool-to-answer-questions"></a>

另一种模式使用 [Vector Store Question Answer Tool](../sub-nodes/n8n-nodes-langchain.toolvectorstore.md)，汇总 Oracle Database Vector Store 节点的结果并回答问题。此模式通过专门用于汇总向量存储数据的工具工作，无需将 Oracle Database Vector Store 直接作为工具连接。

此时的[连接流程](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)如下（链接示例使用 Simple Vector Store，但模式相同）：AI Agent（工具连接器）→ Vector Store Question Answer Tool（Vector Store 连接器）→ Oracle Database Vector Store。

## 节点参数 <a id="node-parameters"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/vector-store-mode.md" %}

### Rerank Results（结果重排序） <a id="rerank-results"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/vector-store-rerank-results.md" %}

<!-- vale off -->
### Get Many（获取多条）参数 <a id="get-many-parameters"></a>
<!-- vale on -->

* **Table Name**（表名称）：输入要查询的表名称。表不存在时，节点会创建该表。
* **Prompt**（提示词）：输入搜索查询。
* **Limit**（上限）：输入数字，设置从向量存储检索的结果数量。例如，设为 `10` 可获取最匹配的十条结果。

### Insert Documents（插入文档）参数 <a id="insert-documents-parameters"></a>

* **Table Name**（表名称）：输入用于存储向量的表名称。表不存在时，节点会创建该表。

### Retrieve Documents（作为链或工具的向量存储）参数 <a id="retrieve-documents-parameters-as-vector-store-for-chaintool"></a>

* **Table Name**（表名称）：输入要查询的表名称。

### Retrieve Documents（作为 AI 智能体的工具）参数 <a id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

* **Name**（名称）：向量存储的名称。
* **Description**（描述）：向 LLM 说明此工具的用途。清晰、具体的描述有助于 LLM 更经常地生成预期结果。
* **Table Name**（表名称）：输入要查询的 Oracle Database 向量表。
* **Limit**（上限）：输入从向量存储检索的结果数量。例如，设为 `10` 可获取最匹配的十条结果。

## 节点选项 <a id="node-options"></a>

### Distance Strategy（距离策略） <a id="distance-strategy"></a>

适用于 **Get Many**（获取多条）和 **Retrieve Documents**（检索文档）模式。此选项指定计算两个向量之间距离的方法，可选：

* **Cosine**（余弦）
* **Inner Product**（内积）
* **Euclidean**（欧几里得）
* **Manhattan**（曼哈顿）
* **Euclidean Squared**（欧几里得距离平方）
* **Hamming**（汉明）

### Metadata Filter（元数据过滤器） <a id="metadata-filter"></a>

适用于 **Get Many**（获取多条）、**Retrieve Documents (As Vector Store for Chain/Tool)**（检索文档，作为链或工具的向量存储）和 **Retrieve Documents (As Tool for AI Agent)**（检索文档，作为 AI 智能体的工具）模式。搜索数据时，可用此选项匹配文档关联的元数据。

在界面中指定多个元数据过滤字段时，所有字段都必须匹配，其行为类似 `AND` 查询。

对于高级过滤，Oracle Database Vector Store 会将元数据过滤器传递给 Oracle AI Vector Search。它支持更丰富的过滤对象，包括数组、嵌套过滤器、`$gte` 等比较运算符、`$nin` 等排除运算符和 `$and` 等逻辑运算符。

插入数据时，通过文档加载器设置元数据。加载文档的更多信息，请参阅 [Default Data Loader](../sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md)。

## 模板与示例 <a id="templates-and-examples"></a>

[浏览 Oracle Database Vector Store（Oracle 数据库向量存储） 集成模板](https://n8n.io/integrations/oracle-database-vector-store)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a id="related-resources"></a>

Oracle Database 向量搜索的更多信息，请参阅 [Oracle AI Vector Search 文档](https://docs.oracle.com/en/database/oracle/oracle-database/23/vecse/)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: 向量存储或向量数据库用于存储信息的数学表示。将其与嵌入模型和检索器配合使用，可创建供 AI 在回答问题时访问的数据库。
[^2]: AI 链通过对组件的一系列调用，让你与大语言模型（LLM）及其他资源交互。n8n 中的 AI 链不使用持久记忆，因此不能通过它引用先前的上下文（此用途请使用 AI 智能体）。
[^3]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大语言模型（LLM）理解用户输入，利用可用的信息和资源，决定如何最好地处理请求。
[^4]: 在 AI 场景中，工具是附加资源，AI 可在响应请求时调用它获取特定信息或功能。AI 模型可以通过工具与外部系统交互，或完成具体、专门的任务。
