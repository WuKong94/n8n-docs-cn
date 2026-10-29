---
nodeTitle: DateTime（日期时间）
originalFilePath: data/expression-reference/datetime.md
originalUrl: https://docs.n8n.io/data/expression-reference/datetime
url: https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# DateTime（日期时间） <a href="#datetime" id="datetime"></a>

## _`DateTime`_.**`day`** <a href="#datetimeday" id="datetimeday"></a>

**说明：** 一个月中的第几天，取值为 1–31。

**语法：** _`DateTime`_.day

**返回值：** Number（数字）

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.day //=> 30
  ```

## _`DateTime`_.**`diffTo()`** <a href="#datetimediffto" id="datetimediffto"></a>

**说明：** 以指定单位返回两个 DateTime 之间的差值。

**语法：** _`DateTime`_.diffTo(otherDateTime, unit)

**返回值：** Number（数字）

**来源：** n8n 自定义功能

**参数：**

  * `otherDateTime `（String|DateTime）— 从此时刻减去基础 DateTime。可以是 ISO 日期字符串或 Luxon DateTime。
  * `unit `（String|Array<String>）— 可选 — 返回结果使用的单位或单位数组。可选值：<code>years</code>、<code>months</code>、<code>weeks</code>、<code>days</code>、<code>hours</code>、<code>minutes</code>、<code>seconds</code>、<code>milliseconds</code>。

**示例：**

  ```javascript
  // dt1 = "2024-03-30T18:49:07.234".toDateTime()
  dt1.diffTo('2025-01-01', 'days') //=> 276.21
  ```

  ```javascript
  // dt1 = "2024-03-30T18:49:07.234".toDateTime()
  // dt2 = "2025-01-01T00:00:00.000".toDateTime()
  dt1.diffTo(dt2, ['months', 'days']) //=> {'months':, 'days':}
  ```

  ```javascript
  Note: should support both day and days, etc.
  ```

## _`DateTime`_.**`diffToNow()`** <a href="#datetimedifftonow" id="datetimedifftonow"></a>

**说明：** 以指定单位返回当前时刻与该 DateTime 之间的差值。如果需要文本形式，请使用 <code>toRelative()</code>。

**语法：** _`DateTime`_.diffToNow(unit)

**返回值：** Number（数字）

**来源：** n8n 自定义功能

**参数：**

  * `unit `（String|Array<String>）— 可选 — 返回结果使用的单位或单位数组。可选值：<code>years</code>、<code>months</code>、<code>weeks</code>、<code>days</code>、<code>hours</code>、<code>minutes</code>、<code>seconds</code>、<code>milliseconds</code>。

**示例：**

  ```javascript
  // dt = "2023-03-30T18:49:07.234".toDateTime()
  dt.diffToNow('days') //=> 371.9
  ```

  ```javascript
  // dt = "2023-03-30T18:49:07.234".toDateTime()
  dt.diffToNow(['months', 'days']) //=> {"months":12, "days":5.9}
  ```

  ```javascript
  Note: should support both day and days, etc.
  ```

## _`DateTime`_.**`endOf()`** <a href="#datetimeendof" id="datetimeendof"></a>

**说明：** 将 DateTime 向上调整到指定单位的结束时刻，例如月末。

**语法：** _`DateTime`_.endOf(unit, opts)

**返回值：** DateTime

**类型：** Luxon

**参数：**

  * `unit `（String）— 要调整到其结束时刻的单位。可选值：<code>year</code>、<code>quarter</code>、<code>month</code>、<code>week</code>、<code>day</code>、<code>hour</code>、<code>minute</code>、<code>second</code> 或 <code>millisecond</code>。
  * `opts `（Object）— 可选 — 包含影响输出结果的选项的对象。可用属性：
<code>useLocaleWeeks</code>（boolean）：计算一周起始日期时，是否遵循区域设置。默认为 false。

**示例：**

  ```javascript
  // dt = "2024-03-20T18:49".toDateTime()
  dt.endOf('month') //=> 2024-03-31T23:59
  ```

## _`DateTime`_.**`equals()`** <a href="#datetimeequals" id="datetimeequals"></a>

**说明：** 返回 <code>true</code> 表示两个 DateTime 代表完全相同的时刻，且时区相同。如需较宽松的比较，请使用 <code>hasSame()</code>。

**语法：** _`DateTime`_.equals(other)

**返回值：** Boolean（布尔值）

**类型：** Luxon

**参数：**

  * `other `（DateTime）— 用于比较的另一个 DateTime。

**示例：**

  ```javascript
  // dt1 = "2024-03-20T18:49+01:00".toDateTime()
  // dt2 = "2024-03-20T19:49+02:00".toDateTime()
  dt1.equals(dt2) //=> false
  ```

## _`DateTime`_.**`extract()`** <a href="#datetimeextract" id="datetimeextract"></a>

**说明：** 以数字形式提取日期或时间的某一部分，例如月份。如需提取文本名称，请参阅 <code>format()</code>。

**语法：** _`DateTime`_.extract(unit?)

**返回值：** Number（数字）

**来源：** n8n 自定义功能

**参数：**

  * `unit`（String）— 可选 — 要返回的日期或时间部分。可选值：<code>year</code>、<code>month</code>、<code>week</code>、<code>day</code>、<code>hour</code>、<code>minute</code>、<code>second</code>。

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.extract('month') //=> 3
  ```

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.extract('hour') //=> 18
  ```

## _`DateTime`_.**`format()`** <a href="#datetimeformat" id="datetimeformat"></a>

**说明：** 使用指定格式将 DateTime 转换为字符串。参阅<a href="https://moment.github.io/luxon/#/formatting?id=table-of-tokens">格式化指南</a>。对于常见格式，使用 <code>toLocaleString()</code> 可能更方便。

**语法：** _`DateTime`_.format(fmt)

**返回值：** String（字符串）

**来源：** n8n 自定义功能

**参数：**

  * `fmt`（String）— 要返回的字符串<a href="https://moment.github.io/luxon/#/formatting?id=table-of-tokens">格式</a>。

**示例：**

  ```javascript
  // dt = "2024-04-30T18:49".toDateTime()
  dt.format('dd/LL/yyyy') //=> '30/04/2024'
  ```

  ```javascript
  // dt = "2024-04-30T18:49".toDateTime()
  dt.format('dd LLL yy') //=> '30 Apr 24'
  dt.setLocale('fr').format('dd LLL yyyy') //=> '30 avr. 2024'
  dt.format("HH 'hours and' mm 'minutes'") //=> '18 hours and 49 minutes'
  ```

{% hint style="warning" %}
**在 Code 节点中不可用**

`format()` 是 n8n 为表达式编辑器中的 Luxon `DateTime` 对象添加的自定义扩展。Code 节点脚本使用未经修改的原生 Luxon，因此不提供此方法。在 Code 节点中调用会抛出 `... .format is not a function`。

请改用 Luxon 原生的 [`toFormat()`](https://moment.github.io/luxon/api-docs/index.html#datetimetoformat)：

```javascript
// In the Code node
DateTime.now().toFormat('dd/LL/yyyy'); //=> '30/04/2024'
```

这一点也适用于本页标为**来源：n8n 自定义功能**的其他方法：它们在表达式中可用，例如 Set 节点中的表达式，但在 Code 节点中可能不可用。更多区别请参阅[内置方法和变量](../../../code-in-n8n/use-built-in-shortcuts.md)。
{% endhint %}

## _`DateTime`_.**`hasSame()`** <a href="#datetimehassame" id="datetimehassame"></a>

**说明：** 返回 <code>true</code> 表示两个 DateTime 在指定单位及更大单位上相同。忽略时区，仅比较本地时间，因此必要时请先使用 <code>toUTC()</code>。

**语法：** _`DateTime`_.hasSame(otherDateTime, unit)

**返回值：** Boolean（布尔值）

**类型：** Luxon

**参数：**

  * `otherDateTime `（DateTime）— 用于比较的另一个 DateTime。
  * `unit `（String）— 比较相同与否时使用的最小时间单位。可选值：<code>year</code>、<code>quarter</code>、<code>month</code>、<code>week</code>、<code>day</code>、<code>hour</code>、<code>minute</code>、<code>second</code> 或 <code>millisecond</code>。

**示例：**

  ```javascript
  // dt1 = "2024-03-20".toDateTime()
  // dt2 = "2024-03-18".toDateTime()
  dt1.hasSame(dt2, 'month') //=> true
  ```

  ```javascript
  // dt1 = "1982-03-20".toDateTime()
  // dt2 = "2024-03-18".toDateTime()
  dt1.hasSame(dt2, 'month') //=> false
  ```

## _`DateTime`_.**`hour`** <a href="#datetimehour" id="datetimehour"></a>

**说明：** 一天中的小时数，取值为 0–23。

**语法：** _`DateTime`_.hour

**返回值：** Number（数字）

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.hour //=> 18
  ```

