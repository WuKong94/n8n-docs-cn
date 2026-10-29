---
contentType: tutorial
nodeTitle: 教程：构建编程式节点
originalFilePath: integrations/creating-nodes/build/programmatic-style-node.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/programmatic-style-node
url: https://docs.n8n.io/connect/create-nodes/build-your-node/tutorial-build-a-programmatic-style-node
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 构建编程式节点 <a href="#build-a-programmatic-style-node" id="build-a-programmatic-style-node"></a>

本教程逐步介绍如何构建编程式节点。开始前，请确认这正是所需的开发方式，更多信息请参阅[选择节点开发方式](../plan-your-node/choose-a-node-building-style.md)。

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

开发机器需要安装以下工具：

{% include "../../../reusable-content/.gitbook/includes/integrations/creating-nodes/prerequisites.md" %}

还需要了解：

- JavaScript/TypeScript
- REST API
- Git
- n8n 中的表达式[^1]


## 构建节点 <a href="#build-your-node" id="build-your-node"></a>

本节将克隆 n8n 节点入门仓库，构建集成 [SendGrid](https://sendgrid.com/) 的节点，实现 SendGrid 的一项功能：创建联系人。

{% hint style="info" %}
**已有节点**

n8n 已内置 SendGrid 节点。为避免冲突，本教程的版本将使用不同名称。
{% endhint %}

### 第一步：设置项目 <a href="#step-1-set-up-the-project" id="step-1-set-up-the-project"></a>

n8n 提供节点开发入门仓库，确保包含所需的全部依赖，并提供 linter。

克隆仓库并进入目录：

1. 根据模板仓库[生成新仓库](https://github.com/n8n-io/n8n-nodes-starter/generate)。
2. 克隆新仓库：
		```shell
		git clone https://github.com/<your-organization>/<your-repo-name>.git n8n-nodes-friendgrid
		cd n8n-nodes-friendgrid
		```

入门项目包含示例节点和凭据，请删除以下目录和文件：

* `nodes/Example`
* `nodes/GithubIssues`
* `credentials/GithubIssuesApi.credentials.ts`
* `credentials/GithubIssuesOAuth2Api.credentials.ts`

然后创建以下目录和文件：

`nodes/FriendGrid`  
`nodes/FriendGrid/FriendGrid.node.json`  
`nodes/FriendGrid/FriendGrid.node.ts`  
`credentials/FriendGridApi.credentials.ts`  

这些是所有节点必需的关键文件。必需文件和推荐组织方式的更多说明，请参阅[节点文件结构](../plan-your-node/choose-node-file-structure.md)。

现在安装项目依赖：

```shell
npm i
```

### 第二步：添加图标 <a href="#step-2-add-an-icon" id="step-2-add-an-icon"></a>

将 [SendGrid SVG 标志](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/SendGrid/sendGrid.svg)另存为 `friendGrid.svg`，放入 `nodes/FriendGrid/`。


{% include "../../../reusable-content/.gitbook/includes/integrations/creating-nodes/node-icons.md" %}


### 第三步：在基础文件中定义节点 <a href="#step-3-define-the-node-in-the-base-file" id="step-3-define-the-node-in-the-base-file"></a>

每个节点都必须有基础文件，参数详情请参阅[节点基础文件](reference/base-files/README.md)。

此示例使用 `FriendGrid.node.ts` 文件。为简化教程，节点全部功能都放在这一个文件中。构建更复杂的节点时，应考虑按模块拆分功能。更多信息请参阅[节点文件结构](../plan-your-node/choose-node-file-structure.md)。

#### 第 3.1 步：导入 <a href="#step-31-imports" id="step-31-imports"></a>

先添加导入语句：

```typescript
import type {
	IDataObject,
	IExecuteFunctions,
	IHttpRequestOptions,
	INodeExecutionData,
	INodeType,
	INodeTypeDescription,
} from 'n8n-workflow';
import { NodeConnectionTypes } from 'n8n-workflow';
```

#### 第 3.2 步：创建主类 <a href="#step-32-create-the-main-class" id="step-32-create-the-main-class"></a>

节点必须导出一个实现 `INodeType` 的类。类的 `description` 配置对象必须包含 `properties` 数组。

{% hint style="info" %}
**类名与文件名**

请确保类名与文件名匹配。例如，类名为 `FriendGrid` 时，文件名必须为 `FriendGrid.node.ts`。
{% endhint %}
```typescript
export class FriendGrid implements INodeType {
	description: INodeTypeDescription = {
		// Basic node details will go here
		properties: [
			// Resources and operations will go here
		],
	};
	// The execute method will go here
	async execute(this: IExecuteFunctions): Promise<INodeExecutionData[][]> {
	}
}
```

#### 第 3.3 步：添加节点详情 <a href="#step-33-add-node-details" id="step-33-add-node-details"></a>

所有编程式节点都需要显示名称、图标等基本参数。将以下内容添加到 `description`：

```typescript
displayName: 'FriendGrid',
name: 'friendGrid',
icon: 'file:friendGrid.svg',
group: ['transform'],
version: 1,
description: 'Consume SendGrid API',
defaults: {
	name: 'FriendGrid',
},
inputs: [NodeConnectionTypes.Main],
outputs: [NodeConnectionTypes.Main],
usableAsTool: true,
credentials: [
	{
		name: 'friendGridApi',
		required: true,
	},
],
```

n8n 使用 `description` 中的部分属性在编辑器界面渲染节点，包括 `displayName`、`icon` 和 `description`。

#### 第 3.4 步：添加资源 <a href="#step-34-add-the-resource" id="step-34-add-the-resource"></a>

资源对象定义节点使用的 API 资源。本教程的节点访问 SendGrid 的 `/v3/marketing/contacts` 端点，因此需为此端点定义资源。将资源对象添加到 `properties` 数组：

```typescript
{
	displayName: 'Resource',
	name: 'resource',
	type: 'options',
	options: [
		{
			name: 'Contact',
			value: 'contact',
		},
	],
	default: 'contact',
	noDataExpression: true,
	required: true,
	description: 'Create a new contact',
},
```

`type` 控制 n8n 为资源显示哪种界面元素，并指定用户应输入的数据类型。`options` 会添加一个供用户单选的下拉菜单。更多信息请参阅[节点界面元素](reference/node-ui-elements.md)。

#### 第 3.5 步：添加操作 <a href="#step-35-add-operations" id="step-35-add-operations"></a>

操作对象定义可对资源做什么，通常对应 REST API 动词（GET、POST 等）。本教程仅包含创建联系人这一项操作，必填字段为待创建联系人的邮箱地址。

将以下内容添加到 `properties` 数组中，放在 `resource` 对象之后：

```typescript
{
	displayName: 'Operation',
	name: 'operation',
	type: 'options',
	displayOptions: {
		show: {
			resource: [
				'contact',
			],
		},
	},
	options: [
		{
			name: 'Create',
			value: 'create',
			description: 'Create a contact',
			action: 'Create a contact',
		},
	],
	default: 'create',
	noDataExpression: true,
},
{
	displayName: 'Email',
	name: 'email',
	type: 'string',
	required: true,
	displayOptions: {
		show: {
			operation: [
				'create',
			],
			resource: [
				'contact',
			],
		},
	},
	default:'',
	placeholder: 'name@email.com',
	description:'Primary email for the contact',
},
```

#### 第 3.6 步：添加可选字段 <a href="#step-36-add-optional-fields" id="step-36-add-optional-fields"></a>

多数 API 都有用于细化查询的可选字段，本示例的 SendGrid API 也不例外。

为避免一次显示过多选项，n8n 将这些字段放在界面的 **Additional Fields**（附加字段）中。

本教程将添加两个附加字段，让用户输入联系人的名字和姓氏。将以下内容添加到 properties 数组：

```typescript
{
	displayName: 'Additional Fields',
	name: 'additionalFields',
	type: 'collection',
	placeholder: 'Add Field',
	default: {},
	displayOptions: {
		show: {
			resource: [
				'contact',
			],
			operation: [
				'create',
			],
		},
	},
	options: [
		{
			displayName: 'First Name',
			name: 'firstName',
			type: 'string',
			default: '',
		},
		{
			displayName: 'Last Name',
			name: 'lastName',
			type: 'string',
			default: '',
		},
	],
},
```

### 第四步：添加 execute 方法 <a href="#step-4-add-the-execute-method" id="step-4-add-the-execute-method"></a>

节点界面和基本信息已设置好，接下来将界面映射到 API 请求，让节点真正执行操作。

节点每次运行时都会执行 `execute` 方法。在该方法中，可访问输入数据项以及用户在界面中设置的参数，包括凭据。

将以下 `execute` 方法添加到 `FriendGrid.node.ts` 中：

```typescript
// Handle data coming from previous nodes
const items = this.getInputData();
let responseData;
const returnData: INodeExecutionData[] = [];
const resource = this.getNodeParameter('resource', 0);
const operation = this.getNodeParameter('operation', 0);

// For each item, make an API call to create a contact
for (let i = 0; i < items.length; i++) {
	try {
		if (resource === 'contact') {
			if (operation === 'create') {
				// Get email input
				const email = this.getNodeParameter('email', i);
				// Get additional fields input
				const additionalFields = this.getNodeParameter('additionalFields', i);
				const data: IDataObject = {
					email,
				};

				Object.assign(data, additionalFields);

				// Make HTTP request according to https://sendgrid.com/docs/api-reference/
				const options: IHttpRequestOptions = {
					headers: {
						'Accept': 'application/json',
					},
					method: 'PUT',
					body: {
						contacts: [
							data,
						],
					},
					url: 'https://api.sendgrid.com/v3/marketing/contacts',
					json: true,
				};
				responseData = await this.helpers.httpRequestWithAuthentication.call(this, 'friendGridApi', options);
				const executionData = this.helpers.constructExecutionMetaData(
					this.helpers.returnJsonArray(responseData as IDataObject),
					{ itemData: { item: i } },
				);

				returnData.push.apply(returnData, executionData);
			}
		}
	} catch (error) {
		if (this.continueOnFail()) {
			const executionData = this.helpers.constructExecutionMetaData(
				this.helpers.returnJsonArray({ error: error.message }),
				{ itemData: { item: i } },
			);
			returnData.push.apply(returnData, executionData);
			continue;
		}
		throw error;
	}
}
return [returnData];
```

请注意代码中的以下几行：

```typescript
const items = this.getInputData();
... 
for (let i = 0; i < items.length; i++) {
	...
	const email = this.getNodeParameter('email', i);
	...
}
```

用户可通过两种方式提供数据：

* 直接在节点字段中填写。
* 映射工作流前面节点的数据。

`getInputData()` 及其后的循环，使节点能够处理来自前序节点的数据，并支持多个输入数据项。例如，前序节点输出五个人的联系信息时，FriendGrid 节点就能创建五个联系人。


### 第五步：设置身份验证 <a href="#step-5-set-up-authentication" id="step-5-set-up-authentication"></a>

SendGrid API 要求使用 API 密钥进行身份验证。

将以下内容添加到 `FriendGridApi.credentials.ts`：

```typescript
import {
	IAuthenticateGeneric,
	ICredentialTestRequest,
	ICredentialType,
	INodeProperties,
} from 'n8n-workflow';

export class FriendGridApi implements ICredentialType {
	name = 'friendGridApi';
	displayName = 'FriendGrid API';
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
			headers: {
				Authorization: '=Bearer {{$credentials.apiKey}}',
			},
		},
	};

	test: ICredentialTestRequest = {
		request: {
			baseURL: 'https://api.sendgrid.com/v3',
			url: '/marketing/contacts',
		},
	};
}

```

凭据文件和选项的更多信息，请参阅[凭据文件](reference/credentials-files.md)。

### 第六步：添加节点元数据 <a href="#step-6-add-node-metadata" id="step-6-add-node-metadata"></a>

节点元数据保存在节点根目录的 JSON 文件中，n8n 将其称为 codex 文件。此示例的文件为 `FriendGrid.node.json`。

将以下代码添加到 JSON 文件：

```json
{
	"node": "n8n-nodes-friendgrid",
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


### 第七步：更新 npm 软件包信息 <a href="#step-7-update-the-npm-package-details" id="step-7-update-the-npm-package-details"></a>

npm 软件包信息位于项目根目录的 `package.json` 中，必须包含 `n8n` 对象，并指向凭据文件和节点基础文件。请更新该文件，加入以下信息：

```json
{
	// All node names must start with "n8n-nodes-"
	"name": "n8n-nodes-friendgrid",
	"version": "0.1.0",
	"description": "n8n node to create contacts in SendGrid",
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
			"dist/credentials/FriendGridApi.credentials.js"
		],
		"nodes": [
			"dist/nodes/FriendGrid/FriendGrid.node.js"
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
* 查看编程式节点示例：n8n 的 [Mattermost 节点](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Mattermost)，它采用了更复杂的编程式节点结构。
* 了解[节点版本控制](reference/versioning.md)。
* 确保理解[数据项关联](../../../build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows.md)和[数据结构](../../../build/work-with-data/understand-n8ns-data-structure.md)等关键概念。

[^1]: n8n 表达式通过执行 JavaScript 代码，动态填写节点参数。无需只提供静态值，可使用 n8n 表达式语法，根据前序节点、其他工作流或 n8n 环境中的数据定义值。

## 相关资源 <a id="related-resources"></a>

* [构建节点](./)
* [设置开发环境](set-up-your-development-environment.md)
* [使用 n8n-node 工具](using-the-n8n-node-tool.md)
* [教程：构建声明式节点](tutorial-build-a-declarative-style-node.md)
* [参考](reference/README.md)
