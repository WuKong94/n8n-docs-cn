---
title: Hugging Face Inference Model（Hugging Face 推理模型） 节点文档
contentType:
- integration
- reference
priority: medium
nodeTitle: Hugging Face Inference Model（Hugging Face 推理模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference
description: 了解如何在 n8n 中使用 Hugging Face Inference Model（Hugging Face 推理模型） 节点，并按照技术文档将其集成到工作流中。
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


# Hugging Face Inference Model（Hugging Face 推理模型） <a id="hugging-face-inference-model"></a>

使用 Hugging Face Inference Model 节点来使用 Hugging Face 模型。

本页列出了 Hugging Face Inference Model 节点的参数，并提供更多资源的链接。

此节点不支持工具，因此无法与 [AI Agent](../root-nodes/n8n-nodes-langchain.agent/README.md) 节点配合使用。请将其连接到 [Basic LLM Chain](../root-nodes/n8n-nodes-langchain.chainllm.md) 节点。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Hugging Face 凭据文档](../../credentials/huggingface.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**（模型）：选择用于生成补全的模型。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Custom Inference Endpoint**（自定义推理端点）：输入自定义推理端点 URL。
* **Frequency Penalty**（频率惩罚）：控制模型重复自身内容的可能性。值越高，重复的可能性越低。
* **Maximum Number of Tokens**（最大 token 数）：输入使用的 token 数量上限，以设置补全长度。
* **Presence Penalty**（存在惩罚）：控制模型谈论新话题的可能性。值越高，谈论新话题的可能性越高。
* **Sampling Temperature**（采样温度）：控制采样过程的随机性。温度越高，采样结果越多样，但产生幻觉的风险也越高。
* **Top K**：输入模型生成下一个 token 时考虑的候选 token 数量。
* **Top P**：设置补全使用的概率范围。较低值会忽略概率较低的选项。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Hugging Face Inference Model（Hugging Face 推理模型） 集成模板](https://n8n.io/integrations/hugging-face-inference-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}
