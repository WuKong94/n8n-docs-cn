---
title: Acuity Scheduling 触发器节点文档
description: 了解如何在 n8n 中使用 Acuity Scheduling 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Acuity Scheduling 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.acuityschedulingtrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.acuityschedulingtrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.acuityschedulingtrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Acuity Scheduling 触发器节点 <a href="#acuity-scheduling-trigger-node" id="acuity-scheduling-trigger-node"></a>

[Acuity Scheduling](https://acuityscheduling.com/) 是基于云的预约排程软件，帮助企业在线管理预约。它可以根据用户时区自动同步日历，并定期发送预约提醒和通知。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Acuity Scheduling 凭据文档](../credentials/acuityscheduling.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Acuity Scheduling Trigger 集成](https://n8n.io/integrations/acuity-scheduling-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* Appointment canceled（预约已取消）
* Appointment changed（预约已更改）
* Appointment rescheduled（预约已重新安排）
* Appointment scheduled（预约已安排）
* Order completed（订单已完成）
