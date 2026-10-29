---
description: 了解如何在 n8n 中使用 Embeddings Databricks 节点，通过 Databricks 模型服务生成嵌入向量，并与 Databricks
  Vector Store 节点配合。
status: preview
tags:
- tag: preview
  primary: true
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Embeddings Databricks（Databricks 嵌入模型） 节点 <a id="embeddings-databricks-node"></a>

使用 Embeddings Databricks 节点，通过 Databricks 工作区提供的嵌入模型为文本生成嵌入向量[^1]。节点查询 [Unity AI Gateway 模型服务](https://docs.databricks.com/aws/en/ai-gateway/model-services)，与 [Databricks Chat Model](n8n-nodes-langchain.lmchatdatabricks.md) 节点使用相同网关。它主要与 [Databricks Vector Store](../root-nodes/n8n-nodes-langchain.vectorstoredatabricks/README.md) 节点配合，后者在每种操作模式下都需要嵌入连接。

本页介绍 Embeddings Databricks 节点的前置条件、配置步骤、配对规则、节点参数及已知问题。

{% hint style="info" %}
**凭据**

身份验证设置方法，请参阅 [Databricks 凭据](../../credentials/databricks.md)。此节点仅接受 **Databricks OAuth2 API** 凭据，可使用服务主体或用户登录，不接受个人访问令牌。
{% endhint %}

{% hint style="info" %}
**预览状态**

Embeddings Databricks 节点从 n8n 2.45.0 起处于 Preview（预览）阶段，未来版本可能发生变化。请避免在生产工作流中依赖此节点。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 前置条件 <a id="prerequisites"></a>

- 已启用 Unity AI Gateway 的 Databricks 工作区。
- n8n 中的 [Databricks OAuth2 凭据](../../credentials/databricks.md#supported-authentication-methods)，使用服务主体或用户登录。
- 凭据对应的身份需要对模型服务所在的目录和架构具有 **USE CATALOG** 和 **USE SCHEMA** 权限，并对模型服务具有 **EXECUTE** 权限。Databricks 默认向所有工作区用户授予 `system.ai` 模型服务的 **EXECUTE** 权限。请参阅[所需 Databricks 权限](../../credentials/databricks.md#required-databricks-privileges)。

## 配置节点 <a id="set-up-the-node"></a>

1. 向工作流添加 [Databricks Vector Store](../root-nodes/n8n-nodes-langchain.vectorstoredatabricks/README.md) 节点，或其他接受嵌入子节点的节点。
2. 选择节点 **Embedding**（嵌入）连接器上的 **+**，再选择 **Embeddings Databricks**。
3. 在 **Credential to connect with**（连接凭据）下，选择现有 Databricks OAuth2 凭据或创建新凭据。
4. 在 **Model**（模型）中打开列表，选择模型服务。n8n 加载凭据可访问且支持嵌入的模型服务，排除聊天模型。输入文字可筛选列表。要使用未列出的服务，将模式切换为 **ID**，输入完整名称，例如 `system.ai.gte-large-en`。

## 将节点与 Databricks 索引配对 <a id="pair-the-node-with-a-databricks-index"></a>

模型选择取决于 Databricks Vector Store 节点使用的索引：

- **Managed index**（托管索引，即使用 Databricks 嵌入模型的 Delta Sync 索引）：Databricks 自行使用索引的模型生成查询嵌入。必须连接 Embeddings Databricks 节点，但不会实际调用，因此任意模型服务均可。
- **Self-managed index**（自行管理的索引，即 Direct Access 索引，或使用自有向量列的 Delta Sync 索引）：Embeddings Databricks 节点为每次搜索查询生成嵌入；对于 Direct Access 索引，也为每个插入文档生成嵌入。请选择与构建索引时相同的模型和维度。使用 1024 维的 `databricks-gte-large-en` 构建的索引，需要 `system.ai.gte-large-en` 模型服务。使用不同模型时，搜索会报 `query vector dimension <n> does not match index vector dimension <m>`，插入会报 `Databricks rejected the upsert into <index>. Failed primary keys: ...`。

向量存储节点如何决定发送哪种查询形式，请参阅 Databricks Vector Store 页面中的[索引类型与嵌入](../root-nodes/n8n-nodes-langchain.vectorstoredatabricks/README.md#index-types-and-embeddings)。

此节点是标准嵌入子节点，也可与 n8n 的其他向量存储节点配合，例如 [Simple Vector Store](../root-nodes/n8n-nodes-langchain.vectorstoreinmemory.md)。

## 节点参数 <a id="node-parameters"></a>

- **Model**（模型）：生成嵌入向量的 Unity AI Gateway 模型服务，名称格式为 `catalog.schema.service`。
    - **From List**（从列表选择）：从凭据可访问且支持嵌入的模型服务中选择。
    - **ID**：直接输入模型服务的完整名称。适用于支持嵌入、但未声明具备嵌入能力的服务。

## 节点选项 <a id="node-options"></a>

- **Batch Size**（批次大小）：单次请求发送的最大文档数量，默认为 `512`，最大为 `2048`。减小此值前，请参阅[速率限制](#rate-limits)。
- **Strip New Lines**（移除换行符）：是否在生成嵌入前移除输入文本中的换行符，默认开启。
- **Timeout**（超时）：请求的最长耗时，单位为毫秒，默认为 `360000`（六分钟）。请求超时会报 `Request timed out.`。
- **Max Retries**（最大重试次数）：请求失败后的重试次数，默认为 `2`。

## 速率限制 <a id="rate-limits"></a>

按 token 付费的模型服务按工作区实施速率限制。Databricks Vector Store 节点插入文档时，会按 **Embedding Batch Size**（嵌入批次大小，默认为 `200`）分块生成嵌入，每个块再按此节点的 **Batch Size**（批次大小）拆成并行请求。较小的 **Batch Size** 会将一个块拆成大量同时发出的请求，可能超过工作区对模型服务的限制。节点会对被拒绝的请求进行退避重试，最多重试 **Max Retries** 次，之后插入会以 `Databricks rate limit reached for <service>: REQUEST_LIMIT_EXCEEDED: Exceeded workspace QPS rate limit` 失败。触及限制的块不会写入，但此前已完成嵌入并写入的块仍保留在索引中，因此重试前请检查索引。

避免此问题的方法是保持默认 **Batch Size**（批次大小），使每个块通过一次请求发送；降低并发插入数量；或为模型使用[预配吞吐量](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis)端点。

## 相关资源 <a id="related-resources"></a>

- [Databricks Vector Store（Databricks 向量存储）](../root-nodes/n8n-nodes-langchain.vectorstoredatabricks/README.md)
- [Databricks AI Agent（Databricks AI 智能体）](../root-nodes/n8n-nodes-langchain.databricksaiagent.md)
- [Databricks Chat Model（Databricks 聊天模型）](n8n-nodes-langchain.lmchatdatabricks.md)
- [Databricks 凭据](../../credentials/databricks.md)
- Databricks 文档中的 [Unity AI Gateway 模型服务](https://docs.databricks.com/aws/en/ai-gateway/model-services)
- 从社区软件包迁移：请参阅[从 n8n-nodes-databricks 社区软件包迁移](../root-nodes/n8n-nodes-langchain.vectorstoredatabricks/migrate-from-the-community-package.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 常见问题 <a id="common-issues"></a>

### No model services found（未找到模型服务） <a id="no-model-services-found"></a>

模型列表为空，节点报告 `No model services found`。工作区未启用 Unity AI Gateway，或凭据对应的身份无法访问任何模型服务。请检查工作区设置，再为至少一个模型服务授予 **USE CATALOG**、**USE SCHEMA** 和 **EXECUTE** 权限。

### No embeddings-capable model services found（未找到支持嵌入的模型服务） <a id="no-embeddings-capable-model-services-found"></a>

凭据可以访问模型服务，但没有任何服务声明支持嵌入。将 **Model**（模型）切换为 **ID**，直接输入服务名称。仅支持聊天的服务不适用于此节点。

### Model service not found（未找到模型服务） <a id="model-service-not-found"></a>

节点以 `The resource you are requesting could not be found` 失败，错误描述指出缺失的服务。**Model**（模型）名称在工作区中不存在。请检查三段式名称，或通过 **From List**（从列表选择）选择服务。

### 查询向量维度与索引不匹配 <a id="query-vector-dimension-doesnt-match-the-index"></a>

模型与 Databricks Vector Store 节点搜索的索引不匹配。请参阅[将节点与 Databricks 索引配对](#pair-the-node-with-a-databricks-index)。

### 达到速率限制 <a id="rate-limit-reached"></a>

执行以 `Databricks rate limit reached for <service>` 和 429 状态失败。请参阅[速率限制](#rate-limits)。

### 主机必须使用 HTTPS <a id="host-must-use-https"></a>

节点以 `Databricks host must use https` 失败，因为凭据的 **Host**（主机）不是 `https://` URL，例如以 `http://` 开头或缺少协议。每次请求都携带令牌，因此节点拒绝纯 HTTP。请输入使用 `https://` 的完整工作区 URL。

### 连接错误 <a id="connection-error"></a>

节点报告 `Connection error.`，但没有 Databricks 消息。凭据的 **Host**（主机）未指向 Databricks 工作区，或 n8n 实例无法访问该工作区。请检查主机 URL 和网络路径。

[^1]: 嵌入是使用向量对数据进行数值化表示。AI 通过将值映射到多个维度，利用嵌入理解复杂数据及其关系。向量数据库或向量存储是专门用于存储和访问嵌入的数据库。
