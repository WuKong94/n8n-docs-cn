---
contentType: reference
nodeTitle: HTTP 请求辅助方法
originalFilePath: integrations/creating-nodes/build/reference/http-helpers.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/reference/http-helpers
url: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/http-request-helpers
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 面向节点开发者的 HTTP 请求辅助方法 <a href="#http-request-helper-for-node-builders" id="http-request-helper-for-node-builders"></a>

n8n 提供灵活的 HTTP 请求辅助方法，封装了大部分复杂细节。

{% hint style="info" %}
**仅适用于编程式**

本文适用于使用编程式构建的节点，不适用于声明式节点。
{% endhint %}

## 用法 <a href="#usage" id="usage"></a>

在 `execute` 函数中调用辅助方法。

```typescript
// If no auth needed
const response = await this.helpers.httpRequest(options);

// If auth needed
const response = await this.helpers.httpRequestWithAuthentication.call(
	this, 
	'credentialTypeName', // For example: pipedriveApi
	options,
);
```

`options` 是一个对象：

```typescript
{
	url: string;
	headers?: object;
	method?: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'HEAD';
	body?: FormData | Array | string | number | object | Buffer | URLSearchParams;
	qs?: object;
	arrayFormat?: 'indices' | 'brackets' | 'repeat' | 'comma';
	auth?: {
		username: string,
		password: string,
	};
	disableFollowRedirect?: boolean;
	encoding?: 'arraybuffer' | 'blob' | 'document' | 'json' | 'text' | 'stream';
	skipSslCertificateValidation?: boolean;
	returnFullResponse?: boolean;
	proxy?: {
		host: string;
		port: string | number;
		auth?: {
			username: string;
			password: string;
		},
		protocol?: string;
	};
	timeout?: number;
	json?: boolean;
}	
```

`url` 为必填字段，其他字段均可选。默认请求方法为 `GET`。

各字段的说明：

- `body`：JSON 请求体可以使用普通 JavaScript 对象，文件上传可以使用 Buffer；`multipart/form-data` 可以使用 FormData 实例，`URLSearchParams` 则用于 `application/x-www-form-urlencoded`。
- `headers`：键值对。
	* 如果 `body` 是 `FormData` 的实例，n8n 会自动添加 `content-type: multipart/form-data`。
	* 如果 `body` 是 `URLSearchParams` 的实例，n8n 会添加 `content-type: application/x-www-form-urlencoded`。
	* 要覆盖此行为，请设置 `content-type` 请求头。
- `arrayFormat`：如果查询字符串包含数据数组，例如 `const qs = {IDs: [15,17]}`，则由 `arrayFormat` 的值决定 n8n 如何格式化。
	* `indices`（默认）：将 `{ a: ['b', 'c'] }` 格式化为 `a[0]=b&a[1]=c`。
	* `brackets`：将 `{ a: ['b', 'c'] }` 格式化为 `a[]=b&a[]=c`。
	* `repeat`：将 `{ a: ['b', 'c'] }` 格式化为 `a=b&a=c`。
	* `comma`：将 `{ a: ['b', 'c'] }` 格式化为 `a=b,c`。
- `auth`：用于 Basic Auth，需要提供 `username` 和 `password`。n8n 建议省略此字段，改用 `helpers.httpRequestWithAuthentication(...)`。
- `disableFollowRedirect`：n8n 默认跟随重定向。可以将此值设为 true，禁止跟随重定向。
- `skipSslCertificateValidation`：用于调用未配置有效证书的 HTTPS 服务。
- `returnFullResponse`：返回包含更多数据的对象，而非仅返回响应体，格式如下：`{body: body, headers: object, statusCode: 200, statusMessage: 'OK'}`
- `encoding`：n8n 可以检测内容类型，也可以指定 `arrayBuffer`，以接收可读取和操作的 Buffer。

> 译注：本页说明和迁移条目写作 arrayBuffer，但上方 options 类型示例列出的值是 arraybuffer，大小写不一致。此处保留原始说明和代码，请结合所用 n8n 版本的类型定义核对实际取值，不据此假定两种写法都受支持。

## 示例 <a href="#example" id="example"></a>

示例请参阅 [Mattermost 节点](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Mattermost/v1/MattermostV1.node.ts)。

## 旧版辅助方法的弃用 <a href="#deprecation-of-the-previous-helper" id="deprecation-of-the-previous-helper"></a>

{% hint style="warning" %}
**功能可用范围**

旧版 `this.helpers.request(options)` 实现使用并暴露 `request-promise` 库，已在 n8n 1.0 中移除。
{% endhint %}

为尽量减少不兼容问题，n8n 在内部透明地切换到另一个名为 `Axios` 的库。

如有问题，请在[社区论坛](https://community.n8n.io/)或 [GitHub](https://github.com/n8n-io/n8n/issues) 上反馈。

## 新版辅助方法迁移指南 <a href="#migration-guide-to-the-new-helper" id="migration-guide-to-the-new-helper"></a>

新版辅助方法更稳定、不依赖特定库，也更易于使用。

所有新节点都应使用新版辅助方法。对于已有自定义节点，也强烈建议迁移。迁移时主要注意以下事项：

- 接受 `url`，不接受 `uri`。
- `encoding: null` 现在必须改为 `encoding: arrayBuffer`。
- `rejectUnauthorized: false` 现在改为 `skipSslCertificateValidation: true`。
- 使用 `body` 指定请求体，具体格式由 `content-type` 请求头决定。
- `resolveWithFullResponse` 现在改为 `returnFullResponse`，行为相似。

## 相关资源 <a id="related-resources"></a>

* [节点构建参考](./)
