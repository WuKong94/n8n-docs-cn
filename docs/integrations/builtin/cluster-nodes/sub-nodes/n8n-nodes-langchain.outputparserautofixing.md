---
title: Auto-fixing Output Parser（自动修复输出解析器） 节点文档
description: 了解如何在 n8n 中使用 Auto-fixing Output Parser（自动修复输出解析器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Auto-fixing Output Parser（自动修复输出解析器） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Auto-fixing Output Parser（自动修复输出解析器） 节点 <a href="#auto-fixing-output-parser-node" id="auto-fixing-output-parser-node"></a>

Auto-fixing Output Parser 节点封装另一个输出解析器。如果被封装的解析器失败，它会调用另一个 LLM 来修复错误。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Auto-fixing Output Parser（自动修复输出解析器） 集成模板](https://n8n.io/integrations/auto-fixing-output-parser)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 结构化输出文档](https://docs.langchain.com/oss/javascript/langchain/structured-output)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

