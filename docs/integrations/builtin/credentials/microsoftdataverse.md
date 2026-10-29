---
description: 在 n8n 中配置 Microsoft Dataverse 凭据，通过 Microsoft Entra ID 实现委派用户访问或仅应用访问。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Dataverse 凭据 <a id="microsoft-dataverse-credentials"></a>

可使用 **Microsoft Dataverse OAuth2 API** 凭据，为 [Microsoft Dataverse 节点](../app-nodes/n8n-nodes-base.microsoftdataverse.md)进行身份验证。

## 前置条件 <a id="prerequisites"></a>

* Microsoft Dataverse 环境及其环境 URL。
* Microsoft Entra ID 应用注册，或创建应用注册的权限。
* 配置委派访问的 API 同意权限，或能够授予同意的管理员。
* 委派访问需要具有适当安全角色的 Dataverse 用户；仅应用访问则需要能够创建应用程序用户的管理员。

请使用仅具有工作流所需表权限的安全角色。身份验证并不会授予读取或修改所有表的权限。

## 支持的身份验证方式 <a id="supported-authentication-methods"></a>

此凭据支持 OAuth2，提供两种 **Grant Type**（授权类型）选项：

| 授权类型 | 访问方式 | 要求 |
| --- | --- | --- |
| **Authorization Code**（授权码，默认） | 以已登录用户的身份操作。n8n 使用刷新令牌续期访问。 | Web 重定向 URI、Dataverse 委派权限，以及有权访问环境的用户。 |
| **Client Credentials**（客户端凭据） | 无需用户登录，以应用身份操作。n8n 在需要时获取新的访问令牌。 | 指定租户 ID，以及具有安全角色的 Dataverse 应用程序用户。无需交互式登录或重定向 URI。 |

