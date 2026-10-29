---
description: 将 .n8np 软件包导入 n8n 实例，控制内容的存放位置及 n8n 解析依赖的方式。
status: preview
layout:
  description:
    visible: false
tags:
- tag: preview
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 导入软件包 <a id="import-a-package"></a>

{% hint style="info" %}
**预览状态**

n8n 软件包处于预览阶段，导入选项在未来版本中可能发生变化。
{% endhint %}

导入会读取一个 [n8n 软件包](README.md)，即 [.n8np 归档](package-format.md)，并将内容写入目标实例。n8n 首先检查整个软件包：只要存在阻止导入的问题，就不会写入任何内容，并一次性返回所有问题。详情请参阅[导入机制](how-import-works.md)。

使用 [n8n CLI](../../../connect/n8n-cli.md)：

```bash
n8n-cli package import --file=triage.n8np --project-id=<target-project-id>
```

也可以直接调用端点。将归档放入名为 `package` 的 multipart 字段，每个选项作为单独的文本字段：

```bash
curl -X POST 'https://n8n.example.com/api/v1/n8n-packages/import' \
	-H "X-N8N-API-KEY: <your-api-key>" \
	-F 'package=@triage.n8np' \
	-F 'workflowConflictPolicy=new-version' \
	-F 'projectId=<target-project-id>'
```

完整的请求和响应结构，请参阅[端点参考](../../../connect/n8n-api/api-reference.md)中的 `N8nPackage` 部分。

{% hint style="info" %}
直接调用端点而不是使用 CLI 时，请求必须为 `multipart/form-data`。其他内容类型会返回 `415`。`workflowConflictPolicy` 是必填字段，CLI 会代为提供。

不需要设置的选项应省略，不要传入空值。策略或模式字段为空时，会被拒绝并返回 `400`。只有 `projectId`、`folderId` 和 `bindings` 接受空值，n8n 会将其视为未提供。
{% endhint %}

## 内容的存放位置 <a id="where-the-contents-land"></a>

对于工作流软件包或文件夹软件包，可以自行选择目标位置：

| 标志 | 说明 |
|------|-------------|
| `--file` | `.n8np` 文件的路径，必填。没有简写别名，因为 `-f` 已用于 `--format`。 |
| `--project-id`、`-p` | 目标项目 ID，默认为个人项目。别名：`--project`。 |
| `--folder-id` | 项目内的目标文件夹 ID，默认为项目根目录。别名：`--folder`。 |

{% hint style="warning" %}
对于项目软件包，`--project-id` 和 `--folder-id` 会被忽略，且不发出警告。项目软件包自带项目，各项目的内容会进入对应项目的根目录。使用 `--project-conflict-policy` 控制项目已存在时的处理方式。
{% endhint %}

{% hint style="info" %}
本文中的标志使用 kebab-case（短横线命名）。`n8n-cli package import --help` 会显示等效的 camelCase（驼峰命名）名称（`--projectId`、`--workflowConflictPolicy`、`--tagConflictPolicy`），错误消息也使用这些名称。两种写法都有效。

不存在 `--conflict-policy`、`--force` 或 `--dry-run`。工作流冲突对应的标志是 `--workflow-conflict-policy`。
{% endhint %}

## 工作流选项 <a id="workflow-options"></a>

