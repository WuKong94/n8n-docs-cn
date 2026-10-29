---
title: 节点开发者的数据项关联说明
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

{% hint style="info" %}
**仅适用于编程式节点**

本指南适用于编程式节点。使用声明式节点时，n8n 会自动处理配对数据项。
{% endhint %}

使用 n8n 数据项关联，可以访问当前数据项之前的数据项内容。n8n 需要知道每个输出数据项来自哪个输入数据项。缺少此信息时，其他节点中的表达式可能失效。作为节点开发者，必须确保节点返回的所有数据项都支持关联。

这适用于编程式节点，包括触发器节点。开发声明式节点时，无需考虑数据项关联。节点类型详见[选择节点开发方式](../../../../../connect/create-nodes/plan-your-node/choose-a-node-building-style.md)。

首先阅读[数据项关联概念](../../../../../build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows.md)，了解其原理，以及 n8n 可以自动处理关联的场景。

需要手动处理关联时，在节点返回的每个数据项上设置 `pairedItem`：

```typescript
// Use the pairedItem information of the incoming item
newItem = {
	"json": { . . . },
	"pairedItem": {
		"item": item.pairedItem,
		// Optional: choose the input to use
		// Set this if your node combines multiple inputs
		"input": 0
};

// Or set the index manually
newItem = {
		"json": { . . . }
		"pairedItem": {
			"item": i,
			// Optional: choose the input to use
			// Set this if your node combines multiple inputs
			"input": 0
		},
};
```
