---
title: Split Out（拆分）
description: 工作流自动化平台 n8n 中的 Split Out（拆分） 节点文档，包括使用说明和示例链接。
contentType:
- integration
- reference
priority: high
nodeTitle: Split Out（拆分）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.splitout.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Split Out（拆分） <a href="#split-out" id="split-out"></a>

使用 Split Out 节点，将包含列表的单个数据项拆分为多个数据项。例如，将客户列表拆开，使每个客户各对应一个数据项。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置节点。

### Field to Split Out（要拆分的字段） <a href="#field-to-split-out" id="field-to-split-out"></a>

输入包含待拆分列表的字段，将列表拆成独立数据项。

处理二进制数据输入时，在表达式中使用 `$binary` 设置要拆分的字段。

### Include（包含） <a href="#include" id="include"></a>

选择是否在每个新的独立数据项中保留输入数据的其他字段，以及保留方式。

可选择：

* **No Other Fields**（不包含其他字段）：不包含任何其他字段。
* **All Other Fields**（包含所有其他字段）：包含所有其他字段。
* **Selected Other Fields**（包含选定的其他字段）：仅包含所选字段。
    * **Fields to Include**（要包含的字段）：输入要包含的字段列表，以逗号分隔。

## 节点选项 <a href="#node-options" id="node-options"></a>

### Disable Dot Notation（禁用点表示法） <a href="#disable-dot-notation" id="disable-dot-notation"></a>

默认情况下，n8n 启用点表示法，以 `parent.child` 格式引用子字段。开启此选项可禁用点表示法，关闭则继续使用。

### Destination Field Name（目标字段名称） <a href="#destination-field-name" id="destination-field-name"></a>

输入用于存放拆分字段内容的输出字段。

### Include Binary（包含二进制数据） <a href="#include-binary" id="include-binary"></a>

选择是否在新输出中包含输入的二进制数据，开启时包含，关闭时不包含。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Split Out（拆分） 集成模板](https://n8n.io/integrations/split-out)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/data-transformation-actions/data-section-link.md" %}
