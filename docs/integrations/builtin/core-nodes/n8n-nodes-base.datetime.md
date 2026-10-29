---
title: Date & Time 节点
description: 了解 n8n 中 Date & Time 节点的用法，并查看相关示例。
contentType:
- integration
- reference
priority: high
nodeTitle: Date & Time 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.datetime.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datetime
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datetime
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Date & Time（日期与时间） <a href="#date-and-time" id="date-and-time"></a>

Date & Time 节点用于处理日期和时间数据，并将其转换为不同格式。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/schedule/timezone-settings.md" %}

{% hint style="info" %}
**在其他节点中处理日期和时间**

可以在 Code 节点以及任意节点的表达式中处理日期和时间。n8n 支持 Luxon，便于在 JavaScript 中操作日期和时间。更多信息，请参阅[使用 Luxon 处理日期和时间](../../../build/work-with-data/handle-special-data-types/work-with-dates-and-times.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* **Add to a Date**（增加日期时间）：为日期增加指定时长。
* **Extract Part of a Date**（提取日期的一部分）：提取年、月、日等日期部分。
* **Format a Date**（格式化日期）：使用预设选项或自定义表达式，将日期转换为新格式。
* **Get Current Date**（获取当前日期）：获取当前日期，并选择是否包含当前时间，可用于触发其他流程或条件逻辑。
* **Get Time Between Dates**（获取日期间隔）：计算两个日期之间以指定单位表示的时间差。
* **Round a Date**（日期取整）：按所选的月、日、小时等单位，对日期向上或向下取整。
* **Subtract From a Date**（减少日期时间）：从日期减去指定时长。

各操作的专用参数和选项见下文。

## Add to a Date（增加日期时间） <a href="#add-to-a-date" id="add-to-a-date"></a>

使用以下参数配置此操作：

* **Date to Add To**（要增加时长的日期）：输入要更改的日期。
* **Time Unit to Add**（增加时长的单位）：选择 **Duration**（时长）参数的时间单位。
* **Duration**（时长）：输入要增加的时间单位数量。
* **Output Field Name**（输出字段名称）：输入用于输出新日期的字段名称。

### Add to a Date（增加日期时间）选项 <a href="#add-to-a-date-options" id="add-to-a-date-options"></a>

此操作有一个选项：**Include Input Fields**（包含输入字段）。开启时，输出包含所有输入字段；关闭时，仅输出 **Output Field Name**（输出字段名称）指定的字段及其内容。

## Extract Part of a Date（提取日期的一部分） <a href="#extract-part-of-a-date" id="extract-part-of-a-date"></a>

使用以下参数配置此操作：

* **Date**（日期）：输入要取整或提取部分内容的日期。
* **Part**（日期部分）：选择要提取的日期部分，可选：
    * **Year**（年）
    * **Month**（月）
    * **Week**（周）
    * **Day**（日）
    * **Hour**（小时）
    * **Minute**（分钟）
    * **Second**（秒）
* **Output Field Name**（输出字段名称）：输入用于输出所提取日期部分的字段名称。

### Extract Part of a Date（提取日期的一部分）选项 <a href="#extract-part-of-a-date-options" id="extract-part-of-a-date-options"></a>

此操作有一个选项：**Include Input Fields**（包含输入字段）。开启时，输出包含所有输入字段；关闭时，仅输出 **Output Field Name**（输出字段名称）指定的字段及其内容。

## Format a Date（格式化日期） <a href="#format-a-date" id="format-a-date"></a>

使用以下参数配置此操作：

* **Date**（日期）：输入要格式化的日期。
* **Format**（格式）：选择目标日期格式，可选：
    * **Custom Format**（自定义格式）：使用 Luxon 的[特殊格式标记](https://moment.github.io/luxon/#/formatting?id=table-of-tokens)输入自定义格式。格式标记区分大小写。
    * **MM/DD/YYYY**：将 `4 September 1986` 格式化为 `09/04/1986`。
    * **YYYY/MM/DD**：将 `4 September 1986` 格式化为 `1986/09/04`。
    * **MMMM DD YYYY**：将 `4 September 1986` 格式化为 `September 04 1986`。
    * **MM-DD-YYYY**：将 `4 September 1986` 格式化为 `09-04-1986`。
    * **YYYY-MM-DD**：将 `4 September 1986` 格式化为 `1986-09-04`。
* **Output Field Name**（输出字段名称）：输入用于输出格式化后日期的字段名称。

### Format a Date（格式化日期）选项 <a href="#format-a-date-options" id="format-a-date-options"></a>

此操作包含以下选项：

* **Include Input Fields**（包含输入字段）：开启时，输出包含所有输入字段；关闭时，仅输出 **Output Field Name**（输出字段名称）指定的字段及其内容。
* **From Date Format**（输入日期格式）：如果节点无法正确识别 **Date**（日期）的格式，在此输入该 **Date** 的格式，便于节点正确处理。使用 Luxon 的[特殊格式标记](https://moment.github.io/luxon/#/formatting?id=table-of-tokens)填写，格式标记区分大小写。
* **Use Workflow Timezone**（使用工作流时区）：关闭时使用输入数据的时区，开启时使用工作流时区。

## Get Current Date（获取当前日期） <a href="#get-current-date" id="get-current-date"></a>

使用以下参数配置此操作：

* **Include Current Time**（包含当前时间）：开启时包含当前时间，关闭时将时间设为午夜。
* **Output Field Name**（输出字段名称）：输入用于输出当前日期的字段名称。

### Get Current Date（获取当前日期）选项 <a href="#get-current-date-options" id="get-current-date-options"></a>

此操作包含以下选项：

* **Include Input Fields**（包含输入字段）：开启时，输出包含所有输入字段；关闭时，仅输出 **Output Field Name**（输出字段名称）指定的字段及其内容。
* **Timezone**（时区）：设置使用的时区。留空时使用 n8n 实例的时区。

{% hint style="info" %}
**+00:00 时区**

对于 +00:00 时区，请使用 `GMT`。
{% endhint %}

## Get Time Between Dates（获取日期间隔） <a href="#get-time-between-dates" id="get-time-between-dates"></a>

使用以下参数配置此操作：

* **Start Date**（开始日期）：输入要比较的较早日期。
* **End Date**（结束日期）：输入要比较的较晚日期。
* **Units**（单位）：选择用于计算时间差的单位，可以选择多个单位，可选：
    * **Year**（年）
    * **Month**（月）
    * **Week**（周）
    * **Day**（日）
    * **Hour**（小时）
    * **Minute**（分钟）
    * **Second**（秒）
    * **Millisecond**（毫秒）
* **Output Field Name**（输出字段名称）：输入用于输出所计算时间差的字段名称。

### Get Time Between Dates（获取日期间隔）选项 <a href="#get-time-between-dates-options" id="get-time-between-dates-options"></a>

Get Time Between Dates 操作包含 **Include Input Fields**（包含输入字段）和 **Output as ISO String**（输出为 ISO 字符串）选项。关闭后一个选项时，每个选定单位会分别返回自己的时间差计算结果，例如：

    timeDifference
    years : 1
    months : 3
    days : 13

开启 **Output as ISO String**（输出为 ISO 字符串）时，节点将输出格式化为单个 ISO 时长字符串，例如 `P1Y3M13D`。

ISO 时长的格式为 `P<n>Y<n>M<n>DT<n>H<n>M<n>S`，其中 `<n>` 表示其后单位对应的数量。

* P = period（时长），是所有 ISO 时长字符串的起始标记。
* Y = 年
* M = 月
* W = 周
* D = 日
* T = 日期与时间的分隔符，用于区分月和分钟
* H = 小时
* M = 分钟
* S = 秒

毫秒没有独立单位，而是表示为小数秒。例如，2.1 毫秒表示为 `0.0021S`。

## Round a Date（日期取整） <a href="#round-a-date" id="round-a-date"></a>

使用以下参数配置此操作：

* **Date**（日期）：输入要取整的日期。
* **Mode**（模式）：选择 **Round Down**（向下取整）或 **Round Up**（向上取整）。
* **To Nearest**（取整单位）：选择取整所用单位，可选：
    * **Year**（年）
    * **Month**（月）
    * **Week**（周）
    * **Day**（日）
    * **Hour**（小时）
    * **Minute**（分钟）
    * **Second**（秒）
* **Output Field Name**（输出字段名称）：输入用于输出取整后日期的字段名称。

### Round a Date（日期取整）选项 <a href="#round-a-date-options" id="round-a-date-options"></a>

此操作有一个选项：**Include Input Fields**（包含输入字段）。开启时，输出包含所有输入字段；关闭时，仅输出 **Output Field Name**（输出字段名称）指定的字段及其内容。

## Subtract From a Date（减少日期时间） <a href="#subtract-from-a-date" id="subtract-from-a-date"></a>

使用以下参数配置此操作：

* **Date to Subtract From**（要减去时长的日期）：输入要从中减去时长的日期。
* **Time Unit to Subtract**（减去时长的单位）：选择要减去的 **Duration**（时长）对应的单位。
* **Duration**（时长）：输入要从 **Date to Subtract From**（要减去时长的日期）中减去的时间单位数量。
* **Output Field Name**（输出字段名称）：输入用于输出减去时长后日期的字段名称。

### Subtract From a Date（减少日期时间）选项 <a href="#subtract-from-a-date-options" id="subtract-from-a-date-options"></a>

此操作有一个选项：**Include Input Fields**（包含输入字段）。开启时，输出包含所有输入字段；关闭时，仅输出 **Output Field Name**（输出字段名称）指定的字段及其内容。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Date & Time 集成模板](https://n8n.io/integrations/date-and-time)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

Date & Time 节点使用 [Luxon](https://moment.github.io/luxon)，也可以在 [Code](../../../build/code-in-n8n/using-the-code-node.md) 节点和[表达式](../../../build/work-with-data/expressions-versus-data-nodes.md)中使用 Luxon。更多信息，请参阅[使用 Luxon 处理日期和时间](../../../build/work-with-data/handle-special-data-types/work-with-dates-and-times.md)。

### 支持的日期格式 <a href="#supported-date-formats" id="supported-date-formats"></a>

n8n 支持 [Luxon 所支持的所有日期格式](https://moment.github.io/luxon/#/formatting?id=table-of-tokens)，格式标记区分大小写。
