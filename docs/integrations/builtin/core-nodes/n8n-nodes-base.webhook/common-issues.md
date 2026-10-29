---
title: Webhook 节点常见问题
contentType:
- integration
- reference
priority: critical
nodeTitle: Webhook 节点常见问题
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.webhook/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/common-issues
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/common-issues
description: 了解 n8n 中 Webhook 节点的常见问题及建议的解决方法。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 常见问题 <a id="common-issues"></a>

以下是 [Webhook 节点](./README.md)的常见疑问、问题及建议的解决方法。

## 监听多种 HTTP 方法 <a href="#listen-for-multiple-http-methods" id="listen-for-multiple-http-methods"></a>

Webhook 节点默认只接受一种方法的调用。例如，可以接受 GET 或 POST 请求，但不能同时接受两者。要接受多种方法的调用：

1. 打开节点的 **Settings**（设置）。
2. 开启 **Allow Multiple HTTP Methods**（允许多种 HTTP 方法）。
3. 返回 **Parameters**（参数）。此时节点默认接受 GET 和 POST 调用，可在 **HTTP Methods**（HTTP 方法）字段中添加其他方法。

Webhook 节点会为每种方法提供一个输出，因此可以根据请求方法执行不同操作。

## 使用 HTTP Request 节点触发 Webhook 节点 <a href="#use-the-http-request-node-to-trigger-the-webhook-node" id="use-the-http-request-node-to-trigger-the-webhook-node"></a>

[HTTP Request](../n8n-nodes-base.httprequest/README.md) 节点向指定的 URL 发送 HTTP 请求。

1. 创建一个新工作流。
2. 将 HTTP Request 节点添加到工作流。
3. 从 **Request Method**（请求方法）下拉列表中选择方法。例如，如果 Webhook 节点的 **HTTP method** 为 GET，则在 HTTP Request 节点中也选择 GET。
4. 复制 Webhook 节点中的 URL，粘贴到 HTTP Request 节点的 **URL** 字段。
5. 如果使用 webhook 测试 URL，先执行包含 Webhook 节点的工作流。
6. 执行 HTTP Request 节点。

## 使用 curl 触发 Webhook 节点 <a href="#use-curl-to-trigger-the-webhook-node" id="use-curl-to-trigger-the-webhook-node"></a>

可以使用 [curl](https://curl.se/) 发送 HTTP 请求，触发 Webhook 节点。

{% hint style="info" %}
在示例中，将 `<https://your-n8n.url/webhook/path>` 替换为你的 webhook URL。\
以下示例分别使用 GET 或 POST 请求，请确保所用方法与 **HTTP Method**（HTTP 方法）的设置一致。
{% endhint %}

发送不带任何参数的 HTTP 请求：

```sh
curl --request GET <https://your-n8n.url/webhook/path>
```

发送带请求体参数的 HTTP 请求：

```sh
curl --request POST <https://your-n8n.url/webhook/path> --data 'key=value'
```

发送带请求头参数的 HTTP 请求。原文下方示例的请求头写作 key=value；实际传递请求头时，应使用 key: value 格式。此处保留原始命令，供对照：

```sh
curl --request GET <https://your-n8n.url/webhook/path> --header 'key=value'
```

发送文件的 HTTP 请求：

```sh
curl --request POST <https://your-n8n.url/webhook/path> --form 'key=@/path/to/file'
```

将 `/path/to/file` 替换为要发送的文件路径。

## 发送字符串类型的响应 <a href="#send-a-response-of-type-string" id="send-a-response-of-type-string"></a>

默认响应格式为 JSON 或数组。要发送字符串类型的响应：

1. 选择 **Response Mode**（响应模式）> **When Last Node Finishes**（最后一个节点完成时）。
2. 选择 **Response Data**（响应数据）> **First Entry JSON**（首个数据项的 JSON）。
3. 选择 **Add Option**（添加选项）> **Property Name**（属性名称）。
4. 输入包含响应的属性名称，默认为 `data`。
5. 将一个 [Edit Fields 节点](../n8n-nodes-base.set.md)连接到 Webhook 节点。
6. 在 Edit Fields 节点中，选择 **Add Value**（添加值）> **String**（字符串）。
7. 在 **Name**（名称）字段中输入属性名称，应与第 4 步的属性名称一致。
8. 在 **Value**（值）字段中输入字符串值。
9. 开启 **Keep Only Set**（仅保留已设置字段），开关显示为绿色。

调用 Webhook 时，它会发送来自 Edit Fields 节点的字符串响应。

## Test URL 与 Production URL 的区别 <a href="#test-url-versus-production-url" id="test-url-versus-production-url"></a>

n8n 为每个 Webhook 节点生成两个 **Webhook URLs**（Webhook URL）：**Test URL**（测试 URL）和 **Production URL**（生产 URL）。

构建或测试工作流时使用 **Test URL**。准备将 Webhook URL 用于生产环境时，使用 **Production URL**。

| **URL 类型** | **触发方式** | **监听时长** | **数据是否显示在编辑器界面？** |
| -------------- | -------------------------------------------------------------------------- | ----------------------------- | :--------------------------: |
| Test URL（测试 URL） | 选择 **Listen for test event**（监听测试事件），并在来源端触发测试事件。 | 120 秒 | ✅ |
| Production URL（生产 URL） | 发布工作流 | 持续监听，直到取消发布工作流 | ❌ |

更多信息，请参阅[工作流开发](workflow-development.md)。

## 允许列表中的 IP 地址无法连接 <a href="#ip-addresses-in-whitelist-are-failing-to-connect" id="ip-addresses-in-whitelist-are-failing-to-connect"></a>

如果 IP 允许列表中的地址无法连接，请检查 n8n 是否运行在反向代理之后。

如果是，将 `N8N_PROXY_HOPS` [环境变量](../../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/README.md)设为 n8n 前方反向代理的层数。

## 每个路径与方法组合只能注册一个 webhook <a href="#only-one-webhook-per-path-and-method" id="only-one-webhook-per-path-and-method"></a>

n8n 对每个路径与 HTTP 方法组合只允许注册一个 webhook，例如对 `GET` 请求和 `/my-request` 路径的组合。这样可以避免无法确定由哪个 webhook 接收请求。

如果收到提示，表示所选路径与方法已被占用，可以：

* 取消发布包含冲突 webhook 的工作流。
* 更改其中一个冲突 webhook 的路径和／或方法。

## n8n Cloud 上的超时 <a href="#timeouts-on-n8n-cloud" id="timeouts-on-n8n-cloud"></a>

n8n Cloud 使用 Cloudflare 防护恶意流量。如果 webhook 在 100 秒内没有响应，传入请求会失败，并返回 [524 状态码](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/)。

因此，对于可能超过此限制的长时间运行任务，可能需要配置两个独立的 webhook 来实现轮询：

* 第一个 webhook 启动长时间运行的任务，并立即响应。
* 第二个 webhook 供调用方定期查询任务状态，并在任务完成后获取结果。
