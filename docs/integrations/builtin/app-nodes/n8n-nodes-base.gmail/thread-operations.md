---
title: Gmail 节点邮件线程操作文档
description: 了解如何在 n8n 中使用 Gmail 节点的邮件线程操作，并按照技术文档将这些操作集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: Gmail 节点邮件线程操作文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Gmail 节点邮件线程操作 <a href="#gmail-node-thread-operations" id="gmail-node-thread-operations"></a>

使用 Thread（邮件线程）操作删除或回复邮件线程、将其移至垃圾箱或恢复、添加或移除标签，以及获取单个线程或线程列表。有关 Gmail 节点本身的更多信息，请参阅 [Gmail 节点](README.md)。

## 为邮件线程添加标签 <a href="#add-label-to-a-thread" id="add-label-to-a-thread"></a>

此操作用于为邮件线程添加标签。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Thread**（邮件线程）。
* **Operation**（操作）：选择 **Add Label**（添加标签）。
* **Thread ID**（邮件线程 ID）：输入要添加标签的邮件线程 ID。
* **Label Names or IDs**（标签名称或 ID）：选择要应用的标签名称，或输入表达式指定 ID。下拉列表根据所选 **Credential**（凭据）填充。


更多信息，请参阅 [Gmail API 方法：users.threads.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/modify)文档。


## 删除邮件线程 <a href="#delete-a-thread" id="delete-a-thread"></a>

此操作用于立即永久删除邮件线程及其所有消息。

{% hint style="info" %}
**永久删除**

