---
title: Plan and Execute AI Agent（规划与执行 AI 智能体） 节点文档
description: 了解如何在 n8n 的 AI Agent 节点中使用 Plan and Execute Agent，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: critical
nodeTitle: Plan and Execute AI Agent（规划与执行 AI 智能体） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent
layout:
  description:
    visible: false
tags:
- tag: deprecated
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Plan and Execute Agent（规划与执行智能体）节点 <a href="#plan-and-execute-agent-node" id="plan-and-execute-agent-node"></a>

{% hint style="warning" %}
**功能可用性**

Plan and Execute Agent 从 n8n 1.82.0 起弃用。新增或更新的 AI Agent 节点改用 [Tools Agent](tools-agent.md)。只有仍使用 AI Agent 节点版本 1 的工作流可选择 Plan and Execute Agent。

AI Agent 节点版本 1 从 n8n 3.0 中移除，因此 Plan and Execute Agent 将在所有工作流中停止工作。详情请参阅 [n8n 3.0 破坏性变更](../../../../../changelog/v30-breaking-changes.md)。
{% endhint %}

Plan and Execute Agent 类似于 [ReAct 智能体](react-agent.md)，但更侧重规划。它先为指定任务制定高层计划，再逐步执行，最适合需要结构化方法和周密规划的任务。

AI Agent 节点本身的更多信息，请参阅 [AI Agent](README.md)。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置 Plan and Execute Agent。

### Prompt（提示词） <a href="#prompt" id="prompt"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/prompt.md" %}

### Require Specific Output Format（要求指定输出格式） <a href="#require-specific-output-format" id="require-specific-output-format"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/output-format.md" %}

## 节点选项 <a href="#node-options" id="node-options"></a>

使用以下选项调整 Plan and Execute Agent 节点的行为：

### Human Message Template（用户消息模板） <a href="#human-message-template" id="human-message-template"></a>

输入 n8n 在每个步骤执行时发送给智能体的消息。

可用的 LangChain 表达式：

* `{previous_steps}`：包含智能体已完成的先前步骤的信息。
* `{current_step}`：包含当前步骤的信息。
* `{agent_scratchpad}`：需要为下一次迭代记住的信息。

### Tracing Metadata（追踪元数据） <a href="#tracing-metadata" id="tracing-metadata"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/tracing-metadata.md" %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

请参阅 AI Agent 主节点的[模板与示例](README.md#templates-and-examples)部分。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见问题及建议的解决办法，请参阅[常见问题](common-issues.md)。


