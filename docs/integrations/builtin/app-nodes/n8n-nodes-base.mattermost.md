---
title: Mattermost 节点文档
description: 了解如何在 n8n 中使用 Mattermost 节点，并按照技术文档将 Mattermost 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Mattermost 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.mattermost.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mattermost
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mattermost
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Mattermost 节点 <a href="#mattermost-node" id="mattermost-node"></a>

使用 Mattermost 节点自动处理 Mattermost 中的工作，并将其与其他应用集成。n8n 内置支持多种 Mattermost 功能，包括创建、删除和获取频道及用户，以及发布消息和添加回应。

本页列出了 Mattermost 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Mattermost 凭据](../credentials/mattermost.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Channel（频道）
    * Add a user to a channel（将用户添加到频道）
    * Create a new channel（创建新频道）
    * Soft delete a channel（软删除频道）
    * Get a page of members for a channel（获取频道的一页成员）
    * Restores a soft deleted channel（恢复已软删除的频道）
    * Search for a channel（搜索频道）
    * Get statistics for a channel（获取频道统计信息）
* Message（消息）
    * Soft delete a post, by marking the post as deleted in the database（通过在数据库中标记帖子为已删除来软删除帖子）
    * Post a message into a channel（向频道发布消息）
    * Post an ephemeral message into a channel（向频道发布临时消息）
* Reaction（回应）
    * Add a reaction to a post.（为帖子添加回应）
    * Remove a reaction from a post（移除帖子的回应）
    * Get all the reactions to one or more posts（获取一个或多个帖子的所有回应）
* User（用户）
    * Create a new user（创建新用户）
    * Deactivates the user and revokes all its sessions by archiving its user object.（通过归档用户对象停用该用户，并撤销其所有会话）
    * Retrieve all users（获取全部用户）
    * Get a user by email（通过邮箱获取用户）
    * Get a user by ID（通过 ID 获取用户）
    * Invite user to team（邀请用户加入团队）


## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Mattermost 集成模板](https://n8n.io/integrations/mattermost)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Mattermost 文档](https://api.mattermost.com/)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

## Channel ID 字段错误 <a href="#channel-id-field-error" id="channel-id-field-error"></a>

如果不是 System Administrator（系统管理员），可能会在 **Channel ID**（频道 ID）字段旁看到错误：**there was a problem loading the parameter options from server: "Mattermost error response: You do not have the appropriate permissions.**（从服务器加载参数选项时出错：Mattermost 返回没有相应权限的错误。）

请系统管理员为你授予 `post:channel` 权限。

## 查找频道 ID <a href="#find-the-channel-id" id="find-the-channel-id"></a>

在 Mattermost 中查找频道 ID 的步骤如下：

1. 从左侧栏中选择频道。
2. 选择顶部的频道名称。
3. 选择 **View Info**（查看信息）。





