---
title: OpenAI Chat Model（OpenAI 聊天模型） 节点文档
contentType:
- integration
- reference
priority: high
nodeTitle: n8n-nodes-langchain.lmchatopenai
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai
description: 了解如何在 n8n 中使用 OpenAI Chat Model（OpenAI 聊天模型） 节点，并按照技术文档将其集成到工作流中。
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


# OpenAI Chat Model（OpenAI 聊天模型） <a id="openai-chat-model"></a>

{% hint style="info" %}
在 n8n Cloud 上，可使用 [Gateway 额度](../../../../../deploy/use-n8n-cloud/gateway-credits/README.md)运行 OpenAI Chat Model 节点，无需自己的 OpenAI API 密钥。在节点的凭据字段选择 **Use Gateway credits**（使用 Gateway 额度），即可在没有 OpenAI 账户的情况下运行节点。
{% endhint %}

使用 OpenAI Chat Model 节点，将 OpenAI 聊天模型与对话智能体[^1]配合使用。

本页列出了 OpenAI Chat Model 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [OpenAI 凭据文档](../../../credentials/openai.md)。
{% endhint %}

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

### Model（模型） <a href="#model" id="model"></a>

选择用于生成补全的模型。

n8n 从 OpenAI 动态加载模型，你只会看到自己的账户可用的模型。

### Use Responses API（使用 Responses API） <a href="#use-responses-api" id="use-responses-api"></a>

OpenAI 提供两个用于生成模型输出的端点：

* **Chat Completions**：Chat Completions API 根据组成对话的消息列表生成模型响应。用户需要手动管理对话状态，例如添加 [Simple Memory](../n8n-nodes-langchain.memorybufferwindow/README.md) 子节点。对于新项目，OpenAI 建议使用 Responses API。
* **Responses**：Responses API 提供智能体循环，使模型可在一次 API 请求内调用多个内置工具。它还支持通过传入 `conversation_id` 实现持久会话。

如果希望模型使用 Responses API 生成输出，请开启 **Use Responses API**（使用 Responses API）。否则，OpenAI Chat Model 节点默认使用 Chat Completions API。

两者的对比，请参阅 OpenAI 文档中的 [Chat Completions 与 Responses API 比较](https://platform.openai.com/docs/guides/migrate-to-responses)。

### 内置工具 <a href="#built-in-tools" id="built-in-tools"></a>

OpenAI Responses API 提供多种[内置工具](https://platform.openai.com/docs/guides/tools)，用于丰富模型响应。开启 **Use Responses API**（使用 Responses API）后，模型可访问以下内置工具：

* **Web Search**（网页搜索）：模型可先搜索互联网获取最新信息，再生成响应。
* **File Search**（文件搜索）：模型可在先前上传的文件构成的知识库中搜索相关信息，再生成响应。更多信息请参阅 [OpenAI 文档](https://platform.openai.com/docs/guides/tools-file-search)。
* **Code Interpreter**（代码解释器）：模型可在沙箱环境中编写并运行 Python 代码。

{% hint style="info" %}
**与 AI Agent 节点配合使用**

仅当 OpenAI Chat Model 节点与 AI Agent 节点配合使用时，才支持内置工具。例如，与 Basic LLM Chain 节点配合时，内置工具不可用。
{% endhint %}

## 节点选项 <a href="#node-options" id="node-options"></a>

使用以下选项进一步调整节点行为。无论是否使用 Responses API 生成模型输出，下列选项都可用。

### Frequency Penalty（频率惩罚） <a href="#frequency-penalty" id="frequency-penalty"></a>

使用此选项控制模型重复自身内容的可能性。值越高，重复的可能性越低。

### Maximum Number of Tokens（最大 token 数） <a href="#maximum-number-of-tokens" id="maximum-number-of-tokens"></a>

输入使用的 token 数量上限，以设置补全长度。

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

## 附加节点选项，仅适用于 Responses API <a href="#additional-node-options-responses-api-only" id="additional-node-options-responses-api-only"></a>

开启 **Use Responses API**（使用 Responses API）后，可使用以下附加选项。

### Conversation ID（会话 ID） <a href="#conversation-id" id="conversation-id"></a>

此响应所属的会话。响应完成后，该响应的输入数据项和输出数据项会自动添加到此会话。

### Prompt Cache Key（提示词缓存键） <a href="#prompt-cache-key" id="prompt-cache-key"></a>

使用此键缓存相似请求，优化缓存命中率。

### Safety Identifier（安全标识符） <a href="#safety-identifier" id="safety-identifier"></a>

应用标识符，以跟踪可能违反使用政策的用户。

### Service Tier（服务层级） <a href="#service-tier" id="service-tier"></a>

选择符合需求的服务层级：Auto（自动）、Flex（灵活）、Default（默认）或 Priority（优先）。

### Metadata（元数据） <a href="#metadata" id="metadata"></a>

用于存储结构化信息的一组键值对。每个对象最多可附加 16 对，便于添加自定义数据，并通过 API 或控制台搜索。

### Top Logprobs（最高对数概率） <a href="#top-logprobs" id="top-logprobs"></a>

设置 0 到 20 之间的整数，指定每个 token 位置返回多少个最可能的 token，每个 token 都附带对应的对数概率。

### Output Format（输出格式） <a href="#output-format" id="output-format"></a>

选择响应格式：Text（文本）、JSON Schema 或 JSON Object（JSON 对象）。希望接收 JSON 格式数据时，建议使用 JSON Schema。

### Prompt（提示词） <a href="#prompt" id="prompt"></a>

配置提示词的唯一 ID、版本及可替换变量。提示词通过 OpenAI 控制台配置。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 OpenAI Chat Model（OpenAI 聊天模型）集成模板](https://n8n.io/integrations/openai-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 的 OpenAI 文档](https://docs.langchain.com/oss/javascript/integrations/chat/openai)。

参数的更多信息，请参阅 [OpenAI 文档](https://platform.openai.com/docs/api-reference/responses/create)。

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见问题及建议的解决办法，请参阅[常见问题](common-issues.md)。

[^1]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大型语言模型（LLM）理解用户输入，并根据可用的信息和资源，决定如何最好地处理请求。
