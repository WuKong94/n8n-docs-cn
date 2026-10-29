---
title: 使用 Azure CLI 配置 SharePoint 应用注册
description: 通过权限清单片段和可复制的 Azure CLI 命令，为 n8n 的 Microsoft SharePoint 节点创建遵循最小权限原则的
  Microsoft Entra 应用注册。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 使用 Azure CLI 配置 SharePoint 应用注册 <a id="provision-a-sharepoint-app-registration-with-the-azure-cli"></a>

本文从全新的 Microsoft 365 租户开始，说明如何创建可供 [Microsoft SharePoint 节点](../app-nodes/n8n-nodes-base.microsoftsharepoint.md)通过 [Microsoft Entra 服务主体凭据](microsoftentraserviceprincipal.md)登录的应用注册。文中提供可粘贴的权限清单片段、可运行的脚本，以及大多数配置容易遗漏的逐站点授权步骤。

本文面向批准并创建应用注册的管理员。如果安全团队需要审核权限请求，权限清单片段和权限表就是应提供的审核内容。

Microsoft SharePoint 节点从第 2 版起支持仅应用访问。

## 开始前 <a id="before-you-start"></a>

需要：

- 已安装 [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)，并通过 `az login --tenant <your-tenant-id>` 登录。
- 能够创建应用注册并授予管理员同意的账户。授予管理员同意需要 Global Administrator（全局管理员）或 Privileged Role Administrator（特权角色管理员）角色。
- 工作流将使用的各个 SharePoint 站点地址，例如 `https://contoso.sharepoint.com/sites/mysite`。

## 选择权限级别 <a id="choose-a-permission-level"></a>

三个选项均为 Microsoft Graph **Application**（应用程序）权限。同名委派权限是另一类权限，不适用于仅应用访问。

| 权限 | 应用可以访问的范围 | 适用情况 |
|---|---|---|
| `Sites.Selected` | 仅访问你授予的站点，并使用你为每个站点分配的角色 | 默认选项。应用最初无法访问任何内容，因此安全团队无需批准整个租户的访问权限即可批准应用。 |
| `Sites.Read.All` | 租户中的所有站点，只读 | 工作流需要读取多个站点，或需要使用节点的站点搜索功能 |
| `Sites.ReadWrite.All` | 租户中的所有站点，读写 | 工作流需要写入多个站点，或需要使用节点的站点搜索功能 |

