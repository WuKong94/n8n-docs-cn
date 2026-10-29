---
description: n8n 内置的自定义方法和变量。
contentType: overview
nodeTitle: 使用内置快捷方法
originalFilePath: code/builtin/overview.md
originalUrl: https://docs.n8n.io/code/builtin/overview
url: https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 内置方法和变量 <a href="#built-in-methods-and-variables" id="built-in-methods-and-variables"></a>

n8n 提供内置方法和变量，用于处理数据和访问 n8n 数据。本节列出表达式[^1]中可用的方法和变量，并提供简要说明。

{% hint style="warning" %}
**在表达式编辑器和 Code 节点中的可用性**

本参考中的方法和变量并非全部可用于 [Code 节点](cookbook/code-node/README.md)。Code 节点使用原生 Luxon 运行普通 JavaScript，而不是 n8n 表达式引擎。因此，参考页中标记为 **Source: Custom n8n functionality（来源：n8n 自定义功能）** 的条目（例如 [`DateTime.format()`](../work-with-data/transform-data/expression-reference/datetime.md#datetimeformat)）属于 n8n 专用扩展，在 Code 节点中可能不存在，或行为不同。

如果 Code 节点中的代码抛出 `... is not a function`，或没有报错却返回错误结果：

* 检查该方法的参考条目是否标记为 **Custom n8n functionality（n8n 自定义功能）**。
* 寻找原生 Luxon 或 JavaScript 的等效方法。例如，使用 [`toFormat()`](https://moment.github.io/luxon/api-docs/index.html#datetimetoformat)，代替 n8n 专用的 `DateTime.format()`。
* 注意两边都有但签名不同的方法，例如 `DateTime.plus()`/`minus()`：n8n 表达式版本接受 `(amount, unit)`，原生 Luxon 版本则只接受单个类似 Duration 的对象（`{ days: 7 }`）。在 Code 节点中使用表达式版本的签名不会报错，但也不会得到预期结果。

所有数据转换函数，即本节列出的顶层辅助函数（例如 `$if()` 或 `$jmespath()`），都仅适用于表达式编辑器，不能用于 Code 节点。
{% endhint %}

[实用示例](README.md)包含常见任务的示例，其中也有一些[仅适用于 Code 节点](cookbook/code-node/README.md)的函数。

## 本节内容 <a id="in-this-section"></a>

* [JMESPath](use-built-in-shortcuts/jmespath.md)：在 n8n 中使用 JMESPath 库。
* [HTTP 节点](use-built-in-shortcuts/http-node.md)：HTTP Request 节点表达式中常见任务的方法。
* [LangChain Code 节点](use-built-in-shortcuts/langchain-code-node.md)：LangChain Code 节点中常见任务的方法。
* [n8n 元数据](use-built-in-shortcuts/n8n-metadata.md)：用于处理 n8n 元数据的方法。

## 相关资源 <a id="related-resources"></a>

* [在 n8n 中编写代码](./)
* [使用 Code 节点](using-the-code-node.md)
* [获取 AI 编程帮助](get-coding-help-from-ai.md)
* [定义自定义变量](define-custom-variables.md)
* [实用示例](cookbook/README.md)

[^1]: 在 n8n 中，表达式通过执行 JavaScript 代码动态填充节点参数。你可以使用 n8n 表达式语法，根据前面节点、其他工作流或 n8n 环境中的数据定义值，而不是提供静态值。