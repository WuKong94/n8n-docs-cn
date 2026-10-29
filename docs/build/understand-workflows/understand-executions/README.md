---
description: 一次执行是指工作流的一次运行。
contentType: overview
nodeTitle: 理解执行
originalFilePath: workflows/executions/index.md
originalUrl: https://docs.n8n.io/workflows/executions
url: https://docs.n8n.io/build/understand-workflows/understand-executions
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 执行 <a href="#executions" id="executions"></a>

一次执行是指工作流的一次运行。

## 本节内容 <a id="in-this-section"></a>

* [手动执行、部分执行与生产执行](types-of-executions.md)：了解这三种执行方式的区别。
* [查看所有执行](view-all-executions.md)：查看和筛选所有工作流的全部执行。
* [查看单个工作流的执行](view-executions-for-a-single-workflow.md)：查看和筛选当前画布中工作流的执行。
* [调试并重新运行以往执行](debug-executions.md)：将以往执行的数据复制到当前工作流中进行调试。
* [自定义执行数据](customize-executions-data.md)：使用 Code 节点为工作流执行添加自定义数据。
* [流式传输实时响应](stream-real-time-responses.md)：在 AI Agent 节点生成数据的同时，将其返回给用户。
* [脏节点](understand-dirty-nodes.md)：了解什么是脏节点，以及它们如何影响工作流执行。

## 执行模式 <a href="#execution-modes" id="execution-modes"></a>

有两种执行模式：

* **手动：** 点击 **Execute Workflow（执行工作流）**，手动运行工作流。通过手动运行进行测试时，应取消发布工作流。
* **生产：** 生产工作流会自动运行。发布工作流的某个版本，即可将其投入生产。

## 执行如何计入配额 <a href="#how-executions-count-towards-quotas" id="how-executions-count-towards-quotas"></a>

无论是云端还是自托管，[付费套餐](https://n8n.io/pricing/)都设有执行次数配额。只有生产执行会计入配额，即由触发器、计划任务或轮询自动启动的执行。无论实例用于开发还是生产等环境，均适用这一区分。

### 按触发器类型计算执行次数 <a href="#execution-count-by-trigger-type" id="execution-count-by-trigger-type"></a>

执行次数的计算方式取决于所用触发器节点的类型：

* **Schedule Trigger 节点：** 每次触发都计为一次执行，无论结果如何。
* **轮询节点（如 Google Drive Trigger）：** 只有发现新数据时，才计为一次执行。未返回结果的轮询不计入执行次数。
* **Webhook Trigger 节点：** 每个激活触发器的入站请求都计为一次执行，包括请求体为空的请求（例如 `{}`）。工作流开始前就失败的格式错误请求不计入执行次数。

### 不计入配额的触发和运行 <a href="#triggers-and-runs-that-dont-count" id="triggers-and-runs-that-dont-count"></a>

以下情况不计入执行配额：

* **手动执行：** 构建或测试时从编辑器运行工作流。
* **子工作流执行：** 工作流通过 Execute Sub-workflow 节点调用其他工作流时，只计算父级（顶层）执行。
* **错误工作流执行：** 被设为[错误工作流](../../flow-logic/handle-errors-gracefully.md)的工作流的运行。
* **未返回数据的轮询：** 轮询触发器只有发现新数据时才计入次数。
* **格式错误或被拒绝的请求：** 在工作流开始前就失败的 Webhook 请求。

## 执行列表 <a href="#execution-lists" id="execution-lists"></a>

n8n 提供两种执行列表：

* [工作流级别的执行](view-executions-for-a-single-workflow.md)：显示单个工作流的执行。
* [所有执行](view-all-executions.md)：显示所有工作流的全部执行。

n8n 支持[为执行添加自定义数据](customize-executions-data.md)。

## 执行数据隐藏 <a href="#execution-data-redaction" id="execution-data-redaction"></a>

可以隐藏执行数据，以保护敏感信息。此功能隐藏工作流执行的输入和输出数据，同时保留状态、时间和节点名称等执行元数据。详情请参阅[执行数据隐藏](../../../deploy/host-n8n/configure-n8n/security/redact-execution-data.md)。

## 来自你无权使用的凭据的执行数据 <a id="execution-data-from-credentials-you-cant-use"></a>

如果某次执行使用了你无权使用的凭据，n8n 会对你隐藏其数据，但仍显示执行状态和时间信息。这也包括使用该凭据的子工作流返回的数据，即使父工作流本身并未使用该凭据。通过公共 API 或 n8n MCP 服务器读取执行时，同样适用这些规则。

详情请参阅[在项目中使用个人凭据](../../../administer/manage-credentials/use-personal-credentials-in-projects.md#execution-data-from-credentials-you-cant-use)。

## 相关资源 <a id="related-resources"></a>

* [理解工作流](../)
* [创建和运行工作流](../create-and-run-workflows.md)
* [保存和发布工作流](../save-and-publish-workflows.md)
* [创建和编辑凭据](../create-and-edit-credentials.md)
* [使用 Gateway 额度](../use-gateway-credits.md)
* [工作流组件](../workflow-components/README.md)
