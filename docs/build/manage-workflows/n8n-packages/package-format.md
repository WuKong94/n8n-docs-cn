---
description: .n8np 文件内部的内容：三种软件包结构、目录布局和清单。
status: preview
layout:
  description:
    visible: false
tags:
- tag: preview
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 软件包格式 <a id="package-format"></a>

{% hint style="info" %}
**预览状态**

n8n 软件包处于预览阶段，软件包格式在未来版本中可能发生变化。
{% endhint %}

[n8n 软件包](README.md)是 gzip 压缩的 tar 归档。标准工具即可读取，因此无需 n8n 也能检查其内容：

```bash
tar -tzf triage.n8np    # list what's inside
tar -xzf triage.n8np    # extract it
```

`.n8np` 扩展名是一种命名约定。n8n 导入时不检查文件名，也接受布局相同的未压缩 tar 文件。

归档内的每个实体都在自己的目录中，以独立的小型 JSON 文件保存；根目录中的 `manifest.json` 为全部内容建立索引。`manifest.json` 必须是归档中的第一个文件，这样 n8n 才能在读取其余内容前验证软件包。

## 三种软件包结构 <a id="three-package-shapes"></a>

结构取决于导出的内容。三种结构携带的文件类型相同，但排列方式不同。

### 工作流软件包 <a id="workflow-package"></a>

按工作流 ID 导出时，工作流直接存放在顶层，其所有依赖也位于顶层：

```
triage.n8np
├── manifest.json
├── workflows/
│   ├── triage-inbound/
│   │   └── workflow.json
│   └── send-email/
│       └── workflow.json
├── credentials/
│   └── linear-api/
│       └── credential.json
├── variables/
│   └── slackchannelid/
│       └── variable.json
├── data-tables/
│   └── countries/
│       └── data-table.json
└── tags/
    └── prod/
        └── tag.json
```

### 文件夹软件包 <a id="folder-package"></a>

按文件夹 ID 导出会保留文件夹树。工作流存放在所属文件夹内的 `workflows/` 目录中；嵌套文件夹直接位于父文件夹中，不会重复添加 `folders/` 路径段。凭据、变量、数据表和标签保留在顶层：

```
in-progress.n8np
├── manifest.json
├── folders/
│   ├── to-production/
│   │   └── folder.json            # an empty folder is just the shell
│   └── in-progress/
│       ├── folder.json
│       ├── workflows/
│       │   └── triage-inbound/
│       │       └── workflow.json
│       └── nested/
│           ├── folder.json
│           └── workflows/
│               └── playground/
│                   └── workflow.json
├── credentials/
│   └── linear-api/
│       └── credential.json
└── tags/
    └── prod/
        └── tag.json
```

### 项目软件包 <a id="project-package"></a>

按项目 ID 导出会增加一层命名空间。一个软件包可以携带多个项目。属于已导出项目的凭据、变量和数据表会嵌套在该项目之下。全局资源或属于包外项目的资源仍位于顶层。标签始终位于顶层，因为 n8n 中的标签是全局的：

```
team-ligo.n8np
├── manifest.json
├── projects/
│   └── team-ligo/
│       ├── project.json
│       ├── workflows/                    # workflows at the project root
│       │   └── triage-inbound/
│       │       └── workflow.json
│       ├── folders/
│       │   └── in-progress/
│       │       ├── folder.json
│       │       └── workflows/
│       │           └── send-email/
│       │               └── workflow.json
│       ├── credentials/                  # owned by this project
│       │   └── linear-api/
│       │       └── credential.json
│       ├── variables/                    # scoped to this project
│       │   └── slackchannelid/
│       │       └── variable.json
│       └── data-tables/
│           └── countries/
│               └── data-table.json
├── credentials/                          # a global credential
│   └── shared-smtp/
│       └── credential.json
├── variables/                            # a global variable
│   └── region/
│       └── variable.json
└── tags/                                 # always global
    └── prod/
        └── tag.json
```

{% hint style="info" %}
在项目软件包中，变量所在位置决定创建位置。位于 `projects/<project-slug>/variables/` 下的变量会在该项目中创建；位于顶层的变量会作为全局变量创建。这也是项目软件包拒绝 `--variable-parent-policy` 的原因：布局已决定其位置。
{% endhint %}

## 目录命名 <a id="directory-naming"></a>

