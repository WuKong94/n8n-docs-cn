---
title: Filter（筛选）
description: 工作流自动化平台 n8n 中的 Filter（筛选） 节点文档，包括使用说明和示例链接。
contentType:
- integration
- reference
priority: critical
nodeTitle: Filter（筛选）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.filter.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.filter
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.filter
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Filter（筛选） <a href="#filter" id="filter"></a>

按条件筛选数据项。数据项满足条件时，Filter 节点会将其传给输出端连接的下一个节点；不满足条件时，则从输出中排除该数据项。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

创建筛选比较 **Conditions**（条件）以执行筛选。

- 使用数据类型下拉菜单，选择条件的数据类型和比较操作类型。例如，要筛选某个日期之后的日期，请选择 **Date & Time > is after**（日期和时间 > 晚于）。
- 条件中需要输入的字段和值，取决于所选的数据类型和比较方式。按数据类型列出的完整比较列表，请参阅[可用的数据类型比较](#available-data-type-comparisons)。

选择 **Add condition**（添加条件）创建更多条件。

### 组合条件 <a href="#combining-conditions" id="combining-conditions"></a>

可选择在以下情况下保留数据项：

* 满足全部条件：创建两个或更多条件，在条件之间的下拉菜单中选择 **AND**（且）。
* 满足任意条件：创建两个或更多条件，在条件之间的下拉菜单中选择 **OR**（或）。

无法混合使用 AND 和 OR 规则。

## 节点选项 <a href="#node-options" id="node-options"></a>

- **Ignore Case**（忽略大小写）：开启时忽略字母大小写，关闭时区分大小写。
- **Less Strict Type Validation**（较宽松的类型验证）：选择是否让 n8n 根据所选操作符尝试转换值类型，开启时尝试，关闭时不尝试。节点出现“wrong type:”错误时，可开启此项。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Filter（筛选） 集成模板](https://n8n.io/integrations/filter)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/data-types.md" %}
