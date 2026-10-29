---
title: 编程式 execute() 方法
description: 介绍节点基础文件中编程式 execute() 方法的参考文档。
contentType: reference
nodeTitle: 编程式 execute 方法
originalFilePath: integrations/creating-nodes/build/reference/node-base-files/programmatic-style-execute-method.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/reference/node-base-files/programmatic-style-execute-method
url: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 编程式 execute() 方法 <a href="#programmatic-style-execute-method" id="programmatic-style-execute-method"></a>

声明式与编程式的主要区别，在于如何处理传入数据和构建 API 请求。编程式需要 `execute()` 方法，读取传入数据和参数后构建请求；声明式则通过 `routing` 键处理请求，该键位于 `operations` 对象中。

`execute()` 方法创建并返回 `INodeExecutionData` 的实例。

{% hint style="warning" %}
**配对数据项**

返回的数据中必须包含输入数据项与输出数据项的配对信息。更多信息请参阅[配对数据项](../item-linking.md)。
{% endhint %}

## 相关资源 <a id="related-resources"></a>

* [基础文件](./)
* [结构](structure.md)
* [标准参数](standard-parameters.md)
* [声明式参数](declarative-style-parameters.md)
* [编程式参数](programmatic-style-parameters.md)