使用 `Sites.Selected` 时，读写权限不是在清单中选择的。应用注册只请求一项权限，随后在[授予应用站点访问权限](#grant-the-app-access-to-a-site)时，逐站点决定授予读取还是写入权限。

站点搜索，即 **Site**（站点）字段的 **From List**（从列表）选项，需要租户范围的读取权限。使用 `Sites.Selected` 时，请将 **Site** 字段设为 **By URL**（按 URL）或 **By ID**（按 ID），这两种方式均无需搜索。

## 权限清单片段 <a id="the-permission-manifest-fragment"></a>

将以下内容保存为 `n8n-sharepoint-permissions.json`。它仅向 Microsoft Graph 请求 `Sites.Selected` 权限：

{% code title="n8n-sharepoint-permissions.json" %}
```json
[
	{
		"resourceAppId": "00000003-0000-0000-c000-000000000000",
		"resourceAccess": [
			{
				"id": "883ea226-0bf2-4a8f-9f9d-92c9162a727d",
				"type": "Role"
			}
		]
	}
]
```
{% endcode %}

如果要使用租户范围权限，请替换其中唯一的 `id` 值：

| 应用程序权限 | `id` 值 | `type` |
|---|---|---|
| `Sites.Selected` | `883ea226-0bf2-4a8f-9f9d-92c9162a727d` | `Role` |
| `Sites.Read.All` | `332a536c-c7ef-4017-ab91-336970924f0d` | `Role` |
| `Sites.ReadWrite.All` | `9492366f-7969-46a4-8d15-ed1a20078fff` | `Role` |

`resourceAppId` 代表 Microsoft Graph。SharePoint 节点调用 Microsoft Graph，因此指向旧版 SharePoint Online API（`00000003-0000-0ff1-ce00-000000000000`）的片段不会授予节点可用的任何权限。`type` 始终为 `Role`：`Role` 表示应用程序权限，`Scope` 表示委派权限。

此文件有两种使用方式：

- **Azure CLI**：以 `--required-resource-accesses @n8n-sharepoint-permissions.json` 参数传入，下方脚本采用此方式。
- **Microsoft Entra admin center**（Microsoft Entra 管理中心）：打开应用注册，选择 **Manifest**（清单），将数组粘贴为 `requiredResourceAccess` 的值。

## 使用 Azure CLI 配置应用注册 <a id="provision-the-app-registration-with-the-azure-cli"></a>

在包含 `n8n-sharepoint-permissions.json` 的文件夹中运行以下命令。它们会创建应用注册和客户端密钥，随后授予管理员同意，同时创建应用的服务主体：

```bash
# Create the app registration for this tenant only, with the permission already requested
APP_ID=$(az ad app create \
	--display-name "n8n SharePoint" \
	--sign-in-audience AzureADMyOrg \
	--required-resource-accesses @n8n-sharepoint-permissions.json \
	--query appId --output tsv)

# Create a client secret valid for one year, and print it once
az ad app credential reset \
	--id "$APP_ID" \
	--display-name "n8n credential" \
	--years 1 \
	--query password --output tsv

# Grant admin consent. This also creates the app's service principal in the tenant
az ad app permission admin-consent --id "$APP_ID"

# Print the two IDs you enter in n8n
echo "Application (client) ID: $APP_ID"
echo "Directory (tenant) ID: $(az account show --query tenantId --output tsv)"
```

从第二条命令的输出中复制密钥。Microsoft 仅显示一次。

请注意以下事项：

- **将 `--append` 添加到 `az ad app credential reset`，以用于已有应用注册。**否则，命令会移除应用已有的密钥和证书，使用这些凭据的服务将停止工作。
- **授予同意前，不要运行 `az ad sp create`。**`az ad app permission admin-consent` 会自行创建服务主体。如果已存在服务主体，授予同意会失败，返回 `Request_BadRequest`，并提示“The `<application-client-id>` service principal name is already present for the tenant”（该租户已存在此服务主体名称）。
- **首次运行时，管理员同意可能失败。**Microsoft Entra 需要几秒钟复制新建的应用注册。命令会返回 `Directory_ObjectNotFound`，并提示“Unable to read the company information from the directory”（无法从目录读取公司信息）。稍等后再次运行。
- **如果管理员同意持续失败，请改在门户中授予。**`az ad app permission admin-consent` 调用旧版 Azure 端点，并不适用于所有账户。在 Microsoft Entra 管理中心打开应用注册的 **API permissions**（API 权限）页面，选择 **Grant admin consent for `<your-tenant>`**（为该租户授予管理员同意）。

## 授予应用站点访问权限 <a id="grant-the-app-access-to-a-site"></a>

如果选择了租户范围权限，请跳过本节。仅有 `Sites.Selected` 的应用无法访问任何站点，必须由管理员逐站点授予访问权限。Microsoft Entra 管理中心和 SharePoint 管理中心都没有执行此步骤的页面，因此配置时容易遗漏。在完成前，每项操作都会因 403 错误而失败。

只读工作流授予 `read`；需要上传文件或修改列表项的工作流授予 `write`。

需要站点 ID，可通过地址请求获取：

```http
GET https://graph.microsoft.com/v1.0/sites/contoso.sharepoint.com:/sites/mysite
```

### PnP PowerShell <a id="pnp-powershell"></a>

SharePoint 管理员可使用 [PnP PowerShell](https://pnp.github.io/powershell/)。先连接站点，再授予应用对该站点的访问权限：

```powershell
Connect-PnPOnline -Url "https://contoso.sharepoint.com/sites/mysite" -Interactive -ClientId <pnp-app-client-id>

Grant-PnPEntraIDAppSitePermission -AppId <application-client-id> -DisplayName "n8n SharePoint" -Permissions Write
```

`-Permissions` 接受 `Read`、`Write`、`Manage` 或 `FullControl`。节点需要 `Read` 或 `Write`。

交互式登录需要为 PnP PowerShell 单独注册应用，可通过 `Register-PnPEntraIDAppForInteractiveLogin` 创建。将该应用的客户端 ID 作为 `-ClientId` 传入。

### Microsoft Graph <a id="microsoft-graph"></a>

以具有 `Sites.FullControl.All` 权限的管理员身份，向每个站点发送一条请求：

```http
POST https://graph.microsoft.com/v1.0/sites/<site-id>/permissions
Content-Type: application/json

{
	"roles": ["write"],
	"grantedToIdentities": [
		{
			"application": {
				"id": "<application-client-id>",
				"displayName": "n8n SharePoint"
			}
		}
	]
}
```

[Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer) 可发送此请求。先打开 **Modify permissions**（修改权限），同意授予 `Sites.FullControl.All`。此请求返回 403 时的含义，请参阅[逐站点授予访问权限](microsoftentraserviceprincipal.md#grant-access-per-site)。

### 为什么 Azure CLI 无法执行此步骤 <a id="why-the-azure-cli-cant-do-this-step"></a>

即使以全局管理员身份登录，对同一端点执行 `az rest --method POST` 也会返回 403。Azure CLI 以其自身由 Microsoft 拥有的应用身份登录，而该应用没有 `Sites.FullControl.All`。在自己的应用注册中同意授予此权限，不会改变 Azure CLI 令牌携带的权限。请改用 PnP PowerShell 或 Graph Explorer。

## 在 n8n 中完成设置 <a id="finish-the-setup-in-n8n"></a>

1. 创建 **Microsoft Entra Service Principal**（Microsoft Entra 服务主体）凭据。输入脚本输出的目录（租户）ID、应用程序（客户端）ID 和客户端密钥。证书选项及主权云的设置，请参阅 [Microsoft Entra 服务主体凭据](microsoftentraserviceprincipal.md)。
2. 在 Microsoft SharePoint 节点中，将 **Authentication**（身份验证）设为 **Microsoft Entra Service Principal (App-Only)**（Microsoft Entra 服务主体，仅应用），选择该凭据。
3. 将 **Site**（站点）字段设为 **By URL**（按 URL），粘贴已授予应用访问权限的站点地址。
4. 运行节点。

从 n8n 2.40.0 起，凭据连接测试仅检查应用能否登录。缺少权限、管理员同意或逐站点授权时，测试仍会通过，但节点运行时会因 403 错误而失败，并指出操作所需的权限。

## 相关资源 <a id="related-resources"></a>

- [Microsoft Entra 服务主体凭据](microsoftentraserviceprincipal.md)
- [Microsoft SharePoint 节点](../app-nodes/n8n-nodes-base.microsoftsharepoint.md)
- [Microsoft 凭据](microsoft.md)
- [Sites.Selected 概述](https://learn.microsoft.com/en-us/graph/permissions-selected-overview)
- [创建站点权限](https://learn.microsoft.com/en-us/graph/api/site-post-permissions)
- [Grant-PnPEntraIDAppSitePermission](https://pnp.github.io/powershell/cmdlets/Grant-PnPEntraIDAppSitePermission.html)
