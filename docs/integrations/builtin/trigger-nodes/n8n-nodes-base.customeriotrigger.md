---
title: Customer.io 触发器节点文档
description: 了解如何在 n8n 中使用 Customer.io 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Customer.io 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.customeriotrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.customeriotrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.customeriotrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Customer.io 触发器节点 <a href="#customerio-trigger-node" id="customerio-trigger-node"></a>

[Customer.io](https://customer.io/) 支持用户利用网站数据，向选定的客户细分群组发送新闻通讯。你可以发送定向邮件、推送通知和短信，以降低客户流失、加强客户关系并促进订阅。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Customer.io 凭据文档](../credentials/customerio.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Customer.io Trigger 集成](https://n8n.io/integrations/customerio-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* Customer（客户）
    * Subscribed（已订阅）
    * Unsubscribe（退订）
* Email（电子邮件）
    * Bounced（已退回）
    * Clicked（已点击）
    * Converted（已转化）
    * Delivered（已送达）
    * Drafted（已起草）
    * Failed（失败）
    * Opened（已打开）
    * Sent（已发送）
    * Spammed（已标记为垃圾邮件）
* Push（推送）
    * Attempted（已尝试发送）
    * Bounced（已退回）
    * Clicked（已点击）
    * Delivered（已送达）
    * Drafted（已起草）
    * Failed（失败）
    * Opened（已打开）
    * Sent（已发送）
* Slack（Slack 消息）
    * Attempted（已尝试发送）
    * Clicked（已点击）
    * Drafted（已起草）
    * Failed（失败）
    * Sent（已发送）
* Sms（短信）
    * Attempted（已尝试发送）
    * Bounced（已退回）
    * Clicked（已点击）
    * Delivered（已送达）
    * Drafted（已起草）
    * Failed（失败）
    * Sent（已发送）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Customer.io 提供应用节点。更多信息请参阅 [Customer.io 节点文档](../app-nodes/n8n-nodes-base.customerio.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/customerio-trigger/)。

API 的详细信息，请参阅 [Customer.io 文档](https://docs.customer.io/api/)。
