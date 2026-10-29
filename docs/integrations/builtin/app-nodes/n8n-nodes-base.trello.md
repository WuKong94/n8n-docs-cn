---
title: Trello 节点文档
description: 了解如何在 n8n 中使用 Trello 节点，并按照技术文档将 Trello 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Trello 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.trello.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.trello
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.trello
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Trello 节点 <a href="#trello-node" id="trello-node"></a>

使用 Trello 节点自动处理 Trello 中的工作，并将其与其他应用集成。n8n 内置支持多种 Trello 功能，包括创建和更新卡片，以及添加和移除成员。

本页列出了 Trello 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Trello 凭据](../credentials/trello.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Attachment（附件）
    * Create a new attachment for a card（为卡片创建新附件）
    * Delete an attachment（删除附件）
    * Get the data of an attachment（获取附件数据）
    * Returns all attachments for the card（返回卡片的所有附件）
* Board（看板）
    * Create a new board（创建新看板）
    * Delete a board（删除看板）
    * Get the data of a board（获取看板数据）
    * Update a board（更新看板）
* Board Member（看板成员）
    * Add（添加）
    * Get All（获取全部）
    * Invite（邀请）
    * Remove（移除）
* Card（卡片）
    * Create a new card（创建新卡片）
    * Delete a card（删除卡片）
    * Get the data of a card（获取卡片数据）
    * Update a card（更新卡片）
* Card Comment（卡片评论）
    * Create a comment on a card（在卡片上创建评论）
    * Delete a comment from a card（从卡片删除评论）
    * Update a comment on a card（更新卡片上的评论）
* Checklist（检查清单）
    * Create a checklist item（创建检查清单项）
    * Create a new checklist（创建新检查清单）
    * Delete a checklist（删除检查清单）
    * Delete a checklist item（删除检查清单项）
    * Get the data of a checklist（获取检查清单数据）
    * Returns all checklists for the card（返回卡片的所有检查清单）
    * Get a specific checklist on a card（获取卡片上的指定检查清单）
    * Get the completed checklist items on a card（获取卡片上已完成的检查清单项）
    * Update an item in a checklist on a card（更新卡片检查清单中的某一项）
* Label（标签）
    * Add a label to a card.（向卡片添加标签）
    * Create a new label（创建新标签）
    * Delete a label（删除标签）
    * Get the data of a label（获取标签数据）
    * Returns all labels for the board（返回看板的所有标签）
    * Remove a label from a card.（从卡片移除标签）
    * Update a label.（更新标签）
* List（列出）
    * Archive/Unarchive a list（归档或取消归档列表）
    * Create a new list（创建新列表）
    * Get the data of a list（获取列表数据）
    * Get all the lists（获取所有列表）
    * Get all the cards in a list（获取列表中的所有卡片）
    * Update a list（更新列表）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Trello 集成模板](https://n8n.io/integrations/trello)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

## 查找列表 ID <a href="#find-the-list-id" id="find-the-list-id"></a>

1. 打开包含该列表的 Trello 看板。
2. 如果列表中没有卡片，请先向列表添加一张卡片。
3. 打开卡片，在 URL 末尾添加 `.json`，按 Enter 键。
4. 在 JSON 文件中找到名为 `idList` 的字段。
5. 复制 `idList` 字段的内容，粘贴到 n8n 的 **List ID**（列表 ID）字段。






