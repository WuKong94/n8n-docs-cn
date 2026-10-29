<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

> 完整文档索引见 [llms.txt](https://docs.n8n.io/llms.txt)。在页面 URL 后附加 `.md` 即可获取 Markdown 版本；本页的 [Markdown 版本](insights.md)可在此获取。

# 洞察 <a id="insights"></a>

洞察相关操作

## 获取洞察摘要 <a id="retrieve-insights-summary"></a>

> 获取所选日期范围的洞察摘要。

```json
{"openapi":"3.0.0","info":{"title":"n8n 公共 API","version":"1.1.1"},"tags":[{"name":"Insights","description":"洞察相关操作"}],"servers":[{"url":"/api/v1","description":"当前 n8n 实例（自托管版本的内置测试台）"},{"url":"{url}/api/v1","description":"自托管 n8n 实例","variables":{"url":{"default":"https://example.com"}}}],"security":[{"ApiKeyAuth":[]},{"BearerAuth":[]},{"CookieAuth":[]}],"components":{"securitySchemes":{"ApiKeyAuth":{"type":"apiKey","in":"header","name":"X-N8N-API-KEY"},"BearerAuth":{"type":"http","scheme":"bearer","bearerFormat":"JWT"},"CookieAuth":{"type":"apiKey","in":"cookie","name":"n8n-auth"}},"responses":{"badRequest":{"description":"请求无效，或提供的数据格式错误。"},"unauthorized":{"description":"未授权"},"forbidden":{"description":"禁止访问"}}},"paths":{"/insights/summary":{"get":{"operationId":"getInsightsSummary","tags":["Insights"],"summary":"获取洞察摘要","description":"获取所选日期范围的洞察摘要。","parameters":[{"schema":{"type":"string","format":"date-time","description":"ISO 8601 格式的开始日期，默认为 7 天前。"},"required":false,"name":"startDate","in":"query"},{"schema":{"type":"string","format":"date-time","description":"ISO 8601 格式的结束日期，默认为当前时间。"},"required":false,"name":"endDate","in":"query"},{"schema":{"type":"string","description":"项目标识符，用于按项目筛选洞察。"},"required":false,"name":"projectId","in":"query"}],"responses":{"200":{"description":"操作成功。","content":{"application/json":{"schema":{"type":"object","properties":{"total":{"type":"object","properties":{"value":{"type":"number"},"deviation":{"type":"number","nullable":true},"unit":{"type":"string","enum":["count"]}},"required":["value","deviation","unit"]},"failed":{"type":"object","properties":{"value":{"type":"number"},"deviation":{"type":"number","nullable":true},"unit":{"type":"string","enum":["count"]}},"required":["value","deviation","unit"]},"failureRate":{"type":"object","properties":{"value":{"type":"number"},"deviation":{"type":"number","nullable":true},"unit":{"type":"string","enum":["ratio"]}},"required":["value","deviation","unit"]},"timeSaved":{"type":"object","properties":{"value":{"type":"number"},"deviation":{"type":"number","nullable":true},"unit":{"type":"string","enum":["minute"]}},"required":["value","deviation","unit"]},"averageRunTime":{"type":"object","properties":{"value":{"type":"number"},"deviation":{"type":"number","nullable":true},"unit":{"type":"string","enum":["millisecond"]}},"required":["value","deviation","unit"]}},"required":["total","failed","failureRate","timeSaved","averageRunTime"]}}}},"400":{"$ref":"#/components/responses/badRequest"},"401":{"$ref":"#/components/responses/unauthorized"},"403":{"$ref":"#/components/responses/forbidden"}}}}}}
```
