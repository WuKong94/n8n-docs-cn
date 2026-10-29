---
title: Cal 触发器节点文档
description: 了解如何在 n8n 中使用 Cal 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Cal 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.caltrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.caltrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.caltrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Cal 触发器节点 <a href="#cal-trigger-node" id="cal-trigger-node"></a>

[Cal](https://cal.com/) 为所有人提供可协调多项日程的排程工具，让你专注于会议本身，而非安排会议。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Cal.com 凭据文档](../credentials/cal.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Cal Trigger 集成](https://n8n.io/integrations/cal-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* Booking cancelled（预约已取消）
* Booking created（预约已创建）
* Booking rescheduled（预约已重新安排）
* Meeting ended（会议已结束）
