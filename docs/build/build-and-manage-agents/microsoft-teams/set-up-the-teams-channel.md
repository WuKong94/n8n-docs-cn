---
title: 设置 Teams 渠道
status: preview
description: 通过推荐或手动方式为 n8n 智能体设置 Microsoft Teams 渠道，包括前提条件、自托管要求和 Microsoft Graph
  权限。
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


# 设置 Teams 渠道 <a id="set-up-the-teams-channel"></a>

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

通过推荐或手动方式，将 n8n 智能体连接到 Microsoft Teams。渠道的工作原理及使用位置请参阅[将智能体连接到 Microsoft Teams](./)。

## 前提条件 <a id="prerequisites"></a>

开始前，请确认具备以下条件：

* 一个你可以编辑、且至少发布过一次的智能体。
* Microsoft 可以通过 HTTPS 访问的 n8n 实例。自托管 n8n 需将 `N8N_WEBHOOK_URL` 设置为实例公开可访问的 HTTPS URL。
* Microsoft 全球云中的 Microsoft 365 工作或学校账号。不支持个人账号和主权云，例如 GCC 或由世纪互联运营的 Microsoft Azure。
* 用于 Azure Bot 的 Azure 订阅。
* 在 Teams 中添加自定义应用的权限。Teams 策略需允许上传自定义应用，或者由管理员将应用发布到组织。

## 推荐设置 <a id="recommended-setup"></a>

