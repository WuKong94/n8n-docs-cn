---
contentType: reference
nodeTitle: 凭据文件
originalFilePath: integrations/creating-nodes/build/reference/credentials-files.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/reference/credentials-files
url: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 凭据文件 <a href="#credentials-file" id="credentials-file"></a>

凭据文件定义节点的授权方式。此文件中的设置决定 n8n 在 **Credentials**（凭据）弹窗中显示的内容，必须符合所连接服务的身份验证要求。

凭据文件支持所有 [n8n 界面元素](node-ui-elements.md)。n8n 使用加密密钥对凭据中存储的数据进行加密。

## 凭据文件的结构 <a href="#structure-of-the-credentials-file" id="structure-of-the-credentials-file"></a>

凭据文件遵循以下基本结构：

1. 添加导入语句。
2. 为凭据创建类。
3. 在类中定义控制节点身份验证的属性。

### 结构概览 <a href="#outline-structure" id="outline-structure"></a>

```js
import {
	IAuthenticateGeneric,
	ICredentialTestRequest,
	ICredentialType,
	INodeProperties,
} from 'n8n-workflow';

export class ExampleNode implements ICredentialType {
	name = 'exampleNodeApi';
	displayName = 'Example Node API';
	documentationUrl = '';
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
    		// Can be body, header, qs or auth
			qs: {
        		// Use the value from `apiKey` above
				'api_key': '={{$credentials.apiKey}}'
			}

		},
	};
	test: ICredentialTestRequest = {
		request: {
			baseURL: '={{$credentials?.domain}}',
			url: '/bearer',
		},
	};
}
```


## 参数 <a href="#parameters" id="parameters"></a>

### `name` <a href="#name" id="name"></a>

字符串。对象的内部名称，用于在节点的其他位置引用该对象。

### `displayName` <a href="#displayname" id="displayname"></a>

字符串。n8n 在图形界面中使用的名称。

### `documentationUrl` <a href="#documentationurl" id="documentationurl"></a>

字符串。凭据文档的 URL。

### `properties` <a href="#properties" id="properties"></a>

每个对象包含：

* `displayName`：n8n 在图形界面中使用的名称。
* `name`：对象的内部名称，用于在节点的其他位置引用该对象。
* `type`：预期的数据类型，例如 `string`。
* `default`：n8n 测试凭据时应使用的 URL。

### `authenticate` <a href="#authenticate" id="authenticate"></a>

* `authenticate`：对象。包含用于告诉 n8n 如何在 API 请求中注入身份验证数据的对象。

#### `type` <a href="#type" id="type"></a>

字符串。如果身份验证方式在请求头、请求体或查询字符串中发送数据，请将此值设为 `'generic'`。

#### `properties` <a href="#properties" id="properties"></a>

对象。定义身份验证方式，可选项：

* `body`：对象。在请求体中发送身份验证数据，可包含嵌套对象。
```typescript
authenticate: IAuthenticateGeneric = {
	type: 'generic',
	properties: {
		body: {
			username: '={{$credentials.username}}',
			password: '={{$credentials.password}}',
		},
	},
};
``` 

* `header`：对象。在请求头中发送身份验证数据。
```typescript
authenticate: IAuthenticateGeneric = {
	type: 'generic',
	properties: {
		header: {
			Authorization: '=Bearer {{$credentials.authToken}}',
		},
	},
};
``` 

* `qs`：对象，表示“查询字符串”（query string）。在请求的查询字符串中发送身份验证数据。
```typescript
authenticate: IAuthenticateGeneric = {
	type: 'generic',
	properties: {
		qs: {
			token: '={{$credentials.token}}',
		},
	},
};
``` 

* `auth`：对象。用于 Basic Auth，要求以 `username` 和 `password` 作为键名。
```typescript
authenticate: IAuthenticateGeneric = {
	type: 'generic',
	properties: {
		auth: {
			username: '={{$credentials.username}}',
			password: '={{$credentials.password}}',
		},
	},
};
```

### `test` <a href="#test" id="test"></a>

提供一个包含 URL 和身份验证类型的 `request` 对象，供 n8n 测试凭据。

```typescript
test: ICredentialTestRequest = {
		request: {
			baseURL: '={{$credentials?.domain}}',
			url: '/bearer',
		},
	};
```

## 相关资源 <a id="related-resources"></a>

* [节点构建参考](./)
