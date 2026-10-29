---
title: Respond to Webhook 节点
contentType:
- integration
- reference
priority: critical
nodeTitle: Respond to Webhook 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook
description: 了解 n8n 中 Respond to Webhook 节点的用法，并查看相关示例。
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


# Respond to Webhook 节点 <a id="respond-to-webhook"></a>

使用 Respond to Webhook 节点控制传入 webhook 的响应。此节点与 [Webhook](n8n-nodes-base.webhook/README.md) 节点配合使用。

{% hint style="info" %}
**使用首个数据项运行一次**

Respond to Webhook 节点使用传入的首个数据项运行一次。更多信息，请参阅[返回多个数据项](n8n-nodes-base.respondtowebhook.md#return-more-than-one-data-item-deprecated)。
{% endhint %}

## 如何使用 Respond to Webhook <a href="#how-to-use-respond-to-webhook" id="how-to-use-respond-to-webhook"></a>

使用 Respond to Webhook 节点的步骤：

1. 将 [Webhook](n8n-nodes-base.webhook/README.md) 节点添加为工作流的触发器节点。
2. 在 Webhook 节点中，将 **Respond**（响应方式）设为 **Using 'Respond to Webhook' node**（使用 Respond to Webhook 节点）。
3. 将 Respond to Webhook 节点添加到工作流中的任意位置。如果要返回其他节点的数据，请将其放在这些节点之后。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用这些参数配置节点行为。

### Respond With（响应内容） <a href="#respond-with" id="respond-with"></a>

选择 webhook 响应中要发送的数据。

* **All Incoming Items**（所有输入数据项）：返回输入中的所有 JSON 数据项。
* **Binary File**（二进制文件）：返回 **Response Data Source**（响应数据来源）中指定的二进制文件。
* **First Incoming Item**（首个输入数据项）：返回首个输入数据项的 JSON 数据。
* **JSON**：返回 **Response Body**（响应体）中定义的 JSON 对象。
* **JWT Token**（JWT 令牌）：返回 JSON Web Token（JWT）。
* **No Data**（无数据）：不返回响应载荷。
* **Redirect**（重定向）：重定向到 **Redirect URL**（重定向 URL）中设置的地址。
* **Text**（文本）：返回 **Response Body**（响应体）中设置的文本。默认以 HTML 格式发送（`Content-Type: text/html`）。

## 节点选项 <a href="#node-options" id="node-options"></a>

选择 **Add Option**（添加选项）查看并设置选项。

* **Response Code**（响应码）：设置要使用的[响应码](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)。
* **Response Headers**（响应头）：定义要发送的响应头。
* **Put Response in Field**（将响应放入字段）：仅当响应内容为 **All Incoming Items**（所有输入数据项）或 **First Incoming Item**（首个输入数据项）时可用。设置用于存放响应数据的字段名称。
* **Enable Streaming**（启用流式传输）：开启时，以流式方式向用户返回数据。要求触发器的 **Response mode**（响应模式）配置为 **Streaming**（流式传输）。

## n8n 如何保护 HTML 响应 <a href="#how-n8n-secures-html-responses" id="how-n8n-secures-html-responses"></a>

{% hint style="info" %}
**功能可用性**

将 webhook 的 HTML 响应自动包装在 `<iframe>` 标签中的功能，自 n8n 1.103.0 起提供。
{% endhint %}

从 n8n 1.103.0 起，n8n 会自动将 webhook 的 HTML 响应包装在 `<iframe>` 标签中，以保护实例用户。

这会产生以下影响：

* HTML 在沙盒 iframe 中呈现，而不是直接在父文档中呈现。
* 尝试访问顶层窗口或本地存储的 JavaScript 代码会失败。
* 沙盒 iframe 中无法使用身份验证请求头，例如 Basic 认证。需要采用其他方式，例如在 HTML 中嵌入短期有效的访问令牌。
* 相对 URL（例如 `<form action="/">`）无法使用，请改用绝对 URL。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Respond to Webhook 集成模板](https://n8n.io/integrations/respond-to-webhook)，或[搜索所有模板](https://n8n.io/workflows/)

## 工作流行为 <a href="#workflow-behavior" id="workflow-behavior"></a>

使用 Respond to Webhook 节点时，工作流遵循以下规则：

* 工作流结束时未执行 Respond to Webhook 节点：返回标准消息，状态码为 200。
* 在首个 Respond to Webhook 节点执行前，工作流发生错误：返回错误消息，状态码为 500。
* 首个 Respond to Webhook 节点执行后，又执行第二个同类节点：工作流会忽略第二个节点。
* 执行 Respond to Webhook 节点时，没有对应的 webhook：工作流会忽略此节点。

## 输出发送给 webhook 的响应 <a href="#output-the-response-sent-to-the-webhook" id="output-the-response-sent-to-the-webhook"></a>

默认情况下，Respond to Webhook 节点只有一个输出分支，其中包含节点的输入数据。

可以按需启用第二个输出分支，其中包含发送给 webhook 的响应。在画布上打开 Respond to Webhook 节点，选择 **Settings**（设置）标签页，然后开启 **Enable Response Output Branch**（启用响应输出分支）。

此时节点有两个输出：

* **Input Data**（输入数据）：原有输出，继续传递节点的输入数据。
* **Response**（响应）：发送给 webhook 的响应对象。

## 返回多个数据项（已弃用） <a href="#return-more-than-one-data-item-deprecated" id="return-more-than-one-data-item-deprecated"></a>

{% hint style="warning" %}
**功能可用性**

从 n8n 1.22.0 起，本节中用于返回多个数据项的变通方法已弃用。后续版本增加了 **All Incoming Items**（所有输入数据项）选项，可直接返回所有数据项。
{% endhint %}

Respond to Webhook 节点使用传入的首个数据项运行一次，使用[表达式](../../../build/work-with-data/expressions-versus-data-nodes.md)时也如此。无法通过 Loop 节点强制循环响应：工作流会运行，但 webhook 响应仍只包含第一次执行的结果。

如果需要返回多个数据项，可以选择以下方式之一：

* 使用 Webhook 节点的 **When Last Node Finishes**（最后一个节点完成时）选项来设置 **Respond**（响应方式），替代 Respond to Webhook 节点。需要返回工作流最终输出的数据时，可采用此方式。
* 使用 [Aggregate](n8n-nodes-base.aggregate.md) 节点将多个数据项合并为一个，再传给 Respond to Webhook 节点。将 **Aggregate**（聚合方式）设为 **All Item Data (Into a Single List)**（所有数据项数据，放入单个列表）。
