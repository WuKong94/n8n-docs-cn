---
title: Vector Store Retriever（向量存储检索器） 节点文档
description: 了解如何在 n8n 中使用 Vector Store Retriever（向量存储检索器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Vector Store Retriever（向量存储检索器） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Vector Store Retriever（向量存储检索器） 节点 <a href="#vector-store-retriever-node" id="vector-store-retriever-node"></a>

使用 Vector Store Retriever 节点，从[向量存储](#user-content-fn-1)[^1]检索文档。

本页列出了 Vector Store Retriever 节点的参数，并提供更多资源的链接。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Limit**（上限）：输入返回结果的最大数量。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Vector Store Retriever（向量存储检索器） 集成模板](https://n8n.io/integrations/vector-store-retriever)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 语义搜索教程](https://docs.langchain.com/oss/javascript/langchain/knowledge-base)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

<a id="user-content-fn-1"></a>
[^1]: 向量存储或向量数据库用于存储信息的数学表示。将其与嵌入模型和检索器配合使用，可创建供 AI 在回答问题时访问的数据库。
