---
description: n8n 如何在写入前检查软件包、按什么顺序写入，以及如何解析凭据、变量、数据表、标签、文件夹和项目。
status: preview
layout:
  description:
    visible: false
tags:
- tag: preview
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 导入机制 <a id="how-import-works"></a>

{% hint style="info" %}
**预览状态**

n8n 软件包处于预览阶段，导入行为在未来版本中可能发生变化。
{% endhint %}

本页介绍调用[导入](import-a-package.md)后，n8n 如何处理 [n8n 软件包](README.md)：如何判断能否继续导入，以及如何解析各类实体。

## 先检查全部内容，再写入 <a id="check-everything-then-write"></a>

导入分为两个阶段。首先，n8n 制定计划：读取软件包，确定对每个实体的处理方式，并收集所有无法继续导入的原因。然后检查这些原因，以及许可证、权限和配额要求。只有不存在任何阻碍时，才开始写入。

**一次返回全部问题。** 导入被拒绝时，会在 `issues` 数组中一起返回全部原因，而不是遇到第一个就停止。这样可以一次修复流水线，而无需每遇到新错误就重新导入。

**被拒绝的导入不会写入任何内容。** 如果导入被阻止，就不会创建或修改工作流、文件夹、凭据、数据表、变量或标签。

{% hint style="warning" %}
导入没有回滚机制。n8n 不会用数据库事务包裹整个导入，因此“被拒绝的导入不写入内容”这一保证仅涵盖可以预见的问题，不包括所有可能的故障。如果写入过程中发生意外，例如数据库连接断开，已写入的内容会保留在实例中，之后也不会清理。预检查使这种情况少见，但无法完全排除。
{% endhint %}

