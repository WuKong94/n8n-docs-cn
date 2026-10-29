---
title: Google Books 节点文档
description: 了解如何在 n8n 中使用 Google Books 节点，并按照技术文档将 Google Books 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Google Books 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googlebooks.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Books 节点 <a href="#google-books-node" id="google-books-node"></a>

使用 Google Books 节点自动处理 Google Books 中的工作，并将其与其他应用集成。n8n 内置支持多种 Google Books 功能，包括获取指定用户的特定书架资源、向书架添加图书，以及获取图书。

本页列出了 Google Books 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Google 凭据](../credentials/google/README.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Bookshelf（书架）
    * Retrieve a specific bookshelf resource for the specified user（获取指定用户的特定书架资源）
    * Get all public bookshelf resource for the specified user（获取指定用户的全部公开书架资源）
* Bookshelf Volume（书架图书）
    * Add a volume to a bookshelf（向书架添加图书）
    * Clears all volumes from a bookshelf（清空书架中的全部图书）
    * Get all volumes in a specific bookshelf for the specified user（获取指定用户特定书架中的全部图书）
    * Moves a volume within a bookshelf（移动书架中的图书）
    * Removes a volume from a bookshelf（从书架移除图书）
* Volume（图书）
    * Get a volume resource based on ID（按 ID 获取图书资源）
    * Get all volumes filtered by query（获取按查询条件筛选的全部图书）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Google Books 集成模板](https://n8n.io/integrations/google-books)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
