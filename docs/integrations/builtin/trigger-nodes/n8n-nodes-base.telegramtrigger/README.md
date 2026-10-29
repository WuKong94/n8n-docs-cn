---
title: Telegram 触发器节点文档
description: 了解如何在 n8n 中使用 Telegram 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: critical
nodeTitle: n8n-nodes-base.telegramtrigger
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Telegram 触发器节点 <a href="#telegram-trigger-node" id="telegram-trigger-node"></a>

[Telegram](https://telegram.org/) 是基于云的即时通信和网络语音服务。用户可以发送消息，交换照片、视频、贴纸、音频及任意类型的文件。本页列出了 Telegram Trigger 节点可响应的事件，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Telegram 凭据文档](../../credentials/telegram.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Telegram Trigger 集成](https://n8n.io/integrations/telegram-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

- **`*`**：除“Chat Member”“Message Reaction”和“Message Reaction Count”之外的所有更新。这是 Telegram API 的默认行为，因为这些事件会产生大量更新调用。
- **Business Connection**（商业账户连接）：机器人连接到商业账户、断开与商业账户的连接，或用户编辑现有机器人连接时触发。
- **Business Message**（商业消息）：收到来自已连接商业账户的新消息时触发。
- **Callback Query**（回调查询）：收到新的回调查询时触发。
- **Channel Post**（频道帖子）：收到任意类型的新频道帖子时触发，包括文字、照片、贴纸等。
- **Chat Boost**（聊天助力）：聊天助力被添加或变更时触发。机器人必须是聊天管理员，才能接收这些更新。
- **Chat Join Request**（加入聊天请求）：有人发送加入聊天的请求时触发。机器人必须在聊天中具有 `can_invite_users` 管理员权限，才能接收这些更新。
- **Chat Member**（聊天成员）：聊天成员的状态更新时触发。机器人必须是聊天管理员。
- **Chosen Inline Result**（已选择的内联结果）：用户选中的内联查询结果被发送时触发。为机器人启用这些更新的方法，请参阅 Telegram API 文档中的[反馈收集](https://core.telegram.org/bots/inline#collecting-feedback)。
- **Deleted Business Messages**（商业消息已删除）：已连接的商业账户中的消息被删除时触发。
- **Edited Business Message**（商业消息已编辑）：已连接的商业账户中的消息出现新版本时触发。
- **Edited Channel Post**（频道帖子已编辑）：机器人已知的频道帖子被编辑并产生新版本时触发。
- **Edited Message**（消息已编辑）：机器人已知的消息被编辑并产生新版本时触发。
- **Inline Query**（内联查询）：收到新的内联查询时触发。
- **Message**（消息）：收到任意类型的新消息时触发，包括文字、照片、贴纸等。
- **Message Reaction**（消息表情回应）：用户更改消息的表情回应时触发。机器人必须是聊天管理员。不会收到机器人设置的表情回应对应的更新。
- **Message Reaction Count**（消息表情回应计数）：带有匿名表情回应的消息，其表情回应发生变更时触发。机器人必须是聊天管理员。这些更新会分组发送，可能延迟几分钟。
- **My Chat Member**（机器人自身的聊天成员状态）：机器人在聊天中的成员状态更新时触发。在私聊中，仅当用户屏蔽或取消屏蔽机器人时，才会收到此更新。
- **Poll**（投票）：出现新的投票状态时触发。机器人只会收到已停止的投票，以及由机器人发送的投票的更新。
- **Poll Answer**（投票回答）：用户更改非匿名投票的回答时触发。机器人只会收到由该机器人自身发起的投票中的新选票。
- **Pre-Checkout Query**（结账前查询）：收到新的结账前查询时触发，包含完整的结账信息。
- **Purchased Paid Media**（已购买付费媒体）：用户购买机器人在非频道聊天中发送的、载荷非空的付费媒体时触发。
- **Removed Chat Boost**（聊天助力已移除）：聊天助力被移除时触发。机器人必须是聊天管理员，才能接收这些更新。
- **Shipping Query**（配送查询）：收到新的配送查询时触发，仅适用于价格可变的发票。

某些**事件可能需要额外权限**，更多信息请参阅 [Telegram API 文档](https://core.telegram.org/bots/api#getting-updates)。

## 选项 <a href="#options" id="options"></a>

- **Download Images/Files**（下载图片或文件）：是否下载附加的图片或文件，将其包含在输出数据中。
    - **Image Size**（图片大小）：启用 **Download Images/Files**（下载图片或文件）后，此项配置要下载的图片大小，默认下载大图。
- **Restrict to Chat IDs**（限定聊天 ID）：仅对所列聊天 ID 的事件触发，多个聊天 ID 以逗号分隔。
- **Restrict to User IDs**（限定用户 ID）：仅对所列用户 ID 的事件触发，多个用户 ID 以逗号分隔。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Telegram 提供应用节点。更多信息请参阅 [Telegram 节点文档](../../app-nodes/n8n-nodes-base.telegram/README.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/telegram-trigger/)。

API 的详细信息，请参阅 [Telegram API 文档](https://core.telegram.org/bots/api)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见问题及建议的解决办法，请参阅[常见问题](common-issues.md)。
