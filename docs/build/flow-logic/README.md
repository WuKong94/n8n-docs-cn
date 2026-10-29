---
title: 流程逻辑
description: 如何在 n8n 工作流中实现逻辑。
contentType: overview
nodeTitle: 流程逻辑
originalFilePath: flow-logic/index.md
originalUrl: https://docs.n8n.io/flow-logic
url: https://docs.n8n.io/build/
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 流程逻辑 <a href="#flow-logic" id="flow-logic"></a>

n8n 支持在工作流中实现复杂逻辑。

## 本节内容 <a href="#in-this-section" id="in-this-section"></a>

* [按条件分支](split-with-conditionals.md)：使用 IF 和 Switch 节点将数据项路由到不同分支。
* [合并数据](merge-data.md)：将多条数据流重新合并为一条。
* [循环](loop.md)：重复执行操作，直到满足某个条件或所有数据项都已处理。
* [等待](wait.md)：暂停工作流执行，并在之后恢复。
* [理解执行顺序](understand-execution-order.md)：了解 n8n 如何决定多分支工作流中哪个分支先运行。
* [将工作流拆分为更小的部分](break-workflows-into-smaller-parts.md)：从一个工作流调用另一个工作流，构建类似微服务的模块化工作流。
* [转换为子工作流](convert-to-sub-workflows.md)：将现有工作流的一部分转为可复用的子工作流。
* [妥善处理错误](handle-errors-gracefully.md)：设置错误工作流，以响应执行失败。

## 相关章节 <a href="#related-sections" id="related-sections"></a>

你需要对 n8n 中的[数据](../work-with-data/README.md)有所了解，包括[数据结构](../work-with-data/understand-n8ns-data-structure.md)和[节点内部的数据流](../work-with-data/understand-n8ns-data-structure.md#how-data-flows-within-nodes)。

构建逻辑时会用到 n8n 的[核心节点](../../integrations/builtin/core-nodes/README.md)，包括：

* 分支：[IF](../../integrations/builtin/core-nodes/n8n-nodes-base.if.md) 和 [Switch](../../integrations/builtin/core-nodes/n8n-nodes-base.switch.md)。
* 合并：[Merge](../../integrations/builtin/core-nodes/n8n-nodes-base.merge.md)、[Compare Datasets](../../integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets.md) 和 [Code](../../integrations/builtin/core-nodes/n8n-nodes-base.code/README.md)。
* 循环：[IF](../../integrations/builtin/core-nodes/n8n-nodes-base.if.md) 和 [Loop Over Items](../../integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md)。
* 等待：[Wait](../../integrations/builtin/core-nodes/n8n-nodes-base.wait.md)。
* 创建子工作流：[Execute Workflow](../../integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md) 和 [Execute Workflow Trigger](../../integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger.md)。
* 错误处理：[Stop And Error](../../integrations/builtin/core-nodes/n8n-nodes-base.stopanderror.md) 和 [Error Trigger](../../integrations/builtin/core-nodes/n8n-nodes-base.errortrigger.md)。

## 相关资源 <a id="related-resources"></a>

* [构建](../)
* [理解工作流](../understand-workflows/README.md)
* [构建和管理智能体](../build-and-manage-agents/README.md)
* [构建工作流的方式](../ways-of-building-workflows/README.md)
* [管理工作流](../manage-workflows/README.md)
* [处理数据](../work-with-data/README.md)
* [在 n8n 中编写代码](../code-in-n8n/README.md)
* [集成 AI](../integrate-ai/README.md)
* [键盘快捷键](../keyboard-shortcuts.md)
