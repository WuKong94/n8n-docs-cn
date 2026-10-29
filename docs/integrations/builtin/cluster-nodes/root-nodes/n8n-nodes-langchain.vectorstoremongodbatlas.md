---
title: MongoDB Atlas Vector Store（MongoDB Atlas 向量存储） 节点文档
contentType:
- integration
- reference
priority: medium
nodeTitle: MongoDB Atlas Vector Store（MongoDB Atlas 向量存储） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas
description: 了解如何在 n8n 中使用 MongoDB Atlas Vector Store（MongoDB Atlas 向量存储） 节点，并按照技术文档将其集成到工作流中。
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


# MongoDB Atlas Vector Store（MongoDB Atlas 向量存储） <a id="mongodb-atlas-vector-store"></a>

MongoDB Atlas Vector Search 是 MongoDB Atlas 的一项功能，可存储和查询嵌入向量。使用此节点，与 MongoDB Atlas 集合中的 Vector Search 索引交互。可插入和检索文档，在链中使用向量存储，或将其用作智能体的工具。

本页列出了 MongoDB Atlas Vector Store 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [MongoDB 凭据文档](../../credentials/mongodb.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

使用此节点前，请先在 MongoDB Atlas 集合中创建 [Vector Search 索引](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-type/)。创建步骤如下：

1. 登录 [MongoDB Atlas 控制台](https://cloud.mongodb.com/)。
2. 选择组织和项目。
3. 找到“Search & Vector Search”（搜索与向量搜索）部分。
4. 选择集群，点击“Go to search”（前往搜索）。
5. 点击“Create Search Index”（创建搜索索引）。
6. 选择“Vector Search”（向量搜索）模式，使用可视化编辑器或 JSON 编辑器。例如：

    ```json
    {
      "fields": [
        {
          "type": "vector",
          "path": "<field-name>",
          "numDimensions": 1536, // any other value
          "similarity": "<similarity-function>"
        }
      ]
    }
    ```
7. 根据嵌入模型调整“dimensions”（维度）值（例如，`1536` 适用于 OpenAI 的 `text-embedding-small-3`）。
8. 为索引命名并创建。

请记下以下值，配置节点时需要使用：

* 集合名称
* 向量索引名称
* 嵌入和元数据的字段名称

## 节点使用模式 <a href="#node-usage-patterns" id="node-usage-patterns"></a>

可按以下方式使用 MongoDB Atlas Vector Store 节点：

### 作为普通节点插入和检索文档 <a href="#use-as-a-regular-node-to-insert-and-retrieve-documents" id="use-as-a-regular-node-to-insert-and-retrieve-documents"></a>

可将 MongoDB Atlas Vector Store 用作普通节点，插入或获取文档。此模式将 MongoDB Atlas Vector Store 放在常规连接流程中，无需使用智能体。

示例请参阅[此模板](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/)的场景 1（该模板使用 Supabase Vector Store，但模式相同）。

### 作为工具直接连接到 AI 智能体 <a href="#connect-directly-to-an-ai-agent-as-a-tool" id="connect-directly-to-an-ai-agent-as-a-tool"></a>

可将 MongoDB Atlas Vector Store 节点直接连接到 [AI 智能体](n8n-nodes-langchain.agent/README.md)的工具连接器，让智能体在回答查询时将向量存储用作资源。

此时连接方式为：AI Agent（工具连接器）→ MongoDB Atlas Vector Store 节点。

### 使用检索器获取文档 <a href="#use-a-retriever-to-fetch-documents" id="use-a-retriever-to-fetch-documents"></a>

可将 [Vector Store Retriever](../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) 节点与 MongoDB Atlas Vector Store 节点配合使用，从 MongoDB Atlas Vector Store 节点获取文档。这通常与 [Question and Answer Chain](n8n-nodes-langchain.chainretrievalqa/README.md) 节点配合，从向量存储获取与给定聊天输入匹配的文档。

[连接流程示例](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)如下（链接示例使用 Pinecone，但模式相同）：Question and Answer Chain（Retriever 连接器）→ Vector Store Retriever（Vector Store 连接器）→ MongoDB Atlas Vector Store。

### 使用 Vector Store Question Answer Tool 回答问题 <a href="#use-the-vector-store-question-answer-tool-to-answer-questions" id="use-the-vector-store-question-answer-tool-to-answer-questions"></a>

另一种模式使用 [Vector Store Question Answer Tool](../sub-nodes/n8n-nodes-langchain.toolvectorstore.md)，汇总 MongoDB Atlas Vector Store 节点的结果并回答问题。此模式通过专门用于汇总向量存储数据的工具工作，无需将 MongoDB Atlas Vector Store 直接作为工具连接。

此时的[连接流程](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)如下（链接示例使用 In-Memory Vector Store，但模式相同）：AI Agent（工具连接器）→ Vector Store Question Answer Tool（Vector Store 连接器）→ In-Memory Vector Store。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/vector-store-mode.md" %}

### Rerank Results（结果重排序） <a href="#rerank-results" id="rerank-results"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/vector-store-rerank-results.md" %}

### Get Many（获取多条）参数 <a href="#get-many-parameters" id="get-many-parameters"></a>

* **Mongo Collection**（Mongo 集合）：输入要使用的 MongoDB 集合名称。
* **Vector Index Name**（向量索引名称）：输入 MongoDB Atlas 集合中 Vector Search 索引的名称。
* **Embedding Field**（嵌入字段）：输入文档中包含嵌入向量的字段名称。
* **Metadata Field**（元数据字段）：输入文档中包含文本元数据的字段名称。

### Insert Documents（插入文档）参数 <a href="#insert-documents-parameters" id="insert-documents-parameters"></a>

* **Mongo Collection**（Mongo 集合）：输入要使用的 MongoDB 集合名称。
* **Vector Index Name**（向量索引名称）：输入 MongoDB Atlas 集合中 Vector Search 索引的名称。
* **Embedding Field**（嵌入字段）：输入文档中包含嵌入向量的字段名称。
* **Metadata Field**（元数据字段）：输入文档中包含文本元数据的字段名称。

### Retrieve Documents（作为链或工具的向量存储）参数 <a href="#retrieve-documents-parameters-as-vector-store-for-chaintool" id="retrieve-documents-parameters-as-vector-store-for-chaintool"></a>

* **Mongo Collection**（Mongo 集合）：输入要使用的 MongoDB 集合名称。
* **Vector Index Name**（向量索引名称）：输入 MongoDB Atlas 集合中 Vector Search 索引的名称。
* **Embedding Field**（嵌入字段）：输入文档中包含嵌入向量的字段名称。
* **Metadata Field**（元数据字段）：输入文档中包含文本元数据的字段名称。

### Retrieve Documents（作为 AI 智能体的工具）参数 <a href="#retrieve-documents-as-tool-for-ai-agent-parameters" id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

* **Name**（名称）：向量存储的名称。
* **Description**（描述）：向 LLM 说明此工具的用途。清晰、具体的描述有助于 LLM 更经常地生成预期结果。
* **Mongo Collection**（Mongo 集合）：输入要使用的 MongoDB 集合名称。
* **Vector Index Name**（向量索引名称）：输入 MongoDB Atlas 集合中 Vector Search 索引的名称。
* **Limit**（上限）：输入从向量存储检索的结果数量。例如，设为 `10` 可获取最匹配的十条结果。

## 节点选项 <a href="#node-options" id="node-options"></a>

### Options（选项） <a href="#options" id="options"></a>

* **Metadata Filter**（元数据过滤器）：根据元数据过滤结果。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 MongoDB Atlas Vector Store（MongoDB Atlas 向量存储） 集成模板](https://n8n.io/integrations/mongodb-atlas-vector-store)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

请参阅：

* [LangChain MongoDB Atlas Vector Search 文档](https://docs.langchain.com/oss/javascript/integrations/vectorstores/mongodb_atlas)，了解该服务的更多信息。
* [MongoDB Atlas Vector Search 文档](https://www.mongodb.com/docs/atlas/atlas-vector-search/)，了解 MongoDB Atlas Vector Search 的更多信息。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/starter-kits/self-hosted-ai-starter-kit.md" %}
