---
description: 处理 n8n 元数据的方法。
contentType: reference
hide:
- toc
nodeTitle: n8n 元数据
originalFilePath: code/builtin/n8n-metadata.md
originalUrl: https://docs.n8n.io/code/builtin/n8n-metadata
url: https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/n8n-metadata
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# n8n 元数据 <a href="#n8n-metadata" id="n8n-metadata"></a>

处理 n8n 元数据的方法。

包括：

* 访问自托管 n8n 的环境变量。
* 工作流、执行和节点的元数据。
* 实例[变量](../define-custom-variables.md)和[外部机密](../../../administer/manage-credentials/use-external-secret-stores.md)的信息。

{% hint style="info" %}
**Python 支持**

可以在 Code 节点中使用 Python，但表达式不支持 Python。
{% endhint %}

## JavaScript <a id="javascript"></a>

| 方法 | 说明 | Code 节点中是否可用 |
| ------ | ----------- | :-------------------------: |
| `$env` | 包含 n8n 实例配置的[环境变量](../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/README.md)。 | ✅ |
| `$execution.customData` | 设置和获取自定义执行数据。更多信息请参阅[自定义执行数据](../../understand-workflows/understand-executions/customize-executions-data.md)。 | ✅ |
| `$execution.id` | 当前工作流执行的唯一 ID。 | ✅ |
| `$execution.mode` | 执行由自动触发还是手动运行工作流启动，可选值为 `test` 和 `production`。 | ✅ |
| `$execution.resumeUrl` | 用于恢复在 [Wait 节点](../../../integrations/builtin/core-nodes/n8n-nodes-base.wait.md)处等待的工作流的 Webhook URL。 | ✅ |
| `$getWorkflowStaticData(type)` | 访问工作流静态数据。测试工作流时，静态数据不会持久保存：需发布工作流，并通过触发器或 Webhook 运行才能保存。要在多次执行之间持久保存数据，可考虑改用[数据表](../../work-with-data/data-tables.md)。查看[示例](../cookbook/built-in-methods-and-variables-examples/getworkflowstaticdata.md)。 | ✅ |
| `$("<node-name>").isExecuted` | 检查节点是否已经执行。 | ✅ |
| `$itemIndex` | 数据项在列表中的索引。 | ❌ |
| `$nodeVersion` | 获取当前节点的版本。 | ✅ |
| `$prevNode.name` | 当前输入来源节点的名称。使用 Merge 节点时，请注意 `$prevNode` 始终使用第一个输入连接点。 | ✅ |
| `$prevNode.outputIndex` | 当前输入来源的输出连接点索引。前一节点有多个输出时使用，例如 If 或 Switch 节点。使用 Merge 节点时，请注意 `$prevNode` 始终使用第一个输入连接点。 | ✅ |
| `$prevNode.runIndex` | 前一节点生成当前输入时对应的运行。使用 Merge 节点时，请注意 `$prevNode` 始终使用第一个输入连接点。 | ✅ |
| `$runIndex` | n8n 已执行当前节点的次数，从零开始计数：第一次运行是 0，第二次是 1，依此类推。 | ✅ |
| `$secrets` | 包含[外部机密](../../../administer/manage-credentials/use-external-secret-stores.md)配置信息。 | ❌ |
| `$vars` | 包含当前环境可用的[变量](../define-custom-variables.md)。 | ✅ |
| `$version` | 节点版本。 | ❌ |
| `$workflow.active` | 工作流是否处于活跃状态：true 表示是，false 表示否。 | ✅ |
| `$workflow.id` | 工作流 ID。 | ✅ |
| `$workflow.name` | 工作流名称。 | ✅ |

## Python（原生） <a id="python-native"></a>

| 方法 | 说明 |
| ------ | ----------- |
| `_items` | 包含“Run once for all items（为所有数据项运行一次）”模式下的传入数据项。 |
| `_item` | 包含“Run once for each item（为每个数据项运行一次）”模式下正在遍历的数据项。 |
| `_query` | 在 Code Tool 中，包含 AI Agent 调用工具时传入的输入字符串。可用于“Run once for all items（为所有数据项运行一次）”模式。 |

## Python（Pyodide，已弃用） <a id="python-pyodide-deprecated"></a>

从 n8n 1.113.2 起，Python（Pyodide）支持已弃用。请改用原生 Python。

| 方法 | 说明 |
| ------ | ----------- |
| `_env` | 包含 n8n 实例配置的[环境变量](../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/README.md)。 |
| `_execution.customData` | 设置和获取自定义执行数据。更多信息请参阅[自定义执行数据](../../understand-workflows/understand-executions/customize-executions-data.md)。 |
| `_execution.id` | 当前工作流执行的唯一 ID。 |
| `_execution.mode` | 执行由自动触发还是手动运行工作流启动，可选值为 `test` 和 `production`。 |
| `_execution.resumeUrl` | 用于恢复在 [Wait 节点](../../../integrations/builtin/core-nodes/n8n-nodes-base.wait.md)处等待的工作流的 Webhook URL。 |
| `_getWorkflowStaticData(type)` | 访问工作流静态数据。测试工作流时，静态数据不会持久保存：需发布工作流，并通过触发器或 Webhook 运行才能保存。要在多次执行之间持久保存数据，可考虑改用[数据表](../../work-with-data/data-tables.md)。查看[示例](../cookbook/built-in-methods-and-variables-examples/getworkflowstaticdata.md)。 |
| `_("<node-name>").isExecuted` | 检查节点是否已经执行。 |
| `_nodeVersion` | 获取当前节点的版本。 | ✅ |
| `_prevNode.name` | 当前输入来源节点的名称。使用 Merge 节点时，请注意 `_prevNode` 始终使用第一个输入连接点。 |
| `_prevNode.outputIndex` | 当前输入来源的输出连接点索引。前一节点有多个输出时使用，例如 If 或 Switch 节点。使用 Merge 节点时，请注意 `_prevNode` 始终使用第一个输入连接点。 |
| `_prevNode.runIndex` | 前一节点生成当前输入时对应的运行。使用 Merge 节点时，请注意 `_prevNode` 始终使用第一个输入连接点。 |
| `_runIndex` | n8n 已执行当前节点的次数，从零开始计数：第一次运行是 0，第二次是 1，依此类推。 |
| `_secrets` | 包含[外部机密](../../../administer/manage-credentials/use-external-secret-stores.md)配置信息。 |
| `_vars` | 包含当前环境可用的[变量](../define-custom-variables.md)。 |
| `_workflow.active` | 工作流是否处于活跃状态：true 表示是，false 表示否。 |
| `_workflow.id` | 工作流 ID。 |
| `_workflow.name` | 工作流名称。 |

## 相关资源 <a id="related-resources"></a>

* [使用内置快捷方法](../use-built-in-shortcuts.md)
* [JMESPath](jmespath.md)
* [HTTP 节点](http-node.md)
* [LangChain Code 节点](langchain-code-node.md)
