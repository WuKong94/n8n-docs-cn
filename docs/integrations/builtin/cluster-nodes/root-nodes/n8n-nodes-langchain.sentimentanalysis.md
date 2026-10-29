---
title: Sentiment Analysis（情感分析） 节点文档
description: 了解如何在 n8n 中使用 Sentiment Analysis（情感分析） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Sentiment Analysis（情感分析） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Sentiment Analysis（情感分析） 节点 <a href="#sentiment-analysis-node" id="sentiment-analysis-node"></a>

使用 Sentiment Analysis 节点，分析传入文本数据的情感。

语言模型根据节点选项中的 [**Sentiment Categories**（情感类别）](#node-options)，判断每个数据项的情感。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Text to Analyze**（要分析的文本）：定义情感分析的输入文本，使用引用输入项字段的表达式。例如，输入来自聊天或消息源时，可使用
`{{ $json.chatInput }}`。默认情况下，节点期望使用 `text` 字段。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Sentiment Categories**（情感类别）：定义要将输入划分到的类别。
    * 默认类别为 `Positive, Neutral, Negative`。可根据具体场景自定义类别，例如使用 `Very Positive, Positive, Neutral, Negative, Very Negative` 进行更细致的分析。
* **Include Detailed Results**（包含详细结果）：开启时，输出包含情感强度和置信度分数。这些分数由语言模型估算生成，只能作为粗略参考，并非精确测量值。
* **System Prompt Template**（系统提示词模板）：修改情感分析使用的系统提示词，其中使用 `{categories}` 占位符表示类别。
* **Enable Auto-Fixing**（启用自动修复）：开启后，节点会将架构解析错误发送给 LLM，要求其修复模型输出，以符合预期格式。

## 使用说明 <a href="#usage-notes" id="usage-notes"></a>

### 模型温度设置 <a href="#model-temperature-setting" id="model-temperature-setting"></a>

强烈建议将所连接语言模型的温度设为 0 或接近 0 的值。这有助于尽可能提高结果的确定性，使多次运行的情感分析更加一致、可靠。

### 语言因素 <a href="#language-considerations" id="language-considerations"></a>

节点表现可能因输入文本的语言而异。

为获得最佳结果，请确保所选语言模型支持输入语言。

### 大批量处理 <a href="#processing-large-volumes" id="processing-large-volumes"></a>

分析大量文本时，可考虑将输入拆分为更小的块，优化处理时间和资源用量。

### 迭代优化 <a href="#iterative-refinement" id="iterative-refinement"></a>

对于复杂的情感分析任务，可能需要迭代调整系统提示词和类别，以获得所需结果。

## 使用示例 <a href="#example-usage" id="example-usage"></a>

### 基础情感分析 <a href="#basic-sentiment-analysis" id="basic-sentiment-analysis"></a>

1. 将数据源（例如 RSS Feed、HTTP Request）连接到 Sentiment Analysis 节点。
2. 将“Text to Analyze”（要分析的文本）字段设为相关数据项的属性（例如，博客文章内容可使用 `{{ $json.content }}`）。
3. 保留默认情感类别。
4. 将节点输出连接到不同路径，分别处理积极、中性和消极情感。

### 自定义类别分析 <a href="#custom-category-analysis" id="custom-category-analysis"></a>

1. 将 **Sentiment Categories**（情感类别）改为 `Excited, Happy, Neutral, Disappointed, Angry`。
2. 调整工作流，处理这五个输出类别。
3. 使用此配置，以更细致的情绪类别分析客户反馈。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

