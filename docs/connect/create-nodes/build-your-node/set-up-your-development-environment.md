---
contentType: howto
nodeTitle: 设置开发环境
originalFilePath: integrations/creating-nodes/build/node-development-environment.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment
url: https://docs.n8n.io/connect/create-nodes/build-your-node/set-up-your-development-environment
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 设置开发环境 <a href="#set-up-your-development-environment" id="set-up-your-development-environment"></a>

本文列出开发节点的必要依赖，并说明如何设置编辑器。

## 要求 <a href="#requirements" id="requirements"></a>

构建和测试节点需要：

* Node.js 和 npm，Node 最低版本为 22.22.0。在 Linux、Mac 和 WSL（Windows Subsystem for Linux）中，可按照 [nvm 安装说明](https://github.com/nvm-sh/nvm)，使用 nvm（Node Version Manager）安装两者。Windows 用户请参阅微软的 [Windows 上安装 NodeJS](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows)指南。
* [`n8n-node` 工具](using-the-n8n-node-tool.md)，用于创建、构建和测试节点。它包含本地开发所需的 n8n，因此无需全局安装 n8n。测试流程请参阅[在本地运行节点](../test-your-node/run-your-node-locally.md)。[构建已验证社区节点](../../../integrations/community-nodes/building-community-nodes.md)时，必须使用 `n8n-node`。

还应安装 [Git](https://git-scm.com/)，以便克隆并使用 [n8n-nodes-starter](https://github.com/n8n-io/n8n-nodes-starter)。

## 编辑器设置 <a href="#editor-setup" id="editor-setup"></a>

n8n 推荐使用 [VS Code](https://code.visualstudio.com/) 作为编辑器。

安装以下扩展：

* [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
* [EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
* [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

使用 VS Code 和这些扩展，可在编写代码时看到 n8n 节点 linter 的警告。

## 相关资源 <a id="related-resources"></a>

* [构建节点](./)
* [使用 n8n-node 工具](using-the-n8n-node-tool.md)
* [教程：构建声明式节点](tutorial-build-a-declarative-style-node.md)
* [教程：构建编程式节点](tutorial-build-a-programmatic-style-node.md)
* [参考](reference/README.md)
