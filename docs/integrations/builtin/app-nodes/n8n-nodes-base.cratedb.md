---
title: CrateDB 节点文档
description: 了解如何在 n8n 中使用 CrateDB 节点，并按照技术文档将 CrateDB 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: CrateDB 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.cratedb.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cratedb
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cratedb
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# CrateDB 节点 <a href="#cratedb-node" id="cratedb-node"></a>

使用 CrateDB 节点自动处理 CrateDB 中的工作，并将其与其他应用集成。n8n 内置支持多种 CrateDB 功能，包括在数据库中执行操作、插入和更新行。

本页列出了 CrateDB 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [CrateDB 凭据](../credentials/cratedb.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Execute an SQL query（执行 SQL 查询）
* Insert rows in database（向数据库插入行）
* Update rows in database（更新数据库中的行）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 CrateDB 集成模板](https://n8n.io/integrations/cratedb)，或[搜索所有模板](https://n8n.io/workflows/)

## 节点参考 <a href="#node-reference" id="node-reference"></a>

### 指定列的数据类型 <a href="#specify-a-columns-data-type" id="specify-a-columns-data-type"></a>

要指定列的数据类型，请在列名后附加 `:type`，其中 `type` 为所需的数据类型。例如，要将 **id** 列指定为 `int` 类型，将 **name** 列指定为 `text` 类型，可以在 **Columns（列）** 字段中填写：`id:int,name:text`。





