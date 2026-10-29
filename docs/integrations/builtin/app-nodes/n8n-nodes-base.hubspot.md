---
title: HubSpot 节点文档
description: 了解如何在 n8n 中使用 HubSpot 节点，并按照技术文档将 HubSpot 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: HubSpot 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.hubspot.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.hubspot
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.hubspot
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# HubSpot 节点 <a href="#hubspot-node" id="hubspot-node"></a>

使用 HubSpot 节点自动处理 HubSpot 中的工作，并将其与其他应用集成。n8n 内置支持多种 HubSpot 功能，包括创建、更新、删除和获取联系人、商机、列表、互动记录及公司。

本页列出了 HubSpot 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [HubSpot 凭据](../credentials/hubspot.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Contact（联系人）
    * Create/Update a contact（创建或更新联系人）
    * Delete a contact（删除联系人）
    * Get a contact（获取联系人）
    * Get all contacts（获取全部联系人）
    * Get recently created/updated contacts（获取最近创建或更新的联系人）
    * Search contacts（搜索联系人）
* Contact List（联系人列表）
    * Add contact to a list（将联系人添加到列表）
    * Remove a contact from a list（将联系人从列表移除）
* Company（公司）
    * Create a company（创建公司）
    * Delete a company（删除公司）
    * Get a company（获取公司）
    * Get all companies（获取全部公司）
    * Get recently created companies（获取最近创建的公司）
    * Get recently modified companies（获取最近修改的公司）
    * Search companies by domain（按域名搜索公司）
    * Update a company（更新公司）
* Deal（商机）
    * Create a deal（创建商机）
    * Delete a deal（删除商机）
    * Get a deal（获取商机）
    * Get all deals（获取全部商机）
    * Get recently created deals（获取最近创建的商机）
    * Get recently modified deals（获取最近修改的商机）
    * Search deals（搜索商机）
    * Update a deal（更新商机）
* Engagement（互动记录）
    * Create an engagement（创建互动记录）
    * Delete an engagement（删除互动记录）
    * Get an engagement（获取互动记录）
    * Get all engagements（获取全部互动记录）
* Form（表单）
    * Get all fields from a form（获取表单的全部字段）
    * Submit data to a form（向表单提交数据）
* Ticket（工单）
    * Create a ticket（创建工单）
    * Delete a ticket（删除工单）
    * Get a ticket（获取工单）
    * Get all tickets（获取全部工单）
    * Update a ticket（更新工单）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 HubSpot 集成模板](https://n8n.io/integrations/hubspot)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
