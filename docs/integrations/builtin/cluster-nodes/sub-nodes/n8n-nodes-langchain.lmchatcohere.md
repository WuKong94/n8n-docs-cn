---
title: Cohere Chat Model（Cohere 聊天模型） 节点文档
description: 了解如何在 n8n 中使用 Cohere Chat Model（Cohere 聊天模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Cohere Chat Model（Cohere 聊天模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatcohere.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatcohere
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatcohere
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Cohere Chat Model（Cohere 聊天模型） 节点 <a href="#cohere-chat-model-node" id="cohere-chat-model-node"></a>

使用 Cohere Chat Model 节点，访问 Cohere 的大型语言模型，执行对话式 AI 和文本生成任务。

本页列出了 Cohere Chat Model 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Cohere 凭据文档](../../credentials/cohere.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**（模型）：选择生成补全的模型。n8n 从 Cohere API 动态加载可用模型。更多信息请参阅 [Cohere 模型文档](https://docs.cohere.com/v2/docs/models#command)。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Sampling Temperature**（采样温度）：控制采样过程的随机性。温度越高，采样结果越多样，但产生幻觉的风险也越高。
* **Max Retries**（最大重试次数）：输入请求的最大重试次数。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Cohere Chat Model（Cohere 聊天模型） 集成模板](https://n8n.io/integrations/cohere-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Cohere API 文档](https://docs.cohere.com/v2/reference/about)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

