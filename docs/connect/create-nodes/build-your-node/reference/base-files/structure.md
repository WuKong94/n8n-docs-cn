---
title: 节点基础文件的结构
description: 介绍节点基础文件基本结构的参考文档。
contentType: reference
nodeTitle: 结构
originalFilePath: integrations/creating-nodes/build/reference/node-base-files/structure.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/reference/node-base-files/structure
url: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/structure
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 节点基础文件的结构 <a href="#structure-of-the-node-base-file" id="structure-of-the-node-base-file"></a>

节点基础文件遵循以下基本结构：

1. 添加导入语句。
2. 为节点创建类。
3. 在节点类中创建用于定义节点的 `description` 对象。

编程式节点还具有 `execute()` 方法，用于读取传入的数据和参数，然后构建请求。声明式节点则通过 `routing` 键处理请求，该键位于 `properties` 对象中，而此对象位于 `descriptions` 内。

## 声明式节点的结构概览 <a href="#outline-structure-for-a-declarative-style-node" id="outline-structure-for-a-declarative-style-node"></a>

以下代码片段展示了节点的大体结构。

```js
import { INodeType, INodeTypeDescription } from 'n8n-workflow';

export class ExampleNode implements INodeType {
	description: INodeTypeDescription = {
		// Basic node details here
		properties: [
			// Resources and operations here
		]
	};
}
```
适用于所有节点类型的参数，请参阅[标准参数](standard-parameters.md)。适用于声明式节点的参数，请参阅[声明式参数](declarative-style-parameters.md)。

## 编程式节点的结构概览 <a href="#outline-structure-for-a-programmatic-style-node" id="outline-structure-for-a-programmatic-style-node"></a>

以下代码片段展示了节点的大体结构。

```js
import { IExecuteFunctions, INodeExecutionData, INodeType, INodeTypeDescription } from 'n8n-workflow';

export class ExampleNode implements INodeType {
	description: INodeTypeDescription = {
    // Basic node details here
    properties: [
      // Resources and operations here
    ]
  };

  async execute(this: IExecuteFunctions): Promise<INodeExecutionData[][]> {
    // Process data and return
  }
};
```

适用于所有节点类型的参数，请参阅[标准参数](standard-parameters.md)。有关编程式节点的更多信息，请参阅[编程式参数](programmatic-style-parameters.md)和[编程式 execute 方法](programmatic-style-execute-method.md)。

## 相关资源 <a id="related-resources"></a>

* [基础文件](./)
* [标准参数](standard-parameters.md)
* [声明式参数](declarative-style-parameters.md)
* [编程式参数](programmatic-style-parameters.md)
* [编程式 execute 方法](programmatic-style-execute-method.md)
