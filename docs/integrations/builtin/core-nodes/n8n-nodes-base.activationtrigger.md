---
title: Activation Trigger（激活触发器） 节点文档
description: 了解如何在 n8n 中使用 Activation Trigger（激活触发器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Activation Trigger（激活触发器） 节点文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.activationtrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.activationtrigger
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.activationtrigger
layout:
  description:
    visible: false
tags:
- tag: deprecated
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Activation Trigger（激活触发器） 节点 <a href="#activation-trigger-node" id="activation-trigger-node"></a>

n8n 或工作流发出事件时，Activation Trigger 节点会触发。

{% hint style="warning" %}
**功能可用性**

Activation Trigger 节点从 n8n 0.117.0 起弃用，由两个新节点替代：[n8n Trigger 节点](n8n-nodes-base.n8ntrigger.md)和 [Workflow Trigger 节点](n8n-nodes-base.workflowtrigger.md)。更多详情请查看[破坏性变更](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md#01170)页面中的对应条目，以及[已弃用和具有版本的节点](../deprecated-nodes.md)。
{% endhint %}

{% hint style="info" %}
**请注意**

要为工作流使用 Activation Trigger 节点，将它添加到该工作流即可，无需另建工作流。
{% endhint %}

Activation Trigger 节点会针对其所在的工作流触发。可用它启动工作流，以通知该工作流的状态。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

- Events（事件）
    - **Activation**（激活）：工作流发布时运行。
    - **Start**（启动）：n8n 启动或重启时运行。
    - **Update**（更新）：处于活跃状态的工作流被保存时运行。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Activation Trigger（激活触发器） 集成模板](https://n8n.io/integrations/activation-trigger)，或[搜索所有模板](https://n8n.io/workflows/)
