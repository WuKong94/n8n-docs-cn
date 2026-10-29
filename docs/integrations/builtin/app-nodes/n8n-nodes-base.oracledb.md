---
title: Oracle Database 节点文档
description: 了解如何在 n8n 中使用 Oracle Database 节点，并按照技术文档将 Oracle Database 节点集成到工作流中。
contentType:
- integration
- reference
priority: critical
nodeTitle: 应用节点
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.oracledb/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Oracle Database 节点 <a href="#oracle-database-node" id="oracle-database-node"></a>

使用 Oracle Database 节点自动处理 Oracle Database 中的工作，并将其与其他应用集成。n8n 内置支持多种 Oracle Database 功能，包括执行 SQL 语句，以及查询、插入、更新或删除数据。此节点内部使用 [node-oracledb 驱动](https://github.com/oracle/node-oracledb)。

本页列出了 Oracle Database 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
有关身份验证设置，请参阅 [Oracle Database 凭据](../credentials/oracledb.md)。

需要 Oracle Database **19c 或更高版本**。
使用透明应用连续性（TAC）和分片等 Oracle Database 高级功能时，还需要 Oracle Client Libraries **19c 或更高版本**。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* [**Delete**](#delete)（删除）：删除整张表或表中的行
* [**Execute SQL**](#execute-sql)（执行 SQL）：执行 SQL 语句
* [**Insert**](#insert)（插入）：向表中插入行
* [**Insert or Update**](#insert-or-update)（插入或更新）：插入或更新表中的行
* [**Select**](#select)（查询）：查询表中的行
* [**Update**](#update)（更新）：更新表中的行

### Delete（删除） <a href="#delete" id="delete"></a>

此操作用于删除整张表或表中的行。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Oracle Database 凭据](../credentials/oracledb.md)。
- **Operation**（操作）：选择 **Delete**（删除）。
- **Schema**（模式）：选择包含目标表的模式。选择 **From list**（从列表）可在下拉列表中选择模式，选择 **By Name**（按名称）可输入模式名。
- **Table**（表）：选择要操作的表。选择 **From list**（从列表）可在下拉列表中选择表，选择 **By Name**（按名称）可输入表名。
- **Command**（命令）：要执行的删除动作：
    - **Truncate**（清空表）：移除表中的数据，但保留表结构。
    - **Delete**（删除行）：删除满足 Select Rows（选择行）条件的行。不设置条件时，Oracle Database 会删除所有行。
        - **Select Rows**（选择行）：通过 **Column**（列）、**Operator**（运算符）和 **Value**（值）设置行匹配条件。值
          可通过表达式或字符串以 JSON 形式传入。
        - **Combine Conditions**（组合条件）：如何组合 Select Rows（选择行）中的条件。**AND**（与）要求所有条件成立，**OR**（或）要求至少一个条件成立。
    - **Drop**（删除表）：永久删除表的数据及结构。

#### 删除选项 <a href="#delete-options" id="delete-options"></a>

- **Auto Commit**（自动提交）：设为 true 时，在语句执行结束时自动提交当前连接中的事务。
- **Statement Batching**（语句批处理）：向数据库发送语句的方式：
    - **Single Statement**（单条语句）：对所有输入数据项使用一条语句。
    - **Independently**（独立执行）：为本次执行中的每个输入数据项执行一条语句。
    - **Transaction**（事务）：在一个事务中执行所有语句。发生失败时，Oracle Database 回滚所有更改。译注：普通表的 Truncate 和 Drop 会触发 DDL 隐式提交，不能依赖此选项回滚这些 DDL 操作。

### Execute SQL（执行 SQL） <a href="#execute-sql" id="execute-sql"></a>

此操作用于执行 SQL 语句。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Oracle Database 凭据](../credentials/oracledb.md)。
- **Operation**（操作）：执行 **Execute SQL**（执行 SQL）操作。
- **Statement**（语句）：要执行的 SQL 语句。可使用 n8n [表达式](../../../build/work-with-data/expressions-versus-data-nodes.md)和位置参数（如 `:1`、`:2`），或命名参数（如 `:name`、`:id`），配合[绑定参数](#use-bind-parameters)使用。
例如，要运行 PL/SQL 过程 `demo`，可使用：
```sql
BEGIN
  demo;
END;
```

#### 执行语句选项 <a href="#execute-statement-options" id="execute-statement-options"></a>

- **Auto Commit**（自动提交）：设为 true 时，在语句执行结束时自动提交当前连接中的事务。
- **Bind Variable Placeholder Values**（绑定变量占位符值）：输入语句中使用的绑定参数值，请参阅[使用绑定参数](#use-bind-parameters)。
- **Output Numbers As String**（将数字输出为字符串）：是否将数字作为字符串获取。
- **Fetch Array Size**（提取数组大小）：用于设置从 Oracle Database 获取查询行的内部缓冲区大小。修改此值可能影响查询性能，但不会改变返回给应用程序的行数。
- **Number of Rows to Prefetch**（预提取行数）：查询调优选项，用于设置底层 Oracle 驱动在查询内部初始语句执行阶段额外获取的行数。

### Insert（插入） <a href="#insert" id="insert"></a>

此操作用于向表中插入行。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Oracle Database 凭据](../credentials/oracledb.md)。
- **Operation**（操作）：选择 **Insert**（插入）。
- **Schema**（模式）：选择包含目标表的模式。选择 **From list**（从列表）可在下拉列表中选择模式，选择 **By Name**（按名称）可输入模式名。
- **Table**（表）：选择要操作的表。选择 **From list**（从列表）可在下拉列表中选择表，选择 **By Name**（按名称）可输入表名。
- **Mapping Column Mode**（列映射模式）：如何将输入数据映射到列名：
    - **Map Each Column Manually**（手动映射每列）：选择每列使用的值，请参阅[使用 n8n 表达式提供绑定值](#use-n8n-expressions-for-bind-values)。
    - **Map Automatically**（自动映射）：自动将输入数据映射到 Oracle Database 中匹配的列名。输入数据字段名必须与 Oracle Database 列名一致。必要时，可在此节点前使用 [Edit Fields (Set)](../core-nodes/n8n-nodes-base.set.md)（编辑字段）节点调整格式。

#### 插入选项 <a href="#insert-options" id="insert-options"></a>

- **Auto Commit**（自动提交）：设为 true 时，在语句执行结束时自动提交当前连接中的事务。
- **Output Columns**（输出列）：选择要输出的列，可从可用列列表选择，或使用[表达式](../../../build/work-with-data/expressions-versus-data-nodes.md)指定 ID。
- **Statement Batching**（语句批处理）：向数据库发送语句的方式：
    - **Single Statement**（单条语句）：对所有输入数据项使用一条语句。
    - **Independently**（独立执行）：为本次执行中的每个输入数据项执行一条语句。
    - **Transaction**（事务）：在一个事务中执行所有语句。发生失败时，Oracle Database 回滚所有更改。

### Insert or Update（插入或更新） <a href="#insert-or-update" id="insert-or-update"></a>

此操作用于插入或更新表中的行。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Oracle Database 凭据](../credentials/oracledb.md)。
- **Operation**（操作）：选择 **Insert or Update**（插入或更新）。
- **Schema**（模式）：选择包含目标表的模式。选择 **From list**（从列表）可在下拉列表中选择模式，选择 **By Name**（按名称）可输入模式名。
- **Table**（表）：选择要操作的表。选择 **From list**（从列表）可在下拉列表中选择表，选择 **By Name**（按名称）可输入表名。
- **Mapping Column Mode**（列映射模式）：如何将输入数据映射到列名：
    - **Map Each Column Manually**（手动映射每列）：选择每列使用的值，请参阅[使用 n8n 表达式提供绑定值](#use-n8n-expressions-for-bind-values)。
    - **Map Automatically**（自动映射）：自动将输入数据映射到 Oracle Database 中匹配的列名。输入数据字段名必须与 Oracle Database 列名一致。必要时，可在此节点前使用 [Edit Fields (Set)](../core-nodes/n8n-nodes-base.set.md)（编辑字段）节点调整格式。

#### 插入或更新选项 <a href="#insert-or-update-options" id="insert-or-update-options"></a>

- **Auto Commit**（自动提交）：设为 true 时，在语句执行结束时自动提交当前连接中的事务。
- **Output Columns**（输出列）：选择要输出的列，可从可用列列表选择，或使用[表达式](../../../build/work-with-data/expressions-versus-data-nodes.md)指定 ID。
- **Statement Batching**（语句批处理）：向数据库发送语句的方式：
    - **Single Statement**（单条语句）：对所有输入数据项使用一条语句。
    - **Independently**（独立执行）：为本次执行中的每个输入数据项执行一条语句。
    - **Transaction**（事务）：在一个事务中执行所有语句。发生失败时，Oracle Database 回滚所有更改。

### Select（查询） <a href="#select" id="select"></a>

此操作用于查询表中的行。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Oracle Database 凭据](../credentials/oracledb.md)。
- **Operation**（操作）：选择 **Select**（查询）。
- **Schema**（模式）：选择包含目标表的模式。选择 **From list**（从列表）可在下拉列表中选择模式，选择 **By Name**（按名称）可输入模式名。
- **Table**（表）：选择要操作的表。选择 **From list**（从列表）可在下拉列表中选择表，选择 **By Name**（按名称）可输入表名。
- **Return All**（返回全部）：是否返回所有结果，或仅返回指定数量以内的结果。
- **Limit**（数量限制）：关闭 **Return All**（返回全部）时，返回的最大数据项数量。
- **Select Rows**（选择行）：通过 **Column**（列）、**Operator**（运算符）和 **Value**（值，采用 `json`）设置行匹配条件。
**Value**（值）可因类型而异。例如，使用 Fixed（固定值）模式时：
    - 字符串："hello"、hellowithoutquotes、"hello with space"
    - 数字：12
    - JSON：{ "key": "val" }

不设置条件时，Oracle Database 会查询所有行。
- **Combine Conditions**（组合条件）：如何组合 **Select Rows**（选择行）中的条件。**AND**（与）要求所有条件成立，**OR**（或）要求至少一个条件成立。
- **Sort**（排序）：选择结果行的排序方式。从列表或按 ID 选择 **Column**（列），并设置排序 **Direction**（方向）。

#### 查询选项 <a href="#select-options" id="select-options"></a>

- **Auto Commit**（自动提交）：设为 true 时，在语句执行结束时自动提交当前连接中的事务。
- **Output Numbers As String**（将数字输出为字符串）：是否将数字作为字符串获取。
- **Fetch Array Size**（提取数组大小）：用于设置从 Oracle Database 获取查询行的内部缓冲区大小。修改此值可能影响查询性能，但不会改变返回给应用程序的行数。
- **Number of Rows to Prefetch**（预提取行数）：查询调优选项，用于设置底层 Oracle 驱动在查询内部初始语句执行阶段额外获取的行数。

### Update（更新） <a href="#update" id="update"></a>

此操作用于更新表中的行。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Oracle Database 凭据](../credentials/oracledb.md)。
- **Operation**（操作）：选择 **Update**（更新）。
- **Schema**（模式）：选择包含目标表的模式。选择 **From list**（从列表）可在下拉列表中选择模式，选择 **By Name**（按名称）可输入模式名。
- **Table**（表）：选择要操作的表。选择 **From list**（从列表）可在下拉列表中选择表，选择 **By Name**（按名称）可输入表名。
- **Mapping Column Mode**（列映射模式）：如何将输入数据映射到列名：
    - **Map Each Column Manually**（手动映射每列）：选择每列使用的值，请参阅[使用 n8n 表达式提供绑定值](#use-n8n-expressions-for-bind-values)。
    - **Map Automatically**（自动映射）：自动将输入数据映射到 Oracle Database 中匹配的列名。输入数据字段名必须与 Oracle Database 列名一致。必要时，可在此节点前使用 [Edit Fields (Set)](../core-nodes/n8n-nodes-base.set.md)（编辑字段）节点调整格式。

#### 更新选项 <a href="#update-options" id="update-options"></a>

- **Auto Commit**（自动提交）：设为 true 时，在语句执行结束时自动提交当前连接中的事务。
- **Output Columns**（输出列）：选择要输出的列，可从可用列列表选择，或使用[表达式](../../../build/work-with-data/expressions-versus-data-nodes.md)指定 ID。
- **Statement Batching**（语句批处理）：向数据库发送语句的方式：
    - **Single Statement**（单条语句）：对所有输入数据项使用一条语句。
    - **Independently**（独立执行）：为本次执行中的每个输入数据项执行一条语句。
    - **Transaction**（事务）：在一个事务中执行所有语句。发生失败时，Oracle Database 回滚所有更改。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [SQL 语言参考](https://www.oracle.com/pls/topic/lookup?ctx=dblatest&id=SQLRF)。

有关 node-oracledb 驱动的更多信息，请参阅 [node-oracledb 文档](https://node-oracledb.readthedocs.io/en/latest/)。

## 使用绑定参数 <a href="#use-bind-parameters" id="use-bind-parameters"></a>

创建在 Oracle 数据库实例中运行的语句时，可通过 **Options**（选项）中的 **Bind Variable Placeholder Values**（绑定变量占位符值）字段将数据传入语句。n8n 会对语句参数中的数据进行安全处理，防止 SQL 注入。

例如，要根据颜色查找特定水果。给定以下输入数据：

```js
[
    {
        "FRUIT_ID": 1,
        "FRUIT_NAME": "Apple",
        "COLOR": "Red" 
    },
    {
        "FRUIT_ID": 2,
        "FRUIT_NAME": "Banana",
        "COLOR": "Yellow"
    }
]
```

可编写如下语句：

```sql
SELECT * FROM FRUITS WHERE COLOR = :col
```

然后在 **Bind Variable Placeholder Values**（绑定变量占位符值）中提供要使用的字段值，可填写固定值或表达式。本例使用表达式，使节点依次从每个输入数据项中提取颜色。译注：原文 SQL 仅含 col 绑定占位符，输入字段为大写 COLOR；参数示例却额外包含 fruits 并引用小写 color。实际使用时，应使绑定值与占位符数量及输入字段大小写一致：

```js
// fruits is an example table name
fruits, {{ $json.color }} 
```

## 使用 n8n 表达式提供绑定值 <a href="#use-n8n-expressions-for-bind-values" id="use-n8n-expressions-for-bind-values"></a>

**Values to Send**（要发送的值）可使用 n8n 表达式。以下列出不同数据类型的示例，可输入常量，也可引用前序数据项的字段（`$json`）：

### JSON <a href="#json" id="json"></a>
- 常量：`{{ { k1: "v1", k2: "v2" } }}`
- 来自前序数据项：`{{ $json.COL_JSON }}`

### VECTOR（向量） <a href="#vector" id="vector"></a>
- 常量：`{{ [1, 2, 3, 4.5] }}`
- 来自前序数据项：`{{ $json.COL_VECTOR }}`

### BLOB（二进制大对象） <a href="#blob" id="blob"></a>
- 常量：`{{ [94, 87, 34] }}` 或 `{{ ' BLOB data string' }}`
- 来自前序数据项：`{{ $json.COL_BLOB }}`

### RAW（原始二进制） <a href="#raw" id="raw"></a>
- 常量：`{{ [94, 87, 34] }}`
- 来自前序数据项：`{{ $json.COL_RAW }}`

### BOOLEAN（布尔值） <a href="#boolean" id="boolean"></a>
- 常量：`{{ true }}`
- 来自前序数据项：`{{ $json.COL_BOOLEAN }}`

### NUMBER（数字） <a href="#number" id="number"></a>
- 常量：`1234`
- 来自前序数据项：`{{ $json.COL_NUMBER }}`

## VARCHAR（可变长字符串） <a href="#varchar" id="varchar"></a>
- 常量：`' Hello World '`
- 来自前序数据项：`{{ $json.COL_CHAR }}`

这些示例假设 JSON 键（例如 `COL_JSON, COL_VECTOR`）直接映射到对应的 SQL 列类型。
