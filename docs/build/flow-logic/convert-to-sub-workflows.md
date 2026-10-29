---
title: 子工作流转换
description: 选择工作流中的节点，将其转换为子工作流。
contentType: howto
nodeTitle: 转换为子工作流
originalFilePath: workflows/subworkflow-conversion.md
originalUrl: https://docs.n8n.io/workflows/subworkflow-conversion
url: https://docs.n8n.io/build/flow-logic/convert-to-sub-workflows
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 子工作流转换 <a href="#sub-workflow-conversion" id="sub-workflow-conversion"></a>

{% hint style="info" %}
**功能可用范围**

从 n8n 1.97.0 起提供子工作流转换功能。
{% endhint %}

使用子工作流转换，将工作流重构为可复用的部分，作为[流程逻辑](./)的一部分。引用其他节点的表达式会自动更新，并作为参数添加到 [Execute Workflow Trigger](../../integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger.md) 节点中。

有关这一概念的概述，请参阅[子工作流](break-workflows-into-smaller-parts.md)。

## 选择用于子工作流的节点 <a href="#selecting-nodes-for-a-sub-workflow" id="selecting-nodes-for-a-sub-workflow"></a>

要将工作流的一部分转为子工作流，必须在原工作流中选择要转换的节点。

选择一组符合条件的节点即可。所选节点必须连续，并且最多通过一个起始节点和一个结束节点与工作流其余部分连接。所选节点必须满足以下条件：

- 不得包含触发器节点。
- 所选节点中，只有一个节点可以接收来自所选范围*之外*节点的连接。
	- 该节点可以有多条传入连接，但只能有一个输入*分支*（因此不能是 [Merge 节点](../../integrations/builtin/core-nodes/n8n-nodes-base.merge.md)等节点）。
	- 该节点不能接收来自所选范围内其他节点的连接。
- 所选节点中，只有一个节点可以向所选范围*之外*的节点发出连接。
	- 该节点可以有多条传出连接，但只能有一个输出分支（因此不能是 [If 节点](../../integrations/builtin/core-nodes/n8n-nodes-base.if.md)等节点）。
	- 该节点不能向所选范围内的其他节点发出连接。
- 必须选中输入节点与输出节点之间的所有节点。

## 如何将工作流的一部分转换为子工作流 <a href="#how-to-convert-part-of-a-workflow-to-a-sub-workflow" id="how-to-convert-part-of-a-workflow-to-a-sub-workflow"></a>

在画布上选择所需节点。右键点击画布背景，选择 **Convert to sub-workflow（转换为子工作流）**。

## 注意事项 <a href="#things-to-keep-in-mind" id="things-to-keep-in-mind"></a>

大多数子工作流转换都能顺利完成，但仍需注意以下限制：

* **必须手动设置输入和输出的类型约束**：默认情况下，子工作流的输入和输出允许所有类型。可以在子工作流的 [Execute Sub-workflow Trigger 节点](../../integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger.md)和 [Edit Fields (set) 节点](../../integrations/builtin/core-nodes/n8n-nodes-base.set.md)中设置预期类型（后者标记为 **Return**，仅在子工作流有输出时添加）。
* **对 AI 节点的支持有限**：处理 AI 工具等子节点时，必须选中所有这些子节点；转换前还可能需要复制与其他 AI 智能体共用的节点。
- **使用 v1 执行顺序：** 无论父工作流如何设置，新工作流都使用 [`v1` 执行顺序](understand-execution-order.md)；可以在设置中将其改回。
* **使用 `first()`、`last()` 和 `all()` 等访问函数时需格外注意**：使用这些函数的表达式不一定能直接适用于子工作流上下文。n8n 可能会转换表达式以尽量保留其功能，但你仍应检查它们在新上下文中是否按预期工作。<br>

	<div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>子节点参数后缀</strong></p><p>n8n 会为这些函数访问的变量名添加 <code>_firstItem</code>、<code>_lastItem</code> 和 <code>_allItems</code> 等后缀。这有助于保留原始表达式的信息，因为子工作流上下文中的数据项顺序可能不同。</p></div>


* **`itemMatching` 函数需要固定索引**：使用 [`itemMatching` 函数](../work-with-data/reference-data/reference-previous-nodes.md)时，索引值不能使用表达式，必须传入固定数字。

## 相关资源 <a id="related-resources"></a>

* [流程逻辑](./)
* [按条件分支](split-with-conditionals.md)
* [合并数据](merge-data.md)
* [循环](loop.md)
* [等待](wait.md)
* [理解执行顺序](understand-execution-order.md)
* [将工作流拆分为更小的部分](break-workflows-into-smaller-parts.md)
* [妥善处理错误](handle-errors-gracefully.md)

