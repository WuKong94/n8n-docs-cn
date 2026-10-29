---
description: 了解如何在 n8n 中使用 Databricks Vector Store 节点，搜索和填充 Databricks Vector Search
  索引，并将其连接到 AI 智能体和链。
status: preview
tags:
- tag: preview
  primary: true
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Databricks Vector Store（Databricks 向量存储） 节点 <a id="databricks-vector-store-node"></a>

使用 Databricks Vector Store 节点，在工作流中操作 [Databricks Vector Search](https://docs.databricks.com/aws/en/generative-ai/vector-search) 索引。可对索引进行相似度搜索、向 Direct Access 索引插入文档、将索引提供给连接到链[^1]的检索器，或作为工具[^3]连接到 AI 智能体[^2]。索引位于 Unity Catalog 中，因此节点只能访问凭据身份有权访问的数据。

本页介绍前置条件、节点支持的索引类型、节点参数和选项，以及完整示例。如果此前使用 `n8n-nodes-databricks` 社区包，请参阅[从社区包迁移](migrate-from-the-community-package.md)。

{% hint style="info" %}
**凭据**

身份验证设置指南，请参阅 [Databricks 凭据](../../../credentials/databricks.md)。此节点仅接受通过服务主体或用户登录配置的 **Databricks OAuth2 API** 凭据，不接受个人访问 token。
{% endhint %}

{% hint style="info" %}
**预览状态**

Databricks Vector Store 节点从 n8n 2.45.0 起处于预览阶段，未来版本中可能发生变化。请避免在生产工作流中依赖此节点。
{% endhint %}

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 前置条件 <a id="prerequisites"></a>

- 具有 Vector Search 端点且端点上至少有一个索引的 Databricks 工作区。请参阅 Databricks 文档中的[创建和查询向量搜索索引](https://docs.databricks.com/aws/en/vector-search/create-query-vector-search)。
- n8n 中通过服务主体或用户登录配置的 [Databricks OAuth2 凭据](../../../credentials/databricks.md#supported-authentication-methods)。
- 连接到节点 **Embedding**（嵌入）输入的 [Embeddings Databricks](../../sub-nodes/n8n-nodes-langchain.embeddingsdatabricks.md) 节点。所有操作模式都需要此输入，即使索引由 Databricks 自行计算嵌入也不例外。请参阅[索引类型与嵌入](#index-types-and-embeddings)。
- 凭据所验证的身份需要以下权限：
    - 对索引所在的目录和架构，分别具有 **USE CATALOG** 和 **USE SCHEMA** 权限。
    - 对索引具有 **SELECT** 权限。**Insert Documents**（插入文档）还需要索引的 **MODIFY** 权限。
    - 对同步其全部列的 Delta Sync 索引的源表具有 **SELECT** 权限，以便节点在 **Content Column**（内容列）和 **Metadata Columns**（元数据列）中列出列。缺少此权限时，**Metadata Columns** 为空，**Content Column** 仅提供嵌入源列，返回的文档只包含内容。
    - 对 Embeddings Databricks 节点使用的嵌入模型服务所在的目录和架构具有 **USE CATALOG** 和 **USE SCHEMA** 权限，并对该服务具有 **EXECUTE** 权限。默认情况下，Databricks 为所有用户授予 `system.ai` 服务的 **EXECUTE** 权限。
    - 使用 **Metadata Filter**（元数据过滤器）时，需要对提供该索引的 Vector Search 端点具有读取权限。节点每次执行读取一次端点类型，检查过滤器是否适用。工作区用户默认具有此权限。

服务主体必须是工作区成员，并具有 **Workspace access**（工作区访问）授权。仅存在于账户级别的服务主体会在工作区 token 端点返回 `invalid_client`，看起来像客户端密钥错误。完整列表，请参阅[所需的 Databricks 权限](../../../credentials/databricks.md#required-databricks-privileges)。

## 索引类型与嵌入 <a id="index-types-and-embeddings"></a>

Databricks 索引的两个属性决定节点可执行的操作：数据行如何进入索引，以及由谁计算嵌入。节点每次执行读取一次索引描述，并据此适配，无需选择查询模式。

### Delta Sync 和 Direct Access 索引 <a id="delta-sync-and-direct-access-indexes"></a>

| 索引类型 | 数据行来源 | Insert Documents（插入文档） |
|------------|---------------------|------------------|
| Delta Sync | Databricks 持续与索引同步的 Delta 表 | 不支持。请向源表添加行。节点会在写入前失败，返回 `Index <name> syncs from its source table. Use a Direct Access index to insert documents`。 |
| Direct Access | 通过 Vector Search API 写入的行 | 支持。**Insert Documents**（插入文档）模式下，**Index**（索引）列表仅显示 Direct Access 索引。 |

三种搜索模式均支持这两种索引类型。**Insert Documents**（插入文档）仅支持 Direct Access 索引。

### 托管和自行管理的嵌入 <a id="managed-and-self-managed-embeddings"></a>

| 嵌入类型 | 由谁生成文本嵌入 | 节点发送的内容 | Embeddings Databricks 节点 |
|------------|--------------------|---------------------|----------------------------|
| 托管：具有 Databricks 嵌入模型的 Delta Sync 索引 | Databricks，根据索引的嵌入源列生成 | 以 `query_text` 发送搜索文本 | 必须连接，但不会调用 |
| 自行管理：Direct Access 索引，或具有自有向量列的 Delta Sync 索引 | 所连接的 Embeddings Databricks 节点 | 以 `query_vector` 发送搜索文本的嵌入 | 每次搜索和每个插入文档都会调用 |

由上表可得 Embeddings Databricks 节点的使用规则：

- 所有模式都必须为 Vector Store 节点连接 Embeddings Databricks 节点。未连接时，节点将拒绝运行，返回 `A Embedding sub-node must be connected and enabled`。
- 对于托管索引，不会调用 Embeddings 节点，由 Databricks 自行生成查询嵌入。
- 对于自行管理的索引，Embeddings 节点为查询和插入文档生成嵌入，因此必须选择与生成索引向量时相同的模型和维度。模型不同会导致搜索返回 `query vector dimension <n> does not match index vector dimension <m>`，或插入返回 `Databricks rejected the upsert into <index>. Failed primary keys: ...`。

## 设置节点 <a id="set-up-the-node"></a>

1. 向工作流添加节点。对于 **Retrieve Documents (As Tool for AI Agent)**（检索文档，作为 AI 智能体的工具），请改为点击 [AI Agent](../n8n-nodes-langchain.agent/README.md) 或 [Databricks AI Agent](../n8n-nodes-langchain.databricksaiagent.md) 节点 **Tool**（工具）连接器上的 **+**。对于 **Retrieve Documents (As Vector Store for Chain/Tool)**（检索文档，作为链或工具的向量存储），点击 [Vector Store Retriever](../../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) 或 [Vector Store Question Answer Tool](../../sub-nodes/n8n-nodes-langchain.toolvectorstore.md) 节点 **Vector Store**（向量存储）连接器上的 **+**。
2. 在 **Credential to connect with**（连接凭据）中选择或创建 Databricks OAuth2 凭据。
3. 设置 **Operation Mode**（操作模式）。各模式的字段，请参阅[节点参数](#node-parameters)。
4. 在 **Index**（索引）中选择索引：
    - **From List**（从列表选择）：节点列出凭据可见的每个 Vector Search 端点上的所有索引，并标注为 `DELTA_SYNC - <endpoint>` 或 `DIRECT_ACCESS - <endpoint>`。输入文字可按名称过滤。在 **Insert Documents**（插入文档）模式下，列表仅显示 Direct Access 索引。
    - **Name**（名称）：输入完整的 Unity Catalog 名称，即 `catalog.schema.index`。节点会拒绝其他格式，在编辑器中返回 `Use the full name: catalog.schema.index`，运行时由表达式生成名称则返回 `Invalid Databricks index "<name>": use catalog.schema.index`。
5. 在 **Content Column**（内容列）中，选择作为文档文本（`pageContent`）的列。列表显示除主键和向量列外的索引列。对于托管索引，嵌入源列排在首位，标记为 `Embedding source column`；将字段留空即可使用该列。对于自行管理的索引，必须选择列：空值会导致失败，返回 `Index <name> uses self-managed embeddings. Select a content column`。
6. 点击 **Embedding**（嵌入）连接器上的 **+**，添加 [Embeddings Databricks](../../sub-nodes/n8n-nodes-langchain.embeddingsdatabricks.md) 节点。
7. 填写操作模式的字段和所需的[选项](#node-options)。

## 节点使用模式 <a id="node-usage-patterns"></a>

可按以下方式使用 Databricks Vector Store 节点。

### 作为普通节点插入和检索文档 <a id="use-as-a-regular-node-to-insert-and-retrieve-documents"></a>

可将 Databricks Vector Store 节点用作普通节点，插入或获取文档。此模式将节点放在常规连接流程中，无需使用智能体：通过 **Insert Documents**（插入文档）将文档加载器的数据载入 Direct Access 索引，通过 **Get Many**（获取多条）按提示词搜索，并在工作流后续步骤处理结果。

### 作为工具直接连接到 AI 智能体 <a id="connect-directly-to-an-ai-agent-as-a-tool"></a>

可将 Databricks Vector Store 节点直接连接到 [AI Agent](../n8n-nodes-langchain.agent/README.md) 或 [Databricks AI Agent](../n8n-nodes-langchain.databricksaiagent.md) 节点的工具连接器，让智能体在回答问题时将索引用作知识源。智能体自行生成搜索查询，工具返回匹配的文档。

此时连接方式为：AI Agent（工具连接器）→ Databricks Vector Store 节点。请参阅[示例：使用 AI 智能体根据 Databricks 索引回答问题](#example-answer-questions-from-a-databricks-index-with-an-ai-agent)。

### 使用检索器获取文档 <a id="use-a-retriever-to-fetch-documents"></a>

可将 [Vector Store Retriever](../../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) 节点与 Databricks Vector Store 节点配合使用，从索引获取文档。这通常与 [Question and Answer Chain](../n8n-nodes-langchain.chainretrievalqa/README.md) 节点配合，从向量存储获取与给定聊天输入匹配的文档。

连接流程为：Question and Answer Chain（Retriever 连接器）→ Vector Store Retriever（Vector Store 连接器）→ Databricks Vector Store。

### 使用 Vector Store Question Answer Tool 回答问题 <a id="use-the-vector-store-question-answer-tool-to-answer-questions"></a>

另一种模式使用 [Vector Store Question Answer Tool](../../sub-nodes/n8n-nodes-langchain.toolvectorstore.md)，汇总 Databricks Vector Store 节点的结果并回答问题。此模式通过专门用于汇总向量存储数据的工具工作，无需将 Databricks Vector Store 直接作为工具连接。

此时的连接流程为：AI Agent（工具连接器）→ Vector Store Question Answer Tool（Vector Store 连接器）→ Databricks Vector Store。

## 节点参数 <a id="node-parameters"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/vector-store-mode.md" %}

此节点不提供 **Update Documents**（更新文档）模式。每种模式都使用[设置节点](#set-up-the-node)中介绍的 **Index**（索引）和 **Content Column**（内容列）字段，以及下方列出的字段。

### Rerank Results（结果重排序） <a id="rerank-results"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/vector-store-rerank-results.md" %}

### Get Many（获取多条）参数 <a id="get-many-parameters"></a>

- **Prompt**（提示词）：输入搜索文本。对于托管索引，节点将其以 `query_text` 发送；对于自行管理的索引，Embeddings Databricks 节点先为其生成嵌入。
- **Limit**（上限）：输入返回结果数量，默认值为 `4`。这是唯一控制结果数量的选项，请参阅[无分数阈值](#no-score-threshold)。
- **Include Metadata**（包含元数据）：是否在输出中包含文档元数据，默认开启。

每个输出项都包含文档及其分数，格式为 `{ "document": { "pageContent": "...", "metadata": { ... } }, "score": 0.73 }`。不同索引或搜索模式的分数不可直接比较。

### Insert Documents（插入文档）参数 <a id="insert-documents-parameters"></a>

- **Index**（索引）：Direct Access 索引，列表仅显示此类索引。按名称输入 Delta Sync 索引时，节点会在任何写入之前失败。
- **Content Column**（内容列）：接收文档文本的列。此列必须存在于索引中，且不能是主键或向量列。节点会在写入之前报告错误选择，例如 `Column id is the primary key of <index>. Select another Content Column` 或 `Index <name> has no column <column>. Select a Content Column from: text, source`。
- **Embedding Batch Size**（嵌入批次大小）：节点在一次请求中发送给 Embeddings Databricks 节点以生成嵌入的文档数量，默认值为 `200`。

将 [Default Data Loader](../../sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md) 等文档加载器连接到 **Document**（文档）输入。节点使用连接的 Embeddings Databricks 节点为文档生成嵌入，每个文档写入一行，并输出已插入的文档。写入的行会在数秒内变得可搜索。

节点按以下方式填充数据行：

- 主键使用随机 UUID。内置文档加载器不设置文档 ID，因此重复运行相同插入操作会将文档添加两次，而非更新。请在上游去重，或在 Databricks 中删除旧行。如果文档自带 `id`，例如来自 [LangChain Code](../n8n-nodes-langchain.code.md) 节点，则使用该键写入，并替换具有相同键的行。
- 加载器元数据中与索引列匹配的键写入对应列。不匹配任何列的键会被丢弃。与主键、内容列或向量列同名的键也会被丢弃。丢弃键时不会警告，输出项仍会显示这些键。
- 取消执行会停止插入。节点已写入的行仍保留在索引中。

### Retrieve Documents（作为链或工具的向量存储）参数 <a id="retrieve-documents-as-vector-store-for-chaintool-parameters"></a>

此模式除 **Index**（索引）和 **Content Column**（内容列）外，没有专属字段。检索文档数量由连接的检索器或工具控制：请在 [Vector Store Retriever](../../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) 或 [Vector Store Question Answer Tool](../../sub-nodes/n8n-nodes-langchain.toolvectorstore.md) 节点设置 **Limit**（上限）。此处设置的[节点选项](#node-options)适用于这些节点执行的每次搜索。

### Retrieve Documents（作为 AI 智能体的工具）参数 <a id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

- **Description**（描述）：向智能体说明索引内容及何时搜索。具体的描述（例如 `Company handbook. Use it for any question about internal policies and processes.`）有助于获得更可靠的工具调用。智能体看到的工具名称为节点名称。
- **Limit**（上限）：输入每次工具调用返回的文档数量，默认值为 `4`。
- **Include Metadata**（包含元数据）：是否在工具结果中包含文档元数据，默认开启。

## 节点选项 <a id="node-options"></a>

这些选项适用于三种搜索模式：**Get Many**（获取多条）、**Retrieve Documents (As Vector Store for Chain/Tool)**（检索文档，作为链或工具的向量存储）和 **Retrieve Documents (As Tool for AI Agent)**（检索文档，作为 AI 智能体的工具）。

### Metadata Columns（元数据列） <a id="metadata-columns"></a>

要在文档元数据中返回的列。默认返回除主键、内容列和向量列之外的全部索引列。可选择部分列，减少智能体需要读取的数据量。列表不提供主键或向量列。

### Search Mode（搜索模式） <a id="search-mode"></a>

- **Vector**（向量，默认）：仅按语义相似度对结果排序，以 `query_type` `ANN` 发送。
- **Hybrid**（混合）：对搜索文本添加关键词匹配，使包含产品代码等精确词项的文档排在前面，以 `query_type` `HYBRID` 发送。对于自行管理的索引，节点同时发送向量和文本。混合搜索每次查询最多返回 200 条结果。

### Metadata Filter（元数据过滤器） <a id="metadata-filter"></a>

JSON 对象，将结果限定为索引列满足条件的数据行。节点将其以 `filters_json` 发送。同一对象内的键以 AND 逻辑组合。键包含列名称；除等值匹配外，还包含运算符：

| 条件 | Metadata Filter（元数据过滤器） |
|-----------|-----------------|
| 等于某个值 | `{"source": "handbook"}` |
| 不等于 | `{"source NOT": "draft"}` |
| 比较（`<`、`<=`、`>`、`>=`） | `{"year >=": 2025}` |
| 单列范围 | `{"price >=": 30000, "price <=": 55000}` |
| 多个值中的任意一个 | `{"source": ["handbook", "faq"]}` |
| token 匹配（不支持 `%` 通配符） | `{"title LIKE": "pricing"}` |
| 多列（AND） | `{"source": "handbook", "year >=": 2025}` |

注意事项：

- 过滤器仅适用于 **Standard** 类型的 Vector Search 端点。Storage Optimized 端点要求 SQL 过滤字符串，节点暂不支持。设置过滤器后，节点每次执行读取一次端点类型；端点不是 Standard 时，在查询前失败：`Index <name> runs on endpoint <endpoint> of type STORAGE_OPTIMIZED. The Metadata Filter works on STANDARD endpoints only.` 不带过滤器的查询适用于所有端点类型。
- 严格的过滤条件可能使返回行数少于 **Limit**（上限）。Databricks 先获取最近的候选项，再进行过滤，因此需要更多匹配项时，可提高 **Limit**。
- 过滤器未匹配任何内容时，返回零个数据项且不报错。JSON 格式错误时，在发出任何请求前即发生验证错误，并指明 **Metadata Filter**（元数据过滤器）字段。
- 不支持 `BETWEEN`、`LIKE` 中的通配符，以及对 JSON 列内嵌套值进行数值比较。完整语法，请参阅 [Databricks 过滤指南](https://docs.databricks.com/aws/en/ai-search/filtering-guide)。

## 已知限制 <a id="known-limits"></a>

- **始终需要 Embeddings 输入**：所有模式都需要 Embeddings Databricks 节点，包括由 Databricks 生成查询嵌入、从不调用此节点的托管索引。
- **Insert Documents 仅适用于 Direct Access 索引**：Delta Sync 索引对本节点为只读。插入时，不允许将主键或向量列用作 **Content Column**（内容列）。
- **插入行使用随机键**，除非文档自带 `id`。内置文档加载器不会设置该键，因此重新运行会产生重复行，而非更新行。
- **Metadata Filter 仅适用于 Standard 端点**：Storage Optimized 端点使用节点暂不支持的 SQL 过滤字符串。对此类端点执行带过滤器的查询，会在查询运行前失败。
- **混合搜索每次查询最多返回 200 条结果**。
- **严格的过滤条件可能使返回行数少于 Limit**，因为 Databricks 在获取最近的候选项之后才进行过滤。
- **按 token 计费服务的速率限制**：一次为大批文档生成嵌入，可能触发工作区嵌入模型服务的速率限制。避免此问题的方法，请参阅 Embeddings Databricks 页面的[速率限制](../../sub-nodes/n8n-nodes-langchain.embeddingsdatabricks.md#rate-limits)。

### 无分数阈值 <a id="no-score-threshold"></a>

节点有意不提供分数阈值字段。Vector 和 Hybrid 搜索使用不同评分尺度：自行管理的索引的相似度分数可能在 `0.003` 附近，而 Hybrid 搜索将精确关键词匹配排在 `1.0`。同一个截断值不可能同时适合两者，错误的值会悄无声息地丢弃全部结果。请使用 **Limit**（上限）控制结果数量；如果需要为特定索引设置截断值，可在后续节点按 `score` 字段过滤。

## 示例：使用 AI 智能体根据 Databricks 索引回答问题 <a id="example-answer-questions-from-a-databricks-index-with-an-ai-agent"></a>

此工作流根据存储在 Delta Sync 索引中的公司手册回答聊天问题，嵌入由 Databricks 计算。请将索引和模型名称替换为你自己的名称。

1. 在 Databricks 中，为手册表创建 Delta Sync 索引，例如 `main.docs.handbook_index`，使用 `content` 列作为嵌入源，使用 `source` 列记录文档来源。请参阅[创建和查询向量搜索索引](https://docs.databricks.com/aws/en/vector-search/create-query-vector-search)。
2. 添加 [Chat Trigger](../../../core-nodes/n8n-nodes-langchain.chattrigger/README.md) 节点。
3. 在其后添加 [Databricks AI Agent](../n8n-nodes-langchain.databricksaiagent.md) 节点。[AI Agent](../n8n-nodes-langchain.agent/README.md) 节点具有相同工作方式，但不提供追踪导出。在 **Options**（选项）中，设置 **System Message**（系统消息），例如 `Answer questions about the company handbook with the handbook tool. Say so when the handbook doesn't cover a question.`
4. 点击智能体 **Chat Model**（聊天模型）连接器上的 **+**，添加 [Databricks Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatdatabricks.md) 节点。选择 Databricks 凭据和支持聊天的模型服务，例如 `system.ai.meta-llama-3-3-70b-instruct`。
5. 点击 **Memory**（记忆）连接器上的 **+**，添加 [Simple Memory](../../sub-nodes/n8n-nodes-langchain.memorybufferwindow/README.md) 节点，使追问保留上下文。
6. 点击 **Tool**（工具）连接器上的 **+**，添加 **Databricks Vector Store** 节点。将节点命名为 `handbook`。将 **Operation Mode**（操作模式）设为 **Retrieve Documents (As Tool for AI Agent)**（检索文档，作为 AI 智能体的工具），在 **Index**（索引）中选择 `main.docs.handbook_index`，将 **Content Column**（内容列）留空，使节点使用嵌入源列，并将 **Description**（描述）设为 `Company handbook. Use it for any question about internal policies and processes.` 保持 **Limit**（上限）为 `4`。
7. 点击向量存储 **Embedding**（嵌入）连接器上的 **+**，添加 [Embeddings Databricks](../../sub-nodes/n8n-nodes-langchain.embeddingsdatabricks.md) 节点，使用相同凭据和嵌入模型服务，例如 `system.ai.gte-large-en`。该索引为托管索引，因此由 Databricks 生成查询嵌入，从不调用此节点，但仍需要建立连接。
8. 可选：在智能体节点中选择 Databricks 凭据，开启 **Export Traces to MLflow**（将追踪导出到 MLflow），以便在 [MLflow Tracing](../n8n-nodes-langchain.databricksaiagent.md#what-the-node-exports) 中查看每次运行，包括手册搜索。
9. 打开聊天，提出一个可从手册中得到答案的问题。执行中会显示一次 `handbook` 工具调用，包含智能体的搜索查询和返回的文档。

如需改为搜索自行管理的索引，请在向量存储节点设置 **Content Column**（内容列），并在 Embeddings Databricks 节点选择生成索引向量时使用的模型。如需将智能体限定到索引的某一部分，请在向量存储节点选项中添加 **Metadata Filter**（元数据过滤器），例如 `{"source": "handbook"}`。

## 相关资源 <a id="related-resources"></a>

- [从社区包迁移](migrate-from-the-community-package.md)
- [Databricks 凭据](../../../credentials/databricks.md)
- [Embeddings Databricks](../../sub-nodes/n8n-nodes-langchain.embeddingsdatabricks.md)
- [Databricks AI Agent](../n8n-nodes-langchain.databricksaiagent.md)
- [Databricks Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatdatabricks.md)
- [Databricks 节点](../../../app-nodes/n8n-nodes-base.databricks.md)，提供创建、列出索引等 Vector Search 索引操作
- [Vector Store Retriever](../../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) 和 [Vector Store Question Answer Tool](../../sub-nodes/n8n-nodes-langchain.toolvectorstore.md)
- Databricks 文档中的 [Databricks Vector Search](https://docs.databricks.com/aws/en/generative-ai/vector-search)、[查询索引 API](https://docs.databricks.com/api/workspace/vectorsearchindexes/queryindex) 和[过滤指南](https://docs.databricks.com/aws/en/ai-search/filtering-guide)

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/starter-kits/self-hosted-ai-starter-kit.md" %}

## 常见问题 <a id="common-issues"></a>

### A Embedding sub-node must be connected and enabled（必须连接并启用嵌入子节点） <a id="a-embedding-sub-node-must-be-connected-and-enabled"></a>

节点的 **Embedding**（嵌入）输入没有连接 Embeddings Databricks 节点。所有模式都需要连接，即使是从不调用此节点的托管索引。

### 索引使用自行管理的嵌入 <a id="index-uses-self-managed-embeddings"></a>

错误 `Index <name> uses self-managed embeddings. Select a content column` 表示索引自带向量，节点无法推断哪一列包含文本。请在 **Content Column**（内容列）中选择该列。

### 索引从源表同步 <a id="index-syncs-from-its-source-table"></a>

**Insert Documents**（插入文档）目标为 Delta Sync 索引时，节点会报告 `Index <name> syncs from its source table. Use a Direct Access index to insert documents`。Databricks 从源表填充 Delta Sync 索引，因此请向源表添加行，或改为向 Direct Access 索引插入。

### Insufficient permissions for UC entity（UC 实体权限不足） <a id="insufficient-permissions-for-uc-entity"></a>

`Databricks Vector Search request failed (403): Insufficient permissions for UC entity <index>` 表示凭据身份缺少索引的 **SELECT** 权限，或缺少插入所需的 **MODIFY** 权限。请在 Unity Catalog 中授予相应权限，以及 **USE CATALOG** 和 **USE SCHEMA** 权限。

### Unity Catalog 实体不存在 <a id="unity-catalog-entity-doesnt-exist"></a>

`Databricks Vector Search request failed (404): Unity Catalog entity <name> does not exist` 表示 **Index**（索引）名称未匹配该身份可见的索引。请检查由三部分组成的名称，或通过 **From List**（从列表选择）选择索引。

### 查询向量维度与索引不匹配 <a id="query-vector-dimension-doesnt-match-the-index"></a>

错误 `query vector dimension <n> does not match index vector dimension <m>` 表示 Embeddings Databricks 节点使用的模型维度与索引不同。请选择生成索引向量时使用的模型。插入时，同样的维度不匹配会表现为 `Databricks rejected the upsert into <index>. Failed primary keys: ...`，节点不会写入任何内容。

### Failed to retrieve Databricks access token（获取 Databricks 访问 token 失败） <a id="failed-to-retrieve-databricks-access-token"></a>

凭据无法从工作区获取 token。使用服务主体时，`invalid_client` 表示主体尚未分配到工作区：请将其添加到工作区，并授予 **Workspace access**（工作区访问）授权。如果错误描述包含 HTML，则凭据的 **Host**（主机）不是 Databricks 工作区 URL。

### Host must use HTTPS（主机必须使用 HTTPS） <a id="host-must-use-https"></a>

节点失败并返回 `Databricks host must use https`，表示凭据的 **Host**（主机）不是 `https://` URL，例如地址以 `http://` 开头或缺少协议。每个请求都携带 token，因此节点拒绝普通 HTTP。请输入包含 `https://` 的完整工作区 URL。

### 插入期间达到速率限制 <a id="rate-limit-reached-during-an-insert"></a>

嵌入模型服务拒绝了某个批次，返回 `REQUEST_LIMIT_EXCEEDED`。节点没有写入触发限制的数据块，但之前已写入的数据块仍保留在索引中，因此重试前请检查索引。请参阅 Embeddings Databricks 页面的[速率限制](../../sub-nodes/n8n-nodes-langchain.embeddingsdatabricks.md#rate-limits)。

### The Metadata Filter works on STANDARD endpoints only（元数据过滤器仅适用于 STANDARD 端点） <a id="the-metadata-filter-works-on-standard-endpoints-only"></a>

已设置 **Metadata Filter**（元数据过滤器），但索引运行在 Storage Optimized 端点上。该端点接受节点暂不支持的 SQL 过滤字符串。请移除过滤器，或将索引迁移到 Standard 端点。如果消息以 `Could not read the type of the endpoint` 开头，表示凭据身份无法读取 Vector Search 端点：请授予该端点的读取权限，或移除过滤器。

[^1]: AI 链通过对组件的一系列调用，让你与大语言模型（LLM）及其他资源交互。n8n 中的 AI 链不使用持久记忆，因此不能通过它引用先前的上下文（此用途请使用 AI 智能体）。
[^2]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大语言模型（LLM）理解用户输入，利用可用的信息和资源，决定如何最好地处理请求。
[^3]: 在 AI 场景中，工具是附加资源，AI 可在响应请求时调用它获取特定信息或功能。AI 模型可以通过工具与外部系统交互，或完成具体、专门的任务。
