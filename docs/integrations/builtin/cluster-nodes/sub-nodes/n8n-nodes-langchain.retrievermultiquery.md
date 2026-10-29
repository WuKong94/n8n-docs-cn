---
title: MultiQuery Retriever（多查询检索器） 节点文档
description: 了解如何在 n8n 中使用 MultiQuery Retriever（多查询检索器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: MultiQuery Retriever（多查询检索器） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievermultiquery.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievermultiquery
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievermultiquery
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MultiQuery Retriever（多查询检索器） 节点 <a href="#multiquery-retriever-node" id="multiquery-retriever-node"></a>

MultiQuery Retriever 节点使用 LLM，针对给定的用户输入查询，从不同角度生成多个查询，从而自动完成提示词调优过程。

本页列出了 MultiQuery Retriever 节点的参数，并提供更多资源的链接。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Query Count**（查询数量）：输入要生成的不同查询版本数量。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 MultiQuery Retriever（多查询检索器） 集成模板](https://n8n.io/integrations/multiquery-retriever)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 检索器文档](https://docs.langchain.com/oss/javascript/integrations/retrievers)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

