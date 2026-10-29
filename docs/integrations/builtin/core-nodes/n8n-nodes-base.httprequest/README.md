---
title: HTTP Request 节点
description: 了解如何在 n8n 中使用 HTTP Request 节点，并将其集成到工作流。
contentType:
- integration
- reference
priority: critical
nodeTitle: n8n-nodes-base.httprequest
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# HTTP Request 节点 <a href="#http-request-node" id="http-request-node"></a>

HTTP Request 是 n8n 中用途最广泛的节点之一，可通过 HTTP 请求查询任何提供 REST API 的应用或服务中的数据。可以将其用作普通节点，也可以连接到 [AI 智能体](../../cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md)，作为[工具](../../../../build/integrate-ai/understand-ai-components/how-tools-work.md){ data-preview }使用。

使用此节点相当于创建 REST API 调用，需要了解基本的 API 术语和概念。

有两种方式创建 HTTP 请求：配置[节点参数](#node-parameters)，或[导入 curl 命令](#import-curl-command)。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [HTTP Request 凭据](../../credentials/httprequest.md)。
{% endhint %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

### Method（请求方法） <a href="#method" id="method"></a>

选择请求使用的方法：

- DELETE
- GET
- HEAD
- OPTIONS
- PATCH
- POST
- PUT

### URL <a href="#url" id="url"></a>

输入要使用的端点。

### Authentication（身份验证） <a href="#authentication" id="authentication"></a>

可用时，n8n 建议选择 **Predefined Credential Type**（预定义凭据类型）。与手动配置通用凭据相比，它更便于设置和管理凭据。

#### 预定义凭据 <a href="#predefined-credentials" id="predefined-credentials"></a>

用于 n8n 支持的集成，包括内置节点和社区节点。使用 **Predefined Credential Type**（预定义凭据类型）执行自定义操作，无需额外设置。更多信息，请参阅[自定义 API 操作](../../custom-api-actions-for-existing-nodes.md)。

#### 通用凭据 <a href="#generic-credentials" id="generic-credentials"></a>

用于 n8n 尚未支持的集成。需要手动配置身份验证流程，包括 API 端点、必要参数及认证方法。

可以选择以下方法之一：

* Basic auth（Basic 认证）
* Custom auth（自定义认证）
* Digest auth（摘要认证）
* Header auth（请求头认证）
* OAuth1 API
* OAuth2 API
* Query auth（查询参数认证）
* Simplified Custom Auth（简化的自定义认证）

有关各凭据类型的设置，请参阅 [HTTP Request 凭据](../../credentials/httprequest.md)。

### Send Query Parameters（发送查询参数） <a href="#send-query-parameters" id="send-query-parameters"></a>

查询参数可用于筛选 HTTP 请求的数据。如果所用 API 支持查询参数，且请求需要筛选条件，开启此选项。

通过以下方式之一**指定查询参数**：

* **Using Fields Below**（使用下方字段）：在 **Query Parameters**（查询参数）中输入 **Name**（名称）/**Value**（值）对。选择 **Add Parameter**（添加参数）可添加更多参数。名称是要筛选的字段名，值是筛选值。
* **Using JSON**（使用 JSON）：输入 **JSON** 来定义查询参数。

有关详细用法，请参阅所用服务的 API 文档。

### Send Headers（发送请求头） <a href="#send-headers" id="send-headers"></a>

使用此参数在请求中发送请求头。请求头包含请求的元数据或上下文信息。

通过以下方式之一设置 **Specify Headers**（指定请求头）：

* **Using Fields Below**（使用下方字段）：在 **Header Parameters**（请求头参数）中输入 **Name**（名称）/**Value**（值）对。选择 **Add Parameter**（添加参数）可添加更多请求头。名称是要设置的请求头，值是要传递的请求头值。
* **Using JSON**（使用 JSON）：输入 **JSON** 来定义请求头参数。

有关详细用法，请参阅所用服务的 API 文档。

### Send Body（发送请求体） <a href="#send-body" id="send-body"></a>

如果 API 请求需要发送请求体，开启此选项。

然后选择最符合待发送内容格式的 **Body Content Type**（请求体内容类型）。


#### Form URLencoded（URL 编码表单） <a href="#form-urlencoded" id="form-urlencoded"></a>


使用此选项，将请求体按 `application/x-www-form-urlencoded` 格式发送。

通过以下方式之一设置 **Specify Body**（指定请求体）：

* **Using Fields Below**（使用下方字段）：在 **Body Parameters**（请求体参数）中输入 **Name**（名称）/**Value**（值）对。选择 **Add Parameter**（添加参数）可添加更多参数。名称应为表单字段名，值为要为该字段设置的内容。
* **Using Single Field**（使用单个字段）：在一个 **Body**（请求体）参数中，按 `fieldname1=value1&fieldname2=value2` 格式输入名称／值对。

有关详细用法，请参阅所用服务的 API 文档。

#### Form-Data（表单数据） <a href="#form-data" id="form-data"></a>

使用此选项，将请求体按 `multipart/form-data` 格式发送。

配置 **Body Parameters**（请求体参数）时，选择 **Parameter Type**（参数类型）：

* 选择 **Form Data**（表单数据），输入 **Name**（名称）/**Value**（值）对。
* 选择 **n8n Binary File**（n8n 二进制文件），从节点可访问的文件中读取请求体数据。
    * **Name**（名称）：输入要设置的字段 ID。
    * **Input Data Field Name**（输入数据字段名称）：输入包含待处理二进制文件数据的输入字段名称。

选择 **Add Parameter**（添加参数）可输入更多参数。

有关详细用法，请参阅所用服务的 API 文档。

#### JSON <a href="#json" id="json"></a>

使用此选项，将请求体按 JSON 格式发送。

通过以下方式之一设置 **Specify Body**（指定请求体）：

* **Using Fields Below**（使用下方字段）：在 **Body Parameters**（请求体参数）中输入 **Name**（名称）/**Value**（值）对。选择 **Add Parameter**（添加参数）可添加更多参数。
* **Using JSON**（使用 JSON）：输入 **JSON** 来定义请求体。

有关详细用法，请参阅所用服务的 API 文档。

#### n8n Binary File（n8n 二进制文件） <a href="#n8n-binary-file" id="n8n-binary-file"></a>

使用此选项，将 n8n 中保存的文件内容作为整个请求体发送。

在 **Input Data Field Name**（输入数据字段名称）中，填写包含该文件的输入字段名称。

有关文件格式要求，请参阅所用服务的 API 文档。

#### Raw（原始数据） <a href="#raw" id="raw"></a>

使用此选项，在请求体中发送原始数据。

* **Content Type**（内容类型）：输入用于原始请求体的 `Content-Type` 请求头值。完整的 MIME 内容类型列表，请参阅 IANA [媒体类型](https://www.iana.org/assignments/media-types/media-types.xhtml)文档。
* **Body**（请求体）：输入要发送的原始请求体内容。

有关详细用法，请参阅所用服务的 API 文档。

## 节点选项 <a href="#node-options" id="node-options"></a>

选择 **Add Option**（添加选项）查看并选择下列选项。除非另有说明，所有参数配置均可使用这些选项。

### Array Format in Query Parameters（查询参数中的数组格式） <a href="#array-format-in-query-parameters" id="array-format-in-query-parameters"></a>

{% hint style="info" %}
**选项可用性**

仅在开启 **Send Query Parameters**（发送查询参数）时可用。
{% endhint %}

使用此选项控制查询参数中数组的格式，可选：

* **No Brackets**（无括号）：为数组中每个数据项生成名称=值形式，例如 `foo=bar&foo=qux`。
* **Brackets Only**（仅括号）：在每个数组名称后添加方括号，例如 `foo[]=bar&foo[]=qux`。
* **Brackets with Indices**（带索引括号）：在每个数组名称后添加包含索引值的方括号，例如 `foo[0]=bar&foo[1]=qux`。

选择哪种格式，请参阅所用服务的 API 文档。

### Batching（批量处理） <a href="#batching" id="batching"></a>

控制如何分批处理大量输入数据项：

* **Items per Batch**（每批数据项数量）：输入每批包含的输入数据项数量。
* **Batch Interval**（批次间隔）：输入每批请求之间的等待时间，单位为毫秒。设为 0 表示不等待。

### Ignore SSL Issues（忽略 SSL 问题） <a href="#ignore-ssl-issues" id="ignore-ssl-issues"></a>

默认情况下，只有 SSL 证书验证成功，n8n 才会下载响应。如果希望证书验证失败时仍下载响应，开启此选项。

### Lowercase Headers（请求头名称转为小写） <a href="#lowercase-headers" id="lowercase-headers"></a>

开启时将请求头名称转为小写（默认），关闭时保留原样。

### Redirects（重定向） <a href="#redirects" id="redirects"></a>

选择是否跟随重定向：默认开启，关闭时不跟随。开启后，在 **Max Redirects**（最大重定向次数）中输入允许跟随的次数上限。

### Response（响应） <a href="#response" id="response"></a>

使用此选项配置预期 API 响应的细节，包括：

* **Include Response Headers and Status**（包含响应头和状态）：默认仅返回响应体。开启后，除响应体外，还返回完整响应，包括响应头和响应状态码。
* **Never Error**（不因状态码报错）：默认仅当响应状态码为 2xx 时，节点才将请求视为成功。开启后，无论返回何种状态码，都将其视为成功。
* **Response Format**（响应格式）：选择返回数据的格式，可选：
    * **Autodetect**（自动检测，默认）：根据返回数据自动检测并设置响应格式。
    * **File**（文件）：将响应存入文件，并在 **Put Output in Field**（输出字段）中填写用于返回该文件的字段名称。
    * **JSON**：将响应按 JSON 格式返回。
    * **Text**（文本）：将响应按纯文本格式返回，并在 **Put Output in Field**（输出字段）中填写用于返回该文本的字段名称。

### Pagination（分页） <a href="#pagination" id="pagination"></a>

使用此选项分页获取结果，适用于 API 无法在一次调用中返回全部数据的较大查询结果。

{% hint style="info" %}
**先查看 API 数据**

部分分页选项需要了解 API 返回的数据。配置分页前，请先查看 API 文档，或执行不分页的 API 调用，了解响应结构。
{% endhint %}
<details>

<summary>了解分页</summary>

分页是将大量数据拆分为多页，每页数据量取决于所设置的数量限制。

例如，调用名为 `/users` 的端点，API 需要返回 300 个用户的信息，但数据过多，无法一次响应全部返回。

如果 API 支持分页，可以逐批获取数据：调用 `/users`，同时设置每页数量，以及页码或页面 URL。例如，每页限制 10 个用户，从第 0 页开始。API 首先返回前 10 个用户。然后再次调用 API，将页码增加 1，即可获取后续 10 个结果。

</details>

配置分页设置：

* **Pagination Mode**（分页模式）：
    * **Off**（关闭）：关闭分页。
    * **Update a Parameter in Each Request**（每次请求更新参数）：需要为每次请求动态设置参数时使用。
    * **Response Contains Next URL**（响应包含下一页 URL）：API 响应中包含下一页 URL 时使用。通过表达式设置 **Next URL**（下一页 URL）。

配置示例请参阅 [HTTP Request 节点使用指南 | 分页](../../../../build/code-in-n8n/cookbook/http-request-node/pagination.md)。

使用分页时，n8n 提供了用于处理 HTTP 节点请求和响应的内置变量：

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/http/pagination-variables.md" %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/http/pagination-api-differences.md" %}

### Proxy（代理） <a href="#proxy" id="proxy"></a>

需要指定 HTTP 代理时，使用此选项。

输入请求要使用的 **Proxy**（代理）。此设置优先于通过 [`HTTP_PROXY`、`HTTPS_PROXY` 或 `ALL_PROXY` 环境变量](../../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment.md)定义的全局配置。

### Timeout（超时） <a href="#timeout" id="timeout"></a>

设置节点等待服务器发送响应头并开始返回响应体的最长时间。初始响应等待超过此值时，节点会中止请求。

输入 **Timeout**（超时）的等待时间，单位为毫秒。

## 仅工具模式可用的选项 <a href="#tool-only-options" id="tool-only-options"></a>

以下选项仅在连接到 [AI 智能体](../../cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md)并作为[工具](../../../../build/integrate-ai/understand-ai-components/how-tools-work.md){ data-preview }使用时可用。

### Optimize Response（优化响应） <a href="#optimize-response" id="optimize-response"></a>

选择是否优化工具响应，以减少传给大语言模型的数据量。优化可能降低成本，也有助于模型忽略不重要的细节，从而改善结果。

优化响应时，需要选择预期的响应类型，它决定后续可配置的选项。支持的响应类型包括：

#### JSON <a href="#json" id="json"></a>

预期为 **JSON** 响应时，可通过以下选项选择响应中使用哪些 JSON 数据：

* **Field Containing Data**（数据所在字段）：指定包含所需数据的 JSON 对象部分。留空时使用完整响应。
* **Include Fields**（包含字段）：选择响应对象中包含哪些字段，共有三种方式：
    * **All**（全部）：包含响应对象中的所有字段。
    * **Selected**（指定字段）：仅包含下方指定的字段。
        * **Fields**（字段）：以逗号分隔的待包含字段列表。可用点表示法指定嵌套字段，也可从 Input（输入）面板拖入字段。
    * **Exclude**（排除）：包含所有字段，*但排除*下方指定字段。
        * **Fields**（字段）：以逗号分隔的待排除字段列表。可用点表示法指定嵌套字段，也可从 Input（输入）面板拖入字段。

#### HTML <a href="#html" id="html"></a>

预期为 **HTML** 时，可指定文档中与模型有关的部分，并使用以下选项优化响应：

* **Selector (CSS)**（CSS 选择器）：指定响应 HTML 中要包含的元素或元素类型，默认使用 `body` 元素。
* **Return Only Content**（仅返回内容）：选择是否移除响应中的 HTML 标签和属性，仅保留实际内容。这可减少 token 用量，也可能便于模型理解。
    * **Elements To Omit**（忽略元素）：提取内容时需要排除的 CSS 选择器列表，以逗号分隔。
* **Truncate Response**（截断响应）：选择是否限制响应大小，以节省 token。
    * **Max Response Characters**（最大响应字符数）：HTML 响应中最多包含的字符数，默认值为 1000。

#### Text（文本） <a href="#text" id="text"></a>

预期为一般的 **Text**（文本）响应时，可使用以下选项优化结果：

* **Truncate Response**（截断响应）：选择是否限制响应大小，以节省 token。
    * **Max Response Characters**（最大响应字符数）：文本响应中最多包含的字符数，默认值为 1000。

## 导入 curl 命令 <a href="#import-curl-command" id="import-curl-command"></a>

[curl](https://curl.se/) 是一个通过 URL 传输数据的命令行工具和库。

可以使用 curl 调用 REST API。如果所用服务的 API 文档提供 curl 示例，可将其复制到 n8n，用于配置 HTTP Request 节点。

导入 curl 命令：

{% hint style="info" %}
**导入格式**

导入时，所有参数值都会成为字符串。要保留数字和布尔值原有的数据类型，请将 **Using Fields Below**（使用下方字段）切换为 **Using JSON**（使用 JSON），并粘贴包含参数的 JSON 对象。
{% endhint %}

1. 在 HTTP Request 节点的 **Parameters**（参数）标签页中，选择 **Import cURL**（导入 cURL）。此时打开 **Import cURL command**（导入 cURL 命令）对话框。
2. 将 curl 命令粘贴到文本框中。
3. 选择 **Import**（导入）。n8n 会将请求配置载入节点字段，并覆盖现有配置。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 HTTP Request 集成模板](https://n8n.io/integrations/http-request)，或[搜索所有模板](https://n8n.io/workflows/)

## 常见问答 <a id="faq"></a>

### 如何在不编写代码的情况下调用 API？ <a id="how-do-i-call-an-api-without-writing-code"></a>

使用 HTTP Request 节点，查询任意提供 REST API 的应用或服务中的数据。可以设置[节点参数](#node-parameters)，包括方法、URL、查询参数、请求头和请求体；也可以从服务 API 文档中[导入 curl 命令](#import-curl-command)，由 n8n 填充字段。

### 如何对 API 请求进行身份验证？ <a id="how-do-i-authenticate-an-api-request"></a>

在 [Authentication](#authentication)（身份验证）部分设置。n8n 支持该服务时，优先使用更易配置的 **Predefined Credential Type**（预定义凭据类型）。其他 API 可使用通用凭据，支持 Basic auth、Header auth、OAuth1、OAuth2 等。请参阅 [HTTP Request 凭据](../../credentials/httprequest.md)。

### 如何处理分多页返回结果的 API？ <a id="how-do-i-handle-an-api-that-returns-results-across-many-pages"></a>

开启 [Pagination](#pagination)（分页）选项，并设置 **Pagination Mode**（分页模式）：每次请求更新参数，或跟随响应中的下一页 URL，让 n8n 获取所有页面，而不只是第一页。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见疑问或问题及建议的解决方法，请参阅[常见问题](common-issues.md)。
