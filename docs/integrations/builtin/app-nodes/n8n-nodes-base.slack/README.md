---
title: Slack 节点文档
description: 了解如何在 n8n 中使用 Slack 节点，并按照技术文档将 Slack 节点集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: Slack 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.slack.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Slack 节点 <a href="#slack-node" id="slack-node"></a>

使用 Slack 节点自动处理 Slack 中的工作，并将其与其他应用集成。n8n 内置支持多种 Slack 功能，包括创建、归档和关闭频道，获取用户及文件，以及删除消息。

本页列出了 Slack 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Slack 凭据](../../credentials/slack.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/hitl-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* **Channel**（频道）
    * **Archive**（归档）频道。
    * **Close**（关闭）私信或多人私信。
    * **Create**（创建）基于公开或私密频道的会话。
    * **Get**（获取）频道信息。
    * **Get Many**（获取多项）：获取 Slack 频道列表。
    * **History**（历史记录）：获取频道的消息及事件历史。
    * **Invite**（邀请）用户加入频道。
    * **Join**（加入）已有频道。
    * **Kick**（移除成员）：从频道移除用户。
    * **Leave**（离开）频道。
    * **Member**（成员）：列出频道成员。
    * **Open**（打开）或恢复私信或多人私信。
    * **Rename**（重命名）频道。
    * **Replies**（回复）：获取发布在频道中的消息讨论串。
    * **Sets purpose**（设置用途）：设置频道用途。
    * **Sets topic**（设置主题）：设置频道主题。
    * **Unarchive**（取消归档）频道。
* **File**（文件）
    * **Get**（获取）文件。
    * **Get Many**（获取多项）：获取并筛选团队文件。
    * **Upload**（上传）：创建文件或上传已有文件。
* **Message**（消息）
    * **Delete**（删除）消息
    * **Get permalink**（获取永久链接）：获取消息的永久链接。
    * **Search**（搜索）消息
    * **Send**（发送）消息
    * **Send and Wait for Response**（发送并等待响应）：发送消息，等待接收者响应后再继续。审批人也可直接在 Slack 中响应。更多信息，请参阅 [Slack 中的审批](approvals.md)。
    * **Update**（更新）消息
* **Reaction**（回应）
    * **Add**（添加）消息回应。
    * **Get**（获取）消息的回应。
    * **Remove**（移除）消息回应。
* **Star**（星标）
    * **Add**（添加）数据项的星标。
    * **Delete**（删除）数据项的星标。
    * **Get Many**（获取多项）：获取已通过身份验证的用户的星标列表。
* **User**（用户）
    * **Get**（获取）用户信息。
    * **Get Many**（获取多项）：获取用户列表。
    * **Get User's Profile**（获取用户资料）。
    * **Get User's Status**（获取用户状态）。
    * **Update User's Profile**（更新用户资料）。
* **User Group**（用户组）
    * **Create**（创建）用户组。
    * **Disable**（禁用）用户组。
    * **Enable**（启用）用户组。
    * **Get Many**（获取多项）：获取用户组列表。
    * **Update**（更新）用户组。

## 消息搜索与版本差异 <a href="#message-search-and-version-specific-behavior" id="message-search-and-version-specific-behavior"></a>

### 搜索消息 <a href="#search-messages" id="search-messages"></a>

节点第 2.7 版及以上版本的 **Message > Search**（消息 > 搜索）操作使用[实时搜索 API](https://docs.slack.dev/apis/web-api/real-time-search-api/)（`assistant.search.context`）。节点第 2.6 版及以下版本使用已弃用的 [`search.messages`](https://api.slack.com/methods/search.messages) 端点。n8n 按节点版本控制此行为，因此不会影响仍使用节点第 2.6 版及以下版本的已有工作流。

节点第 2.7 版及以上版本：

- **新增选项**：**Channel Types**（频道类型，公开、私密、群组私信、私信）、**After** 和 **Before**（日期筛选），以及 **Keyword Search Only**（仅关键词搜索，禁用语义搜索）。
- **语义搜索**：默认情况下，Slack 可能对问题形式的查询应用语义搜索，例如以疑问词开头或以问号结尾的查询，因此结果不一定严格按字面匹配关键词。启用 **Keyword Search Only**（仅关键词搜索）可强制字面匹配。语义排序需要 Slack AI（付费套餐）。
- **数量限制**：节点第 2.7 版及以上版本移除了 **Return All**（返回全部），仅保留 **Limit**（数量限制），上限为 50。端点每次请求返回 20 条结果，且速率限制较严格，约每位用户每分钟 10 次请求，因此不适合穷尽式获取。节点第 2.6 版及以下版本保留 **Return All**。
- **身份验证**：此端点需要用户令牌，请使用 OAuth2，或在 Access Token（访问令牌）身份验证中提供用户令牌。机器人令牌无法调用此端点，且 Slack 应用必须启用 AI 功能。如果使用 OAuth2，请重新连接已有凭据，以获得新的 `search:read.*` 作用域。
- **输出字段**：结果使用 `content`、`message_ts`、`channel_id`、`channel_name` 和 `author_name`，代替原先的 `text`、`ts`、`channel` 和 `username`。

### 自定义机器人头像 <a href="#custom-bot-profile-photo" id="custom-bot-profile-photo"></a>

从节点第 2.6 版起，**Message > Send**（消息 > 发送）中的 **Custom Bot Profile Photo**（自定义机器人头像，自定义图标或表情符号）选项仅适用于 **Access Token**（访问令牌）身份验证，不适用于 OAuth2。它依赖 `chat:write.customize` 作用域，而该作用域仅适用于机器人令牌，OAuth2 用户令牌流程无法使用。节点第 2.5 版及以下版本在使用 OAuth2 时仍显示此选项，但 Slack 会忽略它。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Slack 集成模板](https://n8n.io/integrations/slack)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Slack 文档](https://api.slack.com/)。

## 所需作用域 <a href="#required-scopes" id="required-scopes"></a>

为 [Slack 凭据](../../credentials/slack.md)创建 Slack 应用后，必须为应用添加合适的作用域，节点才能正常工作。请先使用[作用域 | Slack 凭据](../../credentials/slack.md#scopes)页面列出的作用域。

如果这些作用域仍不足，请通过下表查找要使用的资源和操作，再通过链接查看 Slack API 文档，找到正确作用域。



| **资源** | **操作** | **Slack API 方法** |
|--------------|----------------------------|------------------------------------------------------------------------------------|
| Channel（频道） | Archive（归档） | [conversations.archive](https://api.slack.com/methods/conversations.archive) |
| Channel（频道） | Close（关闭） | [conversations.close](https://api.slack.com/methods/conversations.close) |
| Channel（频道） | Create（创建） | [conversations.create](https://api.slack.com/methods/conversations.create) |
| Channel（频道） | Get（获取） | [conversations.info](https://api.slack.com/methods/conversations.info) |
| Channel（频道） | Get Many（获取多项） | [conversations.list](https://api.slack.com/methods/conversations.list) |
| Channel（频道） | History（历史记录） | [conversations.history](https://api.slack.com/methods/conversations.history) |
| Channel（频道） | Invite（邀请） | [conversations.invite](https://api.slack.com/methods/conversations.invite) |
| Channel（频道） | Join（加入） | [conversations.join](https://api.slack.com/methods/conversations.join) |
| Channel（频道） | Kick（移除成员） | [conversations.kick](https://api.slack.com/methods/conversations.kick) |
| Channel（频道） | Leave（离开） | [conversations.leave](https://api.slack.com/methods/conversations.leave) |
| Channel（频道） | Member（成员） | [conversations.members](https://api.slack.com/methods/conversations.members) |
| Channel（频道） | Open（打开） | [conversations.open](https://api.slack.com/methods/conversations.open) |
| Channel（频道） | Rename（重命名） | [conversations.rename](https://api.slack.com/methods/conversations.rename) |
| Channel（频道） | Replies（回复） | [conversations.replies](https://api.slack.com/methods/conversations.replies) |
| Channel（频道） | Set Purpose（设置用途） | [conversations.setPurpose](https://api.slack.com/methods/conversations.setPurpose) |
| Channel（频道） | Set Topic（设置主题） | [conversations.setTopic](https://api.slack.com/methods/conversations.setTopic) |
| Channel（频道） | Unarchive（取消归档） | [conversations.unarchive](https://api.slack.com/methods/conversations.unarchive) |
| File（文件） | Get（获取） | [files.info](https://api.slack.com/methods/files.info) |
| File（文件） | Get Many（获取多项） | [files.list](https://api.slack.com/methods/files.list) |
| File（文件） | Upload（上传） | [files.upload](https://api.slack.com/methods/files.upload) |
| Message（消息） | Delete（删除） | [chat.delete](https://api.slack.com/methods/chat.delete) |
| Message（消息） | Get Permalink（获取永久链接） | [chat.getPermalink](https://api.slack.com/methods/chat.getPermalink) |
| Message（消息） | Search（搜索） | 节点第 2.7 版及以上版本：[assistant.search.context](https://docs.slack.dev/reference/methods/assistant.search.context)（实时搜索 API）。节点第 2.6 版及以下版本：[search.messages](https://api.slack.com/methods/search.messages)（已弃用）。 |
| Message（消息） | Send（发送） | [chat.postMessage](https://api.slack.com/methods/chat.postMessage) |
| Message（消息） | Send and Wait for Response（发送并等待响应） | [chat.postMessage](https://api.slack.com/methods/chat.postMessage) |
| Message（消息） | Update（更新） | [chat.update](https://api.slack.com/methods/chat.update) |
| Reaction（回应） | Add（添加） | [reactions.add](https://api.slack.com/methods/reactions.add) |
| Reaction（回应） | Get（获取） | [reactions.get](https://api.slack.com/methods/reactions.get) |
| Reaction（回应） | Remove（移除） | [reactions.remove](https://api.slack.com/methods/reactions.remove) |
| Star（星标） | Add（添加） | [stars.add](https://api.slack.com/methods/stars.add) |
| Star（星标） | Delete（删除） | [stars.remove](https://api.slack.com/methods/stars.remove) |
| Star（星标） | Get Many（获取多项） | [stars.list](https://api.slack.com/methods/stars.list) |
| User（用户） | Get（获取） | [users.info](https://api.slack.com/methods/users.info) |
| User（用户） | Get Many（获取多项） | [users.list](https://api.slack.com/methods/users.list) |
| User（用户） | Get User's Profile（获取用户资料） | [users.profile.get](https://api.slack.com/methods/users.profile.get) |
| User（用户） | Get User's Status（获取用户状态） | [users.getPresence](https://api.slack.com/methods/users.getPresence) |
| User（用户） | Update User's Profile（更新用户资料） | [users.profile.set](https://api.slack.com/methods/users.profile.set) |
| User Group（用户组） | Create（创建） | [usergroups.create](https://api.slack.com/methods/usergroups.create) |
| User Group（用户组） | Disable（禁用） | [usergroups.disable](https://api.slack.com/methods/usergroups.disable) |
| User Group（用户组） | Enable（启用） | [usergroups.enable](https://api.slack.com/methods/usergroups.enable) |
| User Group（用户组） | Get Many（获取多项） | [usergroups.list](https://api.slack.com/methods/usergroups.list) |
| User Group（用户组） | Update（更新） | [usergroups.update](https://api.slack.com/methods/usergroups.update) |



{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
