---
contentType: howto
nodeTitle: 节点 linter
originalFilePath: integrations/creating-nodes/test/node-linter.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/test/node-linter
url: https://docs.n8n.io/connect/create-nodes/test-your-node/node-linter
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# n8n 节点 linter <a href="#n8n-node-linter" id="n8n-node-linter"></a>

n8n 节点 linter [`@n8n/eslint-plugin-community-nodes`](https://github.com/n8n-io/n8n/tree/master/packages/%40n8n/eslint-plugin-community-nodes) 对社区软件包中的 n8n 节点和凭据源代码执行静态分析（lint），发现问题并自动修复，帮助遵循最佳实践。

`@n8n/eslint-plugin-community-nodes` 包含一组[规则](https://github.com/n8n-io/n8n/tree/master/packages/%40n8n/eslint-plugin-community-nodes#rules)，用于检查社区软件包的节点文件（`*.node.ts`）、凭据文件（`*.credentials.ts`）和 `package.json`。

## 设置 <a href="#setup" id="setup"></a>

使用 [n8n 节点入门项目](https://github.com/n8n-io/n8n-nodes-starter)时，在项目中运行 `npm install` 安装全部依赖，安装完成后即可使用 linter。

使用 VS Code 时，请安装 [ESLint VS Code 扩展](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)。其他 IDE 请参阅各自的 ESLint 集成说明。

{% hint style="info" %}
**不要编辑配置文件**

[`eslint.config.mjs`](https://github.com/n8n-io/n8n-nodes-starter/blob/master/eslint.config.mjs) 包含由 [`@n8n/node-cli`](https://www.npmjs.com/package/@n8n/node-cli) 提供的 ESLint 配置，请勿编辑此文件。
{% endhint %}

## 用法 <a href="#usage" id="usage"></a>

可在社区软件包或 n8n 主仓库中使用 linter。

### 执行 lint 检查 <a href="#linting" id="linting"></a>

社区软件包在安装依赖后、发布到 npm 前会自动运行 linter。在 [n8n 主仓库](https://github.com/n8n-io/n8n)中，每次向拉取请求推送时，会通过 GitHub Actions 自动运行。

这两种情况下，VS Code 都会在开发时于后台执行 lint 检查。将鼠标悬停在问题上，可查看完整说明及更多信息链接。

也可手动运行 linter：

* 运行 `npm run lint`，执行 lint 检查并在控制台查看问题。
* 运行 `npm run lint:fix`，执行 lint 检查并自动修复问题。linter 只自动修复[标记为可自动修复](https://github.com/n8n-io/n8n/tree/master/packages/%40n8n/eslint-plugin-community-nodes#rules)的规则违规。

两个命令均可在社区软件包根目录运行，或在主仓库的 `/packages/nodes-base/` 中运行。

### 例外 <a href="#exceptions" id="exceptions"></a>

除了修正规则违规，也可为特定情况设置例外，使 linter 不再报告。

在 VS Code 中设置 lint 例外：悬停在问题上，按 `Quick fix`（macOS 为 `cmd+.`），选择 **Disable {rule} for this line**（对此行禁用该规则）。只有理由充分时，才为单行禁用规则。如果认为 linter 误报，请[向 n8n 仓库报告](https://github.com/n8n-io/n8n/issues)。

要为单个文件添加 lint 例外，请添加代码注释。更多指南请参阅 [ESLint 文档](https://eslint.org/docs/latest/use/configure/rules#disabling-rules)。

## 相关资源 <a id="related-resources"></a>

* [测试节点](./)
* [在本地运行节点](run-your-node-locally.md)
* [故障排查](troubleshooting.md)
