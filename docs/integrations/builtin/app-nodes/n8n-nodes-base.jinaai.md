---
title: Jina AI 节点文档
description: 了解如何在 n8n 中使用 Jina AI 节点，并按照技术文档将 Jina AI 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Jina AI 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.jinaai.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jinaai
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jinaai
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Jina AI 节点 <a href="#jina-ai-node" id="jina-ai-node"></a>

使用 Jina AI 节点自动处理 Jina AI 中的工作，并将其与其他应用集成。n8n 内置支持多种 Jina AI 功能。

本页列出了 Jina AI 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

该节点的身份验证信息，请参阅 [Jina AI 凭据文档](../credentials/jinaai.md)。
{% endhint %}


## 操作 <a href="#operations" id="operations"></a>

* **Reader**（读取器）：
	* **Read**（读取）：从 URL 获取内容，并转换为简洁、适合大语言模型处理的格式。
	* **Search**（搜索）：通过 Jina AI 执行网页搜索，将排名靠前的结果转换为简洁、适合大语言模型处理的格式。
* **Research**（研究）：
	* **Deep Research**（深度研究）：研究某个主题，并生成结构化研究报告。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Jina AI 集成模板](https://n8n.io/integrations/jina-ai)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Jina AI Reader API 文档](https://r.jina.ai/docs)和 [Jina AI Search API 文档](https://s.jina.ai/docs)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
