---
title: Microsoft Foundry Chat Model（Microsoft Foundry 聊天模型） 节点文档
description: 了解如何在 n8n 中使用 Microsoft Foundry Chat Model（Microsoft Foundry 聊天模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Microsoft Foundry Chat Model（Microsoft Foundry 聊天模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatazureopenai.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatazureopenai
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatazureopenai
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Foundry Chat Model（Microsoft Foundry 聊天模型） 节点 <a href="#azure-openai-chat-model-node" id="azure-openai-chat-model-node"></a>

Microsoft Foundry Chat Model 节点将对话智能体[^1]连接到 Microsoft Foundry 或 Azure OpenAI 资源中的聊天模型。

此节点此前名为 **Azure AI Foundry Chat Model** 和 **Azure OpenAI Chat Model**。

本页列出了 Microsoft Foundry Chat Model 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Microsoft Foundry 凭据文档](../../credentials/azureopenai.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Authentication**（身份验证）：选择 **API Key**（API 密钥）或 **Azure Entra ID (OAuth2)**，每个选项使用独立凭据。
* **Project**（项目）：输入部署所属的 Microsoft Foundry 项目名称。留空则使用凭据中的 **Project**。经典 Azure OpenAI 资源不使用此项。
* **Model (Deployment)**（模型或部署）：选择用于生成补全的部署。
    * **From List**（从列表选择）：从项目中的部署选择，仅显示聊天部署。需要 Microsoft Foundry 凭据，以及在此字段或凭据中设置的 **Project**（项目）。请先设置 **Project**。
    * **By ID**（按 ID）：输入部署名称。使用经典 Azure OpenAI 凭据或未出现在列表中的部署时，使用此项。
* **Model Family**（模型系列）：选择部署使用的 API 系列。Azure 不报告此信息，因此请设置为与部署一致。
    * **OpenAI**：用于 GPT 和其他兼容 OpenAI 的模型。
    * **Anthropic**：用于 Claude 模型，需要使用 Microsoft Foundry 端点类型的凭据。此系列不提供 **Frequency Penalty**（频率惩罚）、**Presence Penalty**（存在惩罚）和 **Response Format**（响应格式）选项。
* **Use Responses API**（使用 Responses API）：选择节点为 OpenAI 系列部署调用的 API，需要使用 Microsoft Foundry 端点类型的凭据。
    * **Off**（关闭，默认）：节点调用 Chat Completions API，适用于大多数部署。
    * **On**（开启）：节点调用 Responses API。部署仅支持 Responses API 时启用。对这类部署调用 Chat Completions 时，Azure 会返回 `400 Model not supported` 错误。

{% hint style="info" %}
**现有工作流**

这些变更之前创建的工作流保留 **Model (Deployment) Name**（模型或部署名称）文本字段，并使用 Chat Completions。要使用部署列表和 **Use Responses API**（使用 Responses API）设置，请创建新节点。
{% endhint %}

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Frequency Penalty**（频率惩罚）：控制模型重复自身内容的可能性。值越高，重复的可能性越低。
* **Maximum Number of Tokens**（最大 token 数）：输入使用的 token 数量上限，以设置补全长度。
* **Response Format**（响应格式）：选择 **Text**（文本）或 **JSON**。**JSON** 确保模型返回有效 JSON。
* **Presence Penalty**（存在惩罚）：控制模型谈论新话题的可能性。值越高，谈论新话题的可能性越高。
* **Sampling Temperature**（采样温度）：控制采样过程的随机性。温度越高，采样结果越多样，但产生幻觉的风险也越高。**OpenAI** 模型系列的最大值为 2，**Anthropic** 模型系列的最大值为 1。
* **Timeout**（超时）：输入请求的最长耗时，单位为毫秒。
* **Max Retries**（最大重试次数）：输入请求的最大重试次数。
* **Top P**：设置补全使用的概率范围。较低值会忽略概率较低的选项。
* **Extra Body**（附加请求体）：输入要添加到请求体的额外 JSON 属性，用于部署支持、但其他选项未涵盖的参数。值必须为 JSON 对象。

## 代理限制 <a href="#proxy-limitations" id="proxy-limitations"></a>

此节点不支持 [`NO_PROXY` 环境变量](../../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment.md)。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Microsoft Foundry Chat Model（Microsoft Foundry 聊天模型） 集成模板](https://n8n.io/integrations/azure-openai-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 的 Azure OpenAI 文档](https://docs.langchain.com/oss/javascript/integrations/chat/azure)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大型语言模型（LLM）理解用户输入，并根据可用的信息和资源，决定如何最好地处理请求。
