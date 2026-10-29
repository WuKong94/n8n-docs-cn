---
nodeTitle: Number（数字）
originalFilePath: data/expression-reference/number.md
originalUrl: https://docs.n8n.io/data/expression-reference/number
url: https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# Number（数字） <a href="#number" id="number"></a>

## _`Number`_.**`abs()`** <a href="#numberabs" id="numberabs"></a>

**说明：** 返回数字的绝对值，即去掉负号。

**语法：** _`Number`_.abs()

**返回值：** Number（数字）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // x = -1.7
  x.abs() //=> 1.7
  ```

## _`Number`_.**`ceil()`** <a href="#numberceil" id="numberceil"></a>

**说明：** 将数字向上取整。

**语法：** _`Number`_.ceil()

**返回值：** Number（数字）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // x = 1.234
  x.ceil() //=> 2
  ```

## _`Number`_.**`floor()`** <a href="#numberfloor" id="numberfloor"></a>

**说明：** 将数字向下取整。

**语法：** _`Number`_.floor()

**返回值：** Number（数字）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // x = 1.234
  x.floor() //=> 1
  ```

## _`Number`_.**`format()`** <a href="#numberformat" id="numberformat"></a>

**说明：** 返回表示该数字的格式化字符串，适合按特定语言或货币格式显示数字。与 <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat”><code>Intl.NumberFormat()</code></a> 相同。

**语法：** _`Number`_.format(locale?, options?)

**返回值：** String（字符串）

**来源：** n8n 自定义功能

**参数：**

  * `locale`（String）— 可选 — 用于格式化数字的<a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locales_argument”>区域设置标签</a>，例如 <code>fr-FR</code>、<code>en-GB</code>、<code>pr-BR</code>。
  * `options`（Object）— 可选 — 数字格式化的配置选项。<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat" target="_blank">更多信息</a>

**示例：**

  ```javascript
  // number = 123456.789;
  number.format('de-DE') //=> 123.456,789
  ```

  ```javascript
  // number = 123456.789;
  number.format('de-DE', {'style': 'currency', 'currency': 'EUR'}) //=> 123.456,79 €
  ```

## _`Number`_.**`isEmpty()`** <a href="#numberisempty" id="numberisempty"></a>

**说明：** 返回 <code>true</code> 的情况是数字为 <code>0</code>、<code>NaN</code>、<code>null</code> 或 <code>undefined</code>。其他数字均返回 <code>false</code>。

{% hint style="warning" %}
`isEmpty()` 并非空值检查。对数字而言，它将 `0` 视为空，因此 `{{ $json.count.isEmpty() }}` 会返回 `true`，无论字段缺失还是值为 `0`。如果只想检查值是否缺失，请直接比较，例如 `{{ $json.count === null }}`，或者使用 **If** 节点中的 **exists（存在）**运算符。
{% endhint %}

**语法：** _`Number`_.isEmpty()

**返回值：** Boolean（布尔值）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // num = 10
  num.isEmpty() // => false
  ```

  ```javascript
  // num = 0
  num.isEmpty() // => true
  ```

  ```javascript
  // num = null
  num.isEmpty() // => true
  ```

## _`Number`_.**`isEven()`** <a href="#numberiseven" id="numberiseven"></a>

**说明：** 返回 <code>true</code> 表示该数字是偶数。如果数字不是整数，则抛出错误。

**语法：** _`Number`_.isEven()

**返回值：** Boolean（布尔值）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // number = 33
  number.isEven() //=> false
  ```

## _`Number`_.**`isInteger()`** <a href="#numberisinteger" id="numberisinteger"></a>

**说明：** 返回 <code>true</code> 表示该数字是整数。

**语法：** _`Number`_.isInteger()

**返回值：** Boolean（布尔值）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // number = 4
  number.isInteger() //=> true
  ```

  ```javascript
  // number = 4.12
  number.isInteger() //=> false
  ```

## _`Number`_.**`isNotEmpty()`** <a href="#numberisnotempty" id="numberisnotempty"></a>

**说明：** 返回 <code>true</code> 的数字包括除 <code>0</code> 和 <code>NaN</code> 之外的所有数字。返回 <code>false</code> 的情况是数字为 <code>0</code>、<code>NaN</code>、<code>null</code> 或 <code>undefined</code>。结果与 <code>isEmpty()</code> 相反。

**语法：** _`Number`_.isNotEmpty()

