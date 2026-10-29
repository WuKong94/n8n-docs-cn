---
title: XML
description: 了解 n8n 工作流自动化平台中的 XML 节点，包括用法说明和示例链接。
contentType:
- integration
- reference
priority: medium
nodeTitle: XML
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.xml.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.xml
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.xml
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# XML <a href="#xml" id="xml"></a>

使用 XML 节点，将数据转换为 XML，或将 XML 转换为其他格式。

{% hint style="info" %}
**二进制文件**

如果 XML 存放在二进制文件中，先使用 [Extract from File](n8n-nodes-base.extractfromfile.md) 节点将其转换为文本。
{% endhint %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

- **Mode**（模式）：数据转换的源格式与目标格式。
    - **JSON to XML**：将 JSON 数据转换为 XML。
    - **XML to JSON**：将 XML 数据转换为 JSON。
- **Property Name**（属性名称）：输入包含待转换数据的属性名称。

## 节点选项 <a href="#node-options" id="node-options"></a>

无论选择哪种 **Mode**（模式），均可使用以下选项：

- **Attribute Key**（属性键）：输入用于访问 XML 属性的前缀，默认值为 `$`。
- **Character Key**（字符内容键）：输入用于访问字符内容的前缀，默认值为 `_`。

其他选项均取决于所选的 **Mode**（模式）。

### JSON to XML 选项 <a href="#json-to-xml-options" id="json-to-xml-options"></a>

仅在 **Mode**（模式）选择 **JSON to XML** 时显示以下选项：

- **Allow Surrogate Chars**（允许代理区字符）：开启时允许使用 Unicode 代理区中的字符，关闭时不允许。
- **Cdata**：需要时，开启此选项可使用 `<![CDATA[ ... ]]>` 包装文本节点，而不是转义文本；关闭时不启用此行为。
    * 开启此选项后，若无需包装，仍不会添加 `<![CDATA[ ... ]]>`。
- **Headless**（无头部）：开启时省略 XML 头部，关闭时包含头部。
- **Root Name**（根元素名称）：输入要使用的根元素名称。

### XML to JSON 选项 <a href="#xml-to-json-options" id="xml-to-json-options"></a>

仅在 **Mode**（模式）选择 **XML to JSON** 时显示以下选项：

- **Explicit Array**（显式数组）：开启时将子节点放入数组；关闭时，仅在存在多个子节点时创建数组。
- **Explicit Root**（显式根节点）：开启时在结果对象中保留根节点，关闭时不保留。
- **Ignore Attributes**（忽略属性）：开启时忽略所有 XML 属性，仅创建文本节点；关闭时不忽略属性。
- **Merge Attributes**（合并属性）：开启时将属性与子元素一起合并为父节点的属性；关闭时，将 XML 属性放在单独的子属性对象中。开启 **Ignore Attributes**（忽略属性）时，此选项被忽略。
- **Normalize**（规范化）：开启时修整文本节点内部的空白，关闭时不作此处理。
- **Normalize Tags**（规范化标签）：开启时将所有标签名转为小写，关闭时保留原样。
- **Trim**（修剪）：开启时去除文本节点首尾的空白，关闭时保留原样。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 XML 集成模板](https://n8n.io/integrations/xml)，或[搜索所有模板](https://n8n.io/workflows/)
