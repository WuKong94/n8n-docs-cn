---
nodeTitle: 表达式参考
originalFilePath: data/expression-reference/index.md
originalUrl: https://docs.n8n.io/data/expression-reference
url: https://docs.n8n.io/build/work-with-data/transform-data/expression-reference
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# 表达式参考 <a href="#expression-reference" id="expression-reference"></a>

以下是一些常用表达式。下方还列出了更全面的参考。

## 本节内容 <a id="in-this-section"></a>

* [Array](array.md)：处理数组的方法。
* [BinaryFile](binaryfile.md)：二进制文件数据的属性。
* [Boolean](boolean.md)：处理布尔值的方法。
* [CustomData](customdata.md)：获取和设置自定义执行数据的方法。
* [Date](date.md)：转换 JavaScript Date 的方法。
* [DateTime](datetime.md)：处理 Luxon DateTime 的方法和属性。
* [ExecData](execdata.md)：当前执行的属性。
* [HTTPResponse](httpresponse.md)：最近一次 HTTP 调用的响应属性。
* [Item](item.md)：当前数据项的属性。
* [NodeInputData](nodeinputdata.md)：读取当前节点输入的方法。
* [NodeOutputData](nodeoutputdata.md)：读取节点输出的方法。
* [Number](number.md)：处理数字的方法。
* [Object](object.md)：处理对象的方法。
* [PrevNodeData](prevnodedata.md)：描述输入来源节点的属性。
* [Root](root.md)：顶层变量和辅助函数，例如 `$json` 和 `$now`。
* [String](string.md)：处理字符串的方法。
* [WorkflowData](workflowdata.md)：当前工作流的属性。

| 类别 | 表达式 | 说明 |
|---|---|---|
| 访问当前输入数据项的数据 | `$json` | 当前数据项的 JSON 数据 |
| | `$json.fieldName` | 当前数据项的字段 |
| | `$binary` | 当前数据项的二进制数据 |
| 访问前面节点的数据 | `$("NodeName").first()` | 节点中的第一个数据项 |
| | `$("NodeName").item` | 节点中关联的数据项。更多信息请参阅[数据项关联](../../reference-data/link-data-items/README.md)。 |
| | `$("NodeName").all()` | 节点中的所有数据项 |
| | `$("NodeName").last()` | 节点中的最后一个数据项 |
| 日期与时间 | `$now` | 当前日期和时间 |
| | `$today` | 今天的日期 |
| | `$now.toFormat("yyyy-MM-dd")` | 将当前日期格式化为字符串 |
| 条件判断 | `$if(condition, "true", "false")` | 根据条件为真或假返回相应值的辅助函数 |
| | `condition ? true : false` | 三元运算符：条件为真时返回一个值，为假时返回另一个值 |
| | `$ifEmpty(value, defaultValue)` | 此辅助函数接收两个参数，检查第一个参数是否为空；不为空时返回第一个参数，为空时返回第二个参数。以下情况视为空：`undefined`、`null`、空字符串 `''`、调用 `value.length` 返回 `false` 的数组，或调用 `Object.keys(value).length` 返回 `false` 的对象。 |
| 字符串方法 | `text.toUpperCase()` | 转换为大写 |
| | `text.toLowerCase()` | 转换为小写 |
| | `text.includes("foo")` | 检查文本是否包含搜索内容 |
| | `text.extractEmail()` | 从文本中提取电子邮件地址 |
| 数组方法 | `array.length` | 获取数组长度 |
| | `array.join(", ")` | 使用逗号作为分隔符连接数组元素 |
| | `array.filter(x => x <= 20)` | 根据过滤条件筛选数组元素 |
| | `array.map(x => x.id)` | 转换数组元素 |

下方表格按操作对象的数据类型列出了方法。点击方法名称，可查看详细文档。

## Array（数组） <a href="#array" id="array"></a>

