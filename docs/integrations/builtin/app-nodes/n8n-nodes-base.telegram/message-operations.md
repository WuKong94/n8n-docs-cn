---
title: Telegram 节点消息操作
contentType:
- integration
- reference
priority: critical
nodeTitle: Telegram 节点消息操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations
description: 了解 n8n 工作流自动化平台中 Telegram 节点的消息操作，以及各项操作的配置详情。
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


# 消息操作 <a id="message-operations"></a>

使用这些操作在聊天中发送、编辑和删除消息，发送文件，以及置顶消息或取消置顶。有关 Telegram 节点本身的更多信息，请参阅 [Telegram](./README.md)。

{% hint style="info" %}
**将机器人添加到频道**

如果要向频道发送消息，需要先将机器人添加到该频道。更多信息，请参阅[常见问题 | 将机器人添加到 Telegram 频道](common-issues.md#add-a-bot-to-a-telegram-channel)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/hitl-tools.md" %}

## Delete Chat Message（删除聊天消息） <a href="#delete-chat-message" id="delete-chat-message"></a>

此操作通过 Bot API 的 [deleteMessage](https://core.telegram.org/bots/api#deletemessage) 方法删除聊天中的一条消息。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Delete Chat Message**（删除聊天消息）。
* **Chat ID**（聊天 ID）：输入待删除消息所在聊天的 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Message ID**（消息 ID）：输入要删除的消息的唯一标识符。

更多信息，请参阅 Telegram Bot API 的 [deleteMessage](https://core.telegram.org/bots/api#deletemessage) 文档。

## Edit Message Text（编辑消息文本） <a href="#edit-message-text" id="edit-message-text"></a>

此操作通过 Bot API 的 [editMessageText](https://core.telegram.org/bots/api#editmessagetext) 方法编辑已有消息的文本。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Edit Message Text**（编辑消息文本）。
* **Chat ID**（聊天 ID）：输入待编辑消息所在聊天的 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Message ID**（消息 ID）：输入要编辑的消息的唯一标识符。
* **Reply Markup**（回复界面）：选择 **Inline Keyboard**（内联键盘）以显示 InlineKeyboardMarkup，选择 **None**（无）则不使用。此选项设置 `reply_markup` 参数。更多信息，请参阅 [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) 文档。
* **Text**（文本）：输入消息修改后的文本。

更多信息，请参阅 Telegram Bot API 的 [editMessageText](https://core.telegram.org/bots/api#editmessagetext) 文档。

### Edit Message Text 附加字段 <a href="#edit-message-text-additional-fields" id="edit-message-text-additional-fields"></a>

使用 **Additional Fields**（附加字段）进一步调整节点行为。选择 **Add Field**（添加字段）可添加以下任意字段：

* **Disable WebPage Preview**（禁用网页预览）：关闭时启用消息中链接的预览，开启时禁用链接预览。此选项通过 `link_preview_options` 中的 `is_disabled` 参数控制。更多信息，请参阅 [LinkPreviewOptions](https://core.telegram.org/bots/api#linkpreviewoptions) 文档。
* **Parse Mode**（解析模式）：选择消息使用的解析格式：**HTML**（默认）、**Markdown (Legacy)**（旧版 Markdown）或 **MarkdownV2**。此选项设置 `parse_mode` 参数。

## Pin Chat Message（置顶聊天消息） <a href="#pin-chat-message" id="pin-chat-message"></a>

此操作通过 Bot API 的 [pinChatMessage](https://core.telegram.org/bots/api#pinchatmessage) 方法在聊天中置顶消息。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Pin Chat Message**（置顶聊天消息）。
* **Chat ID**（聊天 ID）：输入要置顶消息的聊天 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Message ID**（消息 ID）：输入要置顶的消息的唯一标识符。

更多信息，请参阅 Telegram Bot API 的 [pinChatMessage](https://core.telegram.org/bots/api#pinchatmessage) 文档。

### Pin Chat Message 附加字段 <a href="#pin-chat-message-additional-fields" id="pin-chat-message-additional-fields"></a>

使用 **Additional Fields**（附加字段）进一步调整节点行为。选择 **Add Field**（添加字段）可添加以下任意字段：

* **Disable Notifications**（禁用通知）：默认情况下，Telegram 会通知聊天成员有新的置顶消息。开启此选项可停止通知。它会将 `disable_notification` 参数设为 `true`。译注：频道和私聊的置顶通知始终禁用。

## Send Animation（发送动画） <a href="#send-animation" id="send-animation"></a>

此操作通过 Bot API 的 [sendAnimation](https://core.telegram.org/bots/api#sendanimation) 方法向聊天发送动画，支持 GIF 或无声 H.264/MPEG-4 AVC 视频，文件大小不超过 50 MB。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Send Animation**（发送动画）。
* **Chat ID**（聊天 ID）：输入要接收动画的聊天 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Binary File**（二进制文件）：要发送节点本身提供的二进制文件，开启此选项。开启后，必须在 **Input Binary Field**（输入二进制字段）中指定包含待发送文件的字段。
* **Animation**（动画）：不使用 **Binary File**（二进制文件）时，在此指定要发送的动画。传入 `file_id` 可发送 Telegram 服务器上已有的文件（推荐），也可提供 HTTP URL，让 Telegram 从互联网获取文件。
* **Reply Markup**（回复界面）：使用此参数设置更多界面选项。有关这些选项及其用法，请参阅 [Reply Markup 参数](message-operations.md#reply-markup-parameters)。

更多信息，请参阅 Telegram Bot API 的 [sendAnimation](https://core.telegram.org/bots/api#sendanimation) 文档。

### Send Animation 附加字段 <a href="#send-animation-additional-fields" id="send-animation-additional-fields"></a>

使用 **Additional Fields**（附加字段）设置 Telegram 的 sendAnimation 方法中的可选字段，进一步调整节点行为。选择 **Add Field**（添加字段）可添加以下任意字段：

* **Caption**（说明文字）：输入动画的说明文字，最多 1024 个字符。
* **Disable Notification**（禁用通知）：开启时静默发送，关闭时使用普通通知发送。
* **Duration**（时长）：输入动画的持续时间，单位为秒。
* **Height**（高度）：输入动画的高度。
* **Parse Mode**（解析模式）：选择相关文本的解析格式，可选 **HTML**（默认）、**Markdown (Legacy)**（旧版 Markdown）或 **MarkdownV2**。更多信息，请参阅[格式选项](https://core.telegram.org/bots/api#formatting-options)。
* **Reply To Message ID**（回复目标消息 ID）：如果此消息是回复，输入被回复消息的 ID。
* **Message Thread ID**（消息线程 ID）：输入目标论坛消息线程（话题）的唯一标识符，仅适用于论坛超级群组。
* **Thumbnail**（缩略图）：为所发送的文件添加缩略图。如果服务端支持为该文件生成缩略图，可忽略此字段。缩略图应符合以下要求：
  * JPEG 格式。
  * 文件大小小于 200 KB。
  * 宽度和高度均小于 320px。
* **Width**（宽度）：输入视频片段的宽度。

### Send Audio（发送音频） <a href="#send-audio" id="send-audio"></a>

此操作通过 Bot API 的 [sendAudio](https://core.telegram.org/bots/api#sendaudio) 方法向聊天发送音频文件，并在音乐播放器中显示。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Send Audio**（发送音频）。
* **Chat ID**（聊天 ID）：输入要接收音频的聊天 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Binary File**（二进制文件）：要发送节点本身提供的二进制文件，开启此选项。开启后，必须在 **Input Binary Field**（输入二进制字段）中指定包含待发送文件的字段。
* **Audio**（音频）：不使用 **Binary File**（二进制文件）时，在此指定要发送的音频。传入 `file_id` 可发送 Telegram 服务器上已有的文件（推荐），也可提供 HTTP URL，让 Telegram 从互联网获取文件。
* **Reply Markup**（回复界面）：使用此参数设置更多界面选项。有关这些选项及其用法，请参阅 [Reply Markup 参数](message-operations.md#reply-markup-parameters)。

更多信息，请参阅 Telegram Bot API 的 [sendAudio](https://core.telegram.org/bots/api#sendaudio) 文档。

### Send Audio 附加字段 <a href="#send-audio-additional-fields" id="send-audio-additional-fields"></a>

使用 **Additional Fields**（附加字段）设置 Telegram 的 sendAudio 方法中的可选字段，进一步调整节点行为。选择 **Add Field**（添加字段）可添加以下任意字段：

* **Caption**（说明文字）：输入音频的说明文字，最多 1024 个字符。
* **Disable Notification**（禁用通知）：开启时静默发送，关闭时使用普通通知发送。
* **Duration**（时长）：输入音频的持续时间，单位为秒。
* **Parse Mode**（解析模式）：选择相关文本的解析格式，可选 **HTML**（默认）、**Markdown (Legacy)**（旧版 Markdown）或 **MarkdownV2**。更多信息，请参阅[格式选项](https://core.telegram.org/bots/api#formatting-options)。
* **Performer**（表演者）：输入表演者的姓名或名称。
* **Reply To Message ID**（回复目标消息 ID）：如果此消息是回复，输入被回复消息的 ID。
* **Message Thread ID**（消息线程 ID）：输入目标论坛消息线程（话题）的唯一标识符，仅适用于论坛超级群组。
* **Title**（标题）：输入音轨名称。
* **Thumbnail**（缩略图）：为所发送的文件添加缩略图。如果服务端支持为该文件生成缩略图，可忽略此字段。缩略图应符合以下要求：
  * JPEG 格式。
  * 文件大小小于 200 KB。
  * 宽度和高度均小于 320px。

## Send Chat Action（发送聊天动作） <a href="#send-chat-action" id="send-chat-action"></a>

当需要告知用户机器人正在执行某项操作时，使用此操作。它通过 Bot API 的 [sendChatAction](https://core.telegram.org/bots/api#sendchataction) 方法设置状态，状态最长持续 5 秒。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Send Chat Action**（发送聊天动作）。
* **Chat ID**（聊天 ID）：输入要接收聊天动作的聊天 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Action**（动作）：选择要向用户展示的机器人当前动作。可选项包括 **Find Location**（查找位置）、**Typing**（正在输入）、**Recording**（录制）音频或视频，以及 **Uploading**（上传）各类文件。

更多信息，请参阅 Telegram Bot API 的 [sendChatAction](https://core.telegram.org/bots/api#sendchataction) 文档。

## Send Document（发送文档） <a href="#send-document" id="send-document"></a>

此操作通过 Bot API 的 [sendDocument](https://core.telegram.org/bots/api#senddocument) 方法向聊天发送文档。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Send Document**（发送文档）。
* **Chat ID**（聊天 ID）：输入要接收文档的聊天 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Binary File**（二进制文件）：要发送节点本身提供的二进制文件，开启此选项。开启后，必须在 **Input Binary Field**（输入二进制字段）中指定包含待发送文件的字段。
* **Document**（文档）：不使用 **Binary File**（二进制文件）时，在此指定要发送的文档。传入 `file_id` 可发送 Telegram 服务器上已有的文件（推荐），也可提供 HTTP URL，让 Telegram 从互联网获取文件。
* **Reply Markup**（回复界面）：使用此参数设置更多界面选项。有关这些选项及其用法，请参阅 [Reply Markup 参数](message-operations.md#reply-markup-parameters)。

更多信息，请参阅 Telegram Bot API 的 [sendDocument](https://core.telegram.org/bots/api#sendchataction) 文档。

### Send Document 附加字段 <a href="#send-document-additional-fields" id="send-document-additional-fields"></a>

使用 **Additional Fields**（附加字段）设置 Telegram 的 sendDocument 方法中的可选字段，进一步调整节点行为。选择 **Add Field**（添加字段）可添加以下任意字段：

* **Caption**（说明文字）：输入文件的说明文字，最多 1024 个字符。
* **Disable Notification**（禁用通知）：开启时静默发送，关闭时使用普通通知发送。
* **Parse Mode**（解析模式）：选择相关文本的解析格式，可选 **HTML**（默认）、**Markdown (Legacy)**（旧版 Markdown）或 **MarkdownV2**。更多信息，请参阅[格式选项](https://core.telegram.org/bots/api#formatting-options)。
* **Reply To Message ID**（回复目标消息 ID）：如果此消息是回复，输入被回复消息的 ID。
* **Message Thread ID**（消息线程 ID）：输入目标论坛消息线程（话题）的唯一标识符，仅适用于论坛超级群组。
* **Thumbnail**（缩略图）：为所发送的文件添加缩略图。如果服务端支持为该文件生成缩略图，可忽略此字段。缩略图应符合以下要求：
  * JPEG 格式。
  * 文件大小小于 200 KB。
  * 宽度和高度均小于 320px。

## Send Location（发送位置） <a href="#send-location" id="send-location"></a>

此操作通过 Bot API 的 [sendLocation](https://core.telegram.org/bots/api#sendlocation) 方法向聊天发送地理位置。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Send Location**（发送位置）。
* **Chat ID**（聊天 ID）：输入要接收地理位置的聊天 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Latitude**（纬度）：输入位置的纬度。
* **Longitude**（经度）：输入位置的经度。
* **Reply Markup**（回复界面）：使用此参数设置更多界面选项。有关这些选项及其用法，请参阅 [Reply Markup 参数](message-operations.md#reply-markup-parameters)。

更多信息，请参阅 Telegram Bot API 的 [sendLocation](https://core.telegram.org/bots/api#sendlocation) 文档。

### Send Location 附加字段 <a href="#send-location-additional-fields" id="send-location-additional-fields"></a>

使用 **Additional Fields**（附加字段）设置 Telegram 的 sendLocation 方法中的可选字段，进一步调整节点行为。选择 **Add Field**（添加字段）可添加以下任意字段：

* **Disable Notification**（禁用通知）：开启时静默发送，关闭时使用普通通知发送。
* **Reply To Message ID**（回复目标消息 ID）：如果此消息是回复，输入被回复消息的 ID。
* **Message Thread ID**（消息线程 ID）：输入目标论坛消息线程（话题）的唯一标识符，仅适用于论坛超级群组。

## Send Media Group（发送媒体组） <a href="#send-media-group" id="send-media-group"></a>

此操作通过 Bot API 的 [sendMediaGroup](https://core.telegram.org/bots/api#sendmediagroup) 方法发送一组照片和／或视频。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Send Media Group**（发送媒体组）。
* **Chat ID**（聊天 ID）：输入要接收媒体组的聊天 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Media**（媒体）：使用 **Add Media**（添加媒体）将不同类型的媒体添加到媒体组。为每个媒体项选择：
  * **Type**（类型）：选择媒体类型，可选 **Photo**（照片）或 **Video**（视频）。
  * **Media File**（媒体文件）：指定要发送的媒体文件。传入 `file_id` 可发送 Telegram 服务器上已有的文件（推荐），也可提供 HTTP URL，让 Telegram 从互联网获取文件。
  * **Additional Fields**（附加字段）：可为每个媒体文件添加以下字段：
    * **Caption**（说明文字）：输入文件的说明文字，最多 1024 个字符。
    * **Parse Mode**（解析模式）：选择相关文本的解析格式，可选 **HTML**（默认）、**Markdown (Legacy)**（旧版 Markdown）或 **MarkdownV2**。更多信息，请参阅[格式选项](https://core.telegram.org/bots/api#formatting-options)。

更多信息，请参阅 Telegram Bot API 的 [sendMediaGroup](https://core.telegram.org/bots/api#sendmediagroup) 文档。

### Send Media Group 附加字段 <a href="#send-media-group-additional-fields" id="send-media-group-additional-fields"></a>

使用 **Additional Fields**（附加字段）设置 Telegram 的 sendMediaGroup 方法中的可选字段，进一步调整节点行为。选择 **Add Field**（添加字段）可添加以下任意字段：

* **Disable Notification**（禁用通知）：开启时静默发送，关闭时使用普通通知发送。
* **Reply To Message ID**（回复目标消息 ID）：如果此消息是回复，输入被回复消息的 ID。
* **Message Thread ID**（消息线程 ID）：输入目标论坛消息线程（话题）的唯一标识符，仅适用于论坛超级群组。

## Send Message（发送消息） <a href="#send-message" id="send-message"></a>

此操作通过 Bot API 的 [sendMessage](https://core.telegram.org/bots/api#sendmessage) 方法向聊天发送消息。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Send Message**（发送消息）。
* **Chat ID**（聊天 ID）：输入要接收消息的聊天 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Text**（文本）：输入要发送的文本，解析实体后最多 4096 个字符。

更多信息，请参阅 Telegram Bot API 的 [sendMessage](https://core.telegram.org/bots/api#sendmessage) 文档。

{% hint style="warning" %}
**发送消息的限制**

Telegram 普通批量发送的速率上限约为每秒 30 条消息。如果预计会达到此上限，请参阅[分批发送超过 30 条消息](common-issues.md#send-more-than-30-messages-per-second)，按建议分批并等待，遵守该速率限制。
{% endhint %}

### Send Message 附加字段 <a href="#send-message-additional-fields" id="send-message-additional-fields"></a>

使用 **Additional Fields**（附加字段）设置 Telegram 的 sendMessage 方法中的可选字段，进一步调整节点行为。选择 **Add Field**（添加字段）可添加以下任意字段：

* **Append n8n Attribution**（附加 n8n 标识）：选择是否在消息末尾附加 `This message was sent automatically with n8n` 这段文字。开启时附加（默认），关闭时不附加。
* **Disable Notification**（禁用通知）：开启时静默发送，关闭时使用普通通知发送。
* **Disable WebPage Preview**（禁用网页预览）：关闭时启用消息中链接的预览，开启时禁用链接预览。此选项通过 `link_preview_options` 中的 `is_disabled` 参数控制。更多信息，请参阅 [LinkPreviewOptions](https://core.telegram.org/bots/api#linkpreviewoptions) 文档。
* **Parse Mode**（解析模式）：选择相关文本的解析格式，可选 **HTML**（默认）、**Markdown (Legacy)**（旧版 Markdown）或 **MarkdownV2**。更多信息，请参阅 Telegram 的[格式选项](https://core.telegram.org/bots/api#formatting-options)。
* **Reply To Message ID**（回复目标消息 ID）：如果此消息是回复，输入被回复消息的 ID。
* **Message Thread ID**（消息线程 ID）：输入目标论坛消息线程（话题）的唯一标识符，仅适用于论坛超级群组。

## Send and Wait for Response（发送并等待响应） <a href="#send-and-wait-for-response" id="send-and-wait-for-response"></a>

此操作通过 Bot API 的 [`sendMessage`](https://core.telegram.org/bots/api#sendmessage) 方法向聊天发送消息，然后暂停工作流执行，直到用户确认操作。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Send and Wait for Response**（发送并等待响应）。
* **Chat ID**（聊天 ID）：输入要接收消息的聊天 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Message**（消息）：输入要发送的文本。
* **Response Type**（响应类型）：选择要使用的审批或响应类型：
  * **Approval**（审批）：用户可以通过消息批准或拒绝。
  * **Free Text**（自由文本）：用户可以通过表单提交回复。
  * **Custom Form**（自定义表单）：用户可以通过自定义表单提交回复。

更多信息，请参阅 Telegram Bot API 的 [`sendMessage`](https://core.telegram.org/bots/api#sendmessage) 文档。

{% hint style="warning" %}
**发送消息的限制**

Telegram 普通批量发送的速率上限约为每秒 30 条消息。如果预计会达到此上限，请参阅[分批发送超过 30 条消息](common-issues.md#send-more-than-30-messages-per-second)，按建议分批并等待，遵守该速率限制。
{% endhint %}

### Send and Wait for Response 附加字段 <a href="#send-and-wait-for-response-additional-fields" id="send-and-wait-for-response-additional-fields"></a>

可用的附加字段取决于所选的 **Response Type**（响应类型）。

#### Approval（审批） <a href="#approval" id="approval"></a>

**Approval**（审批）响应类型会添加以下选项：

* **Type of Approval**（审批类型）：选择仅显示批准按钮，还是同时显示批准和拒绝按钮。
* **Button Label**（按钮标签）：批准或拒绝按钮的标签。批准和拒绝操作的默认标签分别为 `✅ Approve` 和 `❌ Decline`。
* **Limit Wait Time**（限制等待时间）：选择工作流是否在达到指定时限后自动恢复执行。可设置时间间隔，或指定具体时间点。
* **Approve Within Chat**（在聊天内审批）：选择审批人是否直接点击消息按钮完成响应，而无需在浏览器中打开链接。此选项位于 **Advanced Interactivity**（高级交互）部分。更多信息，请参阅下文的[在聊天内审批](#approve-within-chat)。

#### 在聊天内审批 <a id="approve-within-chat"></a>

{% hint style="info" %}
**要求**

要使用 **Approve Within Chat**（在聊天内审批），你的 n8n 实例必须可以通过互联网以 HTTPS 访问，端口为 `443`、`80`、`88` 或 `8443`（Telegram 支持的 webhook 端口）。无需在 Telegram 端自行注册，也无需配置额外密钥：n8n 会使用现有的 [Telegram 凭据](../../credentials/telegram.md)为你注册 webhook。
{% endhint %}

开启 **Approve Within Chat**（在聊天内审批）后，审批人直接点击消息按钮即可响应，无需在浏览器中打开链接：

* 节点输出会包含响应者的 Telegram 用户 ID、用户名和姓名。
* 可以限制允许响应的用户。其他人点击按钮不会结束等待中的执行，并且会看到提示其未获授权的弹窗。
* 作出决定后，n8n 会编辑消息；具体行为取决于下文的 **After Decision**（作出决定后）选项。

Telegram 每个机器人只允许配置一个 webhook。如果同一机器人还用于 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)，n8n 会自动让触发器与 **Approve Within Chat**（在聊天内审批）共用该 webhook，无需另建机器人。如果触发器在此功能推出之前就已启用，请重新激活其工作流（或将其更新到最新版本），让按钮点击事件能够到达 n8n。如果机器人的 webhook 已被 n8n 以外的服务使用，请为 **Approve Within Chat** 使用另一个机器人，或关闭此选项。

{% hint style="info" %}
**回退为链接按钮**

如果实例无法通过公共 HTTPS 访问，或关闭了 **Approve Within Chat**（在聊天内审批），节点会回退为发送链接按钮。
{% endhint %}

{% hint style="info" %}
**私聊、群组和频道**

按钮点击在私聊、群组和频道中的行为一致。与其他 **Message**（消息）操作一样，机器人需要先加入频道，才能在其中发布和编辑消息。更多信息，请参阅[常见问题 | 将机器人添加到 Telegram 频道](common-issues.md#add-a-bot-to-a-telegram-channel)。
{% endhint %}

开启 **Approve Within Chat**（在聊天内审批）后，同一 **Advanced Interactivity**（高级交互）部分会在该选项下方显示以下字段：

* **Restrict Who Can Approve**（限制审批人）：输入允许批准或拒绝的 Telegram 用户 ID，多个 ID 以逗号分隔。留空时，任何可以看到消息的人都可以响应。
* **Unauthorized Reply**（未授权提示）：不在审批人列表中的用户点击按钮时，以 Telegram 弹窗向其显示的消息。
* **After Decision**（作出决定后）：选择有人响应后如何处理消息：
    * **Show Outcome and Remove Buttons**（显示结果并移除按钮）：移除按钮，并添加一行文字，显示谁批准或拒绝了请求。
    * **Remove Buttons Only**（仅移除按钮）：移除按钮，不添加结果文字。
    * **Keep Message Unchanged**（保持消息不变）：保留消息原样。

#### Free Text（自由文本） <a href="#free-text" id="free-text"></a>

使用 Free Text（自由文本）响应类型时，可使用以下选项：

* **Message Button Label**（消息按钮标签）：消息按钮显示的标签，默认值为 `Respond`。
* **Response Form Title**（响应表单标题）：供用户提交回复的表单标题。
* **Response Form Description**（响应表单描述）：供用户提交回复的表单描述。
* **Response Form Button Label**（响应表单按钮标签）：表单中用于提交回复的按钮标签，默认值为 `Submit`。
* **Limit Wait Time**（限制等待时间）：选择工作流是否在达到指定时限后自动恢复执行。可设置时间间隔，或指定具体时间点。

#### Custom Form（自定义表单） <a href="#custom-form" id="custom-form"></a>

使用 Custom Form（自定义表单）响应类型时，可使用所需的字段和选项构建表单。

可以使用 [n8n Form 触发器的表单元素](../../core-nodes/n8n-nodes-base.formtrigger.md#form-elements)中介绍的设置来自定义各个表单元素。要添加更多字段，选择 **Add Form Element**（添加表单元素）按钮。

还可使用以下选项：

* **Message Button Label**（消息按钮标签）：消息按钮显示的标签，默认值为 `Respond`。
* **Response Form Title**（响应表单标题）：供用户提交回复的表单标题。
* **Response Form Description**（响应表单描述）：供用户提交回复的表单描述。
* **Response Form Button Label**（响应表单按钮标签）：表单中用于提交回复的按钮标签，默认值为 `Submit`。
* **Limit Wait Time**（限制等待时间）：选择工作流是否在达到指定时限后自动恢复执行。可设置时间间隔，或指定具体时间点。

## Send Photo（发送照片） <a href="#send-photo" id="send-photo"></a>

此操作通过 Bot API 的 [sendPhoto](https://core.telegram.org/bots/api#sendphoto) 方法向聊天发送照片。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Send Photo**（发送照片）。
* **Chat ID**（聊天 ID）：输入要接收照片的聊天 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Binary File**（二进制文件）：要发送节点本身提供的二进制文件，开启此选项。开启后，必须在 **Input Binary Field**（输入二进制字段）中指定包含待发送文件的字段。
* **Photo**（照片）：不使用 **Binary File**（二进制文件）时，在此指定要发送的照片。传入 `file_id` 可发送 Telegram 服务器上已有的文件（推荐），也可提供 HTTP URL，让 Telegram 从互联网获取文件。
* **Reply Markup**（回复界面）：使用此参数设置更多界面选项。有关这些选项及其用法，请参阅 [Reply Markup 参数](message-operations.md#reply-markup-parameters)。

更多信息，请参阅 Telegram Bot API 的 [sendPhoto](https://core.telegram.org/bots/api#sendphoto) 文档。

### Send Photo 附加字段 <a href="#send-photo-additional-fields" id="send-photo-additional-fields"></a>

使用 **Additional Fields**（附加字段）设置 Telegram 的 sendPhoto 方法中的可选字段，进一步调整节点行为。选择 **Add Field**（添加字段）可添加以下任意字段：

* **Caption**（说明文字）：输入文件的说明文字，最多 1024 个字符。
* **Disable Notification**（禁用通知）：开启时静默发送，关闭时使用普通通知发送。
* **Parse Mode**（解析模式）：选择相关文本的解析格式，可选 **HTML**（默认）、**Markdown (Legacy)**（旧版 Markdown）或 **MarkdownV2**。更多信息，请参阅 Telegram 的[格式选项](https://core.telegram.org/bots/api#formatting-options)。
* **Reply To Message ID**（回复目标消息 ID）：如果此消息是回复，输入被回复消息的 ID。
* **Message Thread ID**（消息线程 ID）：输入目标论坛消息线程（话题）的唯一标识符，仅适用于论坛超级群组。

## Send Sticker（发送贴纸） <a href="#send-sticker" id="send-sticker"></a>

此操作通过 Bot API 的 [sendSticker](https://core.telegram.org/bots/api#sendsticker) 方法发送静态 .WEBP、动画 .TGS 或视频 .WEBM 贴纸。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Send Sticker**（发送贴纸）。
* **Chat ID**（聊天 ID）：输入要接收贴纸的聊天 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Binary File**（二进制文件）：要发送节点本身提供的二进制文件，开启此选项。开启后，必须在 **Input Binary Field**（输入二进制字段）中指定包含待发送文件的字段。
* **Sticker**（贴纸）：不使用 **Binary File**（二进制文件）时，在此指定要发送的贴纸。传入 `file_id` 可发送 Telegram 服务器上已有的文件（推荐），也可提供 HTTP URL，让 Telegram 从互联网获取文件。
* **Reply Markup**（回复界面）：使用此参数设置更多界面选项。有关这些选项及其用法，请参阅 [Reply Markup 参数](message-operations.md#reply-markup-parameters)。

更多信息，请参阅 Telegram Bot API 的 [sendSticker](https://core.telegram.org/bots/api#sendsticker) 文档。

### Send Sticker 附加字段 <a href="#send-sticker-additional-fields" id="send-sticker-additional-fields"></a>

使用 **Additional Fields**（附加字段）设置 Telegram 的 sendSticker 方法中的可选字段，进一步调整节点行为。选择 **Add Field**（添加字段）可添加以下任意字段：

* **Disable Notification**（禁用通知）：开启时静默发送，关闭时使用普通通知发送。
* **Reply To Message ID**（回复目标消息 ID）：如果此消息是回复，输入被回复消息的 ID。
* **Message Thread ID**（消息线程 ID）：输入目标论坛消息线程（话题）的唯一标识符，仅适用于论坛超级群组。

## Send Video（发送视频） <a href="#send-video" id="send-video"></a>

此操作通过 Bot API 的 [sendVideo](https://core.telegram.org/bots/api#sendvideo) 方法向聊天发送视频。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Send Video**（发送视频）。
* **Chat ID**（聊天 ID）：输入要接收视频的聊天 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Binary File**（二进制文件）：要发送节点本身提供的二进制文件，开启此选项。开启后，必须在 **Input Binary Field**（输入二进制字段）中指定包含待发送文件的字段。
* **Video**（视频）：不使用 **Binary File**（二进制文件）时，在此指定要发送的视频。传入 `file_id` 可发送 Telegram 服务器上已有的文件（推荐），也可提供 HTTP URL，让 Telegram 从互联网获取文件。
* **Reply Markup**（回复界面）：使用此参数设置更多界面选项。有关这些选项及其用法，请参阅 [Reply Markup 参数](message-operations.md#reply-markup-parameters)。

更多信息，请参阅 Telegram Bot API 的 [sendVideo](https://core.telegram.org/bots/api#sendvideo) 文档。

### Send Video 附加字段 <a href="#send-video-additional-fields" id="send-video-additional-fields"></a>

使用 **Additional Fields**（附加字段）设置 Telegram 的 sendVideo 方法中的可选字段，进一步调整节点行为。选择 **Add Field**（添加字段）可添加以下任意字段：

* **Caption**（说明文字）：输入视频的说明文字，最多 1024 个字符。
* **Disable Notification**（禁用通知）：开启时静默发送，关闭时使用普通通知发送。
* **Duration**（时长）：输入视频的持续时间，单位为秒。
* **Height**（高度）：输入视频的高度。
* **Parse Mode**（解析模式）：选择相关文本的解析格式，可选 **HTML**（默认）、**Markdown (Legacy)**（旧版 Markdown）或 **MarkdownV2**。更多信息，请参阅[格式选项](https://core.telegram.org/bots/api#formatting-options)。
* **Reply To Message ID**（回复目标消息 ID）：如果此消息是回复，输入被回复消息的 ID。
* **Message Thread ID**（消息线程 ID）：输入目标论坛消息线程（话题）的唯一标识符，仅适用于论坛超级群组。
* **Thumbnail**（缩略图）：为所发送的文件添加缩略图。如果服务端支持为该文件生成缩略图，可忽略此字段。缩略图应符合以下要求：
  * JPEG 格式。
  * 文件大小小于 200 KB。
  * 宽度和高度均小于 320px。
* **Width**（宽度）：输入视频的宽度。

## Unpin Chat Message（取消置顶聊天消息） <a href="#unpin-chat-message" id="unpin-chat-message"></a>

此操作通过 Bot API 的 [unpinChatMessage](https://core.telegram.org/bots/api#unpinchatmessage) 方法取消聊天中一条消息的置顶状态。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Message**（消息）。
* **Operation**（操作）：选择 **Unpin Chat Message**（取消置顶聊天消息）。
* **Chat ID**（聊天 ID）：输入要取消消息置顶的聊天 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Message ID**（消息 ID）：输入要取消置顶的消息的唯一标识符。

更多信息，请参阅 Telegram Bot API 的 [unpinChatMessage](https://core.telegram.org/bots/api#unpinchatmessage) 文档。

## Reply Markup（回复界面）参数 <a href="#reply-markup-parameters" id="reply-markup-parameters"></a>

对于大多数 **Message**（消息）资源中的 **Send**（发送）操作，例如 Send Animation（发送动画）和 Send Audio（发送音频），可使用 **Reply Markup**（回复界面）参数设置更多界面选项：

* **Force Reply**（强制回复）：Telegram 客户端会像用户选中机器人消息并点击 **Reply**（回复）一样，自动向用户显示回复界面。有关此选项的进一步说明，请参阅 [Force Reply 参数](message-operations.md#force-reply-parameters)。
* **Inline Keyboard**（内联键盘）：在消息旁显示内联键盘。有关此选项的进一步说明，请参阅 [Inline Keyboard 参数](message-operations.md#inline-keyboard-parameters)。
* **Reply Keyboard**（回复键盘）：显示包含回复选项的自定义键盘。有关此选项的进一步说明，请参阅 [Reply Keyboard 参数](message-operations.md#reply-keyboard-parameters)。
* **Reply Keyboard Remove**（移除回复键盘）：Telegram 客户端会移除当前自定义键盘，并显示默认的字母键盘。原文链接指向 [Reply Keyboard 参数](message-operations.md#reply-keyboard-remove-parameters)；移除键盘的具体选项请参阅下文 Reply Keyboard Remove 参数。

{% hint style="info" %}
**Telegram Business 账户**

对于频道消息和代表 Telegram Business 账户发送的消息，Telegram 对以下选项有限制：

* Force Reply（强制回复）
* Reply Keyboard（回复键盘）
* Reply Keyboard Remove（移除回复键盘）
{% endhint %}

### Force Reply（强制回复）参数 <a href="#force-reply-parameters" id="force-reply-parameters"></a>

如果希望在保留隐私模式的同时构建方便用户操作的分步界面，**Force Reply**（强制回复）会很有用。

如果选择 **Reply Markup > Force Reply**（回复界面 > 强制回复），可设置以下 **Force Reply** 参数：

* **Force Reply**（强制回复）：开启后，按上述方式向用户显示回复界面。
* **Selective**（选择性应用）：若只希望以下用户收到强制回复界面，请开启此选项：
  * 在消息文本中被 `@mentioned` 的用户。
  * 如果当前发送的消息是一条回复，则包括被回复消息的发送者。

更多信息，请参阅 [ForceReply](https://core.telegram.org/bots/api#forcereply)。

### Inline Keyboard（内联键盘）参数 <a href="#inline-keyboard-parameters" id="inline-keyboard-parameters"></a>

如果选择 **Reply Markup > Inline Keyboard**（回复界面 > 内联键盘），使用 **Add Button**（添加按钮）定义要显示的内联键盘按钮。使用 **Add Keyboard Row**（添加键盘行）可为键盘添加更多行。

更多信息，请参阅 [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) 和 [InlineKeyboardButtons](https://core.telegram.org/bots/api#inlinekeyboardbutton)。

### Reply Keyboard（回复键盘）参数 <a href="#reply-keyboard-parameters" id="reply-keyboard-parameters"></a>

如果选择 **Reply Markup > Reply Keyboard**（回复界面 > 回复键盘），在 **Reply Keyboard**（回复键盘）部分定义回复键盘的按钮和行。

使用 **Reply Keyboard Options**（回复键盘选项）进一步调整键盘行为：

* **Resize Keyboard**（调整键盘大小）：开启时，请求 Telegram 客户端调整键盘的垂直尺寸，使其恰好容纳内容；关闭时，使用与应用标准键盘相同的高度。
* **One Time Keyboard**（一次性键盘）：开启时，用户使用键盘后，Telegram 客户端会立即隐藏键盘；关闭时，继续显示键盘。
* **Selective**（选择性应用）：若只希望向以下用户显示键盘，请开启此选项：
  * 在消息文本中被 `@mentioned` 的用户。
  * 如果当前发送的消息是一条回复，则包括被回复消息的发送者。

更多信息，请参阅 [ReplyKeyboardMarkup](https://core.telegram.org/bots/api#replykeyboardmarkup)。

### Reply Keyboard Remove（移除回复键盘）参数 <a href="#reply-keyboard-remove-parameters" id="reply-keyboard-remove-parameters"></a>

如果选择 **Reply Markup > Reply Keyboard Remove**（回复界面 > 移除回复键盘），可设置以下 **Reply Keyboard Remove** 参数：

* **Remove Keyboard**（移除键盘）：开启时，请求 Telegram 客户端移除自定义键盘；关闭时，保留该键盘。
* **Selective**（选择性应用）：若只希望为以下用户移除键盘，请开启此选项：
  * 在消息文本中被 `@mentioned` 的用户。
  * 如果当前发送的消息是一条回复，则包括被回复消息的发送者。

更多信息，请参阅 [ReplyKeyboardRemove](https://core.telegram.org/bots/api#replykeyboardremove)。
