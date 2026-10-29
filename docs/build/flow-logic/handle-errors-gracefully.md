---
contentType: howto
description: 如何处理执行错误。
nodeTitle: 妥善处理错误
originalFilePath: flow-logic/error-handling.md
originalUrl: https://docs.n8n.io/flow-logic/error-handling
url: https://docs.n8n.io/build/flow-logic/handle-errors-gracefully
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 错误处理 <a href="#error-handling" id="error-handling"></a>

设计[流程逻辑](./)时，建议考虑潜在错误，并设置妥善处理这些错误的方法。通过错误工作流，可以控制 n8n 在工作流执行失败时如何响应。

{% hint style="info" %}
**排查错误**

要排查失败的执行，可以：

* 查看[执行记录](../understand-workflows/understand-executions/README.md)，包括[单个工作流](../understand-workflows/understand-executions/view-executions-for-a-single-workflow.md)或[你有权访问的所有工作流](../understand-workflows/understand-executions/view-all-executions.md)的记录。可以将[以往执行的数据加载](../understand-workflows/understand-executions/debug-executions.md)到当前工作流中。
* 启用[日志流](../../administer/observe-and-log/stream-logs-to-external-systems.md)。
{% endhint %}

## 如何设置错误工作流？ <a href="#create-and-set-an-error-workflow" id="create-and-set-an-error-workflow"></a>

可以在每个工作流的 **Workflow Settings（工作流设置）** 中指定错误工作流。当执行失败时，错误工作流就会运行。例如，可以在工作流执行出错时发送电子邮件或 Slack 提醒。错误工作流必须以 [Error Trigger](../../integrations/builtin/core-nodes/n8n-nodes-base.errortrigger.md) 开始。

多个工作流可以共用同一个错误工作流。

{% include "../../reusable-content/.gitbook/includes/flow-logic/create-set-error-workflow.md" %}

## 错误工作流会收到哪些数据？ <a href="#error-data" id="error-data"></a>

{% include "../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/error-trigger/error-data.md" %}

## 如何使用 Stop and Error 节点主动让工作流失败？ <a href="#cause-a-workflow-execution-failure-using-stop-and-error" id="cause-a-workflow-execution-failure-using-stop-and-error"></a>

创建并设置错误工作流后，n8n 会在执行失败时运行它。通常，执行失败是由节点设置错误或工作流内存不足等问题引起的。

可以向工作流添加 [Stop And Error](../../integrations/builtin/core-nodes/n8n-nodes-base.stopanderror.md) 节点，在指定条件下主动让执行失败，并触发错误工作流。

## 相关资源 <a id="related-resources"></a>

* [流程逻辑](./)
* [按条件分支](split-with-conditionals.md)
* [合并数据](merge-data.md)
* [循环](loop.md)
* [等待](wait.md)
* [理解执行顺序](understand-execution-order.md)
* [将工作流拆分为更小的部分](break-workflows-into-smaller-parts.md)
* [转换为子工作流](convert-to-sub-workflows.md)
