---
description: 软件包导出和导入的大小限制、许可证功能、API 密钥权限范围，以及 n8n 发出的事件。
status: preview
layout:
  description:
    visible: false
tags:
- tag: preview
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 限制和权限 <a id="limits-and-permissions"></a>

{% hint style="info" %}
**预览状态**

n8n 软件包处于预览阶段，这些限制和要求在未来版本中可能发生变化。
{% endhint %}

本页列出[软件包](README.md)导出和导入的约束：大小上限、许可证功能、API 密钥权限范围及可观测性。

## 软件包大小限制 <a id="package-size-limits"></a>

四个环境变量限定导入接受的内容，避免体积很小的归档解压后异常庞大，影响实例：

| 变量 | 默认值 | 限制内容 |
|----------|---------|--------------|
| `N8N_IMPORT_MAX_UNCOMPRESSED_BYTES` | `314572800`（300 MiB） | 归档内所有文件解压后的总大小，在读取归档时检查 |
| `N8N_IMPORT_MAX_ENTRY_BYTES` | `5242880`（5 MiB） | 任意单个文件解压后的大小 |
| `N8N_IMPORT_MAX_ENTRIES` | `5000` | 归档条目数，包括目录 |
| `N8N_IMPORT_MAX_PATH_LENGTH` | `1024` | 任意条目路径的字符长度 |

超出任意一项限制都会返回 `400`，并说明触及了哪个上限。

{% hint style="warning" %}
上传本身由 [`N8N_PAYLOAD_SIZE_MAX`](../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints.md)单独限制，默认 16 MiB，并非软件包专用设置。该上限针对压缩文件，因此通常最先触及：只有压缩后小于 16 MiB 的软件包，解压大小才可能达到 300 MiB。

导入大软件包时，请先提高 `N8N_PAYLOAD_SIZE_MAX`。只提高导入限制不会改变结果。超过上传上限会返回 `413`。
{% endhint %}

导入请求还受几项不可配置的限制：每次请求只能包含一个文件，每个选项字段最多 64 KB，这也是 `--bindings` 值的实际大小上限。

