---
contentType: reference
nodeTitle: execution
originalFilePath: code/cookbook/builtin/execution.md
originalUrl: https://docs.n8n.io/code/cookbook/builtin/execution
url: https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/execution
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# `execution` <a href="#execution" id="execution"></a>

## `execution.id` <a href="#executionid" id="executionid"></a>

包含当前工作流执行的唯一 ID。

{% tabs %}
{% tab title="JavaScript" %}
```js
let executionId = $execution.id;
```
{% endtab %}

{% tab title="Python" %}
```python
executionId = _execution.id
```
{% endtab %}
{% endtabs %}

## `execution.resumeUrl` <a href="#executionresumeurl" id="executionresumeurl"></a>

用于恢复[等待中](../../../../integrations/builtin/core-nodes/n8n-nodes-base.wait.md)工作流的 Webhook URL。

更多信息请参阅 [Wait > On webhook call（Webhook 调用时）](../../../../integrations/builtin/core-nodes/n8n-nodes-base.wait.md#on-webhook-call)文档。

工作流包含 Wait 节点和等待 Webhook 响应的节点时，可以使用 `execution.resumeUrl`。

## `execution.customData` <a href="#executioncustomdata" id="executioncustomdata"></a>

仅适用于 Code 节点。

{% tabs %}
{% tab title="JavaScript" %}
```js
// Set a single piece of custom execution data
$execution.customData.set("key", "value");

// Set the custom execution data object
$execution.customData.setAll({"key1": "value1", "key2": "value2"})

// Access the current state of the object during the execution
var customData = $execution.customData.getAll()

// Access a specific value set during this execution
var customData = $execution.customData.get("key")
```
{% endtab %}

{% tab title="Python" %}
```python
# Set a single piece of custom execution data
_execution.customData.set("key", "value");

# Set the custom execution data object
_execution.customData.setAll({"key1": "value1", "key2": "value2"})

# Access the current state of the object during the execution
customData = _execution.customData.getAll()

# Access a specific value set during this execution
customData = _execution.customData.get("key")
```
{% endtab %}
{% endtabs %}

更多信息请参阅[自定义执行数据](../../../understand-workflows/understand-executions/customize-executions-data.md)。

---

## 相关资源 <a id="related-resources"></a>

* [内置方法和变量示例](./)


