---
title: 使用 JMESPath 查询 JSON
description: n8n 支持 JMESPath 库，可简化 JSON 格式数据的处理。
contentType: howto
nodeTitle: 查询 JSON 数据
originalFilePath: data/specific-data-types/jmespath.md
originalUrl: https://docs.n8n.io/data/specific-data-types/jmespath
url: https://docs.n8n.io/build/work-with-data/handle-special-data-types/query-json-data
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 使用 JMESPath 查询 JSON <a href="#query-json-with-jmespath" id="query-json-with-jmespath"></a>

[JMESPath](https://jmespath.org/) 是一种 JSON 查询语言，可用于从 JSON 文档中提取和转换元素。完整用法请参阅 [JMESPath 文档](https://jmespath.org/tutorial.html)。


## `jmespath()` 方法 <a href="#the-jmespath-method" id="the-jmespath-method"></a>

n8n 提供了自定义方法 `jmespath()`。你可以使用此方法，以 JMESPath 查询语言搜索 JSON 对象。

基本语法如下：

```js
$jmespath(object, searchString)
```

{% hint style="info" %}
**仅支持 JavaScript**

Python Code 节点不提供 `$jmespath()`。要在 Python 中获得相同结果，请使用标准 Python 写法。下方每个示例都提供了 Python 版本。
{% endhint %}

为了帮助你理解此方法的作用，下面给出了等效但更长的 JavaScript 写法：


```js
var jmespath = require('jmespath');
jmespath.search(object, searchString);
```

{% hint style="info" %}
**表达式必须写在一行中**

上面较长的代码示例不能直接用于表达式，因为表达式必须写在一行中。
{% endhint %}

`object` 是一个 JSON 对象，例如前一个节点的输出。`searchString` 是使用 JMESPath 查询语言编写的表达式。[JMESPath 规范](https://jmespath.org/specification.html#jmespath-specification)列出了支持的表达式，[教程](https://jmespath.org/tutorial.html)和[示例](https://jmespath.org/examples.html)则提供了可交互的示例。

{% hint style="warning" %}
**搜索参数的顺序**

[JMESPath 规范](https://jmespath.org/specification.html#jmespath-specification)中的示例使用 `search(searchString, object)` 形式，而 n8n 所用的 [JMESPath JavaScript 库](https://github.com/jmespath/jmespath.js/)支持的是 `search(object, searchString)`。因此，使用 JMESPath 文档中的示例时，你可能需要调整搜索函数的参数顺序。
{% endhint %}

## 常见任务 <a href="#common-tasks" id="common-tasks"></a>

本节介绍一些常见操作的示例。更多示例和详细说明请参阅 [JMESPath 官方文档](https://jmespath.org/tutorial.html)。

尝试这些示例时，需要将 Code 节点的 **Mode（模式）**设置为 **Run Once for Each Item（为每个数据项运行一次）**。

### 通过投影将 JMESPath 表达式应用于一组元素 <a href="#apply-a-jmespath-expression-to-a-collection-of-elements-with-projections" id="apply-a-jmespath-expression-to-a-collection-of-elements-with-projections"></a>

[JMESPath 投影文档](https://jmespath.org/tutorial.html#projections)中的说明如下：

> 投影是 JMESPath 的核心功能之一，可将表达式应用于一组元素。JMESPath 支持五种投影：
> 
> * 列表投影
> * 切片投影
> * 对象投影
> * 展平投影
> * 过滤投影

以下示例展示列表、切片和对象投影的基本用法。各类投影的详细说明及更多示例，请参阅 [JMESPath 投影文档](https://jmespath.org/tutorial.html#projections)。

假设 Webhook 节点提供了以下 JSON：


```js
[
  {
    "headers": {
      "host": "n8n.instance.address",
      ...
    },
    "params": {},
    "query": {},
    "body": {
      "people": [
        {
          "first": "James",
          "last": "Green"
        },
        {
          "first": "Jacob",
          "last": "Jones"
        },
        {
          "first": "Jayden",
          "last": "Smith"
        }
      ],
      "dogs": {
        "Fido": {
          "color": "brown",
          "age": 7
        },
        "Spot": {
          "color": "black and white",
          "age": 5
        }
      }
    }
  }
]

```


获取所有人的名字组成的[列表](https://jmespath.org/tutorial.html#list-and-slice-projections)：

{% tabs %}
{% tab title="表达式（JavaScript）" %}
```js
{{$jmespath($json.body.people, "[*].first" )}}
// Returns ["James", "Jacob", "Jayden"]
```
{% endtab %}

{% tab title="Code 节点（JavaScript）" %}
```js
let firstNames = $jmespath($json.body.people, "[*].first" )
return {firstNames};
/* Returns:
[
	{
		"firstNames": [
			"James",
			"Jacob",
			"Jayden"
		]
	}
]
*/
```
{% endtab %}

{% tab title="Code 节点（Python）" %}
```python
people = _item["json"]["body"]["people"]
first_names = [person["first"] for person in people]
return {"firstNames": first_names}
"""
Returns:
[
 	{
		"firstNames": [
			"James",
			"Jacob",
			"Jayden"
		]
	}
]
"""
```
{% endtab %}
{% endtabs %}

获取名字列表的一个[切片](https://jmespath.org/tutorial.html#list-and-slice-projections)：

{% tabs %}
{% tab title="表达式（JavaScript）" %}
```js
{{$jmespath($json.body.people, "[:2].first")}}
// Returns ["James", "Jacob"]
```
{% endtab %}

{% tab title="Code 节点（JavaScript）" %}
```js
let firstTwoNames = $jmespath($json.body.people, "[:2].first");
return {firstTwoNames};
/* Returns:
[
	{
		"firstNames": [
			"James",
			"Jacob",
			"Jayden"
		]
	}
]
*/
```
{% endtab %}

{% tab title="Code 节点（Python）" %}
```python
people = _item["json"]["body"]["people"]
first_two_names = [person["first"] for person in people[:2]]
return {"firstTwoNames": first_two_names}
"""
Returns:
[
	{
		"firstTwoNames": [
		"James",
		"Jacob"
		]
	}
]
"""
```
{% endtab %}
{% endtabs %}

使用[对象投影](https://jmespath.org/tutorial.html#object-projections)获取所有狗的年龄列表：

{% tabs %}
{% tab title="表达式（JavaScript）" %}
```js
{{$jmespath($json.body.dogs, "*.age")}}
// Returns [7,5]
```
{% endtab %}

{% tab title="Code 节点（JavaScript）" %}
```js
let dogsAges = $jmespath($json.body.dogs, "*.age");
return {dogsAges};
/* Returns:
[
	{
		"dogsAges": [
			7,
			5
		]
	}
]
*/
```
{% endtab %}

{% tab title="Code 节点（Python）" %}
```python
dogs = _item["json"]["body"]["dogs"]
dogs_ages = [dog["age"] for dog in dogs.values()]
return {"dogsAges": dogs_ages}
"""
Returns:
[
	{
		"dogsAges": [
			7,
			5
		]
	}
]
"""
```
{% endtab %}
{% endtabs %}

### 选择多个元素并创建新的列表或对象 <a href="#select-multiple-elements-and-create-a-new-list-or-object" id="select-multiple-elements-and-create-a-new-list-or-object"></a>

使用[多选（Multiselect）](https://jmespath.org/tutorial.html#multiselect)，从 JSON 对象中选择元素，并将它们组合成新的列表或对象。

假设 Webhook 节点提供了以下 JSON：


```js
[
  {
    "headers": {
      "host": "n8n.instance.address",
      ...
    },
    "params": {},
    "query": {},
    "body": {
      "people": [
        {
          "first": "James",
          "last": "Green"
        },
        {
          "first": "Jacob",
          "last": "Jones"
        },
        {
          "first": "Jayden",
          "last": "Smith"
        }
      ],
      "dogs": {
        "Fido": {
          "color": "brown",
          "age": 7
        },
        "Spot": {
          "color": "black and white",
          "age": 5
        }
      }
    }
  }
]

```


使用多选列表获取名字和姓氏，并创建同时包含两者的新列表：

{% tabs %}
{% tab title="表达式（JavaScript）" %}
```js
{{$jmespath($json.body.people, "[].[first, last]")}}
// Returns [["James","Green"],["Jacob","Jones"],["Jayden","Smith"]]
```
{% endtab %}

{% tab title="Code 节点（JavaScript）" %}
```js
let newList = $jmespath($json.body.people, "[].[first, last]");
return {newList};
/* Returns:
[
	{
		"newList": [
			[
				"James",
				"Green"
			],
			[
				"Jacob",
				"Jones"
			],
			[
				"Jayden",
				"Smith"
			]
		]
	}
]
*/
```
{% endtab %}

{% tab title="Code 节点（Python）" %}
```python
people = _item["json"]["body"]["people"]
new_list = [[person["first"], person["last"]] for person in people]
return {"newList": new_list}
"""
Returns:
[
	{
		"newList": [
			[
				"James",
				"Green"
			],
			[
				"Jacob",
				"Jones"
			],
			[
				"Jayden",
				"Smith"
			]
		]
	}
]
"""
```
{% endtab %}
{% endtabs %}

### 在表达式中替代箭头函数的写法 <a href="#an-alternative-to-arrow-functions-in-expressions" id="an-alternative-to-arrow-functions-in-expressions"></a>

例如，先在 Code 节点中返回以下代码的结果，生成一些输入数据：

```js
return[
  {
    "json": {      
      "num_categories": "0",
      "num_products": "45",
      "category_id": 5529735,
      "parent_id": 1407340,
      "pos_enabled": 1,
      "pos_favorite": 0,
      "name": "HP",
      "description": "",
      "image": ""
    }
  },
  {
    "json": {
      "num_categories": "0",
      "num_products": "86",
      "category_id": 5529740,
      "parent_id": 1407340,
      "pos_enabled": 1,
      "pos_favorite": 0,
      "name": "Lenovo",
      "description": "",
      "image": ""
    }
  }  
]
```

随后可以执行这样的查询：“找出名称为 Lenovo 的数据项，并返回其类别 ID。”

```js
{{ $jmespath($("Code").all(), "[?json.name=='Lenovo'].json.category_id") }}
```

## 相关资源 <a id="related-resources"></a>

* [处理特殊数据类型](./)
* [处理文件和图片](work-with-files-and-images.md)
* [处理日期和时间](work-with-dates-and-times.md)
