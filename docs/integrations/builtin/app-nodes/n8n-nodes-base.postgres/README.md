---
title: Postgres 节点文档
description: 了解如何在 n8n 中使用 Postgres 节点，并按照技术文档将 Postgres 节点集成到工作流中。
contentType:
- integration
- reference
priority: critical
nodeTitle: n8n-nodes-base.postgres
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.postgres/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Postgres 节点 <a href="#postgres-node" id="postgres-node"></a>

使用 Postgres 节点自动处理 Postgres 中的工作，并将其与其他应用集成。n8n 内置支持多种 Postgres 功能，包括执行查询，以及插入和更新数据库中的行。

本页列出了 Postgres 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Postgres 凭据](../../credentials/postgres.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* [**Delete**](#delete)（删除）：删除整张表或表中的行
* [**Execute Query**](#execute-query)（执行查询）：执行 SQL 查询
* [**Insert**](#insert)（插入）：向表中插入行
* [**Insert or Update**](#insert-or-update)（插入或更新）：插入或更新表中的行
* [**Select**](#select)（查询）：查询表中的行
* [**Update**](#update)（更新）：更新表中的行

### Delete（删除） <a href="#delete" id="delete"></a>

此操作用于删除整张表或表中的行。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Postgres 凭据](../../credentials/postgres.md)。
- **Operation**（操作）：选择 **Delete**（删除）。
- **Schema**（模式）：选择包含目标表的模式。选择 **From list**（从列表）可在下拉列表中选择模式，选择 **By Name**（按名称）可输入模式名。
- **Table**（表）：选择要操作的表。选择 **From list**（从列表）可在下拉列表中选择表，选择 **By Name**（按名称）可输入表名。
- **Command**（命令）：要执行的删除动作：
    - **Truncate**（清空表）：移除表中的数据，但保留表结构。
        - **Restart Sequences**（重置序列）：是否在清空表时将自增列重置为初始值。
    - **Delete**（删除行）：删除满足 Select Rows（选择行）条件的行。不设置条件时，Postgres 会删除所有行。
        - **Select Rows**（选择行）：通过 **Column**（列）、**Operator**（运算符）和 **Value**（值）设置行匹配条件。
        - **Combine Conditions**（组合条件）：如何组合 Select Rows（选择行）中的条件。**AND**（与）要求所有条件成立，**OR**（或）要求至少一个条件成立。
    - **Drop**（删除表）：永久删除表的数据及结构。

#### 删除选项 <a href="#delete-options" id="delete-options"></a>

- **Cascade**（级联）：使用 **Truncate**（清空表）时，级联清空通过外键引用该表的其他表；使用 **Drop**（删除表）时，级联删除依赖对象，例如视图。
- **Connection Timeout**（连接超时）：尝试连接数据库的时间，单位为秒。
- **Delay Closing Idle Connection**（延迟关闭空闲连接）：空闲连接可被关闭前需要等待的秒数。
- **Query Batching**（查询批处理）：向数据库发送查询的方式：
    - **Single Query**（单个查询）：对所有输入数据项使用一个查询。
    - **Independently**（独立执行）：为本次执行中的每个输入数据项执行一个查询。
    - **Transaction**（事务）：在一个事务中执行所有查询。发生失败时，Postgres 回滚所有更改。
- **Output Large-Format Numbers As**（大数值输出格式）：`NUMERIC` 和 `BIGINT` 列的输出格式：
    - **Numbers**（数字）：用于常规数值。
    - **Text**（文本）：预计数字超过 16 位时使用，否则数字可能不准确。

### Execute Query（执行查询） <a href="#execute-query" id="execute-query"></a>

此操作用于执行 SQL 查询。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Postgres 凭据](../../credentials/postgres.md)。
- **Operation**（操作）：选择 **Execute Query**（执行查询）。
- **Query**（查询）：要执行的 SQL 查询。可使用 n8n [表达式](../../../../build/work-with-data/expressions-versus-data-nodes.md)及 `$1`、`$2`、`$3` 等占位符构建[预处理语句](https://www.postgresql.org/docs/current/sql-prepare.html)，配合[查询参数](#use-query-parameters)使用。

#### 执行查询选项 <a href="#execute-query-options" id="execute-query-options"></a>

- **Connection Timeout**（连接超时）：尝试连接数据库的时间，单位为秒。
- **Delay Closing Idle Connection**（延迟关闭空闲连接）：空闲连接可被关闭前需要等待的秒数。
- **Query Batching**（查询批处理）：向数据库发送查询的方式：
    - **Single Query**（单个查询）：对所有输入数据项使用一个查询。
    - **Independently**（独立执行）：为本次执行中的每个输入数据项执行一个查询。
    - **Transaction**（事务）：在一个事务中执行所有查询。发生失败时，Postgres 回滚所有更改。
- **Query Parameters**（查询参数）：以英文逗号分隔的值列表，用作[查询参数](#use-query-parameters)。
- **Output Large-Format Numbers As**（大数值输出格式）：`NUMERIC` 和 `BIGINT` 列的输出格式：
    - **Numbers**（数字）：用于常规数值。
    - **Text**（文本）：预计数字超过 16 位时使用，否则数字可能不准确。
- **Replace Empty Strings with NULL**（将空字符串替换为 NULL）：是否将输入中的空字符串替换为 NULL。处理电子表格软件导出的数据时，此选项可能有用。

### Insert（插入） <a href="#insert" id="insert"></a>

此操作用于向表中插入行。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Postgres 凭据](../../credentials/postgres.md)。
- **Operation**（操作）：选择 **Insert**（插入）。
- **Schema**（模式）：选择包含目标表的模式。选择 **From list**（从列表）可在下拉列表中选择模式，选择 **By Name**（按名称）可输入模式名。
- **Table**（表）：选择要操作的表。选择 **From list**（从列表）可在下拉列表中选择表，选择 **By Name**（按名称）可输入表名。
- **Mapping Column Mode**（列映射模式）：如何将输入数据映射到列名：
    - **Map Each Column Manually**（手动映射每列）：选择每列使用的值。
    - **Map Automatically**（自动映射）：自动将输入数据映射到 Postgres 中匹配的列名。输入数据字段名必须与 Postgres 列名一致。必要时，可在此节点前使用 [Edit Fields (Set)](../../core-nodes/n8n-nodes-base.set.md)（编辑字段）节点调整格式。

#### 插入选项 <a href="#insert-options" id="insert-options"></a>

- **Connection Timeout**（连接超时）：尝试连接数据库的时间，单位为秒。
- **Delay Closing Idle Connection**（延迟关闭空闲连接）：空闲连接可被关闭前需要等待的秒数。
- **Query Batching**（查询批处理）：向数据库发送查询的方式：
    - **Single Query**（单个查询）：对所有输入数据项使用一个查询。
    - **Independently**（独立执行）：为本次执行中的每个输入数据项执行一个查询。
    - **Transaction**（事务）：在一个事务中执行所有查询。发生失败时，Postgres 回滚所有更改。
- **Output Columns**（输出列）：选择要输出的列，可从可用列列表选择，或使用[表达式](../../../../build/work-with-data/expressions-versus-data-nodes.md)指定 ID。
- **Output Large-Format Numbers As**（大数值输出格式）：`NUMERIC` 和 `BIGINT` 列的输出格式：
    - **Numbers**（数字）：用于常规数值。
    - **Text**（文本）：预计数字超过 16 位时使用，否则数字可能不准确。
- **Skip on Conflict**（冲突时跳过）：插入违反唯一约束或排除约束时，是否跳过该行，而非抛出错误。
- **Replace Empty Strings with NULL**（将空字符串替换为 NULL）：是否将输入中的空字符串替换为 NULL。处理电子表格软件导出的数据时，此选项可能有用。

### Insert or Update（插入或更新） <a href="#insert-or-update" id="insert-or-update"></a>

此操作用于插入或更新表中的行。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Postgres 凭据](../../credentials/postgres.md)。
- **Operation**（操作）：选择 **Insert or Update**（插入或更新）。
- **Schema**（模式）：选择包含目标表的模式。选择 **From list**（从列表）可在下拉列表中选择模式，选择 **By Name**（按名称）可输入模式名。
- **Table**（表）：选择要操作的表。选择 **From list**（从列表）可在下拉列表中选择表，选择 **By Name**（按名称）可输入表名。
- **Mapping Column Mode**（列映射模式）：如何将输入数据映射到列名：
    - **Map Each Column Manually**（手动映射每列）：选择每列使用的值。
    - **Map Automatically**（自动映射）：自动将输入数据映射到 Postgres 中匹配的列名。输入数据字段名必须与 Postgres 列名一致。必要时，可在此节点前使用 [Edit Fields (Set)](../../core-nodes/n8n-nodes-base.set.md)（编辑字段）节点调整格式。

#### 插入或更新选项 <a href="#insert-or-update-options" id="insert-or-update-options"></a>

- **Connection Timeout**（连接超时）：尝试连接数据库的时间，单位为秒。
- **Delay Closing Idle Connection**（延迟关闭空闲连接）：空闲连接可被关闭前需要等待的秒数。
- **Query Batching**（查询批处理）：向数据库发送查询的方式：
    - **Single Query**（单个查询）：对所有输入数据项使用一个查询。
    - **Independently**（独立执行）：为本次执行中的每个输入数据项执行一个查询。
    - **Transaction**（事务）：在一个事务中执行所有查询。发生失败时，Postgres 回滚所有更改。
- **Output Columns**（输出列）：选择要输出的列，可从可用列列表选择，或使用[表达式](../../../../build/work-with-data/expressions-versus-data-nodes.md)指定 ID。
- **Output Large-Format Numbers As**（大数值输出格式）：`NUMERIC` 和 `BIGINT` 列的输出格式：
    - **Numbers**（数字）：用于常规数值。
    - **Text**（文本）：预计数字超过 16 位时使用，否则数字可能不准确。
- **Replace Empty Strings with NULL**（将空字符串替换为 NULL）：是否将输入中的空字符串替换为 NULL。处理电子表格软件导出的数据时，此选项可能有用。

### Select（查询） <a href="#select" id="select"></a>

此操作用于查询表中的行。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Postgres 凭据](../../credentials/postgres.md)。
- **Operation**（操作）：选择 **Select**（查询）。
- **Schema**（模式）：选择包含目标表的模式。选择 **From list**（从列表）可在下拉列表中选择模式，选择 **By Name**（按名称）可输入模式名。
- **Table**（表）：选择要操作的表。选择 **From list**（从列表）可在下拉列表中选择表，选择 **By Name**（按名称）可输入表名。
- **Return All**（返回全部）：是否返回所有结果，或仅返回指定数量以内的结果。
- **Limit**（数量限制）：关闭 **Return All**（返回全部）时，返回的最大数据项数量。
- **Select Rows**（选择行）：通过 **Column**（列）、**Operator**（运算符）和 **Value**（值）设置行匹配条件。不设置条件时，Postgres 会查询所有行。
- **Combine Conditions**（组合条件）：如何组合 **Select Rows**（选择行）中的条件。**AND**（与）要求所有条件成立，**OR**（或）要求至少一个条件成立。
- **Sort**（排序）：选择结果行的排序方式。从列表或按 ID 选择 **Column**（列），并设置排序 **Direction**（方向）。

#### 查询选项 <a href="#select-options" id="select-options"></a>

- **Connection Timeout**（连接超时）：尝试连接数据库的时间，单位为秒。
- **Delay Closing Idle Connection**（延迟关闭空闲连接）：空闲连接可被关闭前需要等待的秒数。
- **Query Batching**（查询批处理）：向数据库发送查询的方式：
    - **Single Query**（单个查询）：对所有输入数据项使用一个查询。
    - **Independently**（独立执行）：为本次执行中的每个输入数据项执行一个查询。
    - **Transaction**（事务）：在一个事务中执行所有查询。发生失败时，Postgres 回滚所有更改。
- **Output Columns**（输出列）：选择要输出的列，可从可用列列表选择，或使用[表达式](../../../../build/work-with-data/expressions-versus-data-nodes.md)指定 ID。
- **Output Large-Format Numbers As**（大数值输出格式）：`NUMERIC` 和 `BIGINT` 列的输出格式：
    - **Numbers**（数字）：用于常规数值。
    - **Text**（文本）：预计数字超过 16 位时使用，否则数字可能不准确。

### Update（更新） <a href="#update" id="update"></a>

此操作用于更新表中的行。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Postgres 凭据](../../credentials/postgres.md)。
- **Operation**（操作）：选择 **Update**（更新）。
- **Schema**（模式）：选择包含目标表的模式。选择 **From list**（从列表）可在下拉列表中选择模式，选择 **By Name**（按名称）可输入模式名。
- **Table**（表）：选择要操作的表。选择 **From list**（从列表）可在下拉列表中选择表，选择 **By Name**（按名称）可输入表名。
- **Mapping Column Mode**（列映射模式）：如何将输入数据映射到列名：
    - **Map Each Column Manually**（手动映射每列）：选择每列使用的值。
    - **Map Automatically**（自动映射）：自动将输入数据映射到 Postgres 中匹配的列名。输入数据字段名必须与 Postgres 列名一致。必要时，可在此节点前使用 [Edit Fields (Set)](../../core-nodes/n8n-nodes-base.set.md)（编辑字段）节点调整格式。

#### 更新选项 <a href="#update-options" id="update-options"></a>

- **Connection Timeout**（连接超时）：尝试连接数据库的时间，单位为秒。
- **Delay Closing Idle Connection**（延迟关闭空闲连接）：空闲连接可被关闭前需要等待的秒数。
- **Query Batching**（查询批处理）：向数据库发送查询的方式：
    - **Single Query**（单个查询）：对所有输入数据项使用一个查询。
    - **Independently**（独立执行）：为本次执行中的每个输入数据项执行一个查询。
    - **Transaction**（事务）：在一个事务中执行所有查询。发生失败时，Postgres 回滚所有更改。
- **Output Columns**（输出列）：选择要输出的列，可从可用列列表选择，或使用[表达式](../../../../build/work-with-data/expressions-versus-data-nodes.md)指定 ID。
- **Output Large-Format Numbers As**（大数值输出格式）：`NUMERIC` 和 `BIGINT` 列的输出格式：
    - **Numbers**（数字）：用于常规数值。
    - **Text**（文本）：预计数字超过 16 位时使用，否则数字可能不准确。
- **Replace Empty Strings with NULL**（将空字符串替换为 NULL）：是否将输入中的空字符串替换为 NULL。处理电子表格软件导出的数据时，此选项可能有用。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-base.postgres 集成模板](https://n8n.io/integrations/postgres)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 提供 Postgres 触发器节点。更多信息，请参阅 [Postgres Trigger 节点文档](../../trigger-nodes/n8n-nodes-base.postgrestrigger.md)。

## 使用查询参数 <a href="#use-query-parameters" id="use-query-parameters"></a>

创建在 Postgres 数据库中运行的查询时，可通过 **Options**（选项）中的 **Query Parameters**（查询参数）字段将数据传入查询。n8n 会对查询参数中的数据进行安全处理，防止 SQL 注入。

例如，要根据邮箱地址查找某人。给定以下输入数据：

```js
[
    {
        "email": "alex@example.com",
        "name": "Alex",
        "age": 21 
    },
    {
        "email": "jamie@example.com",
        "name": "Jamie",
        "age": 33 
    }
]
```

可编写如下查询：

```sql
SELECT * FROM $1:name WHERE email = $2;
```

然后在 **Query Parameters**（查询参数）中提供要使用的字段值，可填写固定值或表达式。本例使用表达式，使节点依次从每个输入数据项中提取邮箱地址：

```js
// users is an example table name
{{ [ 'users', $json.email ] }} 
```

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见问题及建议的解决方法，请参阅[常见问题](common-issues.md)。
