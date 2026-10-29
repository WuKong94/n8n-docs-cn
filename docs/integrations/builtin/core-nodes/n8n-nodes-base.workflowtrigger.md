---
title: Workflow Trigger（工作流触发器） 节点文档
description: 了解如何在 n8n 中使用 Workflow Trigger（工作流触发器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: Workflow Trigger（工作流触发器） 节点文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.workflowtrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.workflowtrigger
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.workflowtrigger
layout:
  description:
    visible: false
tags:
- tag: deprecated
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Workflow Trigger（工作流触发器） 节点 <a href="#workflow-trigger-node" id="workflow-trigger-node"></a>

工作流更新或激活时，Workflow Trigger 节点会触发。

{% hint style="warning" %}
**功能可用性**

Workflow Trigger 节点从 n8n 1.64.0 起弃用，其功能已移至 [n8n Trigger 节点](n8n-nodes-base.n8ntrigger.md)。更多信息请参阅[已弃用和具有版本的节点](../deprecated-nodes.md)。
{% endhint %}

{% hint style="info" %}
**请注意**

要为工作流使用 Workflow Trigger 节点，将它添加到该工作流即可，无需另建工作流。
{% endhint %}

Workflow Trigger 节点会针对其所在的工作流触发。可用它启动工作流，以通知该工作流的状态。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

节点只有一个参数，用于指定触发它的 **Events**（事件）。可选择：

- **Active Workflow Updated**（活跃工作流已更新）：此工作流更新时触发。
- **Workflow Activated**（工作流已激活）：此工作流激活时触发。

可选择一个或同时选择两个事件。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Workflow Trigger（工作流触发器） 集成模板](https://n8n.io/integrations/workflow-trigger)，或[搜索所有模板](https://n8n.io/workflows/)
