---
contentType: overview
nodeTitle: 引用数据
originalFilePath: data/data-mapping/index.md
originalUrl: https://docs.n8n.io/data/data-mapping
url: https://docs.n8n.io/build/work-with-data/reference-data
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 引用数据 <a href="#referencing-data" id="referencing-data"></a>

引用数据（也称数据映射）是指访问工作流前面节点的信息。这样可以将早期步骤的输出用于后续节点输入，构建数据经过多项操作的动态工作流。

引用数据不会修改数据，只是指向已有值，以便在节点参数、表达式或自定义代码中使用。

如果需要修改引用的数据，请参阅[转换数据](../transform-data/approaches-for-transforming-data.md)。

## 如何引用数据 <a href="#how-to-reference-data" id="how-to-reference-data"></a>

引用数据主要通过[表达式](../expressions-versus-data-nodes.md#expressions)完成。可以在参数字段中输入表达式，或从界面的 Input（输入）面板拖入字段。表达式会通过[数据项关联](link-data-items/README.md)自动确定应使用哪个数据项。

## 本节内容 <a id="in-this-section"></a>

* [使用界面映射器](use-the-ui-mapper.md)：在编辑器中拖放字段，引用数据。
* [引用前面的节点](reference-previous-nodes.md)：处理当前节点输入和前面节点输出的方法。
* [关联数据项](link-data-items/README.md)：数据项如何关联回生成它们的数据项。

## 相关资源 <a id="related-resources"></a>

* [处理数据](../)
* [理解 n8n 的数据结构](../understand-n8ns-data-structure.md)
* [表达式与数据节点](../expressions-versus-data-nodes.md)
* [转换数据](../transform-data/README.md)
* [过滤不需要的数据](../filter-out-unwanted-data.md)
* [固定和模拟数据](../pin-and-mock-data.md)
* [处理特殊数据类型](../handle-special-data-types/README.md)
* [数据表](../data-tables.md)
