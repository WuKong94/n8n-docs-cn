---
title: Snowflake 节点文档
description: 了解如何在 n8n 中使用 Snowflake 节点，并按照技术文档将 Snowflake 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Snowflake 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.snowflake.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.snowflake
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.snowflake
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Snowflake 节点 <a href="#snowflake-node" id="snowflake-node"></a>

使用 Snowflake 节点自动处理 Snowflake 中的工作，并将其与其他应用集成。n8n 内置支持多种 Snowflake 功能，包括执行 SQL 查询和向数据库插入行。

本页列出了 Snowflake 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Snowflake 凭据](../credentials/snowflake.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Execute an SQL query.（执行 SQL 查询）
* Insert rows in database.（向数据库插入行）
* Update rows in database.（更新数据库中的行）

### 执行 SQL 查询 <a href="#execute-an-sql-query" id="execute-an-sql-query"></a>

在 Snowflake 上执行 SQL 查询时，可以使用参数化查询，将值安全地传入 SQL 语句。

#### 使用查询参数 <a href="#use-query-parameters" id="use-query-parameters"></a>

使用 **Options**（选项）中的 **Query Parameters**（查询参数）字段，为查询绑定值。n8n 会对查询参数中的数据进行安全处理，以防止 SQL 注入。

在 SQL 查询中，使用 `$1`、`$2`、`$3` 等占位符标记参数值的插入位置。例如：

```sql
SELECT * FROM users WHERE email = $1 AND status = $2;
```

然后在 **Query Parameters** 中提供要绑定的值，可以是固定值或表达式。使用表达式从输入数据项获取数据：

```js
{{ $json.email }}, {{ $json.status }}
```

各参数值用逗号分隔，第一个值绑定到 `$1`，第二个值绑定到 `$2`，依此类推。

{% hint style="warning" %}
**安全建议**

查询包含外部或不可信输入时，使用查询参数，不要将 `{{ }}` 表达式直接插入查询字符串。通过妥善处理参数值，可以防止 SQL 注入攻击。
{% endhint %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Snowflake 集成模板](https://n8n.io/integrations/snowflake)，或[搜索所有模板](https://n8n.io/workflows/)
