---
title: Spotify 节点文档
description: 了解如何在 n8n 中使用 Spotify 节点，并按照技术文档将 Spotify 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Spotify 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.spotify.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.spotify
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.spotify
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Spotify 节点 <a href="#spotify-node" id="spotify-node"></a>

使用 Spotify 节点自动处理 Spotify 中的工作，并将其与其他应用集成。n8n 内置支持多种 Spotify 功能，包括获取专辑和艺人信息。

本页列出了 Spotify 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Spotify 凭据](../credentials/spotify.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Album（专辑）
    * Get an album by URI or ID.（通过 URI 或 ID 获取专辑）
    * Get a list of new album releases.（获取新发行专辑列表）
    * Get an album's tracks by URI or ID.（通过专辑 URI 或 ID 获取其中的曲目）
    * Search albums by keyword.（按关键词搜索专辑）
* Artist（艺人）
    * Get an artist by URI or ID.（通过 URI 或 ID 获取艺人）
    * Get an artist's albums by URI or ID.（通过艺人 URI 或 ID 获取其专辑）
    * Get an artist's related artists by URI or ID.（通过艺人 URI 或 ID 获取相关艺人）
    * Get an artist's top tracks by URI or ID.（通过艺人 URI 或 ID 获取其热门曲目）
    * Search artists by keyword.（按关键词搜索艺人）
* Library（音乐库）
    * Get the user's liked tracks.（获取用户喜欢的曲目）
* My Data（我的数据）
    * Get your followed artists.（获取你关注的艺人）
* Player（播放器）
    * Add a song to your queue.（向播放队列添加歌曲）
    * Get your currently playing track.（获取当前播放的曲目）
    * Skip to your next track.（跳到下一首曲目）
    * Pause your music.（暂停音乐）
    * Skip to your previous song.（跳到上一首歌曲）
    * Get your recently played tracks.（获取最近播放的曲目）
    * Resume playback on the current active device.（在当前活动设备上恢复播放）
    * Set volume on the current active device.（设置当前活动设备的音量）
    * Start playing a playlist, artist, or album.（开始播放播放列表、艺人作品或专辑）
* Playlist（播放列表）
    * Add tracks to a playlist by track and playlist URI or ID.（通过曲目和播放列表的 URI 或 ID，将曲目添加到播放列表）
    * Create a new playlist.（创建新播放列表）
    * Get a playlist by URI or ID.（通过 URI 或 ID 获取播放列表）
    * Get a playlist's tracks by URI or ID.（通过播放列表 URI 或 ID 获取其中的曲目）
    * Get a user's playlists.（获取用户的播放列表）
    * Remove tracks from a playlist by track and playlist URI or ID.（通过曲目和播放列表的 URI 或 ID，从播放列表移除曲目）
    * Search playlists by keyword.（按关键词搜索播放列表）
* Track（曲目）
    * Get a track by its URI or ID.（通过 URI 或 ID 获取曲目）
    * Get audio features for a track by URI or ID.（通过曲目 URI 或 ID 获取其音频特征）
    * Search tracks by keyword（按关键词搜索曲目）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Spotify 集成模板](https://n8n.io/integrations/spotify)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
