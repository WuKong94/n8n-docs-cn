---
title: Microsoft 凭据
description: Microsoft 凭据文档。使用这些凭据在 n8n 中完成 Microsoft 的身份验证。
contentType:
- integration
- reference
priority: high
nodeTitle: Microsoft 凭据
originalFilePath: integrations/builtin/credentials/microsoft.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/microsoft
url: https://docs.n8n.io/integrations/builtin/credentials/microsoft
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft 凭据 <a href="#microsoft-credentials" id="microsoft-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Microsoft Dynamics CRM](../app-nodes/n8n-nodes-base.microsoftdynamicscrm.md)
- [Microsoft Excel (OneDrive)](../app-nodes/n8n-nodes-base.microsoftexcel.md)
- [Microsoft Excel (SharePoint)](../app-nodes/n8n-nodes-base.microsoftexcelsharepoint.md)
- [Microsoft Graph Security](../app-nodes/n8n-nodes-base.microsoftgraphsecurity.md)
- [Microsoft OneDrive](../app-nodes/n8n-nodes-base.microsoftonedrive.md)
- [Microsoft Outlook](../app-nodes/n8n-nodes-base.microsoftoutlook.md)
- [Microsoft Outlook Trigger（触发器）](../trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger.md)
- [Microsoft SharePoint](../app-nodes/n8n-nodes-base.microsoftsharepoint.md)
- [Microsoft SharePoint Trigger（触发器）](../trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger.md)
- [Microsoft Teams](../app-nodes/n8n-nodes-base.microsoftteams.md)
- [Microsoft Teams Trigger（触发器）](../trigger-nodes/n8n-nodes-base.microsoftteamstrigger.md)
- [Microsoft To Do](../app-nodes/n8n-nodes-base.microsofttodo.md)

{% hint style="info" %}
**选择凭据类型**

