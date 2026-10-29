---
title: Extract From File（从文件提取）
description: 了解 n8n 工作流自动化平台中的 Extract From File 节点，包括用法说明和示例链接。
contentType:
- integration
- reference
priority: high
nodeTitle: Extract From File（从文件提取）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Extract From File（从文件提取） <a href="#extract-from-file" id="extract-from-file"></a>

n8n 工作流常会接收文件，来源可能是 [HTTP 请求节点][HTTP Request Node]（从网站获取的文件）、[Webhook 节点][Webhook Node]（从其他位置发送到工作流的文件），或本地来源。通过这些方式获得的数据通常采用二进制格式，例如电子表格或 PDF。

Extract From File 节点从二进制格式的文件中提取数据，并将其转换为 JSON，便于工作流后续步骤处理。要将 JSON 转回二进制文件，请参阅 [Convert to File](n8n-nodes-base.converttofile.md) 节点。

## 操作 <a href="#operations" id="operations"></a>

通过 **Operations**（操作）下拉列表，选择要提取数据的源文件格式。

- **Extract From CSV**（从 CSV 提取）：CSV（逗号分隔值）文件常用于表格数据。
- **Extract From HTML**（从 HTML 提取）：从标准网页 HTML 格式文件中提取字段。
- **Extract From JSON**（从 JSON 提取）：从二进制文件中提取 JSON 数据。
- **Extract From ICS**（从 ICS 提取）：从 iCalendar 格式文件中提取字段。
- **Extract From ODS**（从 ODS 提取）：从 ODS 电子表格文件中提取字段。
- **Extract From PDF**（从 PDF 提取）：从可移植文档格式文件中提取字段。
- **Extract From RTF**（从 RTF 提取）：从富文本格式文件中提取字段。
- **Extract From Text File**（从文本文件提取）：从标准文本格式文件中提取字段。
- **Extract From XLS**（从 XLS 提取）：从旧版格式的 Microsoft Excel 文件中提取字段。
- **Extract From XLSX**（从 XLSX 提取）：从 Microsoft Excel 文件中提取字段。
- **Move File to Base64 String**（将文件转为 Base64 字符串）：将二进制数据转换为适合文本传输的 [base64][] 格式。

## 示例工作流 <a href="#example-workflow" id="example-workflow"></a>

此示例使用 Webhook 节点触发工作流。将 CSV 文件发送到 webhook 地址后，Webhook 节点输出文件数据，并由 Extract From File 节点接收。

{% @n8n-blocks/n8n-workflow-demo content="%7B%0A%20%20%22name%22%3A%20%22Extract%20from%20file%20example%22%2C%0A%20%20%22nodes%22%3A%20%5B%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22httpMethod%22%3A%20%22POST%22%2C%0A%20%20%20%20%20%20%20%20%22path%22%3A%20%2206696ea7-9dc7-464a-873b-3feb095b0874%22%2C%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22rawBody%22%3A%20true%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.webhook%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%202%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20-380%2C%0A%20%20%20%20%20%20%20%20-80%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22dfbd51af-6050-47c5-a26c-74cba77f65f7%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Webhook%22%2C%0A%20%20%20%20%20%20%22webhookId%22%3A%20%2206696ea7-9dc7-464a-873b-3feb095b0874%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22headerRow%22%3A%20false%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.extractFromFile%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20-160%2C%0A%20%20%20%20%20%20%20%20-80%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%221b1e4643-8269-402b-83af-dfd90fd6a0b5%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Extract%20from%20File%22%0A%20%20%20%20%7D%0A%20%20%5D%2C%0A%20%20%22pinData%22%3A%20%7B%7D%2C%0A%20%20%22connections%22%3A%20%7B%0A%20%20%20%20%22Webhook%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Extract%20from%20File%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%0A%20%20%7D%2C%0A%20%20%22active%22%3A%20true%2C%0A%20%20%22settings%22%3A%20%7B%0A%20%20%20%20%22executionOrder%22%3A%20%22v1%22%0A%20%20%7D%2C%0A%20%20%22versionId%22%3A%20%22dd2bf7f1-692a-41a8-9c2e-7931de57fa13%22%2C%0A%20%20%22meta%22%3A%20%7B%0A%20%20%20%20%22instanceId%22%3A%20%221060f46e51fc7902c377ab29d7cbfb87696ddf6b3c5c27cbbb65c3cb36e21baf%22%0A%20%20%7D%2C%0A%20%20%22id%22%3A%20%229i3iDZf5MpjlJ2sh%22%2C%0A%20%20%22tags%22%3A%20%5B%5D%0A%7D" url="https://raw.githubusercontent.com/n8n-io/n8n-docs/refs/heads/main/docs/_workflows/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile/webhook-example.json" %}

将操作设为“Extract from CSV”（从 CSV 提取）后，节点会将数据输出为一系列 JSON 行对象：

```
{
  "row": {
  "0": "apple",
  "1": "1",
  "2": "2",
  "3": "3"
  }
  ...
```

{% hint style="info" %}
**通过 webhook 接收文件**

在 Webhook 节点中选择 **Add Options**（添加选项）按钮，再选择 **Raw body**（原始请求体）并开启此设置，让节点输出后续节点所需的二进制文件。
{% endhint %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

### Input Binary Field（输入二进制字段） <a href="#input-binary-field" id="input-binary-field"></a>

输入节点输入数据中包含二进制文件的字段名称，默认值为“data”。

### Destination Output Field（目标输出字段） <a href="#destination-output-field" id="destination-output-field"></a>

输入节点输出中用于存放提取数据的字段名称。

此参数仅适用于以下操作：

- Extract From JSON（从 JSON 提取）
- Extract From ICS（从 ICS 提取）
- Extract From Text File（从文本文件提取）
- Move File to Base64 String（将文件转为 Base64 字符串）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Extract From File 集成模板](https://n8n.io/integrations/extract-from-file)，或[搜索所有模板](https://n8n.io/workflows/)

[HTTP Request Node]: n8n-nodes-base.httprequest/README.md
[Webhook Node]: n8n-nodes-base.webhook/README.md
[base64]: https://datatracker.ietf.org/doc/html/rfc4648#section-4
