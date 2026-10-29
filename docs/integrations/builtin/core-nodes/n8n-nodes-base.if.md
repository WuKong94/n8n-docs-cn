---
title: If（条件判断）
description: 工作流自动化平台 n8n 中的 If（条件判断） 节点文档，包括使用说明和示例链接。
contentType:
- integration
- reference
priority: critical
tags:
- if
- if node
- If
- If node
hide:
- tags
nodeTitle: If（条件判断）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.if.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# If（条件判断） <a href="#if" id="if"></a>

使用 If 节点，根据比较操作按条件对工作流进行分支。

## 添加条件 <a href="#add-conditions" id="add-conditions"></a>

为 If 节点创建比较 **Conditions**（条件）。

- 使用数据类型下拉菜单，选择条件的数据类型和比较操作类型。例如，要筛选某个日期之后的日期，请选择 **Date & Time > is after**（日期和时间 > 晚于）。
- 条件中需要输入的字段和值，取决于所选的数据类型和比较方式。按数据类型列出的完整比较列表，请参阅[可用的数据类型比较](#available-data-type-comparisons)。

选择 **Add condition**（添加条件）创建更多条件。

### 组合条件 <a href="#combining-conditions" id="combining-conditions"></a>

可选择在以下情况下保留数据：

* 满足全部条件：创建两个或更多条件，在条件之间的下拉菜单中选择 **AND**（且）。
* 满足任意条件：创建两个或更多条件，在条件之间的下拉菜单中选择 **OR**（或）。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 If（条件判断） 集成模板](https://n8n.io/integrations/if)，或[搜索所有模板](https://n8n.io/workflows/)

## If 和 Merge 节点的分支执行 <a href="#branch-execution-with-if-and-merge-nodes" id="branch-execution-with-if-and-merge-nodes"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/merge/if-merge-branch-execution.md" %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

使用条件在 n8n 中创建复杂逻辑的更多信息，请参阅[使用条件分支](../../../build/flow-logic/split-with-conditionals.md)。

如果需要两个以上的条件输出，请使用 [Switch 节点](n8n-nodes-base.switch.md)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/data-types.md" %}

