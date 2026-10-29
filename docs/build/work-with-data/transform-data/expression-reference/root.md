---
nodeTitle: Root（全局变量与函数）
originalFilePath: data/expression-reference/root.md
originalUrl: https://docs.n8n.io/data/expression-reference/root
url: https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# Root（全局变量与函数） <a href="#root" id="root"></a>

## **`$()`** <a href="#dollar" id="dollar"></a>

**说明：** 返回指定节点的数据。

**语法：** $(nodeName)

**返回值：** NodeData

**来源：** n8n 自定义功能

**参数：**

  * `nodeName`（String）— 要获取数据的节点名称。

## **`$binary`** <a href="#dollarbinary" id="dollarbinary"></a>

**说明：** 返回当前节点中当前数据项的二进制输入数据，是 <code>$input.item.binary</code> 的简写。

**语法：** **`$binary`**

**返回值：** Array<BinaryFile>

**来源：** n8n 自定义功能

## **`$execution`** <a href="#dollarexecution" id="dollarexecution"></a>

**说明：** 获取或设置当前执行的元数据。

**语法：** **`$execution`**

**返回值：** ExecData

**来源：** n8n 自定义功能

## **`$fromAI()`** <a href="#dollarfromai" id="dollarfromai"></a>

**说明：** 当节点参数的值应由大语言模型提供时使用。建议提供说明，以获得更好的结果。

**语法：** $fromAI(key, description?, type?, defaultValue?)

**返回值：** any（任意类型）

**来源：** n8n 自定义功能

**参数：**

  * `key`（String）— 要获取的字段名，仅允许包含字母、数字、下划线和连字符。
  * `description`（String）— 可选 — 向模型提供更多上下文，说明它具体应返回什么内容。
  * `type`（String）— 可选 — 返回值的类型。可选值为 <code>string</code>、<code>number</code>、<code>boolean</code>、<code>json</code>、<code>date</code>、<code>datetime</code>。默认为 <code>string</code>。
  * `defaultValue`（any）— 可选 — 模型未返回该键时使用的值。

**示例：**

  ```javascript
  // Ask the model to provide a name, and use it here
  $fromAI('name')
  ```

  ```javascript
  // Ask the model to provide the age of the person (as a number with a default value of 18), and use it here
  $fromAI('age', 'The age of the person', 'number', 18)
  ```

  ```javascript
  // Ask the model to provide a boolean signifying whether the person is a student (with default value false), and use it here
  $fromAI('isStudent', 'Is the person a student', 'boolean', false)
  ```

## **`$if()`** <a href="#dollarif" id="dollarif"></a>

**说明：** 根据 <code>condition</code> 返回两个值中的一个，与 JavaScript 的 <code>?</code> 运算符类似。

**语法：** $if(condition, valueIfTrue, valueIfFalse)

**返回值：** any（任意类型）

**来源：** n8n 自定义功能

**参数：**

  * `condition`（Boolean）— 要检查的条件，求值结果应为 <code>true</code> 或 <code>false</code>。
  * `valueIfTrue`（any）— 条件为 true 时返回的值。
  * `valueIfFalse`（any）— 条件为 false 时返回的值。

**示例：**

  ```javascript
  // Return "Good day" if time is before 5pm, otherwise "Good evening"
  $if($now.hour < 17, "Good day", "Good evening")
  ```

  ```javascript
  // $if() calls can be combined:
  // Return "Good morning" if time is before 10am, "Good day" it's before 5pm, otherwise "Good evening"
  $if($now.hour < 10, "Good morning", $if($now.hour < 17, "Good day", "Good evening"))
  ```

## **`$ifEmpty()`** <a href="#dollarifempty" id="dollarifempty"></a>

**说明：** 如果第一个参数不为空，则返回第一个参数，否则返回第二个参数。以下值视为空：<code>””</code>、<code>[]</code>、<code>{}</code>、<code>null</code>、<code>undefined</code>。

