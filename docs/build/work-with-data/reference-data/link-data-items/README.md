---
contentType: overview
nodeTitle: 关联数据项
originalFilePath: data/data-mapping/data-item-linking/index.md
originalUrl: https://docs.n8n.io/data/data-mapping/data-item-linking
url: https://docs.n8n.io/build/work-with-data/reference-data/link-data-items
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 关联数据项 <a href="#linking-data-items" id="linking-data-items"></a>

数据项是一条独立数据。节点接收一个或多个数据项，执行操作后输出新数据项。每个数据项都会关联回前面节点中生成它的数据项。

通常，此机制会自动正常工作。以下场景需要深入理解：

* 使用 Code 节点，对输入和输出数据执行复杂操作。
* 开发编程式节点。

本节提供：

* [数据项关联概念](how-items-link-through-workflows.md)概述。
* [节点开发者的数据项关联说明](item-linking-for-node-creators.md)。
* 为需要[沿数据路径](preserving-linking-in-the-code-node.md)读取前面节点数据项，以及在 Code 节点中关联数据项的用户提供指导。
* [错误](item-linking-errors.md)排查指南。

## 本节内容 <a id="in-this-section"></a>

* [数据项如何在工作流中关联](how-items-link-through-workflows.md)：数据项关联的概念概述。
* [在 Code 节点中访问关联的数据项](accessing-linked-items-in-the-code-node.md)：使用 `itemMatching()` 读取关联数据项。
* [在 Code 节点中保留关联](preserving-linking-in-the-code-node.md)：编写自定义代码时保持数据项关联完整。
* [数据项关联错误](item-linking-errors.md)：排查常见关联错误。
* [节点开发者的数据项关联说明](item-linking-for-node-creators.md)：节点开发者需要了解的关联机制。

## 相关资源 <a id="related-resources"></a>

* [引用数据](../)
* [使用界面映射器](../use-the-ui-mapper.md)
* [引用前面的节点](../reference-previous-nodes.md)


