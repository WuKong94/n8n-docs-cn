---
title: Mautic 节点文档
description: 了解如何在 n8n 中使用 Mautic 节点，并按照技术文档将 Mautic 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Mautic 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.mautic.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mautic
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mautic
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Mautic 节点 <a href="#mautic-node" id="mautic-node"></a>

使用 Mautic 节点自动处理 Mautic 中的工作，并将其与其他应用集成。n8n 内置支持多种 Mautic 功能，包括创建、更新、删除和获取公司及联系人，以及添加和移除营销活动联系人。

本页列出了 Mautic 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Mautic 凭据](../credentials/mautic.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Campaign Contact（营销活动联系人）
    * Add contact to a campaign（将联系人添加到营销活动）
    * Remove contact from a campaign（将联系人从营销活动移除）
* Company（公司）
    * Create a new company（创建新公司）
    * Delete a company（删除公司）
    * Get data of a company（获取公司的数据）
    * Get data of all companies（获取全部公司的数据）
    * Update a company（更新公司）
* Company Contact（公司联系人）
    * Add contact to a company（将联系人添加到公司）
    * Remove a contact from a company（将联系人从公司移除）
* Contact（联系人）
    * Create a new contact（创建新联系人）
    * Delete a contact（删除联系人）
    * Edit contact's points（编辑联系人的积分）
    * Add/remove contacts from/to the don't contact list（将联系人添加到禁止联系列表或从中移除）
    * Get data of a contact（获取联系人数据）
    * Get data of all contacts（获取全部联系人的数据）
    * Send email to contact（向联系人发送邮件）
    * Update a contact（更新联系人）
* Contact Segment（联系人细分群组）
    * Add contact to a segment（将联系人添加到细分群组）
    * Remove contact from a segment（将联系人从细分群组移除）
* Segment Email（细分群组邮件）
    * Send（发送）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Mautic 集成模板](https://n8n.io/integrations/mautic)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
