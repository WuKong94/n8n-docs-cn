---
title: Wekan 节点文档
description: 了解如何在 n8n 中使用 Wekan 节点，并按照技术文档将 Wekan 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Wekan 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.wekan.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wekan
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wekan
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Wekan 节点 <a href="#wekan-node" id="wekan-node"></a>

使用 Wekan 节点自动处理 Wekan 中的工作，并将其与其他应用集成。n8n 内置支持多种 Wekan 功能，包括创建、更新、删除和获取看板及卡片。

本页列出了 Wekan 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Wekan 凭据](../credentials/wekan.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Board（看板）
    * Create a new board（创建新看板）
    * Delete a board（删除看板）
    * Get the data of a board（获取看板数据）
    * Get all user boards（获取用户的所有看板）
* Card（卡片）
    * Create a new card（创建新卡片）
    * Delete a card（删除卡片）
    * Get a card（获取卡片）
    * Get all cards（获取所有卡片）
    * Update a card（更新卡片）
* Card Comment（卡片评论）
    * Create a comment on a card（在卡片上创建评论）
    * Delete a comment from a card（从卡片删除评论）
    * Get a card comment（获取卡片评论）
    * Get all card comments（获取所有卡片评论）
* Checklist（检查清单）
    * Create a new checklist（创建新检查清单）
    * Delete a checklist（删除检查清单）
    * Get the data of a checklist（获取检查清单数据）
    * Returns all checklists for the card（返回卡片的所有检查清单）
* Checklist Item（检查清单项）
    * Delete a checklist item（删除检查清单项）
    * Get a checklist item（获取检查清单项）
    * Update a checklist item（更新检查清单项）
* List（列出）
    * Create a new list（创建新列表）
    * Delete a list（删除列表）
    * Get the data of a list（获取列表数据）
    * Get all board lists（获取看板的所有列表）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Wekan 集成模板](https://n8n.io/integrations/wekan)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

## 加载节点的所有参数 <a href="#load-all-the-parameters-for-the-node" id="load-all-the-parameters-for-the-node"></a>

要加载所有参数，例如 Author ID（作者 ID），需要为用户授予管理员权限。如何更改权限，请参阅 [Wekan 文档](https://github.com/wekan/wekan/wiki/Features#members-click-member-initials-or-avatar--permissions-adminnormalcomment-only)。

