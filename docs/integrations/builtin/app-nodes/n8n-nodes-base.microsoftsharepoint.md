---
title: Microsoft SharePoint 节点文档
description: 了解如何在 n8n 中使用 Microsoft SharePoint 节点，并按照技术文档将 Microsoft SharePoint 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Microsoft SharePoint 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.microsoftsharepoint.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsharepoint
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsharepoint
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft SharePoint 节点 <a href="#microsoft-sharepoint-node" id="microsoft-sharepoint-node"></a>

使用 Microsoft SharePoint 节点自动处理 Microsoft SharePoint 中的工作，并将其与其他应用集成。n8n 内置支持多种 Microsoft SharePoint 功能，包括下载、上传和更新文件，管理列表中的数据项，以及获取列表和列表项。

本页列出了 Microsoft SharePoint 节点支持的操作、登录及选择站点的指引、节点第 2 版的变更，以及更多资源的链接。

{% hint style="info" %}
**功能可用范围**

从 n8n 2.37.0 起，向工作流添加 Microsoft SharePoint 节点会创建节点第 2 版，使用 Microsoft Graph API。使用第 1 版构建的工作流仍保留第 1 版，并继续使用原有凭据运行。请参阅[第 1 版之后的变更](#what-changed-from-version-1)。

{% endhint %}

{% hint style="info" %}
**凭据**

节点第 2 版提供两种登录方式，通过 **Authentication**（身份验证）下拉菜单选择：

* **Microsoft OAuth2 (Graph)**：使用通用 [Microsoft OAuth2 凭据](../credentials/microsoft.md)以个人身份登录。在凭据的 **Scope**（作用域）字段填写所需作用域：`Sites.Read.All` 用于读取，`Sites.ReadWrite.All` 用于写入，还需包含 `openid offline_access` 以便刷新令牌。例如，要执行节点的全部操作，请填写 `openid offline_access Sites.ReadWrite.All`。如果组织逐站点授予访问权限，请改用 `openid offline_access Sites.Selected`，并参阅[逐站点访问](#per-site-access)。
* **Microsoft Entra Service Principal (App-Only)**（Microsoft Entra 服务主体，仅应用）：通过 [Microsoft Entra 服务主体凭据](../credentials/microsoftentraserviceprincipal.md)以应用身份登录，适用于没有用户参与的无人值守工作流。为应用注册授予读取所需的 `Sites.Read.All` 和写入所需的 `Sites.ReadWrite.All` 应用程序权限，并授予管理员同意。若要将应用限定于指定站点，请改为授予 `Sites.Selected`，并[逐站点授予访问权限](../credentials/microsoftentraserviceprincipal.md#grant-access-per-site)。

节点第 1 版使用节点专用的 [Microsoft SharePoint 凭据](../credentials/microsoft.md#sharepoint)。第 2 版不提供该选项，因为其令牌面向旧版 SharePoint REST API，无法用于 Microsoft Graph。
{% endhint %}

## 选择登录方式 <a id="choosing-how-to-sign-in"></a>

两种登录方式均支持全部操作。请根据工作流的运行方式选择：

| | Microsoft OAuth2 (Graph) | Microsoft Entra Service Principal (App-Only) |
|---|---|---|
| 登录身份 | 个人 | 应用注册 |
| 适用场景 | 以你的身份操作的工作流，或试用节点 | 无用户参与的无人值守、共享或生产工作流 |
| 访问范围 | 在授予的作用域内，已登录用户有权访问的内容 | 租户中的每个站点，除非使用[逐站点访问](#per-site-access) |
| 授权同意 | 用户登录时同意，可能需要管理员先允许 | 管理员一次性授予管理员同意 |
| 失效条件 | 用户会话被撤销，例如离开组织或重置密码后 | 客户端密钥或证书过期 |
| 设置指南 | [Microsoft OAuth2 凭据](../credentials/microsoft.md) | [Microsoft Entra 服务主体凭据](../credentials/microsoftentraserviceprincipal.md) |

## 操作 <a href="#operations" id="operations"></a>

* **File**（文件）：
    * Download: Download a file.（下载：下载文件）
    * Update: Rename a file, replace its contents, or both.（更新：重命名文件、替换文件内容，或同时执行两者）
    * Upload: Upload a file to a document library.（上传：将文件上传到文档库）
* **Item**（数据项）：
    * Create: Create an item in an existing list.（创建：在已有列表中创建数据项）
    * Create or Update: Create a new item, or update the current one if it already exists (upsert).（创建或更新：创建新数据项；如果已存在，则更新当前数据项，即 upsert）
    * Delete: Delete an item from a list.（删除：从列表中删除数据项）
    * Get: Retrieve an item from a list.（获取：从列表中获取数据项）
    * Get Many: Get specific items in a list or list many items.（获取多项：获取列表中的指定数据项，或列出多条数据项）
    * Update: Update an item in an existing list.（更新：更新已有列表中的数据项）
* **List**（列表）：
    * Get: Retrieve details of a single list.（获取：获取单个列表的详情）
    * Get Many: Retrieve a list of lists.（获取多项：获取列表集合）

## 选择站点 <a id="choosing-a-site"></a>

每项操作都从 **Site**（站点）开始，可通过三种方式设置：

* **From List**（从列表）：按名称搜索组织内的站点。站点搜索需要租户范围的读取权限（`Sites.Read.All` 或 `Sites.ReadWrite.All`），逐站点访问不支持此功能。
* **By URL**（按 URL）：粘贴完整站点地址，例如 `https://contoso.sharepoint.com/sites/mysite`。
* **By ID**（按 ID）：粘贴 Microsoft Graph 文档支持的任一形式的站点 ID，包括站点选择器和 Graph 返回的复合 ID（`contoso.sharepoint.com,<site-GUID>,<web-GUID>`）、单独的站点 GUID、主机名（租户根站点），或 `root`。要查找站点的复合 ID，请通过地址请求：`GET https://graph.microsoft.com/v1.0/sites/contoso.sharepoint.com:/sites/mysite`。

## 逐站点访问 <a id="per-site-access"></a>

部分组织不会授予应用整个 SharePoint 租户的访问权限，而是使用 `Sites.Selected` 权限，逐个授予应用访问指定站点的权限。节点完整支持此方式：除站点搜索外，所有操作和选择器均可使用；Microsoft Graph 不支持在缺少租户范围读取权限时搜索站点。请将 **Site**（站点）字段设为 **By URL**（按 URL）或 **By ID**（按 ID），这两种方式均无需搜索。

逐站点访问的设置方式如下：

* **Signing in as an app**（以应用身份登录）：为应用注册授予 `Sites.Selected` 应用程序权限及管理员同意，再逐站点授予应用 `read` 或 `write` 访问权限。请参阅[逐站点授予访问权限](../credentials/microsoftentraserviceprincipal.md#grant-access-per-site)，或参阅[使用 Azure CLI 配置 SharePoint 应用注册](../credentials/microsoftentraserviceprincipal-sharepoint.md)，获取包含权限清单的可复制设置步骤。
* **Signing in as a person**（以个人身份登录）：将凭据的 **Scope**（作用域）字段设为 `openid offline_access Sites.Selected`。相同的逐站点授权也适用于应用注册，已登录账户本身也需要有权访问站点。

## 第 1 版之后的变更 <a id="what-changed-from-version-1"></a>

第 2 版基于 Microsoft Graph API 重构了节点。已有工作流仍保留构建时使用的版本，因此在添加新节点或切换工作流前，不会发生变化。切换时请注意：

* **凭据发生变化。**第 2 版使用通用 Microsoft OAuth2 凭据登录，也新增 Microsoft Entra 服务主体凭据，用于无人值守的仅应用工作流。第 2 版不提供第 1 版的 **Microsoft SharePoint** 凭据：其令牌面向旧版 SharePoint REST API，调用 Microsoft Graph 会失败。第 1 版工作流继续使用原凭据。
* **数据项更新使用 Microsoft 文档中的路由。**第 1 版通过可用但未在 Microsoft 文档中记录的路由更新数据项。第 2 版改用文档中的 Microsoft Graph 端点，返回与原先相同的输出，因此工作流不会感知差异。对于匹配列识别出多条数据项的情况，第 2 版也更严格：**Update**（更新）和 **Create or Update**（创建或更新）都会明确报错并停止，不再像第 1 版 **Create or Update** 那样创建重复项。
* **下载文件时先获取下载链接。**第 2 版先向 Microsoft Graph 请求文件元数据和短期有效、预先授权的下载链接，再通过该链接获取内容。链接请求本身不会携带登录信息，因为链接已获得授权。下载文件与第 1 版一致，包括文件名。

## 常见问题 <a id="common-issues"></a>

* **逐站点权限下站点搜索失败。**Microsoft Graph 无法为仅有逐站点访问权限的凭据列出站点。请将 **Site**（站点）字段切换为 **By URL**（按 URL）或 **By ID**（按 ID）；如果需要搜索，则授予租户范围的读取权限（`Sites.Read.All` 或 `Sites.ReadWrite.All`）。
* **403 错误指出缺少权限。**节点的权限错误会指出操作所需的 Microsoft Graph 权限，例如 `Sites.ReadWrite.All (or Sites.Selected granted with write access for this site)`。授予该权限，应用程序权限还需管理员同意，然后重试。使用逐站点访问时，还需检查应用是否已获准访问当前站点。
* **服务主体凭据测试通过，但操作失败。**从 n8n 2.40.0 起，连接测试仅检查应用注册能否登录，不检查其持有的权限。请确认 SharePoint 应用程序权限已获管理员同意；使用逐站点访问时，还需确认应用已获站点访问权限。请参阅 [Microsoft Entra 服务主体凭据文档](../credentials/microsoftentraserviceprincipal.md)。
* **连接凭据时出现 AADSTS 错误码。**Microsoft 拒绝了登录或令牌交换，例如 AADSTS7000215（客户端密钥无效）、AADSTS7000222（客户端密钥已过期）或 AADSTS700027（证书断言被拒绝）。请参阅 [Microsoft Entra 服务主体凭据文档中的常见问题](../credentials/microsoftentraserviceprincipal.md#common-issues)。
* **上传超过 250 MB 的文件失败。** **File: Upload**（文件：上传）和 **File: Update**（文件：更新）通过单个请求发送内容，上限为 250 MB，尚不支持分块上传更大的文件。
* **筛选大型列表失败。**SharePoint 对超过 5,000 条数据项的列表，仅支持在已建立索引的列上筛选。请在 SharePoint 的 **List settings**（列表设置）> **Indexed columns**（索引列）中添加索引，或改在已有索引的列上筛选。
* **创建或更新数据项时出现唯一约束错误。**列表中某列要求值唯一，而正在写入的值已存在于另一条数据项。请更改值，或在 SharePoint 中放宽该列的 **Enforce unique values**（强制唯一值）设置。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Microsoft SharePoint 集成模板](https://n8n.io/integrations/microsoft-sharepoint)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>


节点第 2 版使用 Microsoft Graph API。有关该服务的更多信息，请参阅 [Microsoft 的 SharePoint Graph 文档](https://learn.microsoft.com/en-us/graph/api/resources/sharepoint)。第 1 版使用 [SharePoint REST API](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service)。
