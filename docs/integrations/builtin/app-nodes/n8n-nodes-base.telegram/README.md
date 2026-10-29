---
title: Telegram 节点
contentType:
- integration
- reference
priority: critical
nodeTitle: n8n-nodes-base.telegram
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.telegram/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram
description: 了解 n8n 工作流自动化平台中的 Telegram 节点，包括操作及配置详情，以及示例和凭据信息链接。
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


# Telegram <a id="telegram"></a>

使用 Telegram 节点自动处理 [Telegram](https://telegram.org/) 中的工作，并将 Telegram 与其他应用集成。n8n 内置支持多种 Telegram 功能，包括获取文件，以及删除和编辑消息。

本页列出了 Telegram 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Telegram 凭据](../../credentials/telegram.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* [**Chat**（聊天）操作](chat-operations.md)
  * [**Get**](chat-operations.md#get-chat)（获取）：获取聊天的最新信息。
  * [**Get Administrators**](chat-operations.md#get-administrators)（获取管理员）：获取聊天的管理员列表。
  * [**Get Member**](chat-operations.md#get-chat-member)（获取成员）：获取聊天成员的详细信息。
  * [**Leave**](chat-operations.md#leave-chat)（退出）：退出聊天。
  * [**Set Description**](chat-operations.md#set-description)（设置描述）：设置聊天描述。
  * [**Set Title**](chat-operations.md#set-title)（设置标题）：设置聊天标题。
* [**Callback**（回调）操作](callback-operations.md)
  * [**Answer Query**](callback-operations.md#answer-query)（回答查询）：回答来自[内联键盘](https://core.telegram.org/bots/features#inline-keyboards)的回调查询。
  * [**Answer Inline Query**](callback-operations.md#answer-inline-query)（回答内联查询）：回答内联查询。
* [**File**（文件）操作](file-operations.md)
  * [**Get File**](file-operations.md#get-file)（获取文件）：从 Telegram 获取文件。
*   [**Message**（消息）操作](message-operations.md)<br>

    * [**Delete Chat Message**](message-operations.md#delete-chat-message)（删除聊天消息）。
    * [**Edit Message Text**](message-operations.md#edit-message-text)（编辑消息文本）：编辑已有消息的文本。
    * [**Pin Chat Message**](message-operations.md#pin-chat-message)（置顶聊天消息）：在聊天中置顶消息。
    * [**Send Animation**](message-operations.md#send-animation)（发送动画）：向聊天发送动画。
      * 适用于 GIF 或无声 H.264/MPEG-4 AVC 视频，文件大小不超过 50 MB。
    * [**Send Audio**](message-operations.md#send-audio)（发送音频）：向聊天发送音频文件，并在音乐播放器中显示。
    * [**Send Chat Action**](message-operations.md#send-chat-action)（发送聊天动作）：告知用户机器人正在执行某项操作，状态最长持续 5 秒。
    * [**Send Document**](message-operations.md#send-document)（发送文档）：向聊天发送文档。
    * [**Send Location**](message-operations.md#send-location)（发送位置）：向聊天发送地理位置。
    * [**Send Media Group**](message-operations.md#send-media-group)（发送媒体组）：发送一组照片和／或视频。
    * [**Send Message**](message-operations.md#send-message)（发送消息）：向聊天发送消息。
    * [**Send Photo**](message-operations.md#send-photo)（发送照片）：向聊天发送照片。
    * [**Send Sticker**](message-operations.md#send-sticker)（发送贴纸）：向聊天发送贴纸。
      * 适用于静态 .WEBP、动画 .TGS 或视频 .WEBM 贴纸。
    * [**Send Video**](message-operations.md#send-video)（发送视频）：向聊天发送视频。
    * [**Unpin Chat Message**](message-operations.md#unpin-chat-message)（取消置顶聊天消息）：取消聊天中消息的置顶状态。

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>将机器人添加到频道</strong></p><p>如果要通过 <strong>Message</strong>（消息）操作向频道发送消息，需要先将机器人添加到该频道。更多信息，请参阅<a href="common-issues.md#add-a-bot-to-a-telegram-channel">常见问题 | 将机器人添加到 Telegram 频道</a>。</p></div>

    ## 模板与示例 <a id="templates-and-examples"></a>

[浏览 n8n-nodes-base.telegram 集成模板](https://n8n.io/integrations/telegram)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Telegram API 文档](https://core.telegram.org/bots/api)。

n8n 为 Telegram 提供了触发器节点。更多信息，请参阅 [Telegram Trigger 节点文档](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误或问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。