部分节点（例如 Microsoft Excel (OneDrive) 和 Microsoft OneDrive）允许在节点专用凭据（例如 **Microsoft Excel OAuth2 API**）与此通用 **Microsoft OAuth2 API** 凭据之间选择。通用凭据可在多个 Microsoft 节点之间复用，使用时须授予各节点所需的作用域。未显示此下拉菜单的节点使用各自的专用凭据。Microsoft Excel (SharePoint) 节点仅支持此通用凭据，或用于仅应用访问的 Microsoft Entra Service Principal 凭据，不接受 Microsoft Excel 或 Microsoft SharePoint 的节点专用凭据。Microsoft SharePoint 节点从第 2 版起也采用此方式，第 1 版仍使用节点专用的 Microsoft SharePoint 凭据。
{% endhint %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建 [Microsoft Azure](https://azure.microsoft.com/) 账户。
- 创建至少一个有权访问相应服务的用户账户。
- 如果用户账户由企业 Microsoft Entra 账户管理，管理员已为该用户启用“User can consent to apps accessing company data on their behalf”（用户可同意应用代表自己访问公司数据）选项。请参阅 [Microsoft Entra 文档](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

各服务 API 的更多信息，请参阅下方链接中的 Microsoft API 文档：

- Dynamics CRM：[Web API](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview)
- Excel：[Graph API](https://learn.microsoft.com/en-us/graph/api/resources/excel)
- Graph Security：[Graph API](https://learn.microsoft.com/en-us/graph/api/overview)
- OneDrive：[Graph API](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/)
- Outlook：[Graph API](https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview) 和 [Outlook API](https://learn.microsoft.com/en-us/outlook/rest/reference)
- Teams：[Graph API](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview)
- To Do：[Graph API](https://learn.microsoft.com/en-us/graph/todo-concept-overview)

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

部分 Microsoft 服务的 OAuth2 需要额外信息。相关服务的更多指引，请参阅[服务专用设置](#service-specific-settings)。

如果使用自托管版本，或在 n8n Cloud 凭据中选择 **Custom OAuth2**（自定义 OAuth2），需通过以下两个主要步骤从头配置 OAuth2：

1. 在 Microsoft Identity Platform 中[注册应用](#register-an-application)。
2. 为应用添加凭据，可[生成客户端密钥](#generate-a-client-secret)或[注册证书](#authenticate-with-a-certificate)。

各步骤的详细说明见下文。Microsoft OAuth2 Web 流程的更多详情，请参阅 [Microsoft 身份验证与授权基础](https://learn.microsoft.com/en-us/graph/auth/auth-concepts)。

### 注册应用 <a href="#register-an-application" id="register-an-application"></a>

在 Microsoft Identity Platform 中注册应用：

1. 打开 [Microsoft 应用注册门户](https://aka.ms/appregistrations)。
2. 选择 **Register an application**（注册应用）。
3. 输入应用的 **Name**（名称）。
4. 在 **Supported account types**（支持的账户类型）中选择 **Accounts in any organizational directory (Any Azure AD directory - Multi-tenant) and personal Microsoft accounts (for example, Skype, Xbox)**（任何组织目录中的账户，任何 Azure AD 目录、多租户，以及个人 Microsoft 账户，例如 Skype、Xbox）。
5. 在 **Register an application**（注册应用）中：
    1. 从 n8n 凭据复制 **OAuth Callback URL**（OAuth 回调 URL）。
    2. 将其粘贴到 **Redirect URI (optional)**（重定向 URI，可选）字段。
    3. 选择 **Select a platform**（选择平台）> **Web**。
6. 选择 **Register**（注册），完成应用创建。
7. 复制 **Application (client) ID**（应用程序，客户端 ID），填入 n8n 的 **Client ID**（客户端 ID）。

更多信息，请参阅[在 Microsoft Identity Platform 中注册应用](https://learn.microsoft.com/en-us/graph/auth-register-app-v2)。

### 生成客户端密钥 <a href="#generate-a-client-secret" id="generate-a-client-secret"></a>

应用创建完成后，为其生成客户端密钥：

1. 在 Microsoft 应用页面中，从左侧导航栏选择 **Certificates & secrets**（证书和密钥）。
1. 在 **Client secrets**（客户端密钥）中，选择 **+ New client secret**（新建客户端密钥）。
1. 输入客户端密钥的 **Description**（描述），例如 `n8n credential`。
1. 选择 **Add**（添加）。
1. 复制 **Value**（值）列中的 **Secret**（秘密值）。
1. 将其粘贴到 n8n 的 **Client Secret**（客户端密钥）。
1. 如果 n8n 凭据中还显示其他字段，请参阅下方[服务专用设置](#service-specific-settings)，了解如何填写。
1. 在 n8n 中选择 **Connect my account**（连接我的账户），完成连接设置。
1. 登录 Microsoft 账户，允许应用访问你的信息。

添加客户端密钥的更多信息，请参阅 Microsoft 的[添加凭据](https://learn.microsoft.com/en-us/graph/auth-register-app-v2#add-credentials)文档。

### 使用证书进行身份验证 <a href="#authenticate-with-a-certificate" id="authenticate-with-a-certificate"></a>

可使用**证书**代替客户端密钥，对应用进行身份验证。证书用于签名客户端断言，也称为 `private_key_jwt`。当组织安全策略不允许使用文本客户端密钥时，这种方式很有用。OAuth2 流程的其他部分不变：登录、授权同意页面和权限均相同。仅在令牌交换和刷新时，应用的身份证明从密钥改为签名断言。

默认身份验证方式为 **Client Secret**（客户端密钥），因此现有凭据可继续工作。仅在需要使用证书时，将凭据切换为 **Certificate**（证书）。

#### 生成证书 <a href="#generate-a-certificate" id="generate-a-certificate"></a>

如果尚无证书，请使用 [OpenSSL](https://www.openssl.org/) 创建自签名证书和私钥：

```shell
openssl req -x509 -newkey rsa:2048 -nodes \
  -keyout private-key.pem \
  -out certificate.pem \
  -days 365 \
  -subj "/CN=n8n-microsoft-cert"
```

这会生成两个文件：

- `private-key.pem`：RSA 私钥。请妥善保密，将其粘贴到 n8n 中；n8n 不会将它发送给 Microsoft。
- `certificate.pem`：公开证书，需要上传到 Entra 应用注册中。

私钥必须为 **RSA** 密钥。n8n 使用 RS256 签名客户端断言，因此 EC 和 Ed25519 密钥无法使用。

#### 为应用注册证书 <a href="#register-the-certificate-on-your-app" id="register-the-certificate-on-your-app"></a>

1. 在 Microsoft 应用页面中，从左侧导航栏选择 **Certificates & secrets**（证书和密钥）。
2. 选择 **Certificates**（证书）选项卡，再选择 **Upload certificate**（上传证书）。
3. 选择 `certificate.pem` 文件，即公开证书，而非私钥。
4. 可选：输入 **Description**（描述），例如 `n8n credential`，再选择 **Add**（添加）。

添加证书的更多信息，请参阅 Microsoft 的[添加凭据](https://learn.microsoft.com/en-us/graph/auth-register-app-v2#add-credentials)文档。

#### 在 n8n 中完成凭据设置 <a href="#complete-the-certificate-credential-in-n8n" id="complete-the-certificate-credential-in-n8n"></a>

1. 将 **Authentication**（身份验证）设为 **Certificate**（证书）。
2. 将 `private-key.pem` 的内容粘贴到 **Private Key**（私钥）字段。
3. 将 `certificate.pem` 的内容粘贴到 **Certificate**（证书）字段。
4. 如果 n8n 凭据中还显示其他字段，请参阅下方[服务专用设置](#service-specific-settings)，了解如何填写。
5. 在 n8n 中选择 **Connect my account**（连接我的账户），完成连接设置。
6. 登录 Microsoft 账户，允许应用访问你的信息。

令牌刷新也使用证书，因此 n8n 不会发送客户端密钥。

### Microsoft Graph API 基础 URL <a href="#microsoft-graph-api-base-url" id="microsoft-graph-api-base-url"></a>

Microsoft OAuth2 凭据支持不同的 Microsoft 云环境。请根据租户所在云环境选择相应端点：

- **Global**（全球）：用于标准 Microsoft 365 租户，默认选项
- **US Government**（美国政府）：用于 Azure 美国政府（GCC）租户
- **US Government DOD**（美国政府国防部）：用于 Azure 美国政府国防部租户
- **China**（中国）：用于中国由世纪互联运营的 Microsoft 365

此设置适用于所有使用 Microsoft 凭据的 Microsoft Graph API 节点，包括：

- Microsoft Teams
- Microsoft Outlook
- Microsoft Excel (OneDrive)
- Microsoft Excel (SharePoint)
- Microsoft OneDrive
- Microsoft Graph Security
- Microsoft SharePoint（从节点第 2 版起）
- Microsoft SharePoint Trigger（触发器）
- Microsoft To Do

{% hint style="warning" %}
**政府云授权 URL**

使用政府云租户时，可能还需要更新凭据的 **Authorization URL**（授权 URL）和 **Access Token URL**（访问令牌 URL），改用政府云端点。例如：

- 美国政府云：使用 `https://login.microsoftonline.us/{tenant}/oauth2/v2.0/authorize` 和 `https://login.microsoftonline.us/{tenant}/oauth2/v2.0/token`
- 将 `{tenant}` 替换为租户 ID；多租户应用可使用 `common`
{% endhint %}

### 自定义作用域 <a href="#custom-scopes" id="custom-scopes"></a>

定义与以下 Microsoft 服务交互时的细粒度权限：

* Microsoft Teams
* Microsoft Excel
* Microsoft Outlook
* Microsoft SharePoint
* Microsoft OneDrive

要为这些凭据选择不同作用域，请启用 **Custom Scopes**（自定义作用域）开关，再编辑 **Enabled Scopes**（已启用的作用域）列表。作用域限制更严格时，部分功能可能无法按预期工作。

#### Microsoft Outlook 的默认作用域 <a id="default-scopes-for-microsoft-outlook"></a>

Microsoft Outlook 凭据默认使用以下作用域：

* `openid`
* `offline_access`
* `Contacts.Read`
* `Contacts.ReadWrite`
* `Calendars.Read`
* `Calendars.Read.Shared`
* `Calendars.ReadWrite`
* `Mail.ReadWrite`
* `Mail.ReadWrite.Shared`
* `Mail.Send`
* `Mail.Send.Shared`
* `MailboxSettings.Read`

#### Microsoft SharePoint 的默认作用域 <a id="default-scopes-for-microsoft-sharepoint"></a>

Microsoft SharePoint 凭据默认使用以下作用域：

* `openid`
* `offline_access`
* `https://<subdomain>.sharepoint.com/.default`，其中将 `<subdomain>` 替换为凭据的 **Subdomain**（子域名）值

#### Microsoft OneDrive 的默认作用域 <a id="default-scopes-for-microsoft-onedrive"></a>

Microsoft OneDrive 凭据默认使用以下作用域：

* `openid`
* `offline_access`
* `Files.ReadWrite.All`

#### Microsoft Teams 的默认作用域 <a id="default-scopes-for-microsoft-teams"></a>

Microsoft Teams 凭据默认使用以下作用域：

* `openid`
* `offline_access`
* `User.Read.All`
* `Group.ReadWrite.All`
* `Chat.ReadWrite`
* `ChannelMessage.Read.All`
* `ChannelMessage.ReadWrite`（从 n8n 2.40.0 起可用）
* `OnlineMeetings.ReadWrite`（从 n8n 2.39.0 起可用）
* `TeamworkTag.Read`（从 n8n 2.41.0 起可用）
* `TeamsActivity.Send`（从 n8n 2.42.0 起可用）
* `TeamMember.Read.All`（从 n8n 2.45.0 起可用）

`TeamMember.Read.All` 需要管理员同意。n8n 2.45.0 之前连接的凭据会在重新连接时请求此作用域。Microsoft Entra 管理员必须先同意该作用域，再重新连接，否则登录会失败，详见[新增作用域需要重新批准](#new-scopes-need-a-new-approval)。如果凭据使用 **Custom Scopes**（自定义作用域），请先确认 **Enabled Scopes**（已启用的作用域）中包含该作用域；若没有，先添加再重新连接。

各 Microsoft Teams Trigger 事件需要的权限，请参阅 Microsoft Teams Trigger 文档中的[所需作用域](../trigger-nodes/n8n-nodes-base.microsoftteamstrigger.md#required-scopes)。

### 服务专用设置 <a href="#service-specific-settings" id="service-specific-settings"></a>

以下服务的 OAuth2 需要额外信息：

#### Dynamics <a href="#dynamics" id="dynamics"></a>

Dynamics OAuth2 需要 Dynamics 域名和区域信息。请执行以下额外步骤完成凭据设置：

1. 输入 Dynamics **Domain**（域名）。
2. 选择 Dynamics 所在数据中心的 **Region**（区域）。

区域选项及对应 URL 的更多信息，请参阅 [Microsoft 数据中心区域文档](https://learn.microsoft.com/en-us/power-platform/admin/new-datacenter-regions)。

#### Microsoft（通用） <a href="#microsoft-general" id="microsoft-general"></a>

通用 Microsoft OAuth2 还要求为此凭据提供以空格分隔的 **Scope**（作用域）列表。

可用作用域列表，请参阅 [Microsoft 标识平台中的作用域和权限](https://learn.microsoft.com/en-us/entra/identity-platform/scopes-oidc)。

n8n 节点文档列出了各节点所需的确切作用域。例如，[Microsoft SharePoint 节点](../app-nodes/n8n-nodes-base.microsoftsharepoint.md)（从第 2 版起）提供完整作用域字符串，如 `openid offline_access Sites.ReadWrite.All`，其中包含凭据刷新令牌所需的 `openid offline_access` 作用域。

#### Outlook <a href="#outlook" id="outlook"></a>

Outlook OAuth2 支持凭据访问用户的主邮箱或共享邮箱，默认访问用户主邮箱。要更改此行为：

1. 开启 **Use Shared Inbox**（使用共享邮箱）。
2. 将目标用户的 UPN 或 ID 填入 **User Principal Name**（用户主体名称）。

#### SharePoint <a href="#sharepoint" id="sharepoint"></a>

这些设置适用于 Microsoft SharePoint 节点第 1 版使用的节点专用 Microsoft SharePoint 凭据。节点第 2 版使用通用 Microsoft OAuth2 凭据，无需子域名，或使用 [Microsoft Entra Service Principal 凭据](microsoftentraserviceprincipal.md)；应填写的作用域请参阅 [Microsoft SharePoint 节点文档](../app-nodes/n8n-nodes-base.microsoftsharepoint.md)。

SharePoint OAuth2 需要 SharePoint **Subdomain**（子域名）信息。

要完成凭据设置，请输入 SharePoint URL 的 **Subdomain**（子域名）部分。例如，SharePoint URL 为 `https://tenant123.sharepoint.com` 时，子域名为 `tenant123`。

SharePoint 需要以下权限：

应用程序权限：

* `Sites.Read.All`
* `Sites.ReadWrite.All`

委派权限：

* `SearchConfiguration.Read.All`
* `SearchConfiguration.ReadWrite.All`

## 云端 Microsoft Teams：管理员批准 <a href="#microsoft-teams-on-cloud-admin-approval" id="microsoft-teams-on-cloud-admin-approval"></a>

在 n8n Cloud 中，组织的 Microsoft Entra 管理员须先批准一次托管 Microsoft Teams 凭据的权限，非管理员用户才能连接或重新连接。

[Microsoft Teams 默认作用域](#default-scopes-for-microsoft-teams)中有多项权限只能由管理员授予。选择 **Connect my account**（连接我的账户）时，n8n 会请求这些权限；Microsoft 对整个请求采取全部通过或全部拒绝的处理方式：如果租户未批准每一项所请求的权限，登录就会失败，n8n 不会收到令牌。管理员代表组织批准权限后，n8n Cloud 实例的用户即可连接，无需再次看到该提示。同一凭据用于 Microsoft Teams 节点和 Microsoft Teams Trigger。各触发器事件所需的作用域，请参阅 Microsoft Teams Trigger 文档中的[所需作用域](../trigger-nodes/n8n-nodes-base.microsoftteamstrigger.md#required-scopes)。

### 为什么仅重新连接会失败 <a id="why-reconnecting-alone-fails"></a>

如果你不是管理员，且租户尚未批准权限，Microsoft 会在 **Need admin approval**（需要管理员批准）或 **Approval required**（需要批准）页面阻止登录，且没有 **Accept**（接受）按钮。弹窗最终显示 `AADSTS65004` 等错误，n8n 始终不会收到令牌。凭据保持断开，因此所有使用它的节点都会失败，而不只是需要缺失权限的操作。重新连接仍会显示同一页面并以相同方式失败。顺序很重要：先由管理员批准，再由你重新连接。

如果页面提供 **Request approval**（请求批准），则表示租户已启用 Microsoft 的[管理员同意工作流](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/admin-consent-workflow-overview)：输入理由并向管理员发送请求。否则，请直接联系 Microsoft Entra 管理员，请其按照[为组织批准权限](#approve-the-permissions-for-your-organization)中的步骤操作。

### 为组织批准权限 <a id="approve-the-permissions-for-your-organization"></a>

以下步骤供 Microsoft Entra 管理员执行。Microsoft 仅向 Global Administrator（全局管理员）和 Privileged Role Administrator（特权角色管理员）显示 **Consent on behalf of your organization**（代表组织同意）选项。被指定为审核者且具有 Cloud Application Administrator（云应用程序管理员）或 Application Administrator（应用程序管理员）角色的人员，可改为通过[管理员同意工作流](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/review-admin-consent-requests)批准用户请求中的相同权限。还需在 n8n Cloud 实例上有用户账户，或请被阻止的用户发起连接，再由你在其弹窗中登录 Microsoft。

1. 在 n8n 中打开 Microsoft Teams 凭据，或创建新凭据：选择 **Create credential**（创建凭据），选择 **Microsoft Teams OAuth2 API**，并保留 **Managed OAuth2**（托管 OAuth2）。
2. 选择 **Connect my account**（连接我的账户），已有凭据则选择 **Reconnect**（重新连接），使用管理员账户登录。
3. 在 **Permissions requested**（请求的权限）页面检查权限，选择 **Consent on behalf of your organization**（代表组织同意），再选择 **Accept**（接受）。
4. 等待 n8n 显示 **Account connected**（账户已连接）。

Microsoft 将授权同意保存在租户中，而非 n8n 中。可以删除为此使用的凭据，批准仍然有效。用户此时创建或重新连接自己的凭据，登录即可完成，无需经过批准页面。

{% hint style="warning" %}
**在 Microsoft Entra 管理中心授予同意并不涵盖这些权限**

n8n 在登录时请求 Microsoft Teams 权限，而不是在应用注册中声明这些权限。Microsoft Entra 管理中心内应用 **Permissions**（权限）页面上的 **Grant admin consent**（授予管理员同意）仅涵盖已声明权限，因此无法解除凭据阻塞。请[通过登录提示批准权限](#approve-the-permissions-for-your-organization)，或通过[管理员同意工作流](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/review-admin-consent-requests)批准用户请求。
{% endhint %}

### 新增作用域需要重新批准 <a id="new-scopes-need-a-new-approval"></a>

n8n 会持续为 Microsoft Teams 凭据添加作用域，[Microsoft Teams 默认作用域](#default-scopes-for-microsoft-teams)会标明各新增作用域对应的 n8n 版本。在该版本之前连接的凭据可继续使用旧令牌，但需要新作用域的操作会因 403 错误而失败，直到重新连接。如果新作用域需要管理员同意，即使租户以前已批准此凭据，重新连接时仍会出现批准页面。顺序相同：管理员先[通过登录提示批准新权限](#approve-the-permissions-for-your-organization)，然后每位用户重新连接。

### 改用自己的应用注册 <a id="use-your-own-app-registration-instead"></a>

如果组织不允许同意 n8n 的共享应用，或希望自行控制权限，请通过自己的 Microsoft Entra 应用注册连接。此方式同样适用于 n8n Cloud：

1. 在凭据中从 **Managed OAuth2**（托管 OAuth2）切换为 **Custom OAuth2**（自定义 OAuth2）。
2. [注册应用](#register-an-application)，添加[客户端密钥](#generate-a-client-secret)或[证书](#authenticate-with-a-certificate)。使用凭据中显示的 **OAuth Redirect URL**（OAuth 重定向 URL）。在 n8n Cloud 中，这是 n8n 共用的回调 URL，而非实例 URL。
3. 请 Microsoft Entra 管理员为应用注册授予管理员同意。因为该应用由组织拥有，管理员可在应用上声明权限，并在 Microsoft Entra 管理中心批准，或通过 n8n 登录并选择 **Consent on behalf of your organization**（代表组织同意）。Microsoft Entra 凭据文档中的[面向组织范围 Microsoft 集成的委派访问](microsoftentra.md#delegated-access-for-organisation-wide-microsoft-integrations)详细介绍应用注册和授权同意步骤。

需要管理员同意的权限仍须由管理员批准，但对应的是组织自行控制的应用。启用 **Custom Scopes**（自定义作用域），将列表缩减到工作流实际使用的范围。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

Microsoft OAuth2 凭据的常见错误和问题：

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/microsoft-need-admin-approval.md" %}
