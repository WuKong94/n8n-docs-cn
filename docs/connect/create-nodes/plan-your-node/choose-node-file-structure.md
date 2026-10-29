---
contentType: explanation
nodeTitle: 选择节点文件结构
originalFilePath: integrations/creating-nodes/build/reference/node-file-structure.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/reference/node-file-structure
url: https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-node-file-structure
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 节点文件结构 <a href="#node-file-structure" id="node-file-structure"></a>

在节点结构中遵循最佳实践与标准，可以让节点更容易维护，也便于其他人参与代码开发。

节点的文件与目录结构取决于：

* 节点的复杂程度。
* 是否使用节点版本控制。
* npm 软件包中包含多少个节点。

n8n 推荐使用 [`n8n-node` 工具](../build-your-node/using-the-n8n-node-tool.md)创建预期的节点文件结构。可按需自定义生成的脚手架，以满足更复杂的需求。

## 必需文件和目录 <a href="#required-files-and-directories" id="required-files-and-directories"></a>

节点必须包含：

* 位于项目根目录的 `package.json` 文件，每个 npm 模块都需要此文件。
* 包含节点代码的 `nodes` 目录：
    * 此目录必须包含[基础文件](../build-your-node/reference/base-files/README.md)，格式为 `<node-name>.node.ts`，例如 `MyNode.node.ts`。
    * n8n 建议包含 [codex 文件](../build-your-node/reference/codex-files.md)，用于保存节点元数据。codex 文件名必须与节点基础文件名匹配。例如，节点基础文件名为 `MyNode.node.ts` 时，codex 文件名应为 `MyNode.node.json`。
    * `nodes` 目录可包含其他文件和子目录，例如版本目录，以及为实现模块化而拆分到多个文件的节点代码。
* 包含凭据代码的 `credentials` 目录。代码位于单个[凭据文件](../build-your-node/reference/credentials-files.md)中，文件名格式为 `<node-name>.credentials.ts`，例如 `MyNode.credentials.ts`。

## 模块化结构 <a href="#modular-structure" id="modular-structure"></a>


可以将节点全部功能放在一个文件中，也可拆分为基础文件和其他模块，再由基础文件导入。除非节点非常简单，否则建议采用拆分方式。


基本模式是将各个操作拆分开，示例请参阅 [GithubIssues 入门节点](https://github.com/n8n-io/n8n-nodes-starter/tree/master/nodes/GithubIssues)。

对于更复杂的节点，n8n 建议采用目录结构，可参考 [Airtable 节点](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Airtable)或 [Microsoft Outlook 节点](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Microsoft/Outlook)。

* `actions`：包含代表各类资源的子目录。
    * 每个子目录应包含两类文件：
      * 包含资源描述的索引文件，命名为 `<resourceName>.resource.ts` 或 `index.ts`。
      * 操作文件 `<operationName>.operation.ts`。这些文件应有两个导出：操作的 `description` 和一个 `execute` 函数。
* `methods`：可选目录，用于存放动态参数函数。
* `transport`：包含通信实现的目录。


## 版本控制 <a href="#versioning" id="versioning"></a>

如果节点有多个版本且使用完整版本控制，文件结构会更复杂。每个版本需要独立目录，还需要一个设置默认版本的基础文件。版本使用及类型的更多说明，请参阅[节点版本控制](../build-your-node/reference/versioning.md)。

## 决定软件包包含多少个节点 <a href="#decide-how-many-nodes-to-include-in-a-package" id="decide-how-many-nodes-to-include-in-a-package"></a>

构建节点时有两种配置：

* 一个 npm 软件包包含一个节点。
* 一个 npm 软件包包含多个节点。

n8n 支持这两种方式。包含多个节点时，每个节点都应在 `nodes` 目录中拥有自己的目录。

## 编程式节点的最佳实践示例 <a href="#a-best-practice-example-for-programmatic-nodes" id="a-best-practice-example-for-programmatic-nodes"></a>

n8n 内置的 [Airtable 节点](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Airtable)采用模块化结构和版本控制，遵循推荐模式。

## 相关资源 <a id="related-resources"></a>

* [规划节点](./)
* [选择节点类型](choose-a-node-type.md)
* [选择节点开发方式](choose-a-node-building-style.md)
* [节点界面设计](node-ui-design.md)