**语法：** $ifEmpty(value, valueIfEmpty)

**返回值：** any（任意类型）

**来源：** n8n 自定义功能

**参数：**

  * `value`（any）— 非空时要返回的值。
  * `valueIfEmpty`（any）— <code>value</code> 为空时返回的值。

**示例：**

  ```javascript
  "Hi " + $ifEmpty(name, "there") // e.g. "Hi Nathan" or "Hi there"
  ```

## **`$input`** <a href="#dollarinput" id="dollarinput"></a>

**说明：** 当前节点的输入数据。

**语法：** **`$input`**

**返回值：** NodeData

**来源：** n8n 自定义功能

## **`$itemIndex`** <a href="#dollaritemindex" id="dollaritemindex"></a>

**说明：** 当前正在处理的数据项在输入数据项列表中的位置。

**语法：** **`$itemIndex`**

**返回值：** Number（数字）

**来源：** n8n 自定义功能

## **`$jmespath()`** <a href="#dollarjmespath" id="dollarjmespath"></a>

**说明：** 使用 <a href=”/code/cookbook/jmespath/”>JMESPath</a> 表达式从对象或对象数组中提取数据，适合查询复杂的嵌套对象。如果表达式无效，则返回 <code>undefined</code>。

**语法：** $jmespath(obj, expression)

**返回值：** any（任意类型）

**来源：** n8n 自定义功能

**参数：**

  * `obj`（Object|Array）— 要从中获取数据的对象或对象数组。
  * `expression`（String）— 定义要从对象中获取哪些数据的 <a href=”https://jmespath.org/examples.html”>JMESPath 表达式</a>。

**示例：**

  ```javascript
  data = {
    "people": [
      {
        "age": 20,
        "other": "foo",
        "name": "Bob"
      },
      {
        "age": 25,
        "other": "bar",
        "name": "Fred"
      },
      {
        "age": 30,
        "other": "baz",
        "name": "George"
      }
    ]
  }
  
  // Get all names, in an array
  {{ $jmespath(data, '[*].name') }} //=> ["Bob", "Fred", "George"]
  
  // Get the names and ages of everyone under 20
  $jmespath(data, '[?age > `20`].[name, age]') //=> [ ["Fred",25], ["George",30] ]
  
  // Get the name of the first person under 20
  $jmespath($json.people, '[?age > `20`].name | [0]') //=> Fred
  ```

  ```javascript
  data = {
      "reservations": [
        {
          "id": 1,
          "guests": [
            {
              "name": "Nathan",
              "requirements": {
                "room": "double",
                "meal": "vegetarian"
              }
            },
            {
              "name": "Meg",
              "requirements": {
                "room": "single"
              }
            }
          ]
        },
        {
          "id": 2,
          "guests": [
            {
              "name": "Lex",
              "requirements": {
                "room": "double"
              }
            }
          ]
        }
      ]
    }
  
  // Get the names of all the guests in each reservation that require a double room
  $jmespath(data, 'reservations[].guests[?requirements.room==`double`].name')
  ```

## **`$json`** <a href="#dollarjson" id="dollarjson"></a>

**说明：** 返回当前节点中当前数据项的 JSON 输入数据，是 <code>$input.item.json</code> 的简写。<a href="../../understand-n8ns-data-structure.md">更多信息</a>

**语法：** **`$json`**

**返回值：** Object（对象）

**来源：** n8n 自定义功能

## **`$max()`** <a href="#dollarmax" id="dollarmax"></a>

**说明：** 返回给定数字中的最大值。

**语法：** $max(num1, num2, …, numN)

**返回值：** Number（数字）

**来源：** n8n 自定义功能

**参数：**

  * `num1`（Number）— 要比较的第一个数字。
  * `num2`（Number）— 要比较的第二个数字。

## **`$min()`** <a href="#dollarmin" id="dollarmin"></a>

