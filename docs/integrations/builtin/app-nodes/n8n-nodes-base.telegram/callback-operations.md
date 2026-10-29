---
title: Telegram 节点回调操作
contentType:
- integration
- reference
priority: critical
nodeTitle: Telegram 节点回调操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.telegram/callback-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/callback-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/callback-operations
description: 了解 n8n 工作流自动化平台中 Telegram 节点的回调操作，以及各项操作的配置详情。
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


# 回调操作 <a id="callback-operations"></a>

使用这些操作回答来自内联键盘的回调查询，或回答内联查询。有关 Telegram 节点本身的更多信息，请参阅 [Telegram](./README.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## Answer Query（回答查询） <a href="#answer-query" id="answer-query"></a>

此操作通过 Bot API 的 [answerCallbackQuery](https://core.telegram.org/bots/api#answercallbackquery) 方法，回答来自[内联键盘](https://core.telegram.org/bots/features#inline-keyboards)的回调查询。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Callback**（回调）。
* **Operation**（操作）：选择 **Answer Query**（回答查询）。
* **Query ID**（查询 ID）：输入要回答的查询的唯一标识符。
  * 要将查询 ID 直接传入此节点，可使用由 **Callback Query**（回调查询）事件触发的 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md) 节点。
* **Results**（结果）：原文在此列出用于回答查询的 JSON 序列化结果数组，并引用 Telegram [InlineQueryResults](https://core.telegram.org/bots/api#inlinequeryresult) 格式文档。译注：结果数组属于 answerInlineQuery，answerCallbackQuery 不接受此参数。

更多信息，请参阅 Telegram Bot API 的 [answerCallbackQuery](https://core.telegram.org/bots/api#answercallbackquery) 文档。

### Answer Query 附加字段 <a href="#answer-query-additional-fields" id="answer-query-additional-fields"></a>

使用 **Additional Fields**（附加字段）进一步调整节点行为。选择 **Add Field**（添加字段）可添加以下任意字段：

* **Cache Time**（缓存时间）：输入客户端可缓存回调查询结果的最长时间，单位为秒。Telegram 对此方法的默认值为 `0` 秒。
* **Show Alert**（显示弹窗）：Telegram 可以在聊天界面顶部以通知形式显示回答，也可以使用弹窗。关闭时使用默认的顶部通知；开启时以弹窗显示回答。
* **Text**（文本）：如果要在回答中显示文本，在此输入，最多 200 个字符。
* **URL**：输入要由用户客户端打开的 URL。更多信息，请参阅 Telegram Bot API 的 [answerCallbackQuery](https://core.telegram.org/bots/api#answercallbackquery) 文档中 **url** 参数的说明。

## Answer Inline Query（回答内联查询） <a href="#answer-inline-query" id="answer-inline-query"></a>

此操作通过 Bot API 的 [answerInlineQuery](https://core.telegram.org/bots/api#answerinlinequery) 方法回答内联查询。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Callback**（回调）。
* **Operation**（操作）：选择 **Answer Inline Query**（回答内联查询）。
* **Query ID**（查询 ID）：输入要回答的查询的唯一标识符。
  * 要将查询 ID 直接传入此节点，可使用由 **Inline Query**（内联查询）事件触发的 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md) 节点。
* **Results**（结果）：输入要作为查询回答的 JSON 序列化结果数组。数组格式的更多信息，请参阅 Telegram [InlineQueryResults](https://core.telegram.org/bots/api#inlinequeryresult) 文档。

Telegram 允许每次查询最多返回 50 个结果。

更多信息，请参阅 Telegram Bot API 的 [answerInlineQuery](https://core.telegram.org/bots/api#answerinlinequery) 文档。

### Answer Inline Query 附加字段 <a href="#answer-inline-query-additional-fields" id="answer-inline-query-additional-fields"></a>

使用 **Additional Fields**（附加字段）进一步调整节点行为。选择 **Add Field**（添加字段）可添加以下任意字段：

* **Cache Time**（缓存时间）：服务端可缓存内联查询结果的最长时间，单位为秒。Telegram 对此方法的默认值为 `300` 秒。译注：原文此处误写为客户端缓存回调查询结果。
* **Show Alert**（显示弹窗）：原文在此列出顶部通知与弹窗的切换选项（关闭时使用顶部通知，开启时使用弹窗）。译注：这是 answerCallbackQuery 的选项，不是 answerInlineQuery 的顶层参数。
* **Text**（文本）：原文在此列出最多 200 个字符的回答文本。译注：这是 answerCallbackQuery 的通知文本参数，不是 answerInlineQuery 的顶层参数。
* **URL**：原文在此列出由用户客户端打开的 URL。译注：此处所述选项属于 answerCallbackQuery，不是 answerInlineQuery 的顶层参数。
