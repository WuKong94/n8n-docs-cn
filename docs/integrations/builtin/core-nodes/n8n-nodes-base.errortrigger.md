---
title: Error Trigger（错误触发器） 节点文档
description: 了解如何在 n8n 中使用 Error Trigger（错误触发器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Error Trigger（错误触发器） 节点文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.errortrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Error Trigger（错误触发器） 节点 <a href="#error-trigger-node" id="error-trigger-node"></a>

可以使用 Error Trigger 节点创建错误工作流。另一个已关联的工作流失败时，此节点会获取该工作流及其错误的详情，并运行错误工作流。

## 用法 <a href="#usage" id="usage"></a>

{% include "../../../reusable-content/.gitbook/includes/flow-logic/create-set-error-workflow.md" %}


请注意：

* 使用 Error Trigger 节点的工作流无需发布。
* 包含 Error Trigger 节点的工作流，默认以自身作为错误工作流。
* 手动运行工作流时，无法测试错误工作流。Error Trigger 仅在自动工作流发生错误时运行。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Error Trigger（错误触发器） 集成模板](https://n8n.io/integrations/error-trigger)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

可使用 [Stop And Error](n8n-nodes-base.stopanderror.md) 节点向 Error Trigger 发送自定义消息。

有关错误工作流的更多信息，请参阅 n8n 工作流中的[错误工作流](../../../build/flow-logic/handle-errors-gracefully.md)。

## 错误数据 <a href="#error-data" id="error-data"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/error-trigger/error-data.md" %}

