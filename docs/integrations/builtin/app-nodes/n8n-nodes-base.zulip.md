---
title: Zulip 节点文档
description: 了解如何在 n8n 中使用 Zulip 节点，并按照技术文档将 Zulip 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Zulip 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.zulip.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zulip
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zulip
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Zulip 节点 <a href="#zulip-node" id="zulip-node"></a>

使用 Zulip 节点自动处理 Zulip 中的工作，并将其与其他应用集成。n8n 内置支持多种 Zulip 功能，包括创建、删除和获取用户与消息流，以及发送消息。

本页列出了 Zulip 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Zulip 凭据](../credentials/zulip.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Message（消息）
    * Delete a message（删除消息）
    * Get a message（获取消息）
    * Send a private message（发送私信）
    * Send a message to stream（向消息流发送消息）
    * Update a message（更新消息）
    * Upload a file（上传文件）
* Stream（消息流）
    * Create a stream.（创建消息流）
    * Delete a stream.（删除消息流）
    * Get all streams.（获取全部消息流）
    * Get subscribed streams.（获取已订阅的消息流）
    * Update a stream.（更新消息流）
* User（用户）
    * Create a user.（创建用户）
    * Deactivate a user.（停用用户）
    * Get a user.（获取用户）
    * Get all users.（获取全部用户）
    * Update a user.（更新用户）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Zulip 集成模板](https://n8n.io/integrations/zulip)，或[搜索所有模板](https://n8n.io/workflows/)
