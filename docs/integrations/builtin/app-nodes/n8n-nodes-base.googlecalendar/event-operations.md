---
title: Google Calendar 事件操作
contentType:
- integration
- reference
priority: high
nodeTitle: Google Calendar 事件操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations
description: 了解 n8n 工作流自动化平台中 Google Calendar 节点的事件操作，包括操作及配置详情，以及示例和凭据信息链接。
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


# 事件操作 <a id="event-operations"></a>

使用这些操作在 Google Calendar 中创建、删除、获取和更新事件。有关 Google Calendar 节点本身的更多信息，请参阅 [Google Calendar](./README.md)。

## Create（创建） <a href="#create" id="create"></a>

此操作用于向 Google Calendar 日历添加事件。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Calendar 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Event**（事件）。
* **Operation**（操作）：选择 **Create**（创建）。
* **Calendar**（日历）：选择要添加事件的日历。选择 **From list**（从列表）可在下拉列表中按标题选择，选择 **By ID**（按 ID）可输入日历 ID。
* **Start Time**（开始时间）：事件的开始时间。默认使用求值为当前时间的表达式（`{{ $now }}`）。
* **End Time**（结束时间）：事件的结束时间。默认使用求值为当前时间一小时后的表达式（`{{ $now.plus(1, 'hour') }}`）。
* **Use Default Reminders**（使用默认提醒）：是否按照日历配置为事件启用默认提醒。

### 选项 <a href="#options" id="options"></a>

* **All Day**（全天）：事件是否持续全天。
* **Attendees**（参与者）：要邀请参加事件的参与者。
* **Color Name or ID**（颜色名称或 ID）：事件颜色。从列表中选择，或使用表达式指定 ID。
* **Conference Data**（会议数据）：创建会议链接，例如 Hangouts、Meet 等，并将其附加到事件。
* **Description**（描述）：事件的描述。
* **Guests Can Invite Others**（来宾可邀请他人）：组织者以外的参与者是否可以邀请其他人参加事件。
* **Guests Can Modify**（来宾可修改）：组织者以外的参与者是否可以修改事件。
* **Guests Can See Other Guests**（来宾可查看其他来宾）：组织者以外的参与者是否可以查看事件参与者名单。
* **ID**（标识符）：事件的不透明标识符。
* **Location**（地点）：事件的地理位置，以自由格式文本填写。
* **Max Attendees**（最多参与者）：响应中包含的最大参与者数量。如果参与者超过指定数量，则仅返回该参与者。
* **Repeat Frequency**（重复频率）：重复事件的重复间隔。
* **Repeat How Many Times?**（重复次数）：为重复事件创建的实例数量。
* **Repeat Until**（重复截止日期）：重复事件应停止的日期。
* **RRULE**（重复规则）：事件重复规则。设置后会忽略 Repeat Frequency（重复频率）、Repeat How Many Times（重复次数）和 Repeat Until（重复截止日期）参数。
* **Send Updates**（发送更新）：是否发送有关新事件创建的通知。
* **Show Me As**（显示为）：事件是否占用日历中的时间。
* **Summary**（摘要）：事件标题。

