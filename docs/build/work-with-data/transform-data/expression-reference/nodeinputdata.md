---
nodeTitle: NodeInputData（节点输入数据）
originalFilePath: data/expression-reference/nodeinputdata.md
originalUrl: https://docs.n8n.io/data/expression-reference/nodeinputdata
url: https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# NodeInputData（节点输入数据） <a href="#nodeinputdata" id="nodeinputdata"></a>

## `$input`.**`all()`** <a href="#dollarinputall" id="dollarinputall"></a>

**说明：** 返回当前节点输入数据项组成的数组。

**语法：** `$input`.all(branchIndex?, runIndex?)

**返回值：** Array<Item>

**来源：** n8n 自定义功能

**参数：**

  * `branchIndex`（Number）— 可选 — 要使用的节点输出分支索引。默认为第一个分支（索引为 0）。
  * `runIndex`（Number）— 可选 — 要使用节点的第几次运行。默认为第一次运行（索引为 0）。

## `$input`.**`first()`** <a href="#dollarinputfirst" id="dollarinputfirst"></a>

**说明：** 返回当前节点的第一个输入数据项。

**语法：** `$input`.first(branchIndex?, runIndex?)

**返回值：** Item（数据项）

**来源：** n8n 自定义功能

**参数：**

  * `branchIndex`（Number）— 可选 — 要使用的节点输出分支索引。默认为第一个分支（索引为 0）。
  * `runIndex`（Number）— 可选 — 要使用节点的第几次运行。默认为第一次运行（索引为 0）。

## `$input`.**`item`** <a href="#dollarinputitem" id="dollarinputitem"></a>

**说明：** 返回当前正在处理的输入数据项。

**语法：** `$input`.`$input`.**`item`**

**返回值：** Item（数据项）

**来源：** n8n 自定义功能

## `$input`.**`last()`** <a href="#dollarinputlast" id="dollarinputlast"></a>

**说明：** 返回当前节点的最后一个输入数据项。

**语法：** `$input`.last(branchIndex?, runIndex?)

**返回值：** Item（数据项）

**来源：** n8n 自定义功能

**参数：**

  * `branchIndex`（Number）— 可选 — 要使用的节点输出分支索引。默认为第一个分支（索引为 0）。
  * `runIndex`（Number）— 可选 — 要使用节点的第几次运行。默认为第一次运行（索引为 0）。

## `$input`.**`params`** <a href="#dollarinputparams" id="dollarinputparams"></a>

**说明：** 当前节点的配置，即配置节点时填写的参数，例如要执行的操作。

**语法：** `$input`.`$input`.**`params`**

**返回值：** NodeParams

**来源：** n8n 自定义功能


## 相关资源 <a id="related-resources"></a>

* [表达式参考](./)
