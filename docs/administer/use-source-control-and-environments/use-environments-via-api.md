---
description: 使用 n8n 公共 API，在环境间预览、推送和拉取源代码管理中的更改。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 通过公共 API 以编程方式使用环境 <a id="use-environments-programmatically-with-the-public-api"></a>

无需打开 n8n 界面，就能通过公共 API 在脚本和流水线中管理 n8n 环境，从而自动将更改推进到不同实例。例如，按计划或作为 CI/CD 流水线的一部分，将工作从开发实例迁移到生产实例。

本页介绍源代码管理 API 端点如何协同工作，假定你已将实例连接到 Git，并了解界面中的推送和拉取行为。相关背景请参阅[推送和拉取](push-and-pull-changes.md)及[在环境间复制工作](move-work-between-environments.md)。

{% hint style="info" %}
**功能可用范围**

源代码管理的 `status` 和 `push` 端点自 n8n `2.39.0` 版本起可用。
* `GET /api/v1/source-control/status`
* `POST /api/v1/source-control/push`

环境是一项 Enterprise 功能。

译注：本页原文将环境功能列为 Enterprise 功能，而同一版本源代码管理章节的功能可用范围片段列出 Business 和 Enterprise。此处保留原文并提示差异，不据此确定某个方案是否可使用这些 API 端点。
{% endhint %}

## 端点 <a id="the-endpoints"></a>

公共 API 提供三项源代码管理操作：

| 端点 | 方法 | 用途 |
|----------|--------|--------------|
| `/source-control/status` | `GET` | 预览实例与 Git 之间任一方向的待处理更改。 |
| `/source-control/push` | `POST` | 将本地更改提交并推送到已连接的 Git 分支。 |
| `/source-control/pull` | `POST` | 将已连接 Git 分支中的更改获取到实例。 |

`push` 和 `pull` 分别对应源代码管理菜单的 **Push**（推送）和 **Pull**（拉取）按钮。`status` 对应界面在推送、拉取弹窗中确认操作前显示的文件列表。API 将其作为独立端点提供，使脚本也能进行界面内的同类审核。

完整的请求和响应结构请参阅[端点参考](../../connect/n8n-api/api-reference.md)。

### 身份验证与作用域 <a id="authentication-and-scopes"></a>

每个请求都需要通过 `X-N8N-API-KEY` 请求头发送 API 密钥。在 Enterprise 方案中，可以为每个密钥仅授予所需的最小作用域：

| 作用域 | 授予的权限 |
|-------|--------|
| `sourceControl:pull` | 将更改拉取到实例。 |
| `sourceControl:push` | 将本地更改推送到 Git。 |
| `sourceControl:read` | 读取待处理更改的状态。 |

以这种方式限定密钥作用域，可以约束同步方向。对于只应接收更改的生产实例，仅授予密钥 `sourceControl:pull`，使其无法推送。如果还希望该密钥能在拉取前预览传入更改，则同时添加 `sourceControl:read`，以便调用 `status`。

## 先检查状态，再执行操作 <a id="check-the-status-then-act"></a>

不要盲目推送。`push` 要求提供 `fileNames` 数组，且只提交其中列出的文件，因此应先调用 `status`，查看哪些文件符合条件。

步骤如下：

1. 调用 `status`，查看可包含的文件。
2. 决定包含哪些文件：列出全部文件以推送所有内容，或选择子集以推送部分内容。
3. 根据选中的文件构建 `fileNames`，每个文件仅保留 `id` 和 `type`。
4. 携带该数组调用 `push`。

调用 `status` 时，通过 `direction` 查询参数选择要预览的方向：

```curl
curl --request GET \
	--location '<YOUR-INSTANCE-URL>/api/v1/source-control/status?direction=push' \
	--header 'X-N8N-API-KEY: <YOUR-API-KEY>'
```

响应中的每个文件都包含 `id`、`name`、`type`（例如 `workflow` 或 `credential`）和 `status`（例如 `modified` 或 `new`）：

```json
{
	"data": [
		{
			"id": "1a2b3c",
			"name": "Daily sales report",
			"type": "workflow",
			"status": "modified",
			"file": "workflows/1a2b3c.json"
		}
	]
}
```

## 从开发环境推进到只读生产环境的流程 <a id="promotion-flow-from-development-to-read-only-production"></a>

这是一种常见配置：在开发实例中更改，再将更改推进到只接收更新的生产实例。此示例使用两个实例共享的单个 Git 分支。

为每个实例提供带有限定作用域的 API 密钥：

* 开发实例的 API 密钥具有 `sourceControl:read` 和 `sourceControl:push`。
* 生产实例的 API 密钥具有 `sourceControl:read` 和 `sourceControl:pull`。

**1. 预览开发环境中的更改。** 调用 `status` 并设置 `direction=push`，查看 n8n 将提交哪些内容：

```curl
curl --request GET \
	--location '<DEV-INSTANCE-URL>/api/v1/source-control/status?direction=push' \
	--header 'X-N8N-API-KEY: <DEV-API-KEY>'
```

**2. 从开发环境推送到 Git。** 发送提交说明和待推进的文件，在 `fileNames` 中将文件列为 `id`/`type` 对。包含第一步 `status` 响应中的所有文件，可推进全部内容；选择子集则只推进部分内容：

```curl
curl --request POST \
	--location '<DEV-INSTANCE-URL>/api/v1/source-control/push' \
	--header 'Content-Type: application/json' \
	--header 'X-N8N-API-KEY: <DEV-API-KEY>' \
	--data '{
		"commitMessage": "Promote sales reporting workflows",
		"fileNames": [
			{
				"id": "1a2b3c",
				"type": "workflow"
			}
		]
	}'
```

