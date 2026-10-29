---
title: Evaluation Trigger 节点
description: 了解如何在 n8n 工作流中配置和使用 Evaluation Trigger 节点。
contentType:
- integration
- reference
nodeTitle: Evaluation Trigger 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.evaluationtrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluationtrigger
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluationtrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Evaluation Trigger（评估触发器）节点 <a href="#evaluation-trigger-node" id="evaluation-trigger-node"></a>

配置[评估](../../../build/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test.md)时，使用 Evaluation Trigger 节点验证 AI 工作流的可靠性。评估期间，节点从所选的数据表或 Google Sheets 读取评估数据集，按顺序将数据项逐个送入工作流。

本页介绍 Evaluation Trigger 节点的参数和选项。

{% hint style="info" %}
**Google Sheets 凭据**

Evaluation Trigger 节点使用数据表或 Google Sheets 存储测试数据集。要使用 Google Sheets 作为数据集来源，请配置 [Google Sheets 凭据](../credentials/google/README.md)。
{% endhint %}

## 参数 <a href="#parameters" id="parameters"></a>

- **Source:**（来源）选择要读取的评估数据集位置，默认为 **Data table**（数据表）。

    不同的 **Source**（来源）选项对应不同设置。

    * **Source**（来源）为 **Data table**（数据表）时：
        * **Data table:**（数据表）通过名称或 ID 选择数据表。
        * **Limit Rows**（限制行数）：选择是否限制要处理的数据表行数，默认状态为 `off`（关闭）。
            * **Max Rows to Process**（最多处理行数）：开启 **Limit Rows**（限制行数）时，设置评估期间最多读取和处理的行数，默认值为 10。
            * **Filter Rows:**（筛选行）选择是否筛选要处理的数据表行，默认状态为 `off`（关闭）。
     * **Source**（来源）为 **Google Sheets** 时：
        - **Credential to connect with**（连接凭据）：创建或选择已有的 [Google Sheets 凭据](../credentials/google/README.md)。
        * **Document Containing Dataset**（数据集所在电子表格文档）：选择包含测试数据集工作表的电子表格文档。
            - 选择 **From list**（从列表选择），从下拉列表中选择电子表格标题；选择 **By URL**（按 URL）输入电子表格 URL；或选择 **By ID**（按 ID）输入 `spreadsheetId`。
            - 可以从 Google Sheets URL 中找到 `spreadsheetId`，例如 `https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
        * **Sheet Containing Dataset**（数据集所在工作表）：选择包含测试数据集的工作表。
            - 选择 **From list**（从列表选择），从下拉列表中选择工作表标题；选择 **By URL**（按 URL）输入工作表 URL；选择 **By ID**（按 ID）输入 `sheetId`；或选择 **By Name**（按名称）输入工作表标题。
            - 可以从 Google Sheets URL 中找到 `sheetId`，例如 `https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。
        * **Limit Rows**（限制行数）：选择是否限制要处理的工作表行数。
            * **Max Rows to Process**（最多处理行数）：开启 **Limit Rows**（限制行数）时，设置评估期间最多读取和处理的行数。
        * **Filters:**（筛选条件）根据列值筛选评估数据集。
            * **Column**（列）：选择要用于筛选的工作表列。选择 **From list**（从列表选择）可从下拉列表选择列名，选择 **By ID**（按 ID）可通过[表达式](../../../build/work-with-data/expressions-versus-data-nodes.md)指定 ID。
            * **Value**（值）：要用于筛选的列值。评估仅处理所选列中具有给定值的行。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Evaluation Trigger 节点集成模板](https://n8n.io/integrations/evaluation-trigger)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关 n8n 评估的更多信息，请参阅[评估文档](../../../build/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test.md)。

n8n 提供专门的评估应用节点。更多信息，请参阅 [Evaluation 节点文档](n8n-nodes-base.evaluation.md)。

常见疑问、问题及建议的解决方法，请参阅评估的[技巧与常见问题](../../../build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues.md)。
