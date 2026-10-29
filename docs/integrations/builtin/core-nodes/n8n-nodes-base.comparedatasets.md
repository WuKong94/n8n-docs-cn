---
title: Compare Datasets（比较数据集）
description: 工作流自动化平台 n8n 中的 Compare Datasets（比较数据集） 节点文档，包括使用说明和示例链接。
contentType:
- integration
- reference
priority: high
nodeTitle: Compare Datasets（比较数据集）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Compare Datasets（比较数据集） <a href="#compare-datasets" id="compare-datasets"></a>

Compare Datasets 节点用于比较两个输入流的数据。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

1. 确定要比较的字段。在 **Input A Field**（输入 A 字段）中输入要使用的输入流 A 的字段名称，在 **Input B Field**（输入 B 字段）中输入要使用的输入流 B 的字段名称。
2. **可选：**可以按多个字段比较。选择 **Add Fields to Match**（添加匹配字段）设置更多比较。
3. 选择如何处理数据集之间的差异。在 **When There Are Differences**（存在差异时）中选择以下选项之一：
    * **Use Input A Version**（使用输入 A 版本）：以输入流 A 为准。
    * **Use Input B Version**（使用输入 B 版本）：以输入流 B 为准。
    * **Use a Mix of Versions**（混合使用版本）：不同字段使用不同输入。
        * 使用 **Prefer**（优先使用）选择 **Input A Version**（输入 A 版本）或 **Input B Version**（输入 B 版本），作为主要依据。
        * 在 **For Everything Except**（除以下字段外）中输入例外字段，使这些字段取自另一个输入源。多个输入字段以逗号分隔。
    * **Include Both Versions**（包含两个版本）：在输出中包含两个输入流，可能使结构更复杂。
4. 决定是否启用 **Fuzzy Compare**（模糊比较）。开启后，字段比较会容许细微的类型差异。例如，数字 3 和字符串 `3` 在开启时会被视为相同，关闭时则不同。

## 理解数据项比较 <a href="#understand-item-comparison" id="understand-item-comparison"></a>

数据项比较分为两个阶段：

1. n8n 检查两个输入中所选匹配字段的值是否一致。
2. 如果匹配字段一致，n8n 会进一步比较数据项中的全部字段，判断数据项相同还是不同。

## 节点选项 <a href="#node-options" id="node-options"></a>

使用节点的 **Options**（选项）细化比较条件或调整比较行为。

### Fields to Skip Comparing（跳过比较的字段） <a href="#fields-to-skip-comparing" id="fields-to-skip-comparing"></a>

输入比较时要忽略的字段名称。

例如，比较下方两个数据集时，如果将 `person.language` 作为 **Fields to Match**（匹配字段），n8n 会判断它们不同。如果将 `person.name` 添加到 **Fields to Skip Comparing**（跳过比较的字段），则会判断它们匹配。

```json
	// Input 1
	[
		{
			"person":
			{
				"name":	"Stefan",
				"language":	"de"
			}
		},
		{
			"person":
			{
				"name":	"Jim",
				"language":	"en"
			}
		},
		{
			"person":
			{
				"name":	"Hans",
				"language":	"de"
			}
		}
	]
	// Input 2
		[
		{
			"person":
			{
				"name":	"Sara",
				"language":	"de"
			}
		},
		{
			"person":
			{
				"name":	"Jane",
				"language":	"en"
			}
		},
		{
			"person":
			{
				"name":	"Harriet",
				"language":	"de"
			}
		}
	]
```

### Disable Dot Notation（禁用点表示法） <a href="#disable-dot-notation" id="disable-dot-notation"></a>

开启时，不允许在字段名称中使用 `parent.child` 引用子字段；关闭时允许，默认为关闭。

### Multiple Matches（多个匹配） <a href="#multiple-matches" id="multiple-matches"></a>

选择如何处理重复数据。默认为 **Include All Matches**（包含全部匹配），也可选择 **Include First Match Only**（仅包含第一个匹配）。

例如，给定以下两个数据集：
```json
	// Input 1
	[
		{
			"fruit": {
				"type": "apple",
				"color": "red"
			}
		},
				{
			"fruit": {
				"type": "apple",
				"color": "red"
			}
		},
				{
			"fruit": {
				"type": "banana",
				"color": "yellow"
			}
		}
	]
	// Input 2
	[
		{
			"fruit": {
				"type": "apple",
				"color": "red"
			}
		},
				{
			"fruit": {
				"type": "apple",
				"color": "red"
			}
		},
				{
			"fruit": {
				"type": "banana",
				"color": "yellow"
			}
		}
	]
```

n8n 在 **Same Branch**（相同分支）标签页返回三个数据项，两个分支中的数据相同。

如果选择 **Include First Match Only**（仅包含第一个匹配），n8n 在 **Same Branch**（相同分支）标签页返回两个数据项。两个分支的数据相同，但 n8n 只返回匹配的“apple”数据项的首次出现。


## 理解输出 <a href="#understand-the-output" id="understand-the-output"></a>

共有四种输出：

* **In A only Branch**（仅 A 分支）：包含仅出现在第一个输入中的数据。
* **Same Branch**（相同分支）：包含两个输入中相同的数据。
* **Different Branch**（不同分支）：包含两个输入间存在差异的数据。
* **In B only Branch**（仅 B 分支）：包含仅出现在第二个输入中的数据。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Compare Datasets（比较数据集） 集成模板](https://n8n.io/integrations/compare-datasets)，或[搜索所有模板](https://n8n.io/workflows/)

