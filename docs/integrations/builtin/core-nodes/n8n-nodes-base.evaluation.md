---
title: Evaluation 节点
description: 了解 n8n 中 Evaluation 节点的用法，并查看相关示例。
contentType:
- integration
- reference
nodeTitle: Evaluation 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.evaluation.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluation
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluation
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Evaluation（评估）节点 <a href="#evaluation-node" id="evaluation-node"></a>

Evaluation 节点执行与[评估](../../../build/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test.md)有关的各类操作，用于验证 AI 工作流的可靠性。

可在以下场景使用 Evaluation 节点：

* 根据工作流是否正在进行评估，有条件地执行逻辑。
* 将评估结果写回数据表或 Google Sheets 数据集。
* 将评估表现的评分指标记录到 n8n 的评估标签页。

{% hint style="info" %}
**Google Sheets 凭据**

Evaluation 节点的 **Set Outputs**（设置输出）操作会将评估结果记录到数据表或 Google Sheets。要使用 Google Sheets 作为记录位置，请配置 [Google Sheets 凭据](../credentials/google/README.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

Evaluation 节点提供以下操作：

* [**Set Outputs**](#set-outputs)（设置输出）：将评估结果写回数据表或 Google Sheets 数据集。
* [**Set Metrics**](#set-metrics)（设置指标）：将评估表现的评分指标记录到 n8n 的 **Evaluations**（评估）标签页。
* [**Check If Evaluating**](#check-if-evaluating)（检查是否正在评估）：根据当前执行是否为评估，将工作流执行逻辑分支。

可用参数和选项取决于所选操作。

### Set Outputs（设置输出） <a href="#set-outputs" id="set-outputs"></a>

**Set Outputs**（设置输出）操作有以下参数：

- **Source:**（来源）选择评估结果的输出位置，默认为 **Data table**（数据表）。

   不同的 **Source**（来源）选项对应不同设置。

    * **Source**（来源）为 **Data table**（数据表）时：
        * **Data table:**（数据表）通过名称或 ID 选择数据表。
    * **Source**（来源）为 **Google Sheets** 时：
        * **Credential to connect with**（连接凭据）：创建或选择已有的 [Google Sheets 凭据](../credentials/google/README.md)。
        * **Document Containing Dataset**（数据集所在电子表格文档）：选择要写入评估结果的电子表格文档，通常与 [Evaluation Trigger](n8n-nodes-base.evaluationtrigger.md) 节点中选择的文档相同。
        * 选择 **From list**（从列表选择），从下拉列表中选择电子表格标题；选择 **By URL**（按 URL）输入电子表格 URL；或选择 **By ID**（按 ID）输入 `spreadsheetId`。
            * 可以从 Google Sheets URL 中找到 `spreadsheetId`，例如 `https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
        * **Sheet Containing Dataset**（数据集所在工作表）：选择要写入评估结果的工作表，通常与 [Evaluation Trigger](n8n-nodes-base.evaluationtrigger.md) 节点中选择的工作表相同。
            * 选择 **From list**（从列表选择），从下拉列表中选择工作表标题；选择 **By URL**（按 URL）输入工作表 URL；选择 **By ID**（按 ID）输入 `sheetId`；或选择 **By Name**（按名称）输入工作表标题。
            * 可以从 Google Sheets URL 中找到 `sheetId`，例如 `https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。

在 **Outputs**（输出）部分定义要写入数据表或 Google Sheets 的数据项。每个输出需设置：

* **Name**（名称）：用于写入评估结果的数据表或 Google Sheets 列名。
* **Value**（值）：要写入数据表或 Google Sheets 的值。

### Set Metrics（设置指标） <a href="#set-metrics" id="set-metrics"></a>

**Set Metrics**（设置指标）操作包含 **Metrics to Return**（返回的指标）部分，用于定义要记录和跟踪的评估指标。可在工作流的 **Evaluations**（评估）标签页查看结果。

为每个要记录的指标设置以下内容：

* **Name**（名称）：指标名称。
* **Value**（值）：要记录的数值。运行一次评估后，可以将前置节点的值拖放到此处。指标值必须为数字。

### Check If Evaluating（检查是否正在评估） <a href="#check-if-evaluating" id="check-if-evaluating"></a>

**Check If Evaluating**（检查是否正在评估）操作没有参数，通过分支输出连接口，根据当前执行是否为评估来有条件地执行逻辑。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Evaluation 节点集成模板](https://n8n.io/integrations/evaluation)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关 n8n 评估的更多信息，请参阅[评估文档](../../../build/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test.md)。

n8n 提供专门的评估触发器节点。更多信息，请参阅 [Evaluation Trigger 节点文档](n8n-nodes-base.evaluationtrigger.md)。

常见疑问、问题及建议的解决方法，请参阅评估的[技巧与常见问题](../../../build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues.md)。
