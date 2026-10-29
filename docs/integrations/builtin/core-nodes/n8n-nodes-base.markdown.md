---
title: Markdown
description: 了解 n8n 工作流自动化平台中的 Markdown 节点，包括用法说明和示例链接。
contentType:
- integration
- reference
priority: medium
nodeTitle: Markdown
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.markdown.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.markdown
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.markdown
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Markdown <a href="#markdown" id="markdown"></a>

Markdown 节点用于在 Markdown 与 HTML 格式之间相互转换。

## 操作 <a href="#operations" id="operations"></a>

此节点通过 **Modes**（模式）选择操作：

* **Markdown to HTML**：使用此模式将 Markdown 转换为 HTML。
* **HTML to Markdown**：使用此模式将 HTML 转换为 Markdown。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **HTML** 或 **Markdown**：输入要转换的数据。字段名称会根据所选的 **Mode**（模式）变化。
* **Destination Key**（目标键）：输入要存放输出的字段。嵌套字段可使用点表示法，例如 `level1.level2.newKey`。

## 节点选项 <a href="#node-options" id="node-options"></a>

节点的 **Options**（选项）取决于所选的 **Mode**（模式）。

{% hint style="info" %}
**试用各项选项**

部分选项彼此依赖或相互影响。建议实际试用，确认效果符合预期。
{% endhint %}

### Markdown to HTML 选项 <a href="#markdown-to-html-options" id="markdown-to-html-options"></a>

| 选项 | 说明 | 默认值 |
| ------ | ----------- | ------- |
| **Add Blank To Links**（在新窗口打开链接） | 开启时在新窗口打开链接，关闭时不启用此行为。 | 关闭 |
| **Automatic Linking To URLs**（自动将 URL 转为链接） | 开启时，n8n 会将识别为 URL 的字符串转换为链接；关闭时不自动转换。 | 关闭 |
| **Backslash Escapes HTML Tags**（用反斜杠转义 HTML 标签） | 开启时，允许用反斜杠转义 HTML 标签；关闭时不允许。开启后，n8n 会转义 `<` 或 `>`，前提是其前面带有 `\`。例如，`\<div\>` 会显示为 `&lt;div&gt;`。 | 关闭 |
| **Complete HTML Document**（完整 HTML 文档） | 开启时输出完整 HTML 文档，关闭时输出 HTML 片段。完整文档包含 `<DOCTYPE HTML>` 声明、`<html>` 和 `<body>` 标签，以及 `<head>` 元素。 | 关闭 |
| **Customized Header ID**（自定义标题 ID） | 开启时支持自定义标题 ID，关闭时不支持。开启后，可在标题文本后添加 `{header ID here}` 来指定标题 ID。 | 关闭 |
| **Emoji Support**（表情符号支持） | 开启时支持表情符号，关闭时不支持。 | 关闭 |
| **Encode Emails**（编码电子邮件地址） | 开启时，将 ASCII 字符组成的电子邮件地址转换为对应的十进制字符实体；关闭时不转换。 | 开启 |
| **Exclude Trailing Punctuation From URLs**（排除 URL 末尾标点） | 开启时，从自动链接的 URL 中排除末尾标点，关闭时不排除。与 **Automatic Linking To URLs**（自动将 URL 转为链接）配合使用。 | 关闭 |
| **GitHub Code Blocks**（GitHub 代码块） | 开启时启用 GitHub 风格 Markdown 代码块，关闭时不启用。 | 开启 |
| **GitHub Compatible Header IDs**（兼容 GitHub 的标题 ID） | 开启时，按 GitHub 风格 Markdown 规则生成标题 ID；关闭时不采用该规则。此规则用 `-` 替代空格，并移除非字母数字字符。 | 关闭 |
| **GitHub Mention Link**（GitHub 提及链接） | 更改 **GitHub Mentions**（GitHub 用户提及）所使用的链接。 | 关闭 |
| **GitHub Mentions**（GitHub 用户提及） | 开启时支持通过 `@` 提及 GitHub 用户，关闭时不支持。开启后，n8n 会将 `@name` 替换为 `https://github.com/name`。 | 关闭 |
| **GitHub Task Lists**（GitHub 任务列表） | 开启时支持 GitHub 风格 Markdown 任务列表，关闭时不支持。 | 关闭 |
| **Header Level Start**（标题起始级别） | 数字，用于设置标题的起始级别。例如，设为 `2` 后，n8n 会将 `#` 视为 `<h2>`，将 `##` 视为 `<h3>`，依此类推。 | 1 |
| **Mandatory Space Before Header**（标题前必须有空格） | 开启时要求 `#` 与标题文本之间有空格，关闭时不要求。开启后，n8n 会将 `##Some header text` 原样显示为文本，而不会转为标题元素。 | 关闭 |
| **Middle Word Asterisks**（词中星号） | 关闭时，将单词中的星号视为 Markdown 语法；开启时，将其原样显示为星号。 | 关闭 |
| **Middle Word Underscores**（词中下划线） | 关闭时，将单词中的下划线视为 Markdown 语法；开启时，将其原样显示为下划线。 | 关闭 |
| **No Header ID**（不生成标题 ID） | 开启时，禁用自动生成标题 ID。 | 关闭 |
| **Parse Image Dimensions**（解析图片尺寸） | 开启时，支持在 Markdown 语法中设置图片的最大尺寸。 | 关闭 |
| **Prefix Header ID**（标题 ID 前缀） | 定义要添加到标题 ID 的前缀。 | 无 |
| **Raw Header ID**（原始标题 ID） | 开启时，从标题 ID（包括前缀）中移除空格、`'` 和 `"`，并替换为 `-`；关闭时不执行此处理。 | 关闭 |
| **Raw Prefix Header ID**（原始标题 ID 前缀） | 开启时，阻止 n8n 修改标题前缀；关闭时不阻止。 | 关闭 |
| **Simple Line Breaks**（简单换行） | 开启时，行尾无需两个空格即可换行；关闭时不启用此行为。 | 关闭 |
| **Smart Indentation Fix**（智能修复缩进） | 开启时，尝试智能修复缩进代码块中与 ES6 模板字符串有关的缩进问题；关闭时不修复。 | 关闭 |
| **Spaces Indented Sublists**（子列表缩进空格） | 开启时，移除子列表必须缩进四个空格的要求；关闭时保留该要求。 | 关闭 |
| **Split Adjacent Blockquotes**（拆分相邻引用块） | 开启时拆分相邻引用块，关闭时不拆分。未开启时，即使不同行上的引用（以行首 `>` 表示）之间有空行，n8n 仍将其视为同一个引用块。 | 关闭 |
| **Strikethrough**（删除线） | 开启时支持删除线语法，关闭时不支持。开启后，可在单词或短语两侧加上 `~~`，呈现 ~~删除线~~ 效果。 | 关闭 |
| **Tables Header ID**（表头 ID） | 开启时，为表头标签添加 ID；关闭时不添加。 | 关闭 |
| **Tables Support**（表格支持） | 开启时支持表格，关闭时不支持。 | 关闭 |

