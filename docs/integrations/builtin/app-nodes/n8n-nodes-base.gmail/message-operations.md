---
title: Gmail 节点消息操作文档
description: 了解如何在 n8n 中使用 Gmail 节点的消息操作，并按照技术文档将这些操作集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: Gmail 节点消息操作文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Gmail 节点消息操作 <a href="#gmail-node-message-operations" id="gmail-node-message-operations"></a>

使用 Message（消息）操作在 Gmail 中发送、回复、删除消息，将消息标记为已读或未读，为消息添加或移除标签，以及获取单个消息或消息列表。有关 Gmail 节点本身的更多信息，请参阅 [Gmail 节点](README.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/hitl-tools.md" %}

## 为消息添加标签 <a href="#add-label-to-a-message" id="add-label-to-a-message"></a>

此操作用于为消息添加一个或多个标签。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Add Label**（添加标签）。
* **Message ID**（消息 ID）：输入要添加标签的消息 ID。
* **Label Names or IDs**（标签名称或 ID）：选择要添加的标签名称，或输入表达式指定 ID。下拉列表根据所选 **Credential**（凭据）填充。


更多信息，请参阅 [Gmail API 方法：users.messages.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify)文档。


## 删除消息 <a href="#delete-a-message" id="delete-a-message"></a>

此操作用于立即永久删除消息。

{% hint style="info" %}
**永久删除**

此操作无法撤销。如需可恢复的删除，请改用[邮件线程的 Trash（移至垃圾箱）操作](thread-operations.md#trash-a-thread)。
{% endhint %}

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Delete**（删除）。
* **Message ID**（消息 ID）：输入要删除的消息 ID。

更多信息，请参阅 [Gmail API 方法：users.messages.delete](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/delete)文档。

## 获取消息 <a href="#get-a-message" id="get-a-message"></a>

此操作用于获取单个消息。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Get**（获取）。
* **Message ID**（消息 ID）：输入要获取的消息 ID。
* **Simplify**（简化）：开启时返回简化后的响应，关闭时返回原始数据。默认开启。
    * 这相当于将 API 调用的 `format` 设为 `metadata`，返回邮件 ID、标签和邮件头，包括 From（发件人）、To（收件人）、CC（抄送）、BCC（密送）及 Subject（主题）。

更多信息，请参阅 [Gmail API 方法：users.messages.get](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/get)文档。


## 获取多个消息 <a href="#get-many-messages" id="get-many-messages"></a>


此操作用于获取两个或更多消息。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Get Many**（获取多项）。
* **Return All**（返回全部）：开启时返回所有消息，关闭时仅返回设定数量以内的消息。
* **Limit**（数量限制）：输入返回消息的最大数量，仅在关闭 **Return All**（返回全部）时使用。
* **Simplify**（简化）：开启时返回简化后的响应，关闭时返回原始数据。默认开启。
    * 这相当于将 API 调用的 `format` 设为 `metadata`，返回邮件 ID、标签和邮件头，包括 From（发件人）、To（收件人）、CC（抄送）、BCC（密送）及 Subject（主题）。


### 获取多个消息的筛选条件 <a href="#get-many-messages-filters" id="get-many-messages-filters"></a>


使用以下筛选条件进一步调整节点行为：

* **Include Spam and Trash**（包含垃圾邮件和垃圾箱）：选择是否获取 Spam（垃圾邮件）和 Trash（垃圾箱）文件夹中的消息，开启表示包含，关闭表示不包含。
* **Label Names or IDs**（标签名称或 ID）：仅返回带有所选标签的消息。选择要应用的标签名称，或输入表达式指定 ID。下拉列表根据所选 **Credential**（凭据）填充。
* **Search**（搜索）：输入 Gmail 搜索筛选条件，例如 `from:`，筛选返回的消息。更多信息，请参阅[优化 Gmail 搜索](https://support.google.com/mail/answer/7190?hl=en)。
* **Read Status**（已读状态）：选择 **Unread and read emails**（未读及已读邮件）、**Unread emails only**（仅未读邮件，默认）或 **Read emails only**（仅已读邮件）。
* **Received After**（接收时间晚于）：仅返回指定日期和时间之后收到的邮件。通过日期选择器选择日期和时间，或输入表达式，将日期设为 ISO 格式字符串或毫秒时间戳。字符串格式的更多信息，请参阅 [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)。
* **Received Before**（接收时间早于）：仅返回指定日期和时间之前收到的邮件。通过日期选择器选择日期和时间，或输入表达式，将日期设为 ISO 格式字符串或毫秒时间戳。字符串格式的更多信息，请参阅 [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)。
* **Sender**（发件人）：输入邮箱地址或发件人姓名的一部分，仅返回该发件人的消息。

更多信息，请参阅 [Gmail API 方法：users.messages.list](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/list)文档。

## 标记为已读 <a href="#mark-as-read" id="mark-as-read"></a>

此操作用于将消息标记为已读。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Mark as Read**（标记为已读）。
* **Message ID**（消息 ID）：输入要标记为已读的消息 ID。


更多信息，请参阅 [Gmail API 方法：users.messages.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify)文档。


## 标记为未读 <a href="#mark-as-unread" id="mark-as-unread"></a>

此操作用于将消息标记为未读。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Mark as Unread**（标记为未读）。
* **Message ID**（消息 ID）：输入要标记为未读的消息 ID。


更多信息，请参阅 [Gmail API 方法：users.messages.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify)文档。


## 从消息中移除标签 <a href="#remove-label-from-a-message" id="remove-label-from-a-message"></a>

此操作用于从消息中移除一个或多个标签。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Remove Label**（移除标签）。
* **Message ID**（消息 ID）：输入要移除标签的消息 ID。
* **Label Names or IDs**（标签名称或 ID）：选择要移除的标签名称，或输入表达式指定 ID。下拉列表根据所选 **Credential**（凭据）填充。


更多信息，请参阅 [Gmail API 方法：users.messages.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify)文档。


## 回复消息 <a href="#reply-to-a-message" id="reply-to-a-message"></a>

此操作用于发送消息，以回复已有消息。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Reply**（回复）。
* **Message ID**（消息 ID）：输入要回复的消息 ID。
* 选择 **Email Type**（邮件类型），可选 **Text**（文本）或 **HTML**。
* **Message**（消息）：输入电子邮件正文。

### 回复选项 <a href="#reply-options" id="reply-options"></a>

使用以下选项进一步调整节点行为：

* **Append n8n attribution**（附加 n8n 标识）：默认情况下，节点会在邮件末尾附加 `This email was sent automatically with n8n` 声明。关闭此选项即可移除。
* **Attachments**（附件）：选择 **Add Attachment**（添加附件）。填写 **Attachment Field Name (in Input)**（输入中的附件字段名），指定输入节点中包含附件的字段。
    * 多个属性请用英文逗号分隔。
* **BCC**（密送）：输入一个或多个密送收件人的邮箱地址。多个地址用英文逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。
* **CC**（抄送）：输入一个或多个抄送收件人的邮箱地址。多个地址用英文逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。
* **Sender Name**（发件人名称）：输入希望收件人在邮件中看到的发件人名称。
* **Reply to Sender Only**（仅回复发件人）：选择回复所有人（关闭），或仅回复发件人（开启）。

更多信息，请参阅 [Gmail API 方法：users.messages.send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send)文档。

## 发送消息 <a href="#send-a-message" id="send-a-message"></a>

此操作用于发送消息。

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Send**（发送）。
* **To**（收件人）：输入要发送邮件的目标邮箱地址。
* **Subject**（主题）：输入邮件主题。
* 选择 **Email Type**（邮件类型），可选 **Text**（文本）或 **HTML**。
* **Message**（消息）：输入电子邮件正文。

### 发送选项 <a href="#send-options" id="send-options"></a>

使用以下选项进一步调整节点行为：

* **Append n8n attribution**（附加 n8n 标识）：默认情况下，节点会在邮件末尾附加 `This email was sent automatically with n8n` 声明。关闭此选项即可移除。
* **Attachments**（附件）：选择 **Add Attachment**（添加附件）。填写 **Attachment Field Name (in Input)**（输入中的附件字段名），指定输入节点中包含附件的字段。
    * 多个属性请用英文逗号分隔。
* **BCC**（密送）：输入一个或多个密送收件人的邮箱地址。多个地址用英文逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。
* **CC**（抄送）：输入一个或多个抄送收件人的邮箱地址。多个地址用英文逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。
* **Sender Name**（发件人名称）：输入希望收件人在邮件中看到的发件人名称。
* **Send Replies To**（回复地址）：输入用作回复地址的邮箱地址。
* **Reply to Sender Only**（仅回复发件人）：选择回复所有人（关闭），或仅回复发件人（开启）。

更多信息，请参阅 [Gmail API 方法：users.messages.send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send)文档。

## 发送消息并等待审批 <a href="#send-a-message-and-wait-for-approval" id="send-a-message-and-wait-for-approval"></a>

此操作用于发送消息，并在继续执行工作流前等待收件人审批。

{% hint style="info" %}
**复杂审批请使用 Wait 节点**

**Send and Wait for Approval**（发送并等待审批）操作适用于简单审批流程。对于更复杂的审批，可考虑使用 [Wait 节点](../../core-nodes/n8n-nodes-base.wait.md)。
{% endhint %}

填写以下参数：

* 选择 **Credential to connect with**（连接所用凭据），或创建新凭据。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Send and Wait for Approval**（发送并等待审批）。
* **To**（收件人）：输入要发送邮件的目标邮箱地址。
* **Subject**（主题）：输入邮件主题。
* **Message**（消息）：输入电子邮件正文。

### 发送并等待审批的选项 <a href="#send-and-wait-for-approval-options" id="send-and-wait-for-approval-options"></a>

使用以下选项进一步调整节点行为：

* **Type of Approval**（审批类型）：选择 **Approve Only**（仅批准，默认）时，只包含批准按钮；选择 **Approve and Disapprove**（批准和拒绝）时，还会包含拒绝选项。
* **Approve Button Label**（批准按钮文字）：批准按钮使用的文字，默认为 **Approve**。
* **Approve Button Style**（批准按钮样式）：选择 **Primary**（主要，默认）或 **Secondary**（次要）按钮样式。
* **Disapprove Button Label**（拒绝按钮文字）：拒绝按钮使用的文字，默认为 **Decline**。仅在 **Type of Approval**（审批类型）设为 **Approve and Disapprove**（批准和拒绝）时显示。
* **Disapprove Button Style**（拒绝按钮样式）：选择 **Primary**（主要）或 **Secondary**（次要，默认）按钮样式。仅在 **Type of Approval**（审批类型）设为 **Approve and Disapprove**（批准和拒绝）时显示。

更多信息，请参阅 [Gmail API 方法：users.messages.send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send)文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误或问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。
