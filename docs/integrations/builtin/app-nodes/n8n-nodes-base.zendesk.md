---
title: Zendesk 节点文档
description: 了解如何在 n8n 中使用 Zendesk 节点，并按照技术文档将 Zendesk 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Zendesk 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.zendesk.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zendesk
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zendesk
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Zendesk 节点 <a href="#zendesk-node" id="zendesk-node"></a>

使用 Zendesk 节点自动处理 Zendesk 中的工作，并将其与其他应用集成。n8n 内置支持多种 Zendesk 功能，包括创建和删除工单、用户及组织。

本页列出了 Zendesk 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Zendesk 凭据](../credentials/zendesk.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Ticket（工单）
    * Create a ticket（创建工单）
    * Delete a ticket（删除工单）
    * Get a ticket（获取工单）
    * Get all tickets（获取全部工单）
    * Recover a suspended ticket（恢复已暂停的工单）
    * Update a ticket（更新工单）
* Ticket Field（工单字段）
    * Get a ticket field（获取工单字段）
    * Get all system and custom ticket fields（获取全部系统和自定义工单字段）
* User（用户）
    * Create a user（创建用户）
    * Delete a user（删除用户）
    * Get a user（获取用户）
    * Get all users（获取全部用户）
    * Get a user's organizations（获取用户所属的组织）
    * Get data related to the user（获取用户相关数据）
    * Search users（搜索用户）
    * Update a user（更新用户）
* Organization（组织）
    * Create an organization（创建组织）
    * Delete an organization（删除组织）
    * Count organizations（统计组织数量）
    * Get an organization（获取组织）
    * Get all organizations（获取全部组织）
    * Get data related to the organization（获取组织相关数据）
    * Update a organization（更新组织）

{% hint style="warning" %}
**标签替换行为**

使用 Zendesk 节点的“Update Ticket”（更新工单）操作并指定 `Tag Names or IDs` 字段时，工单上的整个标签列表**会被替换**。由于 Zendesk API 默认处理标签更新的方式，未包含在更新中的任何标签都会从工单移除。

**避免意外移除标签的方法：**

- 先获取工单现有标签，与新标签合并后再更新。
- 也可通过 HTTP Request 节点使用 Zendesk 的 `additional_tags` 属性，添加标签而不移除已有标签。
- 还可调用工单的 `/tags` 端点，添加标签而不替换已有标签（[Zendesk 标签端点文档](https://developer.zendesk.com/api-reference/ticketing/ticket-management/tags/)）。

详细信息请参阅官方文档：[为工单添加标签而不覆盖已有标签](https://developer.zendesk.com/documentation/ticketing/managing-tickets/adding-tags-to-tickets-without-overwriting-existing-tags/)。
{% endhint %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Zendesk 集成模板](https://n8n.io/integrations/zendesk)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
