---
description: 将工作流从 n8n-nodes-databricks 社区包迁移到内置 Databricks 节点：节点映射、字段差异及行为变化。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 从 n8n-nodes-databricks 社区包迁移 <a id="migrate-from-the-n8n-nodes-databricks-community-package"></a>

内置 Databricks 节点替代 [n8n-nodes-databricks](https://www.npmjs.com/package/n8n-nodes-databricks) 社区包。本页列出各社区节点对应的内置节点、发生变化的字段，以及迁移后的行为变化。

社区节点和内置节点的节点类型不同，因此不能原地转换。对于工作流中的每个社区节点：添加内置节点、复制设置、重新连接，然后删除社区节点。

内置 AI 节点需要通过服务主体或用户登录配置的 [Databricks OAuth2 凭据](../../../credentials/databricks.md#supported-authentication-methods)。社区包使用的主机和个人访问 token 凭据，在内置 AI 节点中没有对应选项；只有内置 [Databricks](../../../app-nodes/n8n-nodes-base.databricks.md) 和 [Databricks Trigger](../../../trigger-nodes/n8n-nodes-base.databrickstrigger.md) 节点接受个人访问 token。

## 节点映射 <a id="node-mapping"></a>

| 社区节点 | 内置节点 | 变化 |
|----------------|---------------|--------------|
| Databricks | [Databricks](../../../app-nodes/n8n-nodes-base.databricks.md) | 提供相同资源。内置节点新增 Job 操作和 [Databricks Trigger](../../../trigger-nodes/n8n-nodes-base.databrickstrigger.md) 节点。 |
| Databricks Chat Model | [Databricks Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatdatabricks.md) | **Model**（模型）选择 Unity AI Gateway 模型服务 `catalog.schema.service`，而非服务端点。不提供 **Conversation ID**（对话 ID）和 **Return Trace**（返回追踪）选项。 |
| Embeddings Databricks | [Embeddings Databricks](../../sub-nodes/n8n-nodes-langchain.embeddingsdatabricks.md) | **Serving Endpoint**（服务端点）改为 **Model**（模型），列出支持嵌入的模型服务。 |
| Databricks Vector Store | [Databricks Vector Store](README.md) | **Index Name**（索引名称）改为 **Index**（索引），可从列表选择或输入完整的 `catalog.schema.index` 名称。**Text Column**（文本列）改为 **Content Column**（内容列），从索引列中选择。**Metadata Columns**（元数据列）改为多选，而非逗号分隔列表。不再提供 **Score Threshold**（分数阈值），请使用 **Limit**（上限）。新增 **Search Mode**（搜索模式）和 **Metadata Filter**（元数据过滤器）。 |
| Databricks AI Agent | [Databricks AI Agent](../n8n-nodes-langchain.databricksaiagent.md) | **Enable MLflow Tracking**（启用 MLflow 跟踪）改为 **Export Traces to MLflow**（将追踪导出到 MLflow）。默认实验路径 `/Shared/n8n-workflows-<workflow-id>` 不变，新增 **Experiment**（实验）字段可选择现有实验。智能体上的凭据仅在导出时需要。 |

## Vector Store 节点的字段差异 <a id="field-differences-on-the-vector-store-node"></a>

| 社区字段 | 内置字段 | 说明 |
|-----------------|----------------|-------|
| **Index Name**（索引名称，文本） | **Index**（索引） | 选择 **From List**（从列表选择），或在 **Name**（名称）中输入完整名称。**Insert Documents**（插入文档）模式下，列表仅显示 Direct Access 索引。 |
| **Text Column**（文本列，默认 `text`） | **Content Column**（内容列） | 从索引列中选择。托管索引可留空，以使用嵌入源列。 |
| **Metadata Columns**（元数据列，逗号分隔文本） | **Metadata Columns**（元数据列）选项 | 改为多选。留空时，返回除主键、内容列和向量列以外的全部列。 |
| **Score Threshold**（分数阈值，默认 `0.8`） | 无 | 使用 **Limit**（上限）。原因请参阅[无分数阈值](README.md#no-score-threshold)。 |
| 无 | **Search Mode**（搜索模式）选项 | **Vector**（向量）或 **Hybrid**（混合）。 |
| 无 | **Metadata Filter**（元数据过滤器）选项 | 以 `filters_json` 发送的 JSON 过滤器。 |

## 迁移后的行为变化 <a id="behavior-changes-to-expect"></a>

- **支持搜索托管索引。** 社区节点始终发送 `query_vector`，因此对由 Databricks 计算嵌入的 Delta Sync 索引执行的搜索全部失败。内置节点根据索引要求发送 `query_text` 或 `query_vector`。请参阅[索引类型与嵌入](README.md#index-types-and-embeddings)。
- **不会因阈值丢弃结果。** 社区节点的 **Score Threshold**（分数阈值）默认为 `0.8`，会丢弃相似度分数远低于该值的索引中的全部结果。内置节点返回前 **Limit**（上限）条结果。
- **混合搜索和元数据过滤器**适用于所有搜索模式，包括智能体将索引用作工具的场景。
- **在请求前检查插入操作。** 如果指定 Delta Sync 索引或错误的 **Content Column**（内容列），节点会失败，并明确指出问题，而非返回原始 API 错误。
- **智能体实现保持一致。** 内置 Databricks AI Agent 运行 AI Agent 节点自身的代码，而非分叉版本，因此具有相同选项，并获得相同修复。
- 在现有工作流中替换智能体节点时，**追踪仍写入同一实验**，因为默认实验路径包含工作流 ID。

## 相关资源 <a id="related-resources"></a>

- [Databricks Vector Store](README.md)
- [Embeddings Databricks](../../sub-nodes/n8n-nodes-langchain.embeddingsdatabricks.md)
- [Databricks AI Agent](../n8n-nodes-langchain.databricksaiagent.md)
- [Databricks Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatdatabricks.md)
- [Databricks 凭据](../../../credentials/databricks.md)
