---
title: HTTP Request 节点常见问题
description: 了解 n8n 工作流自动化平台中 HTTP Request 节点的常见问题，包括问题详情和建议的解决方法。
contentType:
- integration
- reference
priority: critical
nodeTitle: HTTP Request 节点常见问题
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.httprequest/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/common-issues
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/common-issues
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# HTTP Request 节点常见问题 <a href="#http-request-node-common-issues" id="http-request-node-common-issues"></a>

本页介绍 [HTTP Request 节点](README.md)的一些常见错误和问题，以及解决或排查步骤。

## Bad request - please check your parameters（请求无效，请检查参数） <a href="#bad-request-please-check-your-parameters" id="bad-request-please-check-your-parameters"></a>

节点收到表示请求无效的 400 错误时，会显示此错误。常见原因包括：

* **Query Parameter**（查询参数）的名称或值无效。
* **Query Parameter**（查询参数）中传入数组，但数组格式不正确。可尝试使用 [**Array Format in Query Parameters**](README.md#array-format-in-query-parameters)（查询参数中的数组格式）选项。

请查看服务的 API 文档，按要求设置查询参数格式。


## The resource you are requesting could not be found（找不到请求的资源） <a href="#the-resource-you-are-requesting-could-not-be-found" id="the-resource-you-are-requesting-could-not-be-found"></a>


输入的端点 **URL** 无效时，会显示此错误。

可能是 URL 拼写错误，或 API 已弃用。请参阅服务 API 文档，确认端点有效。


## Connection refused (ECONNREFUSED)（连接被拒绝） <a href="#connection-refused-econnrefused" id="connection-refused-econnrefused"></a>


节点连接网络中的目标主机，但目标端口没有服务监听、TCP 连接被主动拒绝时，会出现此错误。这与 DNS 失败、超时或防火墙静默丢包不同。

在自托管 n8n 中，最常见的原因是 Docker 网络配置。在 n8n 容器内，`localhost` 和 `127.0.0.1` 都指向容器自身，而不是宿主机。从节点请求 `http://localhost:5000` 时，实际访问的是 n8n 容器的 5000 端口，该端口没有服务监听。

要解决此问题，请使用容器能够路由到的目标名称：

* **目标在宿主机，使用 Mac 或 Windows 上的 Docker Desktop**：在 **URL** 字段中使用 `http://host.docker.internal:<port>`。Docker Desktop 会自动添加此主机名。
* **目标在 Linux 宿主机**：为容器传入 `--add-host=host.docker.internal:host-gateway`，或使用 `extra_hosts` 在 `docker-compose.yml` 中配置：
    ```yaml
    services:
      n8n:
        image: n8nio/n8n
        extra_hosts:
          - "host.docker.internal:host-gateway"
    ```
    [MySQL 节点](../../app-nodes/n8n-nodes-base.mysql/common-issues.md#cant-connect-to-a-local-mysql-server-when-using-docker)文档也介绍了同一解决方法。
* **目标在同一 Compose 项目的另一个容器中**：使用服务名称作为主机名，例如 `http://my-api:5000`。使用容器内部端口，而不是对外发布的 `ports:` 映射。

Node.js 17 及更高版本还可能出现另一种情况，即使没有使用 Docker：`localhost` 优先解析为 IPv6 地址 `::1`，而不是 `127.0.0.1`。如果目标仅监听 `127.0.0.1`，IPv6 连接会被拒绝，而 HTTP Request 节点内的 IPv4 回退并不总能成功。

在 **URL** 字段中使用 `http://127.0.0.1:<port>`，代替 `localhost`。

重新执行工作流前，可进入 n8n 容器，用 `wget` 请求该 URL 以检查修复结果：

```sh
docker exec -it n8n wget -qO- http://host.docker.internal:5000/health
```

如果容器内的 `wget` 请求成功，说明该测试请求可连通；还需核对 HTTP Request 节点的请求配置，不能直接保证节点也会成功。若 `wget` 也返回“connection refused”，则原因在网络或目标服务，而不在 n8n。

在 n8n Cloud 中，工作流运行在 n8n 的基础设施上。这里的 `localhost` 不是你的电脑，也没有直接访问你电脑上服务的路径。对于仅本机可访问的服务，可通过隧道公开，再在 HTTP Request 节点中使用公共 URL。

## JSON parameter need to be an valid JSON（JSON 参数必须是有效 JSON） <a href="#json-parameter-need-to-be-an-valid-json" id="json-parameter-need-to-be-an-valid-json"></a>

将参数作为 JSON 传入，但内容不是有效 JSON 时，会显示此错误。

要解决此问题，请检查输入 JSON 是否存在以下问题：

* 使用 JSON 校验器或语法解析器，检查缺少引号、逗号过多或缺失、数组格式错误、方括号或花括号过多或缺失等问题。
* 如果节点中使用了 **Expression**（表达式），请用双层花括号包住整个 JSON，例如：
    ```
    {{
        {
        "myjson":
        {
            "name1": "value1",
            "name2": "value2",
            "array1":
                ["value1","value2"]
        }
        }
    }}
    ```

## Forbidden - perhaps check your credentials（禁止访问，请检查凭据） <a href="#forbidden-perhaps-check-your-credentials" id="forbidden-perhaps-check-your-credentials"></a>

节点收到表示服务器拒绝执行请求的 403 错误时，会显示此错误。译注：403 并不一定表示身份验证失败，也可能是权限或其他拒绝访问的原因。

请检查所选凭据，确认能够通过身份验证。可能需要：

* 更新权限或作用域，让 API 密钥或账户可以执行所选操作。
* 调整通用凭据的格式。
* 生成具有适当权限或作用域的新 API 密钥或令牌。

## 429 - 服务收到的请求过多 <a href="#429-the-service-is-receiving-too-many-requests-from-you" id="429-the-service-is-receiving-too-many-requests-from-you"></a>

节点从调用的服务收到 [429 错误](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429)时，会显示此错误，通常表示达到服务的速率限制。更多信息，请参阅[处理 API 速率限制](../../handle-rate-limits.md)。

可使用 HTTP Request 节点内置的以下选项处理此错误：

### Batching（批量处理） <a href="#batching" id="batching"></a>

使用此选项分批发送请求，并在批次之间添加延迟。

1. 在 HTTP Request 节点中，选择 **Add Option > Batching**（添加选项 > 批量处理）。
1. 将 **Items per Batch**（每批数据项数量）设为每批包含的输入数据项数量。
1. 设置 **Batch Interval (ms)**（批次间隔，毫秒），在请求批次之间添加等待。例如，要每秒向 API 发送一个请求，将 **Batch Interval (ms)** 设为 `1000`。

### Retry on Fail（失败时重试） <a href="#retry-on-fail" id="retry-on-fail"></a>

使用此选项，在一次尝试失败后重新尝试执行节点。

1. 在 HTTP Request 节点的 **Settings**（设置）中，开启 **Retry on Fail**（失败时重试）。
1. 将 **Max Tries**（最大尝试次数）设为 n8n 尝试执行节点的次数上限。
1. 将 **Wait Between Tries (ms)**（尝试间隔，毫秒）设为重试之间的等待时间。例如，要等待一秒再重试请求，将 **Wait Between Tries (ms)** 设为 `1000`。

## 上传的文件名称不正确 <a href="#your-uploaded-file-arrives-with-the-wrong-file-name" id="your-uploaded-file-arrives-with-the-wrong-file-name"></a>

使用 **Body Content Type**（请求体内容类型）的 **Form-Data** 模式上传文件时，n8n 从二进制数据中读取 `multipart/form-data` 部分的文件名，而不是读取 **Name** 字段。**Name** 只设置表单字段名称。二进制数据未提供文件名时，n8n 使用 `file`。

当接收 API 按文件名而不是表单字段名识别上传内容，或要求特定名称或扩展名时，这一区别很重要。请求虽已到达，API 仍可能拒绝，通常返回表示文件缺失的 400 错误。例如，[Convert to File 节点](../n8n-nodes-base.converttofile.md)的 **Convert to Text File** 操作默认将输出命名为 `file.txt`，要求 `index.html` 的 API 就无法找到预期文件。

要解决此问题，请在 HTTP Request 节点之前设置二进制数据的文件名：

* 在 Convert to File 节点中，将 **File Name**（文件名称）设为 API 所要求的名称。
* 在 [Code 节点](../n8n-nodes-base.code/README.md)中，设置二进制属性的文件名：

```javascript
for (const item of $input.all()) {
	item.binary.data.fileName = 'index.html';
}
return $input.all();
```

n8n 会将二进制数据中存放的 MIME 类型复制到该部分的 `Content-Type`，因此，如果 API 检查 MIME 类型，也需要设置它。

## 发送文件时出现 Unsupported media type (415)（不支持的媒体类型） <a href="#unsupported-media-type-415-when-you-send-a-file" id="unsupported-media-type-415-when-you-send-a-file"></a>

API 要求 `multipart/form-data`，而请求体不是 multipart 格式时，会显示此错误。

**Body Content Type > n8n Binary File**（请求体内容类型 > n8n 二进制文件）将文件作为整个请求体发送。n8n 将 `Content-Type` 设置为二进制数据中的 MIME 类型；未提供时，使用 `application/octet-stream`。此模式不会添加 multipart 封装或 boundary，因此仅接受 multipart 上传的 API 会拒绝请求。

要将同一文件作为 multipart 表单上传，请执行以下设置：

1. 将 **Body Content Type**（请求体内容类型）设为 **Form-Data**。
1. 添加一个 **Body Parameters**（请求体参数）条目，将其 **Type**（类型）设为 **n8n Binary File**。
1. 将 **Name** 设为 API 文档规定的表单字段名称。
1. 将 **Input Data Field Name**（输入数据字段名称）设为包含文件的二进制属性，例如 `data`。
