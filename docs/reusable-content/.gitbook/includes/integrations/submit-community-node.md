---
title: 提交社区节点
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

社区节点是托管在 npm registry 中的 npm 软件包。

开发准备提交到社区节点仓库的节点时，请使用以下资源，确保配置正确：

* n8n 建议使用 [`n8n-node` CLI 工具](../../../../connect/create-nodes/build-your-node/using-the-n8n-node-tool.md)构建和测试节点，尤其是计划[提交节点验证](../../../../connect/create-nodes/deploy-your-node/submit-community-nodes.md#submit-your-node-for-verification-by-n8n)时。这样可确保节点结构正确、符合社区节点要求，也能简化 lint 检查和测试。
* 查看 [n8n 自身的节点](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes)，参考可采用的实现模式。
* 参阅[构建自己的节点](../../../../connect/create-nodes/overview.md)文档。
* 确保节点符合以下社区节点标准。

## 标准 <a href="#standards" id="standards"></a>

使用 [`n8n-node` 工具](../../../../connect/create-nodes/build-your-node/using-the-n8n-node-tool.md)开发，可确保节点符合以下标准，以加入 n8n 社区节点仓库：

* 软件包名称必须以 `n8n-nodes-` 或 `@<scope>/n8n-nodes-` 开头，例如 `n8n-nodes-weather` 或 `@weatherPlugins/n8n-nodes-weather`。
* 在软件包关键词中加入 `n8n-community-node-package`。
* 确保将节点和凭据添加到 `package.json` 文件的 `n8n` 属性中。
* 使用 linter（`npm run lint`）检查节点，并在本地测试（`npm run dev`），确保正常工作。
* 将软件包发布到 npm。如果计划通过 [n8n Creator Portal](https://creators.n8n.io/nodes) 提交节点验证，必须使用带有[构建来源证明](https://docs.npmjs.com/generating-provenance-statements)的 GitHub Actions 工作流发布。请参阅下文**发布到 npm**。

## 发布到 npm <a href="#publishing-to-npm" id="publishing-to-npm"></a>

{% hint style="info" %}
**Creator Portal 验证的必要条件**

自 2026 年 5 月 1 日起，提交验证的节点必须通过 GitHub Actions 发布，并附带[构建来源证明](https://docs.npmjs.com/generating-provenance-statements)。n8n 不接受直接从本地机器发布的已验证节点。
{% endhint %}

要通过 n8n Creator Portal 提交节点验证，请使用带有构建来源证明的 GitHub Actions 工作流发布。来源证明让任何人都能通过密码学方法确认：某个软件包由特定仓库、特定提交中的工作流构建。GitHub Actions 使用自身的 OIDC 基础设施签署来源证明。

### 新节点 <a href="#new-nodes" id="new-nodes"></a>

使用 `npm create @n8n/node` 生成节点脚手架时，会包含可直接使用的 `publish.yml` 工作流。在本地运行 `npm run release` 更新版本、提交、打标签并推送，即会触发工作流发布到 npm。

### 已有节点 <a href="#existing-nodes" id="existing-nodes"></a>

将 [n8n-nodes-starter 中的发布工作流](https://github.com/n8n-io/n8n-nodes-starter/blob/master/.github/workflows/publish.yml)添加到仓库的 `.github/workflows/publish.yml`。

同时确保项目将 `@n8n/node-cli` 版本 `0.23.0` 或更高版本列为 `devDependency`，因为更早版本不支持工作流使用的来源证明选项：

```sh
npm list @n8n/node-cli
```

### 一次性设置 <a href="#one-time-setup" id="one-time-setup"></a>

配置 npm 信任仓库的 GitHub Actions 工作流，使其可代你发布，无需长期有效的令牌：

1. 登录 [npmjs.com](https://www.npmjs.com/)，打开软件包设置。
2. 在 **Publish access > Trusted Publishers**（发布访问 > 可信发布者）下，点击 **Add a publisher**（添加发布者）。
3. 选择 **GitHub Actions**，填写：
   - **Repository owner**（仓库所有者）：GitHub 用户名或组织名。
   - **Repository name**（仓库名称）：你的仓库名称。
   - **Workflow name**（工作流名称）：`publish.yml`，指文件名，不是工作流的 `name:` 字段。

也可改用令牌：在 npmjs.com 创建 Granular Access Token（细粒度访问令牌），并作为 `NPM_TOKEN` 保存到仓库的 Actions secrets 中。详情请参阅工作流文件的注释。

## 提交节点供 n8n 验证 <a href="#submit-your-node-for-verification-by-n8n" id="submit-your-node-for-verification-by-n8n"></a>

n8n 会审核已验证社区节点。用户可在 n8n 节点面板中发现和安装这些节点，因此节点需要遵循特定的技术、用户体验标准和限制。

{% hint style="info" %}
**验证要求通过 GitHub Actions 发布**

自 2026 年 5 月 1 日起，通过 [n8n Creator Portal](https://creators.n8n.io/nodes) 提交验证的节点，必须使用 GitHub Actions 发布并附带构建来源证明。设置说明请参阅“发布到 npm”。
{% endhint %}

提交节点给 n8n 审核前，必须：

* 从 [`n8n-node` 工具](../../../../connect/create-nodes/build-your-node/using-the-n8n-node-tool.md)生成的脚手架开始。虽然不是硬性要求，但 n8n 强烈建议对所有计划提交验证的社区节点使用 `n8n-node` CLI 工具，确保遵循预期约定及社区节点要求。
* 确保符合[已验证社区节点的技术指南](../../../../connect/create-nodes/build-your-node/reference/verification-guidelines.md)，并通过全部自动检查。特别需要注意，已验证社区节点不允许使用任何运行时依赖。
* 确保符合[用户体验指南](../../../../connect/create-nodes/build-your-node/reference/ux-guidelines.md)。
* 确保在 [npm 软件包](https://docs.npmjs.com/about-package-readme-files)或相关公开仓库的 README 中提供适当文档。
* 按**发布到 npm**所述，使用带来源证明的 GitHub Actions 工作流发布到 npm，n8n 会从那里获取并做最终审核。

## 准备好提交了吗？ <a href="#ready-to-submit" id="ready-to-submit"></a>
如果符合以上全部要求，请注册或登录 [n8n Creator Portal](https://creators.n8n.io/nodes) 并提交节点验证。注意，n8n 保留拒绝与其付费功能（尤其是企业功能）竞争的节点的权利。
