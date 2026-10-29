---
title: Postgres 节点常见问题
description: 了解 n8n 工作流自动化平台中 Postgres 节点的常见错误和问题，包括问题详情及建议的解决方法。
contentType:
- integration
- reference
priority: high
nodeTitle: Postgres 节点常见问题
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.postgres/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres/common-issues
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres/common-issues
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Postgres 节点常见问题 <a href="#postgres-node-common-issues" id="postgres-node-common-issues"></a>

以下介绍 [Postgres 节点](README.md)的常见错误和问题，以及解决或排查步骤。

## 使用参数动态填充 SQL `IN` 分组 <a href="#dynamically-populate-sql-in-groups-with-parameters" id="dynamically-populate-sql-in-groups-with-parameters"></a>

在 Postgres 中，可使用 SQL 的 [`IN` 比较结构](https://www.postgresql.org/docs/current/functions-comparisons.html#FUNCTIONS-COMPARISONS-IN-SCALAR)比较多组值：

```sql
SELECT color, shirt_size FROM shirts WHERE shirt_size IN ('small', 'medium', 'large');
```

虽然可以在查询中使用 n8n [表达式](../../../../build/work-with-data/expressions-versus-data-nodes.md)动态填充 `IN` 分组中的值，但结合[查询参数](README.md#use-query-parameters)可通过自动安全处理输入，提供额外保护。

要使用查询参数构建 `IN` 分组查询：

1. 将 **Operation**（操作）设为 **Execute Query**（执行查询）。
2. 在 **Options**（选项）中选择 **Query Parameters**（查询参数）。
3. 使用表达式选择输入数据中的数组，例如 `{{ $json.input_shirt_sizes }}`。
4. 在 **Query**（查询）参数中，使用带有空括号的 `IN` 结构编写查询。例如：
	```sql
	SELECT color, shirt_size FROM shirts WHERE shirt_size IN ();
	```
5. 在 `IN` 的括号内，使用表达式按照查询参数数组的元素数量动态生成索引占位符，例如 `$1`、`$2` 和 `$3`。由于占位符从 1 开始编号，可将每个数组索引加一：
	```sql
	SELECT color, shirt_size FROM shirts WHERE shirt_size IN ({{ $json.input_shirt_sizes.map((i, pos) => "$" + (pos+1)).join(', ') }});
	```

通过此方式，n8n 会根据数组的元素数量，为 `IN` 值自动生成对应数量的[预处理语句占位符](https://www.postgresql.org/docs/current/sql-prepare.html)。

## 处理时间戳和时区 <a href="#working-with-timestamps-and-time-zones" id="working-with-timestamps-and-time-zones"></a>

为避免 n8n 与 Postgres 对时间戳和时区数据的解释出现混淆，请遵循以下通用建议：

- **存储和传递日期时使用 UTC**：在不同表示方式和系统之间转换日期时，使用 UTC 可避免时区转换带来的混淆。
- **设置执行时区**：自托管 n8n 可通过[环境变量](../../../../deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-the-timezone.md)设置全局时区，n8n Cloud 可通过[设置](../../../../deploy/use-n8n-cloud/configure-cloud/set-your-timezone.md)配置。还可在[工作流设置](../../../../build/manage-workflows/configure-workflow-settings.md)中指定工作流时区。
- **使用 ISO 8601 格式**：[ISO 8601 格式](https://en.wikipedia.org/wiki/ISO_8601)将日、月、年、小时、分钟和秒编码为标准化字符串。n8n 在节点之间以字符串传递日期，并使用 [Luxon](../../../../build/work-with-data/handle-special-data-types/work-with-dates-and-times.md)解析。若需显式转换为 ISO 8601，可使用 [Date & Time 节点](../../core-nodes/n8n-nodes-base.datetime.md)，将自定义格式设为 `yyyy-MM-dd'T'HH:mm:ss`。

## 将 Date 列输出为日期字符串，而非 ISO 日期时间字符串 <a href="#outputting-date-columns-as-date-strings-instead-of-iso-datetime-strings" id="outputting-date-columns-as-date-strings-instead-of-iso-datetime-strings"></a>

n8n 使用 [`pg` 包](https://www.npmjs.com/package/pg)集成 Postgres，因此该包会影响 n8n 对 Postgres 日期、时间戳及相关类型的处理。

`pg` 包默认将 `DATE` 值解析为 `new Date(row_value)`，得到符合 [ISO 8601 日期时间字符串](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations)格式的日期。例如，日期 `2025-12-25` 可能产生日期时间字符串 `2025-12-25T23:00:00.000Z`，具体取决于实例的时区设置。

可在查询时使用 [Postgres 的 `TO_CHAR` 函数](https://www.postgresql.org/docs/current/functions-formatting.html#FUNCTIONS-FORMATTING)，将日期格式化为所需形式：

```sql
SELECT TO_CHAR(date_col, 'YYYY-MM-DD') AS date_col_as_date FROM table_with_date_col
```

这样会生成不含时间或时区部分的日期字符串。沿用前面的示例，日期 `2025-12-25` 经此转换后会得到字符串 `2025-12-25`。更多信息，请参阅 [`pg` 包关于日期的文档](https://node-postgres.com/features/types#date--timestamp--timestamptz)。
