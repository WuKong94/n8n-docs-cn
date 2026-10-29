---
nodeTitle: PrevNodeData（前一节点数据）
originalFilePath: data/expression-reference/prevnodedata.md
originalUrl: https://docs.n8n.io/data/expression-reference/prevnodedata
url: https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/prevnodedata
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# PrevNodeData（前一节点数据） <a href="#prevnodedata" id="prevnodedata"></a>

## **`name`** <a href="#name" id="name"></a>

**说明：** 提供当前输入的节点名称。

如果当前节点有多个输入连接点（例如 Merge 节点），始终使用第一个输入连接点。

**语法：** **`name`**

**返回值：** String（字符串）

**来源：** n8n 自定义功能

## **`outputIndex`** <a href="#outputindex" id="outputindex"></a>

**说明：** 提供当前输入的输出连接点索引。前一个节点有多个输出时（例如 If 或 Switch 节点），可以使用此值。

如果当前节点有多个输入连接点（例如 Merge 节点），始终使用第一个输入连接点。

**语法：** **`outputIndex`**

**返回值：** Number（数字）

**来源：** n8n 自定义功能

## **`runIndex`** <a href="#runindex" id="runindex"></a>

**说明：** 前一个节点生成当前输入时的运行次数索引。

如果当前节点有多个输入连接点（例如 Merge 节点），始终使用第一个输入连接点。

**语法：** **`runIndex`**

**返回值：** Number（数字）

**来源：** n8n 自定义功能


## 相关资源 <a id="related-resources"></a>

* [表达式参考](./)
