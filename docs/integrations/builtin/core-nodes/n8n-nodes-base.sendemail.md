---
title: Send Email 节点
contentType:
- integration
- reference
priority: high
nodeTitle: Send Email 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.sendemail.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail
description: 了解 n8n 中 Send Email 节点的用法，并查看相关示例。
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


# Send Email（发送邮件） <a id="send-email"></a>

Send Email 节点通过 SMTP 邮件服务器发送电子邮件。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Send Email 凭据文档](../credentials/send-email/README.md)。
{% endhint %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

使用以下参数配置节点。

### Credential to connect with（连接凭据） <a href="#credential-to-connect-with" id="credential-to-connect-with"></a>

选择或创建供节点使用的 [SMTP 账户凭据](../credentials/send-email/README.md)。

### Operation（操作） <a href="#operation" id="operation"></a>

Send Email 节点支持以下操作：

* **Send**（发送）：发送电子邮件。
* **Send and Wait for Response**（发送并等待响应）：发送邮件并等待接收方响应。此操作会暂停工作流执行，直到用户提交响应。

选择 **Send and Wait for Response**（发送并等待响应）会启用[等待响应](n8n-nodes-base.sendemail.md#waiting-for-a-response)中介绍的参数和选项。

### From Email（发件人邮箱） <a href="#from-email" id="from-email"></a>

输入用于发送邮件的邮箱地址，也可按 `Name Name <email@sample.com>` 格式包含名称，例如 `Nathan Doe <nate@n8n.io>`。

### To Email（收件人邮箱） <a href="#to-email" id="to-email"></a>

输入接收邮件的邮箱地址，也可按 `Name Name <email@sample.com>` 格式包含名称，例如 `Nathan Doe <nate@n8n.io>`。多个地址以逗号分隔，例如 `first@sample.com, "Name" <second@sample.com>`。

{% hint style="info" %}
**邮箱地址格式**

此邮箱地址格式也适用于 CC 和 BCC 字段。
{% endhint %}

### Subject（主题） <a href="#subject" id="subject"></a>

输入邮件主题。

### Email Format（邮件格式） <a href="#email-format" id="email-format"></a>

选择发送邮件的格式。此参数仅在 **Send**（发送）操作中可用，可选：

* **Text**（文本）：以纯文本格式发送邮件。
* **HTML**：以 HTML 格式发送邮件。
* **Both**（两种格式）：同时发送两种格式，由接收方的邮件客户端决定显示哪种格式。

## 节点选项 <a href="#node-options" id="node-options"></a>

使用以下 **Options**（选项）进一步配置节点行为。

### Append n8n Attribution（附加 n8n 署名） <a href="#append-n8n-attribution" id="append-n8n-attribution"></a>

开启时，在邮件末尾附加 `This email was sent automatically with n8n`；关闭时，不附加。

### Attachments（附件） <a href="#attachments" id="attachments"></a>

输入包含附件数据的二进制属性名称。使用此选项时：

* 使用 [Read/Write Files from Disk](n8n-nodes-base.readwritefile.md) 或 [HTTP Request](n8n-nodes-base.httprequest/README.md) 节点，将文件载入工作流。
* 输入以逗号分隔的二进制属性列表，可添加多个附件。
* 可在邮件正文中引用内嵌图片或其他内容，例如 `<img src="cid:image_1">`。

### CC Email（抄送邮箱） <a href="#cc-email" id="cc-email"></a>

输入 `cc:` 字段的邮箱地址。

### BCC Email（密送邮箱） <a href="#bcc-email" id="bcc-email"></a>

输入 `bcc:` 字段的邮箱地址。

### Ignore SSL Issues（忽略 SSL 问题） <a href="#ignore-ssl-issues" id="ignore-ssl-issues"></a>

开启时，n8n 忽略 TLS/SSL 证书验证失败；关闭时，强制执行证书验证。

### Reply To（回复地址） <a href="#reply-to" id="reply-to"></a>

输入 Reply To（回复地址）字段的邮箱地址。

## 等待响应 <a href="#waiting-for-a-response" id="waiting-for-a-response"></a>

选择 **Send and Wait for a Response**（发送并等待响应），可发送电子邮件并暂停工作流执行，直到有人确认操作或提供更多信息。

### Response Type（响应类型） <a href="#response-type" id="response-type"></a>

选择以下等待和审批类型之一：

* **Approval**（审批）：用户可在消息中批准或拒绝。
* **Free Text**（自由文本）：用户通过表单提交响应。
* **Custom Form**（自定义表单）：用户通过自定义表单提交响应。

可用选项取决于所选类型。

### Approval（审批）参数和选项 <a href="#approval-parameters-and-options" id="approval-parameters-and-options"></a>

使用 Approval（审批）响应类型时，可用以下选项：

* **Type of Approval**（审批类型）：选择仅显示批准按钮，或同时显示批准和拒绝按钮。
* **Button Label**（按钮标签）：批准或拒绝按钮的标签，默认分别为 `Approve` 和 `Decline`。
* **Button Style**（按钮样式）：按钮的 primary（主要）或 secondary（次要）样式。

此模式还提供以下选项：

* **Limit Wait Time**（限制等待时间）：设置工作流是否在指定时间限制后自动恢复执行，可使用时间间隔或具体时间点。
* **Append n8n Attribution**（附加 n8n 署名）：开启时，在邮件末尾附加 `This email was sent automatically with n8n`；关闭时，不附加。

### Free Text（自由文本）参数和选项 <a href="#free-text-parameters-and-options" id="free-text-parameters-and-options"></a>

使用 Free Text（自由文本）响应类型时，可用以下选项：

* **Message Button Label**（消息按钮标签）：消息中的按钮标签，默认为 `Respond`。
* **Response Form Title**（响应表单标题）：供用户提供响应的表单标题。
* **Response Form Description**（响应表单说明）：供用户提供响应的表单说明。
* **Response Form Button Label**（响应表单按钮标签）：提交表单响应的按钮标签，默认为 `Submit`。
* **Limit Wait Time**（限制等待时间）：设置工作流是否在指定时间限制后自动恢复执行，可使用时间间隔或具体时间点。
* **Append n8n Attribution**（附加 n8n 署名）：开启时，在邮件末尾附加 `This email was sent automatically with n8n`；关闭时，不附加。

### Custom Form（自定义表单）参数和选项 <a href="#custom-form-parameters-and-options" id="custom-form-parameters-and-options"></a>

使用 Custom Form（自定义表单）响应类型时，可使用所需字段和选项构建表单。

可按 [n8n Form 触发器的表单元素](n8n-nodes-base.formtrigger.md#form-elements)设置来自定义每个元素。要添加更多字段，选择 **Add Form Element**（添加表单元素）。

还可使用以下选项：

* **Message Button Label**（消息按钮标签）：消息中的按钮标签，默认为 `Respond`。
* **Response Form Title**（响应表单标题）：供用户提供响应的表单标题。
* **Response Form Description**（响应表单说明）：供用户提供响应的表单说明。
* **Response Form Button Label**（响应表单按钮标签）：提交表单响应的按钮标签，默认为 `Submit`。
* **Limit Wait Time**（限制等待时间）：设置工作流是否在指定时间限制后自动恢复执行，可使用时间间隔或具体时间点。
* **Append n8n Attribution**（附加 n8n 署名）：开启时，在邮件末尾附加 `This email was sent automatically with n8n`；关闭时，不附加。

## 限制 <a href="#limitations" id="limitations"></a>

Send Email（SMTP）节点不支持设置 `In-Reply-To` 和 `References` 等邮件会话串联所需的邮件头，因此每封邮件都会作为新对话处理，而不会显示在同一邮件会话中。

* **替代方法**：使用 Gmail 节点的 **Reply to a message**（回复消息）操作，或支持自定义邮件头的自定义节点。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Send Email 集成模板](https://n8n.io/integrations/send-email)，或[搜索所有模板](https://n8n.io/workflows/)
