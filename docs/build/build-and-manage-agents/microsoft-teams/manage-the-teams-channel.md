---
title: 管理 Teams 渠道
status: preview
description: 管理 n8n 智能体的 Microsoft Teams 渠道：发布或上传应用、更新应用、续订客户端密钥、断开 Teams 连接，以及排查常见问题。
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


# 管理 Teams 渠道 <a id="manage-the-teams-channel"></a>

{% hint style="info" %}
**功能可用范围**

Microsoft Teams 渠道可用于：

* **n8n Cloud：**所有套餐。
* **自托管：**自 n8n 2.32.3 起的所有套餐。

译注：本页原文列出的自托管最低版本为 n8n 2.32.3，而同一版本文档的 Teams 总览将 Cloud 和自托管最低版本均列为 n8n 2.46.0。此处保留原文并提示差异，不据此判断实际版本兼容性。
{% endhint %}

{% hint style="info" %}
**预览状态**

智能体的 Microsoft Teams 渠道处于预览阶段，可能在后续版本中发生变化。请避免在生产环境中依赖此功能。
{% endhint %}

连接 Teams 后，可以在渠道设置中修改配置。打开智能体，进入 **Channels（渠道）**，选择 **Microsoft Teams**。

渠道设置中会显示：

* **Where it works（使用位置）**：[用户可以在哪里使用智能体](./#where-people-can-use-the-agent)中的选项，以及管理员是否已批准 Microsoft Graph 权限。
* **Appearance in Teams（Teams 中的外观）**：应用的显示名称、说明和图标。推荐设置还会显示 **Install app（安装应用）**菜单。
* **Azure Bot**：推荐设置下会显示 **Linked to Azure Bot（已连接 Azure Bot）**和 **Find it in Azure（在 Azure 中查看）**链接；手动设置下会显示 **Find your Azure Bot（查找你的 Azure Bot）**链接。

## 上传应用或发布到组织 <a id="upload-the-app-or-publish-it-to-your-organization"></a>

将应用添加到 Teams 有两种方式：

| | Install for me（为我安装，通过上传） | Publish to organization（发布到组织） |
| --- | --- | --- |
| **谁可以添加应用** | 你自己，以及收到你提供的 zip 文件的任何人 | 组织内的任何人，通过 Teams 应用商店添加 |
| **谁来批准** | Teams 策略允许上传自定义应用时，无需批准 | Teams 管理员；你本身是管理员时无需其他人批准 |
| **所需时间** | 立即可用 | Microsoft 最多需要一天才会列出应用；等待审批时可能更久 |
| **用户如何获得更新** | 每个人重新上传新的 zip 文件 | 再次发布，Teams 会为所有用户更新应用 |
| **适用设置** | 推荐设置和手动设置 | 推荐设置 |

### 为我安装 <a id="install-for-me"></a>

**Install for me（为我安装）**会下载应用包。在 Teams 的 **Apps（应用）** > **Manage your apps（管理你的应用）** > **Upload an app（上传应用）**中上传，然后添加到团队或聊天。在手动设置中，对应的是 **Download app package（下载应用包）**步骤。

如果没有 **Upload an app（上传应用）**选项，请 Teams 管理员允许上传自定义应用，或改为发布应用。

### 发布到组织 <a id="publish-to-your-organization"></a>

**Publish to organization（发布到组织）**会将应用添加到组织在 Teams 中的应用目录。推荐设置的 **Install app（安装应用）**步骤中提供此选项，之后也可以在渠道设置的 **Install app** 菜单中找到。

* **如果你是 Teams 管理员**，n8n 会立即发布应用，但 Microsoft 最多可能需要一天才会列出。根据组织的应用策略，Teams 管理员可能仍需在 Teams 管理中心将应用设置为对所有人可用。
* **如果你不是管理员**，n8n 会提交应用等待审批。应用会在 Teams 管理中心的 **Teams apps（Teams 应用）** > **Manage apps（管理应用）**中显示为 **Pending approval（等待批准）**。管理员批准前，任何人都无法添加应用。在设置流程中选择 **Copy a request for your administrator（复制发给管理员的请求）**，可以复制一条包含应用名称和该页面链接的消息。

如果应用正在等待审批或已被管理员拒绝，渠道设置中会显示相应状态。管理员拒绝时，Microsoft 不会提供原因，需要直接向管理员询问。

手动设置下，n8n 无法代你发布应用。请 Teams 管理员改为在 Teams 管理中心上传应用包。

## 更改使用位置或外观 <a id="change-where-it-works-or-how-it-looks"></a>

在渠道设置中，可以更改 **Where it works（使用位置）**和 **Appearance in Teams（Teams 中的外观）**，例如显示名称和说明。在提交新版本前，Teams 会继续使用旧版应用：

* **手动设置**：选择 **Save and download package（保存并下载应用包）**，然后在 Teams 的 **Apps（应用）** > **Manage your apps（管理你的应用）** > **Upload an app（上传应用）**中上传新应用包。
* **推荐设置**：打开 **Install app（安装应用）**菜单，选择 **Publish to organization（发布到组织）**；或者选择 **Install for me（为我安装）**，下载并上传新应用包。

应用使用智能体的名称和图标。如果之后修改了智能体名称或图标，渠道设置会显示 **Changes to the agent aren't in Teams yet.（智能体的更改尚未同步到 Teams。）**重新安装或发布应用即可更新。

## 切换凭据或登录账号 <a id="switch-to-another-credential-or-sign-in"></a>

不同的凭据或 Microsoft 登录账号对应不同的机器人，因此 n8n 无法直接在已连接的渠道中替换。如果在渠道设置中选择其他凭据或账号，n8n 会询问 **Set up Microsoft Teams again?（重新设置 Microsoft Teams？）**选择 **Set up again（重新设置）**会移除当前 Teams 连接及其设置，并从头开始配置。在完成新设置之前，智能体会停止在 Teams 中响应。

## 续订客户端密钥 <a id="renew-the-client-secret"></a>

客户端密钥会过期。过期后，智能体会停止在 Teams 中回复。

* **推荐设置**：n8n 会按组织允许的最长有效期创建密钥，最长为 24 个月。再次运行 **Create Teams app（创建 Teams 应用）**步骤时，n8n 会复用应用注册；如果当前密钥将在七天内到期，则创建新密钥。
* **手动设置**：在 Microsoft Entra 中创建新客户端密钥，然后更新 n8n 中的凭据。

## 断开 Teams 连接 <a id="disconnect-teams"></a>

要断开 Teams 连接，请从智能体中移除渠道，并选择 **Yes, remove（是，移除）**确认。已发送的消息会保留在 Teams 中。之后如需重新连接，需要再次设置渠道。

断开 Teams 渠道或删除智能体时，n8n 不会删除 Microsoft 中的任何资源。用户可能仍安装着应用，但智能体不再响应。对于推荐设置创建的应用，n8n 会显示提醒，并提供指向 Teams 管理中心的 **Open Teams（打开 Teams）**链接。如果不再需要这些资源，请自行删除：

* 应用注册：位于 [Microsoft Entra](https://entra.microsoft.com/) 的 **App registrations（应用注册）**中。
* Azure Bot：位于 [Azure 门户](https://portal.azure.com/)中。推荐设置创建的机器人位于 `n8n-agents` 资源组中。
* Teams 应用：如果发布过，位于 [Teams 管理中心](https://admin.teams.microsoft.com/)的 **Teams apps（Teams 应用）** > **Manage apps（管理应用）**中。

## 故障排查 <a id="troubleshooting"></a>

### 组织不允许你注册应用 <a id="your-organization-doesnt-let-you-register-apps"></a>

你的 Microsoft 账号无法创建应用注册。请管理员授予相应权限，或者使用管理员为你创建的应用注册，采用[手动设置](set-up-the-teams-channel.md#manual-setup)。

### Teams 应用需要工作或学校账号 <a id="teams-apps-need-a-work-or-school-account"></a>

你使用了个人 Microsoft 账号登录。请使用组织的工作或学校账号重新登录。

### 账号无法在 Azure 订阅中创建资源 <a id="your-account-cant-create-resources-in-the-azure-subscription"></a>

你需要所选 Azure 订阅中的 Contributor 角色。请 Azure 管理员授予权限，或选择其他订阅。

### 凭据与 Microsoft Entra 中的应用不匹配 <a id="the-credential-doesnt-match-an-app-in-microsoft-entra"></a>

凭据信息与应用注册不匹配。检查以下事项：

* 租户 ID 和客户端 ID 属于同一个应用注册。
* 客户端密钥填写的是 **Value（值）**，而非 **Secret ID（密钥 ID）**。
* 客户端密钥尚未过期。

### “The Teams bot needs an HTTPS messaging endpoint”（Teams 机器人需要 HTTPS 消息终结点） <a id="the-teams-bot-needs-an-https-messaging-endpoint"></a>

Microsoft 只向 HTTPS URL 发送消息。自托管 n8n 需将 `N8N_WEBHOOK_URL` 设置为实例公开可访问的 HTTPS URL。

### Teams 中没有“上传应用”选项 <a id="no-upload-an-app-option-in-teams"></a>

Teams 策略不允许上传自定义应用。请 Teams 管理员允许上传，或改为将应用发布到组织。

### 智能体不在频道中回复 <a id="the-agent-doesnt-reply-in-a-channel"></a>

检查以下事项：

* 智能体已发布。
* 已启用 **Team channels（团队频道）**，且 Teams 中已安装最新应用包。
* 有人在帖子中 @提及过智能体，或已启用 **Read all channel messages（读取所有频道消息）**。

### 智能体无法读取附加文件 <a id="the-agent-cant-read-attached-files"></a>

读取频道和群聊中的文件需要 `Files.Read.All` 应用程序权限。管理员通过授予管理员同意，与其他 Graph 权限一并批准一次即可。权限最多可能需要一小时生效。参阅[批准访问权限](set-up-the-teams-channel.md#approve-access)。

### 智能体找不到用户或频道 <a id="the-agent-cant-find-a-person-or-channel"></a>

按电子邮件查找用户需要 `User.ReadBasic.All`，按名称查找频道需要 `Team.ReadBasic.All` 和 `Channel.ReadBasic.All`。管理员通过[批准访问权限](set-up-the-teams-channel.md#approve-access)进行批准。批准前，可以先在频道中 @提及智能体一次，或向智能体提供该用户的 Teams ID。

### 智能体无法发送私信或帖子 <a id="the-agent-cant-send-a-direct-message-or-post"></a>

对于智能体主动发送的消息，Teams 只会投递到已添加应用的位置。发送私信时，收件人必须已在 Teams 中添加应用；发送帖子时，该团队或群聊必须已添加应用。请收件人或团队所有者添加应用，然后重试。

## 相关资源 <a id="related-resources"></a>

* [将智能体连接到 Microsoft Teams](./)
* [设置 Teams 渠道](set-up-the-teams-channel.md)
