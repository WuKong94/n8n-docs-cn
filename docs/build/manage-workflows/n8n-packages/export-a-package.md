---
description: 将工作流、文件夹或完整项目导出为 .n8np 软件包，并控制 n8n 处理子工作流依赖的方式。
status: preview
layout:
  description:
    visible: false
tags:
- tag: preview
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 导出软件包 <a id="export-a-package"></a>

{% hint style="info" %}
**预览状态**

n8n 软件包处于预览阶段，导出选项在未来版本中可能发生变化。
{% endhint %}

导出会生成一个 [n8n 软件包](README.md)，即 [.n8np 归档](package-format.md)，其中包含指定内容，以及这些工作流在目标实例上所需的全部资源引用。导出不会修改源实例。

使用 [n8n CLI](../../../connect/n8n-cli.md)：

```bash
n8n-cli package export --workflow-id=<workflow-id> --output=triage.n8np
```

也可以直接调用端点：

```bash
curl -X POST 'https://n8n.example.com/api/v1/n8n-packages/export' \
	-H "X-N8N-API-KEY: <your-api-key>" \
	-H 'Content-Type: application/json' \
	-d '{"workflowIds": ["<workflow-id>"]}' \
	-o triage.n8np
```

完整的请求和响应结构，请参阅[端点参考](../../../connect/n8n-api/api-reference.md)中的 `N8nPackage` 部分。

## 选择导出内容 <a id="choose-what-to-export"></a>

至少传入一个 ID。要指定多个 ID，请重复使用对应标志，不支持逗号分隔形式。

```bash
# Two workflows
n8n-cli package export --workflow-id=wf7Kq2 --workflow-id=wf9Zx1 --output=triage.n8np

# A folder, and everything nested inside it
n8n-cli package export --folder-id=fdInProg --output=in-progress.n8np

# A workflow and a folder together
n8n-cli package export --workflow-id=wf7Kq2 --folder-id=fdInProg --output=mixed.n8np

# Two whole projects
n8n-cli package export --project-id=prTeam9 --project-id=prOps3 --output=teams.n8np
```

工作流 ID 和文件夹 ID 可以组合使用。项目软件包的结构不同，因此项目 ID 不能与前两者组合。混合这两组 ID 会返回 `400`。

导出文件夹时，始终包含其嵌套文件夹和工作流。如果指定的工作流也位于指定文件夹中，它只会在该文件夹中导出一次。

n8n 对每组 ID 的上限为 300 个。这是每组的限制，因此一次导出可以指定 300 个工作流和 300 个文件夹。超出上限会返回 `400`，CLI 不会在发送请求前检测此问题。

空项目仅导出项目元数据，清单中没有 `workflows` 列表。

## 导出标志 <a id="export-flags"></a>

