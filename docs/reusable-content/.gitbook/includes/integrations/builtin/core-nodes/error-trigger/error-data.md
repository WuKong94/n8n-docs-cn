---
title: 错误触发器的数据
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

Error Trigger 默认收到的错误数据如下：

```json
[
	{
		"execution": {
			"id": "231",
			"url": "https://n8n.example.com/execution/231",
			"retryOf": "34",
			"error": {
				"message": "Example Error Message",
				"stack": "Stacktrace"
			},
			"lastNodeExecuted": "Node With Error",
			"mode": "manual"
		},
		"workflow": {
			"id": "1",
			"name": "Example Workflow"
		}
	}
]

```

除以下字段外，其他信息始终存在：

- `execution.id`：要求执行记录已保存到数据库。如果错误发生在主工作流的触发器节点中，则不会出现此字段，因为工作流尚未执行。
- `execution.url`：要求执行记录已保存到数据库。如果错误发生在主工作流的触发器节点中，则不会出现此字段，因为工作流尚未执行。
- `execution.retryOf`：仅在本次执行是对失败执行的重试时存在。

如果错误由主工作流的触发器节点引起，而不是发生在后续阶段，发送给错误工作流的数据会有所不同。`execution{}` 中的信息会更少，而 `trigger{}` 中的信息会更多：

```json
{
  "trigger": {
    "error": {
      "context": {},
      "name": "WorkflowActivationError",
      "cause": {
        "message": "",
        "stack": ""
      },
      "timestamp": 1654609328787,
      "message": "",
      "node": {
        . . . 
      }
    },
    "mode": "trigger"
  },
  "workflow": {
    "id": "",
    "name": ""
  }
}
```
