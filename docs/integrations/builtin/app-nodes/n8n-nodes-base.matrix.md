---
title: Matrix 节点文档
description: 了解如何在 n8n 中使用 Matrix 节点，并按照技术文档将 Matrix 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Matrix 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.matrix.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.matrix
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.matrix
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Matrix 节点 <a href="#matrix-node" id="matrix-node"></a>

使用 Matrix 节点自动处理 Matrix 中的工作，并将其与其他应用集成。n8n 内置支持多种 Matrix 功能，包括获取当前用户的账户信息、向聊天室发送媒体和消息，以及获取聊天室成员和消息。

本页列出了 Matrix 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Matrix 凭据](../credentials/matrix.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Account（账户）
    * Get current user's account information（获取当前用户的账户信息）
* Event（事件）
    * Get single event by ID（按 ID 获取单个事件）
* Media（媒体）
    * Send media to a chat room（向聊天室发送媒体）
* Message（消息）
    * Send a message to a room（向聊天室发送消息）
    * Gets all messages from a room（获取聊天室的全部消息）
* Room（聊天室）
    * New chat room with defined settings（按指定设置新建聊天室）
    * Invite a user to a room（邀请用户加入聊天室）
    * Join a new room（加入新聊天室）
    * Kick a user from a room（将用户移出聊天室）
    * Leave a room（离开聊天室）
* Room Member（聊天室成员）
    * Get all members（获取全部成员）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Matrix 集成模板](https://n8n.io/integrations/matrix)，或[搜索所有模板](https://n8n.io/workflows/)

