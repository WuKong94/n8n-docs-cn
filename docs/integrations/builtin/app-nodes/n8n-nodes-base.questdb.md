---
title: QuestDB 节点文档
description: 了解如何在 n8n 中使用 QuestDB 节点，并按照技术文档将 QuestDB 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: QuestDB 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.questdb.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.questdb
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.questdb
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# QuestDB 节点 <a href="#questdb-node" id="questdb-node"></a>

使用 QuestDB 节点自动处理 QuestDB 中的工作，并将其与其他应用集成。n8n 支持通过 QuestDB 执行 SQL 查询，并向数据库插入行。

本页列出了 QuestDB 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [QuestDB 凭据](../credentials/questdb.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Executes a SQL query.（执行 SQL 查询）
* Insert rows in database.（向数据库插入行）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 QuestDB 集成模板](https://n8n.io/integrations/questdb)，或[搜索所有模板](https://n8n.io/workflows/)

## 节点参考 <a href="#node-reference" id="node-reference"></a>

### 指定列的数据类型 <a href="#specify-a-columns-data-type" id="specify-a-columns-data-type"></a>

要指定列的数据类型，请在列名后附加 `:type`，其中 `type` 是该列所需的数据类型。例如，为 **id** 列指定 `int` 类型、为 **name** 列指定 `text` 类型时，可在 **Columns**（列）字段中输入：`id:int,name:text`。





