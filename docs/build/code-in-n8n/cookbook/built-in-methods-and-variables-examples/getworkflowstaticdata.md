---
tags:
- static data
- global variables
hide:
- tags
contentType: reference
nodeTitle: getWorkflowStaticData
originalFilePath: code/cookbook/builtin/get-workflow-static-data.md
originalUrl: https://docs.n8n.io/code/cookbook/builtin/get-workflow-static-data
url: https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/getworkflowstaticdata
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# `getWorkflowStaticData(type)` <a href="#getworkflowstaticdatatype" id="getworkflowstaticdatatype"></a>

访问工作流静态数据。

{% hint style="info" %}
**考虑使用数据表**

要在多次执行之间持久保存数据，可以考虑[数据表](../../../work-with-data/data-tables.md)。它们适用于测试执行，也不需要 Code 节点。请参阅[改用数据表](#use-a-data-table-instead)。

静态数据是实验功能：

- 测试工作流时，静态数据不可用。必须发布工作流，并通过触发器[^1]或 Webhook 调用，才能保存静态数据。
- 高频执行工作流时，此功能可能不可靠。
{% endhint %}

可以直接在工作流中保存数据，但数据量应较小。

例如，可以保存从
RSS 订阅源或数据库中处理的最后一个数据项的时间戳。此方法始终返回对象，随后可以读取、删除或
设置对象属性。工作流执行成功时，n8n 会自动检查数据
是否变化，并在必要时保存。

静态数据分为全局和节点两种。全局静态数据在整个
工作流中相同，每个节点都可访问。节点静态数据为各节点独有，只有设置它的节点才能再次读取。

只能在 JavaScript Code 节点中使用静态数据，Python Code 节点不提供此功能。

全局数据示例：

```javascript
// Get the global workflow static data
const workflowStaticData = $getWorkflowStaticData('global');

// Access its data
const lastExecution = workflowStaticData.lastExecution;

// Update its data
workflowStaticData.lastExecution = new Date().getTime();

// Delete data
delete workflowStaticData.lastExecution;
```

节点数据示例：

```javascript
// Get the static data of the node
const nodeStaticData = $getWorkflowStaticData('node');

// Access its data
const lastExecution = nodeStaticData.lastExecution;

// Update its data
nodeStaticData.lastExecution = new Date().getTime();

// Delete data
delete nodeStaticData.lastExecution;
```

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


{% @n8n-blocks/n8n-workflow-demo content="" url="https://api.n8n.io/workflows/templates/2538" %}

## 改用数据表 <a href="#use-a-data-table-instead" id="use-a-data-table-instead"></a>

[数据表](../../../work-with-data/data-tables.md)可以在 n8n 内存储数据，无需 Code 节点，且测试工作流时也会保留数据。

在数据表中保存最后处理数据项等进度标记的步骤如下：

1. 在工作流起点添加 [Data Table 节点](../../../../integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows.md)，通过 **Get row（获取行）** 操作读取保存的值。
2. 在后续节点中通过表达式引用该值，例如 `{{ $('Get row').item.json.lastExecution }}`。
3. 在工作流末尾添加第二个 Data Table 节点，通过 **Upsert row（插入或更新行）** 操作写入新值。

与静态数据不同，不能在表达式或 Code 节点中直接读取数据表值。需要先通过 Data Table 节点读取行，再引用该节点的输出。

[^1]: 触发器节点是一种特殊节点，负责在特定条件满足时启动工作流。所有生产工作流都至少需要一个触发器，以确定何时运行。

## 相关资源 <a id="related-resources"></a>

* [内置方法和变量示例](./)
