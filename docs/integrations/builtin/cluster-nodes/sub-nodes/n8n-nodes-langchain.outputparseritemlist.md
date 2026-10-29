---
title: Item List Output Parser（数据项列表输出解析器） 节点文档
description: 了解如何在 n8n 中使用 Item List Output Parser（数据项列表输出解析器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: Item List Output Parser（数据项列表输出解析器） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Item List Output Parser（数据项列表输出解析器） 节点 <a href="#item-list-output-parser-node" id="item-list-output-parser-node"></a>

使用 Item List Output Parser 节点，返回具有指定长度和分隔符的数据项列表。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Number of Items**（数据项数量）：输入要返回的最大数据项数量，设为 `-1` 表示不限制。
* **Separator**（分隔符）：选择用于将结果拆成独立数据项的分隔符，默认为换行符。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Item List Output Parser（数据项列表输出解析器） 集成模板](https://n8n.io/integrations/item-list-output-parser)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 结构化输出文档](https://docs.langchain.com/oss/javascript/langchain/structured-output)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

