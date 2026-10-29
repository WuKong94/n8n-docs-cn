---
title: Structured Output Parser 节点常见问题
contentType:
- integration
- reference
priority: high
nodeTitle: Structured Output Parser 节点常见问题
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues
description: 工作流自动化平台 n8n 中 Structured Output Parser 节点的常见错误和问题，包括问题详情及建议的解决办法。
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
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 常见问题 <a id="common-issues"></a>

以下列出 [Structured Output Parser 节点](./README.md)的常见错误和问题，以及解决或排查步骤。

## 参数处理 <a href="#processing-parameters" id="processing-parameters"></a>

Structured Output Parser 是子节点[^1]。使用表达式处理多个数据项时，子节点的行为与其他节点不同。

多数节点，包括[根节点](#user-content-fn-2)[^2]，可以接收任意数量的输入数据项，处理后输出结果。你可以用表达式引用输入数据项，节点会依次对每个数据项解析表达式。例如，输入包含五个名称值时，表达式 `{{ $json.name }}` 会依次解析为每个名称。

在子节点中，表达式始终解析为第一个数据项。例如，输入包含五个名称值时，表达式 `{{ $json.name }}` 始终解析为第一个名称。

## 将结构化输出解析器添加到 AI 节点 <a href="#adding-the-structured-output-parser-node-to-ai-nodes" id="adding-the-structured-output-parser-node-to-ai-nodes"></a>

可将输出解析器节点连接到部分 [AI 根节点](../../root-nodes/README.md)。

要为节点添加 Structured Output Parser，请在需要格式化输出的 AI 根节点中启用 **Require Specific Output Format**（要求指定输出格式）。启用后，会显示新的 **output parser**（输出解析器）连接点。点击该连接点，添加 Structured Output Parser 节点。

## 使用结构化输出解析器格式化中间步骤 <a href="#using-the-structured-output-parser-to-format-intermediary-steps" id="using-the-structured-output-parser-to-format-intermediary-steps"></a>

Structured Output Parser 节点用于结构化 AI 智能体的最终输出，不用于结构化传给其他 AI 工具或阶段的中间输出。

要指定中间输出的格式，请在 **AI Agent**（AI 智能体）的 **System Message**（系统消息）中包含响应结构。消息可包含架构或示例响应，供智能体作为生成结果的模板。

## 结构化智能体的输出 <a href="#structuring-output-from-agents" id="structuring-output-from-agents"></a>

与[智能体](../../root-nodes/n8n-nodes-langchain.agent/README.md)配合时，结构化输出解析通常不够可靠。

如果工作流使用智能体，n8n 建议使用单独的 [LLM 链](../../root-nodes/n8n-nodes-langchain.chainllm.md)接收智能体的数据并进行解析。与直接在智能体工作流中解析相比，这通常能获得更好、更一致的结果。

[^1]: n8n 集群节点由连接到根节点的一个或多个子节点组成。子节点通过访问特定服务或资源，或提供特定类型的专用处理（例如计算器功能），扩展根节点的功能。
<a id="user-content-fn-2"></a>
[^2]: 每个 n8n 集群节点都包含一个根节点，用于定义集群的主要功能。一个或多个子节点连接到根节点，以扩展其功能。