## _`DateTime`_.**`isBetween()`** <a href="#datetimeisbetween" id="datetimeisbetween"></a>

**说明：** 返回 <code>true</code> 表示 DateTime 位于指定的两个时刻之间。

**语法：** _`DateTime`_.isBetween(date1, date2)

**返回值：** Boolean（布尔值）

**来源：** n8n 自定义功能

**参数：**

  * `date1`（String|DateTime）— 基础 DateTime 必须晚于的时刻。可以是 ISO 日期字符串或 Luxon DateTime。
  * `date2`（String|DateTime）— 基础 DateTime 必须早于的时刻。可以是 ISO 日期字符串或 Luxon DateTime。

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.isBetween('2020-06-01', '2025-06-01') //=> true
  ```

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.isBetween('2020', $now) //=> true
  ```

## _`DateTime`_.**`isEmpty()`** <a href="#datetimeisempty" id="datetimeisempty"></a>

**说明：** 对所有 DateTime 返回 <code>false</code>。返回 <code>true</code> 的情况是值为 <code>null</code> 或 <code>undefined</code>。

**语法：** _`DateTime`_.isEmpty()

**返回值：** Boolean（布尔值）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // dt = '2023-03-30T18:49:07.234'.toDateTime()
  dt.isEmpty() // => false
  ```

  ```javascript
  // dt = null
  dt.isEmpty() // => true
  ```

## _`DateTime`_.**`isInDST`** <a href="#datetimeisindst" id="datetimeisindst"></a>

**说明：** DateTime 是否处于夏令时。

**语法：** _`DateTime`_.isInDST

**返回值：** Boolean（布尔值）

**类型：** Luxon

## _`DateTime`_.**`isNotEmpty()`** <a href="#datetimeisnotempty" id="datetimeisnotempty"></a>

**说明：** 对所有 DateTime 返回 <code>true</code>。返回 <code>false</code> 的情况是值为 <code>null</code> 或 <code>undefined</code>。

**语法：** _`DateTime`_.isNotEmpty()

**返回值：** Boolean（布尔值）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // dt = '2023-03-30T18:49:07.234'.toDateTime()
  dt.isNotEmpty() // => true
  ```

  ```javascript
  // dt = null
  dt.isNotEmpty() // => false
  ```