导出时，每组最多 300 个 ID，工作流、文件夹和项目 ID 分别计数。请参阅[选择导出内容](export-a-package.md#choose-what-to-export)。

## 归档验证 <a id="archive-validation"></a>

除大小限制外，n8n 还会拒绝结构不符合软件包要求的归档，均返回 `400`：

* `manifest.json` 必须是归档中的第一个文件。
* 条目路径只能包含字母、数字、`.`、`_`、`/` 和 `-`，因此包含非 ASCII 路径的归档会被拒绝。
* 路径必须是相对路径，不能越出软件包根目录，且必须唯一。
* 条目必须是文件或目录，不接受符号链接和硬链接。
* `packageFormatVersion` 必须完全匹配。请参阅[版本兼容性](package-format.md#version-compatibility)。

清单未引用的文件会被忽略，但仍计入大小和条目数限制。

## 许可证功能 <a id="license-features"></a>

软件包本身不需要专门的许可证功能。n8n Cloud 和自托管 n8n 的所有套餐和版本均可使用，导出完全不需要任何许可证功能。

导入会检查两项许可证功能，且仅针对实际要进行的操作：

* **文件夹**：只要软件包包含文件夹就需要。根据包内声明判断，因此即使所有文件夹都已存在于目标上，也仍适用。
* **变量**：仅在导入实际会创建或覆盖变量时需要。如果软件包中的变量全部可以在目标上解析，就不会写入变量，因此不需要相应许可证或变量权限范围。

导入项目软件包还需要支持团队项目的许可证。

缺少许可证功能会返回 `403`，并指出缺失功能。

软件包只能通过 [n8n API](../../../connect/n8n-api/README.md) 访问，因此实例必须启用 API。要阻止软件包进入或离开实例，可以[禁用公共 API](../../../deploy/host-n8n/configure-n8n/security/disable-the-public-api.md)，或不签发具有 `workflow:export` 和 `workflow:import` 权限范围的 API 密钥。

## API 密钥权限范围 <a id="api-key-scopes"></a>

两个端点都使用 API 密钥进行身份验证，导入会归属于该密钥所属的用户。

### 导出 <a id="export"></a>

| 权限范围 | 需要的情况 |
|-------|-------------|
| `workflow:export` | 指定工作流或文件夹 ID。文件夹使用工作流权限范围 |
| `project:export` | 指定项目 ID |
| `variable:list` | 打包变量值，且工作流至少引用一个变量 |

### 导入 <a id="import"></a>

| 权限范围 | 需要的情况 |
|-------|-------------|
| `workflow:import` | 始终需要 |
| `folder:create` 和 `folder:update` | 软件包包含文件夹 |
| `project:create` 和 `project:update` | 属于项目软件包，无论是否创建项目 |
| `dataTable:create` | 软件包引用数据表，且 `--data-table-missing-mode` 为 `create` |
| `dataTable:update` | 导入实际通过 `--data-table-schema-conflict-policy=overwrite` 或 `overwrite-non-destructive` 修改数据表 |
| `variable:create` | 导入实际创建变量 |
| `variable:update` | 导入实际覆盖变量 |
| `tag:create` | 导入实际创建标签 |
| `tag:update` | 导入实际重命名或协调标签 |

`dataTable:update` 和最后四项根据导入实际将写入的内容判断，因此，如果引用的标签或变量都已匹配，就不需要对应权限。其余权限根据包内声明判断，因此即使所有引用表都已存在，也仍需要 `dataTable:create`。

成员角色的 API 密钥不能导入项目软件包、不能导入包含文件夹的软件包，也不能创建或覆盖变量：`project:create`、`project:update`、`folder:create`、`folder:update`、`variable:create` 和 `variable:update` 属于所有者和管理员权限范围。成员可以具有 `workflow:export`、`workflow:import`、`project:export`、`variable:list`、`dataTable:create`、`dataTable:update`、`tag:create` 和 `tag:update`，因此成员可以在导出时打包变量值。

API 密钥权限范围是在你自身权限之外增加的检查，不会代替自身权限。导出只能读取你有权读取的内容，因此 n8n 会检查你对每个工作流、文件夹、项目和凭据的访问权限。导入则检查你向目标项目写入的权限。无权读取的凭据会记录为需求，而不是打包，因此即使只能查看实例的部分内容，生成的软件包也会清楚说明目标必须提供哪些资源。

无权创建标签，或无权创建、修改数据表时，会报告为阻止问题，而不是 `403`。请参阅[为何拒绝导入](how-import-works.md#why-an-import-is-refused)。

## 变量数量限制 <a id="variable-limit"></a>

实例的变量数量有上限，全局变量和项目变量一起计算。如果新增变量会超过上限，n8n 会在写入任何内容前拒绝导入。问题信息会说明上限、剩余数量、导入想要创建的数量，以及具体变量。

只有新变量消耗剩余数量。覆盖已有变量不消耗余量，因为该变量已计入上限。n8n 还会按实际将创建的内容计数，因此，包内多个项目共同需要的同一个全局变量只计一次。

## 事件 <a id="events"></a>

导出和导入都会在日志流和遥测路径上发出事件，便于审计谁迁移了什么内容。

| 事件 | 发出时机 |
|-------|--------------|
| `n8n.audit.n8n-package.export.success` | 导出成功 |
| `n8n.audit.n8n-package.export.failed` | 导出失败 |
| `n8n.audit.n8n-package.import.success` | 导入成功 |
| `n8n.audit.n8n-package.import.failed` | 导入失败 |

为日志流目标订阅这四类事件，即可跟踪进入或离开实例的每个软件包。日志流事件携带实体 ID，对应遥测事件则携带各类实体数量。失败事件将原因分为 `access-denied`、`entity-not-found`、`blocked` 或 `validation`。

各事件载荷的内容，请参阅导出页面的[事件](export-a-package.md#events)和导入页面的[事件](import-a-package.md#events)部分。

## 继续阅读 <a id="read-next"></a>

* [导出软件包](export-a-package.md)和[导入软件包](import-a-package.md)：查看这些限制适用的选项。
* [导入机制](how-import-works.md)：了解许可证和权限范围检查如何融入导入流程。

## 相关资源 <a id="related-resources"></a>

* [n8n 软件包](./)
* [软件包格式](package-format.md)
* [导出软件包](export-a-package.md)
* [导入软件包](import-a-package.md)
* [导入机制](how-import-works.md)
