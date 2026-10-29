---
title: Convert to File（转换为文件）
description: 了解 n8n 工作流自动化平台中的 Convert to File 节点，包括用法说明和示例链接。
contentType:
- integration
- reference
priority: critical
nodeTitle: Convert to File（转换为文件）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.converttofile.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Convert to File（转换为文件） <a href="#convert-to-file" id="convert-to-file"></a>

使用 Convert to File 节点，将输入数据输出为文件。此节点会将输入的 JSON 数据转换为二进制格式。

{% hint style="info" %}
**Extract From File（从文件提取）**

要从文件提取数据并转换为 JSON，请使用 [Extract from File](n8n-nodes-base.extractfromfile.md) 节点。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* [**Convert to CSV**](#convert-to-csv)（转换为 CSV）
* [**Convert to HTML**](#convert-to-html)（转换为 HTML）
* [**Convert to ICS**](#convert-to-ics)（转换为 ICS）
* [**Convert to JSON**](#convert-to-json)（转换为 JSON）
* [**Convert to ODS**](#convert-to-ods)（转换为 ODS）
* [**Convert to RTF**](#convert-to-rtf)（转换为 RTF）
* [**Convert to Text File**](#convert-to-text-file)（转换为文本文件）
* [**Convert to XLS**](#convert-to-xls)（转换为 XLS）
* [**Convert to XLSX**](#convert-to-xlsx)（转换为 XLSX）
* [**Move Base64 String to File**](#move-base64-string-to-file)（将 Base64 字符串转为文件）

节点参数和选项取决于所选操作。

### Convert to CSV（转换为 CSV） <a href="#convert-to-csv" id="convert-to-csv"></a>

通过 **Put Output File in Field**（输出文件字段）参数配置此操作，填写输出数据中用于存放文件的字段名称。

#### Convert to CSV 选项 <a href="#convert-to-csv-options" id="convert-to-csv-options"></a>

也可以通过以下 **Options**（选项）配置此操作：

* **File Name**（文件名称）：输入生成的输出文件的名称。
* 如果文件首行包含表头名称，开启 **Header Row**（表头行）选项。

### Convert to HTML（转换为 HTML） <a href="#convert-to-html" id="convert-to-html"></a>

通过 **Put Output File in Field**（输出文件字段）参数配置此操作，填写输出数据中用于存放文件的字段名称。

#### Convert to HTML 选项 <a href="#convert-to-html-options" id="convert-to-html-options"></a>

也可以通过以下 **Options**（选项）配置此操作：

* **File Name**（文件名称）：输入生成的输出文件的名称。
* 如果文件首行包含表头名称，开启 **Header Row**（表头行）选项。

### Convert to ICS（转换为 ICS） <a href="#convert-to-ics" id="convert-to-ics"></a>

* **Put Output File in Field**（输出文件字段）：输入输出数据中用于存放文件的字段名称。
* **Event Title**（事件标题）：输入事件标题。
* **Start**（开始）：输入事件开始的日期和时间。全天事件忽略时间部分。
* **End**（结束）：输入事件结束的日期和时间。全天事件忽略时间部分；未设置时，节点使用开始日期。
* **All Day**（全天）：开启时设为全天事件，关闭时不设为全天事件。

#### Convert to ICS 选项 <a href="#convert-to-ics-options" id="convert-to-ics-options"></a>

也可以通过以下 **Options**（选项）配置此操作：

* **File Name**（文件名称）：输入生成的输出文件的名称。
* **Attendees**（参与者）：使用此选项为事件添加参与者。为每位参与者填写：
    * **Name**（姓名）
    * **Email**（电子邮箱）
    * **RSVP**（确认出席）：开启时要求参与者确认出席，关闭时不要求确认。
* **Busy Status**（忙闲状态）：为 Outlook 等 Microsoft 应用设置忙闲状态，可选：
    * **Busy**（忙碌）
    * **Tentative**（暂定）
* **Calendar Name**（日历名称）：对于 Apple 和 Microsoft 日历，输入事件的[日历名称](https://learn.microsoft.com/en-us/openspecs/exchange_server_protocols/ms-oxcical/1da58449-b97e-46bd-b018-a1ce576f3e6d)。
* **Description**（描述）：输入事件描述。
* **Geolocation**（地理位置）：输入事件地点的 **Latitude**（纬度）和 **Longitude**（经度）。
* **Location**（地点）：输入计划举办事件的场所或位置。
* **Recurrence Rule**（重复规则）：输入定义事件重复模式的规则（RRULE）。可使用 [iCalendar.org RRULE 工具](https://icalendar.org/rrule-tool.html)生成规则。
* **Organizer**（组织者）：输入组织者的 **Name**（姓名）和 **Email**（电子邮箱）。
* **Sequence**（修订序号）：如果要发送具有相同通用唯一标识符（UID）的事件更新，输入修订序号。
* **Status**（状态）：设置事件状态，可选：
    * **Confirmed**（已确认）
    * **Cancelled**（已取消）
    * **Tentative**（暂定）
* **UID**：输入事件的通用唯一标识符（UID），应在全局范围内唯一。未填写时，节点会自动生成 UID。
* **URL**：输入与事件相关的 URL。
* **Use Workflow Timezone**（使用工作流时区）：关闭时使用 UTC 时区，开启时使用工作流时区。可在[工作流设置](../../../build/manage-workflows/configure-workflow-settings.md)中配置工作流时区。

### Convert to JSON（转换为 JSON） <a href="#convert-to-json" id="convert-to-json"></a>

根据需求选择合适的输出 **Mode**（模式）：

* **All Items to One File**（所有数据项合并为一个文件）：将所有输入数据项写入同一个文件。
* **Each Item to Separate File**（每个数据项单独生成文件）：为每个输入数据项创建一个文件。

#### Convert to JSON 选项 <a href="#convert-to-json-options" id="convert-to-json-options"></a>

也可以通过以下 **Options**（选项）配置此操作：

* **File Name**（文件名称）：输入生成的输出文件的名称。
* **Format**（格式化）：开启时格式化 JSON，使其更易读；关闭时不格式化。
* **Encoding**（编码）：选择数据编码使用的字符集，默认值为 **utf8**。

### Convert to ODS（转换为 ODS） <a href="#convert-to-ods" id="convert-to-ods"></a>

通过 **Put Output File in Field**（输出文件字段）参数配置此操作，填写输出数据中用于存放文件的字段名称。

#### Convert to ODS 选项 <a href="#convert-to-ods-options" id="convert-to-ods-options"></a>

也可以通过以下 **Options**（选项）配置此操作：

* **File Name**（文件名称）：输入生成的输出文件的名称。
* **Compression**（压缩）：选择是否压缩文件，以减小输出文件大小。
* **Header Row**（表头行）：如果文件首行包含表头名称，开启此选项。
* **Sheet Name**（工作表名称）：输入要在电子表格中创建的工作表名称。

### Convert to RTF（转换为 RTF） <a href="#convert-to-rtf" id="convert-to-rtf"></a>

通过 **Put Output File in Field**（输出文件字段）参数配置此操作，填写输出数据中用于存放文件的字段名称。

#### Convert to RTF 选项 <a href="#convert-to-rft-options" id="convert-to-rft-options"></a>

也可以通过以下 **Options**（选项）配置此操作：

* **File Name**（文件名称）：输入生成的输出文件的名称。
* 如果文件首行包含表头名称，开启 **Header Row**（表头行）选项。

### Convert to Text File（转换为文本文件） <a href="#convert-to-text-file" id="convert-to-text-file"></a>

输入 **Text Input Field**（文本输入字段）的名称，该字段包含要转换为文件的字符串。嵌套字段可使用点表示法，例如 `level1.level2.currentKey`。

#### Convert to Text File 选项 <a href="#convert-to-text-file-options" id="convert-to-text-file-options"></a>

也可以通过以下 **Options**（选项）配置此操作：

* **File Name**（文件名称）：输入生成的输出文件的名称。
* **Encoding**（编码）：选择数据编码使用的字符集，默认值为 **utf8**。

### Convert to XLS（转换为 XLS） <a href="#convert-to-xls" id="convert-to-xls"></a>

通过 **Put Output File in Field**（输出文件字段）参数配置此操作，填写输出数据中用于存放文件的字段名称。

#### Convert to XLS 选项 <a href="#convert-to-xls-options" id="convert-to-xls-options"></a>

也可以通过以下 **Options**（选项）配置此操作：

* **File Name**（文件名称）：输入生成的输出文件的名称。
* **Header Row**（表头行）：如果文件首行包含表头名称，开启此选项。
* **Sheet Name**（工作表名称）：输入要在电子表格中创建的工作表名称。

### Convert to XLSX（转换为 XLSX） <a href="#convert-to-xlsx" id="convert-to-xlsx"></a>

通过 **Put Output File in Field**（输出文件字段）参数配置此操作，填写输出数据中用于存放文件的字段名称。

#### Convert to XLSX 选项 <a href="#convert-to-xlsx-options" id="convert-to-xlsx-options"></a>

也可以通过以下 **Options**（选项）配置此操作：

* **File Name**（文件名称）：输入生成的输出文件的名称。
* **Compression**（压缩）：选择是否压缩文件，以减小输出文件大小。
* **Header Row**（表头行）：如果文件首行包含表头名称，开启此选项。
* **Sheet Name**（工作表名称）：输入要在电子表格中创建的工作表名称。

### Move Base64 String to File（将 Base64 字符串转为文件） <a href="#move-base64-string-to-file" id="move-base64-string-to-file"></a>

输入 **Base64 Input Field**（Base64 输入字段）的名称，该字段包含要转换为文件的 Base64 字符串。嵌套字段可使用点表示法，例如 `level1.level2.currentKey`。

#### Move Base64 String to File 选项 <a href="#move-base64-string-to-file-options" id="move-base64-string-to-file-options"></a>

也可以通过以下 **Options**（选项）配置此操作：

* **File Name**（文件名称）：输入生成的输出文件的名称。
* **MIME Type**（MIME 类型）：输入输出文件的 MIME 类型。常用 MIME 类型及对应的文件扩展名，请参阅[常见 MIME 类型](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types)。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Convert to File 集成模板](https://n8n.io/integrations/convert-to-file)，或[搜索所有模板](https://n8n.io/workflows/)
