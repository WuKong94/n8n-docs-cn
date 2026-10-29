---
contentType: overview
nodeTitle: 基础文件
originalFilePath: integrations/creating-nodes/build/reference/node-base-files/index.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/reference/node-base-files
url: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 节点基础文件 <a href="#node-base-file" id="node-base-file"></a>

节点基础文件包含节点的核心代码，每个节点都必须有此文件。根据使用声明式还是编程式构建节点，文件内容有所不同。关于如何选择，请参阅[选择节点构建方式](../../../plan-your-node/choose-a-node-building-style.md)。

这些文档通过简短代码片段介绍代码结构和概念。包含实际代码示例的完整节点构建教程，请参阅[构建声明式节点](../../tutorial-build-a-declarative-style-node.md)或[构建编程式节点](../../tutorial-build-a-programmatic-style-node.md)。

还可以查看 [n8n-nodes-starter](https://github.com/n8n-io/n8n-nodes-starter) 和 n8n 自带的[节点](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes)，了解更多示例。入门项目提供可供扩展的基础示例。n8n 的 [Mattermost 节点](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Mattermost)则展示了更复杂的编程式节点，包括版本控制。

## 本节内容 <a id="in-this-section"></a>

适用于所有节点的内容：

* [节点基础文件的结构](structure.md)
* [标准参数](standard-parameters.md)

声明式节点请参阅：

* [声明式参数](declarative-style-parameters.md)

编程式节点请参阅：

* [编程式参数](programmatic-style-parameters.md)
* [编程式 execute() 方法](programmatic-style-execute-method.md)

## 相关资源 <a id="related-resources"></a>

* [节点构建参考](../)
