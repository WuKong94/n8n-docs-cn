---
title: Groq Chat Model（Groq 聊天模型） 节点文档
description: 了解如何在 n8n 中使用 Groq Chat Model（Groq 聊天模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Groq Chat Model（Groq 聊天模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Groq Chat Model（Groq 聊天模型） 节点 <a href="#groq-chat-model-node" id="groq-chat-model-node"></a>

使用 Groq Chat Model 节点，访问 Groq 的大型语言模型，执行对话式 AI 和文本生成任务。

本页列出了 Groq Chat Model 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Groq 凭据文档](../../credentials/groq.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**（模型）：选择生成补全的模型。n8n 从 Groq API 动态加载可用模型。更多信息请参阅 [Groq 模型文档](https://console.groq.com/docs/models)。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Maximum Number of Tokens**（最大 token 数）：输入使用的 token 数量上限，以设置补全长度。
* **Sampling Temperature**（采样温度）：控制采样过程的随机性。温度越高，采样结果越多样，但产生幻觉的风险也越高。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Groq Chat Model（Groq 聊天模型） 集成模板](https://n8n.io/integrations/groq-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Groq API 文档](https://console.groq.com/docs/quickstart)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

