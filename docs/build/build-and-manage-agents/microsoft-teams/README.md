---
title: 将智能体连接到 Microsoft Teams
status: preview
description: 将 n8n 智能体连接到 Microsoft Teams，让用户通过私聊、团队频道和群聊与其对话。介绍工作原理、使用位置、消息监听方式、文件处理及限制。
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
tags:
- tag: preview
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 将智能体连接到 Microsoft Teams <a id="connect-an-agent-to-microsoft-teams"></a>

Microsoft Teams 渠道让用户可以在 Teams 私聊、团队频道和群聊中与 n8n 智能体对话。

{% hint style="info" %}
**功能可用范围**

Microsoft Teams 渠道可用于：

* **n8n Cloud：**自 n8n 2.46.0 起的所有套餐。
* **自托管：**自 n8n 2.46.0 起的所有套餐。
{% endhint %}

{% hint style="info" %}
**预览状态**

智能体的 Microsoft Teams 渠道处于预览阶段，可能在后续版本中发生变化。请避免在生产环境中依赖此功能。
{% endhint %}

连接 Teams 有两种方式：

* **推荐设置**：使用 Microsoft 账号登录，n8n 会为你创建应用注册、Azure Bot 和 Teams 应用。
* **手动设置**（界面显示为 **Use your own Microsoft app，使用自己的 Microsoft 应用**）：自行创建应用注册和 Azure Bot，再向 n8n 提供凭据。

具体步骤请参阅[设置 Teams 渠道](set-up-the-teams-channel.md)。两种设置方式的最终结果相同。下文关于智能体使用位置、消息监听方式、主动发送的消息、文件和 Microsoft Graph 权限的说明均适用于两种方式。

## Teams 渠道的工作原理 <a id="how-the-teams-channel-works"></a>

Teams 智能体由四部分组成：Microsoft 侧的三个资源，以及 n8n 中的一个凭据。

| 组成部分 | 作用 |
| --- | --- |
| **Microsoft Entra 应用注册** | 为机器人提供身份。这是单租户应用，因此只能在你的组织中使用。 |
| **Azure Bot** | 接收来自 Teams 的消息并转发到 n8n。使用免费的 F0 层级，并启用 Microsoft Teams 渠道。 |
| **Teams 应用包** | 包含应用清单和图标的 zip 文件。用户在 Teams 中添加此应用，即可联系智能体。 |
| **Microsoft Entra Service Principal 凭据** | 在 n8n 中保存应用注册的租户 ID、客户端 ID 和客户端密钥。 |

有人在 Teams 中向智能体发送消息时：

1. Teams 将消息发送到 Azure Bot。
2. Azure Bot 将消息转发到你的 n8n 实例。
3. n8n 运行智能体的已发布版本。
4. 智能体在同一聊天或帖子中回复。处理期间，Teams 会显示正在输入的提示。

每个帖子对应一个独立会话，因此智能体会记住同一帖子中之前的消息。要重新开始，请发送 `/new`。如果某个工具需要批准，智能体会发送审批卡片。在频道和群聊中，只有需要回应的人能看到该卡片。

{% hint style="info" %}
**先发布智能体**

Teams 渠道运行智能体的已发布版本。发布前，智能体不会接收 Teams 消息。可以提前设置渠道，n8n 会在发布时连接渠道。
{% endhint %}

## 用户可以在哪里使用智能体 <a id="where-people-can-use-the-agent"></a>

在 **Choose where it works（选择使用位置）**步骤中，决定用户可以在哪里联系智能体。私聊始终开启。你也可以启用团队频道和群聊，并选择智能体是否读取其中的每条消息。

| 选项 | 使用位置 | 如何开始对话 | 新增权限 | 谁来批准 |
| --- | --- | --- | --- | --- |
| **Direct chat（私聊）** | 与智能体一对一聊天 | 打开应用并发送消息 | 无 | 无需批准 |
| **Team channels（团队频道）** | 已添加应用的团队中的频道 | 将应用添加到团队，然后在频道中 @提及智能体 | `ChannelMessage.Read.Group` | 团队所有者在添加应用时批准 |
| **Group and meeting chats（群聊和会议聊天）** | 已添加应用的群聊和会议聊天 | 将应用添加到聊天，然后 @提及智能体 | `ChatMessage.Read.Chat` | 将应用添加到聊天的人 |
| **Read all channel messages（读取所有频道消息）** | 团队频道 | 频道中的任何消息 | 除 **Team channels** 所需权限外，无其他权限 | 团队所有者在添加应用时批准 |
| **Read all group-chat messages（读取所有群聊消息）** | 群聊和会议聊天 | 聊天中的任何消息 | 除 **Group and meeting chats** 所需权限外，无其他权限 | 将应用添加到聊天的人 |

表中的权限是特定资源同意（RSC）权限。它们包含在应用包中，仅适用于添加该应用的团队或聊天，允许智能体读取其中的消息和粘贴的图片，不授予访问组织其他内容的权限。

这些选项属于应用包的一部分。如果以后修改选项，n8n 会构建新的应用包，你需要重新上传或发布。参阅[管理 Teams 渠道](manage-the-teams-channel.md)。

## 智能体如何监听频道和群聊 <a id="how-the-agent-listens-in-channels-and-group-chats"></a>

在私聊中，每条消息都会运行智能体，回复内容会随着生成逐字显示。

在团队频道和群聊中，智能体有两种监听方式。智能体处理完成后，回复会作为一条完整消息发送。

### 仅在提及时响应 <a id="mention-only"></a>

这是默认方式。只有有人 @提及智能体时，它才会参与：