导入绝不会删除工作流、文件夹、项目、数据表或标签。使用 `--data-table-schema-conflict-policy=overwrite` 时，可能删除数据表中的列。请参阅[数据表](#data-tables)。

## 写入顺序 <a id="write-order"></a>

在同一个项目内，n8n 按固定顺序写入：

```
tags → folders → credentials → data tables → workflows → variables → publish
```

标签最先写入，因为关联标签是写入工作流的一部分。变量最后写入，因为覆盖变量是唯一会改变已有数据的步骤，且之前的步骤均不读取变量：`$vars` 在运行时按名称解析，而不是在导入时解析。

发布是最后的独立步骤，要等软件包内每个项目都写入后才进行。这是必要的，因为工作流调用的所有内容存在后，才能发布。

工作流内容按清单中的顺序写入。发布步骤则根据子工作流依赖图排序，先发布叶子节点，因为子工作流尚未发布时，父工作流发布会失败。循环依赖中的工作流最后发布。

对于项目软件包，n8n 先为每个项目制定计划，检查整个软件包，创建项目基本结构，再依次写入各项目内容，最后统一发布一次。

## 改写引用 <a id="rewriting-references"></a>

导入工作流的引用必须指向目标实例上的实体。n8n 会在过程中建立源 ID 到目标 ID 的映射，并据此改写四类内容：

* 节点上的凭据 ID。
* **Execute Workflow**、**Call n8n Workflow Tool** 和 **Workflow Retriever** 节点上的子工作流 ID，但仅限于从列表中选择工作流，而非通过表达式指定的情况。
* 工作流设置中的错误工作流。
* 工作流设置中的调用方允许列表，逐项改写。无法映射的 ID 保持原样。

两类内容不会改写：通过表达式设置的引用保持不变，因为 n8n 无法知道其求值结果；子工作流节点上缓存的显示名称也不会更新，因此重新映射后，编辑器可能仍显示旧名称，直到再次打开该节点。

## 凭据 <a id="credentials"></a>

软件包不携带凭据数据，因此每个凭据引用都必须在目标实例上解析。n8n 按以下顺序解析：

1. 为该凭据提供了显式[绑定](import-a-package.md#bindings)时，先使用绑定。
2. 否则使用 `--credential-matching-mode` 规则。
3. 仍未解析时，由 `--credential-missing-mode` 决定创建空占位凭据，还是拒绝导入。

无论走哪条路径，n8n 都会检查类型。凭据类型错误时会拒绝导入，并同时告知节点需要的类型与凭据的实际类型。显式绑定也适用此规则。

### 哪些凭据可作为候选 <a id="which-credentials-are-candidates"></a>

n8n 只考虑你有权读取且目标项目有权使用的凭据，以及全局凭据。在任何模式下，无权读取的凭据都不会成为候选，包括 `id-only`。这通常是凭据 ID 相同却未能匹配的原因。

### 如何选择匹配项 <a id="how-a-match-is-chosen"></a>

`id-only` 只检查是否找到对应 ID。`name-and-type` 和 `type-only` 可能找到多个候选，因此 n8n 按严格优先级选择：

1. 属于目标项目的凭据。
2. 共享到目标项目的凭据。
3. 全局凭据。

这些是严格的优先级，而不是评分系统。只要存在属于目标项目的候选，n8n 就不会考虑共享或全局凭据。在胜出的优先级中，选择最近更新的凭据；如果两个凭据的更新时间相同，则选择 ID 最小的。

共享凭据也可以作为候选。跳过它们会破坏常见的环境推进场景，而且无论如何，导入用户都需要凭据的读取权限。

### 占位凭据 <a id="placeholder-credentials"></a>

使用默认 `--credential-missing-mode=create-stub` 时，n8n 无法解析的引用会在目标项目中变成空凭据，名称沿用包内凭据名称。工作流会被导入，n8n 会在 `credentials.stubbed` 下报告该凭据，并返回新绑定，便于下次复用。

无论发布策略如何，使用占位凭据的工作流都不会发布。请先补充凭据信息，再发布工作流。

即使使用 `create-stub`，部分凭据问题仍会拒绝导入，因为占位凭据无法解决：实例未安装对应凭据类型、绑定指向错误类型的凭据，或绑定指定了软件包中未声明的凭据。

## 变量 <a id="variables"></a>

变量按名称匹配，不按 ID 匹配，因为 `$vars.<name>` 在运行时按名称解析。n8n 与运行中的工作流一样，先查找目标项目，再查找全局范围。没有可移植的 ID，因此软件包需求只记录名称。

导出时，同名变量同时存在于项目和全局范围时，优先使用项目值。如果同一名称在软件包中会解析到两个不同变量，则拒绝导出。

导入时，无法解析的变量由 `--variable-missing-mode` 处理，可解析的变量由 `--variable-conflict-policy` 处理。没有需要更改的内容时，即包内没有变量值或值已相同，这两种策略都不会修改已解析变量。

写入变量需要支持变量的许可证。创建变量还需要创建权限范围，且实例变量数量尚有余量。覆盖变量需要更新权限范围，但不消耗额外数量，因为该变量已计入上限。上限同时统计实例上的所有全局变量和项目变量。如果新变量会超出上限，n8n 会在写入任何内容前拒绝导入。

既不创建也不覆盖变量的导入，不需要这些条件。在默认 `--variable-conflict-policy=keep-existing` 下，所有变量名称均可解析的导入都属于这种情况。

使用 `--variable-conflict-policy=overwrite` 时，如果包内多个项目解析到同一变量，却为该变量携带不同值，则会拒绝导入。一个变量不能同时保存两个值，因此 n8n 不会静默采用最后一次写入。

## 数据表 <a id="data-tables"></a>

只有表结构随包迁移。数据行在导出或导入时都不会迁移，因此导入创建的新表最初为空。

在目标项目内按 ID 匹配表，不按名称匹配。新建表保留源 ID。

`--data-table-schema-conflict-policy` 决定匹配表的结构与软件包不同时如何处理：

| 策略 | 行为 |
|--------|--------------|
| `keep-existing`（默认） | 不修改目标表。如果包内某列在目标上缺失或类型不同，则拒绝导入。允许目标表有自身额外的列 |
| `fail` | 与 `keep-existing` 相同，但目标有额外列时也拒绝导入 |
| `overwrite` | 修改目标表，使其与软件包一致。可以添加、重命名、删除列（破坏性操作）、更改列类型（破坏性操作）、调整列顺序，以及重命名表 |
| `overwrite-non-destructive` | 进行与 `overwrite` 相同的修改，但在更改具有破坏性时停止导入，并报告这些更改。不写入任何内容 |

`keep-existing` 和 `fail` 都不会在目标表上添加或重命名列。缺失列会拒绝导入，源端重命名的列也包括在内。要应用重命名，使用 `overwrite` 或 `overwrite-non-destructive`。不会比较列顺序和表名称；比较列名称时区分大小写。

破坏性更改是指删除列或更改列类型，这些列中的值会被移除。其他列的数据保留。重命名列不具有破坏性，会保留列值。两种 `overwrite` 策略下，更改都会影响使用该表的所有工作流。

n8n 2.44.0 之前导出的软件包不携带列 ID。对于这些软件包，两种 `overwrite` 策略都会将重命名列视为先删除再添加，因此属于破坏性更改，并会作相应标记。

如果表 ID 已存在于实例任意位置（包括其他项目），或目标项目中已有同名表，创建表也会失败。使用 `overwrite` 策略重命名表时，如果新名称在目标项目中已被占用，也会失败。

## 标签 <a id="tags"></a>

n8n 中的标签是全局的，名称在整个实例中唯一。n8n 按源 ID 匹配标签，不按名称匹配，因为只有跟踪稳定 ID，才能区分重命名与删除后重建。新建标签采用源 ID。

冲突分为两种：

* **重命名差异**：ID 与目标标签相同，但名称不同，说明有人在某个实例上重命名了它。
* **名称冲突**：目标上没有该 ID，但其他标签已占用该名称。这在标签独立创建、ID 互不关联的已有实例上很常见。

`--tag-conflict-policy=rename` 会处理这两种情况：将名称已变化的标签重命名为包内名称；对于名称冲突，将已有标签改用包内 ID，保留名称及所有已关联的打标内容。唯一仍会拒绝的情况是，需要重命名的标签的新名称已被第三个标签占用。

更新工作流时，n8n 会用软件包中的标签列表精确替换目标标签，包括空列表。完全不带标签列表的工作流则保留目标标签。丢弃的标签会在写入前被过滤，因此，如果某个带标签工作流的包内标签全部被丢弃，更新会清空其标签。要保留目标标签，导出时使用 `--include-tags=false`。

导入不会删除标签。如果目标实例禁用了标签，所有标签处理都会被静默跳过，绝不会因此导致导入失败。

## 文件夹和项目 <a id="folders-and-projects"></a>

`--folder-conflict-policy=merge` 会复用按 ID 匹配到的文件夹，并将包内内容合并进去。已有文件夹保留原名称，合并不会导致重命名。注意，响应中为合并文件夹报告的是包内名称，而不是目标上的实际名称。

无论策略如何，两类文件夹冲突都会拒绝导入，因为它们意味着移动文件夹，而不是合并内容：文件夹 ID 已存在于其他项目；或已有文件夹的父级与导入预定位置不同。

对于项目软件包，n8n 先创建项目基本结构，再对每个项目运行相同流程。如果包内项目 ID 匹配到目标上的个人项目，导入会被拒绝并返回 `403`，冲突策略也无法合并这种情况。

## 节点类型 <a id="node-types"></a>

n8n 会从工作流本身推导软件包所需的节点类型，不会信任清单中的 `requirements.nodeTypes` 列表。清单可以加快导入，但不能让导入作出错误判断。

在默认 `--missing-node-type-mode=fail` 下，如果软件包使用实例没有的节点类型或版本，会在写入任何内容前拒绝导入，并列出每个缺失类型及使用它们的工作流。使用 `import-anyway` 时，这些工作流会被导入，但不会发布。

## 发布结果 <a id="publishing-outcomes"></a>

响应中的每个工作流都包含 `publishing.state`：

| 状态 | 含义 |
|-------|---------|
| `published` | 工作流已上线 |
| `unpublished` | 工作流未上线，符合策略预期 |
| `unchanged` | 未尝试发布或已跳过发布。已有线上版本继续运行 |
| `blocked` | n8n 拒绝发布，`blockedReason` 说明原因 |
| `failed` | 已尝试发布但失败，`error` 说明原因 |

`blockedReason` 的值为 `stub-credential` 或 `missing-node-type`。同时被这两个原因阻止时，工作流会报告 `missing-node-type`，因为该原因意味着它实际无法运行。

`blocked` 表示没有任何版本在线运行。如果工作流已有已发布版本，但新版本无法发布，则会返回 `unchanged`，并附带 `skippedPublishReason`，旧版本继续处理流量。因此，“从不发布”指刚导入的版本，而不是整个工作流。

发布失败不会导致整个导入失败。工作流仍会导入，响应会说明其未上线。

### Webhook 路径冲突 <a id="webhook-path-conflicts"></a>

两个工作流不能以相同 HTTP 方法注册相同的 Webhook 路径。如果软件包会发布两个使用相同路径的工作流，第一个会发布，第二个会报告 `failed`，消息为 `There is a conflict with one of the webhooks.`。导入本身仍然成功。如果路径已被实例上的已发布工作流占用，也会出现相同情况。

n8n 仅比较可按字面读取的路径：节点必须已启用，路径必须是普通值而非表达式，且不能包含路径参数。表达式生成的路径、带参数的路径，以及 n8n 为各工作流添加前缀的 Webhook，不会以这种方式产生冲突。不同 HTTP 方法可以使用相同路径。

## 为何拒绝导入 <a id="why-an-import-is-refused"></a>

导入可能因 12 类原因被阻止。每项都会出现在 `issues` 数组中，带有 `type`；部分还带有 `kind`，进一步细分原因：

| 类型 | 子类 | 含义 |
|------|-------|---------------|
| `workflow-conflict` | | 工作流已存在于目标，且 `--workflow-conflict-policy` 为 `fail` |
| `workflow-id-conflict` | | 使用 `--workflow-id-policy=source` 时，该工作流 ID 已在实例某处使用，包括其他项目及已归档工作流 |
| `workflow-folder-conflict` | | 已有工作流所在文件夹与导入预定位置不同。即使使用 `--workflow-conflict-policy=skip` 也会拒绝导入 |
| `project-conflict` | `fail-policy` | 项目已存在，且 `--project-conflict-policy` 为 `fail` |
| `folder-conflict` | `parent-mismatch`、`id-in-other-project`、`fail-policy` | 无论采用何种策略，前两类都会拒绝导入 |
| `credential-unresolved` | `not_found`、`unknown_type`、`source_not_found`、`type_mismatch` | 只有 `not_found` 能通过占位凭据解决 |
| `data-table-unresolved` | `missing`、`id-conflict`、`name-conflict`、`schema-incompatible`、`module-disabled`、`permission-denied` | 使用 `overwrite-non-destructive` 时，`schema-incompatible` 表示某项更改会删除列或更改列类型，并列出这些列 |
| `tag-unresolved` | `rename-drift`, `name-collision`, `invalid-name`, `invalid-id`, `permission-denied` | |
| `variable-unresolved` | | 引用变量无法解析，且 `--variable-missing-mode` 为 `must-preexist` |
| `variable-conflict` | | 已解析变量的值不同，且 `--variable-conflict-policy` 为 `fail` |
| `variable-limit-exceeded` | | 新变量会超出实例的变量数量上限 |
| `missing-node-type` | | 使用 `--missing-node-type-mode=fail` 时，工作流使用了实例没有的节点类型或版本 |

HTTP 状态取决于问题类型。只要任意问题属于冲突，就返回 `409`：包括工作流、项目、文件夹或变量冲突，数据表 ID 或名称冲突，以及标签重命名差异或名称冲突。其他问题返回 `422`。混合问题中只要包含一个冲突，整个响应就返回 `409`。

部分失败会单独报告，而不与其他问题合并，因为它们会在 n8n 制定计划前阻止流程：缺少许可证功能、缺少 API 密钥权限范围，以及软件包格式错误。

无权创建标签，或无权创建、修改数据表时，不会返回 `403`，而是作为 `permission-denied` 阻止问题返回，并注明所需权限范围。

## 继续阅读 <a id="read-next"></a>

* [导入软件包](import-a-package.md)：查看本页涉及的选项。
* [限制和权限](limits-and-permissions.md)：了解导入检查的许可证功能、权限范围和配额。
* [软件包格式](package-format.md)：了解 n8n 所读取文件中的内容。

## 相关资源 <a id="related-resources"></a>

* [n8n 软件包](./)
* [软件包格式](package-format.md)
* [导出软件包](export-a-package.md)
* [导入软件包](import-a-package.md)
* [限制和权限](limits-and-permissions.md)
