---
description: n8n 公共 REST API 的分页方式。
contentType: howto
nodeTitle: 分页
originalFilePath: api/pagination.md
originalUrl: https://docs.n8n.io/api/pagination
url: https://docs.n8n.io/connect/n8n-api/pagination
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# API 分页 <a href="#api-pagination" id="api-pagination"></a>

默认每页返回 100 条结果，可以调整每页数量，上限为 250 条。

结果超过一页时，响应会包含游标，可使用该游标请求后续页面。

例如，要获取所有活跃工作流，每次获取 150 个。

获取第一页：

```shell
# For a self-hosted n8n instance <a href="#for-a-self-hosted-n8n-instance" id="for-a-self-hosted-n8n-instance"></a>
curl -X 'GET' \
  '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true&limit=150' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>'

# For n8n Cloud <a href="#for-n8n-cloud" id="for-n8n-cloud"></a>
curl -X 'GET' \
  '<your-cloud-instance>/api/v<version-number>/workflows?active=true&limit=150' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>'
```

响应为 JSON 格式，并包含 `nextCursor` 值。以下是响应示例。

```js
{
  "data": [
    // The response contains an object for each workflow
    {
      // Workflow data
    }
  ],
  "nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"
}
```

然后请求下一页：

```bash
# For a self-hosted n8n instance <a href="#for-a-self-hosted-n8n-instance" id="for-a-self-hosted-n8n-instance"></a>
curl -X 'GET' \
  '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true&limit=150&cursor=MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA' \
  -H 'accept: application/json'

# For n8n Cloud <a href="#for-n8n-cloud" id="for-n8n-cloud"></a>
curl -X 'GET' \
  '<your-cloud-instance>/api/v<version-number>/workflows?active=true&limit=150&cursor=MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA' \
  -H 'accept: application/json'
```

## 相关资源 <a id="related-resources"></a>

* [n8n API](./)
* [身份验证](authentication.md)
* [幂等性](idempotency.md)
* [使用 API 测试台](use-an-api-playground.md)
* [端点参考](api-reference.md)