## _`DateTime`_.**`locale`** <a href="#datetimelocale" id="datetimelocale"></a>

**说明：** DateTime 的区域设置，例如 ‘en-GB’。格式化 DateTime 时会使用该区域设置。

**语法：** _`DateTime`_.locale

**返回值：** String（字符串）

**类型：** Luxon

**示例：**

  ```javascript
  $now.locale //=> 'en-US'
  ```

## _`DateTime`_.**`millisecond`** <a href="#datetimemillisecond" id="datetimemillisecond"></a>

**说明：** 一秒中的毫秒数，取值为 0–999。

**语法：** _`DateTime`_.millisecond

**返回值：** Number（数字）

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49:07.234".toDateTime()
  dt.millisecond //=> 234
  ```

## _`DateTime`_.**`minus()`** <a href="#datetimeminus" id="datetimeminus"></a>

**说明：** 从 DateTime 中减去指定时长。

**语法：** _`DateTime`_.minus(n, unit?)

**返回值：** DateTime

**来源：** n8n 自定义功能

**参数：**

  * `n`（Number|Object）— 要减去的单位数量。也可以使用 Luxon <a href=”https://moment.github.io/luxon/api-docs/index.html#duration”>Duration</a> 对象，一次减去多个单位的时长。
  * `unit`（String）— 可选 — 数字对应的单位。可选值：<code>years</code>、<code>months</code>、<code>weeks</code>、<code>days</code>、<code>hours</code>、<code>minutes</code>、<code>seconds</code>、<code>milliseconds</code>。

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.minus(7, 'days') //=> 2024-04-23T18:49
  ```

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.minus(4, 'years') //=> 2020-04-30T18:49
  ```

{% hint style="info" %}
**Code 节点：** Code 节点也提供 Luxon 原生的 `DateTime.prototype.minus()`，但只接受一个 [Duration 类对象](https://moment.github.io/luxon/api-docs/index.html#datetimeminus)，例如 `dt.minus({ days: 7 })`，不支持本页仅适用于 n8n 的 `(n, unit)` 简写。在 Code 节点中传入 `dt.minus(7, 'days')` 不会报错，但也不会减去 7 天。如果在 Code 节点中使用此签名，请仔细检查结果。
{% endhint %}

## _`DateTime`_.**`minute`** <a href="#datetimeminute" id="datetimeminute"></a>

**说明：** 一小时中的分钟数，取值为 0–59。

**语法：** _`DateTime`_.minute

**返回值：** Number（数字）

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.minute //=> 49
  ```

