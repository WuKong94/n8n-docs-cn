---
title: monday.com 节点文档
description: 了解如何在 n8n 中使用 monday.com 节点，并按照技术文档将 monday.com 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: monday.com 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.mondaycom.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# monday.com 节点 <a href="#mondaycom-node" id="mondaycom-node"></a>

使用 monday.com 节点自动处理 monday.com 中的工作，并将其与其他应用集成。n8n 内置支持多种 monday.com 功能，包括创建新看板，以及添加、删除和获取看板中的条目。

本页列出了 monday.com 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**功能可用范围**

从 n8n 1.22.6 起提供 monday.com 节点。
{% endhint %}

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [monday.com 凭据](../credentials/mondaycom.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Board（看板）
    * Archive a board（归档看板）
    * Create a new board（创建新看板）
    * Get a board（获取看板）
    * Get all boards（获取全部看板）
* Board Column（看板列）
    * Create a new column（创建新列）
    * Get all columns（获取全部列）
* Board Group（看板分组）
    * Delete a group in a board（删除看板中的分组）
    * Create a group in a board（在看板中创建分组）
    * Get list of groups in a board（获取看板的分组列表）
* Board Item（看板条目）
    * Add an update to an item.（为条目添加更新）
    * Change a column value for a board item（更改看板条目的某列值）
    * Change multiple column values for a board item（更改看板条目的多个列值）
    * Create an item in a board's group（在看板分组中创建条目）
    * Delete an item（删除数据项）
    * Get an item（获取数据项）
    * Get all items（获取全部数据项）
    * Get items by column value（按列值获取条目）
    * Move item to group（将条目移动到分组）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 monday.com 集成模板](https://n8n.io/integrations/mondaycom)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
