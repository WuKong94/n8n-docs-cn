---
nodeTitle: Object（对象）
originalFilePath: data/expression-reference/object.md
originalUrl: https://docs.n8n.io/data/expression-reference/object
url: https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# Object（对象） <a href="#object" id="object"></a>

## _`Object`_.**`compact()`** <a href="#objectcompact" id="objectcompact"></a>

**说明：** 删除所有值为空的字段，即值为 <code>null</code> 或 <code>""</code> 的字段。

**语法：** _`Object`_.compact()

**返回值：** Object（对象）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // obj = {'x':null, 'y':2, 'z':''}
  obj.compact() //=> {'y':2}
  ```

## _`Object`_.**`hasField()`** <a href="#objecthasfield" id="objecthasfield"></a>

**说明：** 返回 <code>true</code> 表示存在名为 <code>name</code> 的字段。仅检查顶层键，比较时区分大小写。

**语法：** _`Object`_.hasField(name)

**返回值：** Boolean（布尔值）

**来源：** n8n 自定义功能

**参数：**

  * `name`（String）— 要查找的键名。

**示例：**

  ```javascript
  // obj = {'name':'Nathan', 'age':42}
  obj.hasField('name') //=> true
  ```

  ```javascript
  // obj = {'name':'Nathan', 'age':42}
  obj.hasField('Name') //=> false
  obj.hasField('inventedField') //=> false
  ```

## _`Object`_.**`isEmpty()`** <a href="#objectisempty" id="objectisempty"></a>

**说明：** 返回 <code>true</code> 的情况是对象没有设置任何键（字段），或对象为 <code>null</code> 或 <code>undefined</code>。

**语法：** _`Object`_.isEmpty()

**返回值：** Boolean（布尔值）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // obj = {'name': 'Nathan'}
  obj.isEmpty() //=> false
  ```

  ```javascript
  // obj = {}
  obj.isEmpty() //=> true
  ```

## _`Object`_.**`isNotEmpty()`** <a href="#objectisnotempty" id="objectisnotempty"></a>

**说明：** 返回 <code>true</code> 表示对象至少设置了一个键（字段）。

**语法：** _`Object`_.isNotEmpty()

**返回值：** Boolean（布尔值）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // obj = {'name': 'Nathan'}
  obj.isNotEmpty() //=> true
  ```

  ```javascript
  // obj = {}
  obj.isNotEmpty() //=> false
  ```

## _`Object`_.**`keepFieldsContaining()`** <a href="#objectkeepfieldscontaining" id="objectkeepfieldscontaining"></a>

**说明：** 删除值与指定 <code>value</code> 完全不匹配的字段；至少部分匹配的字段予以保留。比较时区分大小写，值不是字符串的字段始终会被删除。

**语法：** _`Object`_.keepFieldsContaining(value)

**返回值：** Object（对象）

**来源：** n8n 自定义功能

**参数：**

  * `value`（String）— 字段值必须包含此文本才会被保留。

**示例：**

  ```javascript
  // obj = {'name': 'Mr Nathan', 'city':'hanoi', age: 42 }
  obj.keepFieldsContaining('Nathan') //=> {'name': 'Mr Nathan'}
  ```

  ```javascript
  // obj = {'name': 'Mr Nathan', 'city':'hanoi', age: 42 }
  obj.keepFieldsContaining('nathan') //=> {}
  obj.keepFieldsContaining('han') //=> {'name': 'Mr Nathan', 'city':'hanoi'}
  ```

## _`Object`_.**`keys()`** <a href="#objectkeys" id="objectkeys"></a>

**说明：** 返回包含对象所有字段名（键）的数组。与 JavaScript 的 <code>Object.keys(obj)</code> 相同。

**语法：** _`Object`_.keys()

**返回值：** Array<String>

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // obj = {'name': 'Mr Nathan', age: 42 }
  obj.keys() //=> ['name', 'age']
  ```

## _`Object`_.**`merge()`** <a href="#objectmerge" id="objectmerge"></a>

**说明：** 将两个对象合并为一个。如果两个对象中存在相同的键（字段名），则使用第一个对象（基础对象）中的值。

**语法：** _`Object`_.merge(otherObject)

**返回值：** Object（对象）

**来源：** n8n 自定义功能

**参数：**

  * `otherObject`（Object）— 要与基础对象合并的对象。

**示例：**

  ```javascript
  // obj1 = {'name':'Nathan', 'age': 42}
  // obj2 = {'name':'Jan', 'city': 'hanoi'}
  obj1.merge(obj2) //=> {'name':'Jan', 'city': 'hanoi', 'age':42}
  ```

## _`Object`_.**`removeField()`** <a href="#objectremovefield" id="objectremovefield"></a>

**说明：** 从对象中删除一个字段。与 JavaScript 的 <code>delete</code> 相同。

**语法：** _`Object`_.removeField(key)

**返回值：** Object（对象）

**来源：** n8n 自定义功能

**参数：**

  * `key`（String）— 要删除的字段名。

**示例：**

  ```javascript
  // obj = {'name':'Nathan', 'city':'hanoi'}
  obj.removeField('name') //=> {'city':'hanoi'}
  ```

## _`Object`_.**`removeFieldsContaining()`** <a href="#objectremovefieldscontaining" id="objectremovefieldscontaining"></a>

**说明：** 删除值与指定 <code>value</code> 至少部分匹配的键（字段）。比较时区分大小写，值不是字符串的字段始终会被保留。

**语法：** _`Object`_.removeFieldsContaining(value)

**返回值：** Object（对象）

**来源：** n8n 自定义功能

**参数：**

  * `value`（String）— 字段值包含此文本时，该字段会被删除。

**示例：**

  ```javascript
  // obj = {'name': 'Mr Nathan', 'city':'hanoi', age: 42}
  obj.removeFieldsContaining('Nathan') //=> {'city':'hanoi', age: 42}
  ```

  ```javascript
  // obj = {'name': 'Mr Nathan', 'city':'hanoi', age: 42}
  obj.removeFieldsContaining('han') //=> {age: 42}
  obj.removeFieldsContaining('nathan') //=> {'name': 'Mr Nathan', 'city':'hanoi', age: 42}
  ```

## _`Object`_.**`toJsonString()`** <a href="#objecttojsonstring" id="objecttojsonstring"></a>

**说明：** 将对象转换为 JSON 字符串。与 JavaScript 的 <code>JSON.stringify()</code> 类似。

**语法：** _`Object`_.toJsonString()

**返回值：** String（字符串）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // obj = {'name':'Nathan', age:42}
  obj.toJsonString() //=> '{"name":"Nathan","age":42}'
  
  ```

## _`Object`_.**`urlEncode()`** <a href="#objecturlencode" id="objecturlencode"></a>

**说明：** 根据对象的键和值生成 URL 参数字符串，仅支持顶层键。

**语法：** _`Object`_.urlEncode()

**返回值：** String（字符串）

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // obj = {'name':'Mr Nathan', 'city':'hanoi'}
  obj.urlEncode() //=> 'name=Mr+Nathan&city=hanoi'
  ```

## _`Object`_.**`values()`** <a href="#objectvalues" id="objectvalues"></a>

**说明：** 返回包含对象所有字段值的数组。与 JavaScript 的 <code>Object.values(obj)</code> 相同。

**语法：** _`Object`_.values()

**返回值：** Array<String>

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // obj = {'name': 'Mr Nathan', age: 42 }
  obj.values() //=> ['Mr Nathan', 42]
  ```


## 相关资源 <a id="related-resources"></a>

* [表达式参考](./)
