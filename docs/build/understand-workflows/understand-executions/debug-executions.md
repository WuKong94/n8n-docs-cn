---
contentType: howto
title: 调试并重新运行以往执行
description: 如何将执行数据复制到当前工作流，以调试以往执行。
nodeTitle: 调试执行
originalFilePath: workflows/executions/debug.md
originalUrl: https://docs.n8n.io/workflows/executions/debug
url: https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 调试并重新运行以往执行 <a href="#debug-and-re-run-past-executions" id="debug-and-re-run-past-executions"></a>

{% hint style="info" %}
**功能可用范围**

以下套餐支持调试并重新运行以往执行：

- **n8n Cloud：** 所有套餐
- **自托管：** 已注册的 Community、Business、Enterprise
{% endhint %}

可以将以往执行的数据加载到当前工作流中。这有助于调试失败的生产执行：查看失败的执行，修改工作流以修复问题，再使用之前的执行数据重新运行。

## 加载数据 <a href="#load-data" id="load-data"></a>

加载以往执行数据的步骤如下：

1. 在工作流中选择 **Executions（执行）** 标签页，查看 **Executions** 列表。
1. 选择要调试的执行。n8n 会根据工作流执行成功或失败显示不同选项：
	* 对于失败的执行：选择 **Debug in editor（在编辑器中调试）**。
	* 对于成功的执行：选择 **Copy to editor（复制到编辑器）**。
1. n8n 会将执行数据复制到当前工作流，并在工作流的第一个节点中[固定数据](../../work-with-data/pin-and-mock-data.md)。

{% hint style="info" %}
**检查保存了哪些执行**

**Executions（执行）** 列表中可用的执行记录取决于[工作流设置](../../manage-workflows/configure-workflow-settings.md)。
{% endhint %}

## 相关资源 <a id="related-resources"></a>

* [理解执行](./)
* [手动执行、部分执行与生产执行](types-of-executions.md)
* [查看所有执行](view-all-executions.md)
* [查看单个工作流的执行](view-executions-for-a-single-workflow.md)
* [自定义执行数据](customize-executions-data.md)
* [流式传输实时响应](stream-real-time-responses.md)
* [脏节点](understand-dirty-nodes.md)
