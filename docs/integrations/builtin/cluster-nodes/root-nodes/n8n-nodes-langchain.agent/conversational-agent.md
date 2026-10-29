---
title: Conversational AI Agent（对话式 AI 智能体） 节点文档
description: 了解如何在 n8n 的 AI Agent 节点中使用 Conversational Agent，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: critical
nodeTitle: Conversational AI Agent（对话式 AI 智能体） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent
layout:
  description:
    visible: false
tags:
- tag: deprecated
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Conversational AI Agent（对话式 AI 智能体） 节点 <a href="#conversational-ai-agent-node" id="conversational-ai-agent-node"></a>

{% hint style="warning" %}
**功能可用性**

Conversational Agent 从 n8n 1.82.0 起弃用。新增或更新的 AI Agent 节点改用 [Tools Agent](tools-agent.md)。只有仍使用 AI Agent 节点版本 1 的工作流可选择 Conversational Agent。

AI Agent 节点版本 1 从 n8n 3.0 中移除，因此 Conversational Agent 将在所有工作流中停止工作。详情请参阅 [n8n 3.0 破坏性变更](../../../../../changelog/v30-breaking-changes.md)。
{% endhint %}

Conversational Agent 支持类似人类的对话，可保持上下文、理解用户意图并给出相关回答，通常用于构建聊天机器人、虚拟助手和客户支持系统。

Conversational Agent 在系统提示词中描述工具[^1]，并通过解析 JSON 响应进行工具调用。首选 AI 模型不支持工具调用，或交互较简单时，它是一个通用选择。它更灵活，但准确性可能低于 [Tools Agent](tools-agent.md)。

AI Agent 节点本身的更多信息，请参阅 [AI Agent](README.md)。

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/use-with-chat-trigger.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置 Conversational Agent。

### Prompt（提示词） <a href="#prompt" id="prompt"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/prompt.md" %}

### Require Specific Output Format（要求指定输出格式） <a href="#require-specific-output-format" id="require-specific-output-format"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/output-format.md" %}

## 节点选项 <a href="#node-options" id="node-options"></a>

使用以下选项调整 Conversational Agent 节点的行为：

### Human Message（用户消息） <a href="#human-message" id="human-message"></a>

告诉智能体可使用哪些工具，并为用户输入添加上下文。

必须包含以下表达式和变量：

* `{tools}`：提供已连接到 Agent 的工具字符串的 LangChain 表达式。请补充上下文或说明，解释谁应该使用这些工具，以及应如何使用。
* `{format_instructions}`：提供已连接输出解析器节点的架构或格式的 LangChain 表达式。指令本身就是上下文，因此无需为此表达式额外补充上下文。
* `{{input}}`：包含用户提示词的 LangChain 变量，由 **Prompt**（提示词）参数的值填充。请补充上下文，说明这是用户输入。

这些字符串的用法示例如下：

例如：

```
工具
------
助手可以请用户使用工具，查找有助于回答用户原始问题的信息。用户可以使用以下工具：

{tools}

{format_instructions}

用户输入
--------------------
以下是用户输入（记住：仅返回包含单个 action 的 JSON 对象的 Markdown 代码片段，不要返回任何其他内容）：

{{input}}
```

### System Message（系统消息） <a href="#system-message" id="system-message"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/system-message.md" %}

### Max Iterations（最大迭代次数） <a href="#max-iterations" id="max-iterations"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/max-iterations.md" %}

### Return Intermediate Steps（返回中间步骤） <a href="#return-intermediate-steps" id="return-intermediate-steps"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/return-intermediate-steps.md" %}

### Tracing Metadata（追踪元数据） <a href="#tracing-metadata" id="tracing-metadata"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/tracing-metadata.md" %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

请参阅 AI Agent 主节点的[模板与示例](README.md#templates-and-examples)部分。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见问题及建议的解决办法，请参阅[常见问题](common-issues.md)。

[^1]: 在 AI 场景中，工具是附加资源，AI 可在响应请求时调用它获取特定信息或功能。AI 模型可以通过工具与外部系统交互，或完成具体、专门的任务。
