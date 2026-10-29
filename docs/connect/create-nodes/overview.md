---
contentType: overview
nodeTitle: 概览
originalFilePath: integrations/creating-nodes/overview.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/overview
url: https://docs.n8n.io/connect/create-nodes/overview
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 创建节点 <a href="#creating-nodes" id="creating-nodes"></a>

了解如何构建自己的自定义节点[^1]。

本节包括：

* 开发规划指南，包括[选择开发方式](plan-your-node/choose-a-node-building-style.md)。
* 针对不同节点开发方式的[教程](build-your-node/README.md)。
* [测试节点](test-your-node/README.md)说明，包括 n8n [节点 linter](test-your-node/node-linter.md)用法及[故障排查](test-your-node/troubleshooting.md)支持。
* 如何向社区[分享节点](deploy-your-node/submit-community-nodes.md)、提交给 [n8n 验证](deploy-your-node/submit-community-nodes.md)，或作为[私有节点](deploy-your-node/install-private-nodes.md)使用。
* [参考资料](build-your-node/reference/README.md)，包括界面元素及组成节点的各类文件说明。

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

本节假定你具备以下基础：

* 对 JavaScript 和 TypeScript 有一定了解。
* 能够管理自己的开发环境，包括 Git。
* 了解 npm，包括创建和提交软件包。
* 熟悉 n8n，并充分了解[数据结构](../../build/work-with-data/understand-n8ns-data-structure.md)和[数据项关联](../../build/work-with-data/reference-data/link-data-items/README.md)。

[^1]: 在 n8n 中，节点是组成工作流的独立组件。节点定义工作流何时运行，可获取、发送和处理数据，定义流程控制逻辑，并连接外部服务。

## 相关资源 <a id="related-resources"></a>

* [创建节点](./)
* [规划节点](plan-your-node/README.md)
* [构建节点](build-your-node/README.md)
* [测试节点](test-your-node/README.md)
* [部署节点](deploy-your-node/README.md)
