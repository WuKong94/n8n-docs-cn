---
title: 子工作流的数据传递
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

例如，假设 **Workflow A（工作流 A）** 中有一个 Execute Sub-workflow 节点，该节点调用另一个名为 **Workflow B（工作流 B）** 的工作流：

1. Execute Sub-workflow 节点将数据传递给 **Workflow B** 的 Execute Sub-workflow Trigger 节点（在画布上名为“When executed by another node”）。
2. **Workflow B** 的最后一个节点将数据返回给 **Workflow A** 中的 Execute Sub-workflow 节点。
