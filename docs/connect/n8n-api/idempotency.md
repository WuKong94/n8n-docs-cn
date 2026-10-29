---
description: 使用 Idempotency-Key 请求头重试 n8n 公共 API POST 请求。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# API 幂等性 <a id="api-idempotency"></a>

在公共 API POST 请求中发送 `Idempotency-Key` 请求头，可使重试返回第一次成功的响应，避免重复执行请求。

{% hint style="info" %}
**功能可用范围**

自 n8n 2.45.0 起，以下方案或版本支持 n8n API 幂等性：

- **n8n Cloud：**Starter、Pro、Enterprise。
- **自托管：**所有版本。

免费试用期间无法使用。
{% endhint %}

此请求头可选。不发送时，每个 POST 都会正常执行。

## 发送幂等键 <a id="send-an-idempotency-key"></a>

在第一次 POST 中设置 `Idempotency-Key` 请求头，重试时再次发送相同请求头。每个独立请求使用新键。UUID v4 是合适的选择，但 n8n 不强制要求该格式。

键值必须包含 1 到 128 个可见 ASCII 字符，可使用字母、数字和符号，不能包含空格。n8n 会忽略键前后的空格。空值或仅含空格的值等同于未发送该请求头。

```shell
curl -X POST \
  'https://<your-instance>/api/v1/workflows' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>' \
  -H 'Idempotency-Key: <idempotency-key>' \
  -H 'Content-Type: application/json' \
  -d '<workflow-json>'
```

将 `<workflow-json>` 替换为工作流请求体。创建 API 密钥的方法请参阅[身份验证](authentication.md)。

键过长、包含空格或其他不允许的字符时，会返回 `400`，且不会创建资源。消息为 `Idempotency-Key must be 1 to 128 visible ASCII characters.`

## 哪些请求使用幂等键 <a id="requests-that-use-the-key"></a>

n8n 会在创建资源或启动工作的 POST 请求中使用此请求头，例如创建工作流或调用 `POST /api/v1/executions/<execution-id>/retry`。[端点参考](api-reference.md)会在每个支持的 POST 中列出该请求头。

对于 `GET`、`PUT`、`PATCH` 和 `DELETE`，n8n 会忽略该请求头。

## n8n 保留响应的时间 <a id="how-long-n8n-keeps-the-response"></a>

从发送键时起，n8n 将第一次成功的响应保留 12 小时。在此窗口内重试，会返回该响应，不再执行 POST。

12 小时后，相同键会再次执行 POST，可能创建重复资源。下一次操作请发送新键。

键属于用户，而非某个 API 密钥。同一用户的两个 API 密钥共享已存储的响应。不同用户使用相同键，会被视为独立请求。

## 重试相同请求 <a id="retry-the-same-request"></a>

再次发送相同键，以及完全相同的路径、查询字符串和请求体，包括 JSON 字段顺序和所有空格。匹配时，返回与第一次响应相同的状态码和 JSON 响应体。

返回文件的 POST 不在支持范围内，重试时会再次执行请求。

### 键相同，请求不同 <a id="same-key-different-request"></a>

如果路径、查询字符串或请求体不同，n8n 会返回 `422`，且不执行 POST：

```json
{
	"message": "This Idempotency-Key was already used with a different request."
}
```

更改后的请求请发送新键，首次创建的资源保持不变。

### 请求仍在进行中 <a id="request-still-in-progress"></a>

如果第一次请求尚未完成，n8n 会返回 `409`：

```json
{
	"message": "A request with this Idempotency-Key is already in progress."
}
```

等待后，再次发送相同键和相同请求。两个同时使用同一键的请求不会创建两个资源：其中一个完成工作，另一个收到 `409`；如果第一个已完成，则收到首次响应。

## 请求失败时 <a id="when-the-request-fails"></a>

如果 POST 失败，n8n 不会保留该响应。使用相同键和相同请求重试，会再次执行 POST。

如果第一次 POST 因请求体无效而返回 `400`，可修正请求体后再次发送相同键。

## 幂等键的限制 <a id="limits-of-an-idempotency-key"></a>

幂等请求头仅适用于 `/api/v1` 下的公共 API 端点。

## 相关资源 <a id="related-resources"></a>

* [n8n API](./)
* [身份验证](authentication.md)
* [分页](pagination.md)
* [使用 API 测试台](use-an-api-playground.md)
* [端点参考](api-reference.md)
