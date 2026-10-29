---
title: GitHub Document Loader（GitHub 文档加载器） 节点文档
description: 了解如何在 n8n 中使用 GitHub Document Loader（GitHub 文档加载器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: GitHub Document Loader（GitHub 文档加载器） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader
layout:
  description:
    visible: false
tags:
- tag: deprecated
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# GitHub Document Loader（GitHub 文档加载器） 节点 <a href="#github-document-loader-node" id="github-document-loader-node"></a>

{% hint style="warning" %}
**功能可用性**

GitHub Document Loader 节点从 n8n 1.122.0 起弃用。更多信息请参阅[已弃用和具有版本的节点](../../deprecated-nodes.md)。
{% endhint %}

使用 GitHub Document Loader 节点，从 GitHub 仓库加载数据，用于[向量存储](#user-content-fn-1)[^1]或摘要处理。

本页列出了 GitHub Document Loader 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [GitHub 凭据文档](../../credentials/github.md)。此节点不支持 OAuth 身份验证。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Text Splitting**（文本拆分）：可选择：
    * **Simple**（简单）：使用 [Recursive Character Text Splitter（递归字符文本拆分器）](n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter.md)，块大小为 1000，重叠量为 200。
    * **Custom**（自定义）：可连接你选择的文本拆分器。
* **Repository Link**（仓库链接）：输入 GitHub 仓库的 URL。
* **Branch**（分支）：输入要使用的分支名称。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Recursive**（递归）：选择是否包含子文件夹和文件，开启时包含，关闭时不包含。
* **Ignore Paths**（忽略路径）：输入要忽略的目录。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 GitHub Document Loader（GitHub 文档加载器） 集成模板](https://n8n.io/integrations/github-document-loader)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-doc-loaders-link.md" %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

<a id="user-content-fn-1"></a>
[^1]: 向量存储或向量数据库用于存储信息的数学表示。将其与嵌入模型和检索器配合使用，可创建供 AI 在回答问题时访问的数据库。
