---
title: Execution Data（执行数据）
description: 工作流自动化平台 n8n 中的 Execution Data（执行数据） 节点文档，包括使用说明和示例链接。
contentType:
- integration
- reference
priority: high
nodeTitle: Execution Data（执行数据）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.executiondata.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executiondata
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executiondata
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Execution Data（执行数据） <a href="#execution-data" id="execution-data"></a>

使用此节点保存工作流执行的元数据。随后可在 **Executions**（执行记录）列表中按这些数据搜索。

工作流执行期间，可使用 Code 节点获取自定义执行数据。更多信息请参阅[自定义执行数据](../../../build/understand-workflows/understand-executions/customize-executions-data.md)。

{% include "../../../reusable-content/.gitbook/includes/workflows/executions/custom-execution-data-availability.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Save Execution Data for Search（保存执行数据以供搜索）

## 要保存的数据 <a href="#data-to-save" id="data-to-save"></a>

为每个要保存的元数据键值对添加一个 **Saved Field**（保存字段）。

## 限制 <a href="#limitations" id="limitations"></a>

Execution Data 节点存储执行元数据时有以下限制：

* `key`：最多 50 个字符。
* `value`：最多 512 个字符。

如果 `key` 或 `value` 超过上述限制，n8n 会将其截断至允许的最大长度，并输出一条日志。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Execution Data（执行数据） 集成模板](https://n8n.io/integrations/execution-data)，或[搜索所有模板](https://n8n.io/workflows/)
