---
title: Microsoft Entra 服务主体凭据
description: Microsoft Entra 服务主体凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Microsoft 服务的身份验证。
contentType:
- integration
- reference
priority: medium
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Entra 服务主体凭据 <a id="microsoft-entra-service-principal-credentials"></a>

**Microsoft Entra Service Principal**（Microsoft Entra 服务主体）凭据为 n8n 提供对 Microsoft Graph 的仅应用访问。n8n 无需以个人身份登录，而是通过管理员在 Microsoft Entra 管理中心一次性设置的应用注册进行身份验证。这适用于无人值守及共享工作流：没有会过期的用户会话，也无需管理逐用户授权同意。

这些凭据可用于以下节点的身份验证：

* [Microsoft Excel (OneDrive)](../app-nodes/n8n-nodes-base.microsoftexcel.md)
* [Microsoft Excel (SharePoint)](../app-nodes/n8n-nodes-base.microsoftexcelsharepoint.md)
* [Microsoft OneDrive](../app-nodes/n8n-nodes-base.microsoftonedrive.md)
* [Microsoft OneDrive Trigger（触发器）](../trigger-nodes/n8n-nodes-base.microsoftonedrivetrigger.md)
* [Microsoft Outlook](../app-nodes/n8n-nodes-base.microsoftoutlook.md)
* [Microsoft Outlook Trigger（触发器）](../trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger.md)
* [Microsoft SharePoint](../app-nodes/n8n-nodes-base.microsoftsharepoint.md)
* [Microsoft SharePoint Trigger（触发器）](../trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger.md)
* [Microsoft Teams](../app-nodes/n8n-nodes-base.microsoftteams.md)
* [Microsoft Teams Trigger（触发器）](../trigger-nodes/n8n-nodes-base.microsoftteamstrigger.md)
* [Microsoft To Do](../app-nodes/n8n-nodes-base.microsofttodo.md)

{% hint style="info" %}
**节点版本要求**

Microsoft Excel (OneDrive)、Microsoft Outlook、Microsoft SharePoint 和 Microsoft Teams 节点从节点第 2 版起支持此凭据；Microsoft Excel (SharePoint) 节点从第 1 版起支持。
{% endhint %}

## 前置条件 <a id="prerequisites"></a>

