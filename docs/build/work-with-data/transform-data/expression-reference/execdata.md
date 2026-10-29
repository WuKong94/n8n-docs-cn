---
nodeTitle: ExecData（执行数据）
originalFilePath: data/expression-reference/execdata.md
originalUrl: https://docs.n8n.io/data/expression-reference/execdata
url: https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/execdata
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# ExecData（执行数据） <a href="#execdata" id="execdata"></a>

## `$exec`.**`customData`** <a href="#dollarexeccustomdata" id="dollarexeccustomdata"></a>

**说明：** 设置和获取自定义执行数据，例如用于筛选执行记录。也可以通过 Execution Data 节点完成这些操作。<a href="../../../understand-workflows/understand-executions/customize-executions-data.md">更多信息</a>

**语法：** `$exec`.`$exec`.**`customData`**

**返回值：** CustomData

**来源：** n8n 自定义功能

## `$exec`.**`id`** <a href="#dollarexecid" id="dollarexecid"></a>

**说明：** 当前工作流执行的 ID。

**语法：** `$exec`.`$exec`.**`id`**

**返回值：** String（字符串）

**来源：** n8n 自定义功能

## `$exec`.**`mode`** <a href="#dollarexecmode" id="dollarexecmode"></a>

**说明：** 可能为以下三个值之一：<code>test</code>（通过点击 n8n 中的按钮触发执行）、<code>production</code>（自动触发执行）。运行工作流测试时，使用 <code>evaluation</code>。

**语法：** `$exec`.`$exec`.**`mode`**

**返回值：** String（字符串）

**来源：** n8n 自定义功能

## `$exec`.**`resumeFormUrl`** <a href="#dollarexecresumeformurl" id="dollarexecresumeformurl"></a>

**说明：** 访问 <a href="../../../../integrations/builtin/core-nodes/n8n-nodes-base.wait.md">Wait 节点</a>所生成表单的 URL。

**语法：** `$exec`.`$exec`.**`resumeFormUrl`**

**返回值：** String（字符串）

**来源：** n8n 自定义功能

## `$exec`.**`resumeUrl`** <a href="#dollarexecresumeurl" id="dollarexecresumeurl"></a>

**说明：** 用于恢复在 <a href="../../../../integrations/builtin/core-nodes/n8n-nodes-base.wait.md">Wait 节点</a>处等待的工作流的 Webhook URL。

**语法：** `$exec`.`$exec`.**`resumeUrl`**

**返回值：** String（字符串）

**来源：** n8n 自定义功能


## 相关资源 <a id="related-resources"></a>

* [表达式参考](./)