* [_`Array`_.**`append(elem1, elem2?, ..., elemN?)`**](array.md#arrayappend)

    将新元素添加到数组末尾。与 <code>push()</code> 类似，但返回修改后的数组。也可以考虑改用展开语法，参见示例。

* [_`Array`_.**`average()`**](array.md#arrayaverage)

    返回数组中数字的平均值。如果存在非数字元素，则抛出错误。

* [_`Array`_.**`chunk(length)`**](array.md#arraychunk)

    将数组拆分为由指定长度的子数组组成的数组。

* [_`Array`_.**`compact()`**](array.md#arraycompact)

    删除数组中的空值。<code>null</code>、<code>""</code> 和 <code>undefined</code> 均视为空。

* [_`Array`_.**`concat(array2, array3?, ... arrayN?)`**](array.md#arrayconcat)

    将一个或多个数组连接到基础数组末尾。

* [_`Array`_.**`difference(otherArray)`**](array.md#arraydifference)

    比较两个数组。返回基础数组中存在、但未包含在
<code>otherArray</code> 中的所有元素。

* [_`Array`_.**`filter(function(element, index?, array?), thisValue?)`**](array.md#arrayfilter)

    返回仅包含满足条件的元素的数组。条件是一个返回 <code>true</code> 或 <code>false</code> 的函数。

* [_`Array`_.**`find(function(element, index?, array?), thisValue?)`**](array.md#arrayfind)

    返回数组中满足指定条件的第一个元素。条件是一个返回 <code>true</code> 或 <code>false</code> 的函数。如果没有匹配项，则返回 <code>undefined</code>。

如果需要所有匹配的元素，请使用 <code>filter()</code>。

* [_`Array`_.**`first()`**](array.md#arrayfirst)

    返回数组的第一个元素。

* [_`Array`_.**`includes(element, start?)`**](array.md#arrayincludes)

    返回 <code>true</code> 表示数组包含指定元素。

* [_`Array`_.**`indexOf(element, start?)`**](array.md#arrayindexof)

    返回数组中第一个匹配元素的位置，未找到时返回 -1。位置从 0 开始。

* [_`Array`_.**`intersection(otherArray)`**](array.md#arrayintersection)

    比较两个数组。返回基础数组中也存在于另一个数组中的所有元素。

* [_`Array`_.**`isEmpty()`**](array.md#arrayisempty)

    返回 <code>true</code> 的情况是数组没有元素，或数组为 <code>null</code> 或 <code>undefined</code>。

* [_`Array`_.**`isNotEmpty()`**](array.md#arrayisnotempty)

    返回 <code>true</code> 表示数组至少包含一个元素。

* [_`Array`_.**`join(separator?)`**](array.md#arrayjoin)

    将数组中的所有元素合并为一个字符串，可选择在各元素之间插入分隔符。

与 <code>split()</code> 的作用相反。

* [_`Array`_.**`last()`**](array.md#arraylast)

    返回数组的最后一个元素。

* [_`Array`_.**`length`**](array.md#arraylength)

    数组中的元素数量。

* [_`Array`_.**`map(function(element, index?, array?), thisValue?)`**](array.md#arraymap)

    对原数组中的每个元素应用一个函数，创建新数组。

* [_`Array`_.**`max()`**](array.md#arraymax)

    返回数组中的最大数字。如果存在非数字元素，则抛出错误。

* [_`Array`_.**`min()`**](array.md#arraymin)

    返回数组中的最小数字。如果存在非数字元素，则抛出错误。

* [_`Array`_.**`pluck(fieldName1?, fieldName2?, …)`**](array.md#arraypluck)

    返回一个数组，其中包含原数组中各对象的指定字段值。忽略非对象元素，以及没有与指定字段名匹配的键的对象。

* [_`Array`_.**`randomItem()`**](array.md#arrayrandomitem)

    返回从数组中随机选择的一个元素。

* [_`Array`_.**`reduce(function(prevResult, currentElem, currentIndex?, array?), initResult)`**](array.md#arrayreduce)

    对数组中的每个元素应用一个函数，将数组归约为单个值。该函数将当前元素与之前元素的归约结果结合，生成新的结果。

* [_`Array`_.**`removeDuplicates(keys?)`**](array.md#arrayremoveduplicates)

    删除数组中重复出现的元素。

* [_`Array`_.**`renameKeys(from, to)`**](array.md#arrayrenamekeys)

    修改数组中各对象的所有匹配键（字段名）。如需重命名多个键，可以
添加更多参数，即 <code>from1, to1, from2, to2, ...</code>。

* [_`Array`_.**`reverse()`**](array.md#arrayreverse)

    反转数组中元素的顺序。

* [_`Array`_.**`slice(start, end)`**](array.md#arrayslice)

    返回数组中从 <code>start</code> 索引开始，到 <code>end</code> 索引之前的一段元素，不包含结束索引处的元素。索引从 0 开始。

* [_`Array`_.**`smartJoin(keyField, nameField)`**](array.md#arraysmartjoin)

    根据对象数组创建单个对象。数组中的每个对象为返回对象提供一个字段。数组中的每个对象都必须包含一个提供键名的字段和一个提供值的字段。

* [_`Array`_.**`sort(compareFunction(a, b)?)`**](array.md#arraysort)

    对数组中的元素重新排序。按字母顺序排列字符串时，不需要参数。数字或对象的排序方法请参阅示例。

* [_`Array`_.**`sum()`**](array.md#arraysum)

    返回数组中所有数字的总和。如果存在非数字元素，则抛出错误。

* [_`Array`_.**`toJsonString()`**](array.md#arraytojsonstring)

    将数组转换为 JSON 字符串。与 JavaScript 的 <code>JSON.stringify()</code> 相同。

* [_`Array`_.**`toSpliced(start, deleteCount, elem1, ....., elemN)`**](array.md#arraytospliced)

    在指定位置添加或删除数组元素。

另请参阅 <code>slice()</code> 和 <code>append()</code>。

* [_`Array`_.**`toString()`**](array.md#arraytostring)

    将数组转换为字符串，各值以逗号分隔。如果要使用其他分隔符，请使用 <code>join()</code>。

* [_`Array`_.**`union(otherArray)`**](array.md#arrayunion)

    连接两个数组，并删除重复元素。

* [_`Array`_.**`unique()`**](array.md#arrayunique)

    删除数组中的重复元素。


## BinaryFile（二进制文件） <a href="#binaryfile" id="binaryfile"></a>

* [`binaryFile`.**`directory`**](binaryfile.md#binaryfiledirectory)

    文件所在目录的路径，可用于区分不同目录中的同名文件。如果 n8n 配置为将文件存储在数据库中，则不设置此值。

* [`binaryFile`.**`fileExtension`**](binaryfile.md#binaryfilefileextension)

    文件名末尾的后缀，例如 <code>txt</code>。

* [`binaryFile`.**`fileName`**](binaryfile.md#binaryfilefilename)

    文件名，包含扩展名。

* [`binaryFile`.**`fileSize`**](binaryfile.md#binaryfilefilesize)

    表示文件大小的字符串。

* [`binaryFile`.**`fileType`**](binaryfile.md#binaryfilefiletype)

    表示文件类型的字符串，例如 <code>image</code>。对应 MIME 类型的第一部分。

* [`binaryFile`.**`id`**](binaryfile.md#binaryfileid)

    文件的唯一 ID。当文件存储在磁盘或 S3 等存储服务中时，用于标识该文件。

* [`binaryFile`.**`mimeType`**](binaryfile.md#binaryfilemimetype)

    表示文件内容格式的字符串，例如 <code>image/jpeg</code>。


## Boolean（布尔值） <a href="#boolean" id="boolean"></a>

* [_`Boolean`_.**`isEmpty()`**](boolean.md#booleanisempty)

    返回 <code>true</code> 的情况是布尔值为 <code>false</code>、<code>null</code> 或 <code>undefined</code>；返回 <code>false</code> 的情况是布尔值为 <code>true</code>。

* [_`Boolean`_.**`isNotEmpty()`**](boolean.md#booleanisnotempty)

    返回 <code>true</code> 的情况是布尔值为 <code>true</code>；返回 <code>false</code> 的情况是布尔值为 <code>false</code>、<code>null</code> 或 <code>undefined</code>。结果与 <code>isEmpty()</code> 相反。

* [_`Boolean`_.**`toNumber()`**](boolean.md#booleantonumber)

    将 <code>true</code> 转换为 1，将 <code>false</code> 转换为 0。

* [_`Boolean`_.**`toString()`**](boolean.md#booleantostring)

    将 <code>true</code> 转换为字符串 ‘true’，将 <code>false</code> 转换为字符串 ‘false’。


## CustomData（自定义数据） <a href="#customdata" id="customdata"></a>

* [`$execution.customData`.**`get(key)`**](customdata.md#dollarexecutioncustomdataget)

    返回存储在指定键下的自定义执行数据。<a href="../../../understand-workflows/understand-executions/customize-executions-data.md">更多信息</a>

* [`$execution.customData`.**`getAll()`**](customdata.md#dollarexecutioncustomdatagetall)

    返回当前执行中已设置的所有自定义数据键值对。<a href="../../../understand-workflows/understand-executions/customize-executions-data.md">更多信息</a>

* [`$execution.customData`.**`set(key, value)`**](customdata.md#dollarexecutioncustomdataset)

    将自定义执行数据存储在指定的键下，便于按这些数据筛选执行记录。<a href="../../../understand-workflows/understand-executions/customize-executions-data.md">更多信息</a>

* [`$execution.customData`.**`setAll(obj)`**](customdata.md#dollarexecutioncustomdatasetall)

    为本次执行设置多组自定义数据键值对，便于按这些数据筛选执行记录。<a href="../../../understand-workflows/understand-executions/customize-executions-data.md">更多信息</a>


## Date（日期） <a href="#date" id="date"></a>

* [_`Date`_.**`toDateTime()`**](date.md#datetodatetime)

    将 JavaScript Date 转换为 Luxon DateTime。DateTime 包含相同的信息，但更易于操作。


## DateTime（日期时间） <a href="#datetime" id="datetime"></a>

* [_`DateTime`_.**`day`**](datetime.md#datetimeday)

    一个月中的第几天，取值为 1–31。

* [_`DateTime`_.**`diffTo(otherDateTime, unit)`**](datetime.md#datetimediffto)

    以指定单位返回两个 DateTime 之间的差值。

* [_`DateTime`_.**`diffToNow(unit)`**](datetime.md#datetimedifftonow)

    以指定单位返回当前时刻与该 DateTime 之间的差值。如果需要文本形式，请使用 <code>toRelative()</code>。

* [_`DateTime`_.**`endOf(unit, opts)`**](datetime.md#datetimeendof)

    将 DateTime 向上调整到指定单位的结束时刻，例如月末。

* [_`DateTime`_.**`equals(other)`**](datetime.md#datetimeequals)

    返回 <code>true</code> 表示两个 DateTime 代表完全相同的时刻，且时区相同。如需较宽松的比较，请使用 <code>hasSame()</code>。

* [_`DateTime`_.**`extract(unit?)`**](datetime.md#datetimeextract)

    以数字形式提取日期或时间的某一部分，例如月份。如需提取文本名称，请参阅 <code>format()</code>。

* [_`DateTime`_.**`format(fmt)`**](datetime.md#datetimeformat)

    使用指定格式将 DateTime 转换为字符串。参阅<a href="https://moment.github.io/luxon/#/formatting?id=table-of-tokens">格式化指南</a>。对于常见格式，使用 <code>toLocaleString()</code> 可能更方便。

* [_`DateTime`_.**`hasSame(otherDateTime, unit)`**](datetime.md#datetimehassame)

    返回 <code>true</code> 表示两个 DateTime 在指定单位及更大单位上相同。忽略时区，仅比较本地时间，因此必要时请先使用 <code>toUTC()</code>。

* [_`DateTime`_.**`hour`**](datetime.md#datetimehour)

    一天中的小时数，取值为 0–23。

* [_`DateTime`_.**`isBetween(date1, date2)`**](datetime.md#datetimeisbetween)

    返回 <code>true</code> 表示 DateTime 位于指定的两个时刻之间。

* [_`DateTime`_.**`isEmpty()`**](datetime.md#datetimeisempty)

    对所有 DateTime 返回 <code>false</code>。返回 <code>true</code> 的情况是值为 <code>null</code> 或 <code>undefined</code>。

* [_`DateTime`_.**`isInDST`**](datetime.md#datetimeisindst)

    DateTime 是否处于夏令时。

* [_`DateTime`_.**`isNotEmpty()`**](datetime.md#datetimeisnotempty)

    对所有 DateTime 返回 <code>true</code>。返回 <code>false</code> 的情况是值为 <code>null</code> 或 <code>undefined</code>。

* [_`DateTime`_.**`locale`**](datetime.md#datetimelocale)

    DateTime 的区域设置，例如 ‘en-GB’。格式化 DateTime 时会使用该区域设置。

* [_`DateTime`_.**`millisecond`**](datetime.md#datetimemillisecond)

    一秒中的毫秒数，取值为 0–999。

* [_`DateTime`_.**`minus(n, unit?)`**](datetime.md#datetimeminus)

    从 DateTime 中减去指定时长。

* [_`DateTime`_.**`minute`**](datetime.md#datetimeminute)

    一小时中的分钟数，取值为 0–59。

* [_`DateTime`_.**`month`**](datetime.md#datetimemonth)

    月份，取值为 1–12。

* [_`DateTime`_.**`monthLong`**](datetime.md#datetimemonthlong)

    完整的月份名称，例如 ‘October’。未指定区域设置时，默认使用系统区域设置。

* [_`DateTime`_.**`monthShort`**](datetime.md#datetimemonthshort)

    缩写的月份名称，例如 ‘Oct’。未指定区域设置时，默认使用系统区域设置。

* [_`DateTime`_.**`plus(n, unit?)`**](datetime.md#datetimeplus)

    为 DateTime 加上指定时长。

* [_`DateTime`_.**`quarter`**](datetime.md#datetimequarter)

    一年中的季度，取值为 1–4。

* [_`DateTime`_.**`second`**](datetime.md#datetimesecond)

    一分钟中的秒数，取值为 0–59。

* [_`DateTime`_.**`set(values)`**](datetime.md#datetimeset)

    为 DateTime 的指定单位赋予新值。如需将 DateTime 调整到单位起点或终点，另请参阅 <code>startOf()</code> 和 <code>endOf()</code>。

* [_`DateTime`_.**`setLocale(locale)`**](datetime.md#datetimesetlocale)

    设置区域，决定 DateTime 使用的语言和格式。生成 DateTime 的文本表示时很有用，例如使用 <code>format()</code> 或 <code>toLocaleString()</code> 时。

* [_`DateTime`_.**`setZone(zone, opts)`**](datetime.md#datetimesetzone)

    将 DateTime 转换为指定时区。除非通过选项另行指定，DateTime 仍表示同一时刻。另请参阅 <code>toLocal()</code> 和 <code>toUTC()</code>。

* [_`DateTime`_.**`startOf(unit, opts)`**](datetime.md#datetimestartof)

    将 DateTime 向下调整到指定单位的起始时刻，例如月初。

* [_`DateTime`_.**`toISO(opts)`**](datetime.md#datetimetoiso)

    返回符合 ISO 8601 标准的 DateTime 字符串表示。

* [_`DateTime`_.**`toLocal()`**](datetime.md#datetimetolocal)

    将 DateTime 转换为工作流的本地时区。除非通过参数另行指定，DateTime 仍表示同一时刻。可以在工作流设置中设置时区。

* [_`DateTime`_.**`toLocaleString(formatOpts)`**](datetime.md#datetimetolocalestring)

    返回 DateTime 的本地化字符串，即使用对应区域的语言和格式。未指定区域时，默认使用系统区域设置。

* [_`DateTime`_.**`toMillis()`**](datetime.md#datetimetomillis)

    返回以毫秒为单位的 Unix 时间戳，即自 1970 年 1 月 1 日起经过的毫秒数。

* [_`DateTime`_.**`toRelative(options)`**](datetime.md#datetimetorelative)

    返回相对于当前时刻的时间文本，例如 ‘in two days’（两天后）。默认向下取整。

* [_`DateTime`_.**`toSeconds()`**](datetime.md#datetimetoseconds)

    返回以秒为单位的 Unix 时间戳，即自 1970 年 1 月 1 日起经过的秒数。

* [_`DateTime`_.**`toString()`**](datetime.md#datetimetostring)

    返回 DateTime 的字符串表示，与 <code>toISO()</code> 类似。更多格式化选项请参阅 <code>format()</code> 或 <code>toLocaleString()</code>。

* [_`DateTime`_.**`toUTC(offset, opts)`**](datetime.md#datetimetoutc)

    将 DateTime 转换为 UTC 时区。除非通过参数另行指定，DateTime 仍表示同一时刻。转换到其他时区请使用 <code>setZone()</code>。

* [_`DateTime`_.**`weekday`**](datetime.md#datetimeweekday)

    星期几。1 表示星期一，7 表示星期日。

* [_`DateTime`_.**`weekdayLong`**](datetime.md#datetimeweekdaylong)

    完整的星期名称，例如 ‘Wednesday’。未指定区域设置时，默认使用系统区域设置。

* [_`DateTime`_.**`weekdayShort`**](datetime.md#datetimeweekdayshort)

    缩写的星期名称，例如 ‘Wed’。未指定区域设置时，默认使用系统区域设置。

* [_`DateTime`_.**`weekNumber`**](datetime.md#datetimeweeknumber)

    一年中的周数，大致取值为 1–52。

* [_`DateTime`_.**`year`**](datetime.md#datetimeyear)

    年份。

* [_`DateTime`_.**`zone`**](datetime.md#datetimezone)

    与 DateTime 关联的时区。


## ExecData（执行数据） <a href="#execdata" id="execdata"></a>

* [`$exec`.**`customData`**](execdata.md#dollarexeccustomdata)

    设置和获取自定义执行数据，例如用于筛选执行记录。也可以通过 Execution Data 节点完成这些操作。<a href="../../../understand-workflows/understand-executions/customize-executions-data.md">更多信息</a>

* [`$exec`.**`id`**](execdata.md#dollarexecid)

    当前工作流执行的 ID。

* [`$exec`.**`mode`**](execdata.md#dollarexecmode)

    可能为以下三个值之一：<code>test</code>（通过点击 n8n 中的按钮触发执行）、<code>production</code>（自动触发执行）。运行工作流测试时，使用 <code>evaluation</code>。

* [`$exec`.**`resumeFormUrl`**](execdata.md#dollarexecresumeformurl)

    访问 <a href="../../../../integrations/builtin/core-nodes/n8n-nodes-base.wait.md">Wait 节点</a>所生成表单的 URL。

* [`$exec`.**`resumeUrl`**](execdata.md#dollarexecresumeurl)

    用于恢复在 <a href="../../../../integrations/builtin/core-nodes/n8n-nodes-base.wait.md">Wait 节点</a>处等待的工作流的 Webhook URL。


## HTTPResponse（HTTP 响应） <a href="#httpresponse" id="httpresponse"></a>

* [`$response`.**`body`**](httpresponse.md#dollarresponsebody)

    最近一次 HTTP 调用的响应对象的正文。仅在 HTTP Request 节点中可用。

* [`$response`.**`headers`**](httpresponse.md#dollarresponseheaders)

    最近一次 HTTP 调用返回的响应头。仅在 HTTP Request 节点中可用。

* [`$response`.**`statusCode`**](httpresponse.md#dollarresponsestatuscode)

    最近一次 HTTP 调用返回的 HTTP 状态码。仅在 HTTP Request 节点中可用。

* [`$response`.**`statusMessage`**](httpresponse.md#dollarresponsestatusmessage)

    关于请求状态的可选消息。仅在 HTTP Request 节点中可用。


## Item（数据项） <a href="#item" id="item"></a>

* [`$item`.**`binary`**](item.md#dollaritembinary)

    返回数据项包含的所有二进制数据。

* [`$item`.**`json`**](item.md#dollaritemjson)

    返回数据项包含的 JSON 数据。<a href="../../understand-n8ns-data-structure.md">更多信息</a>


## NodeInputData（节点输入数据） <a href="#nodeinputdata" id="nodeinputdata"></a>

* [`$input`.**`all(branchIndex?, runIndex?)`**](nodeinputdata.md#dollarinputall)

    返回当前节点输入数据项组成的数组。

* [`$input`.**`first(branchIndex?, runIndex?)`**](nodeinputdata.md#dollarinputfirst)

    返回当前节点的第一个输入数据项。

* [`$input`.**`item`**](nodeinputdata.md#dollarinputitem)

    返回当前正在处理的输入数据项。

* [`$input`.**`last(branchIndex?, runIndex?)`**](nodeinputdata.md#dollarinputlast)

    返回当前节点的最后一个输入数据项。

* [`$input`.**`params`**](nodeinputdata.md#dollarinputparams)

    当前节点的配置，即配置节点时填写的参数，例如要执行的操作。


## NodeOutputData（节点输出数据） <a href="#nodeoutputdata" id="nodeoutputdata"></a>

* [`$()`.**`all(branchIndex?, runIndex?)`**](nodeoutputdata.md#dollarall)

    返回节点输出数据项组成的数组。

* [`$()`.**`first(branchIndex?, runIndex?)`**](nodeoutputdata.md#dollarfirst)

    返回节点输出的第一个数据项。

* [`$()`.**`isExecuted`**](nodeoutputdata.md#dollarisexecuted)

    节点已执行时为 <code>true</code>，否则为 <code>false</code>。

* [`$()`.**`item`**](nodeoutputdata.md#dollaritem)

    返回匹配的数据项，也就是用于生成当前节点中当前数据项的那个数据项。<a href="../../reference-data/link-data-items/README.md">更多信息</a>

* [`$()`.**`itemMatching(currentItemIndex?)`**](nodeoutputdata.md#dollaritemmatching)

    返回匹配的数据项，也就是用于生成当前节点中指定索引处数据项的那个数据项。<a href="../../reference-data/link-data-items/README.md">更多信息</a>

* [`$()`.**`last(branchIndex?, runIndex?)`**](nodeoutputdata.md#dollarlast)

    返回节点输出的最后一个数据项。

* [`$()`.**`params`**](nodeoutputdata.md#dollarparams)

    指定节点的配置，即在节点界面中填写的参数，例如要执行的操作。


## Number（数字） <a href="#number" id="number"></a>

* [_`Number`_.**`abs()`**](number.md#numberabs)

    返回数字的绝对值，即去掉负号。

* [_`Number`_.**`ceil()`**](number.md#numberceil)

    将数字向上取整。

* [_`Number`_.**`floor()`**](number.md#numberfloor)

    将数字向下取整。

* [_`Number`_.**`format(locale?, options?)`**](number.md#numberformat)

    返回表示该数字的格式化字符串，适合按特定语言或货币格式显示数字。与 <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat”><code>Intl.NumberFormat()</code></a> 相同。

* [_`Number`_.**`isEmpty()`**](number.md#numberisempty)

    返回 <code>true</code> 的情况是数字为 <code>0</code>、<code>NaN</code>、<code>null</code> 或 <code>undefined</code>。其他数字均返回 <code>false</code>。

* [_`Number`_.**`isEven()`**](number.md#numberiseven)

    返回 <code>true</code> 表示该数字是偶数。如果数字不是整数，则抛出错误。

* [_`Number`_.**`isInteger()`**](number.md#numberisinteger)

    返回 <code>true</code> 表示该数字是整数。

* [_`Number`_.**`isNotEmpty()`**](number.md#numberisnotempty)

    返回 <code>true</code> 的数字包括除 <code>0</code> 和 <code>NaN</code> 之外的所有数字。返回 <code>false</code> 的情况是数字为 <code>0</code>、<code>NaN</code>、<code>null</code> 或 <code>undefined</code>。结果与 <code>isEmpty()</code> 相反。

* [_`Number`_.**`isOdd()`**](number.md#numberisodd)

    返回 <code>true</code> 表示该数字是奇数。如果数字不是整数，则抛出错误。

* [_`Number`_.**`round(decimalPlaces?)`**](number.md#numberround)

    返回四舍五入到最接近的整数或指定小数位数后的数字。

* [_`Number`_.**`toBoolean()`**](number.md#numbertoboolean)

    将数字转换为布尔值。<code>0</code> 转换为 <code>false</code>，其他值均转换为 <code>true</code>。

* [_`Number`_.**`toDateTime(format?)`**](number.md#numbertodatetime)

    将数字时间戳转换为 DateTime。如果时间戳的单位不是毫秒，必须指定其格式。使用 n8n 的时区或工作流设置中的时区。

* [_`Number`_.**`toLocaleString(locales?, options?)`**](number.md#numbertolocalestring)

    返回表示该数字的本地化字符串，即使用对应区域的语言和格式。未指定区域时，默认使用系统区域设置。

* [_`Number`_.**`toString(radix?)`**](number.md#numbertostring)

    将数字转换为简单的文本表示形式。更多格式化选项请参阅 <code>toLocaleString()</code>。


## Object（对象） <a href="#object" id="object"></a>

* [_`Object`_.**`compact()`**](object.md#objectcompact)

    删除所有值为空的字段，即值为 <code>null</code> 或 <code>""</code> 的字段。

* [_`Object`_.**`hasField(name)`**](object.md#objecthasfield)

    返回 <code>true</code> 表示存在名为 <code>name</code> 的字段。仅检查顶层键，比较时区分大小写。

* [_`Object`_.**`isEmpty()`**](object.md#objectisempty)

    返回 <code>true</code> 的情况是对象没有设置任何键（字段），或对象为 <code>null</code> 或 <code>undefined</code>。

* [_`Object`_.**`isNotEmpty()`**](object.md#objectisnotempty)

    返回 <code>true</code> 表示对象至少设置了一个键（字段）。

* [_`Object`_.**`keepFieldsContaining(value)`**](object.md#objectkeepfieldscontaining)

    删除值与指定 <code>value</code> 完全不匹配的字段；至少部分匹配的字段予以保留。比较时区分大小写，值不是字符串的字段始终会被删除。

* [_`Object`_.**`keys()`**](object.md#objectkeys)

    返回包含对象所有字段名（键）的数组。与 JavaScript 的 <code>Object.keys(obj)</code> 相同。

* [_`Object`_.**`merge(otherObject)`**](object.md#objectmerge)

    将两个对象合并为一个。如果两个对象中存在相同的键（字段名），则使用第一个对象（基础对象）中的值。

* [_`Object`_.**`removeField(key)`**](object.md#objectremovefield)

    从对象中删除一个字段。与 JavaScript 的 <code>delete</code> 相同。

* [_`Object`_.**`removeFieldsContaining(value)`**](object.md#objectremovefieldscontaining)

    删除值与指定 <code>value</code> 至少部分匹配的键（字段）。比较时区分大小写，值不是字符串的字段始终会被保留。

* [_`Object`_.**`toJsonString()`**](object.md#objecttojsonstring)

    将对象转换为 JSON 字符串。与 JavaScript 的 <code>JSON.stringify()</code> 类似。

* [_`Object`_.**`urlEncode()`**](object.md#objecturlencode)

    根据对象的键和值生成 URL 参数字符串，仅支持顶层键。

* [_`Object`_.**`values()`**](object.md#objectvalues)

    返回包含对象所有字段值的数组。与 JavaScript 的 <code>Object.values(obj)</code> 相同。


## PrevNodeData（前一节点数据） <a href="#prevnodedata" id="prevnodedata"></a>

* [**`name`**](prevnodedata.md#name)

    提供当前输入的节点名称。

如果当前节点有多个输入连接点（例如 Merge 节点），始终使用第一个输入连接点。

* [**`outputIndex`**](prevnodedata.md#outputindex)

    提供当前输入的输出连接点索引。前一个节点有多个输出时（例如 If 或 Switch 节点），可以使用此值。

如果当前节点有多个输入连接点（例如 Merge 节点），始终使用第一个输入连接点。

* [**`runIndex`**](prevnodedata.md#runindex)

    前一个节点生成当前输入时的运行次数索引。

如果当前节点有多个输入连接点（例如 Merge 节点），始终使用第一个输入连接点。


## Root（全局变量与函数） <a href="#root" id="root"></a>

* [**`$(nodeName)`**](root.md#dollar)

    返回指定节点的数据。

* [**`$binary`**](root.md#dollarbinary)

    返回当前节点中当前数据项的二进制输入数据，是 <code>$input.item.binary</code> 的简写。

* [**`$execution`**](root.md#dollarexecution)

    获取或设置当前执行的元数据。

* [**`$fromAI(key, description?, type?, defaultValue?)`**](root.md#dollarfromai)

    当节点参数的值应由大语言模型提供时使用。建议提供说明，以获得更好的结果。

* [**`$if(condition, valueIfTrue, valueIfFalse)`**](root.md#dollarif)

    根据 <code>condition</code> 返回两个值中的一个，与 JavaScript 的 <code>?</code> 运算符类似。

* [**`$ifEmpty(value, valueIfEmpty)`**](root.md#dollarifempty)

    如果第一个参数不为空，则返回第一个参数，否则返回第二个参数。以下值视为空：<code>””</code>、<code>[]</code>、<code>{}</code>、<code>null</code>、<code>undefined</code>。

* [**`$input`**](root.md#dollarinput)

    当前节点的输入数据。

* [**`$itemIndex`**](root.md#dollaritemindex)

    当前正在处理的数据项在输入数据项列表中的位置。

* [**`$jmespath(obj, expression)`**](root.md#dollarjmespath)

    使用 <a href=”/code/cookbook/jmespath/”>JMESPath</a> 表达式从对象或对象数组中提取数据，适合查询复杂的嵌套对象。如果表达式无效，则返回 <code>undefined</code>。

* [**`$json`**](root.md#dollarjson)

    返回当前节点中当前数据项的 JSON 输入数据，是 <code>$input.item.json</code> 的简写。<a href="../../understand-n8ns-data-structure.md">更多信息</a>

* [**`$max(num1, num2, …, numN)`**](root.md#dollarmax)

    返回给定数字中的最大值。

* [**`$min(num1, num2, …, numN)`**](root.md#dollarmin)

    返回给定数字中的最小值。

* [**`$nodeVersion`**](root.md#dollarnodeversion)

    当前节点的版本，显示在节点设置面板底部。

* [**`$now`**](root.md#dollarnow)

    表示当前时刻的 DateTime。

使用工作流的时区，可以在工作流设置中修改。

* [**`$pageCount`**](root.md#dollarpagecount)

    节点已获取的结果页数，仅在 HTTP Request 节点中可用。

* [**`$parameter`**](root.md#dollarparameter)

    当前节点的配置，即在节点界面中填写的参数，例如要执行的操作。

* [**`$prevNode`**](root.md#dollarprevnode)

    关于提供当前输入的节点的信息。

在 Merge 节点中，始终使用第一个输入连接点。

* [**`$request`**](root.md#dollarrequest)

    节点最近一次运行时发送的请求对象，仅在 HTTP Request 节点中可用。

* [**`$response`**](root.md#dollarresponse)

    最近一次 HTTP 调用返回的响应，仅在 HTTP Request 节点中可用。

* [**`$runIndex`**](root.md#dollarrunindex)

    当前节点本次执行中当前运行的索引，从 0 开始。

* [**`$secrets`**](root.md#dollarsecrets)

    如果已配置<a href="../../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-secrets.md">外部密钥库</a>，则提供其中的密钥。密钥值不会向用户显示，仅在凭据字段中可用。

* [**`$today`**](root.md#dollartoday)

    表示当天起始午夜时刻的 DateTime。

使用实例的时区，除非工作流设置覆盖了该时区。

* [**`$vars`**](root.md#dollarvars)

    工作流可用的<a href="../../../code-in-n8n/define-custom-variables.md">变量</a>。

* [**`$workflow`**](root.md#dollarworkflow)

    关于当前工作流的信息。


## String（字符串） <a href="#string" id="string"></a>

* [_`String`_.**`base64Encode()`**](string.md#stringbase64decode)

    将 base64 编码的字符串转换为纯文本。

* [_`String`_.**`base64Encode()`**](string.md#stringbase64encode)

    将纯文本转换为 base64 编码的字符串。

* [_`String`_.**`concat(string1, string2?, ..., stringN?)`**](string.md#stringconcat)

    将一个或多个字符串连接到基础字符串末尾。也可以使用 <code>+</code> 运算符，参见示例。

* [_`String`_.**`extractDomain()`**](string.md#stringextractdomain)

    如果字符串是电子邮件地址或 URL，则返回其域名；未找到时返回 <code>undefined</code>。

如果字符串还包含其他内容，可以先尝试使用 <code>extractEmail()</code> 或 <code>extractUrl()</code>。

* [_`String`_.**`extractEmail()`**](string.md#stringextractemail)

    提取字符串中找到的第一个电子邮件地址。未找到时返回 <code>undefined</code>。

* [_`String`_.**`extractUrl()`**](string.md#stringextracturl)

    提取字符串中找到的第一个 URL。未找到时返回 <code>undefined</code>。仅识别完整的 URL，例如以 <code>http</code> 开头的 URL。

* [_`String`_.**`extractUrlPath()`**](string.md#stringextracturlpath)

    返回 URL 中域名之后的部分，未找到 URL 时返回 <code>undefined</code>。

如果字符串还包含其他内容，可以先尝试使用 <code>extractUrl()</code>。

* [_`String`_.**`hash(algo?)`**](string.md#stringhash)

    返回使用指定算法计算出的字符串哈希值。未指定时，默认使用 md5。

* [_`String`_.**`includes(searchString, start?)`**](string.md#stringincludes)

    返回 <code>true</code> 表示字符串包含 <code>searchString</code>，区分大小写。

* [_`String`_.**`indexOf(searchString, start?)`**](string.md#stringindexof)

    返回 <code>searchString</code> 在基础字符串中首次出现的索引（位置），未找到时返回 -1，区分大小写。

* [_`String`_.**`isDomain()`**](string.md#stringisdomain)

    返回 <code>true</code> 表示字符串是域名。

* [_`String`_.**`isEmail()`**](string.md#stringisemail)

    返回 <code>true</code> 表示字符串是电子邮件地址。

* [_`String`_.**`isEmpty()`**](string.md#stringisempty)

    返回 <code>true</code> 的情况是字符串没有字符，或值为 <code>null</code> 或 <code>undefined</code>。

* [_`String`_.**`isNotEmpty()`**](string.md#stringisnotempty)

    返回 <code>true</code> 表示字符串至少包含一个字符。

* [_`String`_.**`isNumeric()`**](string.md#stringisnumeric)

    返回 <code>true</code> 表示字符串表示一个数字。

* [_`String`_.**`isUrl()`**](string.md#stringisurl)

    返回 <code>true</code> 表示字符串是有效的 URL。

* [_`String`_.**`length`**](string.md#stringlength)

    字符串中的字符数量。

* [_`String`_.**`match(regexp)`**](string.md#stringmatch)

    使用<a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions”>正则表达式</a>匹配字符串。返回包含第一个匹配结果的数组；如果正则表达式设置了 <code>g</code> 标志，则返回所有匹配结果。未找到匹配项时返回 <code>null</code>。

如果只需检查文本是否存在，可以考虑改用 <code>includes()</code>。

* [_`String`_.**`parseJson()`**](string.md#stringparsejson)

    返回字符串所表示的 JavaScript 对象或值。如果字符串不是有效的 JSON，则返回 <code>undefined</code>。不支持使用单引号的 JSON。

* [_`String`_.**`quote(mark?)`**](string.md#stringquote)

    为字符串加上引号，并转义字符串中已有的引号。适用于构造 JSON、SQL 等内容。

* [_`String`_.**`removeMarkdown()`**](string.md#stringremovemarkdown)

    删除字符串中的所有 Markdown 格式，同时删除 HTML 标签。

* [_`String`_.**`removeTags()`**](string.md#stringremovetags)

    删除字符串中的标签，例如 HTML 或 XML 标签。

* [_`String`_.**`replace(pattern, replacement)`**](string.md#stringreplace)

    返回一个字符串，其中首次出现的 <code>pattern</code> 被替换为 <code>replacement</code>。

如需替换所有出现的位置，请使用 <code>replaceAll()</code>。

* [_`String`_.**`replaceAll(pattern, replacement)`**](string.md#stringreplaceall)

    返回一个字符串，其中所有出现的 <code>pattern</code> 均被替换为 <code>replacement</code>。

* [_`String`_.**`replaceSpecialChars()`**](string.md#stringreplacespecialchars)

    将字符串中的特殊字符替换为最接近的 ASCII 字符。

* [_`String`_.**`search(regexp)`**](string.md#stringsearch)

    返回模式在字符串中首次出现的索引（位置），未找到时返回 -1。模式使用<a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions”>正则表达式</a>指定。如需使用文本查找，请参阅 <code>indexOf()</code>。

* [_`String`_.**`slice(start, end?)`**](string.md#stringslice)

    从指定位置提取字符串片段。更复杂的提取方式请参阅 <code>match()</code>。

* [_`String`_.**`split(separator?, limit?)`**](string.md#stringsplit)

    将字符串拆分为子字符串数组。每次都在 <code>separator</code> 处拆分，输出不包含分隔符。

与在数组上使用 <code>join()</code> 的作用相反。

* [_`String`_.**`startsWith(searchString, start?)`**](string.md#stringstartswith)

    返回 <code>true</code> 表示字符串以 <code>searchString</code> 开头，区分大小写。

* [_`String`_.**`substring(start, end?)`**](string.md#stringsubstring)

    从指定位置提取字符串片段。更复杂的提取方式请参阅 <code>match()</code>。

* [_`String`_.**`toBoolean()`**](string.md#stringtoboolean)

    将字符串转换为布尔值。<code>0</code>、<code>false</code> 和 <code>no</code> 转换为 <code>false</code>，其他值均转换为 <code>true</code>，不区分大小写。

* [_`String`_.**`toDateTime()`**](string.md#stringtodatetime)

    将字符串转换为 DateTime，便于进一步转换。支持的字符串格式包括 ISO 8601、HTTP、RFC2822、SQL 和以毫秒为单位的 Unix 时间戳。

如需解析其他格式，请使用 <a href=”https://moment.github.io/luxon/api-docs/index.html#datetimefromformat”> <code>DateTime.fromFormat()</code></a>。

* [_`String`_.**`toJsonString()`**](string.md#stringtojsonstring)

    处理字符串，使其可插入 JSON 对象：转义引号和特殊字符，例如换行符，并为字符串加上引号。

与 JavaScript 的 <code>JSON.stringify()</code> 相同。

* [_`String`_.**`toLowerCase()`**](string.md#stringtolowercase)

    将字符串中的所有字母转换为小写。

* [_`String`_.**`toNumber()`**](string.md#stringtonumber)

    将表示数字的字符串转换为数字。如果字符串不是以有效数字开头，则抛出错误。

* [_`String`_.**`toSentenceCase()`**](string.md#stringtosentencecase)

    将字符串转换为句首大写形式，每个句子的首字母大写，其余字母小写。

* [_`String`_.**`toSnakeCase()`**](string.md#stringtosnakecase)

    将字符串转换为蛇形命名形式：空格和连字符替换为 <code>_</code>，删除符号，所有字母转换为小写。

* [_`String`_.**`toTitleCase()`**](string.md#stringtotitlecase)

    将字符串转换为标题大小写形式。每个单词的首字母大写，其余字母保持原样。较短的介词和连词不大写，例如 ‘a’、‘the’。

* [_`String`_.**`toUpperCase()`**](string.md#stringtouppercase)

    将字符串中的所有字母转换为大写。

* [_`String`_.**`trim()`**](string.md#stringtrim)

    删除字符串两端的空白字符，包括换行符、制表符、空格等。

* [_`String`_.**`urlDecode(allChars?)`**](string.md#stringurldecode)

    对 URL 编码的字符串进行解码，将 <code>%XX</code> 形式的字符编码替换为对应字符。

* [_`String`_.**`urlEncode(allChars?)`**](string.md#stringurlencode)

    对字符串进行编码，使其可用于 URL。空格和特殊字符替换为 <code>%XX</code> 形式的编码。


## WorkflowData（工作流数据） <a href="#workflowdata" id="workflowdata"></a>

* [`$workflow`.**`active`**](workflowdata.md#dollarworkflowactive)

    工作流是否处于激活状态。

* [`$workflow`.**`id`**](workflowdata.md#dollarworkflowid)

    工作流 ID，也可以从工作流 URL 中找到。

* [`$workflow`.**`name`**](workflowdata.md#dollarworkflowname)

    工作流名称，即编辑器顶部显示的名称。

## 相关资源 <a id="related-resources"></a>

* [转换数据](../)
* [数据转换方式](../approaches-for-transforming-data.md)
* [使用表达式转换数据](../expressions-for-data-transformation.md)
