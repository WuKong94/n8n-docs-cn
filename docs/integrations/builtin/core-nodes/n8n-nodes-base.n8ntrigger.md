---
title: n8n Trigger（n8n 触发器） 节点文档
description: 了解如何在 n8n 中使用 n8n Trigger（n8n 触发器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: n8n Trigger（n8n 触发器） 节点文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# n8n Trigger（n8n 触发器） 节点 <a href="#n8n-trigger-node" id="n8n-trigger-node"></a>

包含 n8n Trigger 节点的工作流更新或发布时，或 n8n 实例启动或重启时，此节点会触发。它仅响应所在工作流中的事件，其他工作流的变更不会触发它。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

节点只有一个参数，用于指定触发它的 **Events**（事件）。可选择：

- **Published Workflow Updated**（已发布工作流更新）：包含此节点的工作流更新时触发。其他工作流的变更不会触发此节点。
- **Instance started**（实例已启动）：n8n 实例启动或重启时触发。
- **Workflow Published**（工作流已发布）：包含此节点的工作流发布时触发。发布其他工作流不会触发此节点。

可选择一个或多个事件。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n Trigger（n8n 触发器） 集成模板](https://n8n.io/integrations/n8n-trigger)，或[搜索所有模板](https://n8n.io/workflows/)

