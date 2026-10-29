---
contentType: howto
nodeTitle: 查看所有执行
originalFilePath: workflows/executions/all-executions.md
originalUrl: https://docs.n8n.io/workflows/executions/all-executions
url: https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions
description: 查看和筛选所有工作流的全部执行。
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


# 查看所有执行 <a id="view-all-executions"></a>

要查看 n8n 实例中的**所有执行**，进入 **Overview（概览）** 页面，再点击 Executions（执行）标签页。这里会显示你有权访问的工作流的全部执行。

如果 n8n 实例支持**项目**，也可以在有权访问的项目中查看执行标签页。这里仅显示该项目内工作流的执行。

{% hint style="info" %}
**已删除的工作流**

删除工作流时，n8n 也会删除其执行历史，因此无法查看已删除工作流的执行。
{% endhint %}

## 筛选执行 <a href="#filter-executions" id="filter-executions"></a>

可以筛选执行列表：

1. 在 **Overview（概览）** 页面或某个**项目**中，选择 **Executions（执行）** 标签页，打开列表。
2. 选择 **Filters（筛选）**。
3. 输入筛选条件。可以按以下字段筛选：
   * **Workflows（工作流）**：选择所有工作流，或指定工作流名称。
   * **Status（状态）**：选择 **Failed（失败）**、**Running（运行中）**、**Success（成功）** 或 **Waiting（等待中）**。
   * **Execution start（执行开始时间）**：查看在指定时间范围内开始的执行。
   * **Saved custom data（已保存的自定义数据）**：在工作流中通过 Code 节点创建的数据。输入键和值进行筛选。添加此类数据的方法，请参阅[自定义执行数据](customize-executions-data.md)。

{% include "../../../reusable-content/.gitbook/includes/workflows/executions/custom-execution-data-availability.md" %}

## 重试失败的工作流 <a href="#retry-failed-workflows" id="retry-failed-workflows"></a>

工作流执行失败时，可以重试。重试失败工作流的步骤如下：

1. 在 **Overview（概览）** 页面或某个**项目**中，选择 **Executions（执行）** 标签页，打开列表。
2. 在要重试的执行上，选择 **Retry execution（重试执行）** <img src="../../.gitbook/assets/three-dot-options-menu (1).png" alt="选项菜单图标" data-size="line">。

{% include "../../../reusable-content/.gitbook/includes/workflows/executions/retry-options.md" %}

### 重试会运行哪些内容 <a id="what-a-retry-runs"></a>

节点失败后，重试会从保存的执行状态恢复，而不是从触发器重新开始整个工作流：

* n8n 会保留已完成节点运行的结果。例如，工作流先添加一行数据，再在发送消息时失败，重试失败的消息节点不会重复之前的行添加操作。
* 失败节点会再次收到保存的输入，并处理每个数据项，包括失败前已经处理过的数据项。例如，某个节点在失败前已发送部分消息，重试时会再次发送这些消息。重试前，请检查目标应用中哪些数据项已被处理。要让重试更安全，可以使用更新已有记录的操作，代替创建新记录，例如 Google Sheets 节点中的 **Append or Update Row（追加或更新行）** 或 Postgres 节点中的 **Insert or Update（插入或更新）**。
* 如果失败的是 **Execute Sub-workflow** 节点，重试会从头重新运行整个子工作流。
* **Retry with original workflow（使用原工作流重试）** 会使用原执行时的工作流。如果已修改工作流以修复问题，选择 **Retry with currently saved workflow（使用当前保存的工作流重试）**。更改只影响尚未完成的节点，已完成节点保留保存的结果。两种选项都会在重试运行时加载凭据，因此如果只修复了凭据，**Retry with original workflow** 就会使用修复后的凭据。
* 每次重试都是一次新执行。如果重试失败，原执行和失败的重试执行都会显示重试选项。只重试其中一个：同时重试两者可能对同一数据重复操作。要避免额外的失败重试，请先修复原因再重试。
* 成功的执行无法重试，即使其行为不符合预期。例如，**If** 节点可能将所有数据项发送到了 false 分支。此时使用 **Copy to editor（复制到编辑器）**，将保存的数据固定到当前工作流的第一个节点，再重新运行工作流。这次运行会重复执行第一个节点之后的所有节点，包括添加行或发送消息等操作。支持范围和步骤请参阅[调试并重新运行以往执行](debug-executions.md)。
* 只有在 n8n 仍保存该执行记录时，才能重试。如果工作流的 [Save failed production executions（保存失败的生产执行）](../../manage-workflows/configure-workflow-settings.md#save-failed-production-executions)设置为 **Do not save（不保存）**，n8n 就不会保存失败的生产执行。执行保留时长的说明：自托管实例请参阅[执行数据](../../../deploy/host-n8n/configure-n8n/scaling/manage-execution-data.md)，n8n Cloud 请参阅[管理数据](../../../deploy/use-n8n-cloud/configure-cloud/manage-your-data.md)。

## 将以往执行的数据加载到当前工作流 <a href="#load-data-from-previous-executions-into-your-current-workflow" id="load-data-from-previous-executions-into-your-current-workflow"></a>

可以将以往工作流执行的数据重新加载到画布中。更多信息请参阅[调试执行](debug-executions.md)。

## 相关资源 <a id="related-resources"></a>

* [理解执行](./)
* [手动执行、部分执行与生产执行](types-of-executions.md)
* [查看单个工作流的执行](view-executions-for-a-single-workflow.md)
* [调试并重新运行以往执行](debug-executions.md)
* [自定义执行数据](customize-executions-data.md)
* [流式传输实时响应](stream-real-time-responses.md)
* [脏节点](understand-dirty-nodes.md)
