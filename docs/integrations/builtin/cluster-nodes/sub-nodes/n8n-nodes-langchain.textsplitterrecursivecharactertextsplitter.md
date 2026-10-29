---
title: Recursive Character Text Splitter（递归字符文本拆分器） 节点文档
description: 了解如何在 n8n 中使用 Recursive Character Text Splitter（递归字符文本拆分器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Recursive Character Text Splitter（递归字符文本拆分器） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Recursive Character Text Splitter（递归字符文本拆分器） 节点 <a href="#recursive-character-text-splitter-node" id="recursive-character-text-splitter-node"></a>

Recursive Character Text Splitter 节点递归拆分文档数据，尽可能保持段落完整，其次是句子，再其次是单词。

本页列出了 Recursive Character Text Splitter 节点的参数，并提供更多资源的链接。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Chunk Size**（块大小）：输入每个块的字符数。
* **Chunk Overlap**（块重叠量）：输入相邻块之间的重叠量。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Recursive Character Text Splitter（递归字符文本拆分器） 集成模板](https://n8n.io/integrations/recursive-character-text-splitter)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 文本拆分器文档](https://docs.langchain.com/oss/javascript/integrations/splitters)和 [LangChain 按字符递归拆分文档](https://reference.langchain.com/javascript/langchain-textsplitters/RecursiveCharacterTextSplitter)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

