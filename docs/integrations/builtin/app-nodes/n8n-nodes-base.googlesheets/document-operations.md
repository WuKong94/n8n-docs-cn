---
title: Google Sheets 文档操作
contentType:
- integration
- reference
priority: critical
nodeTitle: Google Sheets 文档操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations
description: 了解 n8n 工作流自动化平台中 Google Sheets 节点的文档操作，包括操作及配置详情，以及示例和凭据信息链接。
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


# 电子表格文档操作 <a id="document-operations"></a>

使用这些操作在 Google Sheets 中创建或删除 Google 电子表格。有关 Google Sheets 节点本身的更多信息，请参阅 [Google Sheets](./README.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 创建电子表格 <a href="#create-a-spreadsheet" id="create-a-spreadsheet"></a>

此操作用于创建新电子表格。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Sheets 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Document**（电子表格文档）。
* **Operation**（操作）：选择 **Create**（创建）。
* **Title**（标题）：输入要创建的电子表格标题。
* **Sheets**（工作表）：添加要在电子表格中创建的各个工作表的 **Title(s)**（标题）。

### 选项 <a href="#options" id="options"></a>

* **Locale**（区域设置）：输入电子表格的区域设置。这会影响函数、日期和货币等格式细节。使用以下格式之一：
  * `en` (639-1)
  * `fil`（639-2 用于不存在 639-1 格式的情况）
  * `en_US`（ISO 语言代码与国家代码的组合）。
  * 语言和国家代码，请参阅 [ISO 639 语言代码列表](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)及 [ISO 3166 国家代码列表](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)。请注意，Google 不支持所有区域设置或语言。
* **Recalculation Interval**（重新计算间隔）：选择电子表格函数的重新计算间隔，会影响 `NOW`、`TODAY`、`RAND` 和 `RANDBETWEEN` 的更新频率。选择 **On Change**（发生更改时），在电子表格发生变化时重新计算；选择 **Minute**（每分钟）或 **Hour**（每小时），分别按分钟或小时重新计算。更多信息，请参阅[设置电子表格的位置和计算设置](https://support.google.com/docs/answer/58515)。

更多信息，请参阅 [Method: spreadsheets.create | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/create) API 文档。

## 删除电子表格 <a href="#delete-a-spreadsheet" id="delete-a-spreadsheet"></a>

此操作用于删除已有电子表格。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Sheets 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Document**（电子表格文档）。
* **Operation**（操作）：选择 **Delete**（删除）。
* **Document**（电子表格文档）：选择要删除的电子表格。
  * 选择 **From list**（从列表）可在下拉列表中按标题选择，选择 **By URL**（按 URL）可输入电子表格 URL，选择 **By ID**（按 ID）可输入 `spreadsheetId`。
  * 可在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。

更多信息，请参阅 [Method: files.delete | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/delete) API 文档。
