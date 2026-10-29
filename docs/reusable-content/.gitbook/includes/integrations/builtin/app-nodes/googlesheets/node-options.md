---
title: 节点选项
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

- **Cell Format**（单元格格式）：选择单元格中的数据格式。更多信息，请参阅 [Google Sheets API | CellFormat](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells#CellFormat)。
    - **Let Google Sheets format**（由 Google Sheets 设置格式，默认）：n8n 按照 Google Sheets 默认设置格式化单元格中的文本和数字。
    - **Let n8n format**（由 n8n 设置格式）：工作表中的新单元格将保持 n8n 所提供输入数据的数据类型。
- **Data Location on Sheet**（工作表内数据位置）：需要指定工作表的数据范围时，使用此选项。
    - **Header Row**（表头行）：指定包含列标题的行索引。
    - **First Data Row**（首个数据行）：指定实际数据开始的行索引。
- **Handling extra fields in input**（处理输入中的额外字段）：使用 **Mapping Column Mode > Map Automatically**（列映射模式 > 自动映射）时，通过此选项决定如何处理与工作表现有列不匹配的输入字段。
    - **Insert in New Column(s)**（插入新列，默认）：为所有额外数据添加新列。
    - **Ignore Them**（忽略）：忽略与现有列不匹配的额外数据。
    - **Error**（报错）：抛出错误并停止执行。
- **Use Append**（使用追加接口）：开启此选项，使用 [Google API append 端点](https://developers.google.com/sheets/api/guides/values#append_values)添加新的数据行。
    - 默认情况下，n8n 先追加空行或空列，再添加新数据。这种方式可确保数据对齐，但效率可能较低。使用 append 端点可减少 API 调用次数、简化流程，从而提高性能。不过，如果现有工作表数据不连续，例如行列之间存在空隙或断层，n8n 可能将新数据添加到错误位置，导致错位。
    - 当性能优先，且工作表数据结构连续、没有空隙时，可使用此选项。

