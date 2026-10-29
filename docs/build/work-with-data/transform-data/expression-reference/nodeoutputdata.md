---
nodeTitle: NodeOutputData（节点输出数据）
originalFilePath: data/expression-reference/nodeoutputdata.md
originalUrl: https://docs.n8n.io/data/expression-reference/nodeoutputdata
url: https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# NodeOutputData（节点输出数据） <a href="#nodeoutputdata" id="nodeoutputdata"></a>

## `$()`.**`all()`** <a href="#dollarall" id="dollarall"></a>

**说明：** 返回节点输出数据项组成的数组。

**语法：** `$()`.all(branchIndex?, runIndex?)

**返回值：** Array<Item>

**来源：** n8n 自定义功能

**参数：**

  * `branchIndex`（Number）— 可选 — 要使用的节点输出分支。默认为第一个分支（索引为 0）。
  * `runIndex`（Number）— 可选 — 要使用节点的第几次运行。默认为第一次运行（索引为 0）。

## `$()`.**`first()`** <a href="#dollarfirst" id="dollarfirst"></a>

**说明：** 返回节点输出的第一个数据项。

**语法：** `$()`.first(branchIndex?, runIndex?)

**返回值：** Item（数据项）

**来源：** n8n 自定义功能

**参数：**

  * `branchIndex`（Number）— 可选 — 要使用的节点输出分支。默认为第一个分支（索引为 0）。
  * `runIndex`（Number）— 可选 — 要使用节点的第几次运行。默认为第一次运行（索引为 0）。

## `$()`.**`isExecuted`** <a href="#dollarisexecuted" id="dollarisexecuted"></a>

**说明：** 节点已执行时为 <code>true</code>，否则为 <code>false</code>。

**语法：** `$()`.`$()`.**`isExecuted`**

**返回值：** Boolean（布尔值）

**来源：** n8n 自定义功能

## `$()`.**`item`** <a href="#dollaritem" id="dollaritem"></a>

**说明：** 返回匹配的数据项，也就是用于生成当前节点中当前数据项的那个数据项。<a href="../../reference-data/link-data-items/README.md">更多信息</a>

**语法：** `$()`.`$()`.**`item`**

**返回值：** Item（数据项）

**来源：** n8n 自定义功能

## `$()`.**`itemMatching()`** <a href="#dollaritemmatching" id="dollaritemmatching"></a>

**说明：** 返回匹配的数据项，也就是用于生成当前节点中指定索引处数据项的那个数据项。<a href="../../reference-data/link-data-items/README.md">更多信息</a>

**语法：** `$()`.itemMatching(currentItemIndex?)

**返回值：** Item（数据项）

**来源：** n8n 自定义功能

**参数：**

  * `currentItemIndex`（Number）— 要匹配的当前节点中数据项的索引。

## `$()`.**`last()`** <a href="#dollarlast" id="dollarlast"></a>

**说明：** 返回节点输出的最后一个数据项。

**语法：** `$()`.last(branchIndex?, runIndex?)

**返回值：** Item（数据项）

**来源：** n8n 自定义功能

**参数：**

  * `branchIndex`（Number）— 可选 — 要使用的节点输出分支。默认为第一个分支（索引为 0）。
  * `runIndex`（Number）— 可选 — 要使用节点的第几次运行。默认为第一次运行（索引为 0）。

## `$()`.**`params`** <a href="#dollarparams" id="dollarparams"></a>

**说明：** 指定节点的配置，即在节点界面中填写的参数，例如要执行的操作。

**语法：** `$()`.`$()`.**`params`**

**返回值：** NodeParams

**来源：** n8n 自定义功能


## 相关资源 <a id="related-resources"></a>

* [表达式参考](./)
