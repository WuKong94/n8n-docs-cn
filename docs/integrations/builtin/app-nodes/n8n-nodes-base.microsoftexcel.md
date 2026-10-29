---
title: Microsoft Excel (OneDrive) 节点文档
description: 了解如何在 n8n 中使用 Microsoft Excel (OneDrive) 节点，并按照技术文档将 Microsoft Excel
  (OneDrive) 节点集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: Microsoft Excel (OneDrive) 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Excel (OneDrive) 节点 <a href="#microsoft-excel-365-node" id="microsoft-excel-365-node"></a>

使用 Microsoft Excel (OneDrive) 节点自动处理 Microsoft Excel 中的工作，并将 Microsoft Excel 与其他应用集成。n8n 内置支持多种 Microsoft Excel 功能，包括添加和获取表数据列表及工作簿，以及获取工作表。节点操作存储在 OneDrive 中的工作簿。

本页列出了 Microsoft Excel (OneDrive) 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的 **Authentication**（身份验证）下拉菜单提供三个选项：

- **Excel OAuth2**：专用于 Microsoft Excel 的 OAuth2 凭据，为默认选项。
- **Microsoft OAuth2 (Graph)**：通用 Microsoft Graph 凭据，可在其他 Microsoft 节点中复用。选择此选项时，确保凭据获得该节点所需的作用域，例如 `Files.ReadWrite`；如果管理员已同意的权限是 `Files.ReadWrite.All`，也可使用该权限。
- **Microsoft Entra Service Principal (App-Only)**：通过 Microsoft Entra 应用注册提供仅应用访问，无需用户登录，从节点版本 2 起可用。配置方法和所需应用权限，请参阅 [Microsoft Entra 服务主体凭据](../credentials/microsoftentraserviceprincipal.md)。

有关身份验证设置，请参阅 [Microsoft 凭据](../credentials/microsoft.md)。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果使用政府云租户（美国政府、美国国防部或中国），请确保在 Microsoft 凭据配置中选择正确的 **Microsoft Graph API Base URL（Microsoft Graph API 基础 URL）**。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Table（表）
    * Adds rows to the end of the table（在表的末尾添加行）
    * Retrieve a list of table columns（获取表的列列表）
    * Retrieve a list of table rows（获取表的行列表）
    * Looks for a specific column value and then returns the matching row（查找指定列值并返回匹配行）
* Workbook（工作簿）
    * Adds a new worksheet to the workbook.（向工作簿添加新工作表）
    * Get data of all workbooks（获取全部工作簿的数据）
* Worksheet（工作表）
    * Get all worksheets（获取全部工作表）
    * Get worksheet content（获取工作表内容）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Microsoft Excel (OneDrive) 集成模板](https://n8n.io/integrations/microsoft-excel)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
