---
title: Gmail 节点草稿操作文档
description: 了解如何在 n8n 中使用 Gmail 节点的草稿操作，并按照技术文档将这些操作集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: Gmail 节点草稿操作文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Gmail 节点草稿操作 <a href="#gmail-node-draft-operations" id="gmail-node-draft-operations"></a>

使用 Draft（草稿）操作在 Gmail 中创建、删除或获取草稿，以及列出草稿。有关 Gmail 节点本身的更多信息，请参阅 [Gmail 节点](README.md)。

## 创建草稿 <a href="#create-a-draft" id="create-a-draft"></a>

此操作用于创建新草稿。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Draft**（草稿）。
* **Operation**（操作）：选择 **Create**（创建）。
* **Subject**（主题）：输入邮件主题。
* 选择 **Email Type**（邮件类型），可选 **Text**（文本）或 **HTML**。
* **Message**（消息）：输入电子邮件正文。

### 创建草稿的选项 <a href="#create-draft-options" id="create-draft-options"></a>

使用以下选项进一步调整节点行为：

* **Attachments**（附件）：选择 **Add Attachment**（添加附件）。填写 **Attachment Field Name (in Input)**（输入中的附件字段名），指定输入节点中包含附件的字段。
    * 多个属性请用英文逗号分隔。
* **BCC**（密送）：输入一个或多个密送收件人的邮箱地址。多个地址用英文逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。
* **CC**（抄送）：输入一个或多个抄送收件人的邮箱地址。多个地址用英文逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。
* **From Alias Name or ID**（发件人别名或 ID）：选择发送该草稿所用的别名。此字段根据参数中所选凭据填充。
* **Send Replies To**（回复地址）：输入用作回复地址的邮箱地址。
* **Thread ID**（邮件线程 ID）：如果希望将草稿附加到某个邮件线程，请输入该线程的 ID。
* **To Email**（收件人邮箱）：输入一个或多个收件人邮箱地址。多个地址用英文逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。

更多信息，请参阅 [Gmail API 方法：users.drafts.create](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/create)文档。

## 删除草稿 <a href="#delete-a-draft" id="delete-a-draft"></a>

此操作用于删除草稿。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Draft**（草稿）。
* **Operation**（操作）：选择 **Delete**（删除）。
* **Draft ID**（草稿 ID）：输入要删除的草稿 ID。

更多信息，请参阅 [Gmail API 方法：users.drafts.delete](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/delete)文档。

## 获取草稿 <a href="#get-a-draft" id="get-a-draft"></a>

此操作用于获取单个草稿。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Draft**（草稿）。
* **Operation**（操作）：选择 **Get**（获取）。
* **Draft ID**（草稿 ID）：输入要获取信息的草稿 ID。

### 获取草稿的选项 <a href="#get-draft-options" id="get-draft-options"></a>

使用以下选项进一步调整节点行为：

* **Attachment Prefix**（附件前缀）：输入节点写入附件时所用二进制属性名的前缀。n8n 会在前缀后添加从 `0` 开始的索引。例如，前缀为“attachment_”时，首个附件保存到“attachment_0”。
* **Download Attachments**（下载附件）：选择节点是否下载草稿的附件，开启表示下载，关闭表示不下载。

更多信息，请参阅 [Gmail API 方法：users.drafts.get](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/get)文档。


## 获取多个草稿 <a href="#get-many-drafts" id="get-many-drafts"></a>


此操作用于获取两个或更多草稿。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Draft**（草稿）。
* **Operation**（操作）：选择 **Get Many**（获取多项）。
* **Return All**（返回全部）：开启时返回所有草稿，关闭时仅返回设定数量以内的草稿。
* **Limit**（数量限制）：输入返回草稿的最大数量，仅在关闭 **Return All**（返回全部）时使用。


### 获取多个草稿的选项 <a href="#get-many-drafts-options" id="get-many-drafts-options"></a>


使用以下选项进一步调整节点行为：

* **Attachment Prefix**（附件前缀）：输入节点写入附件时所用二进制属性名的前缀。n8n 会在前缀后添加从 `0` 开始的索引。例如，前缀为“attachment_”时，首个附件保存到“attachment_0”。
* **Download Attachments**（下载附件）：选择节点是否下载草稿的附件，开启表示下载，关闭表示不下载。
* **Include Spam and Trash**（包含垃圾邮件和垃圾箱）：选择是否获取 Spam（垃圾邮件）和 Trash（垃圾箱）文件夹中的草稿，开启表示包含，关闭表示不包含。

更多信息，请参阅 [Gmail API 方法：users.drafts.list](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/list)文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误或问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。