| 标志 | 说明 |
|------|-------------|
| `--workflow-id`、`-w` | 要包含的工作流 ID。重复使用可导出多个。 |
| `--folder-id` | 要包含的文件夹 ID，及其中所有嵌套内容。重复使用可导出多个。 |
| `--project-id`、`-p` | 要包含的项目 ID。重复使用可导出多个。不能与 `--workflow-id` 或 `--folder-id` 组合。 |
| `--output`、`-o` | 软件包的输出文件，默认为当前目录下的 `export.n8np`。 |
| `--include-variable-values` | `true`（默认）或 `false`。控制是否打包变量值。请参阅[变量值](#variable-values)。 |
| `--include-tags` | `true`（默认）或 `false`。控制是否打包所导出工作流的标签。 |
| `--missing-workflow-dependency-policy` | `fail`（默认）、`include-in-package` 或 `reference-only`。控制 n8n 如何处理未指定的子工作流。请参阅[子工作流依赖](#sub-workflow-dependencies)。 |

{% hint style="info" %}
本文中的 `n8n-cli package export` 标志使用 kebab-case（短横线命名）。`--help` 会显示等效的 camelCase（驼峰命名）名称（`--workflowId`、`--includeTags`、`--missingWorkflowDependencyPolicy`），错误消息也使用这些名称。两种写法都有效。
{% endhint %}

`--output` 会覆盖已有文件，且不发出警告。导出失败时，n8n 不会写入任何内容，因此原有文件会保留。

## 子工作流依赖 <a id="sub-workflow-dependencies"></a>

工作流调用的子工作流，或指定的错误工作流，都属于软件包依赖。当某个依赖不在指定的 ID 集合中时，`--missing-workflow-dependency-policy` 决定 n8n 的处理方式。

| 值 | 行为 |
|-------|--------------|
| `fail`（默认） | 中止导出并列出缺失内容，最多列出 20 个 ID |
| `include-in-package` | 遍历依赖图，将缺失的工作流添加到软件包 |
| `reference-only` | 不包含这些工作流，将其记录在 `requirements.workflows` 中，要求目标实例已存在这些工作流 |

**`fail` 和 `include-in-package` 会追踪整条依赖链。** 如果工作流 A 调用 B，B 调用 C，即使导出 A 和 B，仍会因缺少 C 而失败。只有 `reference-only` 在直接引用处停止，因为它假定被引用工作流及其自身依赖已经同时存在于目标实例。

**错误工作流也计为依赖。** 如果工作流在 **Settings > Error workflow（设置 > 错误工作流）** 下配置了错误工作流，默认导出会失败，除非也包含该错误工作流。例外是字面值 `DEFAULT` 和通过表达式指定的错误工作流，n8n 会忽略这两种情况。

n8n 不会将通过表达式设置的引用视为依赖，也不会在导入时改写此类引用。只有静态引用会被识别。

常见的环境推进场景有两种形式：

```bash
# Name the dependency yourself
n8n-cli package export --workflow-id=wf7Kq2 --workflow-id=wf9Zx1 --output=triage.n8np

# Or let n8n work it out
n8n-cli package export --workflow-id=wf7Kq2 \
	--missing-workflow-dependency-policy=include-in-package \
	--output=triage.n8np
```

{% hint style="warning" %}
导出项目时，`include-in-package` 可能引入未指定的项目。属于其他项目的依赖会将该项目的基本结构和文件夹链带入归档。CLI 摘要统计的是指定项目数，而不是归档中的项目数，因此这种情况下会少计。请解压归档或阅读清单，确认实际导出了哪些内容。
{% endhint %}

## 变量值 <a id="variable-values"></a>

默认情况下，导出工作流引用的变量会连同值一起迁移。使用 `--include-variable-values=false` 时，变量仍会迁移，并仍出现在清单和 `requirements.variables` 中，但省略 `value` 字段。

禁用变量值会改变导入行为：目标实例会创建空变量，而不是填入值。这不会阻止变量本身迁移。

打包变量值需要 `variable:list` API 密钥权限范围，但仅在导出工作流至少引用一个变量时才需要。缺少此权限时，导出返回 `403`，提示添加权限或设置 `--include-variable-values=false`。所有有权创建 API 密钥的角色都可以分配 `variable:list`，因此此处出现 `403`，表示所用密钥在创建时未分配该权限。

n8n 会扫描节点参数和工作流设置中的 `$vars.NAME`、`$vars['NAME']` 和 `$vars["NAME"]`，查找变量引用。

如果同一个变量名称在同一软件包中会解析到两个不同变量，导出就会被阻止，因为软件包只能携带其中一个。

## 标签 <a id="tags"></a>

使用 `--include-tags=false` 时，不迁移任何标签数据：导出的工作流不带标签引用，归档中也没有 `tags/` 目录。

这对导入的影响比表面上更大。工作流只要带有标签列表，即使列表为空，也会用该列表精确覆盖目标工作流的标签。完全不带标签列表的工作流则会保留目标的标签。因此，要保留目标上的现有标签，应使用 `--include-tags=false`。

如果源实例设置了 `N8N_WORKFLOW_TAGS_DISABLED=true`，所有导出都会省略标签，不受此标志影响，也不会发出警告。

## 响应中的信息 <a id="what-the-response-tells-you"></a>

导出成功时，以 `application/gzip` 返回归档，并通过 `X-N8n-Export-Counts` 响应头提供各类实体的实际数量：

```
X-N8n-Export-Counts: {"workflows":2,"folders":0,"credentials":1,"dataTables":1,"variables":1,"tags":1}
```

这些数量统计的是展开文件夹内容并自动包含子工作流后，最终进入归档的内容，因此不一定等于指定的 ID 数量。响应头没有 `projects` 键。CLI 根据此响应头输出摘要。

`credentials` 统计打包的凭据文件，因此无权读取的凭据只会记录为需求，不计入数量。`variables` 统计打包的变量文件，而不是引用的名称数量。

无论导出什么，下载文件名始终为 `export.n8np`。CLI 则写入 `--output`。

## 权限 <a id="permissions"></a>

导出需要具有以下权限范围的 API 密钥：

* 指定工作流或文件夹 ID 时，需要 `workflow:export`。文件夹使用工作流权限范围。
* 指定项目 ID 时，需要 `project:export`。
* 打包变量值且工作流至少引用一个变量时，需要 `variable:list`。

除 API 密钥权限外，只能导出你有权读取的内容。n8n 构建软件包时，会检查你对每个工作流、文件夹、项目和凭据的访问权限。无权读取的凭据会记录为需求，而不是打包。

导出不需要任何许可证功能。完整矩阵请参阅[限制和权限](limits-and-permissions.md)。

## 错误 <a id="errors"></a>

| 状态 | 原因 |
|--------|-------|
| `400` | 请求的工作流、文件夹或项目不存在，或你无权访问；也可能是混合了 ID 组、未传入 ID、某组超过 300 个 ID，或 `--missing-workflow-dependency-policy=fail` 阻止了导出 |
| `403` | API 密钥缺少所需权限范围 |

实体不存在和无权访问都会返回相同的 `400` 及相同消息，因此不能利用导出探测某个 ID 是否存在。导出不会返回 `404`。

错误响应体仅包含 `message`。

## 事件 <a id="events"></a>

每次导出都会在日志流和遥测路径上发出事件，便于审计哪些内容离开了实例。

| 事件 | 发出时机 |
|-------|--------------|
| `n8n.audit.n8n-package.export.success` | 导出成功 |
| `n8n.audit.n8n-package.export.failed` | 导出失败 |

成功事件包含用户，以及最终进入软件包的 `workflowIds`、`folderIds` 和 `projectIds`，因此反映的是文件夹内容和自动包含的子工作流，而不只是指定内容。各列表仅在非空时出现。

失败事件包含用户、请求的 ID，以及 `reason`，其值为 `access-denied`、`entity-not-found`、`blocked` 或 `validation`。

日志流事件携带 ID。
遥测事件则发送数量，以保持数据匿名。

## 继续阅读 <a id="read-next"></a>

* [导入软件包](import-a-package.md)：将文件迁移到另一个实例。
* [软件包格式](package-format.md)：了解归档中的内容。
* [限制和权限](limits-and-permissions.md)：了解大小上限和完整的权限范围矩阵。

## 相关资源 <a id="related-resources"></a>

* [n8n 软件包](./)
* [软件包格式](package-format.md)
* [导入软件包](import-a-package.md)
* [导入机制](how-import-works.md)
* [限制和权限](limits-and-permissions.md)
