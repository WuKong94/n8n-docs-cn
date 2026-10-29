---
title: AI Agent Tool（AI 智能体工具） 节点文档
description: 了解如何在 n8n 中使用 AI Agent Tool 节点，并按照技术文档将 AI 智能体工具集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: AI Agent Tool（AI 智能体工具） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolaiagent.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolaiagent
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolaiagent
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# AI Agent Tool（AI 智能体工具） 节点 <a href="#ai-agent-tool-node" id="ai-agent-tool-node"></a>

AI Agent Tool 节点允许工作流中的根级智能体[^1]将其他智能体作为工具调用，简化多智能体编排。

[主智能体](../root-nodes/n8n-nodes-langchain.agent/tools-agent.md)可以监督专长于不同任务和知识的 AI Agent Tool 节点，并向它们分派工作。这样即可在单个工作流中使用多个智能体，无需处理子工作流所要求的复杂上下文和变量管理。还可将 AI Agent Tool 节点嵌套为多层，满足更复杂的分层场景。

本页列出了 AI Agent Tool 节点的参数，并提供更多资源的链接。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置 AI Agent Tool 节点：

* **Description**（描述）：向 LLM 描述此智能体的目的和职责范围。具体、清晰的描述可告诉父智能体何时将任务交给此智能体处理。
* **Prompt (User Message)**（提示词，用户消息）：向 LLM 说明要执行什么操作、返回哪些信息的提示词。
* **Require Specific Output Format**（要求指定输出格式）：选择是否要求特定输出格式。开启后，n8n 会提示连接[主智能体页面介绍的输出解析器](../root-nodes/n8n-nodes-langchain.agent/tools-agent.md#require-specific-output-format)之一。
* **Enable Fallback Model**（启用后备模型）：选择是否启用后备模型。开启后，n8n 会提示连接备用聊天模型，在主模型失败或不可用时使用。

## 节点选项 <a href="#node-options" id="node-options"></a>

使用以下选项调整 AI Agent Tool 节点的行为：

* **System Message**（系统消息）：对话开始前发送给智能体的消息。
* **Max Iterations**（最大迭代次数）：停止前，模型为生成响应最多运行多少次。
* **Return Intermediate Steps**（返回中间步骤）：是否在最终输出中包含智能体执行的中间步骤。
* **Automatically Passthrough Binary Images**（自动传递二进制图像）：是否将二进制图像自动作为图像类型消息传给智能体。
* **Batch Processing**（批处理）：是否启用以下用于速率限制的批处理选项：
    * **Batch Size**（批次大小）：并行处理的数据项数量。有助于控制请求速率，但可能影响日志输出顺序。
    * **Delay Between Batches**（批次间延迟）：批次之间等待的毫秒数。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 AI Agent Tool（AI 智能体工具） 集成模板](https://n8n.io/integrations/ai-agent-tool)，或[搜索所有模板](https://n8n.io/workflows/)

## 使用 `$fromAI()` 动态设置工具参数 <a href="#dynamic-parameters-for-tools-with-dollarfromai" id="dynamic-parameters-for-tools-with-dollarfromai"></a>

动态填充应用节点工具参数的方法，请参阅[让 AI 使用 `$fromAI()` 指定工具参数](../../../../build/integrate-ai/ai-examples/use-ai-for-parameters.md)。

[^1]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大型语言模型（LLM）理解用户输入，并根据可用的信息和资源，决定如何最好地处理请求。
