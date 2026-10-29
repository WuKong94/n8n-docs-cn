---
description: n8n 提供这些方法，方便在表达式中执行常见任务。
contentType: reference
hide:
- toc
nodeTitle: HTTP 节点
originalFilePath: code/builtin/http-node-variables.md
originalUrl: https://docs.n8n.io/code/builtin/http-node-variables
url: https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/http-node
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# HTTP 节点变量 <a href="#http-node-variables" id="http-node-variables"></a>

分页时用于处理 HTTP 节点请求和响应的变量。

HTTP 节点的使用方法，包括分页配置，请参阅 [HTTP Request](../../../integrations/builtin/core-nodes/n8n-nodes-base.httprequest/README.md)。

分页配置示例请参阅 [HTTP Request 节点实用示例：分页](../cookbook/http-request-node/pagination.md)。

{% hint style="info" %}
**仅适用于 HTTP 节点**

这些变量供 HTTP 节点的表达式使用，不能用于其他节点。
{% endhint %}
{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/http/pagination-variables.md" %}

## 相关资源 <a id="related-resources"></a>

* [使用内置快捷方法](../use-built-in-shortcuts.md)
* [JMESPath](jmespath.md)
* [LangChain Code 节点](langchain-code-node.md)
* [n8n 元数据](n8n-metadata.md)
