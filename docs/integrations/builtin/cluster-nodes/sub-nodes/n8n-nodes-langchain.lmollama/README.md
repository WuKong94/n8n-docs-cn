---
title: Ollama Model（Ollama 模型） 节点文档
contentType:
- integration
- reference
priority: high
nodeTitle: n8n-nodes-langchain.lmollama
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama
description: 了解如何在 n8n 中使用 Ollama Model（Ollama 模型） 节点，并按照技术文档将其集成到工作流中。
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


# Ollama Model（Ollama 模型） <a id="ollama-model"></a>

Ollama Model 节点支持使用本地 Llama 2 模型。

本页列出了 Ollama Model 节点的参数，并提供更多资源的链接。

此节点不支持工具，因此无法与 [AI Agent](../../root-nodes/n8n-nodes-langchain.agent/README.md) 节点配合使用。请将其连接到 [Basic LLM Chain](../../root-nodes/n8n-nodes-langchain.chainllm.md) 节点。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Ollama 凭据文档](../../../credentials/ollama.md)。
{% endhint %}

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**（模型）：选择用于生成补全的模型，可选：
  * **Llama2**（Llama2 模型）
  * **Llama2 13B**（130 亿参数）
  * **Llama2 70B**（700 亿参数）
  * **Llama2 Uncensored**（未审查版本）

可用模型的更多信息，请参阅 Ollama 的[模型库文档](https://ollama.com/library)。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Sampling Temperature**（采样温度）：控制采样过程的随机性。温度越高，采样结果越多样，但产生幻觉的风险也越高。
* **Top K**：输入模型生成下一个 token 时考虑的候选 token 数量。
* **Top P**：设置补全使用的概率范围。较低值会忽略概率较低的选项。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Ollama Model（Ollama 模型）集成模板](https://n8n.io/integrations/ollama-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 的 Ollama 文档](https://docs.langchain.com/oss/javascript/integrations/llms/ollama)。

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见问题及建议的解决办法，请参阅[常见问题](common-issues.md)。

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/starter-kits/self-hosted-ai-starter-kit.md" %}
