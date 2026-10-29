---
title: Simple Vector Store（简单向量存储） 节点文档
contentType:
- integration
- reference
priority: medium
nodeTitle: Simple Vector Store（简单向量存储） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory
description: 了解如何在 n8n 中使用 Simple Vector Store（简单向量存储） 节点，并按照技术文档将其集成到工作流中。
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


# Simple Vector Store（简单向量存储） <a id="simple-vector-store"></a>

使用 Simple Vector Store 节点，在 n8n 应用内存中存储和检索嵌入向量[^1]。

本页列出了 Simple Vector Store 节点的参数，并提供更多资源的链接。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

{% hint style="info" %}
**此节点与 AI 记忆节点不同**

此处描述的简单向量存储与 [Simple Memory](../sub-nodes/n8n-nodes-langchain.memorybufferwindow/README.md) 等 AI 记忆节点不同。

此节点在应用内存中创建[向量数据库](#user-content-fn-2)[^2]。
{% endhint %}

## 数据安全限制 <a href="#data-safety-limitations" id="data-safety-limitations"></a>

使用 Simple Vector Store 节点前，需要了解其限制及工作方式。

{% hint style="warning" %}
n8n 建议仅在开发时使用 Simple Vector Store。
{% endhint %}

### 向量存储数据不会持久保存 <a href="#vector-store-data-isnt-persistent" id="vector-store-data-isnt-persistent"></a>

此节点仅将数据存储在内存中。n8n 重启时所有数据都会丢失，内存不足时数据也可能被清除。

### 所有实例用户都能访问向量存储数据 <a href="#all-instance-users-can-access-vector-store-data" id="all-instance-users-can-access-vector-store-data"></a>

Simple Vector Store 节点的记忆键是全局的，不限定于单个工作流。

这意味着，无论原工作流设置了何种访问控制，实例的所有用户都可通过添加 Simple Vector Store 节点并选择记忆键，访问向量存储数据。使用 Simple Vector Store 节点导入数据时，请注意避免暴露敏感信息。

## 节点使用模式 <a href="#node-usage-patterns" id="node-usage-patterns"></a>

可按以下方式使用 Simple Vector Store 节点。

### 作为普通节点插入和检索文档 <a href="#use-as-a-regular-node-to-insert-and-retrieve-documents" id="use-as-a-regular-node-to-insert-and-retrieve-documents"></a>

可将 Simple Vector Store 用作普通节点，插入或获取文档。此模式将 Simple Vector Store 放在常规连接流程中，无需使用智能体。

示例请参阅[此模板](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)的步骤 2。

### 作为工具直接连接到 AI 智能体 <a href="#connect-directly-to-an-ai-agent-as-a-tool" id="connect-directly-to-an-ai-agent-as-a-tool"></a>

可将 Simple Vector Store 节点直接连接到 [AI 智能体](n8n-nodes-langchain.agent/README.md)的工具[^3]连接器，让智能体在回答查询时将向量存储用作资源。

此时连接方式为：AI Agent（工具连接器）→ Simple Vector Store 节点。

### 使用检索器获取文档 <a href="#use-a-retriever-to-fetch-documents" id="use-a-retriever-to-fetch-documents"></a>

可将 [Vector Store Retriever](../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) 节点与 Simple Vector Store 节点配合使用，从 Simple Vector Store 节点获取文档。这通常与 [Question and Answer Chain](n8n-nodes-langchain.chainretrievalqa/README.md) 节点配合，从向量存储获取与给定聊天输入匹配的文档。

[连接流程示例](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)如下（链接示例使用 Pinecone，但模式相同）：Question and Answer Chain（Retriever 连接器）→ Vector Store Retriever（Vector Store 连接器）→ Simple Vector Store。

### 使用 Vector Store Question Answer Tool 回答问题 <a href="#use-the-vector-store-question-answer-tool-to-answer-questions" id="use-the-vector-store-question-answer-tool-to-answer-questions"></a>

另一种模式使用 [Vector Store Question Answer Tool](../sub-nodes/n8n-nodes-langchain.toolvectorstore.md)，汇总 Simple Vector Store 节点的结果并回答问题。此模式通过专门用于汇总向量存储数据的工具工作，无需将 Simple Vector Store 直接作为工具连接。

此时的[连接流程](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)为：AI Agent（工具连接器）→ Vector Store Question Answer Tool（Vector Store 连接器）→ Simple Vector Store。

## 内存管理 <a href="#memory-management" id="memory-management"></a>

Simple Vector Store 通过以下内存管理措施，防止内存使用过多：

* 内存压力增加时，自动清理旧的向量存储
* 移除在可配置的时长内未被访问的非活跃存储

### 配置选项 <a href="#configuration-options" id="configuration-options"></a>

可通过以下环境变量控制内存用量：

| 变量 | 类型 | 默认值 | 描述 |
| ----------------------------- | ------ | ------- | ----------------------------------------------------------------------------------- |
| `N8N_VECTOR_STORE_MAX_MEMORY` | 数值 | -1 | 所有向量存储合计可使用的最大内存，单位为 MB（-1 表示禁用限制）。 |
| `N8N_VECTOR_STORE_TTL_HOURS` | 数值 | -1 | 存储未被访问达到多少小时后将被移除（-1 表示禁用 TTL）。 |

在 n8n Cloud 中，这两个值分别预设为 100MB（约 8,000 个文档，取决于文档大小和元数据）及 7 天。自托管实例中，两者默认均为 -1（不限制内存，也不按时间清理）。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/vector-store-mode.md" %}

### Rerank Results（结果重排序） <a href="#rerank-results" id="rerank-results"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/vector-store-rerank-results.md" %}

### Get Many（获取多条）参数 <a href="#get-many-parameters" id="get-many-parameters"></a>

* **Memory Key**（记忆键）：选择或创建包含要查询的向量记忆的键。
* **Prompt**（提示词）：输入搜索查询。
* **Limit**（上限）：输入从向量存储检索的结果数量。例如，设为 `10` 可获取最匹配的十条结果。

### Insert Documents（插入文档）参数 <a href="#insert-documents-parameters" id="insert-documents-parameters"></a>

* **Memory Key**（记忆键）：选择或创建用于存储向量记忆的键。
* **Clear Store**（清空存储）：开启时，在插入数据之前，清除此工作流给定记忆键对应的向量存储。

### Retrieve Documents（作为链或工具的向量存储）参数 <a href="#retrieve-documents-as-vector-store-for-chaintool-parameters" id="retrieve-documents-as-vector-store-for-chaintool-parameters"></a>

* **Memory Key**（记忆键）：选择或创建包含要查询的向量记忆的键。

### Retrieve Documents（作为 AI 智能体的工具）参数 <a href="#retrieve-documents-as-tool-for-ai-agent-parameters" id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

* **Name**（名称）：向量存储的名称。
* **Description**（描述）：向 LLM 说明此工具的用途。清晰、具体的描述有助于 LLM 更经常地生成预期结果。
* **Memory Key**（记忆键）：选择或创建包含要查询的向量记忆的键。
* **Limit**（上限）：输入从向量存储检索的结果数量。例如，设为 `10` 可获取最匹配的十条结果。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Simple Vector Store（简单向量存储） 集成模板](https://n8n.io/integrations/in-memory-vector-store)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain Memory Vector Store 文档](https://docs.langchain.com/oss/javascript/integrations/vectorstores/memory)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: 嵌入是使用向量对数据进行数值化表示。AI 通过将值映射到多个维度，利用嵌入理解复杂数据及其关系。向量数据库或向量存储是专门用于存储和访问嵌入的数据库。
<a id="user-content-fn-2"></a>
[^2]: 向量存储或向量数据库用于存储信息的数学表示。将其与嵌入模型和检索器配合使用，可创建供 AI 在回答问题时访问的数据库。
[^3]: 在 AI 场景中，工具是附加资源，AI 可在响应请求时调用它获取特定信息或功能。AI 模型可以通过工具与外部系统交互，或完成具体、专门的任务。
