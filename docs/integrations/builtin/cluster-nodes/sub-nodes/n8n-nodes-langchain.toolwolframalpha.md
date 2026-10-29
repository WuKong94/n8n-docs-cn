---
title: Wolfram|Alpha tool（Wolfram|Alpha 工具） 节点文档
description: 了解如何在 n8n 中使用 Wolfram|Alpha tool（Wolfram|Alpha 工具） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Wolfram|Alpha tool（Wolfram|Alpha 工具） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Wolfram|Alpha tool（Wolfram|Alpha 工具） 节点 <a href="#wolframoralpha-tool-node" id="wolframoralpha-tool-node"></a>

使用 Wolfram|Alpha tool 节点，将智能体[^1]和链[^2]连接到 Wolfram|Alpha 的计算智能引擎。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Wolfram|Alpha 凭据文档](../../credentials/wolframalpha.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Wolfram|Alpha tool（Wolfram|Alpha 工具） 集成模板](https://n8n.io/integrations/wolframoralpha)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Wolfram|Alpha 文档](https://products.wolframalpha.com/api)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大型语言模型（LLM）理解用户输入，并根据可用的信息和资源，决定如何最好地处理请求。
[^2]: AI 链通过一系列组件调用，让你与大型语言模型（LLM）及其他资源交互。n8n 中的 AI 链不使用持久记忆，因此不能用它们引用之前的上下文；此类需求请使用 AI 智能体。
