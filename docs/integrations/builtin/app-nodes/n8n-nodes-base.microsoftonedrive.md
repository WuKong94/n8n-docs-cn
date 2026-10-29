---
title: Microsoft OneDrive 节点文档
description: 了解如何在 n8n 中使用 Microsoft OneDrive 节点，并按照技术文档将 Microsoft OneDrive 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Microsoft OneDrive 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.microsoftonedrive.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftonedrive
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftonedrive
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft OneDrive 节点 <a href="#microsoft-onedrive-node" id="microsoft-onedrive-node"></a>

使用 Microsoft OneDrive 节点自动处理 Microsoft OneDrive 中的工作，并将其与其他应用集成。n8n 内置支持多种 Microsoft OneDrive 功能，包括创建、更新、删除和获取文件及文件夹。

本页列出了 Microsoft OneDrive 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的 **Authentication**（身份验证）下拉菜单提供三个选项：

- **OneDrive OAuth2**：专用于 Microsoft OneDrive 的 OAuth2 凭据，为默认选项。
- **Microsoft OAuth2 (Graph)**：通用 Microsoft Graph 凭据，可在其他 Microsoft 节点中复用。选择此选项时，确保凭据获得该节点所需的作用域，例如 `Files.ReadWrite.All`。
- **Microsoft Entra Service Principal (App-Only)**：通过 Microsoft Entra 应用注册提供仅应用访问，无需用户登录。配置方法和所需应用权限，请参阅 [Microsoft Entra 服务主体凭据](../credentials/microsoftentraserviceprincipal.md)。

有关身份验证设置，请参阅 [Microsoft 凭据](../credentials/microsoft.md)。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果使用政府云租户（美国政府、美国国防部或中国），请确保在 Microsoft 凭据配置中选择正确的 **Microsoft Graph API Base URL（Microsoft Graph API 基础 URL）**。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* File（文件）
    * Copy a file（复制文件）
    * Delete a file（删除文件）
    * Download a file（下载文件）
    * Get a file（获取文件）
    * Rename a file（重命名文件）
    * Search a file（搜索文件）
    * Share a file（共享文件）
    * Upload a file up to 4MB in size（上传大小不超过 4MB 的文件）
* Folder（文件夹）
    * Create a folder（创建文件夹）
    * Delete a folder（删除文件夹）
    * Get Children (get items inside a folder)（获取子项，即文件夹内的数据项）
    * Rename a folder（重命名文件夹）
    * Search a folder（搜索文件夹）
    * Share a folder（共享文件夹）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Microsoft OneDrive 集成模板](https://n8n.io/integrations/microsoft-onedrive)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Microsoft 的 OneDrive API 文档](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/)。

## 查找文件夹 ID <a href="#find-the-folder-id" id="find-the-folder-id"></a>

对文件夹执行操作时，需要提供其 ID，可通过以下方式查找：

* In the URL of the folder（从文件夹 URL 中获取）
* 使用节点搜索。使用 MS 365 时必须采用此方式，因为 OneDrive 在后台使用 SharePoint：
    1. 选择 **Resource**（资源）> **Folder**（文件夹）。
    2. 选择 **Operation**（操作）> **Search**（搜索）。
    3. 在 **Query**（查询）中输入文件夹名称。
    4. 选择 **Execute step**（执行步骤）。n8n 会运行查询并返回文件夹数据，其中的 `id` 字段包含文件夹 ID。

