---
description: HTTP Request 节点的分页示例。
contentType: howto
nodeTitle: 分页
originalFilePath: code/cookbook/http-node/pagination.md
originalUrl: https://docs.n8n.io/code/cookbook/http-node/pagination
url: https://docs.n8n.io/build/code-in-n8n/cookbook/http-request-node/pagination
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# HTTP Request 节点中的分页 <a href="#pagination-in-the-http-request-node" id="pagination-in-the-http-request-node"></a>

HTTP Request 节点支持分页。本页提供一些配置示例，包括使用 [HTTP 节点变量](../../use-built-in-shortcuts/http-node.md)。

该节点的更多信息请参阅 [HTTP Request](../../../../integrations/builtin/core-nodes/n8n-nodes-base.httprequest/README.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/http/pagination-api-differences.md" %}


## 启用分页 <a href="#enable-pagination" id="enable-pagination"></a>

在 HTTP Request 节点中，选择 **Add Option（添加选项）** > **Pagination（分页）**。

## 使用 `$response` 从响应 URL 获取下一页 <a href="#use-a-url-from-the-response-to-get-the-next-page-using-dollarresponse" id="use-a-url-from-the-response-to-get-the-next-page-using-dollarresponse"></a>

如果 API 在响应中返回下一页 URL：

1. 将 **Pagination Mode（分页模式）** 设为 **Response Contains Next URL（响应包含下一页 URL）**。n8n 会显示对应参数。
1. 在 **Next URL（下一页 URL）** 中，使用表达式[^1]设置 URL。具体表达式取决于 API 返回的数据。例如，API 在响应体中提供名为 `next-page` 的参数：
	```javascript
	{{ $response.body["next-page"] }}
	```

## 使用 `$pageCount` 按页码获取下一页 <a href="#get-the-next-page-by-number-using-dollarpagecount" id="get-the-next-page-by-number-using-dollarpagecount"></a>

如果所用 API 支持通过页码指定某一页：

1. 将 **Pagination Mode（分页模式）** 设为 **Update a Parameter in Each Request（每次请求更新一个参数）**。
1. 将 **Type（类型）** 设为 **Query（查询）**。
1. 输入查询参数的 **Name（名称）**。名称取决于 API，通常可在其文档中找到。例如，部分 API 使用名为 `page` 的查询参数设置页码，此时 **Name** 应为 `page`。
1. 将鼠标悬停在 **Value（值）** 上，开启 **Expression（表达式）**。
1. 输入 `{{ $pageCount + 1 }}`。

`$pageCount` 表示 HTTP Request 节点已获取的页数，从零开始。多数 API 分页从一开始，即第一页为 1。因此，将 `+1` 加到 `$pageCount` 上，节点就会在第一次循环获取第一页，第二次获取第二页，依此类推。

## 通过请求体参数分页 <a href="#navigate-pagination-through-body-parameters" id="navigate-pagination-through-body-parameters"></a>

如果所用 API 允许通过请求体参数分页：

1. 将 HTTP 请求方法设为 **POST**。
1. 将 **Pagination Mode（分页模式）** 设为 **Update a Parameter in Each Request（每次请求更新一个参数）**。
1. 在 **Type（类型）** 参数中选择 **Body（请求体）**。
1. 输入请求体参数的 **Name（名称）**。具体取决于 API，`page` 是常见键名。
1. 将鼠标悬停在 **Value（值）** 上，开启 **Expression（表达式）**。
1. 输入 `{{ $pageCount + 1 }}`。

## 在查询中设置每页大小 <a href="#set-the-page-size-in-the-query" id="set-the-page-size-in-the-query"></a>

如果所用 API 支持通过查询参数选择每页大小：

1. 在节点主参数中选择 **Send Query Parameters（发送查询参数）**。这是首次打开节点时看到的参数，而非选项内部的设置。
1. 输入查询参数的 **Name（名称）**。具体取决于 API。例如，许多 API 使用名为 `limit` 的参数设置每页大小，此时 **Name** 应为 `limit`。
1. 在 **Value（值）** 中输入每页大小。

[^1]: 在 n8n 中，表达式通过执行 JavaScript 代码动态填充节点参数。你可以使用 n8n 表达式语法，根据前面节点、其他工作流或 n8n 环境中的数据定义值，而不是提供静态值。

## 相关资源 <a id="related-resources"></a>

* [HTTP Request 节点](./)