更多信息，请参阅 [Events: insert | Google Calendar](https://developers.google.com/calendar/api/v3/reference/events/insert) API 文档。

## Delete（删除） <a href="#delete" id="delete"></a>

此操作用于从 Google Calendar 日历删除事件。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Calendar 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Event**（事件）。
* **Operation**（操作）：选择 **Delete**（删除）。
* **Calendar**（日历）：选择要从中删除事件的日历。选择 **From list**（从列表）可在下拉列表中按标题选择，选择 **By ID**（按 ID）可输入日历 ID。
* **Event ID**（事件 ID）：要删除的事件 ID。

### 选项 <a href="#options" id="options"></a>

* **Send Updates**（发送更新）：是否发送有关事件删除的通知。

更多信息，请参阅 [Events: delete | Google Calendar](https://developers.google.com/calendar/api/v3/reference/events/delete) API 文档。

## Get（获取） <a href="#get" id="get"></a>

此操作用于从 Google Calendar 日历获取事件。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Calendar 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Event**（事件）。
* **Operation**（操作）：选择 **Get**（获取）。
* **Calendar**（日历）：选择要从中获取事件的日历。选择 **From list**（从列表）可在下拉列表中按标题选择，选择 **By ID**（按 ID）可输入日历 ID。
* **Event ID**（事件 ID）：要获取的事件 ID。

### 选项 <a href="#options" id="options"></a>

* **Max Attendees**（最多参与者）：响应中包含的最大参与者数量。如果参与者超过指定数量，则仅返回该参与者。
* **Return Next Instance of Recurrent Event**（返回重复事件的下一个实例）：是否返回重复事件的下一个实例，而非事件本身。
* **Timezone**（时区）：响应使用的时区，默认使用 n8n 时区。

更多信息，请参阅 [Events: get | Google Calendar](https://developers.google.com/calendar/api/v3/reference/events/get) API 文档。

## Get Many（获取多项） <a href="#get-many" id="get-many"></a>

此操作用于从 Google Calendar 日历获取多个事件。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Calendar 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Event**（事件）。
* **Operation**（操作）：选择 **Get Many**（获取多项）。
* **Calendar**（日历）：选择要从中获取事件的日历。选择 **From list**（从列表）可在下拉列表中按标题选择，选择 **By ID**（按 ID）可输入日历 ID。
* **Return All**（返回全部）：是否返回所有结果，或仅返回指定数量以内的结果。
* **Limit**（数量限制）：未选择 Return All（返回全部）时，返回的最大结果数量。
* **After**（晚于）：获取在该时间之后发生的事件。事件至少有一部分必须位于该时间之后。默认使用求值为当前时间的表达式（`{{ $now }}`）。将字段切换为 fixed（固定值）可通过日期控件选择日期。
* **Before**（早于）：获取在该时间之前发生的事件。事件至少有一部分必须位于该时间之前。默认使用求值为当前时间一周后的表达式（`{{ $now.plus({ week: 1 }) }}`）。将字段切换为 fixed（固定值）可通过日期控件选择日期。

### 选项 <a href="#options" id="options"></a>

* **Fields**（字段）：指定要返回的字段。默认返回 Google 预定义的一组常用字段。使用“\*”可返回所有字段。更多信息，请参阅 [Google Calendar 关于使用部分资源的文档](https://developers.google.com/calendar/api/guides/performance#partial)。
* **iCalUID**：指定响应中要包含的事件 ID，采用 iCalendar 格式。
* **Max Attendees**（最多参与者）：响应中包含的最大参与者数量。如果参与者超过指定数量，则仅返回该参与者。
* **Order By**（排序依据）：响应中事件的排列顺序。
* **Query**（查询）：用于查找匹配事件的自由文本搜索词，搜索除扩展属性以外的所有字段。
* **Recurring Event Handling**（重复事件处理）：如何处理重复事件：
  * **All Occurrences**（所有实例）：返回指定时间范围内重复事件的所有实例。
  * **First Occurrence**（首次实例）：返回指定时间范围内重复事件的第一个事件。
  * **Next Occurrence**（下一个实例）：返回指定时间范围内重复事件的下一个实例。
* **Show Deleted**（显示已删除事件）：是否在结果中包含已删除的事件，即状态为 cancelled 的事件。
* **Show Hidden Invitations**（显示隐藏邀请）：是否在结果中包含隐藏的邀请。
* **Timezone**（时区）：响应使用的时区，默认使用 n8n 时区。
* **Updated Min**（最早更新时间）：事件最后修改时间的下限，采用 [RFC 3339 时间戳](https://datatracker.ietf.org/doc/html/rfc3339)。

更多信息，请参阅 [Events: list | Google Calendar](https://developers.google.com/calendar/api/v3/reference/events/list) API 文档。

## Update（更新） <a href="#update" id="update"></a>

此操作用于更新 Google Calendar 日历中的事件。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Calendar 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Event**（事件）。
* **Operation**（操作）：选择 **Update**（更新）。
* **Calendar**（日历）：选择要更新事件的日历。选择 **From list**（从列表）可在下拉列表中按标题选择，选择 **By ID**（按 ID）可输入日历 ID。
* **Event ID**（事件 ID）：要更新的事件 ID。
* **Modify**（修改范围）：对于重复事件，选择更新整个重复事件，还是其中的某个实例。
* **Use Default Reminders**（使用默认提醒）：是否按照日历配置为事件启用默认提醒。
* **Update Fields**（更新字段）：要更新的事件字段：
  * **All Day**（全天）：事件是否持续全天。
  * **Attendees**（参与者）：要邀请参加事件的参与者。可选择添加参与者，或替换已有的参与者列表。
  * **Color Name or ID**（颜色名称或 ID）：事件颜色。从列表中选择，或使用表达式指定 ID。
  * **Description**（描述）：事件的描述。
  * **End**（结束）：事件的结束时间。
  * **Guests Can Invite Others**（来宾可邀请他人）：组织者以外的参与者是否可以邀请其他人参加事件。
  * **Guests Can Modify**（来宾可修改）：组织者以外的参与者是否可以修改事件。
  * **Guests Can See Other Guests**（来宾可查看其他来宾）：组织者以外的参与者是否可以查看事件参与者名单。
  * **ID**（标识符）：事件的不透明标识符。
  * **Location**（地点）：事件的地理位置，以自由格式文本填写。
  * **Max Attendees**（最多参与者）：响应中包含的最大参与者数量。如果参与者超过指定数量，则仅返回该参与者。
  * **Repeat Frequency**（重复频率）：重复事件的重复间隔。
  * **Repeat How Many Times?**（重复次数）：为重复事件创建的实例数量。
  * **Repeat Until**（重复截止日期）：重复事件应停止的日期。
  * **RRULE**（重复规则）：事件重复规则。设置后会忽略 Repeat Frequency（重复频率）、Repeat How Many Times（重复次数）和 Repeat Until（重复截止日期）参数。
  * **Send Updates**（发送更新）：是否发送有关事件更新的通知。
  * **Show Me As**（显示为）：事件是否占用日历中的时间。
  * **Start**（开始）：事件的开始时间。
  * **Summary**（摘要）：事件标题。
  * **Visibility**（可见性）：事件的可见性：
    * **Confidential**（保密）：事件为私密事件。此值用于兼容。
    * **Default**（默认）：使用日历中事件的默认可见性。
    * **Public**（公开）：事件公开，所有有权读取日历的人均可查看事件详情。
    * **Private**（私密）：事件为私密事件，仅事件参与者可查看事件详情。

更多信息，请参阅 [Events: update | Google Calendar](https://developers.google.com/calendar/api/v3/reference/events/update) API 文档。
