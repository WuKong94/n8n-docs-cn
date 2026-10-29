---
title: HTML 节点
description: 了解 n8n 中 HTML 节点的用法，并查看相关示例。
contentType:
- integration
- reference
priority: high
nodeTitle: HTML 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.html.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.html
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.html
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# HTML <a href="#html" id="html"></a>

HTML 节点提供在 n8n 中处理 HTML 的操作。

{% hint style="info" %}
**功能可用性**

HTML 节点自 n8n 0.213.0 起提供，替代 HTML Extract 节点。使用较早版本时，仍可查看 [HTML Extract 节点文档](https://github.com/n8n-io/n8n-docs/blob/86fe33b681621e618e3adcab9a27e8605dbc23ad/docs/integrations/builtin/core-nodes/n8n-nodes-base.htmlextract.md)。
{% endhint %}
{% hint style="warning" %}
**跨站脚本**

使用 HTML 节点生成模板时，可能引入 [XSS（跨站脚本）](https://community.owasp.org/attacks/xss/)风险，请谨慎处理不可信输入。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* [**Generate HTML template**](#generate-html-template)（生成 HTML 模板）：将工作流数据输出为 HTML 模板。
* [**Extract HTML content**](#extract-html-content)（提取 HTML 内容）：从 JSON 或二进制文件（`.html`）形式的 HTML 来源中提取内容。
* [**Convert to HTML Table**](#convert-to-html-table)（转换为 HTML 表格）：将内容转换为 HTML 表格。

可用参数和选项取决于所选操作，各操作的详细配置见下文。

## Generate HTML template（生成 HTML 模板） <a href="#generate-html-template" id="generate-html-template"></a>

创建 HTML 模板，将工作流数据输出为 HTML。

可包含：

* 标准 HTML
* `<style>` 标签中的 CSS。
* `<script>` 标签中的 JavaScript，n8n 不会执行这些 JavaScript。
* 用 `{{}}` 包裹的表达式。

模板可使用[表达式](../../../build/work-with-data/expressions-versus-data-nodes.md)，包括 n8n 的[内置方法和变量](../../../build/code-in-n8n/use-built-in-shortcuts.md)。

## Extract HTML Content（提取 HTML 内容） <a href="#extract-html-content" id="extract-html-content"></a>

从 HTML 来源中提取内容，来源可为 JSON 或二进制文件（`.html`）。

使用以下参数：

### Source Data（来源数据） <a href="#source-data" id="source-data"></a>

选择 HTML 内容的来源类型：

* **JSON**：填写 **JSON Property**（JSON 属性），指定包含待提取 HTML 的输入名称；该属性可包含字符串或字符串数组。
* **Binary**（二进制）：填写 **Input Binary Field**（输入二进制字段），指定包含待提取 HTML 的输入名称；该属性可包含字符串或字符串数组。

### Extraction Values（提取值） <a href="#extraction-values" id="extraction-values"></a>

- **Key**（键）：用于保存提取值的键名。
- **CSS Selector**（CSS 选择器）：用于搜索的 CSS 选择器。
- **Return Value**（返回值）：选择返回数据类型：
    - **Attribute**（属性）：返回元素的属性值，例如 `class`。
        - 选择此项后，输入要返回值的 **Attribute**（属性）名称。
    - **HTML**：返回元素包含的 HTML。
    - **Text**（文本）：返回元素的文本内容。
        - 选择此项后，可在 **Skip Selectors**（跳过的选择器）中输入以逗号分隔的选择器列表。
    - **Value**（值）：返回 input、select 或 textarea 元素的值。
- **Return Array**（返回数组）：开启时，将多个提取值作为数组返回；关闭时，作为单个字符串返回。

### Extract HTML Content（提取 HTML 内容）选项 <a href="#extract-html-content-options" id="extract-html-content-options"></a>

还可配置以下选项：

* **Trim Values**（裁剪值）：开启时，移除值开头和结尾的所有空格及换行；关闭时保留。
* **Clean Up Text**（清理文本）：开启时，移除开头、结尾的空白和换行，并将连续多个空白合并为一个空格；关闭时保留原样。

## Convert to HTML Table（转换为 HTML 表格） <a href="#convert-to-html-table" id="convert-to-html-table"></a>

此操作接收其他节点的数据，没有参数，包含以下选项：

* **Capitalize Headers**（标题首字母大写）：开启时，将表头首字母转为大写；关闭时不转换。
* **Custom Styling**（自定义样式）：开启时使用自定义样式，关闭时不使用。
* **Caption**（表格标题）：输入要添加到表格的标题。
* **Table Attributes**（表格属性）：应用到 `<table>` 的属性，例如样式。
* **Header Attributes**（表头属性）：应用到表头 `<th>` 的属性。
* **Row Attributes**（行属性）：应用到表格行 `<tr>` 的属性。
* **Cell Attributes**（单元格属性）：应用到单元格 `<td>` 的属性。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 HTML 集成模板](https://n8n.io/integrations/html)，或[搜索所有模板](https://n8n.io/workflows/)
