---
title: Microsoft Excel (SharePoint) 节点文档
description: 了解如何在 n8n 中使用 Microsoft Excel (SharePoint) 节点，并按照技术文档将 Microsoft Excel
  (SharePoint) 节点集成到工作流中。
contentType:
- integration
- reference
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Excel (SharePoint) 节点 <a id="microsoft-excel-sharepoint-node"></a>

使用 Microsoft Excel (SharePoint) 节点读写存储在 SharePoint 文档库中的 Excel 工作簿，包括通过 Microsoft Teams 站点共享的工作簿。

本页列出了 Microsoft Excel (SharePoint) 节点支持的操作、选择工作簿的指引，以及更多资源的链接。

{% hint style="info" %}
**凭据**

节点提供两种登录方式，通过 **Authentication**（身份验证）下拉菜单选择：

* **Microsoft OAuth2 (Graph)**：使用通用 [Microsoft OAuth2 凭据](../credentials/microsoft.md)以个人身份登录。在凭据的 **Scope**（作用域）字段填写节点所需作用域：`Sites.Read.All` 用于浏览和读取，`Sites.ReadWrite.All` 用于写入，还需包含 `openid offline_access`，让凭据能够刷新令牌。例如，要执行节点的全部操作，请填写 `openid offline_access Sites.ReadWrite.All`。
* **Microsoft Entra Service Principal (App-Only)**（Microsoft Entra 服务主体，仅应用）：使用 [Microsoft Entra 服务主体凭据](../credentials/microsoftentraserviceprincipal.md)以应用身份登录，适用于没有用户参与的无人值守工作流。为应用注册授予读取所需的 `Sites.Read.All` 和写入所需的 `Sites.ReadWrite.All`，并授予管理员同意。若要将应用限定于指定站点，请改为逐站点授予 `Sites.Selected`。

此节点仅接受上述凭据。节点专用的 **Microsoft Excel** 和 **Microsoft SharePoint** 凭据无法用于它：Excel 凭据不包含 SharePoint（`Sites.*`）作用域，SharePoint 凭据则为 SharePoint REST API 签发令牌，而此节点使用 Microsoft Graph。
{% endhint %}

## 应该使用哪个 Excel 节点？ <a id="which-excel-node-should-i-use"></a>

n8n 提供两个 Excel 节点：

* **Microsoft Excel (OneDrive)**：用于存储在个人或企业 OneDrive 中的工作簿。
* **Microsoft Excel (SharePoint)**（本节点）：用于存储在 SharePoint 文档库中的工作簿，包括 Teams 站点背后的文件。此节点也支持仅应用登录，适用于无人值守工作流。

如果有人向你共享工作簿链接，且链接指向 SharePoint 站点，就应使用此节点。

## 选择工作簿 <a id="choosing-a-workbook"></a>

指定工作簿有三种方式：

* **Paste the workbook's address**（粘贴工作簿地址，默认）：通过 SharePoint 或 Excel 的 **Share**（共享）> **Copy link**（复制链接）复制地址，粘贴到 **Workbook**（工作簿）字段。复制按钮提供的链接可直接使用，无需先选择站点或文档库。
* **Pick from a list**（从列表中选择）：选择 **Site**（站点）和 **Document Library**（文档库），再按名称搜索工作簿。
* **By ID**（按 ID）：直接粘贴工作簿 ID。

## 操作 <a id="operations"></a>

* **Sheet**（工作表）：
  * Append: append rows to the end of a sheet.（追加：在工作表末尾追加行）
  * Append or Update: append a new row or update the current one if it already exists.（追加或更新：追加新行；如果行已存在，则更新当前行）
  * Clear: clear a sheet or a range.（清空：清空工作表或区域）
  * Delete: delete a sheet.（删除：删除工作表）
  * Get Many: retrieve a list of the workbook's sheets.（获取多项：获取工作簿的工作表列表）
  * Get Rows: read rows from a range or the used range of a sheet.（获取行：从指定区域或工作表已用区域读取行）
  * Update: update rows matched by a column value.（更新：更新与某列值匹配的行）
* **Table**（表）：
  * Append: append rows to the end of a table.（追加：在表末尾追加行）
  * Convert to Range: convert a table to a plain range of cells.（转换为区域：将表转换为普通单元格区域）
  * Create: create a table from a range of cells.（创建：通过单元格区域创建表）
  * Delete: delete a table.（删除：删除表）
  * Get Columns: retrieve a list of the table's columns.（获取列：获取表的列列表）
  * Get Many: retrieve a list of the workbook's tables.（获取多项：获取工作簿的表列表）
  * Get Rows: retrieve a list of the table's rows.（获取行：获取表中的行列表）
  * Lookup: look for a specific column value and then return the matching row.（查找：搜索指定列值，并返回匹配行）
* **Workbook**（工作簿）：
  * Add Sheet: add a new sheet to the workbook.（添加工作表：向工作簿添加新工作表）
  * Delete: delete a workbook.（删除：删除工作簿）
  * Get Many: retrieve a list of the document library's workbooks.（获取多项：获取文档库中的工作簿列表）

后续还会增加更多操作，本文将随功能发布更新。

## 模板与示例 <a id="templates-and-examples"></a>

[搜索所有模板](https://n8n.io/workflows/)，查看使用此节点的示例。

## 相关资源 <a id="related-resources"></a>

有关该服务的更多信息，请参阅 [Microsoft Excel Graph API 文档](https://learn.microsoft.com/en-us/graph/api/resources/excel)。
