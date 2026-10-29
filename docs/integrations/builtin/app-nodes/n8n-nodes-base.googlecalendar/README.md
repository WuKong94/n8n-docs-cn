---
title: Google Calendar 节点文档
description: 了解如何在 n8n 中使用 Google Calendar 节点，并按照技术文档将 Google Calendar 节点集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: n8n-nodes-base.googlecalendar
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Calendar 节点 <a href="#google-calendar-node" id="google-calendar-node"></a>

使用 Google Calendar 节点自动处理 Google Calendar 中的工作，并将其与其他应用集成。n8n 内置支持多种 Google Calendar 功能，包括添加、获取、删除和更新日历事件。

本页列出了 Google Calendar 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Google Calendar 凭据](../../credentials/google/README.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* **Calendar**（日历）
    * [**Availability**](calendar-operations.md#availability)（可用性）：检查日历中的时段是否空闲
* **Event**（事件）
    * [**Create**](event-operations.md#create)（创建）：向日历添加事件
    * [**Delete**](event-operations.md#delete)（删除）：删除事件
    * [**Get**](event-operations.md#get)（获取）：获取事件
    * [**Get Many**](event-operations.md#get-many)（获取多项）：获取日历中的所有事件
    * [**Update**](event-operations.md#update)（更新）：更新事件

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-base.googlecalendar 集成模板](https://n8n.io/integrations/google-calendar)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 提供 Google Calendar 触发器节点。更多信息，请参阅 [Google Calendar Trigger 节点文档](../../trigger-nodes/n8n-nodes-base.googlecalendartrigger.md)。

有关该服务的更多信息，请参阅 [Google Calendar 文档](https://developers.google.com/calendar/api/v3/reference)。

在 n8n 网站查看[示例工作流及相关内容](https://n8n.io/integrations/google-calendar/)。
