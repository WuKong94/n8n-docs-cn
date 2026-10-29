---
description: 了解如何使用 n8n 的 Track Time Saved 节点，记录工作流每次执行所节省的时间。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Track Time Saved（记录节省时间）节点 <a id="track-time-saved-node"></a>

使用 Track Time Saved 节点，根据执行实际经过的路径，记录工作流节省的分钟数。n8n 会累加一次执行中所有已运行的 Track Time Saved 节点，并在 [Insights](../../../administer/observe-and-log/track-usage-with-insights.md) 中报告总量。

工作流不同路径节省的时间不同时，使用此节点。如果每次执行节省的时间相同，直接在工作流中设置固定值即可，无需此节点。

{% hint style="info" %}
**先将工作流设为 Dynamic（动态）**

只有工作流的 **Estimated time saved**（预计节省时间）设为 **Dynamic**（动态）时，此节点才会计入统计。请参阅[设置工作流节省的时间](../../../administer/observe-and-log/track-usage-with-insights.md#setting-the-time-saved-by-a-workflow)。
{% endhint %}

## 节点参数 <a id="node-parameters"></a>

* **Calculation Mode**（计算模式）：选择 n8n 如何统计分钟数：
  * **Once For All Items**（所有数据项只计算一次）：无论多少数据项到达此节点，都只计一次 **Minutes Saved**（节省的分钟数）。
  * **Per Item**（按数据项计算）：将 **Minutes Saved**（节省的分钟数）乘以输入数据项数量。
* **Minutes Saved**（节省的分钟数）：此步骤节省的分钟数，必须为大于或等于零的整数分钟，默认为 `0`。

节点原样传递所有输入数据项，并将节省时间记录为执行元数据。

## n8n 如何计算总量 <a id="how-n8n-calculates-the-total"></a>

n8n 会累加一次执行中所有实际运行的 Track Time Saved 节点。未运行分支上的节点不计入统计，因此总量能够反映实际经过的路径。

同一工作流可以放置多个 Track Time Saved 节点，n8n 会将它们在本次执行中的值相加。

## n8n 何时统计一次执行 <a id="when-n8n-counts-an-execution"></a>

n8n 仅为**成功的生产执行**记录节省时间。无论节点中设置什么值，以下执行都不计入统计：

* **手动执行。** 从编辑器运行工作流不计入统计，只有生产执行才计入。
* **失败的执行。** 执行最终发生错误时，n8n 不为其记录任何节省时间，即使部分 Track Time Saved 节点已经运行。
* **子工作流执行。** Insights 会跳过此类执行，因此子工作流中的 Track Time Saved 节点不会给子工作流或调用它的父工作流增加统计值。n8n 会将分钟数记录在子工作流自身的执行上，父工作流的总量不会累加这些值。要统计子工作流节省的时间，应将 Track Time Saved 节点放在父工作流中，并置于 Execute Sub-workflow 节点之后。
* **错误工作流执行。** n8n 将其视为运维工作，而不是产出性工作。
* **聊天执行。** 通过 n8n Chat Hub 发送的消息不计入统计，即使执行成功也不计入。
* **智能体执行。** 由 n8n Agent 发起的执行不计入统计，即使成功也不计入。

如果 **Estimated time saved**（预计节省时间）采用 **Fixed**（固定）而不是 **Dynamic**（动态），n8n 会完全忽略这些节点，改用固定值。

## 相关资源 <a id="related-resources"></a>

* [使用 Insights 跟踪用量](../../../administer/observe-and-log/track-usage-with-insights.md)：Insights 仪表盘及工作流级别的节省时间设置。
* [工作流设置](../../../build/manage-workflows/configure-workflow-settings.md)：设置 **Estimated time saved**（预计节省时间）的位置。
