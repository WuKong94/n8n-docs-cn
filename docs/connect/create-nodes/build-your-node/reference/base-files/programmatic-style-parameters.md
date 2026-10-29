---
title: 编程式参数
description: 列出节点基础文件编程式参数的参考文档。
contentType: reference
nodeTitle: 编程式参数
originalFilePath: integrations/creating-nodes/build/reference/node-base-files/programmatic-style-parameters.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/reference/node-base-files/programmatic-style-parameters
url: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 编程式参数 <a href="#programmatic-style-parameters" id="programmatic-style-parameters"></a>

以下参数适用于编程式节点的[节点基础文件](README.md)。

本文通过简短代码片段介绍代码结构和概念。包含实际代码示例的完整节点构建教程，请参阅[构建编程式节点](../../tutorial-build-a-programmatic-style-node.md)。

编程式节点还使用 `execute()` 方法。更多信息请参阅[编程式 execute 方法](programmatic-style-execute-method.md)。

适用于所有节点的参数，请参阅[标准参数](standard-parameters.md)。

## `defaultVersion` <a href="#defaultversion" id="defaultversion"></a>

_数字_ | _可选_

采用完整版本控制方式时，使用 `defaultVersion`。

n8n 支持两种节点版本控制方式。更多信息请参阅[节点版本控制](../versioning.md)。

## `methods` 与 `loadOptions` <a href="#methods-and-loadoptions" id="methods-and-loadoptions"></a>

_对象_ | _可选_

包含编程式节点的 `loadOptions` 方法。你可以用此方法查询服务，获取用户专属设置（例如获取用户的 Gmail 邮件标签），再返回这些设置并显示在图形界面中，供用户在后续查询中选用。

例如，n8n 的 [Gmail 节点](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Google/Gmail/Gmail.node.ts)通过 `loadOptions` 获取所有邮件标签：

```js
	methods = {
		loadOptions: {
			// Get all the labels and display them
			async getLabels(
				this: ILoadOptionsFunctions,
			): Promise<INodePropertyOptions[]> {
				const returnData: INodePropertyOptions[] = [];
				const labels = await googleApiRequestAllItems.call(
					this,
					'labels',
					'GET',
					'/gmail/v1/users/me/labels',
				);
				for (const label of labels) {
					const labelName = label.name;
					const labelId = label.id;
					returnData.push({
						name: labelName,
						value: labelId,
					});
				}
				return returnData;
			},
		},
	};
```

## `version` <a href="#version" id="version"></a>

_数字_ 或 _数组_ | _可选_

采用轻量版本控制方式时，使用 `version`。

如果节点只有一个版本，可以使用数字。如果要支持多个版本，请改用数组，并在其中填写每个节点版本的编号。

n8n 支持两种节点版本控制方式，编程式节点可以任选一种。更多信息请参阅[节点版本控制](../versioning.md)。

## `features` <a href="#features" id="features"></a>

_对象_ | _可选_

定义具名功能标志，并根据节点版本进行判断。可以使用 `@feature` 在 `displayOptions` 中控制参数是否显示，也可以在代码中通过 `this.isNodeFeatureEnabled()` 检查这些标志。

更多信息请参阅[基于功能的版本控制](../versioning.md#feature-based-versioning)。

## 相关资源 <a id="related-resources"></a>

* [基础文件](./)
* [结构](structure.md)
* [标准参数](standard-parameters.md)
* [声明式参数](declarative-style-parameters.md)
* [编程式 execute 方法](programmatic-style-execute-method.md)
