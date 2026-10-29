---
title: Telegram 凭据
contentType:
- integration
- reference
priority: critical
nodeTitle: Telegram 凭据
originalFilePath: integrations/builtin/credentials/telegram.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/telegram
url: https://docs.n8n.io/integrations/builtin/credentials/telegram
description: Telegram 凭据文档。使用这些凭据在 n8n 中完成 Telegram 的身份验证。
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


# Telegram 凭据 <a id="telegram-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Telegram](../app-nodes/n8n-nodes-base.telegram/README.md)
* [Telegram Trigger（触发器）](../trigger-nodes/n8n-nodes-base.telegramtrigger/README.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Telegram](https://telegram.org/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API 机器人访问令牌

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Telegram Bot API 文档](https://core.telegram.org/bots/api)。

创建和使用机器人的更多信息，请参阅 [Telegram 机器人功能](https://core.telegram.org/bots/features)文档。

## 使用 API 机器人访问令牌 <a href="#using-api-bot-access-token" id="using-api-bot-access-token"></a>

配置此凭据需要：

* 机器人的 **Access Token**（访问令牌）

生成访问令牌的步骤如下：

1. 与 [BotFather](https://telegram.me/BotFather) 开始聊天。
2. 输入 `/newbot` 命令，创建新机器人。
3. BotFather 会要求提供新机器人的名称和用户名：
   * **name**（名称）是在联系详情等位置显示的机器人名称，之后可以更改。
   * **username**（用户名）是用于搜索、提及和 t.me 链接的简短名称。创建时须遵循以下规则：
     * 长度必须介于 5 到 32 个字符之间。
     * 不区分大小写。
     * 只能包含拉丁字母、数字和下划线。
     * 必须以 `bot` 结尾，例如 `tetris_bot` 或 `TetrisBot`。
     * 用户名之后无法更改。
4. 复制 BotFather 生成的机器人 **token**（令牌），填入 n8n 的 **Access Token**（访问令牌）。

更多信息，请参阅 [BotFather 创建新机器人的文档](https://core.telegram.org/bots/features#creating-a-new-bot)。
