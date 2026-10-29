---
title: Discord 节点常见问题
contentType:
- integration
- reference
priority: high
nodeTitle: Discord 节点常见问题
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues
description: 了解 n8n 工作流自动化平台中 Discord 节点的常见错误和问题，包括问题详情及建议的解决方法。
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

以下介绍 [Discord 节点](./README.md)的常见错误和问题，以及解决或排查步骤。

## 为嵌入内容添加额外字段 <a href="#add-extra-fields-to-embeds" id="add-extra-fields-to-embeds"></a>

Discord 消息可以包含嵌入内容（embed），这是一种富预览组件，可包含标题、描述、图像、链接等。

Discord 节点在 **Message**（消息）资源的 **Send**（发送）操作中支持嵌入内容。选择 **Add Embeds**（添加嵌入内容）可设置额外字段，包括 Description（描述）、Author（作者）、Title（标题）、URL 和 URL Image（图像 URL）。

要添加默认未提供的字段，请将 **Input Method**（输入方式）设为 **Raw JSON**（原始 JSON）。然后在 **Value**（值）参数中添加 JSON 对象，定义要包含的[字段名](https://discord.com/developers/docs/resources/message#embed-object)和值。

例如，`footer` 和 `fields` 无法通过 **Enter Fields**（输入字段）方式设置。要包含它们，可使用如下 JSON 对象：

```json
{
    "author": "My Name",
	"url": "https://discord.js.org",
	"fields": [
		{
			"name": "Regular field title",
			"value": "Some value here"
		}
	],
	"footer": {
		"text": "Some footer text here",
		"icon_url": "https://i.imgur.com/AfFp7pu.png"
	}
}
```

有关嵌入内容的更多信息，请参阅 [Using Webhooks and Embeds | Discord](https://discord.com/safety/using-webhooks-and-embeds)（使用 Webhook 和嵌入内容）。

如果在 Discord 节点中使用嵌入内容时遇到问题，可使用 [HTTP Request](../../core-nodes/n8n-nodes-base.httprequest/README.md) 节点及已有 Discord 凭据，向以下 URL 发送 `POST` 请求：

```
https://discord.com/api/v10/channels/<CHANNEL_ID>/messages
```

在请求体的消息内容中包含嵌入信息，如下所示：

```json
{
	"content": "Test",
	"embeds": [
		{
			"author": "My Name",
			"url": "https://discord.js.org",
			"fields": [
				{
					"name": "Regular field title",
					"value": "Some value here"
				}
			],
			"footer": {
				"text": "Some footer text here",
				"icon_url": "https://i.imgur.com/AfFp7pu.png"
			}
		}
	]
}
```

## 提及用户和频道 <a href="#mention-users-and-channels" id="mention-users-and-channels"></a>

要在 Discord 消息中提及用户和频道，需要按照 [Discord 消息格式指南](https://discord.com/developers/docs/reference#message-formatting)编排消息。

提及用户需要知道该 Discord 用户的用户 ID。请注意，用户 ID 与显示名称不同。同样，链接到指定频道需要频道 ID。

如何启用开发者模式并复制用户或频道 ID，请参阅 [Discord 关于查找用户、服务器和消息 ID 的文档](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID)。

获取用户或频道 ID 后，即可使用以下语法编排消息：

* **User**（用户）：`<@USER_ID>`
* **Channel**（频道）：`<#CHANNEL_ID>`
* **Role**（角色）：`<@&ROLE_ID>`

## 管理操作因权限错误而失败 <a id="moderation-actions-fail-with-a-permissions-error"></a>

**Member**（成员）资源的 **Ban**（封禁）、**Kick**（踢出）和 **Timeout**（禁言）操作要求机器人具有对应权限，且其角色在服务器角色层级中高于目标成员。任一检查失败，Discord 都会返回 `Missing Permissions` 错误。

请确认：

* 机器人角色包含所需权限：Ban（封禁）和 Unban（解除封禁）需要 **Ban Members**（封禁成员），Kick（踢出）需要 **Kick Members**（踢出成员），Timeout（禁言）需要 **Moderate Members**（管理成员）。
* 机器人的最高角色高于目标成员的最高角色。Discord 禁止对角色层级相同或更高的成员，以及服务器所有者执行管理操作。

可在 Discord 服务器设置的 **Roles**（角色）中检查角色、调整顺序和权限。更新后，再次运行工作流。