## _`DateTime`_.**`month`** <a href="#datetimemonth" id="datetimemonth"></a>

**说明：** 月份，取值为 1–12。

**语法：** _`DateTime`_.month

**返回值：** Number（数字）

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.month //=> 3
  ```

## _`DateTime`_.**`monthLong`** <a href="#datetimemonthlong" id="datetimemonthlong"></a>

**说明：** 完整的月份名称，例如 ‘October’。未指定区域设置时，默认使用系统区域设置。

**语法：** _`DateTime`_.monthLong

**返回值：** String（字符串）

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.monthLong //=> 'March'
  ```

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.setLocale('de-DE').monthLong //=> 'März'
  ```

## _`DateTime`_.**`monthShort`** <a href="#datetimemonthshort" id="datetimemonthshort"></a>

**说明：** 缩写的月份名称，例如 ‘Oct’。未指定区域设置时，默认使用系统区域设置。

**语法：** _`DateTime`_.monthShort

**返回值：** String（字符串）

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.monthShort //=> 'Mar'
  ```

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.setLocale('de-DE').monthShort //=> 'Mär'
  ```

## _`DateTime`_.**`plus()`** <a href="#datetimeplus" id="datetimeplus"></a>

**说明：** 为 DateTime 加上指定时长。

**语法：** _`DateTime`_.plus(n, unit?)

**返回值：** DateTime

**来源：** n8n 自定义功能

**参数：**

  * `n`（Number|Object）— 要增加的单位数量。也可以使用 Luxon <a href=”https://moment.github.io/luxon/api-docs/index.html#duration”>Duration</a> 对象，一次增加多个单位的时长。
  * `unit`（String）— 可选 — 数字对应的单位。可选值：<code>years</code>、<code>months</code>、<code>weeks</code>、<code>days</code>、<code>hours</code>、<code>minutes</code>、<code>seconds</code>、<code>milliseconds</code>。

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.plus(7, 'days') //=> 2024-04-06T18:49
  ```

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.plus(4, 'years') //=> 2028-04-30T18:49
  ```

{% hint style="info" %}
**Code 节点：** Code 节点也提供 Luxon 原生的 `DateTime.prototype.plus()`，但只接受一个 [Duration 类对象](https://moment.github.io/luxon/api-docs/index.html#datetimeplus)，例如 `dt.plus({ days: 7 })`，不支持本页仅适用于 n8n 的 `(n, unit)` 简写。在 Code 节点中传入 `dt.plus(7, 'days')` 不会报错，但也不会加上 7 天。如果在 Code 节点中使用此签名，请仔细检查结果。
{% endhint %}

## _`DateTime`_.**`quarter`** <a href="#datetimequarter" id="datetimequarter"></a>

**说明：** 一年中的季度，取值为 1–4。

**语法：** _`DateTime`_.quarter

**返回值：** Number（数字）

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.quarter //=> 1
  ```

## _`DateTime`_.**`second`** <a href="#datetimesecond" id="datetimesecond"></a>

**说明：** 一分钟中的秒数，取值为 0–59。

**语法：** _`DateTime`_.second

**返回值：** Number（数字）

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49:07.234".toDateTime()
  dt.second //=> 7
  ```

## _`DateTime`_.**`set()`** <a href="#datetimeset" id="datetimeset"></a>

**说明：** 为 DateTime 的指定单位赋予新值。如需将 DateTime 调整到单位起点或终点，另请参阅 <code>startOf()</code> 和 <code>endOf()</code>。

**语法：** _`DateTime`_.set(values)

**返回值：** DateTime

**类型：** Luxon

**参数：**

  * `values `（Object）— 包含要设置的单位及相应值的对象。可用键：<code>year</code>、<code>month</code>、<code>day</code>、<code>hour</code>、<code>minute</code>、<code>second</code> 和 <code>millsecond</code>。

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.set({year:1982, month:10}) //=> 1982-10-20T18:49
  ```

