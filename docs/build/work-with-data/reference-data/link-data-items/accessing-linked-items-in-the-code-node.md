---
description: 如何使用 `("<node-name>").itemMatching(currentNodeinputIndex)`。
contentType: howto
nodeTitle: 在 Code 节点中访问关联的数据项
originalFilePath: data/data-mapping/itemmatching.md
originalUrl: https://docs.n8n.io/data/data-mapping/itemmatching
url: https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/accessing-linked-items-in-the-code-node
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 在 Code 节点中访问关联的数据项 <a href="#accessing-linked-items-in-the-code-node" id="accessing-linked-items-in-the-code-node"></a>

节点输入中的每个数据项，都关联到前面节点用于生成它的数据项。需要从比紧邻前一节点更早的位置读取关联数据时，这很有用。

要访问工作流更早位置的关联数据项，使用 `("<node-name>").itemMatching(currentNodeinputIndex)`。


例如，考虑以下工作流：

1. Customer Datastore 节点生成示例数据：
	```json
	[
		{
			"id": "23423532",
			"name": "Jay Gatsby",
			"email": "gatsby@west-egg.com",
			"notes": "Keeps asking about a green light??",
			"country": "US",
			"created": "1925-04-10"
		},
		{
			"id": "23423533",
			"name": "José Arcadio Buendía",
			"email": "jab@macondo.co",
			"notes": "Lots of people named after him. Very confusing",
			"country": "CO",
			"created": "1967-05-05"
		},
		...
    ]
	```
2. Edit Fields 节点简化数据：
	```json
	[
		{
			"name": "Jay Gatsby"
		},
		{
			"name": "José Arcadio Buendía"
		},
        ...
	]
	```
3. Code 节点为正确的人员恢复邮箱地址：
	```json
	[
		{
			"name": "Jay Gatsby",
			"restoreEmail": "gatsby@west-egg.com"
		},
		{
			"name": "José Arcadio Buendía",
			"restoreEmail": "jab@macondo.co"
		},
		...
	]
	```

Code 节点使用以下代码完成：

{% tabs %}
{% tab title="JavaScript" %}
```js
for(let i=0; i<$input.all().length; i++) {
	$input.all()[i].json.restoreEmail = $('Customer Datastore (n8n training)').itemMatching(i).json.email;
}
return $input.all();
```
{% endtab %}

{% tab title="Python" %}
```python
for i,item in enumerate(_input.all()):
	_input.all()[i].json.restoreEmail = _('Customer Datastore (n8n training)').itemMatching(i).json.email

return _input.all();
```
{% endtab %}
{% endtabs %}

可以在 [n8n 网站：itemMatching 使用示例](https://n8n.io/workflows/1966-itemmatching-usage-example/)中查看和下载此工作流。

## 相关资源 <a id="related-resources"></a>

* [关联数据项](./)
* [数据项如何在工作流中关联](how-items-link-through-workflows.md)
* [在 Code 节点中保留关联](preserving-linking-in-the-code-node.md)
* [数据项关联错误](item-linking-errors.md)
* [节点开发者的数据项关联说明](item-linking-for-node-creators.md)
