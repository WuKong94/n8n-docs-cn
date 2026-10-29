---
title: Gmail 节点文档
contentType:
- integration
- reference
priority: high
nodeTitle: n8n-nodes-base.gmail
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gmail/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail
description: 了解如何在 n8n 中使用 Gmail 节点，并按照技术文档将 Gmail 节点集成到工作流中。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Gmail <a id="gmail"></a>

使用 Gmail 节点自动处理 Gmail 中的工作，并将其与其他应用集成。n8n 内置支持多种 Gmail 功能，包括创建、更新、删除和获取草稿、消息、标签及邮件线程。

本页列出了 Gmail 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Google 凭据](../../credentials/google/README.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* **Draft**（草稿）
  * [**Create**](draft-operations.md#create-a-draft)（创建）草稿
  * [**Delete**](draft-operations.md#delete-a-draft)（删除）草稿
  * [**Get**](draft-operations.md#get-a-draft)（获取）草稿
  * [**Get Many**](draft-operations.md#get-many-drafts)（获取多项）：获取多个草稿
* **Label**（标签）
  * [**Create**](label-operations.md#create-a-label)（创建）标签
  * [**Delete**](label-operations.md#delete-a-label)（删除）标签
  * [**Get**](label-operations.md#get-a-label)（获取）标签
  * [**Get Many**](label-operations.md#get-many-labels)（获取多项）：获取多个标签
* **Message**（消息）
  * [**Add Label**](message-operations.md#add-label-to-a-message)（添加标签）：为消息添加标签
  * [**Delete**](message-operations.md#delete-a-message)（删除）消息
  * [**Get**](message-operations.md#get-a-message)（获取）消息
  * [**Get Many**](message-operations.md#get-many-messages)（获取多项）：获取多个消息
  * [**Mark as Read**](message-operations.md#mark-as-read)（标记为已读）
  * [**Mark as Unread**](message-operations.md#mark-as-unread)（标记为未读）
  * [**Remove Label**](message-operations.md#remove-label-from-a-message)（移除标签）：从消息中移除标签
  * [**Reply**](message-operations.md#reply-to-a-message)（回复）消息
  * [**Send**](message-operations.md#send-a-message)（发送）消息
* **Thread**（邮件线程）
  * [**Add Label**](thread-operations.md#add-label-to-a-thread)（添加标签）：为邮件线程添加标签
  * [**Delete**](thread-operations.md#delete-a-thread)（删除）邮件线程
  * [**Get**](thread-operations.md#get-a-thread)（获取）邮件线程
  * [**Get Many**](thread-operations.md#get-many-threads)（获取多项）：获取多个邮件线程
  * [**Remove Label**](thread-operations.md#remove-label-from-a-thread)（移除标签）：从邮件线程中移除标签
  * [**Reply**](thread-operations.md#reply-to-a-message)（回复）消息
  * [**Trash**](thread-operations.md#trash-a-thread)（移至垃圾箱）邮件线程
  * [**Untrash**](thread-operations.md#untrash-a-thread)（从垃圾箱恢复）邮件线程

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Gmail 集成模板](https://n8n.io/integrations/gmail)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此节点所集成 API 的详细信息，请参阅 Google 的 [Gmail API 文档](https://developers.google.com/gmail/api)。

n8n 提供 Gmail 触发器节点。请参阅 [Gmail Trigger 节点文档](../../trigger-nodes/n8n-nodes-base.gmailtrigger/README.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误或问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。