- Microsoft 365 组织租户。个人 Microsoft 账户不支持应用程序权限。
- 以能够创建应用注册并授予管理员同意的管理员身份访问 [Microsoft Entra 管理中心](https://entra.microsoft.com/)，或由能够代你授予同意的管理员协助。

## 支持的身份验证方式 <a id="supported-authentication-methods"></a>

- OAuth2 客户端凭据，使用客户端密钥或证书，即签名客户端断言

## 相关资源 <a id="related-resources"></a>

更多信息，请参阅 Microsoft 文档：

- [无需用户获取访问权限](https://learn.microsoft.com/en-us/graph/auth-v2-service)：仅应用身份验证的工作方式
- [Microsoft Graph 权限参考](https://learn.microsoft.com/en-us/graph/permissions-reference)
- [为应用程序授予租户范围的管理员同意](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent)

## 仅应用访问与 OAuth2 的区别 <a id="how-app-only-access-differs-from-oauth2"></a>

使用 Microsoft OAuth2 凭据时，节点以已登录用户的身份操作。服务主体凭据没有已登录用户，因此节点的使用方式有所不同：

- **自行选择操作的用户或对象。**选择此凭据后，各节点会显示额外的必填参数：Microsoft OneDrive、Microsoft OneDrive Trigger 和 Microsoft Excel (OneDrive) 中的 **Access As**（访问身份，用户或驱动器），Microsoft Outlook 和 Microsoft Outlook Trigger 中的 **Mailbox**（邮箱），以及 Microsoft To Do 中的 **User**（用户）。输入用户主体名称（UPN），例如 `jane@contoso.com`，或用户对象 ID。在 **Access As** 字段中也可选择 **Drive**（驱动器），填写驱动器 ID。这些字段没有列表选择器，请直接粘贴值。在 Microsoft Teams 节点中，**Authentication**（身份验证）选项标为 **Service Principal (App-Only)**（服务主体，仅应用）；**Task**（任务）操作会隐藏 **Team**（团队）选择器，并将 **Plan**（计划）、**Bucket**（存储桶）和 **Assigned To**（分配给）选择器替换为普通 ID 字段；**Online Meeting**（联机会议）操作则添加 **Organizer**（组织者）字段，指定由应用管理其会议的用户。
- **权限适用于整个租户。**应用程序权限不限定于某个用户。例如，`Mail.Send` 应用程序权限允许应用以租户内任意邮箱的身份发送邮件，除非通过 [Exchange Online 应用程序访问策略](https://learn.microsoft.com/en-us/graph/auth-limit-mailbox-access)加以限制。n8n 建议通过应用程序访问策略限定租户范围的邮件权限。
- **选择器可看到整个租户。**例如，Microsoft Teams 的 **Team**（团队）选择器列出组织内所有团队，而不仅是应用已加入的团队。
- **部分操作不可用。**对于仅适用于已登录用户的功能，例如驱动器搜索或 Teams 聊天，节点会隐藏这些功能，或返回解释性错误以阻止操作。请参阅[仅应用访问不可用的操作](#operations-not-available-with-app-only-access)。

## 设置应用注册 <a id="set-up-the-app-registration"></a>

在 n8n 中创建凭据前，请先在 Microsoft Entra 管理中心完成以下步骤。如果希望改用命令行为 Microsoft SharePoint 节点设置应用注册，请参阅[使用 Azure CLI 配置 SharePoint 应用注册](microsoftentraserviceprincipal-sharepoint.md)。

### 注册应用 <a id="register-an-app"></a>

1. 打开 [Microsoft Entra 管理中心](https://entra.microsoft.com/)，进入 **Entra ID** > **App registrations**（应用注册）。
2. 选择 **New registration**（新注册）。
3. 为应用输入 **Name**（名称），例如 `n8n service principal`。
4. 在 **Supported account types**（支持的账户类型）中选择 **Accounts in this organizational directory only**（仅此组织目录中的账户）。无需重定向 URI。
5. 选择 **Register**（注册）。
6. 在应用的 **Overview**（概览）页面复制 **Application (client) ID**（应用程序，客户端 ID）和 **Directory (tenant) ID**（目录，租户 ID），n8n 需要填写这两个值。

### 添加应用程序权限 <a id="add-application-permissions"></a>

1. 在应用注册中选择 **API permissions**（API 权限）> **Add a permission**（添加权限）> **Microsoft Graph**。
2. 选择 **Application permissions**（应用程序权限），不要选择 **Delegated permissions**（委派权限）：仅应用访问会忽略委派作用域，且这两类权限的名称不同。
3. 添加计划使用节点所需的权限。请参阅[各节点所需的应用程序权限](#required-application-permissions-by-node)。
4. 选择 **Add permissions**（添加权限）。

### 授予管理员同意 <a id="grant-admin-consent"></a>

1. 在 **API permissions**（API 权限）页面选择 **Grant admin consent for `<your-tenant>`**（为该租户授予管理员同意），并确认。
2. 检查每项权限的 **Status**（状态）列是否均显示 **Granted**（已授予）。

{% hint style="warning" %}
**缺少管理员同意会导致通用权限错误**

如果未授予管理员同意，最初一切看起来都正常：凭据能保存，Microsoft 仍会签发令牌。但令牌不包含权限，因此每项操作都会因通用 Microsoft Graph 权限错误而失败，例如 HTTP 403 `Authorization_RequestDenied`（“Insufficient privileges to complete the operation”，没有足够权限完成操作）。问题并非凭据值错误。

要解决此问题，请打开应用注册的 **API permissions**（API 权限）页面，检查每项权限是否显示 **Granted**（已授予）；如果没有，请授予管理员同意。n8n 会缓存访问令牌，因此授予同意后需重新测试凭据。如果仍失败，请重新创建凭据，强制获取新令牌。
{% endhint %}

### 创建客户端密钥 <a id="create-a-client-secret"></a>

1. 在应用注册中选择 **Certificates & secrets**（证书和密钥）> **Client secrets**（客户端密钥）> **New client secret**（新建客户端密钥）。
2. 输入 **Description**（描述），例如 `n8n credential`，选择有效期。
3. 选择 **Add**（添加）。
4. 立即复制密钥的 **Value**（值）。Microsoft 仅显示一次。

### 在 n8n 中创建凭据 <a id="create-the-credential-in-n8n"></a>

在 n8n 中新建 **Microsoft Entra Service Principal**（Microsoft Entra 服务主体）凭据，填写以下字段：

1. **Directory (Tenant) ID**（目录，租户 ID）：应用注册 **Overview**（概览）页面中的目录（租户）ID。也可使用已验证的域名，例如 `contoso.onmicrosoft.com`。
2. **Application (Client) ID**（应用程序，客户端 ID）：应用注册 **Overview**（概览）页面中的应用程序（客户端）ID。
3. **Client Secret**（客户端密钥）：复制的客户端密钥值。
4. **Microsoft Graph API Base URL**（Microsoft Graph API 基础 URL）：除非租户位于主权云，否则保留 **Global**（全球）。请参阅[主权云环境](#sovereign-cloud-environments)。

要通过证书代替客户端密钥进行身份验证，请将 **Authentication**（身份验证）设为 **Certificate**（证书），粘贴私钥和证书。证书必须上传到应用注册的 **Certificates & secrets**（证书和密钥）中。

保存并测试凭据。从 n8n 2.40.0 起，连接测试仅检查应用能否登录，因此本身无需任何应用程序权限。缺少权限或管理员同意时，测试仍会通过，但节点运行时才会失败。在 n8n 2.40.0 之前，测试会通过 Microsoft Graph 读取组织信息，因此还需要 `Organization.Read.All` 或 `Directory.Read.All` 应用程序权限。

## 各节点所需的应用程序权限 <a id="required-application-permissions-by-node"></a>

为计划使用的每个节点添加应用程序权限，再授予管理员同意。本表中的全部权限均为 Microsoft Graph **Application**（应用程序）权限，均非委派权限。

| 节点 | 所需应用程序权限 |
|---|---|
| 所有节点，n8n 2.40.0 之前的凭据测试 | `Organization.Read.All` 或 `Directory.Read.All`。从 n8n 2.40.0 起，凭据测试无需应用程序权限。 |
| Microsoft OneDrive 和 Microsoft OneDrive Trigger | `Files.ReadWrite.All`，只读操作和触发器使用 `Files.Read.All` 即可 |
| Microsoft Excel (OneDrive) | `Files.ReadWrite.All` |
| Microsoft Outlook | `Mail.ReadWrite` 用于消息、草稿、文件夹和附件；Reply（回复）及 Draft: Send（草稿：发送）也需要它，因为这些操作会先创建或更新草稿再发送。`Mail.Send` 用于发送和回复，`Calendars.ReadWrite` 用于日历和事件，`Contacts.ReadWrite` 用于联系人，`MailboxSettings.Read` 用于加载 Categories（类别）下拉列表。仅添加实际操作使用的权限。 |
| Microsoft Outlook Trigger | `Mail.Read` |
| Microsoft SharePoint | 读取操作使用 `Sites.Read.All`，写入操作使用 `Sites.ReadWrite.All`。对于文档库中的项目，也可使用 `Files.Read.All`（Item: Get，项目：获取）或 `Files.ReadWrite.All`（Item: Delete，项目：删除）。若要将应用限定于指定站点，请改为授予 `Sites.Selected`，并参阅[逐站点授予访问权限](#grant-access-per-site)。 |
| Microsoft SharePoint Trigger | `Sites.Read.All`。若要将应用限定于指定站点，请改为授予 `Sites.Selected`，并参阅[逐站点授予访问权限](#grant-access-per-site)。 |
| Microsoft Teams 和 Microsoft Teams Trigger | `Team.ReadBasic.All`，以及下表中相应操作所需的权限 |
| Microsoft To Do | `Tasks.ReadWrite.All` |

Microsoft Teams 节点需要 `Team.ReadBasic.All` 来列出团队，此外每项操作还需要对应权限：

<!-- vale off -->

| Teams 操作 | 应用程序权限 |
|---|---|
| Activity Notification: Send（活动通知：发送） | `TeamsActivity.Send`，以及从列表中选择收件人所需的 `User.Read.All`。收件人还需安装配套的 Teams 应用。请参阅[发送活动通知](../app-nodes/n8n-nodes-base.microsoftteams.md#send-an-activity-notification)。 |
| Channel: Get, Get Many（频道：获取、获取多项） | `Channel.ReadBasic.All` |
| Channel: Create（频道：创建） | `Channel.Create` |
| Channel: Update（频道：更新） | `ChannelSettings.ReadWrite.All` |
| Channel: Delete（频道：删除） | `Channel.Delete.All` |
| Channel Message: Get, Get Many, Get Many Replies（频道消息：获取、获取多项、获取多条回复） | `ChannelMessage.Read.All` |
| Online Meeting: Create, Create or Get, Update, Delete（联机会议：创建、创建或获取、更新、删除） | `OnlineMeetings.ReadWrite.All`，以及面向组织者的应用程序访问策略。请参阅[允许仅应用联机会议](#allow-app-only-online-meetings)。 |
| Online Meeting: Get（联机会议：获取） | `OnlineMeetings.Read.All` 或 `OnlineMeetings.ReadWrite.All`，以及面向组织者的应用程序访问策略 |
| Online Meeting: Organizer picked from the list or given by user principal name（联机会议：从列表中选择组织者，或按用户主体名称指定） | `User.Read.All`。输入组织者对象 ID 时不需要。 |
| Task: all operations（任务：所有操作） | `Tasks.ReadWrite.All` |
| Trigger: New Channel（触发器：新频道） | `Channel.ReadBasic.All` |
| Trigger: New Channel Message（触发器：新频道消息） | `ChannelMessage.Read.All` |
| Trigger: New Team Member（触发器：新团队成员） | `TeamMember.Read.All` |

<!-- vale on -->

## 逐站点授予访问权限 <a id="grant-access-per-site"></a>

租户范围的 `Sites.Read.All` 或 `Sites.ReadWrite.All` 会授予应用访问组织内每个 SharePoint 站点的权限。如果安全团队希望逐站点授予访问权限，请改用 `Sites.Selected`。Microsoft SharePoint 节点（从第 2 版起）、Microsoft SharePoint Trigger 节点和 Microsoft Excel (SharePoint) 节点均支持此权限。

逐站点访问需要两步。第二步在 Entra 管理中心和 SharePoint 管理中心都没有对应页面，因此很多配置容易遗漏：

1. **添加权限并授予管理员同意。**在应用注册中添加 `Sites.Selected` 应用程序权限，替换租户范围的 `Sites.*` 权限，并授予管理员同意。
2. **授予应用对每个站点的访问权限。**管理员针对应用应能访问的每个站点，分别调用一次 Microsoft Graph 站点权限端点：

```http
POST https://graph.microsoft.com/v1.0/sites/<site-id>/permissions
Content-Type: application/json

{
	"roles": ["write"],
	"grantedToIdentities": [
		{
			"application": {
				"id": "<application-client-id>",
				"displayName": "<app-registration-name>"
			}
		}
	]
}
```

只读访问使用 `read` 角色，节点的写入操作使用 `write`。可从 [Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer) 或任何能够调用 Microsoft Graph 的工具发送请求。SharePoint 管理员也可改用 PnP PowerShell 的 [`Grant-PnPEntraIDAppSitePermission`](https://pnp.github.io/powershell/cmdlets/Grant-PnPEntraIDAppSitePermission.html)。从空租户到完成站点授权的完整流程，请参阅[使用 Azure CLI 配置 SharePoint 应用注册](microsoftentraserviceprincipal-sharepoint.md)。

发送请求的人员必须有权管理站点权限：在 Graph Explorer 中打开 **Modify permissions**（修改权限），在发送前同意授予 `Sites.FullControl.All`。此请求返回 403 `Access denied`，表示发送请求的账户或工具缺少该权限，而非被授予访问权限的应用缺少权限。

要查找站点的 `<site-id>`，请通过主机名和路径请求：`GET https://graph.microsoft.com/v1.0/sites/contoso.sharepoint.com:/sites/mysite`。

使用 `Sites.Selected` 时，节点无法搜索或列出站点，因为 Microsoft Graph 不支持在缺少租户范围读取权限时发现站点。请改为粘贴站点 URL 或 ID。缺少逐站点授权时，操作会返回 403 错误，并指出所需权限。

## 允许仅应用联机会议 <a id="allow-app-only-online-meetings"></a>

使用此凭据时，Microsoft Teams 节点的 Online Meeting（联机会议）操作以节点 **Organizer**（组织者）字段所选用户的身份执行。Microsoft Teams 节点从 n8n 2.40.0 起支持此功能。只有 Teams 管理员已为该用户向应用授予[应用程序访问策略](https://learn.microsoft.com/en-us/graph/cloud-communication-online-meeting-application-access-policy)时，Microsoft Graph 才允许执行。否则，每项 Online Meeting 操作都会因 403 错误而失败，n8n 会提示请求需要 `OnlineMeetings.ReadWrite.All` 权限，以及面向组织者的应用程序访问策略。

设置步骤如下：

1. 在应用注册中添加 `OnlineMeetings.ReadWrite.All` 应用程序权限，授予管理员同意。如果只使用 **Get**（获取）操作，`OnlineMeetings.Read.All` 即可。如果希望从列表选择组织者，或输入用户主体名称而非对象 ID，还需添加 `User.Read.All`。
2. 安装 [Microsoft Teams PowerShell 模块](https://learn.microsoft.com/en-us/microsoftteams/teams-powershell-install)，以 Teams 管理员身份登录：

	```powershell
	Connect-MicrosoftTeams
	```

3. 创建应用程序访问策略，列出应用注册的应用程序（客户端）ID：

	```powershell
	New-CsApplicationAccessPolicy -Identity n8n-online-meetings -AppIds "<application-client-id>" -Description "Lets n8n manage online meetings"
	```

4. 按用户对象 ID，将策略授予节点需要代表其操作的每个用户：

	```powershell
	Grant-CsApplicationAccessPolicy -PolicyName n8n-online-meetings -Identity "<user-object-id>"
	```

    如果要覆盖租户中所有未分配独立策略的用户，请改为在租户范围授予：

	```powershell
	Grant-CsApplicationAccessPolicy -PolicyName n8n-online-meetings -Global
	```

策略变更可能需要最多 30 分钟生效。一个用户同一时间只能拥有一项应用程序访问策略，因此授予新策略会替换已有策略。如果多个应用都需要访问，请将它们的 ID 全部列在同一策略中。

## 仅应用访问不可用的操作 <a id="operations-not-available-with-app-only-access"></a>

部分 Microsoft Graph 操作仅适用于已登录用户。选择此凭据时，节点会隐藏或阻止这些操作，并给出解释性错误。如果需要它们，请使用 OAuth2 凭据：

<!-- vale off -->

- **Microsoft OneDrive**：File: Search（文件：搜索）和 Folder: Search（文件夹：搜索）。Microsoft Graph 仅向已登录用户提供驱动器搜索。
- **Microsoft Excel (OneDrive)**：Workbook: Get Many（工作簿：获取多项），以及在 **Workbook**（工作簿）字段中按名称搜索工作簿。请改为将字段设为 **By ID**（按 ID）。
- **Microsoft Teams**：整个 Chat（聊天）、Chat Member（聊天成员）和 Chat Message（聊天消息）资源；Channel Message（频道消息）的 Create（创建）、Reply（回复）、Delete（删除）及 Undo Delete（撤销删除）；Group Member（组成员）模式下的 Task: Get Many（任务：获取多项）。Online Meeting（联机会议）操作可用，但需要应用程序访问策略。请参阅[允许仅应用联机会议](#allow-app-only-online-meetings)。
- **Microsoft Teams Trigger**：New Chat（新聊天）、New Chat Message（新聊天消息）事件，以及监视全部对象的选项。请改为选择特定团队或频道。

<!-- vale on -->

Microsoft Outlook、Microsoft Outlook Trigger、Microsoft SharePoint、Microsoft SharePoint Trigger 和 Microsoft To Do 节点没有被阻止的操作。在 Microsoft SharePoint 节点中，站点搜索需要 `Sites.Read.All` 应用程序权限；仅有 `Sites.Selected` 时，请改为通过 URL 或 ID 选择站点。

Microsoft OneDrive 的 File: Share（文件：共享）和 Folder: Share（文件夹：共享）仍可使用，但以仅应用身份创建共享链接可能需要额外的租户或管理员配置。节点会在这些操作上显示提示。

## 主权云环境 <a id="sovereign-cloud-environments"></a>

选择与租户云环境相匹配的 **Microsoft Graph API Base URL**（Microsoft Graph API 基础 URL）：

<!-- vale off -->

- **Global (https://graph.microsoft.com)**（全球）：标准 Microsoft 365 租户，默认选项
- **US Government (https://graph.microsoft.us)**（美国政府）：Azure 美国政府租户，包括 GCC High
- **US Government DOD (https://dod-graph.microsoft.us)**（美国政府国防部）：Azure 美国政府国防部租户
- **China (https://microsoftgraph.chinacloudapi.cn)**（中国）：中国由世纪互联运营的 Microsoft 365

n8n 会自动推导匹配的登录端点，例如美国政府云使用 `login.microsoftonline.us`，中国使用 `login.partner.microsoftonline.cn`，无需自行配置令牌 URL 或授权 URL。请在所用云自身的 Entra 管理中心完成应用注册，节点会通过所选端点发送所有 Microsoft Graph 调用。

<!-- vale on -->

## 常见问题 <a id="common-issues"></a>

Microsoft Entra Service Principal 凭据的常见错误和问题如下：

- **凭据测试通过，但每项操作都失败。**从 n8n 2.40.0 起，连接测试仅检查应用能否登录，不检查其拥有的权限。缺少应用程序权限、管理员同意或逐站点授权，只有在节点运行时才会显现。
- **每项操作都因通用权限错误而失败。**这几乎总是由于缺少应用程序权限或管理员同意。请参阅[授予管理员同意](#grant-admin-consent)中的警告。Microsoft SharePoint（第 2 版）和 Microsoft Excel (SharePoint) 节点会给出更明确的消息，指出操作所需的权限：“The app registration is missing a consented application permission for this operation.”（应用注册缺少已获同意的、执行此操作所需的应用程序权限。）
- **身份验证失败，提示“Microsoft Entra authentication did not return an access token”（Microsoft Entra 身份验证未返回访问令牌）。**Microsoft 拒绝了令牌交换，例如 AADSTS7000215（客户端密钥无效）、AADSTS7000222（客户端密钥已过期）或 AADSTS700027（证书断言被拒绝）。检查粘贴的是客户端密钥的 **Value**（值）而非 Secret ID（密钥 ID），确认密钥未过期；使用证书身份验证时，还需确认私钥与上传到应用注册的证书匹配。
- **权限或密钥变更未立即生效。**n8n 会缓存访问令牌。授予同意或轮换密钥后，请重新测试凭据；如果缓存令牌持续失败，请重新创建凭据。
- **“Microsoft Entra tenant ID is not a valid GUID or domain.”（Microsoft Entra 租户 ID 不是有效 GUID 或域名。）**请输入应用注册 **Overview**（概览）页面中的目录（租户）ID GUID，或 `contoso.onmicrosoft.com` 等已验证域名。不要输入 URL。
- **Microsoft Teams 节点的 Online Meeting（联机会议）操作因 403 错误而失败。**应用注册需要 `OnlineMeetings.ReadWrite.All` 应用程序权限，以及面向组织者的 Microsoft Teams 应用程序访问策略。请参阅[允许仅应用联机会议](#allow-app-only-online-meetings)。策略变更可能需要最多 30 分钟生效。