**说明：** 返回给定数字中的最小值。

**语法：** $min(num1, num2, …, numN)

**返回值：** Number（数字）

**来源：** n8n 自定义功能

**参数：**

  * `num1`（Number）— 要比较的第一个数字。
  * `num2`（Number）— 要比较的第二个数字。

## **`$nodeVersion`** <a href="#dollarnodeversion" id="dollarnodeversion"></a>

**说明：** 当前节点的版本，显示在节点设置面板底部。

**语法：** **`$nodeVersion`**

**返回值：** String（字符串）

**来源：** n8n 自定义功能

## **`$now`** <a href="#dollarnow" id="dollarnow"></a>

**说明：** 表示当前时刻的 DateTime。

使用工作流的时区，可以在工作流设置中修改。

**语法：** **`$now`**

**返回值：** DateTime

**来源：** n8n 自定义功能

## **`$pageCount`** <a href="#dollarpagecount" id="dollarpagecount"></a>

**说明：** 节点已获取的结果页数，仅在 HTTP Request 节点中可用。

**语法：** **`$pageCount`**

**返回值：** Number（数字）

**来源：** n8n 自定义功能

## **`$parameter`** <a href="#dollarparameter" id="dollarparameter"></a>

**说明：** 当前节点的配置，即在节点界面中填写的参数，例如要执行的操作。

**语法：** **`$parameter`**

**返回值：** NodeParams

**来源：** n8n 自定义功能

## **`$prevNode`** <a href="#dollarprevnode" id="dollarprevnode"></a>

**说明：** 关于提供当前输入的节点的信息。

在 Merge 节点中，始终使用第一个输入连接点。

**语法：** **`$prevNode`**

**返回值：** PrevNodeData

**来源：** n8n 自定义功能

## **`$request`** <a href="#dollarrequest" id="dollarrequest"></a>

**说明：** 节点最近一次运行时发送的请求对象，仅在 HTTP Request 节点中可用。

**语法：** **`$request`**

**返回值：** Object（对象）

**来源：** n8n 自定义功能

## **`$response`** <a href="#dollarresponse" id="dollarresponse"></a>

**说明：** 最近一次 HTTP 调用返回的响应，仅在 HTTP Request 节点中可用。

**语法：** **`$response`**

**返回值：** HTTPResponse

**来源：** n8n 自定义功能

## **`$runIndex`** <a href="#dollarrunindex" id="dollarrunindex"></a>

**说明：** 当前节点本次执行中当前运行的索引，从 0 开始。

**语法：** **`$runIndex`**

**返回值：** Number（数字）

**来源：** n8n 自定义功能

## **`$secrets`** <a href="#dollarsecrets" id="dollarsecrets"></a>

**说明：** 如果已配置<a href="../../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-secrets.md">外部密钥库</a>，则提供其中的密钥。密钥值不会向用户显示，仅在凭据字段中可用。

**语法：** **`$secrets`**

**返回值：** Object（对象）

**来源：** n8n 自定义功能

## **`$today`** <a href="#dollartoday" id="dollartoday"></a>

**说明：** 表示当天起始午夜时刻的 DateTime。

使用实例的时区，除非工作流设置覆盖了该时区。

**语法：** **`$today`**

**返回值：** DateTime

**来源：** n8n 自定义功能

## **`$vars`** <a href="#dollarvars" id="dollarvars"></a>

**说明：** 工作流可用的<a href="../../../code-in-n8n/define-custom-variables.md">变量</a>。

**语法：** **`$vars`**

**返回值：** Object（对象）

**来源：** n8n 自定义功能

## **`$workflow`** <a href="#dollarworkflow" id="dollarworkflow"></a>

**说明：** 关于当前工作流的信息。

**语法：** **`$workflow`**

**返回值：** WorkflowData

**来源：** n8n 自定义功能


## 相关资源 <a id="related-resources"></a>

* [表达式参考](./)
