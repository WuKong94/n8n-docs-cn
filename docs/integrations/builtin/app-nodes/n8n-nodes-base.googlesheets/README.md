---
title: Google Sheets
description: 了解 n8n 中的 Google Sheets 节点，包括操作及配置详情，以及示例和凭据信息链接。
contentType:
- integration
- reference
priority: critical
nodeTitle: n8n-nodes-base.googlesheets
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Sheets <a href="#google-sheets" id="google-sheets"></a>

使用 Google Sheets 节点自动处理 Google Sheets 中的工作，并将其与其他应用集成。n8n 内置支持多种 Google Sheets 功能，包括文档及其中数据的创建、更新、删除、追加、移除和获取。

本页列出了 Google Sheets 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Google Sheets 凭据](../../credentials/google/README.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* **Document**（电子表格文档）
    * [**Create**](document-operations.md#create-a-spreadsheet)（创建）电子表格。
    * [**Delete**](document-operations.md#delete-a-spreadsheet)（删除）电子表格。
* **Sheet Within Document**（文档内工作表）
    * [**Append or Update Row**](sheet-operations.md#append-or-update-row)（追加或更新行）：追加新行，已有匹配行时则更新。
    * [**Append Row**](sheet-operations.md#append-row)（追加行）：创建新行。
    * [**Clear**](sheet-operations.md#clear-a-sheet)（清空）工作表中的所有数据。
    * [**Create**](sheet-operations.md#create-a-new-sheet)（创建）新工作表。
    * [**Delete**](sheet-operations.md#delete-a-sheet)（删除）工作表。
    * [**Delete Rows or Columns**](sheet-operations.md#delete-rows-or-columns)（删除行或列）：从工作表中删除列和行。
    * [**Get Row(s)**](sheet-operations.md#get-rows)（获取行）：读取工作表中的所有行。
    * [**Update Row**](sheet-operations.md#update-row)（更新行）：更新工作表中的行。


## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Google Sheets 集成模板](https://n8n.io/integrations/google-sheets)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Google Sheets API 文档](https://developers.google.com/sheets/api)。



## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见问题及建议的解决方法，请参阅[常见问题](common-issues.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
