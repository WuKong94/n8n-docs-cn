---
title: Contextual Compression Retriever（上下文压缩检索器） 节点文档
description: 了解如何在 n8n 中使用 Contextual Compression Retriever（上下文压缩检索器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Contextual Compression Retriever（上下文压缩检索器） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Contextual Compression Retriever（上下文压缩检索器） 节点 <a href="#contextual-compression-retriever-node" id="contextual-compression-retriever-node"></a>

Contextual Compression Retriever 节点利用查询上下文，改进[向量存储](#user-content-fn-1)[^1]文档相似度搜索返回的答案。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Contextual Compression Retriever（上下文压缩检索器） 集成模板](https://n8n.io/integrations/contextual-compression-retriever)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

<a id="user-content-fn-1"></a>
[^1]: 向量存储或向量数据库用于存储信息的数学表示。将其与嵌入模型和检索器配合使用，可创建供 AI 在回答问题时访问的数据库。