## _`DateTime`_.**`setLocale()`** <a href="#datetimesetlocale" id="datetimesetlocale"></a>

**说明：** 设置区域，决定 DateTime 使用的语言和格式。生成 DateTime 的文本表示时很有用，例如使用 <code>format()</code> 或 <code>toLocaleString()</code> 时。

**语法：** _`DateTime`_.setLocale(locale)

**返回值：** DateTime

**类型：** Luxon

**参数：**

  * `locale `（String）— 要使用的区域设置，例如 ‘en-GB’ 表示英式英语，‘pt-BR’ 表示巴西葡萄牙语。<a href=”https://www.localeplanet.com/icu/”>列表</a>（非官方）。

**示例：**

  ```javascript
  $now.setLocale('de-DE').toLocaleString({'dateStyle':'long'}) //=> 5. Oktober 2024
  ```

  ```javascript
  $now.setLocale('fr-FR').toLocaleString({'dateStyle':'long'}) //=> 5 octobre 2024
  ```

## _`DateTime`_.**`setZone()`** <a href="#datetimesetzone" id="datetimesetzone"></a>

**说明：** 将 DateTime 转换为指定时区。除非通过选项另行指定，DateTime 仍表示同一时刻。另请参阅 <code>toLocal()</code> 和 <code>toUTC()</code>。

**语法：** _`DateTime`_.setZone(zone, opts)

**返回值：** DateTime

**类型：** Luxon

**参数：**

  * `zone `（String）— 可选 — 时区标识符，可以使用 ‘America/New_York’、‘UTC+3’ 格式，或字符串 ‘local’、‘utc’。
  * `opts `（Object）— 可选 — 影响输出结果的选项。可用属性：
<code>keepCalendarTime</code>（boolean）：是否保持本地日期时间不变，仅修改时区偏移量。默认为 false。

**示例：**

  ```javascript
  // dt = "2024-01-01T00:00:00.000+02:00".toDateTime()
  dt.setZone('America/Buenos_aires') //=> 2023-12-31T19:00:00.000-03:00
  ```

  ```javascript
  // dt = "2024-01-01T00:00:00.000+02:00".toDateTime()
  dt.setZone('UTC+7') //=> 2024-01-01T05:00:00.000+07:00
  ```

## _`DateTime`_.**`startOf()`** <a href="#datetimestartof" id="datetimestartof"></a>

**说明：** 将 DateTime 向下调整到指定单位的起始时刻，例如月初。

**语法：** _`DateTime`_.startOf(unit, opts)

**返回值：** DateTime

**类型：** Luxon

**参数：**

  * `unit `（String）— 要调整到其起始时刻的单位。可选值：<code>year</code>、<code>quarter</code>、<code>month</code>、<code>week</code>、<code>day</code>、<code>hour</code>、<code>minute</code>、<code>second</code> 或 <code>millisecond</code>。
  * `opts `（Object）— 可选 — 包含影响输出结果的选项的对象。可用属性：
<code>useLocaleWeeks</code>（boolean）：计算一周起始日期时，是否遵循区域设置。默认为 false。

**示例：**

  ```javascript
  // dt = "2024-03-20T18:49".toDateTime()
  dt.startOf('month') //=> 2024-03-01T00:00
  ```

## _`DateTime`_.**`toISO()`** <a href="#datetimetoiso" id="datetimetoiso"></a>

**说明：** 返回符合 ISO 8601 标准的 DateTime 字符串表示。

**语法：** _`DateTime`_.toISO(opts)

**返回值：** String（字符串）

**类型：** Luxon

**参数：**

  * `opts `（Object）— 可选 — 配置选项。更多信息请参阅 <a href=”https://moment.github.io/luxon/api-docs/index.html#datetimetoiso”>Luxon 文档</a>。

**示例：**

  ```javascript
  $now.toISO() //=> 2024-04-05T18:44:55.525+02:00
  ```

## _`DateTime`_.**`toLocal()`** <a href="#datetimetolocal" id="datetimetolocal"></a>

**说明：** 将 DateTime 转换为工作流的本地时区。除非通过参数另行指定，DateTime 仍表示同一时刻。可以在工作流设置中设置时区。

