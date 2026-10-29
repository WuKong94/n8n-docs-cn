---
title: Workflow Retriever（工作流检索器） 节点文档
description: 了解如何在 n8n 中使用 Workflow Retriever（工作流检索器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Workflow Retriever（工作流检索器） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Workflow Retriever（工作流检索器） 节点 <a href="#workflow-retriever-node" id="workflow-retriever-node"></a>

使用 Workflow Retriever 节点，从 n8n 工作流中检索数据，供 Retrieval QA Chain（检索问答链）或其他检索器节点使用。

本页列出了 Workflow Retriever 节点的参数，并提供更多资源的链接。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

### Source（来源） <a href="#source" id="source"></a>

指定 n8n 要调用的工作流，可选择以下任一方式：

* **Database**（数据库），并输入工作流 ID。
* **Parameter**（参数），并复制完整的[工作流 JSON](../../../../build/manage-workflows/export-and-import.md)。

### 工作流值 <a href="#workflow-values" id="workflow-values"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-sub-nodes/workflow-values.md" %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Workflow Retriever（工作流检索器） 集成模板](https://n8n.io/integrations/workflow-retriever)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 检索器文档](https://docs.langchain.com/oss/javascript/integrations/retrievers)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

