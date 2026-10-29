---
title: Airtable 节点文档
description: 了解如何在 n8n 中使用 Airtable 节点，并按照技术文档将 Airtable 节点集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: n8n-nodes-base.airtable
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.airtable/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Airtable 节点 <a href="#airtable-node" id="airtable-node"></a>

使用 Airtable 节点自动处理 Airtable 中的工作，并将其与其他应用集成。n8n 内置支持多种 Airtable 功能，包括创建、读取、列出、更新和删除表中的数据。

本页列出了 Airtable 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Airtable 凭据](../../credentials/airtable.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* 向表中追加数据
* 从表中删除数据
* 列出表中的数据
* 读取表中的数据
* 更新表中的数据

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-base.airtable 集成模板](https://n8n.io/integrations/airtable)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 提供 Airtable 触发器节点。更多信息，请参阅 [Airtable Trigger 节点文档](../../trigger-nodes/n8n-nodes-base.airtabletrigger.md)。

有关该服务的更多信息，请参阅 [Airtable 文档](https://airtable.com/developers/web/api/introduction)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}


## 节点参考 <a href="#node-reference" id="node-reference"></a>

### 获取记录 ID <a href="#get-the-record-id" id="get-the-record-id"></a>

获取某条记录的数据需要记录 ID（Record ID）。可通过两种方式获取记录 ID。

### 在 Airtable 中创建记录 ID 列 <a href="#create-a-record-id-column-in-airtable" id="create-a-record-id-column-in-airtable"></a>

要在表中创建 `Record ID` 列，请参阅这篇[文章](https://support.airtable.com/docs/finding-airtable-ids)。之后即可在 Airtable 节点中使用该记录 ID。

### 使用 List（列出）操作 <a href="#use-the-list-operation" id="use-the-list-operation"></a>

可使用 Airtable 节点的 **List**（列出）操作获取记录 ID。此操作会同时返回记录 ID 和字段。之后即可在 Airtable 节点中使用该记录 ID。

### 使用 List（列出）操作时筛选记录 <a href="#filter-records-when-using-the-list-operation" id="filter-records-when-using-the-list-operation"></a>

要筛选 Airtable 数据库（base）中的记录，请使用 **Filter By Formula**（按公式筛选）选项。例如，要返回属于 `n8n` 组织的所有用户，请按以下步骤操作：

1. 在 **Operation**（操作）下拉列表中选择 List（列出）。
2. 在 **Base ID**（数据库 ID）和 **Table**（表）字段中，分别输入数据库 ID 和表名。
3. 点击 **Add Option**（添加选项），在下拉列表中选择 Filter By Formula（按公式筛选）。
4. 在 **Filter By Formula**（按公式筛选）字段中输入公式 `{Organization}='n8n'`。

同理，要返回不属于 `n8n` 组织的所有用户，请使用公式 `NOT({Organization}='n8n')`。

有关公式的更多信息，请参阅 Airtable [文档](https://support.airtable.com/docs/formula-field-reference)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误或问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。
