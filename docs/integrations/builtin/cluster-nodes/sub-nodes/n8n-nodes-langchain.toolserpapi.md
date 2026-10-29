---
title: SerpApi (Google Search)（Google 搜索） 节点文档
description: 了解如何在 n8n 中使用 SerpApi (Google Search)（Google 搜索） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: SerpApi (Google Search)（Google 搜索） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi
layout:
  description:
    visible: false
tags:
- tag: deprecated
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# SerpApi (Google Search)（Google 搜索） 节点 <a href="#serpapi-google-search-node" id="serpapi-google-search-node"></a>

{% hint style="warning" %}
**功能可用性**

SerpApi (Google Search) 节点从 n8n 2.35.0 起弃用。请改用经过验证的 **SerpApi Official** 社区节点。更多信息请参阅[已弃用和具有版本的节点](../../deprecated-nodes.md)。
{% endhint %}

SerpAPI 节点支持工作流中的智能体[^1]调用 Google Search API。

本页列出了 SerpAPI 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Serp 凭据文档](../../credentials/serp.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Country**（国家或地区）：输入要使用的国家或地区代码。支持的国家或地区及代码，请参阅 [Google GL 参数：支持的 Google 国家或地区](https://serpapi.com/google-countries)。
* **Device**（设备）：选择用于获取搜索结果的设备。
* **Explicit Array**（显式数组）：选择是否强制 SerpApi 获取 Google 结果，即使已有缓存版本；开启时强制获取，关闭时不强制。
* **Google Domain**（Google 域名）：输入要使用的 Google 域名。支持的域名请参阅[支持的 Google 域名](https://serpapi.com/google-domains)。
* **Language**（语言）：输入要使用的语言代码。支持的语言及代码，请参阅 [Google HL 参数：支持的 Google 语言](https://serpapi.com/google-languages)。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 SerpApi (Google Search)（Google 搜索） 集成模板](https://n8n.io/integrations/serpapi)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Serp 文档](https://serpapi.com/search-api)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大型语言模型（LLM）理解用户输入，并根据可用的信息和资源，决定如何最好地处理请求。
