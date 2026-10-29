---
title: NVIDIA Nemotron Chat Model（NVIDIA Nemotron 聊天模型） 节点文档
description: 了解如何在 n8n 中使用 NVIDIA Nemotron Chat Model（NVIDIA Nemotron 聊天模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: NVIDIA Nemotron Chat Model（NVIDIA Nemotron 聊天模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# NVIDIA Nemotron Chat Model（NVIDIA Nemotron 聊天模型） 节点 <a href="#nvidia-nemotron-chat-model-node" id="nvidia-nemotron-chat-model-node"></a>

使用 NVIDIA Nemotron Chat Model 节点，将 [NVIDIA Nemotron](https://build.nvidia.com/models) 模型与对话智能体[^1]配合使用。节点支持 [build.nvidia.com](https://build.nvidia.com/) 托管的 Nemotron 模型，以及自行托管的 NVIDIA Inference Microservices（NIM）。

本页列出了 NVIDIA Nemotron Chat Model 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [NVIDIA Nemotron 凭据文档](../../credentials/nvidia.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

### Model（模型） <a href="#model" id="model"></a>

选择用于生成补全的 Nemotron 模型。

n8n 从凭据配置的端点动态加载 Nemotron 模型。如果无法访问端点，会回退到经过整理的常见 Nemotron 模型 ID 列表。

## 节点选项 <a href="#node-options" id="node-options"></a>

使用以下选项进一步调整节点行为。

### Frequency Penalty（频率惩罚） <a href="#frequency-penalty" id="frequency-penalty"></a>

使用此选项控制模型重复自身内容的可能性。值越高，重复的可能性越低。

### Maximum Number of Tokens（最大 token 数） <a href="#maximum-number-of-tokens" id="maximum-number-of-tokens"></a>

输入使用的最大 token 数，以设置补全长度。使用 `-1` 表示模型默认值。

### Response Format（响应格式） <a href="#response-format" id="response-format"></a>

选择 **Text**（文本）或 **JSON**。**JSON** 确保模型返回有效 JSON。选择 **JSON** 时，请在链或智能体的提示词中包含 `json` 一词。

### Presence Penalty（存在惩罚） <a href="#presence-penalty" id="presence-penalty"></a>

使用此选项控制模型谈论新话题的可能性。值越高，谈论新话题的可能性越高。

### Sampling Temperature（采样温度） <a href="#sampling-temperature" id="sampling-temperature"></a>

使用此选项控制采样过程的随机性。温度越高，采样结果越多样，但产生幻觉的风险也越高。

### Timeout（超时） <a href="#timeout" id="timeout"></a>

输入请求的最长耗时，单位为毫秒。

### Max Retries（最大重试次数） <a href="#max-retries" id="max-retries"></a>

输入请求的最大重试次数。

### Top P <a href="#top-p" id="top-p"></a>

使用此选项设置补全使用的概率范围。较低值会忽略概率较低的选项。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 NVIDIA Nemotron Chat Model（NVIDIA Nemotron 聊天模型） 集成模板](https://n8n.io/integrations/nvidia-nemotron-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

Nemotron 模型列表请参阅 [NVIDIA 构建目录](https://build.nvidia.com/models)，自行托管指南请参阅 [NIM 文档](https://docs.nvidia.com/nim/)。NVIDIA API 与 OpenAI 规范兼容，底层客户端的更多信息可参阅 [LangChain 的 OpenAI 文档](https://docs.langchain.com/oss/javascript/integrations/chat/openai)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大型语言模型（LLM）理解用户输入，并根据可用的信息和资源，决定如何最好地处理请求。
