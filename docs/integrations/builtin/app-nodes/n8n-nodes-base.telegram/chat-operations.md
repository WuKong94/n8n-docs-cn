---
title: Telegram 节点聊天操作
contentType:
- integration
- reference
priority: critical
nodeTitle: Telegram 节点聊天操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations
description: 了解 n8n 工作流自动化平台中 Telegram 节点的聊天操作，以及各项操作的配置详情。
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


# 聊天操作 <a id="chat-operations"></a>

使用这些操作获取聊天、成员和管理员信息，退出聊天，以及设置聊天标题和描述。有关 Telegram 节点本身的更多信息，请参阅 [Telegram](./README.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## Get Chat（获取聊天信息） <a href="#get-chat" id="get-chat"></a>

此操作通过 Bot API 的 [getChat](https://core.telegram.org/bots/api#getchat) 方法获取聊天的最新信息。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Chat**（聊天）。
* **Operation**（操作）：选择 **Get**（获取）。
* **Chat ID**（聊天 ID）：输入目标聊天的 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。

更多信息，请参阅 Telegram Bot API 的 [getChat](https://core.telegram.org/bots/api#getchat) 文档。

## Get Administrators（获取管理员） <a href="#get-administrators" id="get-administrators"></a>

此操作通过 Bot API 的 [getChatAdministrators](https://core.telegram.org/bots/api#getchatadministrators) 方法获取聊天的管理员列表。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Chat**（聊天）。
* **Operation**（操作）：选择 **Get Administrators**（获取管理员）。
* **Chat ID**（聊天 ID）：输入目标聊天的 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。

更多信息，请参阅 Telegram Bot API 的 [getChatAdministrators](https://core.telegram.org/bots/api#getchatadministrators) 文档。

## Get Chat Member（获取聊天成员） <a href="#get-chat-member" id="get-chat-member"></a>

此操作通过 Bot API 的 [getChatMember](https://core.telegram.org/bots/api#getchatmember) 方法获取聊天成员的详细信息。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Chat**（聊天）。
* **Operation**（操作）：选择 **Get Member**（获取成员）。
* **Chat ID**（聊天 ID）：输入目标聊天的 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **User ID**（用户 ID）：输入要获取其信息的用户的唯一标识符。

更多信息，请参阅 Telegram Bot API 的 [getChatMember](https://core.telegram.org/bots/api#getchatmember) 文档。

## Leave Chat（退出聊天） <a href="#leave-chat" id="leave-chat"></a>

此操作通过 Bot API 的 [leaveChat](https://core.telegram.org/bots/api#leavechat) 方法退出聊天。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Chat**（聊天）。
* **Operation**（操作）：选择 **Leave**（退出）。
* **Chat ID**（聊天 ID）：输入要退出的聊天的 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。

更多信息，请参阅 Telegram Bot API 的 [leaveChat](https://core.telegram.org/bots/api#leavechat) 文档。

## Set Description（设置描述） <a href="#set-description" id="set-description"></a>

此操作通过 Bot API 的 [setChatDescription](https://core.telegram.org/bots/api#setchatdescription) 方法设置聊天描述。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Chat**（聊天）。
* **Operation**（操作）：选择 **Set Description**（设置描述）。
* **Chat ID**（聊天 ID）：输入目标聊天的 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Description**（描述）：输入要为聊天设置的新描述，最多 255 个字符。

更多信息，请参阅 Telegram Bot API 的 [setChatDescription](https://core.telegram.org/bots/api#setchatdescription) 文档。

## Set Title（设置标题） <a href="#set-title" id="set-title"></a>

此操作通过 Bot API 的 [setChatTitle](https://core.telegram.org/bots/api#setchattitle) 方法设置聊天标题。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **Chat**（聊天）。
* **Operation**（操作）：选择 **Set Title**（设置标题）。
* **Chat ID**（聊天 ID）：输入目标聊天的 ID；使用频道用户名时，格式为 `@channelusername`。
  * 要将聊天 ID 直接传入此节点，可使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)（Telegram 触发器）节点。更多信息，请参阅[常见问题 | 获取聊天 ID](common-issues.md#get-the-chat-id)。
* **Title**（标题）：输入要为聊天设置的新标题，最多 128 个字符。译注：原文的 255 与 Telegram setChatTitle 的标题上限不符，此处按该方法修正。

更多信息，请参阅 Telegram Bot API 的 [setChatTitle](https://core.telegram.org/bots/api#setchattitle) 文档。
