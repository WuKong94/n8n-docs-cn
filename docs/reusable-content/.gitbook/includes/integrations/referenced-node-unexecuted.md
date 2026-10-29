---
title: 引用的节点尚未执行
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


## 引用的节点尚未执行 <a href="#referenced-node-is-unexecuted" id="referenced-node-is-unexecuted"></a>


工作流中的前序节点尚未执行，无法提供当前节点所需的输入时，会出现此错误。

错误全文会按以下格式指出具体哪个节点尚未执行：
```
An expression references the node '<node-name>', but it hasn’t been executed yet. Either change the expression, or re-wire your workflow to make sure that node executes first.
```

排查时，先测试工作流，执行到错误中指出的节点。

对于调用 JavaScript 或其他自定义代码的节点，请在使用值之前，通过以下调用判断节点是否已执行：

```js
$("<node-name>").isExecuted
```
