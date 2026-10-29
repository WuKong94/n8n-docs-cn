---
contentType: overview
nodeTitle: 参考
originalFilePath: integrations/creating-nodes/build/reference/index.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/reference
url: https://docs.n8n.io/connect/create-nodes/build-your-node/reference
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 节点构建参考 <a href="#node-building-reference" id="node-building-reference"></a>

本节为节点开发者提供参考资料，涵盖节点界面元素、节点基础文件和凭据文件中的关键参数，以及提交节点接受 [n8n 验证](../../../../integrations/community-nodes/installation-and-management/install-verified-community-nodes.md)的指南。

## 本节内容 <a id="in-this-section"></a>

* [节点界面元素](node-ui-elements.md)：可用于节点参数的预定义界面组件。
* [代码标准](code-standards.md)：节点开发的良好编码实践。
* [错误处理](error-handling.md)：n8n 为节点实现提供的错误类。
* [版本控制](versioning.md)：在不破坏现有行为的情况下修改节点。
* [基础文件](base-files/README.md)：声明式和编程式节点的核心代码。
* [codex 文件](codex-files.md)：保存节点元数据的 JSON 文件。
* [凭据文件](credentials-files.md)：定义节点的授权方式。
* [HTTP 请求辅助方法](http-request-helpers.md)：从节点发起 HTTP 请求。
* [数据项关联](item-linking.md)：将输出数据项关联到生成它们的输入数据项。
* [用户体验指南](ux-guidelines.md)：经过验证的社区节点必须遵循的界面规范。
* [验证指南](verification-guidelines.md)：n8n 验证社区节点时的要求。

## 相关资源 <a id="related-resources"></a>

* [构建节点](../)
* [设置开发环境](../set-up-your-development-environment.md)
* [使用 n8n-node 工具](../using-the-n8n-node-tool.md)
* [教程：构建声明式节点](../tutorial-build-a-declarative-style-node.md)
* [教程：构建编程式节点](../tutorial-build-a-programmatic-style-node.md)
