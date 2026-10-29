---
title: Autopilot 节点文档
description: 了解如何在 n8n 中使用 Autopilot 节点，并按照技术文档将 Autopilot 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Autopilot 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.autopilot.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.autopilot
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.autopilot
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Autopilot 节点 <a href="#autopilot-node" id="autopilot-node"></a>

使用 Autopilot 节点自动处理 Autopilot 中的工作，并将其与其他应用集成。n8n 内置支持多种 Autopilot 功能，包括创建、删除和更新联系人，以及将联系人加入列表。

本页列出了 Autopilot 节点支持的操作，并提供更多资源的链接。

{% hint style="warning" %}
**Autopilot 品牌变更**

Autopilot 已更名为 Ortto。Autopilot 凭据和节点仅兼容原 Autopilot，不兼容新的 Ortto API。
{% endhint %}
{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Autopilot 凭据](../credentials/autopilot.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Contact（联系人）
    * Create/Update a contact（创建或更新联系人）
    * Delete a contact（删除联系人）
    * Get a contact（获取联系人）
    * Get all contacts（获取全部联系人）
* Contact Journey（联系人旅程）
    * Add contact to list（将联系人添加到列表）
* Contact List（联系人列表）
    * Add contact to list（将联系人添加到列表）
    * Check if contact is on list（检查联系人是否在列表中）
    * Get all contacts on list（获取列表中的全部联系人）
    * Remove a contact from a list（从列表中移除联系人）
* List（列出）
    * Create a list（创建列表）
    * Get all lists（获取全部列表）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Autopilot 集成模板](https://n8n.io/integrations/autopilot)，或[搜索所有模板](https://n8n.io/workflows/)

