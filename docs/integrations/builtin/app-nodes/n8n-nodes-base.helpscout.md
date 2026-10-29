---
title: Help Scout 节点文档
description: 了解如何在 n8n 中使用 Help Scout 节点，并按照技术文档将 Help Scout 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Help Scout 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.helpscout.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.helpscout
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.helpscout
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Help Scout 节点 <a href="#help-scout-node" id="help-scout-node"></a>

使用 Help Scout 节点自动处理 Help Scout 中的工作，并将其与其他应用集成。n8n 内置支持多种 Help Scout 功能，包括创建、更新、删除和获取会话及客户。

本页列出了 Help Scout 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Help Scout 凭据](../credentials/helpscout.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Conversation（会话）
    * Create a new conversation（创建会话）
    * Delete a conversation（删除会话）
    * Get a conversation（获取会话）
    * Get all conversations（获取全部会话）
* Customer（客户）
    * Create a new customer（创建新客户）
    * Get a customer（获取客户）
    * Get all customers（获取全部客户）
    * Get customer property definitions（获取客户属性定义）
    * Update a customer（更新客户）
* Mailbox（邮箱）
    * Get data of a mailbox（获取邮箱数据）
    * Get all mailboxes（获取全部邮箱）
* Thread（消息串）
    * Create a new chat thread（创建聊天消息串）
    * Get all chat threads（获取全部聊天消息串）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Help Scout 集成模板](https://n8n.io/integrations/helpscout)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
