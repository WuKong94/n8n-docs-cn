---
title: Gmail 节点标签操作文档
description: 了解如何在 n8n 中使用 Gmail 节点的标签操作，并按照技术文档将这些操作集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: Gmail 节点标签操作文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gmail/label-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/label-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/label-operations
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Gmail 节点标签操作 <a href="#gmail-node-label-operations" id="gmail-node-label-operations"></a>

使用 Label（标签）操作在 Gmail 中创建、删除或获取标签，以及列出标签。有关 Gmail 节点本身的更多信息，请参阅 [Gmail 节点](README.md)。

## 创建标签 <a href="#create-a-label" id="create-a-label"></a>

此操作用于创建新标签。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Label**（标签）。
* **Operation**（操作）：选择 **Create**（创建）。
* **Name**（名称）：输入标签的显示名称。

### 创建标签的选项 <a href="#create-label-options" id="create-label-options"></a>

使用以下选项进一步调整节点行为：

* **Label List Visibility**（标签列表可见性）：设置 Gmail 网页界面中该标签在标签列表中的可见性。可选：
    * **Hide**（隐藏）：不在标签列表中显示该标签。
    * **Show**（显示，默认）：在标签列表中显示该标签。
    * **Show if Unread**（存在未读消息时显示）：如果带有该标签的消息中存在未读消息，则显示该标签。
* **Message List Visibility**（消息列表可见性）：设置 Gmail 网页界面中带有该标签的消息在消息列表中的可见性。选择 **Show**（显示）或 **Hide**（隐藏）这些消息。

更多信息，请参阅 [Gmail API 方法：users.labels.create](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/create)文档。

## 删除标签 <a href="#delete-a-label" id="delete-a-label"></a>

此操作用于删除已有标签。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Label**（标签）。
* **Operation**（操作）：选择 **Delete**（删除）。
* **Label ID**（标签 ID）：输入要删除的标签 ID。

更多信息，请参阅 [Gmail API 方法：users.labels.delete](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/delete)文档。

## 获取标签 <a href="#get-a-label" id="get-a-label"></a>

此操作用于获取已有标签。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Label**（标签）。
* **Operation**（操作）：选择 **Get**（获取）。
* **Label ID**（标签 ID）：输入要获取的标签 ID。

更多信息，请参阅 [Gmail API 方法：users.labels.get](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/get)文档。


## 获取多个标签 <a href="#get-many-labels" id="get-many-labels"></a>


此操作用于获取两个或更多标签。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Label**（标签）。
* **Operation**（操作）：选择 **Get Many**（获取多项）。
* **Return All**（返回全部）：开启时返回所有标签，关闭时仅返回设定数量以内的标签。
* **Limit**（数量限制）：输入返回标签的最大数量，仅在关闭 **Return All**（返回全部）时使用。

更多信息，请参阅 [Gmail API 方法：users.labels.list](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/list)文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误或问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。
