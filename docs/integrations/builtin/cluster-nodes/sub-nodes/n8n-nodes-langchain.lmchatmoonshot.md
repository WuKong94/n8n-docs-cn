---
title: Moonshot Kimi Chat Model 节点
contentType:
- integration
- reference
nodeTitle: Moonshot Kimi Chat Model 节点
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmoonshot.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmoonshot
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmoonshot
description: 将 Moonshot Kimi Chat Model 集成到 n8n 工作流，为 AI 链生成聊天响应，包括生成对话回复和集成 LangChain
  风格工作流。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Moonshot Kimi Chat Model（月之暗面 Kimi 聊天模型）节点 <a id="moonshot-kimi-chat-model-node"></a>

{% hint style="info" %}
在 n8n Cloud 上，可使用 [Gateway 额度](../../../../deploy/use-n8n-cloud/gateway-credits/README.md)运行 Moonshot Kimi Chat Model 节点，无需自己的 Moonshot API 密钥。在节点的凭据字段选择 **Use Gateway credits**（使用 Gateway 额度），即可在没有 Moonshot 账户的情况下运行节点。
{% endhint %}

使用 Moonshot Kimi Chat Model 节点，向 Kimi 聊天 API 发送请求并生成对话响应。需要在工作流中使用 AI 聊天模型时，可用此节点驱动助手、构建多步骤 AI 链，或通过可调整的采样和 token 设置生成模型内容。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Moonshot 凭据文档](../../credentials/moonshot.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 操作 <a href="#operations" id="operations"></a>

### 生成聊天响应 <a href="#generate-chat-response" id="generate-chat-response"></a>

向所选 Kimi 模型发送聊天请求，并返回模型响应。

**参数**

* **Model**（模型，类型：options，字段：`model`）：生成补全的模型，默认为 `kimi-k2.5`。更多信息请参阅 [Moonshot Kimi Chat API 文档](https://platform.kimi.ai/docs/api/chat)。

**选项**

* **Frequency Penalty**（频率惩罚，类型：number，字段：`frequencyPenalty`）：正值根据新 token 已出现的频率施加惩罚，减少模型重复。默认值：`0`。
* **Maximum number of tokens**（最大 token 数，类型：number，字段：`maxTokens`）：补全中生成的最大 token 数。-1 表示使用模型默认值，token 上限取决于所选模型。默认值：`-1`。
* **Response format**（响应格式，类型：options，字段：`responseFormat`）：模型响应格式，默认为 `text`。
* **Presence penalty**（存在惩罚，类型：number，字段：`presencePenalty`）：正值根据新 token 是否已在文本中出现施加惩罚，增加模型讨论新话题的可能性。默认值：`0`。
* **Sampling temperature**（采样温度，类型：number，字段：`temperature`）：控制随机性。较低值使输出更少随机，接近零时模型趋于确定。默认值：`0.7`。
* **Timeout**（超时，类型：number，字段：`timeout`）：请求的最长耗时，单位为毫秒，默认为 360000（六分钟）。
* **Max retries**（最大重试次数，类型：number，字段：`maxRetries`）：失败请求的最大重试次数，默认为两次。
* **Top P**（类型：number，字段：`topP`）：控制多样性的核采样参数。0.5 表示模型考虑按可能性加权的一半候选选项。建议仅调整 **Top P** 或 **Sampling Temperature**（采样温度）之一，不要同时调整。默认值：`1`。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Moonshot Kimi Chat Model（月之暗面 Kimi 聊天模型）集成模板](https://n8n.io/integrations/moonshot-kimi-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务及可用模型选项的更多信息，请参阅 [Moonshot Kimi Chat Model 文档](https://platform.kimi.ai/docs/api/chat)。
