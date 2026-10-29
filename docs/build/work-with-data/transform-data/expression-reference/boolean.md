---
nodeTitle: Boolean（布尔值）
originalFilePath: data/expression-reference/boolean.md
originalUrl: https://docs.n8n.io/data/expression-reference/boolean
url: https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/boolean
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# Boolean（布尔值） <a href="#boolean" id="boolean"></a>

## _`Boolean`_.**`isEmpty()`** <a href="#booleanisempty" id="booleanisempty"></a>

**说明：** 返回 <code>true</code> 的情况是布尔值为 <code>false</code>、<code>null</code> 或 <code>undefined</code>；返回 <code>false</code> 的情况是布尔值为 <code>true</code>。

{% hint style="warning" %}
`isEmpty()` 并非空值检查。对布尔值而言，它将 `false` 视为空，因此 `{{ $json.flag.isEmpty() }}` 会返回 `true`，无论字段缺失还是值为 `false`。如果只想检查值是否缺失，请直接比较，例如 `{{ $json.flag === null }}`，或者使用 **If** 节点中的 **exists（存在）**运算符。
{% endhint %}

**语法：** _`Boolean`_.isEmpty()

**返回值：** Boolean（布尔值）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // bool = true
  bool.isEmpty() // => false
  ```

  ```javascript
  // bool = false
  bool.isEmpty() // => true
  ```

  ```javascript
  // bool = null
  bool.isEmpty() // => true
  ```

## _`Boolean`_.**`isNotEmpty()`** <a href="#booleanisnotempty" id="booleanisnotempty"></a>

**说明：** 返回 <code>true</code> 的情况是布尔值为 <code>true</code>；返回 <code>false</code> 的情况是布尔值为 <code>false</code>、<code>null</code> 或 <code>undefined</code>。结果与 <code>isEmpty()</code> 相反。

**语法：** _`Boolean`_.isNotEmpty()

**返回值：** Boolean（布尔值）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // bool = true
  bool.isNotEmpty() // => true
  ```

  ```javascript
  // bool = false
  bool.isNotEmpty() // => false
  ```

  ```javascript
  // bool = null
  bool.isNotEmpty() // => false
  ```

## _`Boolean`_.**`toNumber()`** <a href="#booleantonumber" id="booleantonumber"></a>

**说明：** 将 <code>true</code> 转换为 1，将 <code>false</code> 转换为 0。

**语法：** _`Boolean`_.toNumber()

**返回值：** Number（数字）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  true.toNumber() //=> 1
  ```

  ```javascript
  false.toNumber() //=> 0
  ```

## _`Boolean`_.**`toString()`** <a href="#booleantostring" id="booleantostring"></a>

**说明：** 将 <code>true</code> 转换为字符串 ‘true’，将 <code>false</code> 转换为字符串 ‘false’。

**语法：** _`Boolean`_.toString()

**返回值：** String（字符串）

**来源：** JavaScript 函数

**示例：**

  ```javascript
  // bool = true
  bool.toString() //=> 'true'
  ```

  ```javascript
  // bool = false
  bool.toString() //=> 'false'
  ```


## 相关资源 <a id="related-resources"></a>

* [表达式参考](./)
