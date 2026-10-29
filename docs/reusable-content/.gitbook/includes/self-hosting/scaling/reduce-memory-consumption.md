---
title: reduce-memory-consumption
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

* 将需要处理的数据拆成较小的数据块。例如，每次执行处理 200 行，而不是每次获取 10,000 行。
* 尽可能避免使用 Code 节点。
* 处理较大数据量时，避免手动执行。
* 将工作流拆分为子工作流，并确保每个子工作流仅向父工作流返回有限的数据。

拆分工作流起初可能显得不符合直觉，因为通常至少还需要添加两个节点：用于将数据项分成小批次的 [Loop Over Items（循环遍历数据项）](../../../../../integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md)节点，以及用于启动子工作流的 [Execute Workflow（执行工作流）](../../../../../integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md)节点。

不过，只要由子工作流完成每个批次的主要处理，再仅向主工作流返回较小的结果集，就能减少内存消耗。原因在于，子工作流只在内存中保留当前批次的数据，处理完后便可释放这些内存。
