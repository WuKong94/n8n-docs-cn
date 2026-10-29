---
title: Anthropic Chat Model（Anthropic 聊天模型） 节点文档
description: 了解如何在 n8n 中使用 Anthropic Chat Model（Anthropic 聊天模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Anthropic Chat Model（Anthropic 聊天模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Anthropic Chat Model（Anthropic 聊天模型） 节点 <a href="#anthropic-chat-model-node" id="anthropic-chat-model-node"></a>

{% hint style="info" %}
在 n8n Cloud 上，可使用 [Gateway 额度](../../../../deploy/use-n8n-cloud/gateway-credits/README.md)运行 Anthropic Chat Model 节点，无需自己的 Anthropic API 密钥。在节点的凭据字段选择 **Use Gateway credits**（使用 Gateway 额度），即可在没有 Anthropic 账户的情况下运行节点。
{% endhint %}

使用 Anthropic Chat Model 节点，将 Anthropic 的 Claude 系列聊天模型与对话智能体[^1]配合使用。

本页列出了 Anthropic Chat Model 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Anthropic 凭据文档](../../credentials/anthropic.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**（模型）：选择用于生成补全的模型，可选：
    * **Claude**（Claude 模型）
    * **Claude Instant**（Claude Instant 模型）

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Maximum Number of Tokens**（最大 token 数）：输入使用的 token 数量上限，以设置补全长度。
* **Sampling Temperature**（采样温度）：控制采样过程的随机性。温度越高，采样结果越多样，但产生幻觉的风险也越高。
* **Top K**：输入模型生成下一个 token 时考虑的候选 token 数量。
* **Top P**：设置补全使用的概率范围。较低值会忽略概率较低的选项。
* **Prompt Caching**（提示词缓存）：通过 [Anthropic 提示词缓存](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)，在请求间缓存系统提示词、工具定义和对话历史。可选择 **Disabled**（禁用，默认）、**5 Minutes**（5 分钟）或 **1 Hour**（1 小时），决定缓存内容在需要重新写入前的有效时长。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Anthropic Chat Model（Anthropic 聊天模型） 集成模板](https://n8n.io/integrations/anthropic-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 的 Anthropic 文档](https://docs.langchain.com/oss/javascript/integrations/chat/anthropic)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大型语言模型（LLM）理解用户输入，并根据可用的信息和资源，决定如何最好地处理请求。
