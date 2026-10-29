---
title: Supabase Vector Store（Supabase 向量存储） 节点文档
contentType:
- integration
- reference
priority: medium
nodeTitle: Supabase Vector Store（Supabase 向量存储） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase
description: 了解如何在 n8n 中使用 Supabase Vector Store（Supabase 向量存储） 节点，并按照技术文档将其集成到工作流中。
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


# Supabase Vector Store（Supabase 向量存储） <a id="supabase-vector-store"></a>

使用 Supabase Vector Store，将 Supabase 数据库作为向量存储进行交互。可向向量数据库插入文档、从中获取多个文档，以及检索文档并提供给连接到链的检索器。

使用 Supabase Vector Store，将 Supabase 数据库作为[向量存储](#user-content-fn-1)[^1]进行交互。可向向量数据库插入文档、从中获取文档、检索文档并提供给连接到链[^2]的检索器，或直接连接到智能体[^3]作为工具[^4]使用。也可根据 ID 更新向量存储中的数据项。

本页列出了 Supabase 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Supabase 凭据文档](../../credentials/supabase.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

Supabase 提供了[设置向量存储的快速入门指南](https://supabase.com/docs/guides/ai/langchain?database-method=sql)。如果使用与快速入门默认值不同的设置，可能会影响 n8n 中的参数设置。请确保理解所做的配置。

## 节点使用模式 <a href="#node-usage-patterns" id="node-usage-patterns"></a>

可按以下方式使用 Supabase Vector Store 节点。

### 作为普通节点插入、更新和检索文档 <a href="#use-as-a-regular-node-to-insert-update-and-retrieve-documents" id="use-as-a-regular-node-to-insert-update-and-retrieve-documents"></a>

可将 Supabase Vector Store 用作普通节点，插入、更新或获取文档。此模式将 Supabase Vector Store 放在常规连接流程中，无需使用智能体。

示例请参阅[此模板](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/)的场景 1。

### 作为工具直接连接到 AI 智能体 <a href="#connect-directly-to-an-ai-agent-as-a-tool" id="connect-directly-to-an-ai-agent-as-a-tool"></a>

可将 Supabase Vector Store 节点直接连接到 [AI 智能体](n8n-nodes-langchain.agent/README.md)的工具连接器，让智能体在回答查询时使用向量存储作为资源。

此时连接方式为：AI Agent（工具连接器）→ Supabase Vector Store 节点。

### 使用检索器获取文档 <a href="#use-a-retriever-to-fetch-documents" id="use-a-retriever-to-fetch-documents"></a>

可将 [Vector Store Retriever](../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) 节点与 Supabase Vector Store 节点配合使用，从 Supabase Vector Store 节点获取文档。这通常与 [Question and Answer Chain](n8n-nodes-langchain.chainretrievalqa/README.md) 节点配合，从向量存储获取与给定聊天输入匹配的文档。

[连接流程示例](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)如下（示例使用 Pinecone，但模式相同）：Question and Answer Chain（Retriever 连接器）→ Vector Store Retriever（Vector Store 连接器）→ Supabase Vector Store。

### 使用 Vector Store Question Answer Tool 回答问题 <a href="#use-the-vector-store-question-answer-tool-to-answer-questions" id="use-the-vector-store-question-answer-tool-to-answer-questions"></a>

另一种模式使用 [Vector Store Question Answer Tool](../sub-nodes/n8n-nodes-langchain.toolvectorstore.md)，汇总 Supabase Vector Store 节点的结果并回答问题。此模式通过专门用于汇总向量存储数据的工具工作，无需将 Supabase Vector Store 直接作为工具连接。

此时的[连接流程](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/)为：AI Agent（工具连接器）→ Vector Store Question Answer Tool（Vector Store 连接器）→ Supabase Vector Store。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

### Operation Mode（操作模式） <a href="#operation-mode" id="operation-mode"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/vector-store-mode-with-update.md" %}

### Rerank Results（结果重排序） <a href="#rerank-results" id="rerank-results"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/vector-store-rerank-results.md" %}

### Get Many（获取多条）参数 <a href="#get-many-parameters" id="get-many-parameters"></a>

* **Table Name**（表名称）：输入要使用的 Supabase 表。
* **Prompt**（提示词）：输入搜索查询。
* **Limit**（上限）：输入从向量存储检索的结果数量。例如，设为 `10` 可获取最匹配的十条结果。

### Insert Documents（插入文档）参数 <a href="#insert-documents-parameters" id="insert-documents-parameters"></a>

* **Table Name**（表名称）：输入要使用的 Supabase 表。

### Retrieve Documents（作为链或工具的向量存储）参数 <a href="#retrieve-documents-as-vector-store-for-chaintool-parameters" id="retrieve-documents-as-vector-store-for-chaintool-parameters"></a>

* **Table Name**（表名称）：输入要使用的 Supabase 表。

### Retrieve Documents（作为 AI 智能体的工具）参数 <a href="#retrieve-documents-as-tool-for-ai-agent-parameters" id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

* **Name**（名称）：向量存储的名称。
* **Description**（描述）：向 LLM 说明此工具的用途。清晰、具体的描述有助于 LLM 更经常地生成预期结果。
* **Table Name**（表名称）：输入要使用的 Supabase 表。
* **Limit**（上限）：输入从向量存储检索的结果数量。例如，设为 `10` 可获取最匹配的十条结果。

### Update Documents（更新文档） <a href="#update-documents" id="update-documents"></a>

* **Table Name**（表名称）：输入要使用的 Supabase 表。
* **ID**：嵌入条目的 ID。

**Update Documents**（更新文档）参数

* ID

## 节点选项 <a href="#node-options" id="node-options"></a>

### Query Name（查询名称） <a href="#query-name" id="query-name"></a>

在 Supabase 中设置的匹配函数名称。如果按照 [Supabase 快速入门指南](https://supabase.com/docs/guides/ai/langchain?database-method=sql)配置，此值为 `match_documents`。

### Metadata Filter（元数据过滤器） <a href="#metadata-filter" id="metadata-filter"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/vector-store-metadata-filter.md" %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Supabase Vector Store（Supabase 向量存储） 集成模板](https://n8n.io/integrations/supabase-vector-store)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

<a id="user-content-fn-1"></a>
[^1]: 向量存储或向量数据库用于存储信息的数学表示。将其与嵌入模型和检索器配合使用，可创建供 AI 在回答问题时访问的数据库。
[^2]: AI 链通过对组件的一系列调用，让你与大语言模型（LLM）及其他资源交互。n8n 中的 AI 链不使用持久记忆，因此不能通过它引用先前的上下文（此用途请使用 AI 智能体）。
[^3]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大语言模型（LLM）理解用户输入，利用可用的信息和资源，决定如何最好地处理请求。
[^4]: 在 AI 场景中，工具是附加资源，AI 可在响应请求时调用它获取特定信息或功能。AI 模型可以通过工具与外部系统交互，或完成具体、专门的任务。
