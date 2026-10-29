---
title: Code 节点中的数据项关联
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

引用前面节点时，需要确定使用哪个数据项，这由数据项关联解决。多数节点会自动将每个输出数据项关联到输入数据项，形成可向前回溯的关联链。概念详解见[数据项关联概念](../../../../../build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows.md)，本文侧重实际用法示例。

使用 Code 节点时，某些场景需要手动提供关联信息，才能在后续工作流中使用 `$("<node-name>").item`。这些情况仅适用于多个输入数据项，单个数据项的关联由 n8n 自动处理。

需要手动处理的场景包括：

* 添加新数据项：新数据项尚未关联到任何输入。
* 返回新建的数据项。
* 希望手动控制数据项关联。

其他场景由 [n8n 的自动数据项关联](../../../../../build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows.md)处理。

要控制关联，在返回数据时设置 `pairedItem`。例如，关联到索引为 0 的数据项：

```js
[
	{
		"json": {
			. . . 
		},
		// The index of the input item that generated this output item
		"pairedItem": 0
	}
]
```


### `pairedItem` 使用示例 <a href="#paireditem-usage-example" id="paireditem-usage-example"></a>

对于以下输入数据：

```json
[
  {
    "id": "23423532",
    "name": "Jay Gatsby"
  },
  {
    "id": "23423533",
    "name": "José Arcadio Buendía"
  },
  {
    "id": "23423534",
    "name": "Max Sendak"
  },
  {
    "id": "23423535",
    "name": "Zaphod Beeblebrox"
  },
  {
    "id": "23423536",
    "name": "Edmund Pevensie"
  }
]
```

使用它生成新的数据项，只包含名称，并加入一条新数据：

```js
newItems = [];
for(let i=0; i<items.length; i++){
  newItems.push(
    {
    "json":
      {
        "name": items[i].json.name,
				"aBrandNewField": "New data for item " + i
      }
    }
  )
}

return newItems;
```

`newItems` 是没有 `pairedItem` 的数据项数组，因此无法从这些数据项回溯到生成它们的数据项。

添加 `pairedItem` 对象：

```js
newItems = [];
for(let i=0; i<items.length; i++){
  newItems.push(
    {
      "json":
        {
          "name": items[i].json.name,
					"aBrandNewField": "New data for item " + i
        },
      "pairedItem": i
    }    
  )
}
return newItems;
```

现在，每个新数据项都关联到用于创建它的数据项。
