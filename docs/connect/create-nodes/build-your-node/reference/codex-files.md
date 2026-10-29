---
contentType: reference
nodeTitle: codex 文件
originalFilePath: integrations/creating-nodes/build/reference/node-codex-files.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/reference/node-codex-files
url: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/codex-files
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 节点 codex 文件 <a href="#node-codex-files" id="node-codex-files"></a>

codex 文件包含节点的元数据，是节点根目录下的 JSON 文件，例如 n8n 入门项目中的 [`GithubIssues.node.json`](https://github.com/n8n-io/n8n-nodes-starter/blob/master/nodes/GithubIssues/GithubIssues.node.json) 文件。

codex 文件名必须与节点基础文件名对应。例如，节点基础文件名为 `MyNode.node.ts` 时，codex 文件名应为 `MyNode.node.json`。

| 参数 | 说明 |
| -------- | ----------- |
| `node` | 标识节点。社区节点使用软件包名称，格式为 `n8n-nodes-<your-node-name>`，例如 `n8n-nodes-github-issues`。n8n 内置节点使用 `n8n-nodes-base.` 前缀，例如 `n8n-nodes-base.openweatherapi`。 |
| `nodeVersion` | 节点版本，必须与节点主文件中的 `version` 参数值相同，例如 `"1.0"`。 |
| `codexVersion` | codex 文件版本，当前版本为 `"1.0"`。 |
| `categories` | `categories` 数组中的设置决定 n8n 在图形界面中将节点归入哪个类别。更多信息请参阅[节点类别](#node-categories)。 |
| `resources` | `resources` 对象包含节点文档的链接。n8n 会在图形界面中自动为凭据和节点添加帮助链接。 |

## 节点类别 <a href="#node-categories" id="node-categories"></a>

可以在节点配置 JSON 中定义一个或多个类别，帮助 n8n 将节点放入节点面板中的正确分类。

可选择以下类别：

* Data & Storage（数据与存储）
* Finance & Accounting（财务与会计）
* Marketing & Content（营销与内容）
* Productivity（生产力）
* Miscellaneous（其他）
* Sales（销售）
* Development（开发）
* Analytics（分析）
* Communication（通信）
* Utility（实用工具）

语法必须完全匹配。例如，应使用 `Data & Storage`，而非 `data and storage`。

## 相关资源 <a id="related-resources"></a>

* [节点构建参考](./)
