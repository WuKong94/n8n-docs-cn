---
title: Gmail 触发器节点文档
contentType:
- integration
- reference
priority: high
nodeTitle: n8n-nodes-base.gmailtrigger
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger
description: 了解如何在 n8n 中使用 Gmail 触发器节点，并按照技术文档将其集成到工作流中。
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


# Gmail 触发器 <a id="gmail-trigger"></a>

[Gmail](https://www.gmail.com) 是 Google 开发的电子邮件服务。Gmail Trigger 节点可根据 Gmail 中的事件启动工作流。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Google 凭据文档](../../credentials/google/README.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Gmail Trigger 集成](https://n8n.io/integrations/gmail-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* **Message Received**（收到消息）：节点按照所选 **Poll Time**（轮询时间）为新邮件触发。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置节点：

* **Credential to connect with**（连接凭据）：选择或创建供触发器使用的 Google 凭据。创建凭据的更多信息，请参阅 [Google 凭据](../../credentials/google/README.md)。
* **Poll Times**（轮询时间）：选择轮询 **Mode**（模式），设置轮询触发频率。选择不同模式时，会添加或移除相应字段。各模式的参数配置，请参阅[轮询模式选项](poll-mode-options.md)。
* **Simplify**（简化）：选择返回简化响应（开启，默认）或原始数据（关闭）。
  * 简化响应包含邮件消息 ID、标签和邮件头，包括 From、To、CC、BCC 和 Subject。
* **Max Emails per Poll**（每次轮询的最大邮件数）：输入节点每个轮询周期获取的邮件数量上限。默认值为 10，最大值为 50。如果未读邮件数量超过上限，节点会将剩余邮件加入队列，在下个轮询周期继续获取。

## 节点筛选条件 <a href="#node-filters" id="node-filters"></a>

使用以下筛选条件进一步调整节点行为：

* **Include Spam and Trash**（包含垃圾邮件和已删除邮件）：选择是否对 Spam 和 Trash 文件夹中的新邮件触发，开启时包含，关闭时不包含。
* **Label Names or IDs**（标签名称或 ID）：仅对添加了所选标签的邮件触发。选择所需标签名称，或输入表达式指定 ID。下拉菜单的内容根据所选 **Credential**（凭据）填充。
* **Search**（搜索）：输入 Gmail 搜索筛选条件，例如 `from:`，只对满足筛选条件的邮件触发。更多信息请参阅[优化 Gmail 搜索](https://support.google.com/mail/answer/7190?hl=en)。
* **Read Status**（已读状态）：选择 **Unread and read emails**（未读及已读邮件）、**Unread emails only**（仅未读邮件，默认）或 **Read emails only**（仅已读邮件）。
* **Sender**（发件人）：输入邮箱地址或发件人名称的一部分，仅对来自该发件人的邮件触发。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Gmail 提供应用节点。更多信息请参阅 [Gmail 节点文档](../../app-nodes/n8n-nodes-base.gmail/README.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/gmail-trigger/)。

API 的详细信息，请参阅 [Google Gmail API 文档](https://developers.google.com/gmail/api/guides)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见问题及建议的解决办法，请参阅[常见问题](common-issues.md)。
