---
title: Twist 节点文档
description: 了解如何在 n8n 中使用 Twist 节点，并按照技术文档将 Twist 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Twist 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.twist.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.twist
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.twist
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Twist 节点 <a href="#twist-node" id="twist-node"></a>

使用 Twist 节点自动处理 Twist 中的工作，并将其与其他应用集成。n8n 内置支持多种 Twist 功能，包括在频道中创建会话，以及在讨论串中创建和删除评论。

本页列出了 Twist 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Twist 凭据](../credentials/twist.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Channel（频道）
    * Archive a channel（归档频道）
    * Initiates a public or private channel-based conversation（发起基于公开或私密频道的会话）
    * Delete a channel（删除频道）
    * Get information about a channel（获取频道信息）
    * Get all channels（获取全部频道）
    * Unarchive a channel（取消归档频道）
    * Update a channel（更新频道）
* Comment（评论）
    * Create a new comment to a thread（在讨论串中创建新评论）
    * Delete a comment（删除评论）
    * Get information about a comment（获取评论信息）
    * Get all comments（获取全部评论）
    * Update a comment（更新评论）
* Message Conversation（消息会话）
    * Create a message in a conversation（在会话中创建消息）
    * Delete a message in a conversation（删除会话中的消息）
    * Get a message in a conversation（获取会话中的消息）
    * Get all messages in a conversation（获取会话中的所有消息）
    * Update a message in a conversation（更新会话中的消息）
* Thread（讨论串）
    * Create a new thread in a channel（在频道中创建新讨论串）
    * Delete a thread（删除讨论串）
    * Get information about a thread（获取讨论串信息）
    * Get all threads（获取所有讨论串）
    * Update a thread（更新讨论串）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Twist 集成模板](https://n8n.io/integrations/twist)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

## 获取用户 ID <a href="#get-the-user-id" id="get-the-user-id"></a>

获取用户 ID 的步骤如下：

1. 打开 **Team**（团队）选项卡。
2. 选择用户头像。
3. 复制 Twist URL 中 `/u/` 后的字符串，该字符串就是用户 ID。例如，URL 为 `https://twist.com/a/4qw45/people/u/475370` 时，用户 ID 为 `475370`。

