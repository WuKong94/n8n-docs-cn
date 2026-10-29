---
title: Grist 节点文档
description: 了解如何在 n8n 中使用 Grist 节点，并按照技术文档将 Grist 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Grist 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.grist.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.grist
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.grist
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Grist 节点 <a href="#grist-node" id="grist-node"></a>

使用 Grist 节点自动处理 Grist 中的工作，并将其与其他应用集成。n8n 内置支持多种 Grist 功能，包括创建、更新、删除和读取表中的行。

本页列出了 Grist 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Grist 凭据](../credentials/grist.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Create rows in a table（在表中创建行）
* Delete rows from a table（从表中删除行）
* Read rows from a table（读取表中的行）
* Update rows in a table（更新表中的行）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Grist 集成模板](https://n8n.io/integrations/grist)，或[搜索所有模板](https://n8n.io/workflows/)

## 获取行 ID <a href="#get-the-row-id" id="get-the-row-id"></a>

更新或删除特定记录时，需要行 ID。获取行 ID 有两种方式：

**在 Grist 中创建行 ID 列**

在 Grist 表中创建新列，并使用公式 `$id`。

**使用 Get All（获取全部）操作**

**Get All**（获取全部）操作会随字段一并返回每条记录的行 ID。
 
可通过表达式 `{{$("GristNodeName").item.json.id}}` 获取。


## 使用 Get All 操作时筛选记录 <a href="#filter-records-when-using-the-get-all-operation" id="filter-records-when-using-the-get-all-operation"></a>

- 选择 **Add Option**（添加选项），再从下拉菜单选择 **Filter**（筛选）。
- 可为任意数量的列添加筛选条件。结果仅包含与所有列条件都匹配的记录。
- 每列可输入任意数量的值，以逗号分隔。结果包含与该列任意一个值匹配的记录。

