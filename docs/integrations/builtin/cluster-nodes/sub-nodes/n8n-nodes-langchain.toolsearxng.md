---
title: SearXNG Tool（SearXNG 工具） 节点文档
description: 了解如何在 n8n 中使用 SearXNG Tool（SearXNG 工具） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: SearXNG Tool（SearXNG 工具） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolsearxng.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolsearxng
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolsearxng
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# SearXNG Tool（SearXNG 工具） 节点 <a href="#searxng-tool-node" id="searxng-tool-node"></a>

SearXNG Tool 节点支持将 SearXNG 搜索功能集成到工作流中。SearXNG 汇总多个搜索引擎的结果，不跟踪用户。

本页列出了 SearXNG Tool 节点的选项，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [SearXNG 凭据文档](../../credentials/searxng.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Number of Results**（结果数量）：要获取的结果数量，默认为 10。
* **Page Number**（页码）：要获取的搜索结果页码，默认为 1。
* **Language**（语言）：用于按语言筛选搜索结果的两字母[语言代码](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)，例如 `en` 表示英语，`fr` 表示法语。默认为 `en`。
* **Safe Search**（安全搜索）：启用或禁用搜索结果中的露骨内容筛选。可选 None（无）、Moderate（适中）或 Strict（严格），默认为 None。

## 运行 SearXNG 实例 <a href="#running-a-searxng-instance" id="running-a-searxng-instance"></a>

此节点要求 SearXNG 服务与 n8n 实例位于同一网络。请确保 n8n 实例可通过网络访问 SearXNG 服务。

此节点要求 JSON 格式结果，而 SearXNG 默认配置未启用。要启用 JSON 输出，请将 `json` 添加到 `search.formats` 部分；该部分位于 SearXNG 实例的 `settings.yml` 文件中：

```yaml
search:
  # options available for formats: [html, csv, json, rss]
  formats:
    - html
    - json
```

如果没有 `formats` 部分，请添加。`settings.yml` 文件的确切位置取决于 SearXNG 的安装方式。更多信息请参阅 [SearXNG 配置文档](https://docs.searxng.org/admin/installation-searxng.html#configuration)。

搜索结果的质量和可用性取决于所用 SearXNG 实例的配置和健康状态。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 SearXNG Tool（SearXNG 工具） 集成模板](https://n8n.io/integrations/searxng)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [SearXNG 文档](https://docs.searxng.org/)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

