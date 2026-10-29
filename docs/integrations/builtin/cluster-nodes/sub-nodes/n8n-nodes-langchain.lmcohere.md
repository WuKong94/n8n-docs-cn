---
title: Cohere Model（Cohere 模型） 节点文档
contentType:
- integration
- reference
nodeTitle: Cohere Model（Cohere 模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere
description: 了解如何在 n8n 中使用 Cohere Model（Cohere 模型） 节点，并按照技术文档将其集成到工作流中。
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


# Cohere Model（Cohere 模型） <a id="cohere-model"></a>

使用 Cohere Model 节点来使用 Cohere 模型。

本页列出了 Cohere Model 节点的参数，并提供更多资源的链接。

此节点不支持工具，因此无法与 [AI Agent](../root-nodes/n8n-nodes-langchain.agent/README.md) 节点配合使用。请将其连接到 [Basic LLM Chain](../root-nodes/n8n-nodes-langchain.chainllm.md) 节点。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Cohere 凭据文档](../../credentials/cohere.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Maximum Number of Tokens**（最大 token 数）：输入使用的 token 数量上限，以设置补全长度。
* **Sampling Temperature**（采样温度）：控制采样过程的随机性。温度越高，采样结果越多样，但产生幻觉的风险也越高。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Cohere Model（Cohere 模型） 集成模板](https://n8n.io/integrations/cohere-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 的 Cohere 文档](https://docs.langchain.com/oss/javascript/integrations/llms/cohere)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}