此操作无法撤销。如需可恢复的删除，请改用 [Trash（移至垃圾箱）操作](#trash-a-thread)。
{% endhint %}

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Thread**（邮件线程）。
* **Operation**（操作）：选择 **Delete**（删除）。
* **Thread ID**（邮件线程 ID）：输入要删除的邮件线程 ID。

更多信息，请参阅 [Gmail API 方法：users.threads.delete](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/delete)文档。

## 获取邮件线程 <a href="#get-a-thread" id="get-a-thread"></a>

此操作用于获取单个邮件线程。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Thread**（邮件线程）。
* **Operation**（操作）：选择 **Get**（获取）。
* **Thread ID**（邮件线程 ID）：输入要获取的邮件线程 ID。
* **Simplify**（简化）：开启时返回简化后的响应，关闭时返回原始数据。默认开启。
    * 这相当于将 API 调用的 `format` 设为 `metadata`，返回邮件 ID、标签和邮件头，包括 From（发件人）、To（收件人）、CC（抄送）、BCC（密送）及 Subject（主题）。

### 获取邮件线程的选项 <a href="#get-thread-options" id="get-thread-options"></a>

使用以下选项进一步调整节点行为：

* **Return Only Messages**（仅返回消息）：选择是否仅返回线程中的消息，开启表示仅返回消息。

更多信息，请参阅 [Gmail API 方法：users.threads.get](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/get)文档。


## 获取多个邮件线程 <a href="#get-many-threads" id="get-many-threads"></a>


此操作用于获取两个或更多邮件线程。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Thread**（邮件线程）。
* **Operation**（操作）：选择 **Get Many**（获取多项）。
* **Return All**（返回全部）：开启时返回所有邮件线程，关闭时仅返回设定数量以内的线程。
* **Limit**（数量限制）：输入返回邮件线程的最大数量，仅在关闭 **Return All**（返回全部）时使用。


### 获取多个邮件线程的筛选条件 <a href="#get-many-threads-filters" id="get-many-threads-filters"></a>


使用以下筛选条件进一步调整节点行为：

* **Include Spam and Trash**（包含垃圾邮件和垃圾箱）：选择是否获取 Spam（垃圾邮件）和 Trash（垃圾箱）文件夹中的邮件线程，开启表示包含，关闭表示不包含。
* **Label Names or IDs**（标签名称或 ID）：仅返回带有所选标签的邮件线程。选择要应用的标签名称，或输入表达式指定 ID。下拉列表根据所选 **Credential**（凭据）填充。
* **Search**（搜索）：输入 Gmail 搜索筛选条件，例如 `from:`，筛选返回的邮件线程。更多信息，请参阅[优化 Gmail 搜索](https://support.google.com/mail/answer/7190?hl=en)。
* **Read Status**（已读状态）：选择 **Unread and read emails**（未读及已读邮件）、**Unread emails only**（仅未读邮件，默认）或 **Read emails only**（仅已读邮件）。
* **Received After**（接收时间晚于）：仅返回指定日期和时间之后收到的邮件。通过日期选择器选择日期和时间，或输入表达式，将日期设为 ISO 格式字符串或毫秒时间戳。字符串格式的更多信息，请参阅 [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)。
* **Received Before**（接收时间早于）：仅返回指定日期和时间之前收到的邮件。通过日期选择器选择日期和时间，或输入表达式，将日期设为 ISO 格式字符串或毫秒时间戳。字符串格式的更多信息，请参阅 [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)。

更多信息，请参阅 [Gmail API 方法：users.threads.list](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/list)文档。

## 从邮件线程中移除标签 <a href="#remove-label-from-a-thread" id="remove-label-from-a-thread"></a>

此操作用于从邮件线程中移除标签。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Thread**（邮件线程）。
* **Operation**（操作）：选择 **Remove Label**（移除标签）。
* **Thread ID**（邮件线程 ID）：输入要移除标签的邮件线程 ID。
* **Label Names or IDs**（标签名称或 ID）：选择要移除的标签名称，或输入表达式指定其 ID。下拉列表根据所选 **Credential**（凭据）填充。


更多信息，请参阅 [Gmail API 方法：users.threads.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/modify)文档。


## 回复消息 <a href="#reply-to-a-message" id="reply-to-a-message"></a>

此操作用于回复消息。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Thread**（邮件线程）。
* **Operation**（操作）：选择 **Reply**（回复）。
* **Thread ID**（邮件线程 ID）：输入要回复的邮件线程 ID。
* **Message Snippet or ID**（消息摘要或 ID）：选择要回复的消息，或输入表达式指定其 ID。下拉列表根据所选 **Credential**（凭据）填充。
* 选择 **Email Type**（邮件类型），可选 **Text**（文本）或 **HTML**。
* **Message**（消息）：输入电子邮件正文。

### 回复选项 <a href="#reply-options" id="reply-options"></a>

使用以下选项进一步调整节点行为：

* **Attachments**（附件）：选择 **Add Attachment**（添加附件）。填写 **Attachment Field Name (in Input)**（输入中的附件字段名），指定输入节点中包含附件的字段。
    * 多个属性请用英文逗号分隔。
* **BCC**（密送）：输入一个或多个密送收件人的邮箱地址。多个地址用英文逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。
* **CC**（抄送）：输入一个或多个抄送收件人的邮箱地址。多个地址用英文逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。
* **Sender Name**（发件人名称）：输入希望收件人在邮件中看到的发件人名称。
* **Reply to Sender Only**（仅回复发件人）：选择回复所有人（关闭），或仅回复发件人（开启）。

更多信息，请参阅 [Gmail API 方法：users.messages.send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send)文档。

## 将邮件线程移至垃圾箱 <a href="#trash-a-thread" id="trash-a-thread"></a>

此操作用于将邮件线程及其所有消息移至垃圾箱。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Thread**（邮件线程）。
* **Operation**（操作）：选择 **Trash**（移至垃圾箱）。
* **Thread ID**（邮件线程 ID）：输入要移至垃圾箱的邮件线程 ID。

更多信息，请参阅 [Gmail API 方法：users.threads.trash](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/trash)文档。

## 从垃圾箱恢复邮件线程 <a href="#untrash-a-thread" id="untrash-a-thread"></a>

此操作用于从垃圾箱恢复邮件线程及其所有消息。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Thread**（邮件线程）。
* **Operation**（操作）：选择 **Untrash**（从垃圾箱恢复）。
* **Thread ID**（邮件线程 ID）：输入要从垃圾箱恢复的邮件线程 ID。

更多信息，请参阅 [Gmail API 方法：users.threads.untrash](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/untrash)文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误或问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。
