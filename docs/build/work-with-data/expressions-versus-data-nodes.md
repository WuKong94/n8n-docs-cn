---
description: 比较表达式、Code 节点、AI Transform 节点和数据转换节点在 n8n 中的数据处理方式。
contentType: howto
nodeTitle: 表达式与数据节点
originalFilePath: data/expressions.md
originalUrl: https://docs.n8n.io/data/expressions
url: https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 表达式与数据节点 <a href="#expressions-versus-data-nodes" id="expressions-versus-data-nodes"></a>

n8n 提供多种数据处理和转换方式。了解各自适用场景，有助于构建高效工作流。

| 方式 | 适用需求 | 示例 | 可用环境 |
|---|---|---|---|
| 表达式 | 使用已有数据设置单个参数值 | 获取 `{{$json.city}}`、格式化日期、简单计算 | Cloud 和自托管 |
| Code 节点 | 编写完整 JavaScript/Python 进行复杂转换 | 重组数据、遍历数据项、使用外部库 | Cloud 和自托管 |
| AI Transform 节点 | 根据自然语言生成转换代码 | `Group by user and sum totals`（按用户分组并求和）、`categorize by sentiment`（按情感分类） | 仅 Cloud |
| 其他数据转换节点 | 通过可视化界面完成常见操作 | 聚合数据项、拆分数组、排序、去重 | Cloud 和自托管 |

### 表达式 <a href="#expressions" id="expressions"></a>

表达式是使用 n8n 的 `{{ ... }}` 语法，直接写在节点参数中的小段类似 JavaScript 的代码。它可以根据前面节点的数据、工作流元数据或环境变量动态设置参数值。

{% hint style="info" %}
**尽可能使用表达式**

表达式能即时预览计算结果，因此适用时应优先使用。
{% endhint %}

**表达式的适用场景：**

* 从前面节点的数据中提取值，例如 `{{$json.body.city}}`。
* 直接在字段中进行轻量转换或计算。
* 避免添加额外节点，让逻辑靠近要设置的参数。

### Code 节点 <a href="#code-node" id="code-node"></a>

[Code 节点](../../integrations/builtin/core-nodes/n8n-nodes-base.code/README.md)专门用于编写 JavaScript 或 Python，并作为工作流步骤运行。可以访问前面节点传入的数据，通过添加、删除或更新数据项进行处理，也可以创建所需的自定义函数，并通过 `$` 语法使用 n8n 内置方法和变量。

**Code 节点的适用场景：**

* 需要比表达式更复杂的逻辑或转换，例如重组数组和对象、聚合或拆分数据项，以及自定义算法。
* 希望一次转换多个数据项。
* 希望使用 Promise、`console.log`，或在自托管环境中使用外部 npm 模块。

### AI Transform 节点 <a href="#ai-transform-node" id="ai-transform-node"></a>

此节点根据简短自然语言提示词生成代码片段，能够理解上下文、工作流节点和数据类型。生成的代码在节点中为只读，可复制到 Code 节点编辑。

**AI Transform 节点的适用场景：**

* 清楚需要什么转换，但不想手写代码。
* 希望 AI 起草转换逻辑，再直接在节点中运行，或复制到 Code 节点进一步定制。

### 其他数据转换节点 <a href="#other-data-transformation-nodes" id="other-data-transformation-nodes"></a>

n8n 提供一系列数据转换节点：

* [Aggregate](../../integrations/builtin/core-nodes/n8n-nodes-base.aggregate.md)：将多个独立数据项或其中部分内容聚合为单个数据项。
* [Limit](../../integrations/builtin/core-nodes/n8n-nodes-base.limit.md)：移除超过指定最大数量的数据项。
* [Remove Duplicates](../../integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/README.md)：识别并删除所有字段或部分字段相同的数据项。
* [Sort](../../integrations/builtin/core-nodes/n8n-nodes-base.sort.md)：按所需顺序整理列表，或随机选择数据。
* [Split Out](../../integrations/builtin/core-nodes/n8n-nodes-base.splitout.md)：将包含列表的单个数据项拆分为多个数据项。
* [Summarize](../../integrations/builtin/core-nodes/n8n-nodes-base.summarize.md)：聚合数据项，类似 Excel 数据透视表。

**数据转换节点的适用场景：**

* 需要的操作与某个专用转换节点的用途相符。
* 希望使用带有引导界面的无代码方案。
* 更喜欢可视化构建，而不是编写表达式或代码。

更多引用、转换和组织数据的方式，请参阅[处理数据](README.md)。

## 相关资源 <a id="related-resources"></a>

* [处理数据](./)
* [理解 n8n 的数据结构](understand-n8ns-data-structure.md)
* [引用数据](reference-data/README.md)
* [转换数据](transform-data/README.md)
* [过滤不需要的数据](filter-out-unwanted-data.md)
* [固定和模拟数据](pin-and-mock-data.md)
* [处理特殊数据类型](handle-special-data-types/README.md)
* [数据表](data-tables.md)

