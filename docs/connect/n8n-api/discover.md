<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

> 完整文档索引见 [llms.txt](https://docs.n8n.io/llms.txt)。在页面 URL 后附加 `.md` 即可获取 Markdown 版本；本页的 [Markdown 版本](discover.md)可在此获取。

# 能力发现 <a id="discover"></a>

API 能力发现

## 发现可用的 API 能力 <a id="discover-available-api-capabilities"></a>

> 根据调用方的 API 密钥作用域，返回筛选后的能力映射。每个资源都包含已认证 API 密钥可以访问的操作和端点。可通过查询参数缩小响应范围。

```json
{"openapi":"3.0.0","info":{"title":"n8n 公共 API","version":"1.1.1"},"tags":[{"name":"Discover","description":"API 能力发现"}],"servers":[{"url":"/api/v1","description":"当前 n8n 实例（自托管版本的内置测试台）"},{"url":"{url}/api/v1","description":"自托管 n8n 实例","variables":{"url":{"default":"https://example.com"}}}],"security":[{"ApiKeyAuth":[]},{"BearerAuth":[]},{"CookieAuth":[]}],"components":{"securitySchemes":{"ApiKeyAuth":{"type":"apiKey","in":"header","name":"X-N8N-API-KEY"},"BearerAuth":{"type":"http","scheme":"bearer","bearerFormat":"JWT"},"CookieAuth":{"type":"apiKey","in":"cookie","name":"n8n-auth"}},"responses":{"badRequest":{"description":"请求无效，或提供的数据格式错误。"},"unauthorized":{"description":"未授权"}}},"paths":{"/discover":{"get":{"operationId":"getDiscover","tags":["Discover"],"summary":"发现可用的 API 能力","description":"根据调用方的 API 密钥作用域，返回筛选后的能力映射。每个资源都包含已认证 API 密钥可以访问的操作和端点。可通过查询参数缩小响应范围。","parameters":[{"schema":{"type":"string","enum":["schemas"],"description":"包含附加数据。使用 \"schemas\" 可在每个端点中内联请求体架构，无需获取完整 OpenAPI 规范。"},"required":false,"name":"include","in":"query"},{"schema":{"type":"string","description":"筛选特定资源，例如 \"workflow\"、\"tags\" 或 \"credential\"。"},"required":false,"name":"resource","in":"query"},{"schema":{"type":"string","description":"筛选具有特定操作的端点，例如 \"read\"、\"create\" 或 \"list\"。"},"required":false,"name":"operation","in":"query"}],"responses":{"200":{"description":"操作成功。","content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"object","properties":{"scopes":{"type":"array","items":{"type":"string"},"description":"API 密钥当前有效的作用域"},"resources":{"type":"object","additionalProperties":{"type":"object","properties":{"operations":{"type":"array","items":{"type":"string"}},"endpoints":{"type":"array","items":{"type":"object","properties":{"method":{"type":"string"},"path":{"type":"string"},"operationId":{"type":"string"},"requestSchema":{"type":"object","description":"请求体架构（仅在 include=schemas 且端点接受请求体时返回）。"}},"required":["method","path","operationId"]}}},"required":["operations","endpoints"]}},"filters":{"type":"object","additionalProperties":{"type":"object","properties":{"description":{"type":"string"},"values":{"type":"array","items":{"type":"string"}}},"required":["description","values"]},"description":"可用的查询参数筛选条件。values 数组反映调用方作用域允许的值。"},"specUrl":{"type":"string","description":"完整 OpenAPI 规范的 URL"}},"required":["scopes","resources","filters","specUrl"]}},"required":["data"]}}}},"400":{"$ref":"#/components/responses/badRequest"},"401":{"$ref":"#/components/responses/unauthorized"}}}}}}
```
