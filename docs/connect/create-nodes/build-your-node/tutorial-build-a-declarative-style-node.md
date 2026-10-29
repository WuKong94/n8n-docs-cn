---
contentType: tutorial
nodeTitle: 教程：构建声明式节点
originalFilePath: integrations/creating-nodes/build/declarative-style-node.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/declarative-style-node
url: https://docs.n8n.io/connect/create-nodes/build-your-node/tutorial-build-a-declarative-style-node
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 构建声明式节点 <a href="#build-a-declarative-style-node" id="build-a-declarative-style-node"></a>

本教程逐步介绍如何构建声明式节点。开始前，请确认这正是所需的开发方式，更多信息请参阅[选择节点开发方式](../plan-your-node/choose-a-node-building-style.md)。

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

开发机器需要安装以下工具：

{% include "../../../reusable-content/.gitbook/includes/integrations/creating-nodes/prerequisites.md" %}

还需要了解：

- JavaScript/TypeScript
- REST API
- Git

## 构建节点 <a href="#build-your-node" id="build-your-node"></a>

本节将克隆 n8n 节点入门仓库，构建集成 [NASA API](https://api.nasa.gov/) 的节点，使用 NASA 的 APOD（每日天文图片）和 Mars Rover Photos（火星车照片）两项服务。为缩短代码示例，不会实现火星车照片端点的全部选项。

{% hint style="info" %}
**已有节点**

n8n 已内置 NASA 节点。为避免冲突，本教程的版本将使用不同名称。
{% endhint %}

### 第一步：设置项目 <a href="#step-1-set-up-the-project" id="step-1-set-up-the-project"></a>


n8n 提供节点开发入门仓库，确保包含所需的全部依赖，并提供 linter。

克隆仓库并进入目录：

1. 根据模板仓库[生成新仓库](https://github.com/n8n-io/n8n-nodes-starter/generate)。
2. 克隆新仓库：
		```shell
		git clone https://github.com/<your-organization>/<your-repo-name>.git n8n-nodes-nasa-pics
		cd n8n-nodes-nasa-pics
		```

入门项目包含示例节点和凭据，请删除以下目录和文件：

* `nodes/Example`
* `nodes/GithubIssues`
* `credentials/GithubIssuesApi.credentials.ts`
* `credentials/GithubIssuesOAuth2Api.credentials.ts`

然后创建以下目录和文件：

`nodes/NasaPics`  
`nodes/NasaPics/NasaPics.node.json`  
`nodes/NasaPics/NasaPics.node.ts`  
`credentials/NasaPicsApi.credentials.ts`  

这些是所有节点必需的关键文件。必需文件和推荐组织方式的更多说明，请参阅[节点文件结构](../plan-your-node/choose-node-file-structure.md)。

现在安装项目依赖：

```shell
npm i
```

### 第二步：添加图标 <a href="#step-2-add-an-icon" id="step-2-add-an-icon"></a>

将 [NASA SVG 标志](https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg)另存为 `nasapics.svg`，放入 `nodes/NasaPics/`。


{% include "../../../reusable-content/.gitbook/includes/integrations/creating-nodes/node-icons.md" %}


### 第三步：创建节点 <a href="#step-3-create-the-node" id="step-3-create-the-node"></a>

每个节点都必须有基础文件，参数详情请参阅[节点基础文件](reference/base-files/README.md)。

此示例使用 `NasaPics.node.ts` 文件。为简化教程，节点全部功能都放在这一个文件中。构建更复杂的节点时，应考虑按模块拆分功能。更多信息请参阅[节点文件结构](../plan-your-node/choose-node-file-structure.md)。

#### 第 3.1 步：导入 <a href="#step-31-imports" id="step-31-imports"></a>

先添加导入语句：

```typescript
import { NodeConnectionTypes } from 'n8n-workflow';
import type { INodeType, INodeTypeDescription } from 'n8n-workflow';
```

#### 第 3.2 步：创建主类 <a href="#step-32-create-the-main-class" id="step-32-create-the-main-class"></a>

节点必须导出一个实现 INodeType 的类。类的 `description` 配置对象必须包含 `properties` 数组。

{% hint style="info" %}
**类名与文件名**

请确保类名与文件名匹配。例如，类名为 `NasaPics` 时，文件名必须为 `NasaPics.node.ts`。
{% endhint %}
```typescript
export class NasaPics implements INodeType {
	description: INodeTypeDescription = {
		// Basic node details will go here
		properties: [
		// Resources and operations will go here
		]
	};
}
```

#### 第 3.3 步：添加节点详情 <a href="#step-33-add-node-details" id="step-33-add-node-details"></a>

所有节点都需要显示名称、图标及请求基本信息等参数。将以下内容添加到 `description`：

```typescript
displayName: 'NASA Pics',
name: 'nasaPics',
icon: 'file:nasapics.svg',
group: ['transform'],
version: 1,
subtitle: '={{$parameter["operation"] + ": " + $parameter["resource"]}}',
description: 'Get data from NASAs API',
defaults: {
	name: 'NASA Pics',
},
usableAsTool: true,
inputs: [ NodeConnectionTypes.Main ],
outputs: [ NodeConnectionTypes.Main ],
credentials: [
	{
		name: 'NasaPicsApi',
		required: true,
	},
],
requestDefaults: {
	baseURL: 'https://api.nasa.gov',
	headers: {
		Accept: 'application/json',
		'Content-Type': 'application/json',
	},
},
```

n8n 使用 `description` 中的部分属性，在编辑器界面渲染节点，包括 `displayName`、`icon`、`description` 和 `subtitle`。

#### 第 3.4 步：添加资源 <a href="#step-34-add-resources" id="step-34-add-resources"></a>

资源对象定义节点使用的 API 资源。本教程创建的节点访问两个 NASA API 端点：`planetary/apod` 和 `mars-photos`，因此需在 `NasaPics.node.ts` 中定义两个资源选项。将资源对象添加到 `properties` 数组：

```typescript
properties: [
	{
		displayName: 'Resource',
		name: 'resource',
		type: 'options',
		noDataExpression: true,
		options: [
			{
				name: 'Astronomy Picture of the Day',
				value: 'astronomyPictureOfTheDay',
			},
			{
				name: 'Mars Rover Photos',
				value: 'marsRoverPhotos',
			},
		],
		default: 'astronomyPictureOfTheDay',
	},
	// Operations will go here

]
```

`type` 控制 n8n 为资源显示哪种界面元素，并指定用户应输入的数据类型。`options` 会添加一个供用户单选的下拉菜单。更多信息请参阅[节点界面元素](reference/node-ui-elements.md)。

#### 第 3.5 步：添加操作 <a href="#step-35-add-operations" id="step-35-add-operations"></a>

操作对象定义可对资源执行哪些操作。

声明式节点的操作对象包含 `routing`，位于 `options` 数组中，用于配置 API 调用详情。

将以下内容添加到 `properties` 数组中，放在 `resource` 对象之后：

```typescript
{
	displayName: 'Operation',
	name: 'operation',
	type: 'options',
	noDataExpression: true,
	displayOptions: {
		show: {
			resource: [
				'astronomyPictureOfTheDay',
			],
		},
	},
	options: [
		{
			name: 'Get',
			value: 'get',
			action: 'Get the APOD',
			description: 'Get the Astronomy Picture of the day',
			routing: {
				request: {
					method: 'GET',
					url: '/planetary/apod',
				},
			},
		},
	],
	default: 'get',
},
{
	displayName: 'Operation',
	name: 'operation',
	type: 'options',
	noDataExpression: true,
	displayOptions: {
		show: {
			resource: [
				'marsRoverPhotos',
			],
		},
	},
	options: [
		{
			name: 'Get',
			value: 'get',
			action: 'Get Mars Rover photos',
			description: 'Get photos from the Mars Rover',
			routing: {
				request: {
					method: 'GET',
				},
			},
		},
	],
	default: 'get',
},
{
	displayName: 'Rover name',
	description: 'Choose which Mars Rover to get a photo from',
	required: true,
	name: 'roverName',
	type: 'options',
	options: [
		{name: 'Curiosity', value: 'curiosity'},
		{name: 'Opportunity', value: 'opportunity'},
		{name: 'Perseverance', value: 'perseverance'},
		{name: 'Spirit', value: 'spirit'},
	],
	routing: {
		request: {
			url: '=/mars-photos/api/v1/rovers/{{$value}}/photos',
		},
	},
	default: 'curiosity',
	displayOptions: {
		show: {
			resource: [
				'marsRoverPhotos',
			],
		},
	},
},
{
	displayName: 'Date',
	description: 'Earth date',
	required: true,
	name: 'marsRoverDate',
	type: 'dateTime',
	default:'',
	displayOptions: {
		show: {
			resource: [
				'marsRoverPhotos',
			],
		},
	},
	routing: {
		request: {
			// You've already set up the URL. qs appends the value of the field as a query string
			qs: {
				earth_date: '={{ new Date($value).toISOString().substr(0,10) }}',
			},
		},
	},
},
// Optional/additional fields will go here
```

此代码创建两个操作：获取当天的 APOD 图片，以及发送 GET 请求以获取某辆火星车的照片。名为 `roverName` 的对象要求用户选择哪辆火星车，火星车操作中的 `routing` 对象再引用此值来构建 API 调用 URL。

#### 第 3.6 步：可选字段 <a href="#step-36-optional-fields" id="step-36-optional-fields"></a>

多数 API 都有用于细化查询的可选字段，本示例的 NASA API 也不例外。

为避免一次显示过多选项，n8n 将这些字段放在界面的 **Additional Fields**（附加字段）中。

本教程将添加一个附加字段，让用户选择 APOD 端点使用的日期。将以下内容添加到 properties 数组：

```typescript
{
	displayName: 'Additional Fields',
	name: 'additionalFields',
	type: 'collection',
	default: {},
	placeholder: 'Add Field',
	displayOptions: {
		show: {
			resource: [
				'astronomyPictureOfTheDay',
			],
			operation: [
				'get',
			],
		},
	},
	options: [
		{
			displayName: 'Date',
			name: 'apodDate',
			type: 'dateTime',
			default: '',
			routing: {
				request: {
					// You've already set up the URL. qs appends the value of the field as a query string
					qs: {
						date: '={{ new Date($value).toISOString().substr(0,10) }}',
					},
				},
			},
		},
	],									
}
```


### 第四步：设置身份验证和凭据测试 <a href="#step-4-set-up-authentication-and-a-credential-test" id="step-4-set-up-authentication-and-a-credential-test"></a>

NASA API 要求使用 API 密钥进行身份验证，也可通过发送请求检查密钥是否有效。

将以下内容添加到 `nasaPicsApi.credentials.ts`：

```typescript
import {
	IAuthenticateGeneric,
	ICredentialTestRequest,
	ICredentialType,
	INodeProperties,
} from 'n8n-workflow';

export class NasaPicsApi implements ICredentialType {
	name = 'NasaPicsApi';
	displayName = 'NASA Pics API';
	// Uses the link to this tutorial as an example
	// Replace with your own docs links when building your own nodes
	documentationUrl = 'https://docs.n8n.io/integrations/creating-nodes/build/declarative-style-node/';
	properties: INodeProperties[] = [
		{
			displayName: 'API Key',
			name: 'apiKey',
			type: 'string',
			default: '',
		},
	];
	authenticate: IAuthenticateGeneric = {
		type: 'generic',
		properties: {
			qs: {
				'api_key': '={{$credentials.apiKey}}'
			}
		},
	};
	test: ICredentialTestRequest = {
		request: {
			baseURL: 'https://api.nasa.gov',
			url: '/apod',
		},
	};
}
```

凭据文件和选项的更多信息，请参阅[凭据文件](reference/credentials-files.md)。


### 第五步：添加节点元数据 <a href="#step-5-add-node-metadata" id="step-5-add-node-metadata"></a>

节点元数据保存在节点根目录的 JSON 文件中，n8n 将其称为 codex 文件。此示例的文件为 `NasaPics.node.json`。

将以下代码添加到 JSON 文件：

```json
{
	"node": "n8n-nodes-nasapics",
	"nodeVersion": "1.0",
	"codexVersion": "1.0",
	"categories": [
		"Miscellaneous"
	],
	"resources": {
		"credentialDocumentation": [
			{
				"url": ""
			}
		],
		"primaryDocumentation": [
			{
				"url": ""
			}
		]
	}
}
```

这些参数的更多信息，请参阅[节点 codex 文件](reference/codex-files.md)。

### 第六步：更新 npm 软件包信息 <a href="#step-6-update-the-npm-package-details" id="step-6-update-the-npm-package-details"></a>

npm 软件包信息位于项目根目录的 `package.json` 中，必须包含 `n8n` 对象，并指向凭据文件和节点基础文件。请更新该文件，加入以下信息：

```json
{
	// All node names must start with "n8n-nodes-"
	"name": "n8n-nodes-nasapics",
	"version": "0.1.0",
	"description": "n8n node to call NASA's APOD and Mars Rover Photo services.",
	"keywords": [
		// This keyword is required for community nodes
		"n8n-community-node-package"
	],
	"license": "MIT",
	"homepage": "https://n8n.io",
	"author": {
		"name": "Test",
		"email": "test@example.com"
	},
	"repository": {
		"type": "git",
		// Change the git remote to your own repository
		// Add the new URL here
		"url": "git+<your-repo-url>"
	},
	"main": "index.js",
	"scripts": {
		// don't change
	},
	"files": [
		"dist"
	],
	// Link the credentials and node
	"n8n": {
		"n8nNodesApiVersion": 1,
		"credentials": [
			"dist/credentials/NasaPicsApi.credentials.js"
		],
		"nodes": [
			"dist/nodes/NasaPics/NasaPics.node.js"
		]
	},
	"devDependencies": {
		// don't change
	},
	"peerDependencies": {
		// don't change
	}
}
```

请更新 `package.json`，填入自己的姓名、仓库 URL 等信息。npm `package.json` 文件的更多说明，请参阅 [npm 的 package.json 文档](https://docs.npmjs.com/cli/v8/configuring-npm/package-json)。

## 测试节点 <a href="#test-your-node" id="test-your-node"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/creating-nodes/testing.md" %}

## 后续步骤 <a href="#next-steps" id="next-steps"></a>

* [部署节点](../deploy-your-node/README.md)。
* 查看声明式节点示例：n8n 的 [Brevo 节点](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Brevo)。主节点采用声明式，触发节点则采用编程式。
* 了解[节点版本控制](reference/versioning.md)。

## 相关资源 <a id="related-resources"></a>

* [构建节点](./)
* [设置开发环境](set-up-your-development-environment.md)
* [使用 n8n-node 工具](using-the-n8n-node-tool.md)
* [教程：构建编程式节点](tutorial-build-a-programmatic-style-node.md)
* [参考](reference/README.md)
