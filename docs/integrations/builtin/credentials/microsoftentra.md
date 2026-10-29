---
title: Microsoft Entra ID 凭据
description: Microsoft Entra ID 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Microsoft Entra ID 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Microsoft Entra ID 凭据
originalFilePath: integrations/builtin/credentials/microsoftentra.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/microsoftentra
url: https://docs.n8n.io/integrations/builtin/credentials/microsoftentra
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Entra ID 凭据 <a href="#microsoft-entra-id-credentials" id="microsoft-entra-id-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Microsoft Entra ID](../app-nodes/n8n-nodes-base.microsoftentra.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建 Microsoft Entra ID 账户或订阅。
- 如果用户账户由企业 Microsoft Entra 账户管理，管理员必须为该用户启用“User can consent to apps accessing company data on their behalf”（用户可同意应用代表其访问公司数据）选项，请参阅 [Microsoft Entra 文档](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent)。

创建 [Microsoft Azure](https://azure.microsoft.com/) 账户时，Microsoft 会提供 Entra ID 免费方案。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Microsoft Entra ID 文档](https://www.microsoft.com/en-us/security/business/identity-access/azure-active-directory)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

自托管用户从头配置 OAuth2，主要需要两个步骤：

1. 向 Microsoft 标识平台注册[应用](#register-an-application)。
2. 为该应用[生成客户端密钥](#generate-a-client-secret)。

请按照下方各步骤的详细说明操作。Microsoft OAuth2 Web 流程的更多信息，请参阅 [Microsoft 身份验证与授权基础知识](https://learn.microsoft.com/en-us/graph/auth/auth-concepts)。

### 注册应用 <a href="#register-an-application" id="register-an-application"></a>

向 Microsoft 标识平台注册应用：

1. 打开 [Microsoft 应用注册门户](https://aka.ms/appregistrations)。
2. 选择 **Register an application**（注册应用）。
3. 输入应用的 **Name**（名称）。
4. 在 **Supported account types**（支持的账户类型）中，选择 **Accounts in any organizational directory (Any Azure AD directory - Multi-tenant) and personal Microsoft accounts (for example, Skype, Xbox)**（任何组织目录中的账户，任何 Azure AD 目录、多租户，以及个人 Microsoft 账户，例如 Skype、Xbox）。
5. 在 **Register an application**（注册应用）中：
    1. 从 n8n 凭据复制 **OAuth Callback URL**（OAuth 回调 URL）。
    2. 将其粘贴到 **Redirect URI (optional)**（重定向 URI，可选）字段。
    3. 选择 **Select a platform**（选择平台）> **Web**。
6. 选择 **Register**（注册），完成应用创建。
7. 复制 **Application (client) ID**（应用程序，客户端 ID），填入 n8n 的 **Client ID**（客户端 ID）。

更多信息，请参阅[向 Microsoft 标识平台注册应用](https://learn.microsoft.com/en-us/graph/auth-register-app-v2)。

### 生成客户端密钥 <a href="#generate-a-client-secret" id="generate-a-client-secret"></a>

应用创建完成后，为其生成客户端密钥：

1. 在 Microsoft 应用页面的左侧导航栏，选择 **Certificates & secrets**（证书与秘密）。
1. 在 **Client secrets**（客户端密钥）中，选择 **+ New client secret**（新建客户端密钥）。
1. 输入客户端密钥的 **Description**（描述），例如 `n8n credential`。
1. 选择 **Add**（添加）。
1. 复制 **Value**（值）列中的 **Secret**（秘密值）。
1. 将其粘贴到 n8n 的 **Client Secret**（客户端密钥）。
1. 在 n8n 中选择 **Connect my account**（连接我的账户），完成连接设置。
1. 登录 Microsoft 账户，允许应用访问你的信息。

添加客户端密钥的更多信息，请参阅 Microsoft 的[添加凭据](https://learn.microsoft.com/en-us/graph/auth-register-app-v2#add-credentials)。

也可使用证书（`private_key_jwt`）代替客户端密钥进行身份验证。将 **Authentication**（身份验证）设为 **Certificate**（证书），并提供私钥和证书。完整步骤，请参阅[使用证书进行身份验证](microsoft.md#authenticate-with-a-certificate)。

### Microsoft Graph API Base URL（基础 URL） <a href="#microsoft-graph-api-base-url" id="microsoft-graph-api-base-url"></a>

Microsoft Entra ID 凭据扩展了 Microsoft OAuth2 API 凭据，支持不同的 Microsoft 云环境。请根据租户所在云环境选择适当端点：

- **Global**（全球）：用于标准 Microsoft 365 租户，默认选项
- **US Government**（美国政府）：用于 Azure 美国政府（GCC）租户
- **US Government DOD**（美国政府国防部）：用于 Azure 美国政府国防部租户
- **China**（中国）：用于由世纪互联运营的中国 Microsoft 365

{% hint style="warning" %}
**政府云授权 URL**

使用政府云租户时，可能还需要更新凭据的 **Authorization URL**（授权 URL）和 **Access Token URL**（访问令牌 URL），改用政府云端点。例如：
- 美国政府云：使用 `https://login.microsoftonline.us/{tenant}/oauth2/v2.0/authorize` 和 `https://login.microsoftonline.us/{tenant}/oauth2/v2.0/token`
- 将 `{tenant}` 替换为租户 ID；多租户应用可使用 `common`
{% endhint %}

## 设置自定义权限范围 <a href="#setting-custom-scopes" id="setting-custom-scopes"></a>

Microsoft Entra ID 凭据默认使用以下作用域：

* [`openid`](https://learn.microsoft.com/en-us/entra/identity-platform/scopes-oidc#the-openid-scope)
* [`offline_access`](https://learn.microsoft.com/en-us/entra/identity-platform/scopes-oidc#the-offline_access-scope)
* [`AccessReview.ReadWrite.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#accessreviewreadwriteall)
* [`Directory.ReadWrite.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#directoryreadwriteall)
* [`NetworkAccessPolicy.ReadWrite.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#networkaccesspolicyreadwriteall)
* [`DelegatedAdminRelationship.ReadWrite.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#delegatedadminrelationshipreadwriteall)
* [`EntitlementManagement.ReadWrite.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#entitlementmanagementreadwriteall)
* [`User.ReadWrite.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#userreadwriteall)
* [`Directory.AccessAsUser.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#directoryaccessasuserall)
* [`Sites.FullControl.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#sitesfullcontrolall)
* [`GroupMember.ReadWrite.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#groupmemberreadwriteall)

如需为凭据选择其他作用域，请启用 **Custom Scopes**（自定义作用域）开关，编辑 **Enabled Scopes**（已启用的作用域）列表。使用更严格的作用域时，部分功能可能无法正常运行。


## 面向组织的 Microsoft 集成委派访问 <a href="#delegated-access-for-organisation-wide-microsoft-integrations" id="delegated-access-for-organisation-wide-microsoft-integrations"></a>

本节介绍 n8n 管理员如何注册一个具有委派权限的 Entra ID 应用，一次性授予管理员同意，再预配置 n8n，使组织中的其他用户无需自行注册 OAuth 应用，即可连接 Outlook、Teams、OneDrive 等 Microsoft 服务。

### 注册应用 <a href="#register-the-app" id="register-the-app"></a>

1. 在 [Microsoft Entra 管理中心](https://entra.microsoft.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade/quickStartType~/null/sourceType/Microsoft_AAD_IAM)，进入 **App registrations**（应用注册），选择 **+ New registration**（新注册）。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>请在 <strong>App registrations（应用注册）</strong>中注册，不要在 <strong>Enterprise applications（企业应用）</strong>中注册。</p></div>

2. 输入有意义的应用 **Name**（名称），例如 `n8n Outlook`。
3. 在 **Supported account types**（支持的账户类型）中，选择 **Multiple Entra ID tenants**（多个 Entra ID 租户）。
4. 在 **Allow only certain tenants (Preview)**（仅允许特定租户，预览）中，选择 **Manage allowed tenants**（管理允许的租户），添加你的租户。添加后红色横幅会消失。
5. 暂时将 **Redirect URI**（重定向 URI）留空，选择 **Register**（注册）。
6. 在应用概览页复制 **Application (client) ID**（应用程序，客户端 ID），后续会用到。

### 生成客户端密钥 <a href="#generate-a-client-secret" id="generate-a-client-secret"></a>

1. 在应用概览页的 **Client credentials**（客户端凭据）下，选择 **Add a certificate or secret**（添加证书或秘密）。
2. 选择 **+ New client secret**（新建客户端密钥）。
3. 输入 **Description**（描述），例如 `n8n token`，并选择符合组织凭据政策的有效期。
4. 选择 **Add**（添加）。
5. 立即复制 **Value**（值）。<br>

    <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p>密钥值仅显示一次，请勿在复制前离开页面，否则之后无法再次获取。</p></div>

### 配置 API 权限 <a href="#configure-api-permissions" id="configure-api-permissions"></a>

1. 在左侧导航栏点击 **API permissions**（API 权限）。
2. 点击 **+ Add a permission**（添加权限）> **Microsoft Graph** > **Delegated permissions**（委派权限）。
3. 在 **Select permissions**（选择权限）框中搜索每个必需作用域，勾选对应复选框。为计划启用的每个集成重复此操作，添加全部所需作用域。完整列表，请参阅下方[各集成所需作用域](#required-scopes-by-integration)。
4. 选择 **Add permissions**（添加权限）。

### 添加重定向 URI <a href="#add-the-redirect-uri" id="add-the-redirect-uri"></a>

1. 在 n8n 中创建工作流，添加一个要配置的 Microsoft 集成节点，例如 Microsoft Outlook。
2. 打开节点，选择 **Set up credential**（设置凭据）> **Create new credential**（创建新凭据）。
3. 为凭据设置有意义的名称，例如 `admin@yourorg.com`。
4. 复制 n8n 凭据面板显示的 **OAuth Redirect URL**（OAuth 重定向 URL）。
5. 返回 Entra 应用概览页，在 **Redirect URIs**（重定向 URI）下选择 **Add a redirect URI**（添加重定向 URI）。
6. 选择 **+ Add redirect URI**（添加重定向 URI），选择 **Web**，粘贴从 n8n 复制的 URL，再选择 **Configure**（配置）。

### 在 n8n 中授予管理员同意 <a href="#grant-admin-consent-in-n8n" id="grant-admin-consent-in-n8n"></a>

1. 在 n8n 凭据面板中，粘贴之前复制的 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）。
2. 选择 **Connect to [service]**（连接到服务），例如 **Connect to Microsoft Outlook**。
3. 在登录弹窗中勾选 **Consent on behalf of your organization**（代表组织同意），再选择 **Accept**（接受）。<br>

    <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p>必须以管理员身份登录，才能授予组织范围的同意。非管理员账户会看到需要管理员批准的提示。</p></div>

4. n8n 中的成功横幅会确认连接正常，且已正确授予同意。

### 为用户预配置凭据 <a href="#pre-configure-credentials-for-users" id="pre-configure-credentials-for-users"></a>

授予管理员同意后，使用[凭据覆盖配置](../../../administer/manage-credentials/credential-overwrites.md)预设 Client ID 和 Client Secret，使组织用户无需自行注册应用即可连接。Docker 和 Kubernetes 的设置步骤，请参阅 [Microsoft OAuth 凭据覆盖配置指南](../../../deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/pre-configure-microsoft-oauth-credentials.md)。

### 各集成所需作用域 <a href="#required-scopes-by-integration" id="required-scopes-by-integration"></a>

以下列出截至 2026 年 3 月各 Microsoft 集成所需的作用域。在 Entra 中配置 API 权限时，请为计划启用的每个集成添加对应作用域。

| 集成 | 所需作用域 |
|---|---|
| **Microsoft Dynamics** | `openid`、`offline_access` |
| **Microsoft Entra ID** | `openid`、`offline_access`、`AccessReview.ReadWrite.All`、`Directory.ReadWrite.All`、`NetworkAccessPolicy.ReadWrite.All`、`DelegatedAdminRelationship.ReadWrite.All`、`EntitlementManagement.ReadWrite.All`、`User.ReadWrite.All`、`Directory.AccessAsUser.All`、`Sites.FullControl.All`、`GroupMember.ReadWrite.All` |
| **Microsoft Excel** | `openid`、`offline_access`、`Files.ReadWrite` |
| **Microsoft Graph Security** | `SecurityEvents.ReadWrite.All`、`offline_access` |
| **Microsoft OneDrive** | `openid`、`offline_access`、`Files.ReadWrite.All` |
| **Microsoft Outlook** | `openid`、`offline_access`、`Contacts.Read`、`Contacts.ReadWrite`、`Calendars.Read`、`Calendars.Read.Shared`、`Calendars.ReadWrite`、`Mail.ReadWrite`、`Mail.ReadWrite.Shared`、`Mail.Send`、`Mail.Send.Shared`、`MailboxSettings.Read` |
| **Microsoft SharePoint** | `openid`、`offline_access`、`Sites.Read.All` 或 `Sites.ReadWrite.All` |
| **Microsoft Teams** | `openid`、`offline_access`、`User.Read.All`、`Group.ReadWrite.All`、`Chat.ReadWrite`、`ChannelMessage.Read.All`、`ChannelMessage.ReadWrite`、`OnlineMeetings.ReadWrite`、`TeamworkTag.Read`、`TeamsActivity.Send`、`TeamMember.Read.All`（从 n8n 2.45.0 起可用） |
| **Microsoft To Do** | `openid`、`offline_access`、`Tasks.ReadWrite` |
| **Microsoft Teams Trigger** | `openid`、`offline_access`、`Team.ReadBasic.All`、`Channel.ReadBasic.All`、`Chat.Read`、`ChannelMessage.Read.All`；New Team Member（新团队成员）事件还需要 `TeamMember.Read.All`。各事件需要的权限，请参阅 Microsoft Teams Trigger 文档中的[所需作用域](../trigger-nodes/n8n-nodes-base.microsoftteamstrigger.md#required-scopes)。 |

**Microsoft SharePoint** 的作用域适用于节点版本 2。只读工作流使用 `Sites.Read.All` 即可。如需将应用限定到选定站点，请改用委派的 `Sites.Selected` 作用域：应用注册需要按照[按站点授予访问权限](microsoftentraserviceprincipal.md#grant-access-per-site)配置授权，登录用户也必须有权访问每个站点。节点版本 1 使用节点专用的 Microsoft SharePoint 凭据，其权限请参阅 Microsoft 凭据文档中的 [SharePoint](microsoft.md#sharepoint)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下列出 Microsoft Entra 凭据的已知常见错误和问题。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/microsoft-need-admin-approval.md" %}

### 设置委派访问时需要管理员批准 <a href="#admin-approval-required-during-delegated-access-setup" id="admin-approval-required-during-delegated-access-setup"></a>

如果用户看到需要管理员批准的页面，表示尚未为应用注册授予组织范围的同意。

解决方法是使用 Entra ID 管理员账户，完成上方[在 n8n 中授予管理员同意](#grant-admin-consent-in-n8n)的步骤。

管理员也可直接在 Entra 中授予同意，无需通过 n8n，路径如下：

**Enterprise applications**（企业应用）> [你的应用] > **Security**（安全）> **Permissions**（权限）> **Grant admin consent for [your organisation]**（为你的组织授予管理员同意）

授予同意后，普通用户即可进行身份验证，不再遇到管理员批准提示。