### HTML to Markdown 选项 <a href="#html-to-markdown-options" id="html-to-markdown-options"></a>

| 选项 | 说明 | 默认值 |
| ------ | ----------- | ------- |
| **Bullet Marker**（无序列表标记） | 指定用于无序列表的字符。 | * |
| **Code Block Fence**（代码块围栏） | 指定用于代码块的字符。 | ``` |
| **Emphasis Delimiter**（强调分隔符） | 指定用于 `<em>` 的字符。 | _ |
| **Global Escape Pattern**（全局转义模式） | 覆盖默认的字符转义设置。可以考虑改用 Text Replacement Pattern（文本替换模式）。 | 无 |
| **Ignored Elements**（忽略元素） | 忽略指定的 HTML 元素及其子元素。 | 无 |
| **Keep Images With Data**（保留带数据的图片） | 开启时保留带数据的图片，关闭时不保留。支持最大 1MB 的文件。 | 关闭 |
| **Line Start Escape Pattern**（行首转义模式） | 覆盖默认的字符转义设置。可以考虑改用 Text Replacement Pattern（文本替换模式）。 | 无 |
| **Max Consecutive New Lines**（最大连续换行数） | 数字，用于指定允许的最大连续换行数。 | 3 |
| **Place URLs At The Bottom**（将 URL 放在底部） | 开启时，将 URL 放在页面底部，并采用链接引用定义格式；关闭时不启用此行为。 | 关闭 |
| **Strong Delimiter**（加粗分隔符） | 指定用于 `<strong>` 的字符。 | ** |
| **Style For Code Block**（代码块样式） | 指定代码块的样式，可选 **Fence**（围栏）和 **Indented**（缩进）。 | Fence |
| **Text Replacement Pattern**（文本替换模式） | 使用正则表达式定义文本替换模式。 | 无 |
| **Treat As Blocks**（按块处理） | 指定要按块处理的 HTML 元素，即在其前后添加空行。 | 无 |

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Markdown 集成模板](https://n8n.io/integrations/markdown)，或[搜索所有模板](https://n8n.io/workflows/)

## 解析器 <a href="#parsers" id="parsers"></a>

n8n 使用以下解析器：

* 从 HTML 转换为 Markdown：[node-html-markdown](https://www.npmjs.com/package/node-html-markdown)。
* 从 Markdown 转换为 HTML：[Showdown](https://www.npmjs.com/package/showdown)。部分选项可用 [GitHub 风格 Markdown](https://github.github.com/gfm/)语法扩展 Markdown。


