---
title: MySQL 节点文档
description: 了解如何在 n8n 中使用 MySQL 节点，并按照技术文档将 MySQL 节点集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: n8n-nodes-base.mysql
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.mysql/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MySQL 节点 <a href="#mysql-node" id="mysql-node"></a>

使用 MySQL 节点自动处理 MySQL 中的工作，并将其与其他应用集成。n8n 内置支持多种 MySQL 功能，包括执行 SQL 查询，以及插入和更新数据库中的行。

本页列出了 MySQL 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [MySQL 凭据](../../credentials/mysql.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Delete（删除）
* Execute SQL（执行 SQL）
* Insert（插入）
* Insert or Update（插入或更新）
* Select（查询）
* Update（更新）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-base.mysql 集成模板](https://n8n.io/integrations/mysql)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [MySQL 连接器与 API 文档](https://dev.mysql.com/doc/index-connectors.html)。

有关编写 SQL 查询的更多信息，请参阅 MySQL 的 [SELECT 语句文档](https://dev.mysql.com/doc/refman/8.4/en/select.html)。

## 使用查询参数 <a href="#use-query-parameters" id="use-query-parameters"></a>

创建在 MySQL 数据库中运行的查询时，可通过 **Options**（选项）中的 **Query Parameters**（查询参数）字段将数据传入查询。n8n 会对查询参数中的数据进行安全处理，防止 SQL 注入。

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
users, {{ $json.email }} 
```

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误或问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。