以下设置使用 **Client Secret**（客户端密钥）身份验证。此凭据还继承了 Microsoft OAuth2 凭据的 **Certificate**（证书）身份验证方式。要以私钥和证书代替客户端密钥，请参阅[使用证书进行身份验证](microsoft.md#authenticate-with-a-certificate)。

## 配置凭据 <a id="configure-the-credential"></a>

在 n8n 中创建 **Microsoft Dataverse OAuth2 API** 凭据。在连接或保存完整凭据前，先注册应用并配置计划使用的授权类型。

### 注册应用 <a id="register-an-application"></a>

1. 打开 [Microsoft Entra 管理中心](https://entra.microsoft.com/)，进入 **App registrations**（应用注册）> **New registration**（新注册）。
2. 输入名称，例如 `n8n Dataverse`。
3. 选择组织支持的账户类型。仅在一个租户内访问时，选择 **Accounts in this organizational directory only**（仅此组织目录中的账户）。
4. 如果计划使用 **Authorization Code**（授权码），从 n8n 凭据编辑器复制 **OAuth Redirect URL**（OAuth 重定向 URL）。在 **Redirect URI**（重定向 URI）下选择 **Web**，完整粘贴所显示的 URL。使用 **Client Credentials**（客户端凭据）时，重定向 URI 留空。
5. 选择 **Register**（注册）。
6. 在应用的 **Overview**（概览）中，将 **Application (client) ID**（应用程序，客户端 ID）复制到 n8n 的 **Client ID**（客户端 ID），将 **Directory (tenant) ID**（目录，租户 ID）复制到 n8n 的 **Tenant ID**（租户 ID）。

对于已有应用，请在应用注册的 **Authentication**（身份验证）设置中，将 n8n 重定向 URL 添加为 **Web** 重定向 URI。

### 生成客户端密钥 <a id="generate-a-client-secret"></a>

1. 在应用注册中打开 **Certificates & secrets**（证书和密钥）> **Client secrets**（客户端密钥）。
2. 选择 **New client secret**（新建客户端密钥），输入描述，选择符合组织策略的有效期。
3. 选择 **Add**（添加），复制密钥的 **Value**（值），不要复制 **Secret ID**（密钥 ID）。Microsoft 仅显示一次该值。
4. 在 n8n 中将 **Authentication**（身份验证）设为 **Client Secret**（客户端密钥），把该值粘贴到 **Client Secret**。

将密钥保存在 n8n 凭据中，不要放在工作流字段中。轮换密钥时，请在旧密钥过期前更新凭据。

### 设置环境和租户 <a id="set-the-environment-and-tenant"></a>

在 n8n 凭据中填写以下字段：

| n8n 字段 | 值 |
| --- | --- |
| **Grant Type**（授权类型） | 用户访问使用 **Authorization Code**（授权码）；仅应用访问使用 **Client Credentials**（客户端凭据）。 |
| **Client ID**（客户端 ID） | Entra 应用注册中的 **Application (client) ID**（应用程序，客户端 ID）。 |
| **Client Secret**（客户端密钥） | 密钥的 **Value**（值），适用于 **Client Secret** 身份验证。 |
| **Tenant ID**（租户 ID） | 应用注册中的 **Directory (tenant) ID**（目录，租户 ID）。使用 **Client Credentials** 时，请填写租户 GUID。 |
| **Environment URL**（环境 URL） | 环境的 HTTPS 基础 URL，例如 `https://contoso.crm.dynamics.com`。不要追加 `/api/data/v9.2`、表名或应用路径。 |
| **National Cloud**（国家云） | 托管 Dataverse 环境的 Microsoft 云。默认值为 **Global (Public Cloud)**（全球，公有云）。 |

在 [Power Platform 管理中心](https://admin.powerplatform.microsoft.com/)的环境详情中查找环境 URL。凭据接受末尾带斜杠的 URL，并在构建作用域和请求时移除该斜杠。

使用 **Authorization Code**（授权码）时，**Tenant ID**（租户 ID）也接受已验证的租户域名。默认值 `common` 用于多租户授权码应用。单租户应用应将其替换为指定租户 GUID 或域名。**Client Credentials**（客户端凭据）不能使用 `common`。

### 配置委派用户访问 <a id="configure-delegated-user-access"></a>

使用 **Authorization Code**（授权码）的步骤如下：

1. 在 Entra 应用注册中进入 **API permissions**（API 权限）> **Add a permission**（添加权限）。
2. 选择 **Dynamics CRM** > **Delegated permissions**（委派权限），再选择 **user_impersonation**。此权限的名称为 **Access Dynamics 365 as organization users**（以组织用户身份访问 Dynamics 365）。
3. 选择 **Add permissions**（添加权限）。如果租户要求，请让管理员授予同意。
4. 确认登录用户有权访问 Dataverse 环境，并拥有包含所需表权限的安全角色。
5. 在 n8n 中将 **Grant Type**（授权类型）设为 **Authorization Code**（授权码），确认应用的 **Web** 重定向 URI 与凭据编辑器中的 **OAuth Redirect URL**（OAuth 重定向 URL）一致。
6. 选择 **Connect my account**（连接我的账户），登录并接受请求的访问权限，或完成组织的批准流程。
7. 保存凭据。

委派权限的要求，请参阅 Microsoft 的 [Dataverse OAuth 文档](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-oauth)。

### 配置仅应用访问 <a id="configure-app-only-access"></a>

使用 **Client Credentials**（客户端凭据）时，请在目标 Dataverse 环境中创建应用程序用户：

1. 在 [Power Platform 管理中心](https://admin.powerplatform.microsoft.com/)中进入 **Manage**（管理）> **Environments**（环境），选择所需环境。
2. 打开 **Settings**（设置）> **Users + permissions**（用户和权限）> **Application users**（应用程序用户）。
3. 选择 **New app user**（新建应用程序用户），再选择 **Add an app**（添加应用）。通过应用程序 ID 找到 Entra 应用注册，选择 **Add**（添加）。
4. 选择合适的 **Business Unit**（业务部门），按要求输入电子邮件地址，并分配具有工作流所需权限的安全角色。
5. 选择 **Create**（创建），创建应用程序用户。
6. 在 n8n 中将 **Grant Type**（授权类型）设为 **Client Credentials**（客户端凭据）。在 **Tenant ID**（租户 ID）中填写租户 GUID，确认应用凭据、**Environment URL**（环境 URL）和 **National Cloud**（国家云）。
7. 保存凭据。此流程没有交互式账户连接步骤。

Dataverse 的仅应用访问使用应用程序用户的安全角色，不要求委派的 `user_impersonation` 权限或 Microsoft Graph 权限。详情请参阅 Microsoft 的[应用程序用户设置](https://learn.microsoft.com/en-us/power-platform/admin/manage-application-users#create-an-application-user)。

{% hint style="info" %}
**凭据测试**

保存凭据时，n8n 会对已配置的环境调用 `GET /api/data/v9.2/WhoAmI` 进行测试。仅获取到访问令牌，并不能证明应用程序用户存在或有权访问 Dataverse。凭据测试成功也不能保证拥有每项表操作的权限。
{% endhint %}

## 国家云和作用域 <a id="national-clouds-and-scopes"></a>

**National Cloud**（国家云）控制 Microsoft Entra 登录主机。请选择与环境相匹配的云：

| 国家云 | 登录主机 |
| --- | --- |
| **Global (Public Cloud)**（全球，公有云） | `https://login.microsoftonline.com` |
| **US Government (GCC High)**（美国政府，GCC High） | `https://login.microsoftonline.us` |
| **US Government (DoD)**（美国政府，国防部） | `https://login.microsoftonline.us` |
| **China (21Vianet)**（中国，世纪互联） | `https://login.partner.microsoftonline.cn` |

凭据根据 **National Cloud**（国家云）和 **Tenant ID**（租户 ID）构建授权 URL 和令牌 URL，根据 **Environment URL**（环境 URL）构建作用域：

* **Authorization Code**（授权码）：`<environment-url>/.default offline_access`
* **Client Credentials**（客户端凭据）：`<environment-url>/.default`

例如，`https://contoso.crm.dynamics.com` 对应的 Authorization Code（授权码）作用域为 `https://contoso.crm.dynamics.com/.default offline_access`。

无需手动输入这些 URL 或作用域。节点调用 Dataverse 环境，而非 Microsoft Graph，因此凭据会隐藏 Microsoft Graph 基础 URL 字段。

## 常见问题 <a id="common-issues"></a>

### 重定向 URI 不匹配 <a id="redirect-uri-mismatch"></a>

从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），将完全相同的 URL 注册为 Entra 中的 **Web** 重定向 URI。检查协议、主机、端口和路径，不要替换成 Dataverse 环境 URL。重定向 URI 适用于 **Authorization Code**（授权码），不适用于 **Client Credentials**（客户端凭据）。

### 需要管理员批准 <a id="admin-approval-required"></a>

请 Entra 管理员审核并授予请求的 Dataverse 委派权限，然后重新连接凭据。Entra 授权同意与 Dataverse 安全角色是分别需要满足的要求：仅有授权同意，并不会让用户有权访问环境中的行。

### 令牌请求失败 <a id="token-request-fails"></a>

检查 **Client ID**（客户端 ID）是否属于该应用注册，**Client Secret**（客户端密钥）是否填写当前密钥值，而非密钥 ID。使用 **Client Credentials**（客户端凭据）时，将 `common` 替换为租户 GUID。确认 **National Cloud**（国家云）与环境匹配，**Environment URL**（环境 URL）为该环境的 HTTPS 基础 URL。

### 凭据测试或节点请求返回访问错误 <a id="credential-test-or-node-requests-return-an-access-error"></a>

委派访问时，请验证已登录用户能够访问环境，并具有所需的 Dataverse 安全角色。

仅应用访问时，请验证 **Environment URL**（环境 URL）对应的环境中存在活动的应用程序用户，其应用程序 ID 与 **Client ID**（客户端 ID）相同，且拥有所需角色。仅添加缺失权限，不要授予宽泛的管理员访问权限。

如果凭据测试成功，但表或列选择器失败，请检查选择器需要的元数据访问权限。如果写入失败，请检查目标表及相关行的权限。

## 相关资源 <a id="related-resources"></a>

* [Microsoft Dataverse 节点](../app-nodes/n8n-nodes-base.microsoftdataverse.md)
* [为 Dataverse 注册应用](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/walkthrough-register-app-azure-active-directory)
* [在 Dataverse 中使用 OAuth](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-oauth)
* [管理 Dataverse 应用程序用户](https://learn.microsoft.com/en-us/power-platform/admin/manage-application-users)