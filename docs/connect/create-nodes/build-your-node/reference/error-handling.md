---
contentType: reference
nodeTitle: 错误处理
originalFilePath: integrations/creating-nodes/build/reference/error-handling.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/reference/error-handling
url: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/error-handling
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# n8n 节点中的错误处理 <a href="#error-handling-in-n8n-nodes" id="error-handling-in-n8n-nodes"></a>

正确处理错误，是构建稳定 n8n 节点的关键，能在发生问题时向用户提供清晰反馈。n8n 提供两个专门的错误类，用于处理节点实现中的不同故障：

- [**`NodeApiError`**](#nodeapierror)：用于 API 相关错误和外部服务故障。
- [**`NodeOperationError`**](#nodeoperationerror)：用于操作错误、验证失败和配置问题。

## NodeApiError <a href="#nodeapierror" id="nodeapierror"></a>

处理外部 API 调用和 HTTP 请求时，请使用 `NodeApiError`。此错误类专用于处理 API 响应错误，并增强了解析和展示以下 API 相关故障的能力：

 * HTTP 请求失败
 * 外部 API 错误
 * 身份验证或授权失败
 * 请求速率限制错误
 * 服务不可用错误
 
使用以下方式初始化新的 `NodeApiError` 实例：

```typescript
new NodeApiError(node: INode, errorResponse: JsonObject, options?: NodeApiErrorOptions)
```

### 常见用法 <a href="#common-usage-patterns" id="common-usage-patterns"></a>

对于基本的 API 请求失败，捕获错误并将其包装为 `NodeApiError`：

```typescript
try {
	const response = await this.helpers.httpRequestWithAuthentication.call(
		this,
		credentialType,
		options
	);
	return response;
} catch (error) {
	throw new NodeApiError(this.getNode(), error as JsonObject);
}
```

针对特定 HTTP 状态码提供自定义消息：

```typescript
try {
	const response = await this.helpers.httpRequestWithAuthentication.call(
		this,
		credentialType,
		options
	);
	return response;
} catch (error) {
	if (error.httpCode === "404") {
		const resource = this.getNodeParameter("resource", 0);
		const errorOptions = {
			message: `${
				resource.charAt(0).toUpperCase() + resource.slice(1)
			} not found`,
			description:
				"The requested resource could not be found. Please check your input parameters.",
		};
		throw new NodeApiError(
			this.getNode(),
			error as JsonObject,
			errorOptions
		);
	}

	if (error.httpCode === "401") {
		throw new NodeApiError(this.getNode(), error as JsonObject, {
			message: "Authentication failed",
			description: "Please check your credentials and try again.",
		});
	}

	throw new NodeApiError(this.getNode(), error as JsonObject);
}
```

## NodeOperationError <a href="#nodeoperationerror" id="nodeoperationerror"></a>

以下情况请使用 `NodeOperationError`：

 * 操作错误
 * 验证失败
 * 与外部 API 调用无关的配置问题
 * 输入验证错误
 * 缺少必填参数
 * 数据转换错误
 * 工作流逻辑错误
 
 使用以下方式初始化新的 `NodeOperationError` 实例：

```typescript
new NodeOperationError(node: INode, error: Error | string | JsonObject, options?: NodeOperationErrorOptions)
```

### 常见用法 <a href="#common-usage-patterns" id="common-usage-patterns"></a>

使用 `NodeOperationError` 验证用户输入：

```typescript
const email = this.getNodeParameter("email", itemIndex);

if (email.indexOf("@") === -1) {
	const description = `The email address '${email}' in the 'email' field isn't valid`;
	throw new NodeOperationError(this.getNode(), "Invalid email address", {
		description,
		itemIndex, // for multiple items, this will link the error to the specific item
	});
}
```

处理多个数据项时，请包含数据项索引，以提供更完整的错误上下文：

```typescript
for (let i = 0; i < items.length; i++) {
	try {
		// Process item
		const result = await processItem(items[i]);
		returnData.push(result);
	} catch (error) {
		if (this.continueOnFail()) {
			returnData.push({
				json: { error: error.message },
				pairedItem: { item: i },
			});
			continue;
		}

		throw new NodeOperationError(this.getNode(), error as Error, {
			description: error.description,
			itemIndex: i,
		});
	}
}
```

## 声明操作失败的原因 <a id="declaring-why-an-operation-failed"></a>

{% hint style="info" %}
**功能可用范围**

从 n8n 3.37 起可使用失败声明。
{% endhint %}

`NodeApiError` 和 `NodeOperationError` 都接受 `failure` 选项，用于说明操作失败的原因。当节点能根据响应确定具体问题时，例如配额耗尽或凭据失效，可以使用此选项。该声明作为普通数据存储在错误的 `failure` 属性中。节点只声明原因，不决定处理措施；所有根据声明采取的行为由 n8n 决定，例如轮询触发器在轮询失败后如何退避。

构造错误时传入声明：

```typescript
throw new NodeApiError(this.getNode(), error as JsonObject, {
	failure: { cause: 'rate-limited' },
});
```

### 失败原因 <a id="failure-causes"></a>

`cause` 字段接受六个值之一。前三个值描述可自行恢复的故障，后三个值需要有人采取措施，操作才能成功。

| `cause` | 含义 |
|---------|---------|
| `rate-limited` | 服务正在限制请求速率。 |
| `quota-exhausted` | 用量配额已耗尽，配额重置前操作都会失败。 |
| `temporarily-unavailable` | 服务当前不可用或处于降级状态。 |
| `credential-invalid` | 凭据已失效，用户需要重新连接。 |
| `configuration-invalid` | 节点指向的对象已不存在，或已不再允许访问。 |
| `node-defect` | 节点自身存在缺陷，与凭据和配置无关。 |

### 等待提示 <a id="wait-hints"></a>

对于 `rate-limited`、`quota-exhausted` 和 `temporarily-unavailable`，可以添加可选提示，说明操作何时可能恢复。其他原因没有可等待的恢复条件，因此不接受这些提示。

| 字段 | 含义 |
|-------|---------|
| `retryAfterMs` | 服务要求的最短等待时间，单位为毫秒。 |
| `resetsAtEpochMs` | 服务声明操作恢复的时间，使用 Unix 纪元毫秒数表示。 |

例如，对于已知重置时间的配额，可以声明其恢复时间：

```typescript
throw new NodeApiError(this.getNode(), error as JsonObject, {
	failure: { cause: 'quota-exhausted', resetsAtEpochMs: nextQuotaReset() },
});
```

### 对 API 错误进行分类 <a id="classifying-api-errors"></a>

只声明响应能够证明的原因。如果无法确定错误类别，请原样抛出错误；没有声明的错误仍然有效。

```typescript
try {
	return await this.helpers.httpRequestWithAuthentication.call(
		this,
		credentialType,
		options
	);
} catch (error) {
	if (error.httpCode === "401") {
		throw new NodeApiError(this.getNode(), error as JsonObject, {
			failure: { cause: "credential-invalid" },
		});
	}

	if (error.httpCode === "429") {
		throw new NodeApiError(this.getNode(), error as JsonObject, {
			failure: { cause: "rate-limited" },
		});
	}

	throw new NodeApiError(this.getNode(), error as JsonObject);
}
```

## 相关资源 <a id="related-resources"></a>

* [节点构建参考](./)
