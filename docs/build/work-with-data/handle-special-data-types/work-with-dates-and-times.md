---
title: 使用 Luxon 处理日期和时间
description: 使用 Luxon 处理 n8n 中的日期和时间。
contentType: howto
nodeTitle: 处理日期和时间
originalFilePath: data/specific-data-types/luxon.md
originalUrl: https://docs.n8n.io/data/specific-data-types/luxon
url: https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-dates-and-times
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 使用 Luxon 处理日期和时间 <a href="#date-and-time-with-luxon" id="date-and-time-with-luxon"></a>

[Luxon](https://github.com/moment/luxon/) 是一个 JavaScript 库，可以简化日期和时间的处理。完整用法请参阅 [Luxon 文档](https://moment.github.io/luxon/#/?id=luxon)。

n8n 在节点之间以字符串形式传递日期，因此你需要先解析这些字符串。Luxon 可以简化这一步。

{% hint style="info" %}
**Python 支持**

Luxon 是一个 JavaScript 库。在 Code 节点中使用 Python 时，也可以使用 n8n 提供的两个便捷[变量](#get-the-current-datetime-or-date)，但其功能有限：

* 无法对这些变量执行 Luxon 操作。例如，Python 中没有与 `$today.minus(...)` 等效的写法。
* Python 用户无法使用通用的 Luxon 功能，例如[将日期字符串转换为 Luxon 对象](#convert-date-string-to-luxon)。
{% endhint %}

## n8n 中日期和时间的行为 <a href="#date-and-time-behavior-in-n8n" id="date-and-time-behavior-in-n8n"></a>

请注意以下几点：

* 在工作流中，n8n 会在节点之间传递数据时将日期和时间转换为字符串。对其他节点提供的日期和时间进行运算时，请留意这一点。
* 在 n8n 中，建议使用 Luxon 的 `DateTime()`。原生 JavaScript 的 `Date()` 无法配合某些 n8n 功能正常工作，例如不会遵循[工作流专用时区](../../manage-workflows/configure-workflow-settings.md#timezone)。
* 使用原生 JavaScript 时，可以通过 `new Date('2019-06-23')` 将字符串转换为日期。在 Luxon 中，则必须使用明确指定格式的函数，例如 `DateTime.fromISO('2019-06-23')` 或 `DateTime.fromFormat("23-06-2019", "dd-MM-yyyy")`。

## 在 n8n 中设置时区 <a href="#setting-the-timezone-in-n8n" id="setting-the-timezone-in-n8n"></a>

Luxon 使用 n8n 的时区，其值来自以下设置之一：

* 默认值：`America/New York`
* 通过 `GENERIC_TIMEZONE` 环境变量为 n8n 实例设置的自定义时区。
* 在工作流设置中为单个工作流配置的自定义时区。

## 常见任务 <a href="#common-tasks" id="common-tasks"></a>

本节介绍一些常见操作的示例。更多示例和详细说明请参阅 [Luxon 官方文档](https://moment.github.io/luxon/#/?id=luxon)。

### 获取当前日期时间或日期 <a href="#get-the-current-datetime-or-date" id="get-the-current-datetime-or-date"></a>

使用 `$now` 和 `$today` Luxon 对象，可以获取当前时间或当天日期：

* `now`：包含当前时间戳的 Luxon 对象，等效于 `DateTime.now()`。
* `today`：包含当前时间戳并向下取整到当天起始时刻的 Luxon 对象，等效于 `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 })`。

请注意，将这些变量转换为字符串时，返回的时间格式可能不同：

{% tabs %}
{% tab title="表达式（JavaScript）" %}
```javascript
{{$now}}
// n8n displays the ISO formatted timestamp
// For example 2022-03-09T14:02:37.065+00:00
{{"Today's date is " + $now}}
// n8n displays "Today's date is <unix timestamp>"
// For example "Today's date is 1646834498755"
```
{% endtab %}

{% tab title="Code 节点（JavaScript）" %}
```javascript
$now
// n8n displays <ISO formatted timestamp>
// For example 2022-03-09T14:00:25.058+00:00
let rightNow = "Today's date is " + $now
// n8n displays "Today's date is <unix timestamp>"
// For example "Today's date is 1646834498755"
```
{% endtab %}

{% tab title="Code 节点（Python）" %}
```python
_now
# n8n displays <ISO formatted timestamp>
# For example 2022-03-09T14:00:25.058+00:00
rightNow = "Today's date is " + str(_now)
# n8n displays "Today's date is <unix timestamp>"
# For example "Today's date is 1646834498755"
```
{% endtab %}
{% endtabs %}

n8n 提供了内置便捷函数，支持在表达式中转换日期数据。更多信息请参阅[表达式参考](../transform-data/expression-reference/README.md)。

### 将 JavaScript 日期转换为 Luxon 对象 <a href="#convert-javascript-dates-to-luxon" id="convert-javascript-dates-to-luxon"></a>

将原生 JavaScript 日期转换为 Luxon 日期的方法如下：

* 在表达式中，使用 `.toDateTime()` 方法。例如，`{{ (new Date()).toDateTime() }}`。
* 在 Code 节点中，使用 `DateTime.fromJSDate()`。例如，`let luxondate = DateTime.fromJSDate(new Date())`。

### 将日期字符串转换为 Luxon 对象 <a href="#convert-date-string-to-luxon" id="convert-date-string-to-luxon"></a>

你可以将日期字符串和其他日期格式转换为 Luxon DateTime 对象，既支持标准格式，也支持自定义格式的字符串。

{% hint style="info" %}
**Luxon DateTime 与 JavaScript Date 的区别**

使用原生 JavaScript 时，可以通过 `new Date('2019-06-23')` 将字符串转换为日期。在 Luxon 中，则必须使用明确指定格式的函数，例如 `DateTime.fromISO('2019-06-23')` 或 `DateTime.fromFormat("23-06-2019", "dd-MM-yyyy")`。
{% endhint %}

#### 日期采用受支持的标准技术格式时 <a href="#if-you-have-a-date-in-a-supported-standard-technical-format" id="if-you-have-a-date-in-a-supported-standard-technical-format"></a>

大多数日期使用 `fromISO()`。此方法根据 ISO 8601 字符串创建 Luxon DateTime 对象。例如：

{% tabs %}
{% tab title="表达式（JavaScript）" %}
```js
{{DateTime.fromISO('2019-06-23T00:00:00.00')}}
```
{% endtab %}

{% tab title="Code 节点（JavaScript）" %}
```js
let luxonDateTime = DateTime.fromISO('2019-06-23T00:00:00.00')
```
{% endtab %}
{% endtabs %}

Luxon 的 API 文档提供了关于 [fromISO](https://moment.github.io/luxon/api-docs/index.html#datetimefromiso) 的更多信息。

Luxon 提供了可转换多种格式的函数。详情请参阅 Luxon 的[解析技术格式](https://moment.github.io/luxon/#/parsing?id=parsing-technical-formats)指南。

#### 日期是非标准格式的字符串时 <a href="#if-you-have-a-date-as-a-string-that-doesnt-use-a-standard-format" id="if-you-have-a-date-as-a-string-that-doesnt-use-a-standard-format"></a>

使用 Luxon 的[自定义格式解析（Ad-hoc parsing）](https://moment.github.io/luxon/#/parsing?id=ad-hoc-parsing)。具体做法是调用 `fromFormat()` 函数，传入字符串，以及一组描述其格式的[格式标记](https://moment.github.io/luxon/#/parsing?id=table-of-tokens)。

例如，n8n 的成立日期是 2019 年 6 月 23 日，格式为 `23-06-2019`。你希望将它转换为 Luxon 对象：

{% tabs %}
{% tab title="表达式（JavaScript）" %}
```js
{{DateTime.fromFormat("23-06-2019", "dd-MM-yyyy")}}
```
{% endtab %}

{% tab title="Code 节点（JavaScript）" %}
```js
let newFormat = DateTime.fromFormat("23-06-2019", "dd-MM-yyyy")
```
{% endtab %}
{% endtabs %}

使用自定义格式解析时，请留意 Luxon 关于[局限性](https://moment.github.io/luxon/#/parsing?id=limitations)的提示。如果结果不符合预期，可以参阅其[调试](https://moment.github.io/luxon/#/parsing?id=debugging)指南。

### 获取今天前后 n 天的日期 <a href="#get-n-days-from-today" id="get-n-days-from-today"></a>

获取今天之前或之后若干天的日期。

{% tabs %}
{% tab title="表达式（JavaScript）" %}
例如，你希望某个字段始终显示当前日期七天前的日期。

在表达式编辑器中输入：


``` js
{{$today.minus({days: 7})}}
```

在 2019 年 6 月 23 日执行时，返回 `[Object: "2019-06-16T00:00:00.000+00:00"]`。

为方便起见，此示例使用 n8n 的自定义变量 `$today`，它等效于 `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 }).minus({days: 7})`。
{% endtab %}

{% tab title="Code 节点（JavaScript）" %}
例如，你希望某个变量保存当前日期七天前的日期。

在代码编辑器中输入：

``` js
let sevenDaysAgo = $today.minus({days: 7})
```

在 2019 年 6 月 23 日执行时，返回 `[Object: "2019-06-16T00:00:00.000+00:00"]`。

为方便起见，此示例使用 n8n 的自定义变量 `$today`，它等效于 `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 }).minus({days: 7})`。
{% endtab %}
{% endtabs %}

更多详细说明和示例，请参阅：

* Luxon 的[日期时间运算指南](https://moment.github.io/luxon/#/math)
* API 文档中的 [DateTime plus](https://moment.github.io/luxon/api-docs/index.html#datetimeplus) 和 [DateTime minus](https://moment.github.io/luxon/api-docs/index.html#datetimeminus)

### 创建易读的日期 <a href="#create-human-readable-dates" id="create-human-readable-dates"></a>

在[获取今天前后 n 天的日期](#get-n-days-from-today)一节中，示例获取当前日期七天前的日期，并返回 `[Object: "yyyy-mm-dd-T00:00:00.000+00:00"]`（表达式）或 `yyyy-mm-dd-T00:00:00.000+00:00`（Code 节点）。可以使用 Luxon 的格式化函数，让结果更易读。

例如，你希望将日期字段的格式设为 DD/MM/YYYY，这样在 2019 年 6 月 23 日执行时，会返回 `23/06/2019`。

以下表达式获取今天七天前的日期，并将其转换为 DD/MM/YYYY 格式。

{% tabs %}
{% tab title="表达式（JavaScript）" %}
```js
{{$today.minus({days: 7}).toLocaleString()}}
```
{% endtab %}

{% tab title="Code 节点（JavaScript）" %}
```js
let readableSevenDaysAgo = $today.minus({days: 7}).toLocaleString()
```
{% endtab %}
{% endtabs %}

你可以修改格式。例如：

{% tabs %}
{% tab title="表达式（JavaScript）" %}
```js
{{$today.minus({days: 7}).toLocaleString({month: 'long', day: 'numeric', year: 'numeric'})}}
```

在 2019 年 6 月 23 日执行时，返回 "16 June 2019"。
{% endtab %}

{% tab title="Code 节点（JavaScript）" %}
```js
let readableSevenDaysAgo = $today.minus({days: 7}).toLocaleString({month: 'long', day: 'numeric', year: 'numeric'})
```

在 2019 年 6 月 23 日执行时，返回 "16 June 2019"。
{% endtab %}
{% endtabs %}

更多信息请参阅 Luxon 的 [toLocaleString（面向读者的字符串）](https://moment.github.io/luxon/#/formatting?id=tolocalestring-strings-for-humans)指南。


### 获取两个日期之间的时间差 <a href="#get-the-time-between-two-dates" id="get-the-time-between-two-dates"></a>

要获取两个日期之间的时间差，请使用 Luxon 的 diffs 功能。它将一个日期减去另一个日期，并返回一段时长。

例如，获取两个日期之间相差的月数：

{% tabs %}
{% tab title="表达式（JavaScript）" %}
```js
{{DateTime.fromISO('2019-06-23').diff(DateTime.fromISO('2019-05-23'), 'months').toObject()}}
```

返回结果为 `[Object: {"months":1}]`。
{% endtab %}

{% tab title="Code 节点（JavaScript）" %}
```js
let monthsBetweenDates = DateTime.fromISO('2019-06-23').diff(DateTime.fromISO('2019-05-23'), 'months').toObject()
```

返回结果为 `{"months":1}`。
{% endtab %}
{% endtabs %}

更多信息请参阅 Luxon 的[日期差值（Diffs）](https://moment.github.io/luxon/#/math?id=diffs)说明。

### 一个较长的示例：距离圣诞节还有多少天？ <a href="#a-longer-example-how-many-days-to-christmas" id="a-longer-example-how-many-days-to-christmas"></a>

此示例结合了多种 Luxon 功能，使用 JMESPath，并执行一些基本的字符串操作。

场景：你希望实现一个到 12 月 25 日的倒计时。它每天告诉你距离圣诞节还剩多少天，并且每年都能自动适用，无需为下一年手动更新。

{% tabs %}
{% tab title="表达式（JavaScript）" %}
```js
{{"There are " + $today.diff(DateTime.fromISO($today.year + '-12-25'), 'days').toObject().days.toString().substring(1) + " days to Christmas!"}}
```
{% endtab %}

{% tab title="Code 节点（JavaScript）" %}
```js
let daysToChristmas = "There are " + $today.diff(DateTime.fromISO($today.year + '-12-25'), 'days').toObject().days.toString().substring(1) + " days to Christmas!";
```
{% endtab %}
{% endtabs %}

输出结果为 `"There are <number of days> days to Christmas!"`。例如，在 3 月 9 日执行时，输出 "There are 291 days to Christmas!"。

下面详细解释代码的作用：

* `{{` 和 `}}`：在表达式版本中，表示表达式的开始和结束。Code 节点版本不需要它们。
* `"There are "`：一个字符串。
* `+`：用于连接两个字符串。
* `$today.diff()`：与[获取两个日期之间的时间差](#get-the-time-between-two-dates)一节的示例类似，但使用了 n8n 的自定义变量 `$today`。
* `DateTime.fromISO($today.year + '-12-25'), 'days'`：这一部分通过 `$today.year` 获取当前年份，将其与月份和日期组合为 ISO 字符串，再把完整的 ISO 字符串转换为 Luxon DateTime 数据结构。同时，它指定 Luxon 以天为单位返回时长。
* `toObject()` 将 diff() 的结果转换为更易用的对象。此时，表达式返回 `[Object: {"days":-<number-of-days>}]`。例如，在 3 月 9 日执行时，返回 `[Object: {"days":-291}]`。
* `.days` 使用 JMESPath 语法，只从对象中提取天数。有关在 n8n 中使用 JMESPath 的更多信息，请参阅 [JMESPath 文档](query-json-data.md)。得到的结果是距离圣诞节的天数，值为负数。
* `.toString().substring(1)` 将数字转换为字符串，并去掉 `-`。
* `+ " days to Christmas!"`：另一个字符串，通过 `+` 与前面的字符串连接。

## 相关资源 <a id="related-resources"></a>

* [处理特殊数据类型](./)
* [处理文件和图片](work-with-files-and-images.md)
* [查询 JSON 数据](query-json-data.md)
