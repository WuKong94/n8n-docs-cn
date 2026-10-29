---
title: Wait 节点
contentType:
- integration
- reference
priority: critical
nodeTitle: Wait 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.wait.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait
description: 了解 n8n 中 Wait 节点的用法，并查看相关示例。
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


# Wait 节点 <a id="wait"></a>

使用 Wait 节点暂停工作流执行。暂停时，执行数据通常会卸载到数据库，满足恢复条件后重新加载数据并继续执行。短于 65 秒的等待有例外，详见本页关于时间操作的说明。

## 操作 <a href="#operations" id="operations"></a>

Wait 节点可以在以下条件下 **Resume**（恢复执行）：

* [**After Time Interval**](n8n-nodes-base.wait.md#after-time-interval)（经过时间间隔后）：等待指定时长。
* [**At Specified Time**](n8n-nodes-base.wait.md#at-specified-time)（在指定时间）：等待到某个特定时间。
* [**On Webhook Call**](n8n-nodes-base.wait.md#on-webhook-call)（收到 Webhook 调用时）：等待收到 HTTP 调用。
* [**On Form Submitted**](n8n-nodes-base.wait.md#on-form-submitted)（表单提交时）：等待收到表单提交。

详细操作说明见下文各节。

### After Time Interval（经过时间间隔后） <a href="#after-time-interval" id="after-time-interval"></a>

等待指定时长。

此参数还包含两个字段：

* **Wait Amount**（等待时长）：输入要等待的时间量。
* **Wait Unit**（等待单位）：选择 **Wait Amount**（等待时长）的计量单位，可选：
  * **Seconds**（秒）
  * **Minutes**（分钟）
  * **Hours**（小时）
  * **Days**（天）

关于时间间隔的工作方式及所用时区，请参阅[基于时间的操作](n8n-nodes-base.wait.md#time-based-operations)。

### At Specified Time（在指定时间） <a href="#at-specified-time" id="at-specified-time"></a>

等待到指定日期和时间后继续执行。使用日期与时间选择器设置 **Date and Time**（日期和时间）。

关于所用时区，请参阅[基于时间的操作](n8n-nodes-base.wait.md#time-based-operations)。

### On Webhook Call（收到 Webhook 调用时） <a href="#on-webhook-call" id="on-webhook-call"></a>

此参数让工作流在 Wait 节点收到 HTTP 调用时恢复执行。

用于恢复执行的 webhook URL 在运行时生成。Wait 节点提供 `$execution.resumeUrl` 变量，便于提前引用并将这个稍后生成的 URL 发送到所需位置，例如第三方服务或电子邮件。

工作流执行时，Wait 节点使用 `$execution.resumeUrl` 生成恢复 URL 及工作流中的 webhook。每次执行生成的 URL 都是唯一的，因此工作流可包含多个 Wait 节点；调用 webhook URL 时，会依次恢复各个 Wait 节点。

使用此 **Resume**（恢复执行）方式时，还需配置以下参数。

#### Authentication（身份验证） <a href="#authentication" id="authentication"></a>

选择是否以及如何对传入 `$execution.resumeUrl` 的恢复 webhook 请求进行身份验证，可选：

* **Basic Auth**（Basic 认证）：使用 Basic 身份验证。选择或新建要使用的 **Credential for Basic Auth**（Basic 认证凭据）。
* **Header Auth**（请求头认证）：使用请求头身份验证。选择或新建要使用的 **Credential for Header Auth**（请求头认证凭据）。
* **JWT Auth**（JWT 认证）：使用 JWT 身份验证。选择或新建要使用的 **Credential for JWT Auth**（JWT 认证凭据）。
* **None**（无）：不使用身份验证。

{% hint style="info" %}
**身份验证参考**

有关各认证类型的更多信息，请参阅 [Webhook 节点的身份验证文档](n8n-nodes-base.webhook/README.md#supported-authentication-methods)。
{% endhint %}

#### HTTP Method（HTTP 方法） <a href="#http-method" id="http-method"></a>

选择 webhook 使用的 HTTP 方法。更多信息，请参阅 [Webhook 节点的 HTTP Method 文档](n8n-nodes-base.webhook/README.md#http-method)。

#### Response Code（响应码） <a href="#response-code" id="response-code"></a>

输入 webhook 应返回的响应码，可以使用常见响应码，也可以输入自定义值。

#### Respond（响应方式） <a href="#respond" id="respond"></a>

选择何时以及如何响应 webhook：

* **Immediately**（立即）：节点一执行就响应。
* **When Last Node Finishes**（最后一个节点完成时）：返回响应码，以及工作流中最后执行节点的输出数据。选择此选项后，还需设置：
  * **Response Data**（响应数据）：选择要返回的数据及其格式，可选：
    * **All Entries**（所有数据项）：将最后一个节点的所有数据项作为数组返回。
    * **First Entry JSON**（首个数据项的 JSON）：将最后一个节点首个数据项的 JSON 数据作为 JSON 对象返回。
    * **First Entry Binary**（首个数据项的二进制数据）：将最后一个节点首个数据项的二进制数据作为二进制文件返回。
    * **No Response Body**（无响应体）：返回时不包含响应体。
* **Using 'Respond to Webhook' Node**（使用 Respond to Webhook 节点）：按照 [Respond to Webhook](n8n-nodes-base.respondtowebhook.md) 节点中的定义响应。

#### Limit Wait Time（限制等待时间） <a href="#limit-wait-time" id="limit-wait-time"></a>

设置工作流是否在达到指定限制后自动恢复执行：开启时自动恢复，关闭时不自动恢复。开启后，还需设置：

* **Limit Type**（限制类型）：选择要实施的限制类型：
  * **After Time Interval**（经过时间间隔后）：等待指定时长。
    * 输入时间限制的 **Amount**（数值）。
    * 选择时间限制的 **Unit**（单位）。
  * **At Specified Time**（在指定时间）：等待到指定日期和时间后恢复执行。
    * **Max Date and Time**（最晚日期和时间）：使用日期与时间选择器设置节点应恢复执行的时间。

#### On Webhook Call（收到 Webhook 调用时）选项 <a href="#on-webhook-call-options" id="on-webhook-call-options"></a>

* **Binary Property**（二进制属性）：输入用于写入所接收文件数据的二进制属性名称。仅在收到二进制数据时适用。
* **Ignore Bots**（忽略机器人）：开启时忽略链接预览器、网络爬虫等机器人的请求，关闭时不忽略。
* **IP(s) Whitelist**（IP 允许列表）：限制可调用 webhook URL 的来源，输入以逗号分隔的允许 IP 地址。列表外的 IP 会收到 403 错误。留空时，所有 IP 地址均可调用。
* **No Response Body**（无响应体）：关闭时，n8n 发送响应体；开启时，阻止 n8n 发送响应体。
* **Raw Body**（原始请求体）：开启时，以 JSON 或 XML 等原始格式返回 body 数据；关闭时不使用原始格式。
* **Response Data**（响应数据）：输入希望在响应中发送的自定义数据。
* **Response Headers**（响应头）：在 webhook 响应中发送额外响应头。更多信息，请参阅 [MDN Web Docs | 响应头](https://developer.mozilla.org/en-US/docs/Glossary/Response_header)。
* **Webhook Suffix**（Webhook 后缀）：输入要附加到恢复 URL 的后缀。如果工作流包含多个 Wait 节点，可借此为每个节点创建唯一的 webhook URL。生成的 `$resumeWebhookUrl` 不会自动包含此后缀，向外部提供 webhook URL 前，必须手动追加后缀。

#### On Webhook Call（收到 Webhook 调用时）的限制 <a href="#on-webhook-call-limitations" id="on-webhook-call-limitations"></a>

使用 On Webhook Call 时，应注意以下限制：

* 部分执行工作流会更改 `$resumeWebhookUrl`，因此，向第三方发送此 URL 的节点必须与 Wait 节点处于同一次执行中。

### On Form Submitted（表单提交时） <a href="#on-form-submitted" id="on-form-submitted"></a>

等待收到表单提交后再继续执行。配置以下参数：

#### Form Title（表单标题） <a href="#form-title" id="form-title"></a>

输入显示在表单顶部的标题。

#### Form Description（表单说明） <a href="#form-description" id="form-description"></a>

输入显示在标题下方的表单说明，可用于提示用户如何填写表单。

#### Form Fields（表单字段） <a href="#form-fields" id="form-fields"></a>

使用以下参数配置每个要在表单中显示的字段：

* **Field Label**（字段标签）：输入要在表单中显示的字段标签。
* **Field Type**（字段类型）：选择要在表单中显示的字段类型，可选：
  * **Date**（日期）
  * **Dropdown List**（下拉列表）：在 **Field Options**（字段选项）中输入各个下拉选项。
    * **Multiple Choice**（多选）：关闭时，用户只能选择一个下拉选项；开启时，可以选择多个。
  * **Number**（数字）
  * **Password**（密码）
  * **Text**（文本）
  * **Textarea**（多行文本）
* **Required Field**（必填字段）：开启时，用户必须填写此字段才能提交表单；关闭时，可不填写此字段直接提交。

#### Respond When（响应时机） <a href="#respond-when" id="respond-when"></a>

选择何时响应表单提交：

* **Form Is Submitted**（表单提交时）：此节点收到表单提交后立即响应。
* **Workflow Finishes**（工作流结束时）：工作流的最后一个节点完成后响应。
* **Using 'Respond to Webhook' Node**（使用 Respond to Webhook 节点）：在 [Respond to Webhook](n8n-nodes-base.respondtowebhook.md) 节点执行时响应。

#### Limit Wait Time（限制等待时间） <a href="#limit-wait-time" id="limit-wait-time"></a>

设置工作流是否在达到指定限制后自动恢复执行：开启时自动恢复，关闭时不自动恢复。

开启后，还需设置：

* **Limit Type**（限制类型）：选择要实施的限制类型：
  * **After Time Interval**（经过时间间隔后）：等待指定时长。
    * 输入时间限制的 **Amount**（数值）。
    * 选择时间限制的 **Unit**（单位）。
  * **At Specified Time**（在指定时间）：等待到指定日期和时间后恢复执行。
    * **Max Date and Time**（最晚日期和时间）：使用日期与时间选择器设置节点应恢复执行的时间。

#### On Form Response（表单响应）选项 <a href="#on-form-response-options" id="on-form-response-options"></a>

* **Form Response**（表单响应）：通过以下 **Respond With**（响应内容）选项选择表单的响应方式及内容：
  * **Form Submitted Text**（表单提交提示文本）：用户填写表单后，显示 **Text to Show**（要显示的文本）中输入的内容。需要显示确认消息时可使用此选项。
  * **Redirect URL**（重定向 URL）：用户填写表单后，跳转到 **URL to Redirect to**（重定向目标 URL）。必须是有效的 URL。
* **Webhook Suffix**（Webhook 后缀）：输入要附加到恢复 URL 的后缀。如果工作流包含多个 Wait 节点，可借此为每个节点创建唯一的 webhook URL。生成的 `$resumeWebhookUrl` 不会自动包含此后缀，向外部提供 webhook URL 前，必须手动追加后缀。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Wait 集成模板](https://n8n.io/integrations/wait)，或[搜索所有模板](https://n8n.io/workflows/)

## 基于时间的操作 <a href="#time-based-operations" id="time-based-operations"></a>

对于基于时间的恢复操作，请注意：

* 等待时间短于 65 秒时，工作流不会将执行数据卸载到数据库。进程会继续运行，并在指定间隔过去后恢复执行。
* 始终使用 n8n 服务器时间，不受时区设置影响。工作流的时区设置及其变更，不会影响 Wait 节点的时间间隔或指定时间。
