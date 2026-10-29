---
title: Execute Sub-workflow Trigger（执行子工作流触发器） 节点文档
description: 了解如何在 n8n 中使用 Execute Sub-workflow Trigger（执行子工作流触发器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: Execute Sub-workflow Trigger（执行子工作流触发器） 节点文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Execute Sub-workflow Trigger（执行子工作流触发器） 节点 <a href="#execute-sub-workflow-trigger-node" id="execute-sub-workflow-trigger-node"></a>

使用此节点，响应另一个工作流的调用来启动工作流。它应作为工作流的第一个节点。

n8n 允许从一个工作流调用其他工作流，适用于以下需求：

* 复用工作流：例如，多个工作流分别从不同来源获取并处理数据，再共同调用一个用于生成报告的工作流。
* 将大型工作流拆分为更小的组件。

## 用法 <a href="#usage" id="usage"></a>

此节点响应 [Execute Sub-workflow](n8n-nodes-base.executeworkflow.md) 或 [Call n8n Workflow Tool](../cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md) 节点的调用而运行。

{% include "../../../reusable-content/.gitbook/includes/flow-logic/subworkflow-usage.md" %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Execute Sub-workflow Trigger（执行子工作流触发器） 集成模板](https://n8n.io/integrations/execute-workflow-trigger)，或[搜索所有模板](https://n8n.io/workflows/)

## 工作流之间如何传递数据 <a href="#how-data-passes-between-workflows" id="how-data-passes-between-workflows"></a>

{% include "../../../reusable-content/.gitbook/includes/flow-logic/subworkflow-data-flow.md" %}
