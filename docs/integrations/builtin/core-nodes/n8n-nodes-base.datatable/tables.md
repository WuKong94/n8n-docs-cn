---
title: Data Table 节点的表操作
description: Data Table 节点表操作的参考文档，包括创建、删除、列出和更新。
contentType:
- integration
- reference
priority: critical
nodeTitle: Data Table 节点的表操作
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.datatable/tables.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/tables
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/tables
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


使用表操作创建、删除、列出和更新数据表。有关节点本身的更多信息，请参阅 [Data Table 节点](README.md)文档。

## 创建数据表 <a href="#create-a-data-table" id="create-a-data-table"></a>

使用此操作创建新数据表。

配置以下参数：

- **Resource:**（资源）选择 **Table**（数据表）。
- **Operation:**（操作）选择 **Create**（创建）。
- **Name:**（名称）输入数据表名称，或使用表达式定义。
- **Columns:**（列）点击 **Add Column**（添加列），定义数据表列的参数。可以添加多列，每列配置如下：
    - **Name:**（名称）设置列名，或使用表达式定义。
    - **Type:**（类型）选择列的数据类型：**Boolean**（布尔值）、**Date**（日期）、**Number**（数字）或 **String**（字符串）。

### 创建数据表的选项 <a href="#create-a-data-table-options" id="create-a-data-table-options"></a>

使用以下选项进一步配置操作行为：

- **Reuse Existing Tables:**（复用现有表）开启后，如果已存在同名表，就返回该表，而不抛出错误。

## 删除数据表 <a href="#delete-a-data-table" id="delete-a-data-table"></a>

使用此操作永久删除现有数据表。此操作无法撤销。

配置以下参数：

- **Resource:**（资源）选择 **Table**（数据表）。
- **Operation:**（操作）选择 **Delete**（删除）。
- **Data table:**（数据表）选择如何指定要删除的数据表：
    - **From list:**（从列表选择）从所有数据表的下拉列表中选择。
    - **By Name:**（按名称）输入数据表名称。
    - **By ID:**（按 ID）输入数据表 ID。

## 列出数据表 <a href="#list-data-tables" id="list-data-tables"></a>

使用此操作列出现有数据表。可以返回全部表、按指定数量上限返回，或筛选要返回的表。

配置以下参数：

- **Resource:**（资源）选择 **Table**（数据表）。
- **Operation:**（操作）选择 **List**（列出）。
- **Return All:**（返回全部）开启时返回所有匹配的表；关闭时，在 **Limit**（数量上限）中输入要返回的表数量，例如 `50`。

### 列出数据表的选项 <a href="#list-data-tables-options" id="list-data-tables-options"></a>

使用以下选项进一步配置操作行为：

- **Filter by Name:**（按名称筛选）输入值或表达式，返回名称包含指定文本的数据表。匹配时不区分大小写。
- **Sort Field:**（排序字段）选择用于结果排序的字段。
- **Sort Direction:**（排序方向）选择按 **Ascending**（升序）或 **Descending**（降序）排列结果。

## 更新数据表 <a href="#update-a-data-table" id="update-a-data-table"></a>

使用此操作更新现有数据表的名称。

配置以下参数：

- **Resource:**（资源）选择 **Table**（数据表）。
- **Operation:**（操作）选择 **Update**（更新）。
- **Data table:**（数据表）选择如何指定要更新的数据表：
    - **From list:**（从列表选择）从所有数据表的下拉列表中选择。
    - **By Name:**（按名称）输入数据表名称。
    - **By ID:**（按 ID）输入数据表 ID。
- **New name:**（新名称）输入值或表达式，为数据表设置新名称。
