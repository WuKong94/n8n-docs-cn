---
description: 使用 Code 节点为工作流执行添加自定义数据，之后可以按这些数据筛选执行。
contentType: howto
nodeTitle: 自定义执行数据
originalFilePath: workflows/executions/custom-executions-data.md
originalUrl: https://docs.n8n.io/workflows/executions/custom-executions-data
url: https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 自定义执行数据 <a href="#custom-executions-data" id="custom-executions-data"></a>

可以通过 Code 节点或 [Execution Data 节点](../../../integrations/builtin/core-nodes/n8n-nodes-base.executiondata.md)为工作流设置自定义数据，n8n 会随每次执行记录这些数据。之后，可以在筛选执行列表时使用这些数据，也可以在工作流中通过 Code 节点获取。

{% include "../../../reusable-content/.gitbook/includes/workflows/executions/custom-execution-data-availability.md" %}

## 使用 Code 节点设置和访问自定义数据 <a href="#set-and-access-custom-data-using-the-code-node" id="set-and-access-custom-data-using-the-code-node"></a>

本节介绍如何通过 Code 节点设置和访问数据。通过 Execution Data 节点设置数据的方法，请参阅 [Execution Data 节点](../../../integrations/builtin/core-nodes/n8n-nodes-base.executiondata.md)。Execution Data 节点不能用于读取自定义数据。

### 设置自定义执行数据 <a href="#set-custom-executions-data" id="set-custom-executions-data"></a>

设置单条附加数据：

{% tabs %}
{% tab title="JavaScript" %}
```js
$execution.customData.set("key", "value");
```
{% endtab %}

{% tab title="Python" %}
```python
_execution.customData.set("key", "value");
```
{% endtab %}
{% endtabs %}

设置全部附加数据。这会覆盖本次执行的整个自定义数据对象：

{% tabs %}
{% tab title="JavaScript" %}
```js
$execution.customData.setAll({"key1": "value1", "key2": "value2"})
```
{% endtab %}

{% tab title="Python" %}
```python
_execution.customData.setAll({"key1": "value1", "key2": "value2"})
```
{% endtab %}
{% endtabs %}

存在以下限制：

* 必须是字符串
* `key` 最长为 50 个字符
* `value` 最长为 255 个字符
* n8n 最多支持 10 条自定义数据

### 在执行过程中访问自定义数据对象 <a href="#access-the-custom-data-object-during-execution" id="access-the-custom-data-object-during-execution"></a>

执行过程中，可以读取自定义数据对象，或其中某个特定值：


{% tabs %}
{% tab title="JavaScript" %}
```js
// Access the current state of the object during the execution
const customData = $execution.customData.getAll();

// Access a specific value set during this execution
const customData = $execution.customData.get("key");
```
{% endtab %}

{% tab title="Python" %}
```python
# Access the current state of the object during the execution
customData = _execution.customData.getAll();

# Access a specific value set during this execution
customData = _execution.customData.get("key");
```
{% endtab %}
{% endtabs %}

## 相关资源 <a id="related-resources"></a>

* [理解执行](./)
* [手动执行、部分执行与生产执行](types-of-executions.md)
* [查看所有执行](view-all-executions.md)
* [查看单个工作流的执行](view-executions-for-a-single-workflow.md)
* [调试并重新运行以往执行](debug-executions.md)
* [流式传输实时响应](stream-real-time-responses.md)
* [脏节点](understand-dirty-nodes.md)
