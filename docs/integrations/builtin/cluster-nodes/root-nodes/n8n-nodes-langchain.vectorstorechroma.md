---
title: Chroma Vector Store（Chroma 向量存储） 节点文档
contentType:
- integration
- reference
priority: medium
nodeTitle: Chroma Vector Store（Chroma 向量存储） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorechroma.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorechroma
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorechroma
description: 了解如何在 n8n 中使用 Chroma Vector Store（Chroma 向量存储） 节点，并按照技术文档将其集成到工作流中。
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


# Chroma Vector Store（Chroma 向量存储） <a id="chroma-vector-store"></a>

使用 Chroma 节点，将 Chroma 数据库作为[向量存储](#user-content-fn-1)[^1]进行交互。可向向量数据库插入文档、从中获取文档、检索文档并提供给连接到链[^2]的检索器，或作为工具[^4]直接连接到智能体[^3]。

本页列出了 Chroma 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Chroma 凭据文档](../../credentials/chroma.md)。
{% endhint %}

## 节点使用模式 <a href="#node-usage-patterns" id="node-usage-patterns"></a>

可按以下方式使用 Chroma Vector Store 节点。

### 作为普通节点插入和检索文档 <a href="#use-as-a-regular-node-to-insert-and-retrieve-documents" id="use-as-a-regular-node-to-insert-and-retrieve-documents"></a>

可将 Chroma Vector Store 用作普通节点，插入或获取文档。此模式将 Chroma Vector Store 放在常规连接流程中，无需使用智能体。

### 作为工具直接连接到 AI 智能体 <a href="#connect-directly-to-an-ai-agent-as-a-tool" id="connect-directly-to-an-ai-agent-as-a-tool"></a>

可将 Chroma Vector Store 节点直接连接到 [AI 智能体](n8n-nodes-langchain.agent/README.md)的工具连接器，让智能体在回答查询时使用向量存储作为资源。

此时连接方式为：AI Agent（工具连接器）→ Chroma Vector Store 节点。

### 使用检索器获取文档 <a href="#use-a-retriever-to-fetch-documents" id="use-a-retriever-to-fetch-documents"></a>

可将 [Vector Store Retriever](../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) 节点与 Chroma Vector Store 节点配合使用，从 Chroma Vector Store 节点获取文档。这通常与 [Question and Answer Chain](n8n-nodes-langchain.chainretrievalqa/README.md) 节点配合，从向量存储获取与给定聊天输入匹配的文档。

连接流程示例如下：

Question and Answer Chain（Retriever 连接器）→ Vector Store Retriever（Vector Store 连接器）→ Chroma Vector Store。

### 使用 Vector Store Question Answer Tool 回答问题 <a href="#use-the-vector-store-question-answer-tool-to-answer-questions" id="use-the-vector-store-question-answer-tool-to-answer-questions"></a>

另一种模式使用 [Vector Store Question Answer Tool](../sub-nodes/n8n-nodes-langchain.toolvectorstore.md)，汇总 Chroma Vector Store 节点的结果并回答问题。此模式通过专门用于汇总向量存储数据的工具工作，无需将 Chroma Vector Store 直接作为工具连接。

此时的连接流程为：AI Agent（工具连接器）→ Vector Store Question Answer Tool（Vector Store 连接器）→ Chroma Vector Store。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

### Operation Mode（操作模式） <a href="#operation-mode" id="operation-mode"></a>

此向量存储节点有四种模式：**Get Many**（获取多条）、**Insert Documents**（插入文档）、**Retrieve Documents (As Vector Store for Chain/Tool)**（检索文档，作为链或工具的向量存储）和 **Retrieve Documents (As Tool for AI Agent)**（检索文档，作为 AI 智能体的工具）。所选模式决定节点可执行的操作，以及可用的输入和输出。

#### Get Many（获取多条） <a href="#get-many" id="get-many"></a>

此模式通过提供提示词，从向量数据库检索多个文档。提示词会转换为嵌入向量，用于相似度搜索。节点返回与提示词最相似的文档及其相似度分数，适合检索相似文档列表并作为额外上下文传给智能体。

#### Insert Documents（插入文档） <a href="#insert-documents" id="insert-documents"></a>

