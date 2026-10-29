---
title: MiniMax Chat Model（MiniMax 聊天模型） 节点文档
description: 了解如何在 n8n 中使用 MiniMax Chat Model（MiniMax 聊天模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: MiniMax Chat Model（MiniMax 聊天模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MiniMax Chat Model（MiniMax 聊天模型） 节点 <a href="#minimax-chat-model-node" id="minimax-chat-model-node"></a>

{% hint style="info" %}
在 n8n Cloud 上，可使用 [Gateway 额度](../../../../deploy/use-n8n-cloud/gateway-credits/README.md)运行 MiniMax Chat Model 节点，无需自己的 MiniMax API 密钥。在节点的凭据字段选择 **Use Gateway credits**（使用 Gateway 额度），即可在没有 MiniMax 账户的情况下运行节点。
{% endhint %}

使用 MiniMax Chat Model 节点，将 MiniMax 聊天模型与对话智能体[^1]配合使用。

本页列出了 MiniMax Chat Model 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [MiniMax 凭据文档](../../credentials/minimax.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**（模型）：选择生成补全的模型。可用模型请参阅 [MiniMax 模型文档](https://platform.minimax.io/docs/guides/models-intro)。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Hide Thinking**（隐藏思考）：开启时（默认），节点会从模型响应中移除 `<think>` 标签。关闭此项可在输出中包含模型推理。
* **Maximum Number of Tokens**（最大 token 数）：输入使用的 token 数量上限，以设置补全长度。
* **Sampling Temperature**（采样温度）：控制采样过程的随机性。温度越高，采样结果越多样，但产生幻觉的风险也越高。
* **Timeout**（超时）：输入请求的最长耗时，单位为毫秒。
* **Max Retries**（最大重试次数）：输入请求的最大重试次数。
* **Top P**：设置补全使用的概率范围。较低值会忽略概率较低的选项。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 MiniMax Chat Model（MiniMax 聊天模型） 集成模板](https://n8n.io/integrations/minimax-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [MiniMax 文档](https://platform.minimax.io/docs/guides/models-intro)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大型语言模型（LLM）理解用户输入，并根据可用的信息和资源，决定如何最好地处理请求。
