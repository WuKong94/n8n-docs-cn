---
title: HTTP 分页变量
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

| 变量 | 说明 |
| -------- | ----------- |
| `$pageCount` | 分页计数，跟踪节点已获取多少页。 |
| `$request` | HTTP 节点发送的请求对象。 |
| `$response` | HTTP 调用的响应对象，包含 `$response.body`、`$response.headers` 和 `$response.statusCode`。`body` 和 `headers` 的内容取决于 API 发送的数据。 |