每个实体都有一个根据名称生成 slug 的目录，其中保存一个 JSON 文件。生成 slug 时，名称先转为小写，再移除 a 到 z 字母、数字、空白和连字符以外的所有字符，最后将连续空白替换为单个连字符：

| 实体名称 | 目录 |
|-------------|-----------|
| `Triage inbound` | `triage-inbound` |
| `Linear api` | `linear-api` |
| `slackChannelId` | `slackchannelid` |
| `Q4 报告` | `q4` |
| `報告` | `workflow` |

最后一行展示了回退规则：如果生成 slug 后没有剩余字符，n8n 就使用实体类型作为名称（`workflow`、`folder`、`project`、`credential`、`variable`、`data-table` 或 `tag`）。名称生成相同 slug 时，从 2 开始添加数字后缀，因此第二个 `Triage inbound` 会变为 `triage-inbound-2`。

目录名便于人阅读归档。n8n 始终通过清单和 JSON 文件中的 ID 识别实体，不使用目录名。

## `manifest.json` <a id="manifestjson"></a>

清单是一份索引，说明软件包包含什么，以及目标实例必须提供什么。这样，导入可以在不读取每个文件的情况下尽早发现问题并失败。

以下四个字段始终存在：

* `packageFormatVersion`：软件包格式版本，当前为字符串 `"1"`。
* `exportedAt`：n8n 创建软件包的时间，格式为 ISO 8601 时间戳。
* `sourceN8nVersion`：创建软件包的 n8n 版本。
* `sourceId`：创建软件包的实例标识符。

之后是各类实体的条目列表，只有对应类型存在时才出现：`workflows`、`folders`、`projects`、`credentials`、`dataTables`、`variables` 和 `tags`。空列表会完全省略。每个条目都有相同的三个字段：

* `id`：实体在源实例上的 ID。
* `name`：实体名称。
* `target`：保存实体 JSON 文件的目录，相对于软件包根目录。

最后是 `requirements`，列出工作流在目标实例运行所需的资源。最多包含六个部分，每个条目都带有 `usedByWorkflows`，即依赖该资源的工作流 ID：

| 部分 | 条目结构 | 说明 |
|---------|-------------|-------|
| `credentials` | `{ id, name, type, usedByWorkflows }` | n8n 不会导出凭据数据，因此凭据需求始终表示必须由目标实例提供 |
| `dataTables` | `{ id, name, usedByWorkflows }` | 表结构本身位于包内的 `data-table.json` 中 |
| `workflows` | `{ id, name, usedByWorkflows }` | 子工作流和错误工作流引用。`name` 为可选字段，因为导出用户不一定能查看被引用的工作流 |
| `variables` | `{ name, usedByWorkflows }` | 仅名称，没有 ID，因为 `$vars.<name>` 在运行时按名称解析 |
| `tags` | `{ id, name, usedByWorkflows }` | |
| `nodeTypes` | `{ type, typeVersion, usedByWorkflows }` | 工作流使用的所有节点类型和版本。阅读此列表可判断目标实例能否导入软件包，因为这些节点必须全部安装。导入时，n8n 会根据工作流重新推导此列表，而不是信任清单中的列表 |

{% hint style="warning" %}
`requirements` 列出工作流的需求，不等同于软件包内容。`requirements.workflows` 列出每个静态工作流引用，包括已打包的子工作流。导出用户无权读取的凭据会出现在 `requirements.credentials` 中，但没有对应文件。因此，不应将 `requirements` 视为归档内容清单，应查看实体条目列表。
{% endhint %}

以下是包含两个工作流的工作流软件包的完整清单：

