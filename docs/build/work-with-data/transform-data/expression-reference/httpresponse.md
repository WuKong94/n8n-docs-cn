---
nodeTitle: HTTPResponse（HTTP 响应）
originalFilePath: data/expression-reference/httpresponse.md
originalUrl: https://docs.n8n.io/data/expression-reference/httpresponse
url: https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/httpresponse
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# HTTPResponse（HTTP 响应） <a href="#httpresponse" id="httpresponse"></a>

## `$response`.**`body`** <a href="#dollarresponsebody" id="dollarresponsebody"></a>

**说明：** 最近一次 HTTP 调用的响应对象的正文。仅在 HTTP Request 节点中可用。

**语法：** `$response`.`$response`.**`body`**

**返回值：** Object（对象）

**来源：** n8n 自定义功能

## `$response`.**`headers`** <a href="#dollarresponseheaders" id="dollarresponseheaders"></a>

**说明：** 最近一次 HTTP 调用返回的响应头。仅在 HTTP Request 节点中可用。

**语法：** `$response`.`$response`.**`headers`**

**返回值：** Object（对象）

**来源：** n8n 自定义功能

## `$response`.**`statusCode`** <a href="#dollarresponsestatuscode" id="dollarresponsestatuscode"></a>

**说明：** 最近一次 HTTP 调用返回的 HTTP 状态码。仅在 HTTP Request 节点中可用。

**语法：** `$response`.`$response`.**`statusCode`**

**返回值：** Number（数字）

**来源：** n8n 自定义功能

## `$response`.**`statusMessage`** <a href="#dollarresponsestatusmessage" id="dollarresponsestatusmessage"></a>

**说明：** 关于请求状态的可选消息。仅在 HTTP Request 节点中可用。

**语法：** `$response`.`$response`.**`statusMessage`**

**返回值：** String（字符串）

**来源：** n8n 自定义功能


## 相关资源 <a id="related-resources"></a>

* [表达式参考](./)
