---
title: Data Table 节点
description: 了解 n8n 中 Data Table 节点的用法，并查看相关示例。
contentType:
- integration
- reference
priority: critical
tags:
- data table node
- data
hide:
- tags
search:
  boost: 1.5
nodeTitle: n8n-nodes-base.datatable
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.datatable/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Data Table（数据表） <a href="#data-table" id="data-table"></a>

使用 Data Table 节点创建和管理内部数据表。数据表可以将结构化数据直接存储在 n8n 内部，并在多个工作流之间使用。

Data Table 节点可以用于：

- 创建、列出和管理数据表
- 插入、更新、删除数据行，以及执行 upsert（存在则更新，否则插入）
- 根据匹配条件查询和检索数据行

{% hint style="info" %}
**使用数据表**

除了在工作流中使用 Data Tables 节点，还可在项目 **Overview**（概览）中的 **Data Tables**（数据表）标签页手动查看和管理数据表。

关于在此标签页中操作数据表，以及数据表的适用场景与限制，请参阅[数据表](../../../../build/work-with-data/data-tables.md)。
{% endhint %}

## 资源 <a href="#resources" id="resources"></a>

Data Table 节点支持以下资源：

- **Data Table:**（数据表）创建、列出、更新和删除表。
- **Row:**（数据行）插入、检索、更新、删除表内数据行，以及执行 upsert。

### 操作 <a href="#operations" id="operations"></a>

可用操作如下。不同操作类型的详细参数，请参阅[表操作](tables.md)和[行操作](rows.md)。

* **Rows**（数据行）
    * [**Delete:**](rows.md#delete-row)（删除）删除一行或多行。
    * [**Get:**](rows.md#get-row)（获取）根据筛选条件从表中获取一行或多行。
    * [**If Row Exists:**](rows.md#if-row-exists)（如果行存在）指定一组条件，匹配数据表中存在对应行的输入数据项。
    * [**If Row Does Not Exist:**](rows.md#if-row-does-not-exist)（如果行不存在）指定一组条件，匹配数据表中不存在对应行的输入数据项。
    * [**Insert:**](rows.md#insert-row)（插入）将数据行插入现有表。
    * [**Update:**](rows.md#update-row)（更新）更新一行或多行。
    * [**Upsert:**](rows.md#upsert-row)（存在则更新，否则插入）行存在时更新，否则创建新行。

* **Tables**（数据表）
    * [**Create:**](tables.md#create-a-data-table)（创建）创建新数据表。
    * [**Delete:**](tables.md#delete-a-data-table)（删除）删除现有数据表。
    * [**List:**](tables.md#list-data-tables)（列出）列出现有数据表。
    * [**Update:**](tables.md#update-a-data-table)（更新）更新现有数据表。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

[数据表](../../../../build/work-with-data/data-tables.md)介绍了如何创建和管理数据表。
