---
title: Ghost 节点文档
description: 了解如何在 n8n 中使用 Ghost 节点，并按照技术文档将 Ghost 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Ghost 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.ghost.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.ghost
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.ghost
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Ghost 节点 <a href="#ghost-node" id="ghost-node"></a>

使用 Ghost 节点自动处理 Ghost 中的工作，并将其与其他应用集成。n8n 内置支持多种 Ghost 功能，包括文章的创建、更新、删除和获取，涵盖 Admin API 与 Content API。

本页列出了 Ghost 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Ghost 凭据](../credentials/ghost.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

### Admin API（管理 API） <a href="#admin-api" id="admin-api"></a>

* **Post（文章）**
    * Create a post（创建帖子）
    * Delete a post（删除帖子）
    * Get a post（获取帖子）
    * Get all posts（获取全部帖子）
    * Update a post（更新帖子）


### Content API（内容 API） <a href="#content-api" id="content-api"></a>

* **Post（文章）**
    * Get a post（获取帖子）
    * Get all posts（获取全部帖子）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Ghost 集成模板](https://n8n.io/integrations/ghost)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

