---
title: SQL AI Agent（SQL AI 智能体） 节点文档
description: 了解如何在 n8n 的 AI Agent 节点中使用 SQL Agent，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: critical
nodeTitle: SQL AI Agent（SQL AI 智能体） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/sql-agent.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/sql-agent
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/sql-agent
layout:
  description:
    visible: false
tags:
- tag: deprecated
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# SQL AI Agent（SQL AI 智能体） 节点 <a href="#sql-ai-agent-node" id="sql-ai-agent-node"></a>

{% hint style="warning" %}
**功能可用性**

SQL Agent 从 n8n 1.82.0 起弃用。新增或更新的 AI Agent 节点改用 [Tools Agent](tools-agent.md)。只有仍使用 AI Agent 节点版本 1 的工作流可选择 SQL Agent。

AI Agent 节点版本 1 从 n8n 3.0 中移除，因此 SQL Agent 将在所有工作流中停止工作。详情请参阅 [n8n 3.0 破坏性变更](../../../../../changelog/v30-breaking-changes.md)。
{% endhint %}

SQL Agent 以 SQL 数据库为数据源，可理解自然语言问题，将其转换为 SQL 查询、执行查询，再以易读的格式呈现结果，适合构建数据库的自然语言接口。

AI Agent 节点本身的更多信息，请参阅 [AI Agent](README.md)。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置 SQL Agent。

### Data Source（数据源） <a href="#data-source" id="data-source"></a>

选择节点使用的数据库数据源，可选：

* **MySQL**：使用 MySQL 数据库。
    * 还需选择 **Credential for MySQL**（MySQL 凭据）。
* **SQLite**：使用 SQLite 数据库。
    * 必须在 Agent 前添加 [Read/Write File From Disk](../../../core-nodes/n8n-nodes-base.readwritefile.md) 节点，读取 SQLite 文件。
    * 还需输入 Read/Write File From Disk 节点传入 SQLite 文件的 **Input Binary Field**（输入二进制字段）名称。
* **Postgres**：使用 Postgres 数据库。
    * 还需选择 **Credential for Postgres**（Postgres 凭据）。

{% hint style="warning" %}
**Postgres 和 MySQL 智能体**

使用 [Postgres](../../../credentials/postgres.md) 或 [MySQL](../../../credentials/mysql.md) 时，此智能体不支持凭据的隧道选项。
{% endhint %}

### Prompt（提示词） <a href="#prompt" id="prompt"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/prompt.md" %}

## 节点选项 <a href="#node-options" id="node-options"></a>

使用以下选项调整 SQL Agent 节点的行为：

### Ignored Tables（忽略的表） <a href="#ignored-tables" id="ignored-tables"></a>

希望节点忽略数据库中的某些表时，输入以逗号分隔的表名称列表。

留空时，智能体不忽略任何表。

### Include Sample Rows（包含示例行） <a href="#include-sample-rows" id="include-sample-rows"></a>

输入发送给智能体的提示词中包含的示例行数，默认为 `3`。

示例行有助于智能体理解数据库架构，但也会增加 token 用量。

### Included Tables（包含的表） <a href="#included-tables" id="included-tables"></a>

希望仅包含数据库中的指定表时，输入以逗号分隔的表名称列表。

留空时，智能体包含所有表。

### Prefix Prompt（前缀提示词） <a href="#prefix-prompt" id="prefix-prompt"></a>

输入放在 **Prompt**（提示词）文本之前发送给智能体的消息，可为智能体提供更多上下文和指引，说明允许和不允许的操作，以及响应的格式。

n8n 会在此字段中填入示例。

### Suffix Prompt（后缀提示词） <a href="#suffix-prompt" id="suffix-prompt"></a>

输入放在 **Prompt**（提示词）文本之后发送给智能体的消息。

可用的 LangChain 表达式：

* `{chatHistory}`：本次对话的消息历史，用于保持上下文。
* `{input}`：包含用户提示词。
* `{agent_scratchpad}`：需要为下一次迭代记住的信息。

n8n 会在此字段中填入示例。

### Limit（上限） <a href="#limit" id="limit"></a>

输入返回结果的最大数量。

默认为 `10`。

### Tracing Metadata（追踪元数据） <a href="#tracing-metadata" id="tracing-metadata"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/tracing-metadata.md" %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

请参阅 AI Agent 主节点的[模板与示例](README.md#templates-and-examples)部分。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见问题及建议的解决办法，请参阅[常见问题](common-issues.md)。


