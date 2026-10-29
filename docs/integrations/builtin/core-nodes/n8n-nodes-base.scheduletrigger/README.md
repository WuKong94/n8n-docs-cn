---
title: Schedule Trigger 节点
description: 了解如何在 n8n 工作流中配置和使用 Schedule Trigger 节点。
contentType:
- integration
- reference
priority: critical
nodeTitle: n8n-nodes-base.scheduletrigger
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Schedule Trigger（定时触发）节点 <a href="#schedule-trigger-node" id="schedule-trigger-node"></a>

使用 Schedule Trigger 节点，按固定间隔和时间运行工作流。它的工作方式类似 Unix 类系统中的 Cron 工具。

{% hint style="info" %}
**必须发布工作流**

如果工作流使用 Schedule 节点作为触发器，请确保已保存并发布工作流。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/schedule/timezone-settings.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

添加 **Trigger Rules**（触发规则），确定触发器运行的时间。

使用 **Trigger Interval**（触发间隔）选择定时触发所用的时间单位。其他参数均取决于所选间隔，可选：

- [以秒为单位的触发间隔](#seconds-trigger-interval)
- [以分钟为单位的触发间隔](#minutes-trigger-interval)
- [以小时为单位的触发间隔](#hours-trigger-interval)
- [以天为单位的触发间隔](#days-trigger-interval)
- [以周为单位的触发间隔](#weeks-trigger-interval)
- [以月为单位的触发间隔](#months-trigger-interval)
- [自定义 Cron 间隔](#custom-cron-interval)

可以添加多个 **Trigger Rules**（触发规则），让节点按不同时间安排运行。

各类 **Trigger Interval**（触发间隔）的配置见下文。更多示例，请参阅[模板与示例](#templates-and-examples)。

{% hint style="info" %}
**n8n 2.45.0 起的默认计时方式**

只要 `N8N_USE_WORKFLOW_PUBLICATION_SERVICE` 保持开启（默认状态），Schedule Trigger 节点就默认使用持久化调度器。Seconds（秒）和 Minutes（分钟）间隔从工作流发布时刻起均匀计时，而不是对齐时钟边界。Custom (Cron)（自定义 Cron）间隔保留原有计时方式。关于对齐时钟的计时方式，请参阅 [Schedule Trigger 计时](../../../../deploy/host-n8n/configure-n8n/durable-scheduler.md#trigger-node-mode)；要切换调度器，请参阅[使用内存调度器](../../../../deploy/host-n8n/configure-n8n/durable-scheduler.md#use-the-in-memory-scheduler)。
{% endhint %}

### 以秒为单位的触发间隔 <a href="#seconds-trigger-interval" id="seconds-trigger-interval"></a>

* **Seconds Between Triggers**（触发间隔秒数）：输入两次触发之间的秒数。例如，输入 `30`，触发器就会每 30 秒运行一次。

### 以分钟为单位的触发间隔 <a href="#minutes-trigger-interval" id="minutes-trigger-interval"></a>

* **Minutes Between Triggers**（触发间隔分钟数）：输入两次触发之间的分钟数。例如，输入 `5`，触发器就会每 5 分钟运行一次。

### 以小时为单位的触发间隔 <a href="#hours-trigger-interval" id="hours-trigger-interval"></a>

* **Hours Between Triggers**（触发间隔小时数）：输入两次触发之间的小时数。
* **Trigger at Minute**（触发分钟）：输入每个触发小时内的分钟数，范围为 `0` 到 `59`。

例如，将 **Hours Between Triggers**（触发间隔小时数）设为 `6`，**Trigger at Minute**（触发分钟）设为 `30`，节点会每六小时在该小时的第 30 分钟运行。

### 以天为单位的触发间隔 <a href="#days-trigger-interval" id="days-trigger-interval"></a>

* **Days Between Triggers**（触发间隔天数）：输入两次触发之间的天数。
* **Trigger at Hour**（触发小时）：选择一天中触发节点的小时。
* **Trigger at Minute**（触发分钟）：输入每个触发小时内的分钟数，范围为 `0` 到 `59`。


例如，将 **Days Between Triggers**（触发间隔天数）设为 `2`，将 **Trigger at Hour**（触发小时）设为 **9am**（上午九点），将 **Trigger at Minute**（触发分钟）设为 `15`，节点会每两天在上午 9:15 运行。


### 以周为单位的触发间隔 <a href="#weeks-trigger-interval" id="weeks-trigger-interval"></a>

* **Weeks Between Triggers**（触发间隔周数）：输入两次触发之间的周数。
* **Trigger on Weekdays**（触发星期）：选择在一周中的哪一天或哪几天触发节点。
* **Trigger at Hour**（触发小时）：选择一天中触发节点的小时。
* **Trigger at Minute**（触发分钟）：输入每个触发小时内的分钟数，范围为 `0` 到 `59`。

例如，将 **Weeks Between Triggers**（触发间隔周数）设为 `2`，将 **Trigger on Weekdays**（触发星期）设为 **Monday**（星期一），将 **Trigger at Hour**（触发小时）设为 **3pm**（下午三点），将 **Trigger at Minute**（触发分钟）设为 `30`，节点会每两周在星期一下午 3:30 运行。

### 以月为单位的触发间隔 <a href="#months-trigger-interval" id="months-trigger-interval"></a>

* **Months Between Triggers**（触发间隔月数）：输入两次触发之间的月数。
* **Trigger at Day of Month**（触发日期）：输入在每月哪一天触发，范围为 `1` 到 `31`。如果某个月没有该日期，节点就不会触发。例如，输入 `30` 时，节点不会在二月触发。
* **Trigger at Hour**（触发小时）：选择一天中触发节点的小时。
* **Trigger at Minute**（触发分钟）：输入每个触发小时内的分钟数，范围为 `0` 到 `59`。

例如，将 **Months Between Triggers**（触发间隔月数）设为 `3`，将 **Trigger at Day of Month**（触发日期）设为 `28`，将 **Trigger at Hour**（触发小时）设为 **9am**（上午九点），将 **Trigger at Minute**（触发分钟）设为 `0`，节点就会每季度在当月 28 日上午 9:00 运行。

### 自定义 Cron 间隔 <a href="#custom-cron-interval" id="custom-cron-interval"></a>

输入自定义 cron **Expression**（表达式），设置触发时间。

可以使用 [crontab guru](https://crontab.guru) 生成 Cron 表达式，再将其粘贴到 n8n 的 **Expression**（表达式）字段中。

#### 示例 <a href="#examples" id="examples"></a>


| 类型 | Cron 表达式 | 说明 |
|---|---|---|
| 每隔若干秒 | `*/10 * * * * *` | 每 10 秒。 |
| 每隔若干分钟 | `*/5 * * * *` | 每 5 分钟。 |
| 每小时 | `0 * * * *` | 每小时整点。 |
| 每天 | `0 6 * * *` | 每天上午 6:00。 |
| 每周 | `0 12 * * 1` | 每周一中午。 |
| 每月 | `0 0 1 * *` | 每月 1 日午夜。 |
| 日期按步长触发 | `0 0 */3 * *` | 每月从首日开始，以 3 日为步长，在对应日期的午夜触发；跨月时重新按日历日期匹配。 |
| 仅工作日 | `0 9 * * 1-5` | 周一至周五上午 9:00。 |
| 自定义小时范围 | `0 9-17 * * *` | 每天上午 9:00 至下午 5:00，每小时触发。 |
| 每季度 | `0 0 1 1,4,7,10 *` | 一月、四月、七月和十月的 1 日午夜。 |


{% hint style="warning" %}
**在 Cron 表达式中使用变量**

定时触发器可以使用变量，但只会在工作流发布时求出变量值。工作流发布后，即使在设置中更改变量值，也不会改变 cron 定时规则。要重新求值，请先取消发布，再重新发布工作流。
{% endhint %}

#### 为什么 Cron 表达式有六个星号 <a href="#why-there-are-six-asterisks-in-the-cron-expression" id="why-there-are-six-asterisks-in-the-cron-expression"></a>

相较五字段 Cron 表达式，额外的秒字段位于最左侧。此字段可选，即使不设置秒，节点仍会执行。

|  (*)  |  *  |  *  |  *  |  *  |  *  |
|:--:|:--:|:--:|:--:|:--:|:--:|
| （秒，可选） | 分钟 | 小时 | 每月日期 | 月份 | 星期（日至六） |

## 节点选项 <a href="#node-options" id="node-options"></a>

节点的 **Settings**（设置）标签页提供以下选项，用于控制错过定时执行时的行为，例如实例停机导致的错过执行：

* **If Execution Is Missed**（错过执行时）：选择如何处理错过的执行：
    * **Don't Run Missed Executions**（不补跑，默认）：丢弃错过的执行，恢复按计划运行。
    * **Run the Most Recent Missed Execution**（补跑最近一次错过的执行）：按最近一次错过的时间补跑一次，然后恢复按计划运行。
    * **Run the Most Recent Missed Execution Per Rule**（每条规则补跑最近一次错过的执行）：类似上一选项，但每条触发规则各自补跑一次。
* **Missed Execution Grace Period (Seconds)**（错过执行的宽限期，秒）：执行允许延迟启动多久，超过后才算错过。设为 `0` 时使用实例设置（`N8N_SCHEDULER_MISFIRE_GRACE`，默认为 60 秒）。低于实例最小值的配置会被上调至该最小值，默认配置下为 60 秒；超过 30 天的值会被限制为该时长。

{% hint style="info" %}
**功能可用性**

这些选项自 n8n 2.36 起提供，适用于从该版本起添加的 Schedule Trigger 节点。仅在实例运行[持久化调度器](../../../../deploy/host-n8n/configure-n8n/durable-scheduler.md)时生效，该调度器从 n8n 2.45.0 起默认开启。如果设置 `N8N_SCHEDULER_ENABLED=false`，Schedule Trigger 节点将使用内存调度器，不会补跑错过的执行。
{% endhint %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-base.scheduletrigger 集成模板](https://n8n.io/integrations/schedule-trigger)，或[搜索所有模板](https://n8n.io/workflows/)

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见疑问或问题及建议的解决方法，请参阅[常见问题](common-issues.md)。
