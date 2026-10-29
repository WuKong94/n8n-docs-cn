---
title: Reddit 节点文档
description: 了解如何在 n8n 中使用 Reddit 节点，并按照技术文档将 Reddit 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Reddit 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.reddit.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.reddit
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.reddit
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Reddit 节点 <a href="#reddit-node" id="reddit-node"></a>

使用 Reddit 节点自动处理 Reddit 中的工作，并将其与其他应用集成。n8n 内置支持多种 Reddit 功能，包括获取个人资料和用户、获取帖子评论与子版块，以及提交、获取和删除帖子。

本页列出了 Reddit 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Reddit 凭据](../credentials/reddit.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Post（帖子）
    * Submit a post to a subreddit（向子版块提交帖子）
    * Delete a post from a subreddit（从子版块删除帖子）
    * Get a post from a subreddit（从子版块获取帖子）
    * Get all posts from a subreddit（获取子版块的全部帖子）
    * 在子版块或整个 Reddit 中搜索帖子。
* Post Comment（帖子评论）
    * Create a top-level comment in a post（在帖子中创建顶层评论）
    * Retrieve all comments in a post（获取帖子中的全部评论）
    * Remove a comment from a post（从帖子中移除评论）
    * Write a reply to a comment in a post（回复帖子中的评论）
* Profile（个人资料）
    * Get（获取）
* Subreddit（子版块）
    * Retrieve background information about a subreddit.（获取子版块的背景信息）
    * 从整个 Reddit 获取子版块信息。
* User（用户）
    * Get（获取）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Reddit 集成模板](https://n8n.io/integrations/reddit)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
