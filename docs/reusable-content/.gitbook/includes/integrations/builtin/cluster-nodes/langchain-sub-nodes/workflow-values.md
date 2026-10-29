---
title: 工作流值
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

设置要传给所调用工作流的值。

这些值会出现在所调用工作流的触发器节点输出中，可在该工作流的表达式中访问。例如：

* **Workflow Values**（工作流值）中有一个 **Name**（名称）为 `myCustomValue` 的值。
* 工作流使用 Execute Sub-workflow Trigger（执行子工作流触发器）作为触发器。

访问 `myCustomValue` 的值所用的表达式为 `{{ $('Execute Sub-workflow Trigger').item.json.myCustomValue }}`。
