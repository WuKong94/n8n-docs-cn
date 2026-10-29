---
contentType: explanation
nodeTitle: 数据转换方式
originalFilePath: data/transforming-data.md
originalUrl: https://docs.n8n.io/data/transforming-data
url: https://docs.n8n.io/build/work-with-data/transform-data/approaches-for-transforming-data
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 数据转换方式 <a href="#approaches-for-transforming-data" id="approaches-for-transforming-data"></a>

n8n 中的数据转换，是指在数据流经工作流时对其修改、重组或补充，包括更改格式、筛选或聚合值、添加计算字段，以及转换结构以便与不同节点配合。

n8n 使用预定义的[数据结构](../understand-n8ns-data-structure.md)，让所有节点都能正确处理传入数据。如果数据不符合此结构，或需要根据用途修改，就需要进行转换。

n8n 提供多种数据转换方式：

* [表达式](../expressions-versus-data-nodes.md#expressions)：通过 n8n 表达式语法（`{{ }}`），直接在节点参数中转换数据。
* [Code 节点](../expressions-versus-data-nodes.md#code-node)：编写自定义 JavaScript 或 Python，完成复杂转换。
* [AI Transform 节点](../expressions-versus-data-nodes.md#ai-transform-node)：根据自然语言提示词生成转换代码。
* 高级转换技巧：对于复杂数据处理，n8n 支持：
   * **三元运算符**：直接在表达式中使用条件逻辑（`condition ? valueIfTrue : valueIfFalse`）
   * **链式函数**：组合多个转换函数
   * **复杂表达式**：在表达式语法中使用 JavaScript 方法和运算符
* 用于常见结构转换的专用节点：
   * [Aggregate](../../../integrations/builtin/core-nodes/n8n-nodes-base.aggregate.md)：将独立数据项聚合到一起
   * [Limit](../../../integrations/builtin/core-nodes/n8n-nodes-base.limit.md)：限制数据项数量
   * [Remove Duplicates](../../../integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/README.md)：移除相同数据项
   * [Sort](../../../integrations/builtin/core-nodes/n8n-nodes-base.sort.md)：排序或随机排列数据项
   * [Split Out](../../../integrations/builtin/core-nodes/n8n-nodes-base.splitout.md)：将列表拆分为独立数据项
   * [Summarize](../../../integrations/builtin/core-nodes/n8n-nodes-base.summarize.md)：像 Excel 数据透视表一样聚合数据

这些方式的比较，请参阅[表达式与数据节点](../expressions-versus-data-nodes.md)。

## 相关资源 <a id="related-resources"></a>

* [转换数据](./)
* [使用表达式转换数据](expressions-for-data-transformation.md)
* [表达式参考](expression-reference/README.md)
