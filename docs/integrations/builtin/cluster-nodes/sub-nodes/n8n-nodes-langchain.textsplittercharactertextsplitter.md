---
title: Character Text Splitter（字符文本拆分器） 节点文档
description: 了解如何在 n8n 中使用 Character Text Splitter（字符文本拆分器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Character Text Splitter（字符文本拆分器） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittercharactertextsplitter.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittercharactertextsplitter
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittercharactertextsplitter
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Character Text Splitter（字符文本拆分器） 节点 <a href="#character-text-splitter-node" id="character-text-splitter-node"></a>

使用 Character Text Splitter 节点，按字符拆分文档数据。

本页列出了 Character Text Splitter 节点的参数，并提供更多资源的链接。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Separator**（分隔符）：选择用于将文档拆成独立数据项的分隔符。
* **Chunk Size**（块大小）：输入每个块的字符数。
* **Chunk Overlap**（块重叠量）：输入相邻块之间的重叠量。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Character Text Splitter（字符文本拆分器） 集成模板](https://n8n.io/integrations/character-text-splitter)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 文本拆分器文档](https://docs.langchain.com/oss/javascript/integrations/splitters)和 [LangChain 字符文本拆分 API 文档](https://reference.langchain.com/javascript/langchain-textsplitters/CharacterTextSplitter)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

