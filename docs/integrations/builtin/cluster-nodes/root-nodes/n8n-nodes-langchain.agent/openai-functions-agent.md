---
title: OpenAI Functions Agent（OpenAI 函数智能体） 节点文档
contentType:
- integration
- reference
priority: critical
nodeTitle: OpenAI Functions Agent（OpenAI 函数智能体） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent
description: 了解如何在 n8n 的 AI Agent 节点中使用 OpenAI Functions Agent，并按照技术文档将其集成到工作流中。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
tags:
- tag: deprecated
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# OpenAI Functions Agent（OpenAI 函数智能体） <a id="openai-functions-agent"></a>

{% hint style="warning" %}
**功能可用性**

OpenAI Functions Agent 从 n8n 1.82.0 起弃用。新增或更新的 AI Agent 节点改用 [Tools Agent](tools-agent.md)。只有仍使用 AI Agent 节点版本 1 的工作流可选择 OpenAI Functions Agent。

AI Agent 节点版本 1 从 n8n 3.0 中移除，因此 OpenAI Functions Agent 将在所有工作流中停止工作。详情请参阅 [n8n 3.0 破坏性变更](../../../../../changelog/v30-breaking-changes.md)。
{% endhint %}

使用 OpenAI Functions Agent 节点，调用 [OpenAI 函数模型](https://platform.openai.com/docs/guides/function-calling)。这类模型会判断何时应调用函数，并返回应该传给函数的输入。

AI Agent 节点本身的更多信息，请参阅 [AI Agent](./README.md)。

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/use-with-chat-trigger.md" %}

{% hint style="info" %}
**需要 OpenAI Chat Model**

必须将此智能体与 [OpenAI Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatopenai/README.md) 配合使用。
{% endhint %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置 OpenAI Functions Agent。

### Prompt（提示词） <a href="#prompt" id="prompt"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/prompt.md" %}

### Require Specific Output Format（要求指定输出格式） <a href="#require-specific-output-format" id="require-specific-output-format"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/output-format.md" %}

## 节点选项 <a href="#node-options" id="node-options"></a>

使用以下选项调整 OpenAI Functions Agent 节点的行为：

### System Message（系统消息） <a href="#system-message" id="system-message"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/system-message.md" %}

### Max Iterations（最大迭代次数） <a href="#max-iterations" id="max-iterations"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/max-iterations.md" %}

### Return Intermediate Steps（返回中间步骤） <a href="#return-intermediate-steps" id="return-intermediate-steps"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/return-intermediate-steps.md" %}

### Tracing Metadata（追踪元数据） <a href="#tracing-metadata" id="tracing-metadata"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/tracing-metadata.md" %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

请参阅 AI Agent 主节点的[模板与示例](./README.md#templates-and-examples)部分。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见问题及建议的解决办法，请参阅[常见问题](common-issues.md)。
