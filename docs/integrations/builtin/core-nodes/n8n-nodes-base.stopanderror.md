---
title: Stop And Error（停止并报错）
description: 工作流自动化平台 n8n 中的 Stop And Error（停止并报错） 节点文档，包括使用说明和示例链接。
contentType:
- integration
- reference
priority: high
nodeTitle: Stop And Error（停止并报错）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.stopanderror.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Stop And Error（停止并报错） <a href="#stop-and-error" id="stop-and-error"></a>

使用 Stop And Error 节点显示自定义错误消息、在特定条件下使执行失败，以及向错误工作流发送自定义错误信息。

## 操作 <a href="#operations" id="operations"></a>

* Error Message（错误消息）
* Error Object（错误对象）

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

两种操作都包含 **Error Type**（错误类型）参数，用于选择要抛出的错误类型。可在 **Error Message**（错误消息）和 **Error Object**（错误对象）两种操作间选择。

其他参数取决于所选操作。

### Error Message（错误消息）参数 <a href="#error-message-parameters" id="error-message-parameters"></a>

Error Type（错误类型）设为 Error Message 时，会添加 **Error Message**（错误消息）参数。输入要抛出的消息。

### Error Object（错误对象）参数 <a href="#error-object-parameters" id="error-object-parameters"></a>

Error Type（错误类型）设为 Error Object 时，会添加 **Error Object**（错误对象）参数。输入包含所需错误属性的 JSON 对象。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Stop And Error（停止并报错） 集成模板](https://n8n.io/integrations/stop-and-error)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

可将 Stop And Error 节点与 [Error Trigger（错误触发器）](n8n-nodes-base.errortrigger.md)节点配合使用。

有关错误工作流的更多信息，请参阅 n8n 工作流中的[错误工作流](../../../build/flow-logic/handle-errors-gracefully.md)。