推荐设置会为你创建 Microsoft 侧的所有资源。n8n Cloud 开箱即用。自托管 n8n 则需要实例所有者先完成配置，参阅[在自托管 n8n 中使用推荐设置](#use-the-recommended-setup-on-self-hosted-n8n)。如果推荐设置不可用，Teams 渠道只会显示[手动设置](#manual-setup)，标记为 **Use your own Microsoft app（使用自己的 Microsoft 应用）**。

连接 Teams 的步骤：

1. 打开智能体，进入 **Channels（渠道）**，选择 **Microsoft Teams**。确认已选择 **Recommended setup（推荐设置）**。
2. 在 **Connect to Microsoft（连接 Microsoft）**中选择 **Sign in with Microsoft（使用 Microsoft 登录）**，使用将要使用智能体的组织中的工作或学校账号登录。
3. 在 **Create Teams app（创建 Teams 应用）**中选择 **Create app（创建应用）**。n8n 会在 Microsoft Entra 中注册应用，最多可能需要 30 秒。
4. 在 **Deploy Azure Bot（部署 Azure Bot）**中选择 **Azure subscription（Azure 订阅）**，再选择 **Create Azure Bot（创建 Azure Bot）**，最多可能需要一分钟。
5. 在 **Choose where it works（选择使用位置）**中，选择[用户可以在哪里使用智能体](./#where-people-can-use-the-agent)中介绍的选项。
6. 在 **Install app（安装应用）**中选择 **Install for me（为我安装）**或 **Publish to organization（发布到组织）**。参阅[上传应用或发布到组织](manage-the-teams-channel.md#upload-the-app-or-publish-it-to-your-organization)。
7. 在 **Approve access（批准访问权限）**中立即批准 Microsoft Graph 权限，或稍后在渠道设置中批准。参阅[批准访问权限](#approve-access)。
8. 在 **Connect Microsoft Teams（连接 Microsoft Teams）**中，完成 Teams 中的应用添加，然后选择 **Done（完成）**。

### n8n 为你创建的资源 <a id="what-n8n-creates-for-you"></a>

| 资源 | 详情 |
| --- | --- |
| 应用注册 | 名为 `<agent-name> (n8n)` 的单租户应用，包含名为 `n8n agent channel` 的客户端密钥。n8n 也会创建其服务主体。 |
| 资源组 | 西欧区域中的 `n8n-agents`。如果尚不存在，会在你选择的订阅中创建。 |
| Azure Bot | 以智能体命名，使用免费的 F0 层级，并启用 Microsoft Teams 渠道。渠道设置中提供其链接。 |
| n8n 凭据 | 保存应用 ID 和密钥的 Microsoft Entra Service Principal 凭据，无需手动复制密钥。 |

如果重新运行某个步骤，n8n 会复用同一应用注册和机器人，不会重新创建。

### 推荐设置所需的权限 <a id="permissions-for-the-recommended-setup"></a>

登录时，n8n 会向 Microsoft 请求以下委派权限。n8n 仅以当前登录用户的身份，使用这些权限来设置智能体：

| 权限 | n8n 的用途 |
| --- | --- |
| `User.Read` | 读取你的个人资料和组织信息。 |
| `Application.ReadWrite.All` | 创建应用注册、客户端密钥和服务主体。 |
| `AppCatalog.ReadWrite.All` | 将 Teams 应用发布到组织的应用目录。 |
| `AppCatalog.Submit` | 无法直接发布时，将 Teams 应用提交给管理员审批。 |
| Azure Service Management（`user_impersonation`） | 列出 Azure 订阅并创建 Azure Bot。 |

`Application.ReadWrite.All` 和 `AppCatalog.ReadWrite.All` 需要管理员同意。Microsoft 组织的管理员只需批准 n8n 一次，之后其他人登录时就不再显示权限页面。如果登录时 Microsoft 显示 **Need admin approval（需要管理员批准）**，则必须先由管理员批准 n8n。选择 **Copy link for an admin（复制管理员链接）**，并将链接发送给管理员。

这些权限只允许 n8n 以你的身份操作。你的 Microsoft 账号还需要具备以下权限：

| 步骤 | 账号所需权限 | 缺少权限时 |
| --- | --- | --- |
| **Create Teams app（创建 Teams 应用）** | 在 Microsoft Entra 中注册应用的权限。组织可能将其限制为特定角色。 | 请管理员注册应用，或在设置中选择 **Use your own Microsoft app instead（改用自己的 Microsoft 应用）**链接，切换到[手动设置](#manual-setup)。 |
| **Deploy Azure Bot（部署 Azure Bot）** | Azure 订阅中的 Contributor（参与者）角色。 | 请 Azure 管理员授予 Contributor 权限，或选择 **Use your own Microsoft app instead（改用自己的 Microsoft 应用）**链接，切换到手动设置。 |
| **Publish to organization（发布到组织）** | Teams 管理员角色，可直接发布。 | n8n 会改为提交应用等待审批。参阅[发布到组织](manage-the-teams-channel.md#publish-to-your-organization)。 |

## 手动设置 <a id="manual-setup"></a>

如果推荐设置不可用，或组织不允许使用，请采用手动设置。自行在 Microsoft 中创建资源，再通过凭据将其连接起来。

在 Teams 渠道中选择 **Use your own Microsoft app（使用自己的 Microsoft 应用）**。推荐设置中的 **Use your own Microsoft app instead（改用自己的 Microsoft 应用）**链接也会跳转到这里。按以下步骤操作：

1. [在 Microsoft Entra 中注册应用](#register-the-app-in-microsoft-entra)。
2. [在 n8n 中创建凭据](#create-the-credential-in-n8n)。
3. [部署 Azure Bot](#deploy-the-azure-bot)。
4. [选择使用位置](#choose-where-it-works)。
5. [下载应用包](#download-the-app-package)。
6. [批准 Graph 权限](#approve-the-graph-permissions)（可选）。
7. [在 Teams 中添加应用](#add-the-app-in-teams)。

### 在 Microsoft Entra 中注册应用 <a id="register-the-app-in-microsoft-entra"></a>

如果已拥有某个应用注册的凭据，且没有其他智能体使用该凭据，可以跳过此步骤。

1. 选择 **Open Microsoft Entra（打开 Microsoft Entra）**，或进入 [Microsoft Entra 管理中心](https://entra.microsoft.com/) > **App registrations（应用注册）** > **New registration（新注册）**。
2. 输入名称，例如智能体名称。
3. 在 **Supported account types（支持的账号类型）**中，选择 **Accounts in this organizational directory only（仅此组织目录中的账号）**，即单租户。
4. 无需填写重定向 URI。选择 **Register（注册）**。
5. 在 **Overview（概览）**页面，复制 **Directory (tenant) ID（目录/租户 ID）**和 **Application (client) ID（应用程序/客户端 ID）**。
6. 进入 **Certificates & secrets（证书和密钥）** > **Client secrets（客户端密钥）** > **New client secret（新客户端密钥）**。添加说明和到期时间，然后复制密钥的 **Value（值）**，而非 **Secret ID（密钥 ID）**。Microsoft 只会显示该值一次。

机器人收发消息本身不需要任何 API 权限。

### 在 n8n 中创建凭据 <a id="create-the-credential-in-n8n"></a>

在 **Create credential（创建凭据）**中创建一个新凭据：

1. **Authentication（身份验证）**：选择 **Client Secret（客户端密钥）**。Teams 渠道不支持证书。
2. **Directory (Tenant) ID（目录/租户 ID）**：填写复制的租户 ID。
3. **Application (Client) ID（应用程序/客户端 ID）**：填写复制的客户端 ID。
4. **Client Secret（客户端密钥）**：填写复制的密钥值。
5. **Microsoft Graph API Base URL**：选择 **Global（全球）**。

n8n 会向 Microsoft 验证凭据。通过后，显示 **Credential verified with Microsoft Entra.（已通过 Microsoft Entra 验证凭据。）**每个凭据只能将一个智能体连接到 Teams。如果另一个智能体已使用该凭据，请为当前智能体注册新应用。

此凭据类型的更多信息请参阅 [Microsoft Entra 服务主体凭据](../../../integrations/builtin/credentials/microsoftentraserviceprincipal.md)。

### 部署 Azure Bot <a id="deploy-the-azure-bot"></a>

选择以下方式之一：

* **新机器人**：选择 **Deploy to Azure（部署到 Azure）**。Azure 门户会打开一个模板，n8n 已填入机器人名称、应用 ID 和消息终结点。Azure 可能提示模板并非来自 Microsoft。选择订阅和资源组，然后创建部署。你需要订阅中的 Contributor 角色。
* **现有机器人**：选择 **Use an existing Azure Bot（使用现有 Azure Bot）**，复制 **Messaging endpoint（消息终结点）**。在 Azure 门户中打开机器人的 **Configuration（配置）**页面，将其粘贴到 **Messaging endpoint**，并确认机器人使用同一个应用注册。然后进入 **Channels（渠道）**并启用 **Microsoft Teams**。

### 选择使用位置 <a id="choose-where-it-works"></a>

选择用户在哪里使用智能体，以及智能体如何监听消息。私聊始终开启。启用 **Team channels（团队频道）**或 **Group and meeting chats（群聊和会议聊天）**后，用户可以在那里添加并 @提及智能体。读取所有消息选项会让每条消息都运行智能体，每次都会消耗模型额度。详情请参阅[用户可以在哪里使用智能体](./#where-people-can-use-the-agent)和[智能体如何监听频道和群聊](./#how-the-agent-listens-in-channels-and-group-chats)。

### 下载应用包 <a id="download-the-app-package"></a>

选择 **Download app package（下载应用包）**。这也会将渠道连接到智能体。应用包使用智能体的名称和图标。

### 批准 Graph 权限 <a id="approve-the-graph-permissions"></a>

要让智能体查找用户和频道并读取附加文件，管理员需要添加 Microsoft Graph 应用程序权限并授予管理员同意。选择 **Approve access（批准访问权限）**，再选择 **Approve now（立即批准）**或 **Copy link for admin（复制管理员链接）**。参阅[批准访问权限](#approve-access)。

如果智能体只需在收到消息时回复，可以跳过此步骤。稍后仍可在渠道设置中批准。

### 在 Teams 中添加应用 <a id="add-the-app-in-teams"></a>

1. 在 Teams 中，进入 **Apps（应用）** > **Manage your apps（管理你的应用）** > **Upload an app（上传应用）**，上传 zip 文件。
2. 根据智能体的使用位置，选择 **Add to a team（添加到团队）**或 **Add to a chat（添加到聊天）**。
3. 在 n8n 中选择 **Done（完成）**。

如果没有 **Upload an app（上传应用）**选项，说明 Teams 策略不允许自定义应用。请 Teams 管理员允许上传自定义应用，或将应用上传到组织的应用目录。

### 手动设置所需的权限 <a id="permissions-for-the-manual-setup"></a>

| 权限 | 类型 | 授予者 | 用途 | 缺少权限时 |
| --- | --- | --- | --- | --- |
| 注册应用程序 | Microsoft Entra 设置或角色 | Microsoft Entra 管理员 | 注册应用 | 无法创建应用注册。 |
| Contributor（参与者） | Azure 订阅中的角色 | Azure 管理员 | 部署 Azure Bot | 无法创建机器人。 |
| 上传自定义应用 | Teams 应用设置策略 | Teams 管理员 | 上传应用包 | 只能由管理员通过 Teams 管理中心添加应用。 |
| `User.ReadBasic.All`、`Team.ReadBasic.All`、`Channel.ReadBasic.All` 和 `Files.Read.All` | Microsoft Graph 应用程序权限 | Microsoft 管理员，需授予管理员同意 | 查找用户和频道，读取频道与群聊中的附件 | 智能体只能在收到消息时回复，且无法读取这些文件。 |
| `ChannelMessage.Read.Group` | RSC 权限，启用 **Team channels（团队频道）**时添加 | 团队所有者在添加应用时授予 | 读取频道消息和粘贴的图片 | 智能体无法在频道中工作。 |
| `ChatMessage.Read.Chat` | RSC 权限，启用 **Group and meeting chats（群聊和会议聊天）**时添加 | 将应用添加到聊天的人 | 读取聊天消息和粘贴的图片 | 智能体无法在群聊中工作。 |

## 在自托管 n8n 中使用推荐设置 <a id="use-the-recommended-setup-on-self-hosted-n8n"></a>

在自托管 n8n 中，推荐设置需要一个用于用户登录设置流程的 Microsoft 应用。n8n Cloud 提供了这样的应用。在自己的实例中，需要由实例所有者提供：

1. 在 Microsoft Entra 中注册多租户应用，选择 **Accounts in any organizational directory（任何组织目录中的账号）**。
2. 添加重定向 URI `<n8n-url>/rest/oauth2-credential/callback`，平台类型设为 **Web**。
3. 添加以下委派 API 权限：
	* Microsoft Graph：`User.Read`、`Application.ReadWrite.All`、`AppCatalog.ReadWrite.All`、`AppCatalog.Submit`、`openid`、`profile`、`offline_access`
	* Azure Service Management：`user_impersonation`
4. 创建客户端密钥。
5. 通过凭据覆盖，为凭据类型 `microsoftTeamsManagerOAuth2Api` 提供客户端 ID 和密钥：

	```json
	{
		"microsoftTeamsManagerOAuth2Api": {
			"clientId": "<client-id>",
			"clientSecret": "<client-secret>"
		}
	}
	```

配置覆盖后，Teams 渠道会显示 **Recommended setup（推荐设置）**。凭据覆盖的设置方法请参阅[凭据覆盖](../../../administer/manage-credentials/credential-overwrites.md)和[预配置 Microsoft OAuth 凭据](../../../deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/pre-configure-microsoft-oauth-credentials.md)。

## Microsoft Graph 权限 <a id="microsoft-graph-permissions"></a>

在对话中回复以及读取粘贴的图片，使用应用包中的权限即可。除此之外的功能，需要为应用注册添加四项 Microsoft Graph **应用程序权限**：

| 权限 | 智能体可执行的操作 |
| --- | --- |
| `User.ReadBasic.All` | 按电子邮件查找用户，以便向其发送私信和提及他们。 |
| `Team.ReadBasic.All` | 按名称查找团队，以便在其频道中发帖。 |
| `Channel.ReadBasic.All` | 按名称查找频道，以便在其中发帖。 |
| `Files.Read.All` | 读取用户在频道和群聊中附加的文件。 |

Microsoft 组织的管理员会一次性批准全部四项权限，不能只批准其中一部分。未获批准时，智能体只能在收到消息时回复。

### 批准访问权限 <a id="approve-access"></a>

两种设置方式都提供 **Approve access（批准访问权限）**步骤，说明中会列出针对已启用使用位置，批准后可获得的能力。也可以稍后批准：管理员批准前，渠道设置的 **Where it works（使用位置）**下会显示警告。

选择 **Approve access（批准访问权限）**，然后选择以下方式之一：

* **Approve now（立即批准）**：如果你是组织管理员，直接打开审批页面。
* **Copy link for admin（复制管理员链接）**：复制链接，发送给有权批准的管理员。

链接打开的页面取决于设置方式：

* **推荐设置**：Microsoft 管理员同意页面。n8n 已将权限添加到应用注册，管理员检查并接受即可。
* **手动设置**：Microsoft Entra 中应用注册的 **API permissions（API 权限）**页面。管理员在那里添加权限：
	1. 选择 **Add a permission（添加权限）** > **Microsoft Graph** > **Application permissions（应用程序权限）**。
	2. 搜索并添加上表中的每项权限。
	3. 选择 **Grant admin consent（授予管理员同意）**。

{% hint style="warning" %}
**使用应用程序权限**

添加权限时，选择 **Application（应用程序）**权限，而非 **Delegated（委派）**权限。智能体以应用身份操作，而非以登录用户身份操作，因此无法使用委派权限。
{% endhint %}

连接渠道后，两种设置方式的渠道设置都会检查审批状态。Microsoft 确认批准后，会显示 **Permissions approved.（权限已批准。）**智能体可能最多需要等待一小时才能使用这些权限。

## 相关资源 <a id="related-resources"></a>

* [将智能体连接到 Microsoft Teams](./)
* [管理 Teams 渠道](manage-the-teams-channel.md)
* [Microsoft Entra 服务主体凭据](../../../integrations/builtin/credentials/microsoftentraserviceprincipal.md)
