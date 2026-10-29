---
title: 手动执行、部分执行与生产执行
description: 了解手动执行、部分执行和自动执行工作流的区别。
contentType: explanation
nodeTitle: 执行类型
originalFilePath: workflows/executions/manual-partial-and-production-executions.md
originalUrl: https://docs.n8n.io/workflows/executions/manual-partial-and-production-executions
url: https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 手动执行、部分执行与生产执行 <a href="#manual-partial-and-production-executions" id="manual-partial-and-production-executions"></a>

n8n 手动执行工作流（点击 **Execute Workflow（执行工作流）** 按钮）与自动执行工作流（工作流已**发布**并由事件或计划任务触发）的方式存在一些重要区别。

## 手动执行 <a href="#manual-executions" id="manual-executions"></a>

手动执行可以让你直接从画布[^1]运行工作流，测试工作流逻辑。这类执行是“临时运行”：只有手动选择 **Execute workflow（执行工作流）** 按钮时才会运行。

手动执行便于在构建过程中反复测试，跟踪流程逻辑并观察数据转换，从而降低构建难度。可以提供不同的输入数据项并修改节点选项，测试条件分支、数据格式变化和循环行为。

{% hint style="info" %}
**固定执行数据**

手动执行时，可以使用[数据固定](../../work-with-data/pin-and-mock-data.md)来“固定”或“冻结”节点的输出数据，也可以按需编辑固定的数据。

后续运行时，n8n 会使用固定数据代替实际执行该节点，再继续沿流程逻辑执行。这样可以在迭代时避免使用不断变化的数据，或反复向外部服务发起查询。生产执行会忽略所有固定数据。
{% endhint %}

## 部分执行 <a href="#partial-executions" id="partial-executions"></a>

在 **Editor（编辑器）** 标签页中点击工作流底部的 **Execute workflow（执行工作流）** 按钮，会手动运行整个工作流。也可以使用部分执行，只运行工作流中的特定步骤。部分执行属于手动执行，仅运行工作流中的部分节点。

要进行部分执行，选择节点，打开其详情视图，再选择 **Execute step（执行步骤）**。这会执行该节点，以及为其提供输入数据所需的前置节点。构建过程中，也可以临时停用工作流链中的特定节点，避免与对应服务交互。

更新特定节点的逻辑时，部分执行尤其有用，因为可以使用相同输入数据重新执行该节点。

### 排查部分执行问题 <a href="#troubleshooting-partial-executions" id="troubleshooting-partial-executions"></a>

运行部分执行时，可能遇到以下常见问题：


> The destination node is not connected to any trigger. Partial executions need a trigger.（目标节点未连接到任何触发器。部分执行需要触发器。）


在工作流未连接触发器的情况下尝试部分执行时，会出现此错误。手动执行（包括部分执行）会尽可能模拟生产执行，其中一项要求就是通过触发器节点说明何时应执行工作流逻辑。

解决方法是为包含待执行节点的工作流连接一个触发器节点。通常，[手动触发器](../../../integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger.md)是最简单的选择。

> Please execute the whole workflow, rather than just the node. (Existing execution data is too large.)（请执行整个工作流，而不是仅执行该节点。现有执行数据过大。）

对包含大量分支的工作流进行部分执行时，可能出现此错误。部分执行需要向 n8n 后端发送数据和工作流逻辑，而完整执行不需要以这种方式发送。当工作流超过这类消息允许的最大大小时，就会出现此错误。

解决方法是在部分执行期间使用 [Limit 节点](../../../integrations/builtin/core-nodes/n8n-nodes-base.limit.md)限制节点输出。工作流按预期运行后，可以先停用或删除 Limit 节点，再启用生产执行。

## 生产执行 <a href="#production-executions" id="production-executions"></a>

触发事件或计划任务自动运行工作流时，就会发生生产执行。在[付费套餐](https://n8n.io/pricing/)中，生产执行计入执行配额。哪些情况计入或不计入的详细说明，请参阅[执行如何计入配额](README.md#how-executions-count-towards-quotas)。

要配置生产执行，必须添加一个[触发器节点](#user-content-fn-2)[^2]（除[手动触发器](../../../integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger.md)之外的任意触发器均可），并使用 **Publish（发布）** 按钮[发布工作流](../save-and-publish-workflows.md)。发布后，每当触发条件满足，工作流就会自动执行。

与手动执行不同，生产执行的流程不会显示在工作流的 Editor 标签页中。根据[工作流设置](../../manage-workflows/configure-workflow-settings.md)，可以在 **Executions（执行）** 标签页查看执行记录，再通过[在编辑器中调试](debug-executions.md)功能排查问题。

[^1]: 画布是 n8n 编辑器中构建工作流的主要界面。你可以在画布上添加并连接节点，组成工作流。
<a id="user-content-fn-2"></a>
[^2]: 触发器节点是一种特殊节点，负责在特定条件满足时启动工作流。所有生产工作流都至少需要一个触发器，以确定何时运行。

## 相关资源 <a id="related-resources"></a>

* [理解执行](./)
* [查看所有执行](view-all-executions.md)
* [查看单个工作流的执行](view-executions-for-a-single-workflow.md)
* [调试并重新运行以往执行](debug-executions.md)
* [自定义执行数据](customize-executions-data.md)
* [流式传输实时响应](stream-real-time-responses.md)
* [脏节点](understand-dirty-nodes.md)
