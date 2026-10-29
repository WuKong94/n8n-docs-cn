---
description: 在 n8n 中使用 JMESPath 库的方法。
contentType: reference
hide:
- toc
nodeTitle: JMESPath
originalFilePath: code/builtin/jmespath.md
originalUrl: https://docs.n8n.io/code/builtin/jmespath
url: https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/jmespath
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# JMESPath 方法 <a href="#jmespath-method" id="jmespath-method"></a>

这是 n8n 提供的用于操作 [JMESPath](../../work-with-data/handle-special-data-types/query-json-data.md) 库的方法。

{% hint style="info" %}
**仅适用于 JavaScript**

Python Code 节点不提供此方法。在 Python 中查询 JSON，请使用标准 Python。各示例的 Python 版本见[使用 JMESPath 查询 JSON](../../work-with-data/handle-special-data-types/query-json-data.md)。
{% endhint %}

| 方法 | 说明 | Code 节点中是否可用 |
| ------ | ----------- | :-------------------------: |
| `$jmespath()` | 使用 JMESPath 搜索 JSON 对象。 | ✅ |

## 相关资源 <a id="related-resources"></a>

* [使用内置快捷方法](../use-built-in-shortcuts.md)
* [HTTP 节点](http-node.md)
* [LangChain Code 节点](langchain-code-node.md)
* [n8n 元数据](n8n-metadata.md)
