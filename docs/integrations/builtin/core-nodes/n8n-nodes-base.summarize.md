---
title: Summarize（汇总）
description: 工作流自动化平台 n8n 中的 Summarize（汇总） 节点文档，包括使用说明和示例链接。
contentType:
- integration
- reference
priority: high
nodeTitle: Summarize（汇总）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.summarize.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.summarize
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.summarize
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Summarize（汇总） <a href="#summarize" id="summarize"></a>

使用 Summarize 节点聚合数据项，方式类似于 Excel 数据透视表。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

### Fields to Summarize（要汇总的字段） <a href="#fields-to-summarize" id="fields-to-summarize"></a>

使用以下字段，定义如何汇总输入数据。

* **Aggregation**（聚合方式）：选择对指定字段使用的聚合方法，可选：
    * **Append**（追加）：追加。
        * 选择此项后，还需决定是否 **Include Empty Values**（包含空值）。
    * **Average**（平均值）：计算输入数据的数值平均值。
    * **Concatenate**（串联）：将输入数据中的值串联起来。
        * 选择此项后，还需决定是否 **Include Empty Values**（包含空值）。
        * **Separator**（分隔符）：选择串联值之间插入的分隔符。
    * **Count**（计数）：统计输入数据中的值的总数。
    * **Count Unique**（唯一值计数）：统计输入数据中的唯一值数量。
    * **Max**（最大值）：查找输入数据中的最大数值。
    * **Min**（最小值）：查找输入数据中的最小数值。
    * **Sum**（求和）：将输入数据中的数值相加。
* **Field**（字段）：输入要执行聚合的字段名称。

### Fields to Split By（分组字段） <a href="#fields-to-split-by" id="fields-to-split-by"></a>

输入用于拆分汇总结果的输入字段名称，类似于 group by 语句，从而按其他字段的值分别生成汇总。

例如，输入数据包含 `Sales Rep` 和 `Deal Amount` 列，并且要对 `Deal Amount` 字段执行 **Sum**（求和），就可以按 `Sales Rep` 分组，得到每位销售代表的 **Sum** 总计。

输入多个分组字段时，请以逗号分隔。

## 节点选项 <a href="#node-options" id="node-options"></a>

### Continue if Field Not Found（未找到字段时继续） <a href="#continue-if-field-not-found" id="continue-if-field-not-found"></a>

默认情况下，如果所有数据项都没有某个 **Field to Summarize**（要汇总的字段），节点会抛出错误。开启此选项则继续执行并返回一个空数据项；关闭则保留默认报错行为。

### Disable Dot Notation（禁用点表示法） <a href="#disable-dot-notation" id="disable-dot-notation"></a>

默认情况下，n8n 启用点表示法，以 `parent.child` 格式引用子字段。开启此选项可禁用点表示法，关闭则继续使用。

### Output Format（输出格式） <a href="#output-format" id="output-format"></a>

选择输出格式。使用 **Fields to Split By**（分组字段）时，建议配置此选项。

* **Each Split in a Separate Item**（每组一个独立数据项）：为每个拆分结果生成独立的输出数据项。
* **All Splits in a Single Item**（所有分组放入一个数据项）：生成单个数据项，列出各拆分字段。

## 忽略缺少有效分组字段的数据项 <a href="#ignore-items-without-valid-fields-to-group-by" id="ignore-items-without-valid-fields-to-group-by"></a>

设置是否忽略不包含 **Fields to Split By**（分组字段）的输入数据项，开启时忽略，关闭时不忽略。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Summarize（汇总） 集成模板](https://n8n.io/integrations/summarize)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/data-transformation-actions/data-section-link.md" %}