**3. 预览生产环境中的更改。** 调用 `status` 并设置 `direction=pull`，在任何内容被改动前查看 n8n 将应用哪些更改：

```curl
curl --request GET \
	--location '<PROD-INSTANCE-URL>/api/v1/source-control/status?direction=pull' \
	--header 'X-N8N-API-KEY: <PROD-API-KEY>'
```

**4. 拉取到生产环境。** 生产实例读取同一分支并应用更改。使用 `force` 接受传入版本，并设置 `autoPublish`，在工作流到达时发布：

```curl
curl --request POST \
	--location '<PROD-INSTANCE-URL>/api/v1/source-control/pull' \
	--header 'Content-Type: application/json' \
	--header 'X-N8N-API-KEY: <PROD-API-KEY>' \
	--data '{
		"force": true,
		"autoPublish": "published"
	}'
```

`autoPublish` 参数可设为 `none`（默认值）、`published`（仅重新发布生产环境中已发布的工作流）或 `all`（发布全部拉取的工作流）。各模式的更多说明请参阅[推送和拉取](push-and-pull-changes.md#auto-publish-workflows-on-pull)。

{% hint style="info" %}
**使用多个分支**

如果实例使用不同的 Git 分支，就无法直接推进。请从开发实例推送到其分支，在 Git 托管平台将该分支合并到生产分支，再在生产实例拉取。分支模式请参阅[在环境间复制工作](move-work-between-environments.md)。
{% endhint %}

## 计划备份流程 <a id="scheduled-backup-flow"></a>

要按计划将实例内容以版本形式保存在 Git 中，可定时获取所有符合条件的文件并全部推送。可以通过 cron 作业、CI 流水线，或使用 [Schedule Trigger](../../integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/README.md) 的 n8n 工作流运行此流程。

**1. 获取全部符合条件的文件。** 调用 `status` 并设置 `direction=push`：

```curl
curl --request GET \
	--location '<YOUR-INSTANCE-URL>/api/v1/source-control/status?direction=push' \
	--header 'X-N8N-API-KEY: <YOUR-API-KEY>'
```

**2. 推送完整列表。** 将 `status` 响应返回的每个文件映射为其 `id` 和 `type`，并以 `fileNames` 传入。与环境推进流程不同，此作业无人值守运行，并将 `force` 设为 `true`。这样会跳过冲突检查，始终使用实例当前状态覆盖分支。请确保每次计划运行前，实例中保存的是所需版本，否则可能覆盖 Git 中较新的更改。

```curl
curl --request POST \
	--location '<YOUR-INSTANCE-URL>/api/v1/source-control/push' \
	--header 'Content-Type: application/json' \
	--header 'X-N8N-API-KEY: <YOUR-API-KEY>' \
	--data '{
		"commitMessage": "Scheduled backup",
		"force": true,
		"fileNames": [
			{
				"id": "1a2b3c",
				"type": "workflow"
			},
			{
				"id": "4d5e6f",
				"type": "workflow"
			},
			...
		]
	}'
```

## 处理推送冲突 <a id="handle-push-conflicts"></a>

自上次同步以来，如果实例与 Git 都修改了某个文件，该文件就会发生冲突。`status` 会使用 `"conflict": true` 标记这些文件。如果调用 `push` 时未设置 `force`，且所选文件中有任何冲突，n8n 会以 `409` 响应拒绝整个推送：

```json
{
	"message": "Push blocked by conflicting files. Pass `force: true` to push anyway.",
	"conflicts": [
		{
			"id": "1a2b3c",
			"name": "Daily sales report",
			"type": "workflow",
			"status": "modified",
			"file": "workflows/1a2b3c.json",
			"conflict": true
		}
	]
}
```

要继续推送，使用实例版本覆盖 Git 中的冲突文件，请将 `force` 设为 `true`：

```curl
curl --request POST \
	--location '<YOUR-INSTANCE-URL>/api/v1/source-control/push' \
	--header 'Content-Type: application/json' \
	--header 'X-N8N-API-KEY: <YOUR-API-KEY>' \
	--data '{
		"commitMessage": "Push reviewed workflows only",
		"force": true,
		"fileNames": [
			{
				"id": "1a2b3c",
				"type": "workflow"
			}
		]
	}'
```

## 推送和拉取的内容 <a id="what-gets-pushed-and-pulled"></a>

API 提交和应用的资源与界面相同：工作流、凭据存根、变量存根、数据表结构、项目、文件夹和标签。完整列表和各资源类型的合并行为，请参阅[推送和拉取](push-and-pull-changes.md#what-gets-committed)。

## 相关资源 <a id="related-resources"></a>

* [使用源代码管理与环境](./)
* [理解源代码管理](understand-source-control.md)
* [使用环境](work-with-environments.md)
* [在 n8n 中使用 Git](use-git-in-n8n.md)
* [选择分支模式](choose-branching-patterns.md)
* [设置源代码管理](set-up-source-control.md)
* [推送和拉取更改](push-and-pull-changes.md)
* [比较版本](compare-versions.md)
* [在环境间迁移工作](move-work-between-environments.md)
* [教程：使用源代码管理创建环境](tutorial-create-environments-with-source-control.md)
* [源代码管理](../../connect/n8n-api/source-control.md)：源代码管理端点的请求和响应结构。
* [端点参考](../../connect/n8n-api/api-reference.md)：完整的公共 API 结构定义。
