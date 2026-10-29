---
title: Mistral Cloud Chat Model（Mistral Cloud 聊天模型） 节点文档
description: 了解如何在 n8n 中使用 Mistral Cloud Chat Model（Mistral Cloud 聊天模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Mistral Cloud Chat Model（Mistral Cloud 聊天模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Mistral Cloud Chat Model（Mistral Cloud 聊天模型） 节点 <a href="#mistral-cloud-chat-model-node" id="mistral-cloud-chat-model-node"></a>

使用 Mistral Cloud Chat Model 节点，将 Mistral Cloud 聊天模型与对话智能体[^1]配合使用。

本页列出了 Mistral Cloud Chat Model 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Mistral Cloud 凭据文档](../../credentials/mistral.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**（模型）：选择用于生成补全的模型。n8n 从 Mistral Cloud 动态加载模型，你只会看到自己的账户可用的模型。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Maximum Number of Tokens**（最大 token 数）：输入使用的 token 数量上限，以设置补全长度。
* **Sampling Temperature**（采样温度）：控制采样过程的随机性。温度越高，采样结果越多样，但产生幻觉的风险也越高。
* **Timeout**（超时）：输入请求的最长耗时，单位为毫秒。
* **Max Retries**（最大重试次数）：输入请求的最大重试次数。
* **Top P**：设置补全使用的概率范围。较低值会忽略概率较低的选项。
* **Enable Safe Mode**（启用安全模式）：在补全开头注入安全提示词以启用安全模式，有助于防止模型生成冒犯性内容。
* **Random Seed**（随机种子）：输入随机采样的种子。设置后，不同调用会生成确定性结果。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Mistral Cloud Chat Model（Mistral Cloud 聊天模型） 集成模板](https://n8n.io/integrations/mistral-cloud-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 的 Mistral 文档](https://docs.langchain.com/oss/javascript/integrations/chat/mistral)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大型语言模型（LLM）理解用户输入，并根据可用的信息和资源，决定如何最好地处理请求。
