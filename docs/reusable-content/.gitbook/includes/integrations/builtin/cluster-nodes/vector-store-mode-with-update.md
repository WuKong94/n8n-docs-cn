---
title: 支持更新的向量存储模式
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

此向量存储节点有五种模式：**Get Many**（获取多条）、**Insert Documents**（插入文档）、**Retrieve Documents (As Vector Store for Chain/Tool)**（检索文档，作为链或工具的向量存储）、**Retrieve Documents (As Tool for AI Agent)**（检索文档，作为 AI 智能体工具）及 **Update Documents**（更新文档）。所选模式决定可执行的操作，以及可用的输入和输出。


#### Get Many（获取多条） <a href="#get-many" id="get-many"></a>

此模式下，可提供提示词，从向量数据库检索多个文档。提示词会转换为嵌入向量，用于相似度搜索。节点返回与提示词最相似的文档及其相似度分数。适合检索一组相似文档，再将其作为额外上下文传给智能体。

#### Insert Documents（插入文档） <a href="#insert-documents" id="insert-documents"></a>

使用 Insert Documents（插入文档）模式，将新文档插入向量数据库。

#### Retrieve Documents (As Vector Store for Chain/Tool)（检索文档，作为链或工具的向量存储） <a href="#retrieve-documents-as-vector-store-for-chaintool" id="retrieve-documents-as-vector-store-for-chaintool"></a>

将 Retrieve Documents (As Vector Store for Chain/Tool)（检索文档，作为链或工具的向量存储）模式与向量存储检索器配合使用，从向量数据库检索文档，并提供给与链相连的检索器。此模式下，必须将节点连接到检索器节点或根节点。

#### Retrieve Documents (As Tool for AI Agent)（检索文档，作为 AI 智能体工具） <a href="#retrieve-documents-as-tool-for-ai-agent" id="retrieve-documents-as-tool-for-ai-agent"></a>

使用 Retrieve Documents (As Tool for AI Agent)（检索文档，作为 AI 智能体工具）模式，将向量存储用作回答查询的工具资源。生成响应时，向量存储的名称和描述与问题详情匹配，智能体便会使用该向量存储。

#### Update Documents（更新文档） <a href="#update-documents" id="update-documents"></a>

使用 Update Documents（更新文档）模式，按 ID 更新向量数据库中的文档。在 **ID** 中填入要更新的嵌入条目 ID。