| 标志 | 值 | 说明 |
|------|--------|-------------|
| `--workflow-conflict-policy` | `new-version`（默认）、`fail`、`skip` | 工作流已存在于目标实例时的处理方式。`new-version` 保存已有工作流的新版本；`fail` 拒绝整个导入；`skip` 保持原工作流不变，继续导入其他内容。 |
| `--workflow-id-policy` | `source`（默认）、`new` | 控制导入工作流保留包内 ID，还是获得新 ID。`source` 适合在实例之间推进部署；`new` 适合将同一软件包反复导入同一实例，并将包内 ID 记录为工作流的源 ID。 |
| `--workflow-publishing-policy` | `preserve-published-state`（默认）、`match-source`、`publish-all`、`unpublish-all` | 控制导入工作流最终是否发布。请参阅[发布](#publishing)。 |
| `--missing-node-type-mode` | `fail`（默认）、`import-anyway` | 工作流使用的节点类型或节点版本在目标实例上不存在时的处理方式。`fail` 在写入任何内容前拒绝导入，并列出所有缺失类型及使用它们的工作流；`import-anyway` 会导入工作流，但绝不会发布这些工作流。 |

n8n 先根据目标中记录的源工作流 ID，将包内工作流匹配到已有工作流；未匹配时，再查找自身 ID 与包内 ID 相同的目标工作流。因此，重复推进部署会收敛到同一结果：第二次导入更新已有工作流，而不是创建副本。

### 发布 <a id="publishing"></a>

n8n 始终先以未发布状态写入导入的工作流。全部内容就绪后，再在导入结束时统一应用一次发布策略。

| 值 | 行为 |
|-------|--------------|
| `preserve-published-state`（默认） | 新工作流保留为草稿。更新已有工作流时，只有目标原本已发布且包内工作流也已发布，才会重新发布。 |
| `match-source` | 遵循包内工作流的发布状态。 |
| `publish-all` | 发布所有导入的工作流。需要对目标项目具有 `workflow:publish` 权限。 |
| `unpublish-all` | 新工作流保持草稿，更新的已有工作流会被取消发布。 |

两种情况会覆盖发布策略：使用占位凭据的工作流绝不会发布，使用实例中缺失节点类型的工作流也不会发布。n8n 会将其报告为 `blocked` 并说明原因。已归档的工作流同样不会发布。

发布也可能失败而不导致整个导入失败，最常见的原因是两个工作流使用相同的 Webhook 路径。请参阅[发布结果](how-import-works.md#publishing-outcomes)。

## 文件夹和项目选项 <a id="folder-and-project-options"></a>

| 标志 | 值 | 说明 |
|------|--------|-------------|
| `--folder-conflict-policy` | `merge`（默认）、`fail` | 包内文件夹已存在于目标项目时的处理方式。`merge` 复用已有文件夹并将包内内容合并进去，保留原名称；`fail` 拒绝导入。 |
| `--project-conflict-policy` | `merge`（默认）、`fail`、`overwrite` | 仅适用于项目软件包。包内项目已存在时的处理方式。`merge` 保留项目详情并加入包内内容；`overwrite` 还会替换项目名称、说明和图标，软件包未携带的内容保持原样；`fail` 拒绝导入。 |

工作流软件包和文件夹软件包会忽略 `--project-conflict-policy`。

即使使用 `merge`，两类文件夹冲突仍会拒绝导入：文件夹 ID 已存在于其他项目；或已有文件夹的父级与导入预定位置不同。两种情况都意味着移动文件夹，无法通过策略解决。

包含文件夹的软件包需要支持文件夹功能的许可证。

## 凭据选项 <a id="credential-options"></a>

| 标志 | 值 | 说明 |
|------|--------|-------------|
| `--credential-matching-mode` | `id-only`（默认）、`name-and-type`、`type-only` | 控制 n8n 如何为包内引用查找目标凭据。 |
| `--credential-missing-mode` | `create-stub`（默认）、`must-preexist` | 引用无法解析时的处理方式。`create-stub` 在目标项目创建空占位凭据，工作流可以导入但无法发布；`must-preexist` 拒绝导入。 |

所有模式下，n8n 都只考虑你有权读取且目标项目有权使用的凭据，以及全局凭据。无权读取的凭据绝不会成为候选，`id-only` 模式也不例外。这通常是 ID 相同却未能匹配的原因。

排序规则和完整解析顺序，请参阅[凭据](how-import-works.md#credentials)。

## 数据表选项 <a id="data-table-options"></a>

| 标志 | 值 | 说明 |
|------|--------|-------------|
| `--data-table-matching-mode` | `by-id`（默认且唯一的值） | 匹配目标项目中 ID 相同的数据表，绝不会回退到按名称匹配。 |
| `--data-table-missing-mode` | `create`（默认）、`must-preexist`、`do-nothing` | 引用的数据表不在目标项目中时的处理方式。`create` 根据包内表结构创建表，保留源 ID，不包含数据行；`must-preexist` 拒绝导入；`do-nothing` 跳过创建。 |
| `--data-table-schema-conflict-policy` | `keep-existing`（默认）、`fail`、`overwrite`、`overwrite-non-destructive` | 匹配表的结构与软件包不同时的处理方式。`keep-existing` 允许目标表存在自身额外的列；`fail` 也会拒绝这类额外列；`overwrite` 修改目标表，使其与软件包一致；`overwrite-non-destructive` 进行相同修改，但当更改会删除列或更改列类型时拒绝导入。 |

使用 `keep-existing` 和 `fail` 时，包内每一列都必须在匹配的目标表中存在，且名称和类型相同。缺列或类型不匹配会拒绝导入，源端重命名的列也会被视为缺失。这两种策略都不修改目标表，因此不会向其中添加包内列。

`overwrite` 会添加、删除、重命名列、更改列类型和顺序，以及重命名表。数据行和其他列会保留。删除列或更改列类型会移除该列中的值；重命名列会保留值。这些变化会影响使用该表的所有工作流。

`overwrite-non-destructive` 进行相同修改，但当更改会删除列或更改列类型时停止导入，不写入任何内容。目标表有而软件包没有的列，视为将被删除。

各策略的详细说明，请参阅[数据表](how-import-works.md#data-tables)。

即使使用 `--data-table-missing-mode=do-nothing`，匹配到的表仍会进行结构检查。该选项控制缺失表的处理，不控制结构比较。

## 变量选项 <a id="variable-options"></a>

| 标志 | 值 | 说明 |
|------|--------|-------------|
| `--variable-missing-mode` | `create-with-value`（默认）、`create-stub`、`must-preexist`、`do-nothing` | 引用变量既不在目标项目中，也不在全局范围中时的处理方式。`create-with-value` 使用包内值创建变量；包内无值时，回退为创建空变量；`create-stub` 始终创建空变量；`must-preexist` 拒绝导入；`do-nothing` 仍然导入并报告未解析名称，工作流将在运行时失败。 |
| `--variable-conflict-policy` | `keep-existing`（默认）、`overwrite`、`fail` | 引用变量已可解析，但软件包携带不同值时的处理方式。`keep-existing` 保留目标值；`overwrite` 替换目标值；`fail` 拒绝导入。 |
| `--variable-parent-policy` | `project`（省略此选项时的行为）、`global` | 新变量的创建位置。项目软件包会拒绝此选项并返回 `400`，因为其布局已决定变量位置。 |

n8n 始终按名称匹配变量，不按 ID 匹配，与 `$vars.<name>` 在运行时的解析方式一致：先查目标项目，再查全局范围。

{% hint style="warning" %}
`--variable-conflict-policy=overwrite` 会写入实际解析到的作用域中的变量。如果名称解析到全局变量，其他读取该变量的项目也会看到新值，且不会发出警告。
{% endhint %}

创建或覆盖变量需要支持变量的许可证、对应的 API 密钥权限范围，且实例的变量数量必须尚未达到上限。如果导入中的所有变量都已可解析，则不会写入变量，因此不需要上述条件。

## 标签选项 <a id="tag-options"></a>

| 标志 | 值 | 说明 |
|------|--------|-------------|
| `--tag-missing-mode` | `create`（默认）、`do-nothing` | 包内引用的标签不在目标实例时的处理方式。`create` 使用源 ID 和名称创建全局标签；`do-nothing` 导入工作流但不添加这些标签，并将其列为已跳过。 |
| `--tag-conflict-policy` | `skip`（默认）、`fail`、`rename` | 标签冲突时的处理方式。`skip` 丢弃标签并列为已跳过；`fail` 拒绝导入；`rename` 对名称已变化的目标标签重命名，发生名称冲突时，将已有标签改用包内 ID，保留其名称及所有关联的打标内容。 |

标签按源 ID 匹配，不按名称匹配，因为只有通过稳定 ID 才能检测重命名。

冲突有两种：重命名差异，即目标标签 ID 相同但名称不同，表示有人在某个实例上重命名了标签；名称冲突，即目标上没有该 ID，但另一个标签已占用该名称。这在标签独立创建的已有实例上很常见。

{% hint style="warning" %}
丢弃标签可能导致已有工作流失去标签。更新工作流时，n8n 会用软件包的标签列表完全替换目标工作流的标签。丢弃的标签会先从该列表中过滤掉，因此，如果带标签工作流在包内的标签全部被丢弃，更新就会清空其当前标签。

要保留已有标签，导出时使用 `--include-tags=false`，这样会省略标签列表，而不是发送空列表。
{% endhint %}

如果目标实例设置了 `N8N_WORKFLOW_TAGS_DISABLED=true`，全部标签处理会被静默跳过，绝不会因此导致导入失败。

## 绑定 <a id="bindings"></a>

绑定将包内某个实体映射到实例上的指定实体，跳过匹配规则。传入按实体类型分组的 JSON 对象，目前只接受 `credentials`：

```bash
n8n-cli package import --file=triage.n8np \
	--bindings='{"credentials":{"crLin44":"crProd8"}}'
```

这会将包内 `crLin44` 凭据映射到目标上的 `crProd8`，因此所有使用 `crLin44` 的工作流都会改用 `crProd8`。n8n 在运行 `--credential-matching-mode` 前应用绑定，且仍会检查类型是否匹配：绑定到错误类型的凭据会拒绝导入。

n8n 会拒绝 `credentials` 以外的任何键，并返回 `400`，而不是将其忽略。

绑定的凭据无法解析时，始终会拒绝导入，即使使用默认的 `create-stub` 也不例外。只有未绑定的引用才会获得占位凭据。

n8n 会在响应中返回实际使用的绑定。保存 `credentials` 映射，并在后续导入中作为 `--bindings='{"credentials":{...}}'` 传回，可以保持映射稳定。响应还包含 `workflows` 映射，但仅供参考；将其传回会被拒绝并返回 `400`。

## 导入响应 <a id="the-import-response"></a>

导入成功会返回 `200`，包含九个键：

```json
{
	"package": {
		"sourceN8nVersion": "2.34.0",
		"sourceId": "f9e1e962bba26edf357042c12f367dab17f4c63ec368e1f39cbf7ce43c8b9f8b",
		"exportedAt": "2026-08-04T09:14:02.117Z"
	},
	"workflows": [
		{ "sourceWorkflowId": "wf9Zx1", "localId": "wf9Zx1", "name": "Send email",
			"projectId": "prProd4", "parentFolderId": null,
			"activeVersionId": null, "publishing": { "state": "unchanged" }, "status": "created" },
		{ "sourceWorkflowId": "wf7Kq2", "localId": "wf7Kq2", "name": "Triage inbound",
			"projectId": "prProd4", "parentFolderId": null,
			"activeVersionId": null, "publishing": { "state": "unchanged" }, "status": "created" }
	],
	"folders": [],
	"projects": [],
	"bindings": {
		"workflows": { "wf7Kq2": "wf7Kq2", "wf9Zx1": "wf9Zx1" },
		"credentials": { "crLin44": "crLin44" }
	},
	"credentials": { "matched": ["crLin44"], "stubbed": [] },
	"dataTables": { "matched": 0, "created": 1, "updated": 0 },
	"variables": { "matched": [], "missing": [], "created": ["slackChannelId"], "stubbed": [], "updated": [] },
	"tags": { "matched": [], "created": ["prod"], "renamed": [], "reconciled": [], "skipped": [] }
}
```

| 键 | 内容 |
|-----|---------------|
| `package` | 从清单复制的源实例 n8n 版本、实例 ID 和导出时间戳 |
| `workflows` | 每个工作流一行，包含其 `status`（`created`、`updated` 或 `skipped`）及 `publishing` 结果 |
| `folders` | 每个文件夹一行，`status` 为 `created` 或 `skipped` |
| `projects` | 每个项目一行，`status` 为 `created`、`updated` 或 `skipped`。工作流软件包和文件夹软件包中为空 |
| `bindings` | 工作流和凭据的源 ID 到目标 ID 映射。后续导入时只能传回 `credentials` 映射 |
| `credentials` | 源凭据 ID，分为 `matched` 和 `stubbed` |
| `dataTables` | 数据表 `matched`、`created` 和 `updated` 的数量。`updated` 统计通过 `overwrite` 或 `overwrite-non-destructive` 修改的表 |
| `variables` | 变量名称，分为 `matched`、`missing`、`created`、`stubbed` 和 `updated`。不会出现变量值 |
| `tags` | 标签名称，分为 `matched`、`created`、`renamed`、`reconciled` 和 `skipped` |

工作流的 `localId` 是其在目标实例上的 ID：`--workflow-id-policy=source` 策略下为包内 ID，`new` 策略下为新 ID；如果工作流被更新或跳过，则为已有工作流的 ID。

`publishing.state` 的值为 `published`、`unpublished`、`unchanged`、`blocked` 或 `failed`。各值含义请参阅[发布结果](how-import-works.md#publishing-outcomes)。

示例中的两个工作流都是新建的，默认 `preserve-published-state` 策略不会发布新工作流，因此两者都报告 `unchanged`。要让新工作流导入后即处于已发布状态，使用 `--workflow-publishing-policy=publish-all`，或使用 `match-source`（前提是它们在包内被指定为 `published`）。

## 错误 <a id="errors"></a>

导入被拒绝时，会返回发现的全部问题，而不只是第一个：

```json
{
	"message": "Import blocked: 2 issue(s) must be resolved before the package can be imported.",
	"issues": [
		{ "type": "missing-node-type", "nodeType": "@acme/cool-node", "typeVersion": 3,
			"usedByWorkflows": ["wf7Kq2"] },
		{ "type": "credential-unresolved", "kind": "not_found", "sourceId": "crLin44",
			"usedByWorkflows": ["wf7Kq2"] }
	]
}
```

未写入任何内容。CLI 会以非零状态退出，并输出问题列表。

| 状态 | 含义 |
|--------|---------|
| `400` | 请求或软件包格式错误；也可能是在项目软件包上使用 `--variable-parent-policy`，或 `--bindings` 的值无效 |
| `403` | 缺少 API 密钥权限范围、无权访问目标项目，或许可证不支持文件夹、变量或团队项目 |
| `404` | 传入的项目 ID 不存在，或用户没有个人项目 |
| `409` | 因冲突拒绝导入 |
| `413` | 上传内容超过实例允许的大小 |
| `415` | 请求不是 `multipart/form-data` |
| `422` | 因其他原因拒绝导入，例如凭据无法解析或缺少节点类型 |

所有拒绝导入的原因及对应状态，请参阅[为何拒绝导入](how-import-works.md#why-an-import-is-refused)。

## 事件 <a id="events"></a>

每次导入都会在日志流和遥测路径上发出事件，便于审计哪些内容进入了实例。

| 事件 | 发出时机 |
|-------|--------------|
| `n8n.audit.n8n-package.import.success` | 导入成功 |
| `n8n.audit.n8n-package.import.failed` | 导入失败 |

成功事件包含用户、内容存放的项目和文件夹、已写入的工作流、此次导入使用的所有选项、软件包中的源实例 ID 和格式版本，以及分为已匹配、已创建和已更新的凭据 ID。被跳过的工作流不包含在内。即使软件包包含多个项目，也只发出一个事件。

失败事件包含用户、`reason`（值为 `access-denied`、`entity-not-found`、`blocked` 或 `validation`），以及目标项目和文件夹（前提是导入已进行到能够解析它们的阶段）。它不包含工作流 ID，因为许多失败发生在 n8n 读取软件包之前。

被拒绝的导入不会发出成功事件。日志流事件携带 ID，不携带数量；遥测事件携带数量，不携带 ID。

## 继续阅读 <a id="read-next"></a>

* [导入机制](how-import-works.md)：了解 n8n 写入内容的顺序和各类实体的解析方式。
* [导出软件包](export-a-package.md)：了解决定软件包初始结构的选项。
* [限制和权限](limits-and-permissions.md)：了解上传上限和完整的权限范围矩阵。

## 相关资源 <a id="related-resources"></a>

* [n8n 软件包](./)
* [软件包格式](package-format.md)
* [导出软件包](export-a-package.md)
* [导入机制](how-import-works.md)
* [限制和权限](limits-and-permissions.md)
