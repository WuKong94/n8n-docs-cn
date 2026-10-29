---
title: Email Trigger (IMAP) 节点
description: 了解如何在 n8n 工作流中配置和使用 Email Trigger (IMAP) 节点。
contentType:
- integration
- reference
priority: high
nodeTitle: Email Trigger (IMAP) 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.emailimap.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Email Trigger (IMAP)（IMAP 邮件触发器）节点 <a href="#email-trigger-imap-node" id="email-trigger-imap-node"></a>

使用 IMAP Email 节点，通过 IMAP 邮件服务器接收电子邮件。此节点是触发器节点。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [IMAP 凭据文档](../credentials/imap/README.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

- 接收电子邮件

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置节点。

### Credential to connect with（连接凭据） <a href="#credential-to-connect-with" id="credential-to-connect-with"></a>

选择或创建用于连接服务器的 [IMAP 凭据](../credentials/imap/README.md)。

### Mailbox Name（邮箱名称） <a href="#mailbox-name" id="mailbox-name"></a>

输入要从中接收邮件的邮箱。

### Action（操作） <a href="#action" id="action"></a>

选择 n8n 接收邮件后是否将其标记为已读。**None**（不处理）会保留未读标记，**Mark as Read**（标记为已读）会将其标记为已读。

### Download Attachments（下载附件） <a href="#download-attachments" id="download-attachments"></a>

此开关控制是否下载邮件附件：开启时下载，关闭时不下载。下载会增加处理量，请仅在需要时开启。

### Format（格式） <a href="#format" id="format"></a>

选择邮件返回格式：

* **RAW**（原始）：返回完整邮件数据，正文在 raw 字段中表示为 base64url 编码字符串，不使用 payload 字段。
* **Resolved**（已解析）：返回解析全部数据后的完整邮件，并将附件保存为二进制数据。
* **Simple**（简单）：返回完整邮件。如果需要获取内嵌附件，不要使用此格式。

## 节点选项 <a href="#node-options" id="node-options"></a>

还可使用以下 **Options**（选项）进一步配置节点。

### Custom Email Rules（自定义邮件规则） <a href="#custom-email-rules" id="custom-email-rules"></a>

输入自定义邮件获取规则，决定节点应获取哪些邮件。

更多信息，请参阅 [node-imap 搜索函数的条件说明](https://github.com/mscdex/node-imap)。

### Force Reconnect Every Minutes（强制重连间隔，分钟） <a href="#force-reconnect-every-minutes" id="force-reconnect-every-minutes"></a>

设置强制重新连接的间隔，单位为分钟。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Email Trigger (IMAP) 节点集成模板](https://n8n.io/integrations/email-trigger-imap)，或[搜索所有模板](https://n8n.io/workflows/)
