---
title: Google Sheets 文档内工作表操作
contentType:
- integration
- reference
priority: critical
nodeTitle: Google Sheets 文档内工作表操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations
description: 了解 n8n 工作流自动化平台中 Google Sheets 节点的工作表操作，包括操作及配置详情，以及示例和凭据信息链接。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 文档内工作表操作 <a id="sheet-within-document-operations"></a>

使用这些操作在 Google Sheets 的电子表格文档中创建、更新、清空或删除工作表。有关 Google Sheets 节点本身的更多信息，请参阅 [Google Sheets](./README.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## Append or Update Row（追加或更新行） <a href="#append-or-update-row" id="append-or-update-row"></a>

此操作用于更新已有行；工作表中没有匹配项时，则在数据末尾添加新行。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Sheets 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Sheet Within Document**（文档内工作表）。
* **Operation**（操作）：选择 **Append or Update Row**（追加或更新行）。
* **Document**（电子表格文档）：选择包含待追加或更新行的工作表的电子表格。
  * 选择 **From list**（从列表）可在下拉列表中按电子表格标题选择，选择 **By URL**（按 URL）可输入电子表格 URL，选择 **By ID**（按 ID）可输入 `spreadsheetId`。
  * 可在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
* **Sheet**（工作表）：选择要追加或更新行的工作表。
  * 选择 **From list**（从列表）可在下拉列表中按工作表标题选择，选择 **By URL**（按 URL）可输入工作表 URL，选择 **By ID**（按 ID）可输入 `sheetId`，选择 **By Name**（按名称）可输入工作表标题。
  * 可在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。
* **Mapping Column Mode**（列映射模式）：
  * **Map Each Column Manually**（手动映射每列）：输入每列的 **Values to Send**（要发送的值）。
  * **Map Automatically**（自动映射）：n8n 自动查找与 Google Sheets 列匹配的输入数据。此模式下，请确保输入数据字段与 Google Sheets 列名一致。必要时，可在此节点前使用 [Edit Fields](../../core-nodes/n8n-nodes-base.set.md)（编辑字段）节点修改字段。
  * **Nothing**（不映射）：不映射任何数据。

### 选项 <a href="#options" id="options"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/googlesheets/node-options.md" %}

更多信息，请参阅 [Method: spreadsheets.values.update | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/update) API 文档。

## Append Row（追加行） <a href="#append-row" id="append-row"></a>

此操作用于在工作表数据末尾追加新行。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Sheets 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Sheet Within Document**（文档内工作表）。
* **Operation**（操作）：选择 **Append Row**（追加行）。
* **Document**（电子表格文档）：选择包含待追加行的工作表的电子表格。
  * 选择 **From list**（从列表）可在下拉列表中按电子表格标题选择，选择 **By URL**（按 URL）可输入电子表格 URL，选择 **By ID**（按 ID）可输入 `spreadsheetId`。
  * 可在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
* **Sheet**（工作表）：选择要追加行的工作表。
  * 选择 **From list**（从列表）可在下拉列表中按工作表标题选择，选择 **By URL**（按 URL）可输入工作表 URL，选择 **By ID**（按 ID）可输入 `sheetId`，选择 **By Name**（按名称）可输入工作表标题。
  * 可在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。
* **Mapping Column Mode**（列映射模式）：
  * **Map Each Column Manually**（手动映射每列）：输入每列的 **Values to Send**（要发送的值）。
  * **Map Automatically**（自动映射）：n8n 自动查找与 Google Sheets 列匹配的输入数据。此模式下，请确保输入数据字段与 Google Sheets 列名一致。必要时，可在此节点前使用 [Edit Fields](../../core-nodes/n8n-nodes-base.set.md)（编辑字段）节点修改字段。
  * **Nothing**（不映射）：不映射任何数据。

### 选项 <a href="#options" id="options"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/googlesheets/node-options.md" %}

更多信息，请参阅 [Method: spreadsheets.values.append | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append) API 文档。

## 清空工作表 <a href="#clear-a-sheet" id="clear-a-sheet"></a>

此操作用于清空工作表中的所有数据。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Sheets 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Sheet Within Document**（文档内工作表）。
* **Operation**（操作）：选择 **Clear**（清空）。
* **Document**（电子表格文档）：选择包含待清空数据的工作表的电子表格。
  * 选择 **From list**（从列表）可在下拉列表中按电子表格标题选择，选择 **By URL**（按 URL）可输入电子表格 URL，选择 **By ID**（按 ID）可输入 `spreadsheetId`。
  * 可在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
* **Sheet**（工作表）：选择要清空数据的工作表。
  * 选择 **From list**（从列表）可在下拉列表中按工作表标题选择，选择 **By URL**（按 URL）可输入工作表 URL，选择 **By ID**（按 ID）可输入 `sheetId`，选择 **By Name**（按名称）可输入工作表标题。
  * 可在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。
* **Clear**（清空范围）：选择要清空工作表中的哪些数据。
  * **Whole Sheet**（整个工作表）：清空整个工作表的数据。开启 **Keep First Row**（保留首行）可保留工作表第一行。
  * **Specific Rows**（指定行）：清空指定行中的数据，还需填写：
    * **Start Row Number**（起始行号）：输入要清空的第一行行号。
    * **Number of Rows to Delete**（清空行数）：输入要清空的行数。`1` 表示仅清空 **Start Row Number**（起始行号）指定行中的数据。
  * **Specific Columns**（指定列）：清空指定列中的数据，还需填写：
    * **Start Column**（起始列）：使用字母表示法输入要清空的第一列。
    * **Number of Columns to Delete**（清空列数）：输入要清空的列数。`1` 表示仅清空 **Start Column**（起始列）指定列中的数据。
  * **Specific Range**（指定范围）：使用 [A1 表示法](https://developers.google.com/sheets/api/guides/concepts#cell)输入要清空数据的表格范围。

更多信息，请参阅 [Method: spreadsheets.values.clear | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/clear) API 文档。

## 创建新工作表 <a href="#create-a-new-sheet" id="create-a-new-sheet"></a>

此操作用于创建新工作表。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Sheets 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Sheet Within Document**（文档内工作表）。
* **Operation**（操作）：选择 **Create**（创建）。
* **Document**（电子表格文档）：选择要在其中创建新工作表的电子表格。
  * 选择 **From list**（从列表）可在下拉列表中按电子表格标题选择，选择 **By URL**（按 URL）可输入电子表格 URL，选择 **By ID**（按 ID）可输入 `spreadsheetId`。
  * 可在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
* **Title**（标题）：输入新工作表的标题。

### 选项 <a href="#options" id="options"></a>

* **Hidden**（隐藏）：开启此选项，在界面中隐藏工作表。
* **Right To Left**（从右到左）：开启此选项，使用从右到左（RTL）的工作表布局，而非从左到右（LTR）。
* **Sheet ID**（工作表 ID）：输入工作表 ID。
  * 可在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。
* **Sheet Index**（工作表索引）：默认将新工作表放在电子表格的最后。若需更改位置，请输入新工作表要使用的索引。在指定索引处添加工作表时，Google 会将其后所有工作表的索引加一。更多信息，请参阅 [Sheets | SheetProperties](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#SheetProperties) 文档。
* **Tab Color**（标签颜色）：输入十六进制颜色代码，或使用颜色选择器设置界面中工作表标签的颜色。

更多信息，请参阅 [Method: spreadsheets.batchUpdate | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate) API 文档。

## 删除工作表 <a href="#delete-a-sheet" id="delete-a-sheet"></a>

此操作用于永久删除工作表。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Sheets 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Sheet Within Document**（文档内工作表）。
* **Operation**（操作）：选择 **Delete**（删除）。
* **Document**（电子表格文档）：选择包含待删除工作表的电子表格。
  * 选择 **From list**（从列表）可在下拉列表中按电子表格标题选择，选择 **By URL**（按 URL）可输入电子表格 URL，选择 **By ID**（按 ID）可输入 `spreadsheetId`。
  * 可在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
* **Sheet**（工作表）：选择要删除的工作表。
  * 选择 **From list**（从列表）可在下拉列表中按工作表标题选择，选择 **By URL**（按 URL）可输入工作表 URL，选择 **By ID**（按 ID）可输入 `sheetId`，选择 **By Name**（按名称）可输入工作表标题。
  * 可在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。

更多信息，请参阅 [Method: spreadsheets.batchUpdate | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate) API 文档。

## Delete Rows or Columns（删除行或列） <a href="#delete-rows-or-columns" id="delete-rows-or-columns"></a>

此操作用于删除工作表中的行或列。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Sheets 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Sheet Within Document**（文档内工作表）。
* **Operation**（操作）：选择 **Delete Rows or Columns**（删除行或列）。
* **Document**（电子表格文档）：选择包含待删除行或列的工作表的电子表格。
  * 选择 **From list**（从列表）可在下拉列表中按电子表格标题选择，选择 **By URL**（按 URL）可输入电子表格 URL，选择 **By ID**（按 ID）可输入 `spreadsheetId`。
  * 可在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
* **Sheet**（工作表）：选择要删除行或列的工作表。
  * 选择 **From list**（从列表）可在下拉列表中按工作表标题选择，选择 **By URL**（按 URL）可输入工作表 URL，选择 **By ID**（按 ID）可输入 `sheetId`，选择 **By Name**（按名称）可输入工作表标题。
  * 可在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。
* **Start Row Number**（起始行号）或 **Start Column**（起始列）：输入开始删除的行号或列字母。
* **Number of Rows to Delete**（删除行数）或 **Number of Columns to delete**（删除列数）：输入要删除的行数或列数。

更多信息，请参阅 [Method: spreadsheets.batchUpdate | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate) API 文档。

## Get Row(s)（获取行） <a href="#get-rows" id="get-rows"></a>

此操作用于读取工作表中的一行或多行。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Sheets 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Sheet Within Document**（文档内工作表）。
* **Operation**（操作）：选择 **Get Row(s)**（获取行）。
* **Document**（电子表格文档）：选择包含待读取行的工作表的电子表格。
  * 选择 **From list**（从列表）可在下拉列表中按电子表格标题选择，选择 **By URL**（按 URL）可输入电子表格 URL，选择 **By ID**（按 ID）可输入 `spreadsheetId`。
  * 可在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
* **Sheet**（工作表）：选择要读取行的工作表。
  * 选择 **From list**（从列表）可在下拉列表中按工作表标题选择，选择 **By URL**（按 URL）可输入工作表 URL，选择 **By ID**（按 ID）可输入 `sheetId`，选择 **By Name**（按名称）可输入工作表标题。
  * 可在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。
* **Filters**（筛选条件）：默认返回工作表中的所有行。设置筛选条件可限制返回的结果：
  * **Column**（列）：选择工作表中要用于搜索的列。
  * **Value**（值）：输入要搜索的单元格值，可将输入数据参数拖入此处。筛选条件匹配多行时，n8n 默认返回第一个结果。如需所有匹配行：
    1. 在 **Options**（选项）中，选择 **Add Option**（添加选项）> **When Filter Has Multiple Matches**（筛选条件有多个匹配项时）。
    2. 将 **When Filter Has Multiple Matches**（筛选条件有多个匹配项时）设为 **Return All Matches**（返回所有匹配项）。

### 选项 <a href="#options" id="options"></a>

* **Data Location on Sheet**（工作表内数据位置）：指定数据范围。默认由 n8n 自动检测范围，直到工作表的最后一行。
* **Output Formatting**（输出格式）：选择 n8n 如何格式化 Google Sheets 返回的数据。
  * **General Formatting**（常规格式）：
    * **Values (unformatted)**（未格式化值，默认）：n8n 移除货币符号及其他特殊格式，数据类型仍为数字。
    * **Values (formatted)**（已格式化值）：n8n 将数字类型转换为字符串，使值按 Google Sheets 中显示的形式呈现，例如保留逗号或货币符号。
    * **Formulas**（公式）：n8n 返回公式，不计算公式结果。例如，单元格 B2 中的公式为 `=A2` 时，n8n 将 B2 的值作为文本 `=A2` 返回。更多信息，请参阅 [About date & time values | Google Sheets](https://developers.google.com/sheets/api/guides/formats#about_date_time_values)（日期和时间值说明）。
  * **Date Formatting**（日期格式）：更多信息，请参阅 [DateTimeRenderOption | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/DateTimeRenderOption)。
    * **Formatted Text**（已格式化文本，默认）：按 Google Sheets 中显示的形式返回，具体取决于电子表格的区域设置，例如 `01/01/2024`。
    * **Serial Number**（序列号）：自 1899 年 12 月 30 日起经过的天数。
  * **When Filter Has Multiple Matches**（筛选条件有多个匹配项时）：设为 **Return All Matches**（返回所有匹配项）可获取多个匹配结果。默认仅返回第一个结果。

{% hint style="info" %}
**第一行**

n8n 将 Google 工作表的第一行视为表头，读取所有行时不会返回该行。如果需要读取第一行，请通过 **Options**（选项）设置 **Data Location on Sheet**（工作表内数据位置）。
{% endhint %}

更多信息，原文引用了 [Method: spreadsheets.batchUpdate | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate) API 文档。译注：该链接说明批量修改接口；本节用于读取行数据，Google 的 spreadsheets.values.get 可读取指定范围的值。

## Update Row（更新行） <a href="#update-row" id="update-row"></a>

此操作仅更新工作表中的已有行。若希望在没有匹配项时追加新行，请改用 **Append or Update Row**（追加或更新行）操作。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Sheets 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Sheet Within Document**（文档内工作表）。
* **Operation**（操作）：选择 **Update Row**（更新行）。
* **Document**（电子表格文档）：选择包含待更新工作表的电子表格。
  * 选择 **From list**（从列表）可在下拉列表中按电子表格标题选择，选择 **By URL**（按 URL）可输入电子表格 URL，选择 **By ID**（按 ID）可输入 `spreadsheetId`。
  * 可在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
* **Sheet**（工作表）：选择要更新的工作表。
  * 选择 **From list**（从列表）可在下拉列表中按工作表标题选择，选择 **By URL**（按 URL）可输入工作表 URL，选择 **By ID**（按 ID）可输入 `sheetId`，选择 **By Name**（按名称）可输入工作表标题。
  * 可在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。
* **Mapping Column Mode**（列映射模式）：
  * **Map Each Column Manually**（手动映射每列）：输入每列的 **Values to Send**（要发送的值）。
  * **Map Automatically**（自动映射）：n8n 自动查找与 Google Sheets 列匹配的输入数据。此模式下，请确保输入数据字段与 Google Sheets 列名一致。必要时，可在此节点前使用 [Edit Fields](../../core-nodes/n8n-nodes-base.set.md)（编辑字段）节点修改字段。
  * **Nothing**（不映射）：不映射任何数据。

### 选项 <a href="#options" id="options"></a>

* **Cell Format**（单元格格式）：选择单元格中的数据格式。更多信息，请参阅 [Google Sheets API | CellFormat](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells#CellFormat)。
  * **Let Google Sheets format**（由 Google Sheets 设置格式，默认）：n8n 按照 Google Sheets 默认设置格式化单元格中的文本和数字。
  * **Let n8n format**（由 n8n 设置格式）：工作表中的新单元格将保持 n8n 所提供输入数据的数据类型。
* **Data Location on Sheet**（工作表内数据位置）：需要指定工作表中的数据范围时，使用此选项。
  * **Header Row**（表头行）：指定包含列标题的行索引。
  * **First Data Row**（首个数据行）：指定实际数据开始的行索引。

更多信息，请参阅 [Method: spreadsheets.batchUpdate | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate) API 文档。
