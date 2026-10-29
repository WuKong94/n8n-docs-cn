---
title: Model Selector（模型选择器）
description: 了解如何在 n8n 中使用 Model Selector（模型选择器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: Model Selector（模型选择器）
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.modelselector.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.modelselector
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.modelselector
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Model Selector（模型选择器） <a href="#model-selector" id="model-selector"></a>

Model Selector 节点在工作流执行期间，根据一组定义的条件动态选择某个已连接的语言模型，可实现错误处理的后备机制，或为特定任务选择最合适的模型。

本页介绍 Model Selector 节点的参数，并提供相关资源的链接。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

### Number of Inputs（输入数量） <a href="#number-of-inputs" id="number-of-inputs"></a>

指定用于连接语言模型的输入连接数量。

### Rules（规则） <a href="#rules" id="rules"></a>

每条规则定义特定条件匹配时使用的模型。

Model Selector 节点从第一个输入开始，按顺序评估规则，找到匹配后立即停止。因此，即使多条规则都能匹配，n8n 也只使用第一条匹配规则定义的模型。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Model Selector（模型选择器） 集成模板](https://n8n.io/integrations/model-selector)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}
