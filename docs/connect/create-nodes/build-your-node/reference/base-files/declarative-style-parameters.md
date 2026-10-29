---
title: 声明式参数
description: 列出节点基础文件声明式参数的参考文档。
contentType: reference
nodeTitle: 声明式参数
originalFilePath: integrations/creating-nodes/build/reference/node-base-files/declarative-style-parameters.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/reference/node-base-files/declarative-style-parameters
url: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 声明式参数 <a href="#declarative-style-parameters" id="declarative-style-parameters"></a>

以下参数适用于声明式节点的[节点基础文件](README.md)。

本文通过简短代码片段介绍代码结构和概念。包含实际代码示例的完整节点构建教程，请参阅[构建声明式节点](../../tutorial-build-a-declarative-style-node.md)。

适用于所有节点的参数，请参阅[标准参数](standard-parameters.md)。

## `methods` 与 `loadOptions` <a href="#methods-and-loadoptions" id="methods-and-loadoptions"></a>

_对象_ | _可选_

`methods` 包含 `loadOptions` 对象。你可以使用 `loadOptions` 查询服务，获取用户专属设置，再返回这些设置并显示在图形界面中，供用户在后续查询中选用。此对象必须包含查询服务的路由信息，以及定义如何处理返回选项的输出设置。例如：

```js
methods : {
	loadOptions: {
		routing: {
			request: {
				url: '/webhook/example-option-parameters',
				method: 'GET',
			},
			output: {
				postReceive: [
					{
						// When the returned data is nested under another property
						// Specify that property key
						type: 'rootProperty',
						properties: {
							property: 'responseData',
						},
					},
					{
						type: 'setKeyValue',
						properties: {
							name: '={{$responseItem.key}} ({{$responseItem.value}})',
							value: '={{$responseItem.value}}',
						},
					},
					{
						// If incoming data is an array of objects, sort alphabetically by key
						type: 'sort',
						properties: {
							key: 'name',
						},
					},
				],
			},
		},
	}
},
```

## `routing` <a href="#routing" id="routing"></a>

_对象_ | _必填_

`routing` 是操作对象和输入字段对象的 `options` 数组中使用的对象，包含 API 调用的详细信息。

以下代码示例来自[声明式节点教程](../../tutorial-build-a-declarative-style-node.md)，演示如何集成 NASA API，以及如何使用 `requestDefaults` 设置 API 调用的基本信息，再使用 `routing` 为每项操作添加信息。

```js
description: INodeTypeDescription = {
  // Other node info here
  requestDefaults: {
			baseURL: 'https://api.nasa.gov',
			url: '',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json',
			},
		},
    properties: [
      // Resources here
      {
        displayName: 'Operation'
        // Other operation details
        options: [
          {
            name: 'Get'
            value: 'get',
            description: '',
            routing: {
              request: {
                method: 'GET',
                url: '/planetary/apod'
              }
            }
          }
        ]
      }
    ]
}
```



## `version` <a href="#version" id="version"></a>

_数字_ 或 _数组_ | _可选_

如果节点只有一个版本，可以使用数字。如果要支持多个版本，请改用数组，并在其中填写每个节点版本的编号。

n8n 支持两种节点版本控制方式，但声明式节点必须使用轻量版本控制。更多信息请参阅[节点版本控制](../versioning.md)。

## `features` <a href="#features" id="features"></a>

_对象_ | _可选_

定义具名功能标志，并根据节点版本进行判断。可以使用 `@feature` 在 `displayOptions` 中控制参数是否显示。

更多信息请参阅[基于功能的版本控制](../versioning.md#feature-based-versioning)。

## 相关资源 <a id="related-resources"></a>

* [基础文件](./)
* [结构](structure.md)
* [标准参数](standard-parameters.md)
* [编程式参数](programmatic-style-parameters.md)
* [编程式 execute 方法](programmatic-style-execute-method.md)
