---
contentType: explanation
nodeTitle: 数据项如何在工作流中关联
originalFilePath: data/data-mapping/data-item-linking/item-linking-concepts.md
originalUrl: https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-concepts
url: https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 数据项如何在工作流中关联 <a href="#how-items-link-through-workflows" id="how-items-link-through-workflows"></a>

节点创建的每个输出数据项，都包含关联元数据，指向用于生成它的一个或多个输入数据项。这形成一条可向前回溯的数据项链，便于访问早期数据项。节点拆分或合并数据时，这一机制可能较难理解。开发自己的编程式节点，或在某些场景中使用 Code 节点时，需要了解数据项关联。

本文概述这一功能。使用细节见：

* [节点开发者的数据项关联说明](item-linking-for-node-creators.md)：开发节点时如何处理关联。
* [在 Code 节点中保留关联](preserving-linking-in-the-code-node.md)：Code 节点中的处理方法。
* [数据项关联错误](item-linking-errors.md)：编辑器中可能遇到的错误。

## n8n 的自动数据项关联 <a href="#n8ns-automatic-item-linking" id="n8ns-automatic-item-linking"></a>

节点未自行控制输入和输出数据项的关联时，n8n 会尝试自动推断：

* 单个输入、单个输出：输出关联到该输入。
* 单个输入、多个输出：所有输出都关联到该输入。
* 多个输入和输出：
	* 保留输入数据项但更改顺序，或删除部分、保留其他数据项时，n8n 能自动添加正确的关联信息。
	* 输入和输出数量相同时，n8n 按顺序关联，即 output-1 对应 input-1，output-2 对应 input-2，依此类推。
	* 数量不同，或创建了完全新的数据项时，n8n 无法自动关联。

如果 n8n 无法自动关联，节点也未处理关联，就会显示错误。更多信息请参阅[数据项关联错误](item-linking-errors.md)。

## 数据项关联示例 <a href="#item-linking-example" id="item-linking-example"></a>

![示意图展示多个数据项通过关联链回溯工作流的路径](../../../.gitbook/assets/item-linking-multiple-lines.png)

此示例中，即使数据项顺序改变，n8n 仍能将某个节点的数据项关联回更早的多个步骤。这意味着，按字母顺序排列电影的节点，仍可以访问获取著名演员节点中关联数据项的信息。

根据使用界面、表达式还是 Code 节点，访问关联数据项的方法有所不同。请查看以下资源：

* [在界面中映射](../use-the-ui-mapper.md)
* [在 Code 节点中保留关联](preserving-linking-in-the-code-node.md)
* [数据项关联错误](item-linking-errors.md)

## 相关资源 <a id="related-resources"></a>

* [关联数据项](./)
* [在 Code 节点中访问关联的数据项](accessing-linked-items-in-the-code-node.md)
* [在 Code 节点中保留关联](preserving-linking-in-the-code-node.md)
* [数据项关联错误](item-linking-errors.md)
* [节点开发者的数据项关联说明](item-linking-for-node-creators.md)