**返回值：** Boolean（布尔值）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // num = 10
  num.isNotEmpty() // => true
  ```

  ```javascript
  // num = 0
  num.isNotEmpty() // => false
  ```

  ```javascript
  // num = null
  num.isNotEmpty() // => false
  ```

## _`Number`_.**`isOdd()`** <a href="#numberisodd" id="numberisodd"></a>

**说明：** 返回 <code>true</code> 表示该数字是奇数。如果数字不是整数，则抛出错误。

**语法：** _`Number`_.isOdd()

**返回值：** Boolean（布尔值）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // number = 33
  number.isOdd() //=> true
  ```

## _`Number`_.**`round()`** <a href="#numberround" id="numberround"></a>

**说明：** 返回四舍五入到最接近的整数或指定小数位数后的数字。

**语法：** _`Number`_.round(decimalPlaces?)

**返回值：** Number（数字）

**来源：** n8n 自定义功能

**参数：**

  * `decimalPlaces`（Number）— 可选 — 要保留的小数位数。

**示例：**

  ```javascript
  // number = 1.256
  number.round() //=> 1
  ```

  ```javascript
  // number = 1.256
  number.round(1) //=> 1.3
  number.round(2) //=> 1.26
  ```

## _`Number`_.**`toBoolean()`** <a href="#numbertoboolean" id="numbertoboolean"></a>

**说明：** 将数字转换为布尔值。<code>0</code> 转换为 <code>false</code>，其他值均转换为 <code>true</code>。

**语法：** _`Number`_.toBoolean()

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // number = 12
  number.toBoolean() //=> true
  ```

  ```javascript
  // number = 0
  number.toBoolean() //=> false
  ```

## _`Number`_.**`toDateTime()`** <a href="#numbertodatetime" id="numbertodatetime"></a>

**说明：** 将数字时间戳转换为 DateTime。如果时间戳的单位不是毫秒，必须指定其格式。使用 n8n 的时区或工作流设置中的时区。

**语法：** _`Number`_.toDateTime(format?)

**返回值：** DateTime

**来源：** n8n 自定义功能

**参数：**

  * `format`（String）— 可选 — 要转换的时间戳类型。可选值为 <code>ms</code>（以毫秒为单位的 Unix 时间戳）、<code>s</code>（以秒为单位的 Unix 时间戳）或 <code>excel</code>（自 1900 年起的天数）。

**示例：**

  ```javascript
  // ts = 1708695471
  ts.toDateTime('s') //=> 2024-02-23T14:37:51+01:00
  ```

  ```javascript
  // ts = 1708695471000
  ts.toDateTime('ms') //=> 2024-02-23T14:37:51+01:00
  ```

  ```javascript
  // ts = 45345
  ts.toDateTime('excel') //=> 2024-02-23T01:00:00+01:00
  ```

## _`Number`_.**`toLocaleString()`** <a href="#numbertolocalestring" id="numbertolocalestring"></a>

**说明：** 返回表示该数字的本地化字符串，即使用对应区域的语言和格式。未指定区域时，默认使用系统区域设置。

**语法：** _`Number`_.toLocaleString(locales?, options?)

**返回值：** String（字符串）

**来源：** JavaScript 函数

**参数：**

  * `locales`（String|Array<String>）— 可选 — 要使用的区域设置，例如 ‘en-GB’ 表示英式英语，‘pt-BR’ 表示巴西葡萄牙语。参阅<a href=”https://www.localeplanet.com/icu/”>完整列表</a>（非官方）。也接受区域设置数组。未指定时，默认使用系统区域设置。
  * `options`（Object）— 可选 — 包含<a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat#parameters”>格式化选项</a>的对象。

**示例：**

  ```javascript
  // num = 500000.125
  num.toLocaleString() //=> '500,000.125' (if in US English locale)
  ```

  ```javascript
  // num = 500000.125
  num.toLocaleString('fr-FR') //=> '500 000,125'
  ```

  ```javascript
  // num = 500000.125
  num.toLocaleString('fr-FR', {style:'currency', currency:'EUR'}) //=> '500 000,13 €'
  ```

## _`Number`_.**`toString()`** <a href="#numbertostring" id="numbertostring"></a>

**说明：** 将数字转换为简单的文本表示形式。更多格式化选项请参阅 <code>toLocaleString()</code>。

**语法：** _`Number`_.toString(radix?)

**返回值：** String（字符串）

**来源：** JavaScript 函数

**参数：**

  * `radix`（Number）— 可选 — 使用的进制，必须是 2 到 36 之间的整数。例如，基数 <code>2</code> 表示二进制，基数 <code>16</code> 表示十六进制。

**示例：**

  ```javascript
  // num = 500000.125
  num.toString() //=> '500000.125'
  ```

  ```javascript
  // num = 500000.125
  num.toString(16) //=> '7a120.2'
  ```


## 相关资源 <a id="related-resources"></a>

* [表达式参考](./)