**语法：** _`DateTime`_.toLocal()

**返回值：** DateTime

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-01-01T00:00:00.000Z".toDateTime()
  dt.toLocal() //=> 2024-01-01T01:00:00.000+01:00, if time zone is Europe/Berlin
  ```

## _`DateTime`_.**`toLocaleString()`** <a href="#datetimetolocalestring" id="datetimetolocalestring"></a>

**说明：** 返回 DateTime 的本地化字符串，即使用对应区域的语言和格式。未指定区域时，默认使用系统区域设置。

**语法：** _`DateTime`_.toLocaleString(formatOpts)

**返回值：** String（字符串）

**类型：** Luxon

**参数：**

  * `formatOpts `（Object）— 可选 — 显示结果的配置选项。完整列表请参阅 <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#parameters”>Intl.DateTimeFormat</a>。默认显示简短日期。

**示例：**

  ```javascript
  $now.toLocaleString() //=> '4/30/2024'
  $now.toLocaleString({'dateStyle':'medium', 'timeStyle':'short'}) //=> 'Apr 30, 2024, 10:00 PM'
  // (if in US English locale)
  ```

  ```javascript
  $now.setLocale('de-DE').toLocaleString() //=> '30.4.2024'
  ```

  ```javascript
  $now.toLocaleString({'dateStyle':'short'}) //=> '4/30/2024'
  $now.toLocaleString({'dateStyle':'medium'}) //=> 'Apr 30, 2024'
  $now.toLocaleString({'dateStyle':'long'}) //=> 'April 30, 2024'
  $now.toLocaleString({'dateStyle':'full'}) //=> 'Tuesday, April 30, 2024'
  // (if in US English locale)
  ```

  ```javascript
  $now.toLocaleString({'year':'numeric', 'month':'numeric', 'day':'numeric'}) //=> '4/30/2024'
  $now.toLocaleString({'year':'2-digit', 'month':'2-digit', 'day':'2-digit'}) //=> '04/30/24'
  $now.toLocaleString({'month':'short', 'weekday':'short', 'day':'numeric'}) //=> 'Tue, Apr 30'
  $now.toLocaleString({'month':'long', 'weekday':'long', 'day':'numeric'}) //=> 'Tuesday, April 30'
  // (if in US English locale)
  ```

  ```javascript
  $now.toLocaleString({'timeStyle':'short'}) //=> '10:00 PM'
  $now.toLocaleString({'timeStyle':'medium'}) //=> '10:00:58 PM'
  $now.toLocaleString({'timeStyle':'long'}) //=> '10:00:58 PM GMT+2'
  $now.toLocaleString({'timeStyle':'full'}) //=> '10:00:58 PM Central European Summer Time'
  // (if in US English locale)
  ```

  ```javascript
  $now.toLocaleString({'hour':'numeric', 'minute':'numeric', hourCycle:'h24'}) //=> '22:00'
  $now.toLocaleString({'hour':'2-digit', 'minute':'2-digit', hourCycle:'h12'}) //=> '10:00 PM'
  // (if in US English locale)
  ```

## _`DateTime`_.**`toMillis()`** <a href="#datetimetomillis" id="datetimetomillis"></a>

**说明：** 返回以毫秒为单位的 Unix 时间戳，即自 1970 年 1 月 1 日起经过的毫秒数。

**语法：** _`DateTime`_.toMillis()

**返回值：** Number（数字）

**类型：** Luxon

**示例：**

  ```javascript
  $now.toMillis() //=> 1712334324677
  ```

## _`DateTime`_.**`toRelative()`** <a href="#datetimetorelative" id="datetimetorelative"></a>

**说明：** 返回相对于当前时刻的时间文本，例如 ‘in two days’（两天后）。默认向下取整。

**语法：** _`DateTime`_.toRelative(options)

**返回值：** String（字符串）

**类型：** Luxon

**参数：**

  * `options `（Object）— 可选 — 影响输出结果的选项。可用属性：
<code>unit</code> = 默认使用的单位，例如 <code>years</code>、<code>months</code>、<code>days</code> 等。
<code>locale</code> = 使用的语言和格式，例如 <code>de</code>、<code>fr</code>。

**示例：**

  ```javascript
  $now.plus(1, 'day').toRelative() //=> "in 1 day"
  ```

  ```javascript
  $now.plus(1, 'day').toRelative({unit:'hours'}) //=> "in 24 hours"
  ```

  ```javascript
  $now.plus(1, 'day').toRelative({locale:'es'}) //=> "dentro de 1 día"
  ```

## _`DateTime`_.**`toSeconds()`** <a href="#datetimetoseconds" id="datetimetoseconds"></a>

**说明：** 返回以秒为单位的 Unix 时间戳，即自 1970 年 1 月 1 日起经过的秒数。

**语法：** _`DateTime`_.toSeconds()

**返回值：** Number（数字）

**类型：** Luxon

**示例：**

  ```javascript
  $now.toSeconds() //=> 1712334442.372
  ```

## _`DateTime`_.**`toString()`** <a href="#datetimetostring" id="datetimetostring"></a>

**说明：** 返回 DateTime 的字符串表示，与 <code>toISO()</code> 类似。更多格式化选项请参阅 <code>format()</code> 或 <code>toLocaleString()</code>。

**语法：** _`DateTime`_.toString()

**返回值：** string（字符串）

**类型：** Luxon

**示例：**

  ```javascript
  $now.toString() //=> 2024-04-05T18:44:55.525+02:00
  ```

## _`DateTime`_.**`toUTC()`** <a href="#datetimetoutc" id="datetimetoutc"></a>

**说明：** 将 DateTime 转换为 UTC 时区。除非通过参数另行指定，DateTime 仍表示同一时刻。转换到其他时区请使用 <code>setZone()</code>。

**语法：** _`DateTime`_.toUTC(offset, opts)

**返回值：** DateTime

**类型：** Luxon

**参数：**

  * `offset `（Number）— 可选 — 相对于 UTC 的偏移量，以分钟为单位。
  * `opts `（Object）— 可选 — 包含影响输出结果的选项的对象。可用属性：
<code>keepCalendarTime</code>（boolean）：是否保持本地日期时间不变，仅修改时区偏移量。默认为 false。

**示例：**

  ```javascript
  // dt = "2024-01-01T00:00:00.000+02:00".toDateTime()
  dt.toUTC() //=> 2023-12-31T22:00:00.000Z
  ```

## _`DateTime`_.**`weekday`** <a href="#datetimeweekday" id="datetimeweekday"></a>

**说明：** 星期几。1 表示星期一，7 表示星期日。

**语法：** _`DateTime`_.weekday

**返回值：** Number（数字）

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.weekday //=> 6
  ```

