---
title: Call n8n Workflow Tool（调用 n8n 工作流工具） 节点文档
description: 了解如何在 n8n 中使用 Call n8n Workflow Tool（调用 n8n 工作流工具） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: Call n8n Workflow Tool（调用 n8n 工作流工具） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Call n8n Workflow Tool（调用 n8n 工作流工具） 节点 <a href="#call-n8n-workflow-tool-node" id="call-n8n-workflow-tool-node"></a>

Call n8n Workflow Tool 节点是一种工具[^1]，让智能体[^2]能够运行另一个 n8n 工作流并获取其输出数据。

本页列出了 Call n8n Workflow Tool 节点的参数，并提供更多资源的链接。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

### 描述 <a href="#description" id="description"></a>

为此工作流工具输入描述，告诉智能体何时使用它。例如：

> 调用此工具获取随机颜色。输入应为字符串，用逗号分隔要排除的颜色名称。

### Source（来源） <a href="#source" id="source"></a>

指定 n8n 要调用的工作流，可选择以下任一方式：

* **Database**（数据库）：从列表选择工作流，或输入工作流 ID。
* **Define Below**（在下方定义）：复制完整的[工作流 JSON](../../../../build/manage-workflows/export-and-import.md)。

{% hint style="warning" %}
工作流来源为 **Database**（数据库），且智能体在生产环境运行而非手动或聊天测试面板时，子工作流必须已发布。否则，工具调用会以 `Workflow is not active and cannot be executed` 错误失败，错误文本作为工具结果返回智能体，在较长的智能体回复中可能被忽略。如果智能体报告无法获取数据，请检查子工作流是否已发布，以及其执行记录列表是否有运行记录。
{% endhint %}

### Workflow Inputs（工作流输入） <a href="#workflow-inputs" id="workflow-inputs"></a>

工作流来源为 **Database**（数据库）时，选择子工作流并在其中定义 **Workflow Input Schema**（工作流输入架构）后，即可定义 **Workflow Inputs**（工作流输入）。

选择 **Refresh**（刷新）按钮，从子工作流获取输入字段。

可组合以下任意方式定义工作流输入值：

* 提供固定值。
* 使用表达式引用当前工作流的数据。
* 选择字段右侧的 AI 按钮，[让 AI 模型指定参数](../../../../build/integrate-ai/ai-examples/use-ai-for-parameters.md)。
* 在表达式中使用 [`$fromAI()` 函数](../../../../build/integrate-ai/ai-examples/use-ai-for-parameters.md#use-the-fromai-function)，控制模型填充数据的方式，并混合 AI 生成的输入与其他自定义输入。

要引用当前工作流的数据，请先选择 Expressions（表达式）模式，再将输入面板中的字段拖到目标字段。

开始使用 `$fromAI()` 函数时，选择字段右侧的“Let the model define this parameter”（让模型定义此参数）按钮，再使用框中的 **X** 恢复为用户定义值。字段会变成表达式字段，并预填 `$fromAI()` 表达式。随后可自定义表达式，添加其他静态或动态内容，或调整 `$fromAI()` 函数参数。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Call n8n Workflow Tool（调用 n8n 工作流工具） 集成模板](https://n8n.io/integrations/workflow-tool)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/tools-link.md" %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: 在 AI 场景中，工具是附加资源，AI 可在响应请求时调用它获取特定信息或功能。AI 模型可以通过工具与外部系统交互，或完成具体、专门的任务。
[^2]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大型语言模型（LLM）理解用户输入，并根据可用的信息和资源，决定如何最好地处理请求。
