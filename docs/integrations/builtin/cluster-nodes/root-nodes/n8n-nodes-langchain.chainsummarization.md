---
title: Summarization Chain（摘要链） 节点文档
description: 了解如何在 n8n 中使用 Summarize Chain 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: Summarization Chain（摘要链） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Summarization Chain（摘要链） 节点 <a href="#summarization-chain-node" id="summarization-chain-node"></a>

使用 Summarization Chain 节点，为多个文档生成摘要。

本页列出了 Summarization Chain 节点的参数，并提供更多资源的链接。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

在 **Data to Summarize**（要生成摘要的数据）中选择数据类型。所选数据类型决定其他节点参数。

* **Use Node Input (JSON)**（使用节点输入，JSON）和 **Use Node Input (Binary)**（使用节点输入，二进制）：对工作流中传入节点的数据生成摘要。
    * 可配置 **Chunking Strategy**（分块策略），选择定义数据块大小的策略。
        * 选择 **Simple (Define Below)**（简单，在下方定义）后，可设置 **Characters Per Chunk**（每块字符数）和 **Chunk Overlap (Characters)**（块重叠字符数）。
        * 如需连接提供更多配置选项的拆分器子节点，请选择 **Advanced**（高级）。
* **Use Document Loader**（使用文档加载器）：对文档加载器子节点提供的数据生成摘要。

## 节点选项 <a href="#node-options" id="node-options"></a>

可配置摘要生成方法和提示词。选择 **Add Option**（添加选项）> **Summarization Method and Prompts**（摘要生成方法与提示词）。

**Summarization Method**（摘要生成方法）选项：

* **Map Reduce**：分别对每个块生成摘要，再合并这些摘要。这是推荐选项。
* **Refine**（逐步完善）：先为第一个块生成摘要，再依次使用后续各块更新摘要。
* **Stuff**（全部填入）：在一个提示词中将全部文本发送给模型。适用于能容纳在模型上下文窗口中的短文本。

可自定义 **Individual Summary Prompts**（单独摘要提示词）和 **Final Prompt to Combine**（最终合并提示词）。节点内提供了示例。必须包含 `"{text}"` 占位符。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Summarization Chain（摘要链） 集成模板](https://n8n.io/integrations/summarization-chain)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

