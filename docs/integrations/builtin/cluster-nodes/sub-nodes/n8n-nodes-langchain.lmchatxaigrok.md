---
title: xAI Grok Chat Model（xAI Grok 聊天模型） 节点文档
description: 了解如何在 n8n 中使用 xAI Grok Chat Model（xAI Grok 聊天模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: xAI Grok Chat Model（xAI Grok 聊天模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatxaigrok.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatxaigrok
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatxaigrok
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# xAI Grok Chat Model（xAI Grok 聊天模型） 节点 <a href="#xai-grok-chat-model-node" id="xai-grok-chat-model-node"></a>

使用 xAI Grok Chat Model 节点，访问 xAI Grok 的大型语言模型，执行对话式 AI 和文本生成任务。

本页列出了 xAI Grok Chat Model 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [xAI 凭据文档](../../credentials/xai.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**（模型）：选择生成补全的模型。n8n 从 xAI Grok API 动态加载可用模型。更多信息请参阅 [xAI Grok 模型文档](https://docs.x.ai/docs/models)。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Frequency Penalty**（频率惩罚）：控制模型重复自身内容的可能性。值越高，重复的可能性越低。
* **Maximum Number of Tokens**（最大 token 数）：输入使用的 token 数量上限，以设置补全长度。大多数模型的上下文长度为 2048 token，最新模型支持最多 32,768 token。
* **Response Format**（响应格式）：选择 **Text**（文本）或 **JSON**。**JSON** 确保模型返回有效 JSON。
* **Presence Penalty**（存在惩罚）：控制模型谈论新话题的可能性。值越高，谈论新话题的可能性越高。
* **Sampling Temperature**（采样温度）：控制采样过程的随机性。温度越高，采样结果越多样，但产生幻觉的风险也越高。
* **Timeout**（超时）：输入请求的最长耗时，单位为毫秒。
* **Max Retries**（最大重试次数）：输入请求的最大重试次数。
* **Top P**：设置补全使用的概率范围。较低值会忽略概率较低的选项。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 xAI Grok Chat Model（xAI Grok 聊天模型） 集成模板](https://n8n.io/integrations/xai-grok-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [xAI Grok API 文档](https://docs.x.ai/docs/api-reference)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

