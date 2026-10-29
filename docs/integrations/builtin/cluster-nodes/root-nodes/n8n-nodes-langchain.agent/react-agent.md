---
title: ReAct AI Agent（ReAct AI 智能体） 节点文档
description: 了解如何在 n8n 的 AI Agent 节点中使用 ReAct Agent，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: critical
nodeTitle: ReAct AI Agent（ReAct AI 智能体） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent
layout:
  description:
    visible: false
tags:
- tag: deprecated
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# ReAct AI Agent（ReAct AI 智能体） 节点 <a href="#react-ai-agent-node" id="react-ai-agent-node"></a>

{% hint style="warning" %}
**功能可用性**

ReAct Agent 从 n8n 1.82.0 起弃用。新增或更新的 AI Agent 节点改用 [Tools Agent](tools-agent.md)。只有仍使用 AI Agent 节点版本 1 的工作流可选择 ReAct Agent。

AI Agent 节点版本 1 从 n8n 3.0 中移除，因此 ReAct Agent 将在所有工作流中停止工作。详情请参阅 [n8n 3.0 破坏性变更](../../../../../changelog/v30-breaking-changes.md)。
{% endhint %}

ReAct Agent 节点实现 [ReAct](https://react-lm.github.io/) 逻辑。ReAct（推理与行动）结合了思维链提示和行动计划生成的推理能力。

ReAct Agent 针对给定任务进行推理，确定所需行动并执行，持续进行推理与行动循环，直到任务完成。它可以将复杂任务拆成更小的子任务，确定优先级并依次执行。

AI Agent 节点本身的更多信息，请参阅 [AI Agent](README.md)。

{% hint style="info" %}
**无记忆**

ReAct 智能体不支持记忆子节点，因此无法回忆之前的提示词或模拟持续对话。
{% endhint %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置 ReAct Agent。

### Prompt（提示词） <a href="#prompt" id="prompt"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/prompt.md" %}

### Require Specific Output Format（要求指定输出格式） <a href="#require-specific-output-format" id="require-specific-output-format"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/output-format.md" %}

## 节点选项 <a href="#node-options" id="node-options"></a>

使用以下选项创建在对话开始时发送给智能体的消息。消息类型取决于所用模型：

* **Chat models**（聊天模型）：具有 AI、系统和用户三个组件交互的概念，可接收系统消息和用户消息（提示词）。
* **Instruct models**（指令模型）：不区分独立的 AI、系统和用户组件，只接收一段指令消息文本。

### Human Message Template（用户消息模板） <a href="#human-message-template" id="human-message-template"></a>

使用此选项扩展用户提示词，让智能体将信息从一次迭代传给下一次。

可用的 LangChain 表达式：

* `{input}`：包含用户提示词。
* `{agent_scratchpad}`：需要为下一次迭代记住的信息。

### Prefix Message（前缀消息） <a href="#prefix-message" id="prefix-message"></a>

输入对话开始时放在工具列表前的文本。无需添加工具列表，LangChain 会自动添加。

### Suffix Message for Chat Model（聊天模型后缀消息） <a href="#suffix-message-for-chat-model" id="suffix-message-for-chat-model"></a>

输入智能体使用聊天模型时，在对话开始处放在工具列表后的文本。无需添加工具列表，LangChain 会自动添加。

### Suffix Message for Regular Model（常规模型后缀消息） <a href="#suffix-message-for-regular-model" id="suffix-message-for-regular-model"></a>

输入智能体使用常规模型或指令模型时，在对话开始处放在工具列表后的文本。无需添加工具列表，LangChain 会自动添加。

### Return Intermediate Steps（返回中间步骤） <a href="#return-intermediate-steps" id="return-intermediate-steps"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/return-intermediate-steps.md" %}

### Tracing Metadata（追踪元数据） <a href="#tracing-metadata" id="tracing-metadata"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/tracing-metadata.md" %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

更多信息请参阅 LangChain 的 [ReAct Agents](https://docs.langchain.com/oss/javascript/langchain/agents) 文档。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

请参阅 AI Agent 主节点的[模板与示例](README.md#templates-and-examples)部分。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见问题及建议的解决办法，请参阅[常见问题](common-issues.md)。


