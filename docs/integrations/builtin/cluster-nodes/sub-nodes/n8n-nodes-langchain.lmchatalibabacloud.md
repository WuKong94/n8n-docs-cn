---
title: Qwen Cloud Chat Model（通义千问云聊天模型） 节点文档
contentType:
- integration
- reference
nodeTitle: Qwen Cloud Chat Model（通义千问云聊天模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud
description: Qwen Cloud Chat Model 节点将提示词发送到 Qwen Cloud 的对话模型，用于高级 AI 链。本页介绍节点配置及常见用途。
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


# Qwen Cloud Chat Model（通义千问云聊天模型） <a id="qwen-cloud-chat-model"></a>

{% hint style="info" %}
在 n8n Cloud 上，可使用 [Gateway 额度](../../../../deploy/use-n8n-cloud/gateway-credits/README.md)运行 Qwen Cloud Chat Model 节点，无需自己的 Qwen Cloud API 密钥。在节点的凭据字段选择 **Use Gateway credits**（使用 Gateway 额度），即可在没有 Qwen Cloud 账户的情况下运行节点。
{% endhint %}

Qwen Cloud Chat Model 节点将聊天提示词发送到 Qwen Cloud 的对话模型，用于高级 AI 链和 LangChain 集成。可用它生成对话响应、将模型输出集成到工作流，或使用自定义采样、重试和超时设置运行提示词。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Qwen Cloud 凭据文档](../../credentials/alibaba.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 操作 <a href="#operations" id="operations"></a>

### 生成聊天响应 <a href="#generate-chat-response" id="generate-chat-response"></a>

使用所选 Qwen Cloud 模型生成聊天式响应。

**参数**

* **Model**（模型，类型：_options_，字段：`model`）：生成补全的模型。可用模型的更多信息，请参阅 Qwen Cloud 的[选择模型](https://docs.qwencloud.com/developer-guides/getting-started/model-selection)。

**选项**

* **Frequency Penalty**（频率惩罚，类型：_number_，字段：`frequencyPenalty`）：正值根据新 token 已出现的频率施加惩罚，降低模型逐字重复同一行的可能性。默认值：`0`。
* **Maximum Number of Tokens**（最大 token 数，类型：_number_，字段：`maxTokens`）：补全中生成的最大 token 数，限制取决于所选模型。负一表示使用模型的默认上限。默认值：`-1`。
* **Response Format**（响应格式，类型：_options_，字段：`responseFormat`）：节点返回的输出格式，例如纯文本或结构化格式。默认为 text。
* **Presence Penalty**（存在惩罚，类型：_number_，字段：`presencePenalty`）：正值根据新 token 是否已在文本中出现施加惩罚，增加模型讨论新话题的可能性。默认值：`0`。
* **Sampling Temperature**（采样温度，类型：_number_，字段：`temperature`）：控制随机性。较低值使输出更少随机，接近零时趋于确定。默认值：`0.7`。
* **Timeout**（超时，类型：_number_，字段：`timeout`）：请求允许的最长时间，单位为毫秒，超过后中止请求。默认值：`360000`。
* **Max Retries**（最大重试次数，类型：_number_，字段：`maxRetries`）：失败请求的最大重试次数。默认值：`2`。
* **Top P**（类型：_number_，字段：`topP`）：控制多样性的核采样参数。0.5 表示考虑一半的概率质量。调整 **Top P** 或 **Sampling Temperature**（采样温度）之一即可，不要同时调整两者。默认值：`1`。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Qwen Cloud Chat Model（通义千问云聊天模型） 集成模板](https://n8n.io/integrations/alibaba-cloud-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

可用模型及其能力的更多信息，请参阅[选择模型](https://docs.qwencloud.com/developer-guides/getting-started/model-selection)。
