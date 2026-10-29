---
title: YouTube 节点文档
description: 了解如何在 n8n 中使用 YouTube 节点，并按照技术文档将 YouTube 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: YouTube 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.youtube.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.youtube
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.youtube
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# YouTube 节点 <a href="#youtube-node" id="youtube-node"></a>

使用 YouTube 节点自动处理 YouTube 中的工作，并将其与其他应用集成。n8n 内置支持多种 YouTube 功能，包括获取和更新频道，以及创建和删除播放列表。

本页列出了 YouTube 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [YouTube 凭据](../credentials/google/README.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Channel（频道）
    * Retrieve a channel（获取频道）
    * Retrieve all channels（获取全部频道）
    * Update a channel（更新频道）
    * Upload a channel banner（上传频道横幅）
* Playlist（播放列表）
    * Create a playlist（创建播放列表）
    * Delete a playlist（删除播放列表）
    * Get a playlist（获取播放列表）
    * Retrieve all playlists（获取全部播放列表）
    * Update a playlist（更新播放列表）
* Playlist Item（播放列表条目）
    * Add an item to a playlist（向播放列表添加条目）
    * Delete a item from a playlist（从播放列表删除条目）
    * Get a playlist's item（获取播放列表条目）
    * Retrieve all playlist items（获取全部播放列表条目）
* Video（视频）
    * Delete a video（删除视频）
    * Get a video（获取视频）
    * Retrieve all videos（获取全部视频）
    * Rate a video（评价视频）
    * Update a video（更新视频）
    * Upload a video（上传视频）
* Video Category（视频类别）
    * Retrieve all video categories（获取全部视频类别）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 YouTube 集成模板](https://n8n.io/integrations/youtube)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
