---
title: Lemonade Model（Lemonade 模型） 节点文档
description: 了解如何在 n8n 中使用 Lemonade Model（Lemonade 模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Lemonade Model（Lemonade 模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Lemonade Model（Lemonade 模型） 节点 <a href="#lemonade-model-node" id="lemonade-model-node"></a>

使用 Lemonade Model 节点，通过 Lemonade 服务器托管和管理的语言模型生成文本补全。此节点是兼容 LangChain 的简单语言模型子节点，适用于 n8n 工作流中的文本补全任务。

本页列出了 Lemonade Model 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Lemonade 凭据文档](../../credentials/lemonade.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置节点。

### Model（模型） <a href="#model" id="model"></a>

生成补全的模型。模型通过 Lemonade 服务器加载和管理，请从节点提供的列表选择所需模型。

## 节点选项 <a href="#node-options" id="node-options"></a>

使用以下选项进一步调整节点行为。

### Sampling Temperature（采样温度） <a href="#sampling-temperature" id="sampling-temperature"></a>

控制生成文本的随机性。较低值使输出更集中、更确定，较高值使输出更多样、更随机。

| 属性 | 值 |
|----------|-------|
| 类型 | number（数字） |
| 必填 | 否 |
| 默认值 | 0.7 |

### Top P <a href="#top-p" id="top-p"></a>

控制模型生成文本时可选择的词。较低值会逐步排除最不可能的选项，使模型只能从较小、置信度较高的候选集中选择。

| 属性 | 值 |
|----------|-------|
| 类型 | number（数字） |
| 必填 | 否 |
| 默认值 | 1 |

### Frequency Penalty（频率惩罚） <a href="#frequency-penalty" id="frequency-penalty"></a>

调整对生成文本中已出现 token 的惩罚。正值减少重复，负值鼓励重复。

| 属性 | 值 |
|----------|-------|
| 类型 | number（数字） |
| 必填 | 否 |
| 默认值 | 0 |

### Presence Penalty（存在惩罚） <a href="#presence-penalty" id="presence-penalty"></a>

根据 token 是否已在生成文本中出现来调整惩罚。正值惩罚已出现的 token，鼓励多样性。

| 属性 | 值 |
|----------|-------|
| 类型 | number（数字） |
| 必填 | 否 |
| 默认值 | 0 |

### Max Tokens to Generate（生成 token 上限） <a href="#max-tokens-to-generate" id="max-tokens-to-generate"></a>

要生成的最大 token 数，设为 -1 表示不限制。设置较大值时请谨慎，因为可能产生非常长的输出。

| 属性 | 值 |
|----------|-------|
| 类型 | number（数字） |
| 必填 | 否 |
| 默认值 | -1 |

### Stop Sequences（停止序列） <a href="#stop-sequences" id="stop-sequences"></a>

以逗号分隔的序列列表，模型遇到其中的序列时停止生成文本。

| 属性 | 值 |
|----------|-------|
| 类型 | string（字符串） |
| 必填 | 否 |
| 默认值 | "" |

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Lemonade Model（Lemonade 模型） 集成模板](https://n8n.io/integrations/lemonade-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Lemonade Server 文档](https://lemonade-server.ai/docs/)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