## _`DateTime`_.**`weekdayLong`** <a href="#datetimeweekdaylong" id="datetimeweekdaylong"></a>

**说明：** 完整的星期名称，例如 ‘Wednesday’。未指定区域设置时，默认使用系统区域设置。

**语法：** _`DateTime`_.weekdayLong

**返回值：** String（字符串）

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.weekdayLong //=> 'Saturday'
  ```

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.setLocale('de-DE').weekdayLong //=> 'Samstag'
  ```

## _`DateTime`_.**`weekdayShort`** <a href="#datetimeweekdayshort" id="datetimeweekdayshort"></a>

**说明：** 缩写的星期名称，例如 ‘Wed’。未指定区域设置时，默认使用系统区域设置。

**语法：** _`DateTime`_.weekdayShort

**返回值：** String（字符串）

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.weekdayShort //=> 'Sat'
  ```

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.setLocale('fr-FR').weekdayShort //=> 'sam.'
  ```

## _`DateTime`_.**`weekNumber`** <a href="#datetimeweeknumber" id="datetimeweeknumber"></a>

**说明：** 一年中的周数，大致取值为 1–52。

**语法：** _`DateTime`_.weekNumber

**返回值：** Number（数字）

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.weekNumber //=> 13
  ```

## _`DateTime`_.**`year`** <a href="#datetimeyear" id="datetimeyear"></a>

**说明：** 年份。

**语法：** _`DateTime`_.year

**返回值：** Number（数字）

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.year //=> 2024
  ```

## _`DateTime`_.**`zone`** <a href="#datetimezone" id="datetimezone"></a>

**说明：** 与 DateTime 关联的时区。

**语法：** _`DateTime`_.zone

**返回值：** Object（对象）

**类型：** Luxon

**示例：**

  ```javascript
  $now.zone //=> {"zoneName": "Europe/Berlin", "valid": true}
  ```
## 相关资源 <a id="related-resources"></a>

* [表达式参考](./)
