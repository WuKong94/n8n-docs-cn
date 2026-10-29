---
description: 处理当前节点输入和前面节点输出的方法。
contentType: reference
nodeTitle: 引用前面的节点
originalFilePath: data/data-mapping/referencing-other-nodes.md
originalUrl: https://docs.n8n.io/data/data-mapping/referencing-other-nodes
url: https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 引用前面的节点 <a href="#referencing-previous-nodes" id="referencing-previous-nodes"></a>

在 n8n 中处理数据时，经常需要引用当前节点或工作流前面节点的信息。

## 常见引用方式 <a href="#common-ways-of-referencing" id="common-ways-of-referencing"></a>

最常用的数据访问方法包括：

- **`$json`**：访问当前输入数据项的 JSON 数据
- **`$('<node-name>').item.json`**：访问前面节点中[关联数据项](link-data-items/README.md)的 JSON 数据
- **`$('<node-name>').item.binary`**：访问前面节点中[关联数据项](link-data-items/README.md)的二进制数据，例如文件和图片

## 其他引用方法 <a href="#other-referencing-methods" id="other-referencing-methods"></a>

以下方法可同时用于表达式和 Code 节点：

| 方法 | 说明 |
| ------ | ----------- |
| `$binary` | 访问当前输入数据项的二进制数据 |
| `$input.item` | 当前正在处理的输入数据项 |
| `$('<node-name>').first()` | 获取指定节点的第一个数据项 |
| `$('<node-name>').last()` | 获取指定节点的最后一个数据项 |
| `$('<node-name>').all()` | 获取指定节点的所有数据项 |

## 当前节点输入 <a href="#current-node-input" id="current-node-input"></a>

用于处理当前节点输入的方法。部分方法和变量在 Code 节点中不可用。

{% hint style="info" %}
**Python 支持**

可以在 Code 节点中使用 Python，但表达式不支持 Python。
{% endhint %}
{% tabs %}
{% tab title="JavaScript" %}
| 方法 | 说明 | Code 节点中是否可用 |
| ------ | ----------- | :-------------------------: |
| `$binary` | `$input.item.binary` 的简写，表示节点传入的二进制数据 | ❌ |
| `$input.item` | 当前节点正在处理的输入数据项。配对数据项和关联机制的更多信息，见[数据项关联](link-data-items/README.md)。 | ✅ |
| `$input.all()` | 当前节点的所有输入数据项。 | ✅ |
| `$input.first()` | 当前节点的第一个输入数据项。 | ✅ |
| `$input.last()` | 当前节点的最后一个输入数据项。 | ✅ |
| `$input.params` | 包含前一节点查询设置的对象，例如执行的操作、结果数量上限等。 | ✅ |
| `$json` | `$input.item.json` 的简写，表示节点传入的 JSON 数据。数据项结构见[数据结构](../understand-n8ns-data-structure.md)。 | ✅（逐项运行时） |
| `$input.context.noItemsLeft` | 布尔值，仅适用于 Loop Over Items 节点。提供节点运行状态，可用来判断节点是否仍在处理数据项。 | ✅ |
{% endtab %}

{% tab title="Python" %}
| 方法 | 说明 |
| ------ | ----------- | 
| `_input.item` | 当前节点正在处理的输入数据项。配对数据项和关联机制的更多信息，见[数据项关联](link-data-items/README.md)。 |
| `_input.all()` | 当前节点的所有输入数据项。 |
| `_input.first()` | 当前节点的第一个输入数据项。 |
| `_input.last()` | 当前节点的最后一个输入数据项。 |
| `_input.params` | 包含前一节点查询设置的对象，例如执行的操作、结果数量上限等。 |
| `_json` | `_input.item.json` 的简写，表示节点传入的 JSON 数据。数据项结构见[数据结构](../understand-n8ns-data-structure.md)。将 **Mode（模式）** 设为 **Run Once for Each Item（为每个数据项运行一次）** 时可用。 |
| `_input.context.noItemsLeft` | 布尔值，仅适用于 Loop Over Items 节点。提供节点运行状态，可用来判断节点是否仍在处理数据项。 |
{% endtab %}
{% endtabs %}

## 其他节点的输出 <a href="#output-of-other-nodes" id="output-of-other-nodes"></a>

用于处理其他节点输出的方法。部分方法和变量在 Code 节点中不可用。

| 方法 | 说明 | Code 节点中是否可用 |
| ------ | ----------- | :-------------------------: |
| `$("<node-name>").all(branchIndex?, runIndex?)` | 返回指定节点的所有数据项。未提供 `branchIndex` 时，默认使用连接 `node-name` 与当前表达式或代码所在节点的输出。 | ✅ |
| `$("<node-name>").first(branchIndex?, runIndex?)` | 指定节点输出的第一个数据项。未提供 `branchIndex` 时，默认使用连接 `node-name` 与当前表达式或代码所在节点的输出。 | ✅ |
| `$("<node-name>").last(branchIndex?, runIndex?)` | 指定节点输出的最后一个数据项。未提供 `branchIndex` 时，默认使用连接 `node-name` 与当前表达式或代码所在节点的输出。 | ✅ |
| `$("<node-name>").item` | 关联的数据项，即指定节点中用于生成当前数据项的数据项。关联机制见[数据项关联](link-data-items/README.md)。 | ✅ |
| `$("<node-name>").item.binary` | 关联数据项的二进制数据，以二进制属性名为键（默认为 `data`）。可用属性见 [`BinaryFile`](../transform-data/expression-reference/binaryfile.md)。 | ✅ |
| `$("<node-name>").params` | 包含指定节点查询设置的对象，例如执行的操作、结果数量上限等。 | ✅ |
| `$("<node-name>").context` | 布尔值，仅适用于 Loop Over Items 节点。提供节点运行状态，可用来判断节点是否仍在处理数据项。 | ✅ |
| `$("<node-name>").itemMatching(currentNodeInputIndex)` | 在 Code 节点中需要从输入数据项回溯时，用它代替 `$("<node-name>").item`。 | ✅ |

## 引用前面节点的二进制数据 <a id="reference-binary-data-from-a-previous-node"></a>

`$('<node-name>').item` 返回完整的[关联数据项](link-data-items/README.md)，因此读取二进制数据的方式与读取 JSON 类似：`.item.json` 用于该数据项的 JSON 对象，`.item.binary` 用于文件、图片和其他附件等二进制数据。

一个数据项可以包含多个二进制属性，每个属性都有自己的名称，因此 `.item.binary` 返回这些属性组成的对象，而非单个值。多数节点将二进制数据放在名为 `data` 的属性下，但具体名称取决于上游节点。每个二进制属性都是 `BinaryFile`，包含 `fileName`、`mimeType` 和 `fileExtension` 等字段。

例如，要获取 **HTTP Request** 节点生成的 `data` 二进制属性的文件名：

```js
{{ $('HTTP Request').item.binary.data.fileName }}
```

二进制数据及生成它的节点，详见[二进制数据](../handle-special-data-types/work-with-files-and-images.md)。

## 相关资源 <a id="related-resources"></a>

* [引用数据](./)
* [使用界面映射器](use-the-ui-mapper.md)
* [关联数据项](link-data-items/README.md)
