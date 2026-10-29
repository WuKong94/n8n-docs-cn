---
title: Remove Duplicates（去重）节点
description: 了解 n8n 中 Remove Duplicates 节点的用法，包括当前输入去重、跨执行去重及相关示例。
contentType:
- integration
- reference
priority: medium
nodeTitle: n8n-nodes-base.removeduplicates
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Remove Duplicates（去重）节点 <a href="#remove-duplicates-node" id="remove-duplicates-node"></a>

使用 Remove Duplicates 节点识别并删除符合以下条件的数据项：

* 在单次执行中，所有字段或部分字段相同。
* 与先前执行中出现的数据项相同，或其值、日期未超过先前执行中的数据项。

当数据可能重复时，这个节点很有用，例如用户创建多个账户，或客户多次提交同一订单。数据集较大时，识别和移除这些数据项会更加困难。

通过与先前执行的数据比较，Remove Duplicates 节点可以删除以前已出现过的数据项，也可以确保新数据项的日期晚于先前日期，或其值高于先前值。

{% hint style="info" %}
**1.64.0 中的重大变更**

n8n 团队在 n8n 1.64.0 中全面改进了此节点。本文档介绍新版节点。如果使用较早的 n8n 版本，请参阅[此文档的旧版本](https://github.com/n8n-io/n8n-docs/blob/7a66308290e6e5b104fcb82a3beafa0d6987df36/docs/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates.md)。
{% endhint %}

## 操作模式 <a href="#operation-modes" id="operation-modes"></a>

Remove Duplicates 节点的行为取决于 **operation**（操作）参数：

* **[Remove Items Repeated Within Current Input](#remove-items-repeated-within-current-input)**（移除当前输入内的重复项）：比较所有字段或部分字段，识别并移除当前输入中的重复数据项。
* **[Remove Items Processed in Previous Executions](#remove-items-processed-in-previous-executions)**（移除先前执行已处理的数据项）：将当前输入与先前执行的数据项比较，移除重复项。
* **[Clear Deduplication History](#clear-deduplication-history)**（清除去重历史）：清除记录的先前执行数据项。

### Remove Items Repeated Within Current Input（移除当前输入内的重复项） <a href="#remove-items-repeated-within-current-input" id="remove-items-repeated-within-current-input"></a>

将“Operations”字段设为 **Remove Items Repeated Within Current Input**（移除当前输入内的重复项）时，Remove Duplicates 节点会识别并移除当前输入中的重复数据项，可以比较所有字段，也可以只比较部分字段。

#### 移除当前输入内的重复项：参数 <a href="#remove-items-repeated-within-current-input-parameters" id="remove-items-repeated-within-current-input-parameters"></a>

使用 **Remove Items Repeated Within Current Input** 操作时，可配置以下参数：

* **Compare**（比较）：选择 n8n 应比较哪些输入字段，判断数据项是否相同。可选：
	* **All Fields**（所有字段）：比较输入数据的所有字段。
	* **All Fields Except**（除指定字段外的所有字段）：输入要从比较中排除的字段，多个值用逗号分隔。
	* **Selected Fields**（选定字段）：输入要纳入比较的字段，多个值用逗号分隔。

#### 移除当前输入内的重复项：选项 <a href="#remove-items-repeated-within-current-input-options" id="remove-items-repeated-within-current-input-options"></a>

比较类型选择 **All Fields Except** 或 **Selected Fields** 时，可以添加以下选项：

* **Disable Dot Notation**（禁用点号表示法）：关闭时，使用 `parent.child` 格式的点号表示法引用子字段；开启时，不使用这种表示法。
* **Remove Other Fields**（移除其他字段）：开启时，移除未参与比较的字段；关闭时，保留这些字段。

### Remove Items Processed in Previous Executions（移除先前执行已处理的数据项） <a href="#remove-items-processed-in-previous-executions" id="remove-items-processed-in-previous-executions"></a>

将“Operation”字段设为 **Remove Items Processed in Previous Executions** 时，Remove Duplicates 节点会将当前输入与先前执行的数据项比较。

#### 移除先前执行已处理的数据项：参数 <a href="#remove-items-processed-in-previous-executions-parameters" id="remove-items-processed-in-previous-executions-parameters"></a>

使用 **Remove Items Processed in Previous Executions** 操作时，可配置以下参数：

* **Keep Items Where**（保留条件）：选择 n8n 判断应保留哪些数据项的方式。可选：
	* **Value Is New**（值是新的）：如果数据项的值与先前执行中的值相同，n8n 会移除该项。
	* **Value Is Higher than Any Previous Value**（值高于所有先前值）：如果当前值未高于先前的所有值，n8n 会移除该项。
	* **Value Is a Date Later than Any Previous Date**（日期晚于所有先前日期）：如果当前日期未晚于先前的所有日期，n8n 会移除该日期数据项。

* **Value to Dedupe On**（去重依据值）：要比较的一个或多个输入字段。所需的具体格式由 **Keep Items Where** 的选择决定：
	* 使用 **Value Is New** 时，必须是具有唯一 ID 的输入字段或字段组合。
	* 使用 **Value Is Higher than Any Previous Value** 时，必须是具有递增值的输入字段或字段组合。
	* 使用 **Value Is a Date Later than Any Previous Date** 时，必须是包含 ISO 格式日期值的输入字段。

#### 移除先前执行已处理的数据项：选项 <a href="#remove-items-processed-in-previous-executions-options" id="remove-items-processed-in-previous-executions-options"></a>

使用 **Remove Items Processed in Previous Executions** 操作时，可配置以下选项：

* **Scope**（作用域）：设置 n8n 存储和使用去重比较数据的方式。可选：
	* **Node**（节点，默认）：此节点的数据独立于工作流中其他 Remove Duplicates 节点实例存储。使用此作用域时，可以[清除此节点实例的去重历史](#clear-deduplication-history)，而不影响其他节点。
	* **Workflow**（工作流）：在工作流级别存储去重数据，与其他使用“workflow”作用域的 Remove Duplicates 节点共享。使用“node”作用域的其他 Remove Duplicates 节点，其去重数据仍独立管理。

**Keep Items Where** 选择 **Value Is New** 时，还可配置以下选项：

* **History Size**（历史大小）：n8n 为跨执行去重而存储的数据项数量。**Scope** 决定此历史大小是仅针对当前 Remove Duplicates 节点实例，还是与工作流中其他实例共享。默认存储 10,000 个数据项。

### Clear Deduplication History（清除去重历史） <a href="#clear-deduplication-history" id="clear-deduplication-history"></a>

将“Operation”字段设为 **Clear Deduplication History** 时，Remove Duplicates 节点会管理并清除先前执行所存储的数据项。此操作不影响当前输入中的任何数据项，而是管理“Remove Items Processed in Previous Executions”操作使用的数据项数据库。

#### 清除去重历史：参数 <a href="#clear-deduplication-history-parameters" id="clear-deduplication-history-parameters"></a>

使用 **Clear Deduplication History** 操作时，可配置以下参数：

* **Mode**（模式）：选择如何管理数据库中存储的键／值项。可选：
	* **Clean Database**（清理数据库）：删除数据库中存储的全部去重数据，将去重数据库重置为初始状态。

#### 清除去重历史：选项 <a href="#clear-deduplication-history-options" id="clear-deduplication-history-options"></a>

使用 **Clear Deduplication History** 操作时，可配置以下选项：

* **Scope**（作用域）：设置 n8n 管理去重数据库时使用的范围。
	* **Node**（节点，默认）：管理当前 Remove Duplicates 节点实例专用的去重数据库。
	* **Workflow**（工作流）：管理所有使用工作流作用域的 Remove Duplicates 节点实例共享的去重数据库。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

使用 Remove Duplicates 节点的模板及用法示例，请参阅[模板与示例](templates-and-examples.md)。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/data-transformation-actions/data-section-link.md" %}
