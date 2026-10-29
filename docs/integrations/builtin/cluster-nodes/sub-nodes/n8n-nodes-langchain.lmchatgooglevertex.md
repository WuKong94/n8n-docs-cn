---
title: Google Vertex Chat Model（Google Vertex 聊天模型） 节点文档
description: 了解如何在 n8n 中使用 Google Vertex Chat Model（Google Vertex 聊天模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Google Vertex Chat Model（Google Vertex 聊天模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Vertex Chat Model（Google Vertex 聊天模型） 节点 <a href="#google-vertex-chat-model-node" id="google-vertex-chat-model-node"></a>

使用 Google Vertex AI Chat Model 节点，将 Google 的 Vertex AI 聊天模型与对话智能体[^1]配合使用。

本页列出了 Google Vertex AI Chat Model 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

使用 [Google Vertex AI 凭据](../../credentials/googlevertexai.md)，将项目、区域和服务账户详情一并存储。此节点也支持 [Google 服务账户凭据](../../credentials/google/service-account.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Authentication**（身份验证）：选择 **Google Service Account**（Google 服务账户，默认）或 **Google Vertex AI**。
* **Project ID**（项目 ID）：使用 **Google Service Account** 身份验证时，n8n 根据服务账户的访问权限加载项目列表。可选择列表中的项目，也可手动输入项目 ID。使用 **Google Vertex AI** 身份验证时，在凭据中配置项目。
* **Model Name**（模型名称）：输入用于生成补全的模型名称，例如 `gemini-2.5-flash`。可用模型列表，请参阅 [Google 模型](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models)。
* **Region**（区域）：选择 **Default (Use Credential Region)**（默认，使用凭据区域），使用凭据中设置的区域。要覆盖此值，选择 **Global**（全球）、**EU (Multi-Region)**（欧盟，多区域）或 **US (Multi-Region)**（美国，多区域）。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Maximum Number of Tokens**（最大 token 数）：输入使用的 token 数量上限，以设置补全长度。
* **Sampling Temperature**（采样温度）：控制采样过程的随机性。温度越高，采样结果越多样，但产生幻觉的风险也越高。
* **Thinking Budget**（思考预算）：控制思考模型的推理 token。设为 `0` 可禁用自动思考，设为 `-1` 则动态思考，留空为自动模式。
* **Top K**：输入模型生成下一个 token 时考虑的候选 token 数量。
* **Top P**：设置补全使用的概率范围。较低值会忽略概率较低的选项。
* **Safety Settings**（安全设置）：Gemini 支持可调整的安全设置。可用筛选器及级别的详情，请参阅 Google 的 [Gemini API 安全设置](https://ai.google.dev/docs/safety_setting_gemini)。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Google Vertex Chat Model（Google Vertex 聊天模型） 集成模板](https://n8n.io/integrations/google-vertex-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>


该服务的更多信息，请参阅 [LangChain 的 Google Vertex AI 文档](https://docs.langchain.com/oss/javascript/integrations/chat/google_vertex_ai)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大型语言模型（LLM）理解用户输入，并根据可用的信息和资源，决定如何最好地处理请求。
