---
contentType: howto
description: 从其他工作流调用工作流，并将大型工作流拆分为较小的组件。
nodeTitle: 将工作流拆分为更小的部分
originalFilePath: flow-logic/subworkflows.md
originalUrl: https://docs.n8n.io/flow-logic/subworkflows
url: https://docs.n8n.io/build/flow-logic/break-workflows-into-smaller-parts
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 子工作流 <a href="#sub-workflows" id="sub-workflows"></a>

可以从一个工作流调用另一个工作流，将其作为[流程逻辑](./)的一部分，构建类似微服务的模块化工作流。当工作流过大而遇到[内存问题](../../deploy/host-n8n/configure-n8n/scaling/fix-memory-issues.md)时，这种方式也有帮助。创建子工作流会用到 [Execute Workflow](../../integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md) 和 [Execute Sub-workflow Trigger](../../integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger.md) 节点。

子工作流执行不计入套餐的每月执行次数限额或活跃工作流数量限额。

## 设置和使用子工作流 <a href="#set-up-and-use-a-sub-workflow" id="set-up-and-use-a-sub-workflow"></a>

本节将介绍如何设置父工作流和子工作流。

{% include "../../reusable-content/.gitbook/includes/flow-logic/subworkflow-usage.md" %}

## 数据如何在工作流之间传递 <a href="#how-data-passes-between-workflows" id="how-data-passes-between-workflows"></a>

{% include "../../reusable-content/.gitbook/includes/flow-logic/subworkflow-data-flow.md" %}

## 子工作流转换 <a href="#sub-workflow-conversion" id="sub-workflow-conversion"></a>

将现有工作流拆分为子工作流的方法，请参阅[子工作流转换](convert-to-sub-workflows.md)。

## 相关资源 <a id="related-resources"></a>

* [流程逻辑](./)
* [按条件分支](split-with-conditionals.md)
* [合并数据](merge-data.md)
* [循环](loop.md)
* [等待](wait.md)
* [理解执行顺序](understand-execution-order.md)
* [转换为子工作流](convert-to-sub-workflows.md)
* [妥善处理错误](handle-errors-gracefully.md)