```json
{
	"packageFormatVersion": "1",
	"exportedAt": "2026-08-04T09:14:02.117Z",
	"sourceN8nVersion": "2.34.0",
	"sourceId": "f9e1e962bba26edf357042c12f367dab17f4c63ec368e1f39cbf7ce43c8b9f8b",

	"workflows": [
		{ "id": "wf7Kq2", "name": "Triage inbound", "target": "workflows/triage-inbound" },
		{ "id": "wf9Zx1", "name": "Send email", "target": "workflows/send-email" }
	],
	"credentials": [
		{ "id": "crLin44", "name": "Linear api", "target": "credentials/linear-api" }
	],
	"dataTables": [
		{ "id": "dtCn12", "name": "countries", "target": "data-tables/countries" }
	],
	"variables": [
		{ "id": "vaSl03", "name": "slackChannelId", "target": "variables/slackchannelid" }
	],
	"tags": [
		{ "id": "tgPr01", "name": "prod", "target": "tags/prod" }
	],

	"requirements": {
		"credentials": [
			{ "id": "crLin44", "name": "Linear api", "type": "linearApi", "usedByWorkflows": ["wf7Kq2"] }
		],
		"dataTables": [
			{ "id": "dtCn12", "name": "countries", "usedByWorkflows": ["wf7Kq2"] }
		],
		"workflows": [
			{ "id": "wf9Zx1", "name": "Send email", "usedByWorkflows": ["wf7Kq2"] }
		],
		"variables": [
			{ "name": "slackChannelId", "usedByWorkflows": ["wf7Kq2"] }
		],
		"tags": [
			{ "id": "tgPr01", "name": "prod", "usedByWorkflows": ["wf7Kq2"] }
		],
		"nodeTypes": [
			{ "type": "n8n-nodes-base.formTrigger", "typeVersion": 2.5, "usedByWorkflows": ["wf7Kq2"] },
			{ "type": "n8n-nodes-base.linear", "typeVersion": 1, "usedByWorkflows": ["wf7Kq2"] },
			{ "type": "n8n-nodes-base.executeWorkflow", "typeVersion": 1.2, "usedByWorkflows": ["wf7Kq2"] },
			{ "type": "n8n-nodes-base.dataTable", "typeVersion": 1, "usedByWorkflows": ["wf7Kq2"] },
			{ "type": "n8n-nodes-base.emailSend", "typeVersion": 2.1, "usedByWorkflows": ["wf9Zx1"] }
		]
	}
}
```

## `data-table.json` <a id="data-tablejson"></a>

每个数据表文件保存该表的结构，数据行不会随包迁移。

```json
{
	"id": "dtCn12",
	"name": "countries",
	"columns": [
		{ "id": "dcNm01", "name": "name", "type": "string", "index": 0 },
		{ "id": "dcCd02", "name": "code", "type": "string", "index": 1 }
	]
}
```

| 字段 | 说明 |
|-------|-------------|
| `id` | 表在源实例上的 ID。导入时创建的新表会保留此 ID |
| `name` | 表名称 |
| `columns` | 每列一个条目，包含其 `id`、`name`、`type` 和 `index`（在表中的位置） |
| `columns[].id` | 列在源实例上的 ID。n8n 2.44.0 之前导出的软件包不包含此字段 |

列 ID 让导入过程能够识别重命名的列，从而保留列值。n8n 2.44.0 之前导出的软件包不携带列 ID，因此 n8n 会按名称匹配列，重命名列会被视为破坏性更改。请参阅[数据表](how-import-works.md#data-tables)。

## 版本兼容性 <a id="version-compatibility"></a>

`packageFormatVersion` 当前为 `"1"`。只有格式版本完全一致时，n8n 实例才会导入软件包。不存在兼容范围，也没有迁移路径：声明其他版本的软件包会在写入任何内容前被拒绝，并返回 `400`。

`sourceN8nVersion` 仅供参考，不会与目标实例的版本比较。因此，只要格式版本一致，且目标实例安装了工作流使用的节点类型，就可以在不同 n8n 版本的实例之间迁移软件包。

数据表列 ID 是例外。从 n8n 2.44.0 起，导出的数据表会携带列 ID，较旧实例会拒绝含列 ID 的软件包，并返回 `400`。请先升级导入实例。

## 在流水线中比较软件包 <a id="comparing-packages-in-a-pipeline"></a>

归档生成是确定性的：文件时间戳固定为 Unix 纪元，权限固定，gzip 使用可移植模式。相同内容两次导出时，容器中的字节相同。

唯一例外是 `manifest.json`，每次导出都会携带新的 `exportedAt`。仅因这一字段，即使内容未变，两次导出的字节也不完全相同。如果在流水线中通过校验和检测软件包变化，请从比较中排除 `exportedAt`，否则每次运行都会出现差异。

## 继续阅读 <a id="read-next"></a>

* [导出软件包](export-a-package.md)：了解如何生成三种结构。
* [导入软件包](import-a-package.md)：了解控制内容存放位置的选项。
* [导入机制](how-import-works.md)：了解 n8n 如何处理各实体文件。

## 相关资源 <a id="related-resources"></a>

* [n8n 软件包](./)
* [导出软件包](export-a-package.md)
* [导入软件包](import-a-package.md)
* [导入机制](how-import-works.md)
* [限制和权限](limits-and-permissions.md)
