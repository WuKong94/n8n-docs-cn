---
contentType: howto
nodeTitle: 过滤不需要的数据
originalFilePath: data/data-filtering.md
originalUrl: https://docs.n8n.io/data/data-filtering
url: https://docs.n8n.io/build/work-with-data/filter-out-unwanted-data
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 筛选数据 <a href="#filtering-data" id="filtering-data"></a>

在 n8n 中，“筛选”可以指不同操作，取决于目标。本指南同时介绍界面中的可视化筛选，以及工作流执行期间的数据过滤。

## 在界面中可视化筛选数据 <a href="#filter-data-visually-in-the-ui" id="filter-data-visually-in-the-ui"></a>

{% hint style="info" %}
**功能可用范围**

以下套餐支持在节点 **INPUT（输入）** 和 **OUTPUT（输出）** 面板中筛选数据：

- **n8n Cloud：** Pro、Enterprise
- **自托管：** 所有版本
{% endhint %}

在节点 **INPUT（输入）** 和 **OUTPUT（输出）** 面板中搜索、筛选数据，可以检查节点数据并找到特定数据项。

搜索步骤如下：

1. 在节点的 **INPUT（输入）** 或 **OUTPUT（输出）** 面板中，选择 **Search（搜索）** <img src="../.gitbook/assets/search.png" alt="搜索图标" data-size="line">。
1. 输入搜索词。

n8n 会在输入时实时筛选，显示包含搜索词的对象或行。

此筛选仅影响显示，不会修改或删除数据。关闭节点并重新打开后，筛选条件会重置。

## 在工作流执行期间过滤数据 <a href="#filter-data-during-workflow-execution" id="filter-data-during-workflow-execution"></a>

要在工作流中实际移除或筛选数据，可以采用以下方式：

### 过滤整个数据项 <a href="#filter-out-items" id="filter-out-items"></a>

根据条件移除整个数据项时，使用 [Filter 节点](../../integrations/builtin/core-nodes/n8n-nodes-base.filter.md)。它会判断条件，只传递符合要求的数据项。

### 过滤字段 <a href="#filter-out-fields" id="filter-out-fields"></a>

要保留数据项或对象本身、仅移除特定字段，使用 [Edit Fields (Set) 节点](../../integrations/builtin/core-nodes/n8n-nodes-base.set.md)，配置为移除不需要的字段。

### 筛选数组元素 <a href="#filter-array-elements" id="filter-array-elements"></a>

要筛选数据项内部数组的元素，在表达式或 Code 节点中使用 `.filter()` 方法。例如：

```javascript
{{ $json.myArray.filter(item => item.value > 10) }}
```

这样会移除不满足条件的数组元素，同时保留数据项结构。

### 过滤以往执行中出现过的重复数据项 <a href="#filter-out-duplicate-items-from-previous-executions" id="filter-out-duplicate-items-from-previous-executions"></a>

要移除在工作流之前执行中已经出现过的数据项，使用 [Remove Duplicates](../../integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/README.md) 节点。事件多次触发、但只希望处理第一次时，可以采用此方式。

## 相关资源 <a id="related-resources"></a>

* [处理数据](./)
* [理解 n8n 的数据结构](understand-n8ns-data-structure.md)
* [表达式与数据节点](expressions-versus-data-nodes.md)
* [引用数据](reference-data/README.md)
* [转换数据](transform-data/README.md)
* [固定和模拟数据](pin-and-mock-data.md)
* [处理特殊数据类型](handle-special-data-types/README.md)
* [数据表](data-tables.md)
