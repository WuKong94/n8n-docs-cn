---
title: Telegram 节点常见问题
contentType:
- integration
- reference
priority: critical
nodeTitle: Telegram 节点常见问题
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues
description: 了解 n8n 工作流自动化平台中 Telegram 节点的常见问题，包括问题详情和建议的解决方法。
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


# 常见问题 <a id="common-issues"></a>

本页介绍 [Telegram 节点](./README.md)的一些常见错误和问题，以及解决或排查步骤。

## 将机器人添加到 Telegram 频道 <a href="#add-a-bot-to-a-telegram-channel" id="add-a-bot-to-a-telegram-channel"></a>

机器人要向频道发送消息，必须先加入该频道。若尚未将机器人添加到频道中，你会看到描述类似于 `Error: Forbidden: bot is not a participant of the channel` 的错误。

按以下步骤将机器人添加到频道：

1. 在 Telegram 应用中打开目标频道，然后选择频道名称。
2. 如果要通过公开用户名访问频道，将其设为 **public channel**（公开频道）；使用数字聊天 ID 访问私有频道时，无需将频道公开。
3. 选择 **Administrators**（管理员）> **Add Admin**（添加管理员）。
4. 搜索机器人的用户名并选中它。
5. 选择右上角的勾选标记，将机器人添加到频道。

## 获取聊天 ID <a href="#get-the-chat-id" id="get-the-chat-id"></a>

`@channelusername` 形式适用于具有公开用户名的频道或超级群组。没有可用公开用户名的群组等聊天，需要使用其聊天 ID。

有三种方式可获取该 ID：

1. 通过 Telegram Trigger：在工作流中使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md) 节点获取聊天 ID。此节点支持多种触发事件，执行成功后会返回聊天 ID。
2. 通过网页浏览器：在浏览器中打开 Telegram，再打开群聊。原文提供的查找方式是取字母“g”后的一串数字作为群组聊天 ID；在 n8n 中输入该 ID 时，在前面加上 `-`。
3. 邀请 [@RawDataBot](https://t.me/RawDataBot) 加入群组：添加后，该机器人会输出一个包含 `chat` 对象的 JSON 文件。该对象的 `id` 就是群组聊天 ID。获取后，将 RawDataBot 从群组中移除。

## 分批发送超过 30 条消息 <a href="#send-more-than-30-messages-per-second" id="send-more-than-30-messages-per-second"></a>

Telegram API 的普通批量发送[速率限制](https://core.telegram.org/bots/faq#broadcasting-to-users)约为每秒 30 条消息。要发送总计超过 30 条的消息，可按以下步骤分批并等待；这种做法用于遵守速率限制，并不能提高每秒速率上限：

1. **Loop Over Items node**（循环处理项目节点）：使用 [Loop Over Items](../../core-nodes/n8n-nodes-base.splitinbatches.md) 节点，每批从数据库获取最多 30 个聊天 ID。
2. **Telegram node**（Telegram 节点）：将 Telegram 节点连接到 Loop Over Items 节点。使用 **Expression Editor**（表达式编辑器）选择 Loop Over Items 节点中的聊天 ID。
3. **Code node**（代码节点）：将 [Code](../../core-nodes/n8n-nodes-base.code/README.md) 节点连接到 Telegram 节点，使用 Code 节点等待几秒后再获取下一批聊天 ID，并将此节点连接回 Loop Over Items 节点。

也可以使用此[工作流](https://n8n.io/workflows/772)。

## 从已发送消息中移除 n8n 标识 <a href="#remove-the-n8n-attribution-from-sent-messages" id="remove-the-n8n-attribution-from-sent-messages"></a>

使用此节点[发送 Telegram 消息](message-operations.md#send-message)时，消息末尾会自动附加以下 n8n 标识：

> This message was sent automatically with n8n（此消息由 n8n 自动发送）

按以下步骤移除此标识：

1. 在节点的 **Additional Fields**（附加字段）部分，选择 **Add Field**（添加字段）。
2. 选择 **Append n8n attribution**（附加 n8n 标识）。
3. 关闭该开关。

更多信息，请参阅 [Send Message 附加字段](message-operations.md#send-message-additional-fields)。