* 有人 @提及智能体时，它会加入对话。在频道中，加入的是该帖子；在群聊中，加入的是整个聊天。
* 加入后，该帖子或聊天中的后续消息即使没有提及智能体，也会传递给它。
* 智能体尚未加入的帖子或聊天中的消息，不会传递给它。

### 读取所有消息 <a id="read-all-messages"></a>

启用 **Read all channel messages（读取所有频道消息）**或 **Read all group-chat messages（读取所有群聊消息）**后：

* 频道或聊天中的每条消息都会运行智能体，无需 @提及。
* 智能体自行决定是否回复。如果消息不是发给它的，可以保持沉默。
* 每条消息都会消耗模型额度，即使智能体不回复。
* n8n 会忽略其他机器人发送的消息。

用户直接向智能体求助时，保留默认设置即可。如果智能体需要跟踪完整对话，例如回答未直接向它提出的问题，可以开启读取所有消息选项。在消息频繁的频道中，这会消耗大量模型额度。

## 智能体主动发送的消息 <a id="messages-the-agent-sends-on-its-own"></a>

智能体不仅能回复，还能主动发起对话，例如通过“向 anna@example.com 发送周一摘要”这样的定时任务：

* **私信**：智能体向某个人发送私信。该用户必须已在 Teams 中添加此应用。
* **频道和群聊消息**：智能体在团队频道或群聊中发起新帖子。该团队或聊天必须已添加此应用。

要联系某个人，智能体需要其 Teams ID；要联系频道，则需要频道 ID。它可以为你查找这些 ID：

* 按电子邮件查找：根据电子邮件地址查找用户，需要 `User.ReadBasic.All`。
* 按名称查找：根据团队名和频道名查找频道，例如“Marketing General”。需要 `Team.ReadBasic.All` 和 `Channel.ReadBasic.All`。

这些权限由管理员与文件访问权限一并批准，参阅 [Microsoft Graph 权限](set-up-the-teams-channel.md#microsoft-graph-permissions)。未获得这些权限时，只要有人曾在某个频道中 @提及智能体，它仍可以联系该频道；如果已知某个人的 Teams ID，也仍可以联系该用户。

## 文件及文件权限 <a id="files-and-file-permissions"></a>

用户可以在消息中附加文件，智能体会连同文本一起接收。每个文件最大为 10 MB，每条消息最多附加 10 个文件。如果 n8n 无法读取文件，智能体仍会收到消息。

文件如何传递给智能体，取决于用户在哪里发送。

### 私信中的文件 <a id="files-in-direct-messages"></a>

在私聊中，Teams 会随消息本身发送文件，无需额外权限。

### 频道和群聊中的文件 <a id="files-in-channels-and-group-chats"></a>

在团队频道和群聊中，Teams 不会将文件包含在消息中。n8n 会通过 Microsoft Graph 再次读取消息，以找到文件：

* **粘贴的图片**可以使用应用已有的 RSC 权限访问，即 `ChannelMessage.Read.Group` 或 `ChatMessage.Read.Chat`，参阅[用户可以在哪里使用智能体](#where-people-can-use-the-agent)。无需其他权限。
* **附加文件**存储在 SharePoint 或 OneDrive 中。要下载这些文件，应用注册需要 Microsoft Graph 的 `Files.Read.All` **应用程序权限**，并获得管理员同意。参阅 [Microsoft Graph 权限](set-up-the-teams-channel.md#microsoft-graph-permissions)。

即使拥有 `Files.Read.All`，n8n 也只会在满足以下任一条件时下载文件：

* 文件位于该频道的 **Files（文件）**文件夹中。
* 文件位于消息发送者的 OneDrive 中。

这可以防止智能体打开与当前对话无关的文件。

### 智能体无法读取文件时 <a id="when-the-agent-cant-read-a-file"></a>

如果 n8n 无法下载文件，会将原因告知智能体，让它向发送者解释：

| 原因 | 处理方法 |
| --- | --- |
| 管理员尚未批准权限 | 按[批准访问权限](set-up-the-teams-channel.md#approve-access)中的说明批准，然后最多等待一小时。 |
| Teams 中的应用缺少权限 | 上传或发布最新应用包。旧应用包可能没有 RSC 权限。 |
| 文件不在该频道的文件中，且发送者不是文件所有者 | 请发送者在频道中共享文件，或从自己的 OneDrive 共享。 |

## 限制 <a id="limitations"></a>

* Teams 渠道仅适用于 Microsoft 全球云，不支持主权云。
* 机器人凭据必须使用客户端密钥，不支持证书身份验证。
* 每个凭据只能将一个智能体连接到 Teams，每个智能体只能有一个 Teams 连接。
* 按名称查找频道时，智能体最多搜索 50 个团队。
* 推荐设置始终在西欧区域的 `n8n-agents` 资源组中创建机器人。
* 每个文件最大为 10 MB，每条消息最多附加 10 个文件。
* 情景记忆暂不适用于 Teams 对话。智能体会记住同一帖子中的早期消息，但不会回想其他帖子或聊天中的上下文。

## 本节内容 <a id="in-this-section"></a>

* [设置 Teams 渠道](set-up-the-teams-channel.md)：通过推荐或手动方式连接智能体与 Teams，并批准 Microsoft Graph 权限。
* [管理 Teams 渠道](manage-the-teams-channel.md)：发布或上传应用、更新应用、续订客户端密钥、断开 Teams 连接，以及解决常见问题。

## 相关资源 <a id="related-resources"></a>

* [构建和管理智能体](../)