使用插入文档模式，将新文档插入向量数据库。

#### Retrieve Documents（作为链或工具的向量存储） <a href="#retrieve-documents-as-vector-store-for-chaintool" id="retrieve-documents-as-vector-store-for-chaintool"></a>

将 Retrieve Documents (As Vector Store for Chain/Tool)（检索文档，作为链或工具的向量存储）模式与向量存储检索器配合使用，从向量数据库检索文档，并将其提供给连接到链的检索器。在此模式下，必须将节点连接到检索器节点或根节点。

#### Retrieve Documents（作为 AI 智能体的工具） <a href="#retrieve-documents-as-tool-for-ai-agent" id="retrieve-documents-as-tool-for-ai-agent"></a>

使用 Retrieve Documents (As Tool for AI Agent)（检索文档，作为 AI 智能体的工具）模式，让智能体在回答查询时将向量存储用作工具资源。生成响应时，如果向量存储的名称和描述与问题详情匹配，智能体就会使用该向量存储。

### Rerank Results（结果重排序） <a href="#rerank-results" id="rerank-results"></a>

启用重排序[^5]。开启此选项后，必须为向量存储连接重排序节点，该节点将对查询结果重新排序。此选项可用于 `Get Many`、`Retrieve Documents (As Vector Store for Chain/Tool)` 和 `Retrieve Documents (As Tool for AI Agent)` 模式。

### Get Many（获取多条）参数 <a href="#get-many-parameters" id="get-many-parameters"></a>

* **Chroma collection name**（Chroma 集合名称）：从获取到的集合列表中选择集合。
* **Prompt**（提示词）：输入搜索查询。
* **Limit**（上限）：输入从向量存储检索的结果数量。例如，设为 `5` 可获取最匹配的五条结果。

此操作模式包含一个**节点选项**：Metadata Filter（元数据过滤器）。

### Insert Documents（插入文档）参数 <a href="#insert-documents-parameters" id="insert-documents-parameters"></a>

* **Chroma collection name**（Chroma 集合名称）：从获取到的集合列表中选择集合。

### Retrieve Documents（作为链或工具的向量存储）参数 <a href="#retrieve-documents-as-vector-store-for-chaintool-parameters" id="retrieve-documents-as-vector-store-for-chaintool-parameters"></a>

* **Chroma collection name**（Chroma 集合名称）：从获取到的集合列表中选择集合。

此操作模式包含一个**节点选项**：Metadata Filter（元数据过滤器）。

### Retrieve Documents（作为 AI 智能体的工具）参数 <a href="#retrieve-documents-as-tool-for-ai-agent-parameters" id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

* **Description**（描述）：向 LLM 说明此工具的用途。清晰、具体的描述有助于 LLM 更经常地生成预期结果。
* **Chroma collection name**（Chroma 集合名称）：从获取到的集合列表中选择集合。
* **Limit**（上限）：输入从向量存储检索的结果数量。例如，设为 `5` 可获取最匹配的五条结果。

## 节点选项 <a href="#node-options" id="node-options"></a>

### Metadata Filter（元数据过滤器） <a href="#metadata-filter" id="metadata-filter"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/vector-store-metadata-filter.md" %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

查看 n8n 的[高级 AI](../../../../build/integrate-ai/README.md) 文档。

<a id="user-content-fn-1"></a>
[^1]: 向量存储或向量数据库用于存储信息的数学表示。将其与嵌入模型和检索器配合使用，可创建供 AI 在回答问题时访问的数据库。
[^2]: AI 链通过对组件的一系列调用，让你与大语言模型（LLM）及其他资源交互。n8n 中的 AI 链不使用持久记忆，因此不能通过它引用先前的上下文（此用途请使用 AI 智能体）。
[^3]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大语言模型（LLM）理解用户输入，利用可用的信息和资源，决定如何最好地处理请求。
[^4]: 在 AI 场景中，工具是附加资源，AI 可在响应请求时调用它获取特定信息或功能。AI 模型可以通过工具与外部系统交互，或完成具体、专门的任务。
[^5]: 重排序是一种优化候选文档列表顺序的技术，用于提高搜索结果的相关性。检索增强生成（RAG）等应用使用重排序，优先选出最相关的信息，供生成或下游任务使用。
