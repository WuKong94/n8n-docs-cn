---
title: Google Calendar 日历操作
contentType:
- integration
- reference
priority: high
nodeTitle: Google Calendar 日历操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/calendar-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/calendar-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/calendar-operations
description: 了解 n8n 工作流自动化平台中 Google Calendar 节点的日历操作，包括操作及配置详情，以及示例和凭据信息链接。
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


# 日历操作 <a id="calendar-operations"></a>

使用此操作检查 Google Calendar 日历中的空闲情况。有关 Google Calendar 节点本身的更多信息，请参阅 [Google Calendar](./README.md)。

## Availability（可用性） <a href="#availability" id="availability"></a>

此操作用于检查日历中的某个时段是否空闲。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Calendar 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Calendar**（日历）。
* **Operation**（操作）：选择 **Availability**（可用性）。
* **Calendar**（日历）：选择要检查的日历。选择 **From list**（从列表）可在下拉列表中按标题选择，选择 **By ID**（按 ID）可输入日历 ID。
* **Start Time**（开始时间）：要检查时段的开始时间。默认使用求值为当前时间的表达式（`{{ $now }}`）。
* **End Time**（结束时间）：要检查时段的结束时间。默认使用求值为当前时间一小时后的表达式（`{{ $now.plus(1, 'hour') }}`）。

### 选项 <a href="#options" id="options"></a>

* **Output Format**（输出格式）：选择空闲信息的格式：
  * **Availability**（可用性）：返回是否已有事件与给定时段重叠。
  * **Booked Slots**（已预订时段）：返回已预订的时段。
  * **RAW**（原始数据）：返回 API 的原始数据。
* **Timezone**（时区）：响应使用的时区，默认使用 n8n 时区。

更多信息，请参阅 [Freebusy: query | Google Calendar](https://developers.google.com/calendar/api/v3/reference/freebusy/query) API 文档。
