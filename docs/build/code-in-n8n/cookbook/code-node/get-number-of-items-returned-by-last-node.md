---
contentType: howto
nodeTitle: 获取前一节点返回的数据项数量
originalFilePath: code/cookbook/code-node/number-items-last-node.md
originalUrl: https://docs.n8n.io/code/cookbook/code-node/number-items-last-node
url: https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-number-of-items-returned-by-last-node
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 获取前一节点返回的数据项数量 <a href="#get-number-of-items-returned-by-the-previous-node" id="get-number-of-items-returned-by-the-previous-node"></a>

获取前一节点返回的数据项数量：

{% tabs %}
{% tab title="JavaScript" %}
```js
if (Object.keys(items[0].json).length === 0) {
return [
	{
		json: {
			results: 0,
		}
	}
]
}
return [
	{
		json: {
			results: items.length,
		}
	}
];
```

输出类似如下内容。

```json
[
	{
		"results": 8
	}
]
```
{% endtab %}

{% tab title="Python" %}
```python
if len(items[0].json) == 0:
	return [
		{
			"json": {
				"results": 0,
			}
		}
	]
else:
	return [
		{
			"json": {
				"results": len(items),
			}
		}
	]
```
输出类似如下内容。

```json
[
	{
		"results": 8
	}
]
```
{% endtab %}
{% endtabs %}

## 相关资源 <a id="related-resources"></a>

* [Code 节点实用示例](./)
* [获取二进制数据缓冲区](get-the-binary-data-buffer.md)
* [输出到浏览器控制台](output-to-the-browser-console.md)
