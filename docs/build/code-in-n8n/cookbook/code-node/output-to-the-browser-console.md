---
description: 如何使用 console.log() 或 print()。
contentType: howto
nodeTitle: 输出到浏览器控制台
originalFilePath: code/cookbook/code-node/console-log.md
originalUrl: https://docs.n8n.io/code/cookbook/code-node/console-log
url: https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/output-to-the-browser-console
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 在 Code 节点中使用 `console.log()` 或 `print()` 输出到浏览器控制台 <a href="#output-to-the-browser-console-with-consolelog-or-print-in-the-code-node" id="output-to-the-browser-console-with-consolelog-or-print-in-the-code-node"></a>

编写和调试代码时，可以在 Code 节点中使用 `console.log()` 或 `print()` 辅助排查。

打开浏览器控制台的方法，请参阅 [Balsamiq 的指南](https://balsamiq.com/support/faqs/browserconsole/)。

## console.log（JavaScript） <a href="#consolelog-javascript" id="consolelog-javascript"></a>

`console.log()` 的技术信息请参阅 [MDN 开发者文档](https://developer.mozilla.org/en-US/docs/Web/API/Console/log)。

例如，将以下代码复制到 Code 节点，打开控制台并运行节点：

```js
let a = "apple";
console.log(a);
```

## print（Python） <a href="#print-python" id="print-python"></a>

`print()` 的技术信息请参阅 [Real Python 指南](https://realpython.com/python-print/)。

例如，将 Code 节点的 **Language（语言）** 设为 **Python**，将以下代码复制到节点，打开控制台并运行节点：

```python
a = "apple"
print(a)
```

### 打印节点数据 <a href="#printing-node-data" id="printing-node-data"></a>

`_items` 和 `_item` 是标准 Python 对象，可以直接打印：

```python
print(_items)
```

{% hint style="info" %}
**`type()` 不可用**

Python Code 节点默认禁止部分内置函数，包括 `type()`。完整列表及自托管时的修改方式，请参阅[任务运行器环境变量](../../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/task-runners.md)。
{% endhint %}

## 相关资源 <a id="related-resources"></a>

* [Code 节点实用示例](./)
* [获取前一节点返回的数据项数量](get-number-of-items-returned-by-last-node.md)
* [获取二进制数据缓冲区](get-the-binary-data-buffer.md)








