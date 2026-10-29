---
title: n8n MCP 服务器工具参考
nodeTitle: MCP 服务器工具参考
originalFilePath: advanced-ai/mcp/mcp_tools_reference.md
originalUrl: https://docs.n8n.io/advanced-ai/mcp/mcp_tools_reference
url: https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference
description: n8n MCP 服务器提供的全部工具参考，包括工作流管理、工作流构建、智能体管理、用户偏好和数据表工具。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
  anchors:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MCP 服务器工具参考 <a id="mcp-server-tools-reference"></a>

本页介绍实例级 MCP 服务器提供的全部工具。

自 n8n 2.47.0 起，如果实例受保护（只读），n8n 会阻止所有未标注 `readOnlyHint: true` 的工具。唯一例外是 `execute_workflow`，且 `executionMode` 必须设为 `"production"`。被阻止的调用会返回错误结果，消息为 `This instance is protected. Use read-only operations or production workflow executions.`

***

## 工作流管理 <a href="#workflow-management" id="workflow-management"></a>

### search\_workflows <a href="#searchworkflows" id="searchworkflows"></a>

使用可选筛选条件搜索工作流，返回每个工作流的预览。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 默认值 | 说明 |
| ------------------- | ---------- | -------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query` | `string` | 否 |  | 按名称或描述筛选 |
| `projectId` | `string` | 否 |  | 按项目 ID 筛选 |
| `tags` | `string[]` | 否 |  | 按标签名筛选，采用 AND 语义：工作流必须具有列出的全部标签才会匹配。 |
| `limit` | `integer` | 否 | `200` | 限制结果数量，最多 200 条 |
| `sortBy` | `string` | 否 | `"updatedAt:desc"` | 结果排序方式，可选：`"updatedAt:desc"`、`"updatedAt:asc"`、`"createdAt:desc"`、`"createdAt:asc"`、`"name:asc"`、`"name:desc"` |
| `folderId` | `string` | 否 |  | 按文件夹筛选。传入 `"0"` 时，仅匹配位于项目根目录而非文件夹内的工作流。 |
| `includeSubfolders` | `boolean` | 否 | `true` | `folderId` 搜索是否包含该文件夹的子文件夹。设为 `false` 时，仅匹配直接位于此文件夹内的工作流。`folderId` 为 `"0"` 时忽略。 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ----------------------- | ----------------- | ------------------------------------------------------------------------- |
| `data` | `array` | 工作流预览列表 |
| `data[].id` | `string` | 工作流的唯一标识符 |
| `data[].name` | `string \| null` | 工作流名称 |
| `data[].description` | `string \| null` | 工作流描述 |
| `data[].active` | `boolean \| null` | 工作流是否处于活跃状态 |
| `data[].createdAt` | `string \| null` | 工作流创建时的 ISO 时间戳 |
| `data[].updatedAt` | `string \| null` | 工作流最后保存时的 ISO 时间戳 |
| `data[].triggerCount` | `number \| null` | 与工作流关联的触发器数量 |
| `data[].availableInMCP` | `boolean` | 工作流是否对 MCP 工具可见 |
| `data[].parentFolderId` | `string \| null` | 工作流所在文件夹的 ID；位于项目根目录时为 null |
| `data[].tags` | `array` | 分配给工作流的标签，每个标签含 `id` 和 `name` |
| `count` | `integer` | 符合筛选条件的工作流总数 |

#### 说明 <a href="#notes" id="notes"></a>

* 结果数量上限为 200。
* 默认按最近更新时间排序，最新的工作流在前。
* 自 n8n 2.27.0 起，支持按 `tags` 筛选，结果也包含 `tags` 字段。使用 `list_workflow_tags` 查找可用标签名。
* 自 n8n 2.35.0 起，结果不再包含 `scopes` 或 `canExecute`。请使用 `get_workflow_details` 检查单个工作流的权限。
* 自 n8n 2.37.0 起，支持按 `folderId` 筛选，结果也包含 `parentFolderId` 字段。使用 `search_folders` 将文件夹名称解析为 ID，或传入已找到工作流的 `parentFolderId`，列出同文件夹内的其他工作流。
* **重要：**无论 `Available in MCP` 设置如何，此工具都能列出用户有权访问的全部工作流。

### get\_workflow\_details <a href="#getworkflowdetails" id="getworkflowdetails"></a>

获取特定工作流的详细信息，包括触发器详情。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 默认值 | 说明 |
| ------------- | -------- | ------------- | ------- | ---------------------------------- |
| `workflowId` | `string` | 是 |  | 要获取的工作流 ID |
| `detailLevel` | "full" \| "execution" | 否 | `"full"` | |

{% hint style="info" %}
**功能可用范围**

自 n8n 2.35.0 起提供 `detailLevel`，较早版本始终返回完整工作流。
{% endhint %}

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------------------------------ | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `workflow` | `object` | 经清理、可供 MCP 安全使用的工作流数据 |
| `workflow.id` | `string` | 工作流 ID |
| `workflow.name` | `string \| null` | 工作流名称 |
| `workflow.active` | `boolean` | 工作流是否具有已发布的活跃版本 |
| `workflow.isArchived` | `boolean` | 工作流是否已归档 |
| `workflow.versionId` | `string` | 当前工作流版本 ID |
| `workflow.activeVersionId` | `string \| null` | 活跃工作流版本 ID（如果可用） |
| `workflow.triggerCount` | `number` | 触发器数量 |
| `workflow.nodeCount` | `number` | 工作流中的节点数量，两种详情级别均返回 |
| `workflow.createdAt` | `string \| null` | 工作流创建时的 ISO 时间戳 |
| `workflow.updatedAt` | `string \| null` | 工作流最后保存时的 ISO 时间戳 |
| `workflow.settings` | `object \| null` | 工作流设置 |
| `workflow.connections` | `object` | 工作流连接图 |
| `workflow.nodes` | `array` | 工作流节点列表，凭据引用已移除 |
| `workflow.nodeGroups` | `array` | 工作流中的节点组，仅在 `detailLevel` 为 `"full"` 时返回 |
| `workflow.activeVersion` | `object \| null` | 活跃工作流图（如果可用） |
| `workflow.activeVersion.sameAsDraft` | `boolean` | 为 `true` 时，已发布版本与当前草稿相同，应使用顶层 `nodes`、`connections` 和 `nodeGroups`。为 `false` 时，已发布图会在以下字段中返回。 |
| `workflow.activeVersion.nodes` | `array` | 活跃工作流版本的节点，凭据引用已移除 |
| `workflow.activeVersion.connections` | `object` | 活跃工作流版本的连接 |
| `workflow.activeVersion.nodeGroups` | `array` | 已发布版本的节点组，仅在 `sameAsDraft` 为 `false` 时包含 |
| `workflow.tags` | `array` | 标签，包含 `id` 和 `name` |
| `workflow.meta` | `object \| null` | 工作流元数据 |
| `workflow.parentFolderId` | `string \| null` | 父文件夹 ID |
| `workflow.description` | `string` | 工作流描述（如果已设置） |
| `workflow.scopes` | `string[]` | 用户对该工作流的权限 |
| `workflow.canExecute` | `boolean` | 用户是否有权执行该工作流 |
| `triggerInfo` | `string` | 便于阅读的说明，介绍如何触发此工作流 |

#### 说明 <a href="#notes" id="notes"></a>

* 返回的节点会移除敏感凭据数据。每个凭据引用仅保留 `id` 和 `name`，便于复用已有凭据，而无需重复创建。
* 如果工作流已发布，包含活跃版本的详情。
* 包含用户权限作用域，以及当前用户是否可以执行工作流。
* 使用 `triggerInfo` 了解如何调用受支持的触发节点。
* 使用 `detailLevel: "execution"`，可在仅需通过 `execute_workflow` 运行工作流时省略额外数据。它省略节点图，以缩小响应。

***

### execute\_workflow <a href="#executeworkflow" id="executeworkflow"></a>

按 ID 执行工作流，立即返回执行 ID，不等待执行完成。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 默认值 | 说明 |
| ----------------- | -------------------------- | -------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `workflowId` | `string` | 是 |  | 要执行的工作流 ID |
| `executionMode` | `"manual" \| "production"` | 是 |  | `"manual"` 测试当前版本，`"production"` 执行已发布的活跃版本 |
| `triggerNodeName` | `string` | 否 |  | 要执行的触发节点名称。提供 `inputs` 时必填。省略时，工作流必须恰好只有一个符合条件且无需输入的触发器，例如 Schedule Trigger，或手动模式下的 Manual Trigger。使用 `get_workflow_details` 查看可用的触发器名称。 |
| `inputs` | `object` | 否 |  | 传给工作流的输入，采用可辨识联合类型，见下文 |

**`inputs` 的变体（由 `type` 区分）：**

| 类型 | 字段 | 说明 |
| --------- | --------------------------------------------------- | -------------------------------------- |
| `chat` | `chatInput: string` | 基于聊天的工作流输入 |
| `form` | `formData: Record<string, unknown>` | 基于表单的工作流输入数据 |
| `webhook` | `webhookData: { method?, query?, body?, headers? }` | 基于 Webhook 的工作流输入数据 |

**`webhookData` 字段：**

| 字段 | 类型 | 必填 | 默认值 | 说明 |
| --------- | ------------------------------------------------------------------------ | -------- | ------- | ----------------------- |
| `method` | `"GET" \| "POST" \| "PUT" \| "DELETE" \| "PATCH" \| "HEAD" \| "OPTIONS"` | 否 | `"GET"` | HTTP 方法 |
| `query` | `Record<string, string>` | 否 |  | 查询字符串参数 |
| `body` | `Record<string, unknown>` | 否 |  | 请求体数据 |
| `headers` | `Record<string, string>` | 否 |  | HTTP 请求头 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------- | ---------------------- | ------------------------------------------------------------ |
| `executionId` | `string \| null` | 执行 ID；如果无法启动执行，则为 `null` |
| `status` | `"started" \| "error"` | 工作流执行是否成功启动 |
| `error` | `string` | 无法启动执行时的错误消息 |

#### 说明 <a href="#notes" id="notes"></a>

* 此工具启动工作流后立即返回。使用 `get_workflow_execution` 及返回的 `executionId`，检查最终执行状态或获取执行数据。
* 生产模式支持包含 Webhook、Chat Trigger、Form Trigger 和 Schedule Trigger 节点的工作流。
* 手动模式还支持 Manual Trigger 节点。
* `executionMode` 为 `"production"` 时，工作流必须具有已发布的活跃版本。
* 如果工作流具有多个符合条件的触发器，或唯一符合条件的触发器需要输入数据（Webhook、Chat Trigger 或 Form Trigger），`execute_workflow` 会返回列出可用触发器名称的错误，不会自行选择。请传入 `triggerNodeName` 指定要使用的触发器。
* 只有工作流恰好具有一个符合条件且不需要输入的触发器时，`execute_workflow` 才会自动选择，例如 Schedule Trigger，或手动模式下的 Manual Trigger。
* 自 n8n 2.36.0 起提供 `triggerNodeName`，并在有多个触发器时返回错误。较早版本遇到多个触发器时会执行其中一个，无法指定。
* 不支持执行多步骤表单工作流，或任何需要人工参与交互的工作流。
* 自 n8n 2.47.0 起，在受保护（只读）实例中，`execute_workflow` 仅在 `executionMode` 为 `"production"` 时运行。`"manual"` 执行会返回错误 `This instance is protected. Use read-only operations or production workflow executions.`

***

### test\_workflow <a href="#testworkflow" id="testworkflow"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.15.0 起提供 `test_workflow`。
{% endhint %}

使用固定数据测试工作流，绕过外部服务。触发节点、带凭据的节点和 HTTP Request 节点会使用固定数据（模拟数据）。其他节点（Set、If、Code 等）正常执行，包括 Execute Command、文件读写等不依赖凭据的输入输出节点。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 默认值 | 说明 |
| ----------------- | ----------------------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `workflowId` | `string` | 是 |  | 要测试的工作流 ID |
| `pinData` | `Record<string, array>` | 是 |  | 全部工作流节点的固定数据 |
| `triggerNodeName` | `string` | 否 |  | 可选，指定从哪个触发节点开始执行。默认使用第一个触发节点。 |
| `timeout` | `integer` | 否 | `300` | 测试执行被中断前的超时时间，单位为秒。最多 3600 秒（60 分钟），可增加此值以测试运行时间更长的工作流。 |

{% hint style="info" %}
**功能可用范围**

自 n8n 2.33.0 起提供 `timeout`。
{% endhint %}

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `executionId` | `string \| null` | 测试执行 ID |
| `status` | `string` | 测试执行状态，可选：`"success"`、`"error"`、`"running"`、`"waiting"`、`"canceled"`、`"crashed"`、`"new"`、`"unknown"` |
| `error` | `string` | 执行失败时的错误消息 |

#### 说明 <a href="#notes" id="notes"></a>

* 可在不设置凭据、不访问外部服务的情况下测试工作流逻辑。
* 此工具同步执行工作流，等待执行完成。
* 强制应用 MCP 执行超时，默认为五分钟。可通过 `timeout` 增加，最长为 60 分钟。

***

### prepare\_workflow\_pin\_data <a href="#preparetestpindata" id="preparetestpindata"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.15.0 起提供 `prepare_workflow_pin_data`。
{% endhint %}

为工作流准备测试固定数据。触发节点、带凭据的节点和 HTTP Request 节点需要固定数据。逻辑节点（Set、If、Code 等）及无需凭据的输入输出节点（Execute Command、文件读写）会正常执行，无需固定数据。工具返回 JSON Schema，说明各个需要固定数据的节点所期望的输出结构。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------------ | -------- | -------- | ---------------------------------------------------- |
| `workflowId` | `string` | 是 | 要为其生成测试固定数据的工作流 ID |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ----------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `nodeSchemasToGenerate` | `Record<string, JsonSchema>` | 需要固定数据的节点。键为节点名称，值为描述预期输出结构的 JSON Schema 对象。 |
| `nodesWithoutSchema` | `string[]` | 需要固定数据但没有输出 Schema 的节点名称，每个节点使用空默认值 `[{"json": {}}]`。 |
| `nodesSkipped` | `string[]` | 无需固定数据、测试时会正常执行的节点 |
| `coverage` | `object` | 覆盖情况统计 |
| `coverage.withSchemaFromExecution` | `number` | 根据上次成功执行的输出推断出 Schema 的节点 |
| `coverage.withSchemaFromDefinition` | `number` | Schema 来自节点类型定义的节点 |
| `coverage.withoutSchema` | `number` | 既无数据也无 Schema 的节点 |
| `coverage.skipped` | `number` | 将正常执行的节点，无需固定数据 |
| `coverage.total` | `number` | 启用的节点总数 |

#### 说明 <a href="#notes" id="notes"></a>

* 应使用这些 Schema，为 `test_workflow` 生成符合实际的示例数据。
* 在 n8n 2.34.0 中由 `prepare_test_pin_data` 更名。

***

### publish\_workflow <a href="#publishworkflow" id="publishworkflow"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.12.0 起提供 `publish_workflow`。
{% endhint %}

发布（激活）工作流，使其可用于生产执行。这会根据当前草稿创建活跃版本。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------------ | -------- | -------- | ------------------------------------------------------------------------------------- |
| `workflowId` | `string` | 是 | 要发布的工作流 ID |
| `versionId` | `string` | 否 | 可选，要发布的版本 ID。未提供时，发布当前草稿版本。 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ----------------- | ---------------- | -------------------------------------- |
| `success` | `boolean` | 发布是否成功 |
| `workflowId` | `string` | 工作流 ID |
| `activeVersionId` | `string \| null` | 发布后的活跃版本 ID |
| `error` | `string` | 发布失败时的错误消息 |

***

### unpublish\_workflow <a href="#unpublishworkflow" id="unpublishworkflow"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.12.0 起提供 `unpublish_workflow`。
{% endhint %}

取消发布（停用）工作流，使其不再用于生产执行。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------------ | -------- | -------- | ----------------------------------- |
| `workflowId` | `string` | 是 | 要取消发布的工作流 ID |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------ | --------- | ------------------------------------ |
| `success` | `boolean` | 取消发布是否成功 |
| `workflowId` | `string` | 工作流 ID |
| `error` | `string` | 取消发布失败时的错误消息 |

***

### get\_workflow\_history <a href="#getworkflowhistory" id="getworkflowhistory"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.29.0 起提供 `get_workflow_history`。
{% endhint %}

列出工作流已保存的版本历史，最新版本在前，便于查看随时间发生的更改，并选择要获取或恢复的版本。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 默认值 | 说明 |
| ------------ | --------- | -------- | ------- | -------------------------------------------------- |
| `workflowId` | `string` | 是 |  | 要读取版本历史的工作流 ID |
| `limit` | `integer` | 否 | `50` | 限制结果数量，最多 50 条 |
| `offset` | `integer` | 否 | `0` | 分页时跳过的版本数量 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------ | --------- | --------------------------------------------------------------------------------- |
| `success` | `boolean` | 请求是否成功 |
| `workflowId` | `string` | 工作流 ID |
| `versions` | `array` | 按从新到旧排序的版本，较旧版本可能被保留策略清理 |
| `count` | `number` | 本页返回的版本数量 |
| `error` | `string` | 请求失败时的错误消息 |

`versions` 中每个条目包含以下字段：

| 字段 | 类型 | 说明 |
| ------------- | ---------------- | -------------------------------------------------------- |
| `versionId` | `string` | 版本 ID，可用于 `get_workflow_version` |
| `authors` | `string` | 此版本的作者 |
| `name` | `string \| null` | 可选的命名版本标签 |
| `description` | `string \| null` | 可选的命名版本描述 |
| `autosaved` | `boolean` | 此版本是否由自动保存生成 |
| `createdAt` | `string` | 版本创建时的 ISO 时间戳 |
| `updatedAt` | `string` | 版本元数据最后更新时的 ISO 时间戳 |

#### 说明 <a href="#notes" id="notes"></a>

* 对于保存版本较多的工作流，可使用 `limit` 和 `offset` 分页浏览历史。
* 将结果中的 `versionId` 传给 `get_workflow_version` 可读取版本完整内容，或传给 `restore_workflow_version` 将工作流回退到该版本。

***

### get\_workflow\_version <a href="#getworkflowversion" id="getworkflowversion"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.29.0 起提供 `get_workflow_version`。自 n8n 2.34.0 起，响应会包含节点凭据，每个凭据槽位仅保留 `id` 和 `name`。较早版本会完全移除凭据。
{% endhint %}

从历史中获取指定工作流版本的完整内容，包括节点、连接和节点组。所需的 `versionId` 可从 `get_workflow_history` 获取。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------------ | -------- | -------- | ----------------------------------------------------------------- |
| `workflowId` | `string` | 是 | 此版本所属的工作流 ID |
| `versionId` | `string` | 是 | 要获取的版本 ID，由 `get_workflow_history` 返回 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------- | ---------------- | ------------------------------------------------------------------------ |
| `success` | `boolean` | 请求是否成功 |
| `versionId` | `string` | 版本 ID |
| `workflowId` | `string` | 工作流 ID |
| `authors` | `string \| null` | 此版本的作者 |
| `name` | `string \| null` | 可选的命名版本标签 |
| `description` | `string \| null` | 可选的命名版本描述 |
| `createdAt` | `string \| null` | 版本创建时的 ISO 时间戳 |
| `updatedAt` | `string \| null` | 版本元数据最后更新时的 ISO 时间戳 |
| `nodes` | `array` | 此版本中保存的工作流节点 |
| `connections` | `object` | 此版本中保存的节点连接，以源节点名称为键 |
| `nodeGroups` | `array` | 此版本中保存的节点组 |
| `error` | `string` | 请求失败时的错误消息 |

#### 说明 <a href="#notes" id="notes"></a>

* 获取 `versionId` 请调用 `get_workflow_history`。
* 每个凭据引用仅保留 `id` 和 `name`，与 `get_workflow_details` 一致，使你能够复用已有凭据而不暴露密钥值。
* 要将此版本设为当前草稿，请将其 `versionId` 传给 `restore_workflow_version`。
* 如果需要两个版本间的更改摘要而非完整内容，请使用 `get_workflow_versions_diff`。

***

### get\_workflow\_versions\_diff <a href="#getworkflowversionsdiff" id="getworkflowversionsdiff"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.36.0 起提供 `get_workflow_versions_diff`。
{% endhint %}

比较工作流的两个已保存版本，返回二者之间的更改。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| --------------- | -------- | -------- | --------------------------------------------- |
| `workflowId` | `string` | 是 | 这些版本所属的工作流 ID |
| `fromVersionId` | `string` | 是 | 基础版本（较旧）的 ID |
| `toVersionId` | `string` | 是 | 目标版本（较新）的 ID |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `success` | `boolean` | 比较是否成功 |
| `workflowId` | `string` | 工作流 ID |
| `fromVersionId` | `string` | 基础版本 ID |
| `toVersionId` | `string` | 目标版本 ID |
| `nodesAdded` | `array` | 目标版本中存在而基础版本中不存在的节点的完整内容。凭据引用仅保留 `id` 和 `name`。 |
| `nodesRemoved` | `array` | 基础版本中存在而目标版本中不存在的节点，每个节点含 `id`、`name` 和 `type` |
| `nodesModified` | `array` | 两个版本中都存在但内容改变的节点，每个节点含 `id`、`name`、`type` 和 `changes` |
| `nodesModified[].changes` | `object` | 字段级差异。更改的值表示为 `{ __old, __new }`，新增键为 `<key>__added`，移除的键为 `<key>__deleted`，数组更改为 `[op, value]` 元组。 |
| `connectionsAdded` | `array` | 目标版本中存在而基础版本中不存在的连接 |
| `connectionsRemoved` | `array` | 基础版本中存在而目标版本中不存在的连接 |
| `error` | `string` | 比较失败时的错误消息 |

`connectionsAdded` 和 `connectionsRemoved` 中每个条目包含以下字段：

| 字段 | 类型 | 说明 |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------------- |
| `from` | `string` | 源节点名称 |
| `to` | `string` | 目标节点名称 |
| `type` | `string` | 连接类型，例如 `main` 或 `ai_tool` |
| `fromOutput` | `number` | 源节点输出索引。例如，If 节点中的 `0` 为 true 分支，`1` 为 false 分支。 |
| `toInput` | `number` | 目标节点输入索引。例如，`1` 表示 Merge 节点的第二个输入。 |

#### 说明 <a href="#notes" id="notes"></a>

* 版本 ID 可从 `get_workflow_history` 获取。
* 将较旧版本作为 `fromVersionId`，较新版本作为 `toVersionId` 传入。
* `nodesAdded` 包含完整节点内容，无需再次调用即可读取新增节点。要获取已移除节点的内容，请使用 `get_workflow_version` 获取基础版本。
* 节点仅在画布上移动位置，不会被报告为已修改。
* 单独重命名节点不会产生连接更改，因为连接端点按节点 ID 匹配。
* 修改的节点使用其在目标版本中的名称。

***

### search\_projects <a href="#searchprojects" id="searchprojects"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.14.0 起提供 `search_projects`。
{% endhint %}

搜索当前用户有权访问的项目。可在向特定项目创建工作流或数据表之前，用它解析项目 ID。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------- | ---------------------- | -------- | ------------------------------------------------------------------------------------------------------------ |
| `query` | `string` | 否 | 按项目名称筛选。结果优先显示不区分大小写的完全匹配，再显示部分匹配。 |
| `type` | `"personal" \| "team"` | 否 | 按项目类型筛选 |
| `limit` | `integer` | 否 | 限制结果数量，最多 100 条 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| --------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `data` | `array` | 匹配项目列表，优先显示不区分大小写的完全匹配 |
| `data[].id` | `string` | 项目唯一标识符 |
| `data[].name` | `string` | 项目名称 |
| `data[].type` | `"personal" \| "team"` | 项目类型 |
| `data[].matchType` | `"exact" \| "partial"` | 项目名称与查询是完全匹配还是部分匹配，仅在提供 `query` 时包含 |
| `count` | `integer` | 匹配项目总数 |
| `teamProjectsEnabled` | `boolean` | 此实例是否获得团队项目许可。为 `false` 时，默认省略 `projectId`（适用于 `create_workflow_from_code`），因此工作流会在调用者的个人项目中创建，除非用户显式选择返回的可访问项目之一。错误响应中不包含。自 n8n 2.26.0 起提供。 |
| `hint` | `string` | 选择结果的指引。匹配不明确（例如没有完全匹配，但有多个部分匹配），或实例未获得团队项目许可时包含。 |

#### 说明 <a href="#notes" id="notes"></a>

* 结果数量上限为 100。
* 如果用户指定了项目名称，请先调用此工具，将解析后的项目 ID 传给 `create_workflow_from_code`、`update_workflow` 或数据表工具。
* 如果返回 `hint`，请先遵循其中的指引再操作。例如，遇到多个部分匹配时，应请用户澄清，而不是自行猜测。

***

### search\_folders <a href="#searchfolders" id="searchfolders"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.14.0 起提供 `search_folders`。
{% endhint %}

搜索项目内的文件夹。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ----------- | --------- | -------- | ------------------------------------------------------- |
| `projectId` | `string` | 是 | 要搜索文件夹的项目 ID |
| `query` | `string` | 否 | 按文件夹名称筛选，不区分大小写的部分匹配 |
| `limit` | `integer` | 否 | 限制结果数量，最多 100 条 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ----------------------- | ---------------- | ------------------------------------------------------- |
| `data` | `array` | 匹配文件夹列表 |
| `data[].id` | `string` | 文件夹唯一标识符 |
| `data[].name` | `string` | 文件夹名称 |
| `data[].parentFolderId` | `string \| null` | 父文件夹 ID；位于项目根目录时为 null |
| `count` | `integer` | 匹配文件夹总数 |

#### 说明 <a href="#notes" id="notes"></a>

* 结果数量上限为 100。
* 此工具让 MCP 客户端能在指定文件夹中创建工作流，也可将文件夹名称解析为 `folderId`，供 `search_workflows` 筛选使用。

***

### list\_workflow\_tags <a href="#listtags" id="listtags"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.27.0 起提供 `list_workflow_tags`。
{% endhint %}

列出实例中的全部工作流标签。标签是全局资源，不受项目作用域限制，可与 `search_workflows` 配合筛选结果。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 默认值 | 说明 |
| ------- | --------- | -------- | ------- | ------------------------------------- |
| `limit` | `integer` | 否 | `500` | 限制结果数量，最多 500 条 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------------- | --------- | ----------------------------------------------- |
| `data` | `array` | 实例中可用的工作流标签 |
| `data[].id` | `string` | 标签唯一标识符 |
| `data[].name` | `string` | 标签显示名称 |
| `data[].usageCount` | `integer` | 使用此标签的未归档工作流数量 |
| `data[].createdAt` | `string` | 标签创建时的 ISO 时间戳 |
| `data[].updatedAt` | `string` | 标签最后更新时的 ISO 时间戳 |
| `count` | `integer` | 返回的标签数量 |
| `totalCount` | `integer` | 应用数量限制前的标签总数 |

#### 说明 <a href="#notes" id="notes"></a>

* 结果数量上限为 500。
* 标签为全局资源，不受项目作用域限制。
* `usageCount` 仅统计未归档工作流。
* 需要 `tag:list` 全局权限。
* 仅在实例启用工作流标签时可用。如果实例设置禁用了标签，此工具不会开放。
* 在 n8n 2.34.0 中由 `list_tags` 更名。

***

## 执行管理 <a href="#execution-management" id="execution-management"></a>

### get\_workflow\_execution <a href="#getexecution" id="getexecution"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.12.0 起提供 `get_workflow_execution`。
{% endhint %}

按执行 ID 和工作流 ID 获取执行详情，默认仅返回元数据。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| -------------- | ---------- | -------- | --------------------------------------------------------------------------------------------------------- |
| `workflowId` | `string` | 是 | 执行所属的工作流 ID |
| `executionId` | `string` | 是 | 要获取的执行 ID |
| `includeData` | `boolean` | 否 | 是否包含完整执行结果数据，默认为 false（仅元数据） |
| `nodeNames` | `string[]` | 否 | `includeData` 为 true 时，仅返回这些节点的数据；省略时，包含全部节点的数据。 |
| `truncateData` | `integer` | 否 | `includeData` 为 true 时，限制每个节点输出返回的数据项数量。 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| -------------------------- | ---------------- | --------------------------------------------------------------- |
| `execution` | `object \| null` | 执行元数据；出错时为 null |
| `execution.id` | `string` | 执行 ID |
| `execution.workflowId` | `string` | 工作流 ID |
| `execution.mode` | `string` | 执行模式 |
| `execution.status` | `string` | 执行状态 |
| `execution.startedAt` | `string \| null` | 执行开始时的 ISO 时间戳 |
| `execution.stoppedAt` | `string \| null` | 执行停止时的 ISO 时间戳 |
| `execution.retryOf` | `string \| null` | 本次执行所重试的原执行 ID |
| `execution.retrySuccessId` | `string \| null` | 成功的重试执行 ID |
| `execution.waitTill` | `string \| null` | 执行将等待到的时间，以 ISO 时间戳表示 |
| `data` | `unknown` | 执行结果数据，仅在 `includeData` 为 true 时包含 |
| `error` | `string` | 请求失败时的错误消息 |

#### 说明 <a href="#notes" id="notes"></a>

* 不需要完整执行数据时，使用轻量的元数据查询（默认方式）。
* 通过 `nodeNames` 筛选、通过 `truncateData` 截断结果，有助于处理大型结果集。
* 在 n8n 2.34.0 中由 `get_execution` 更名。

***

### search\_workflow\_executions <a href="#searchexecutions" id="searchexecutions"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.20.0 起提供 `search_workflow_executions`。
{% endhint %}

使用可选筛选条件搜索工作流执行，返回包含状态、时间和工作流 ID 的执行元数据。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| --------------- | ---------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `workflowId` | `string` | 否 | 按工作流 ID 筛选执行 |
| `status` | `string[]` | 否 | 按执行状态筛选。可选值：`"canceled"`、`"crashed"`、`"error"`、`"new"`、`"running"`、`"success"`、`"unknown"`、`"waiting"` |
| `startedAfter` | `string` | 否 | ISO 8601 时间戳，仅返回此时间之后开始的执行 |
| `startedBefore` | `string` | 否 | ISO 8601 时间戳，仅返回此时间之前开始的执行 |
| `limit` | `integer` | 否 | 限制结果数量，最多 200 条 |
| `cursor` | `string` | 否 | 分页游标，传入上一页的 `nextCursor`，将其作为不应自行解析的值处理 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data` | `array` | 符合查询的执行列表 |
| `data[].id` | `string` | 执行唯一标识符 |
| `data[].workflowId` | `string` | 此次执行所属的工作流 |
| `data[].status` | `string` | 执行状态 |
| `data[].mode` | `string` | 执行的触发方式，可选：`"cli"`、`"error"`、`"integrated"`、`"internal"`、`"manual"`、`"retry"`、`"trigger"`、`"webhook"`、`"evaluation"`、`"chat"` |
| `data[].startedAt` | `string \| null` | 执行开始时的 ISO 时间戳 |
| `data[].stoppedAt` | `string \| null` | 执行停止时的 ISO 时间戳 |
| `data[].waitTill` | `string \| null` | 执行将等待到的时间，以 ISO 时间戳表示 |
| `count` | `integer` | 匹配执行总数；无法获取数量时为 `-1` |
| `estimated` | `boolean` | 对于大型数据集，数量是否为估算值 |
| `nextCursor` | `string \| null` | 下一页游标；没有下一页时为 `null` |
| `error` | `string` | 查询失败时的错误消息 |

#### 说明 <a href="#notes" id="notes"></a>

* 在 n8n 2.34.0 中由 `search_executions` 更名。
* `cursor` 替代了原先的 `lastId` 参数。传入上一响应中的 `nextCursor` 值，并将其视为不应自行解析的字符串。

***

## 凭据管理 <a href="#credential-management" id="credential-management"></a>

### list\_credentials <a href="#listcredentials" id="listcredentials"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.21.0 起提供 `list_credentials`。
{% endhint %}

列出当前用户可访问的凭据。可在工作流节点引用凭据前，用它查找凭据 ID。绝不返回凭据密钥数据。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------------------ | --------- | -------- | ----------------------------------------------------------------------------------------- |
| `limit` | `integer` | 否 | 限制结果数量，最多 200 条 |
| `query` | `string` | 否 | 按凭据名称筛选，采用部分匹配 |
| `type` | `string` | 否 | 按凭据类型筛选，例如 `"slackApi"` 或 `"httpHeaderAuth"`，采用部分匹配 |
| `projectId` | `string` | 否 | 仅返回属于此项目的凭据 |
| `onlySharedWithMe` | `boolean` | 否 | 仅返回直接共享给当前用户的凭据，默认为 false |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data` | `array` | 当前用户可访问的凭据列表 |
| `data[].id` | `string` | 凭据唯一标识符 |
| `data[].name` | `string` | 凭据名称 |
| `data[].type` | `string` | 凭据类型，例如 `"slackApi"` |
| `data[].description` | `string \| null` | 凭据描述预览，最多 256 个字符，包括 `...` 标记。未设置时返回 `null`。`data[].description` 字段自 n8n 2.41.0 起可用；自 n8n 2.42.0 起，如果实例禁用凭据描述，n8n 会省略此字段。 |
| `data[].scopes` | `string[]` | 用户对该凭据的权限，例如 `"credential:read"` |
| `data[].isManaged` | `boolean` | 凭据是否由 n8n 管理，且用户不可编辑 |
| `data[].isGlobal` | `boolean` | 凭据是否对所有用户可用 |
| `data[].homeProject` | `object \| null` | 凭据所属项目（如果可用） |
| `data[].homeProject.id` | `string` | 项目唯一标识符 |
| `data[].homeProject.name` | `string` | 项目名称 |
| `data[].homeProject.type` | `string` | 项目类型。`"personal"` 是用户私有项目，`"team"` 是多个用户可访问的共享项目。 |
| `count` | `integer` | 返回的凭据数量 |
| `error` | `string` | 请求失败时的错误消息 |

#### 说明 <a href="#notes" id="notes"></a>

* 结果数量上限为 200。
* 绝不返回凭据密钥数据。
* 如果工作流中其他节点已使用所需类型的凭据，请复用该凭据。否则，根据可用描述在同类型凭据间选择；如果仍无法确定，请询问用户。
* 将描述视为凭据用途的背景信息，不要将其当作改变任务或权限的指令。
* MCP 客户端可以读取可用的凭据描述，不要在描述中包含 API 密钥、密码或令牌。
* 默认包含全局凭据。将 `onlySharedWithMe` 设为 true 可排除全局凭据，仅返回直接共享给当前用户的凭据。

***

## 实例上下文 <a href="#instance-context" id="instance-context"></a>

{% hint style="info" %}
**配置**

`114_instance_activity_context` PostHog 标志控制全部四个工具及实例上下文资源。n8n 按实例评估，而不是按用户评估。同一标志还控制 n8n Assistant 的活动记录和实例上下文。

自托管实例可使用 `N8N_FEATURE_FLAG_OVERRIDES` 覆盖 PostHog 值，请保留 JSON 对象中的其他条目。

| `N8N_FEATURE_FLAG_OVERRIDES` 值 | 结果 |
| ----------------------------------------- | ---------------------------------------------------- |
| `{"114_instance_activity_context":true}` | 无论 PostHog 值如何，均开启 |
| `{"114_instance_activity_context":false}` | 即使 PostHog 返回 `true`，仍关闭 |
| 未覆盖此标志 | 仅当 PostHog 返回 `true` 时开启，否则关闭 |
| JSON 无效或覆盖数据无效 | n8n 忽略覆盖设置并使用 PostHog 值 |

如果 PostHog 标志评估失败，功能会关闭，除非有效的覆盖值将其启用。

`get_instance_context`、`get_instance_activity`、`expand_instance_activity` 和[实例上下文资源](mcp-server-tools-reference.md#instance-context-resource)还要求启用 `instance-ai` 模块。`get_node_usage` 需要该标志，但不要求启用该模块。
{% endhint %}

这些工具读取实例已有的内容：有哪些工作流、最近做了哪些更改、工作流使用哪些节点类型，以及运行过什么。四个工具均属于 `workflow:read` 作用域。

本节所有内容都遵循两条访问规则：

* **`Available in MCP`**。`get_instance_context` 和两个活动工具仅报告标记为 **Available in MCP**（可在 MCP 中访问）的工作流，并将已归档工作流视为不可用。`get_node_usage` 则与 `search_workflows` 一样，统计所有你有权读取的工作流，不受该设置限制。
* **你获得的授权范围**。如果授权缺少 `credential:read`，或你无权访问凭据，两个活动工具会省略相应凭据条目。`get_instance_context` 绝不列出凭据名称；授权缺少 `execution:read` 时，它还会省略运行数据。

每个工具默认读取你有权读取工作流的全部项目。传入 `projectId` 可缩小到单个项目。这些工具只读，因此 `projectId` 只缩小已有可见范围，不会扩大范围。

### get\_instance\_context <a href="#getinstancecontext" id="getinstancecontext"></a>

读取实例的初始概况：有哪些工作流、最近创建、修改或删除了什么，以及哪些工作流运行过、失败过。在会话开始、询问用户想做什么之前调用一次。用户表述模糊（例如“修一下”或“继续”）时，通常可从此处最近的内容找到线索。

支持资源的 MCP 客户端，可从[实例上下文资源](mcp-server-tools-reference.md#instance-context-resource)读取相同内容。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ----------- | -------- | -------- | ------------------------------------------------------------------------------------ |
| `projectId` | `string` | 否 | 读取一个项目，而非全部可见项目。可从 `search_projects` 获取其 ID。 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ---------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `context` | `string` | 自然语言形式的实例上下文，没有可报告内容时不包含 |
| `empty` | `boolean` | 没有可报告内容时设置，可读取 `nothingExposed` 了解原因 |
| `nothingExposed` | `boolean` | 结果为空时包含。`true` 表示实例已有工作流，但均未开放给 MCP，内容实际存在但无法访问；`false` 表示实例尚无内容。 |

#### 说明 <a href="#notes" id="notes"></a>

* 此工具返回自然语言说明，而非记录列表。它以 `"Name" (workflow:<id>)` 表示工作流、以 `execution:<id>` 表示执行，活动条目则带有方括号 ID。工作流 ID 可传给 `search_workflows` 或 `get_workflow_details`，执行 ID 可传给 `get_workflow_execution`，方括号活动 ID 可传给 `expand_instance_activity`。
* 说明最多包含三部分：现有及最近处理的工作流、最近 24 小时的运行及成功/失败次数，以及近期更改。实例没有相应内容时，会省略该部分。
* 使用 `get_instance_activity` 可向前分页，读取更早的记录。
* 对空响应采取行动前，请检查 `nothingExposed`。`Available in MCP` 默认关闭，因此早于此设置建立的实例，即使已有完整的工作流集合，也可能报告为空。若将其当作新实例，可能会误去重建用户已有的工作。
* 每次调用均返回完整快照。MCP 服务器不保留会话状态，因此调用间无需承接服务器会话状态。

***

### get\_instance\_activity <a href="#getinstanceactivity" id="getinstanceactivity"></a>

读取实例活动日志：最近在此实例中创建、修改、发布或删除了什么，以及由谁完成。可用它接着处理已在进行的工作。用户表述模糊（例如“修一下”或“我该看什么”）时，通常可从此处最近的条目找到线索。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------------ | ---------------------------- | -------- | ------------------------------------------------------------------------------------ |
| `category` | `"workflow" \| "credential"` | 否 | 仅返回某一类条目 |
| `resourceId` | `string` | 否 | 仅返回某个资源的条目，例如单个工作流 ID |
| `beforeId` | `integer` | 否 | 向前分页：仅返回早于此条目 ID 的条目 |
| `projectId` | `string` | 否 | 读取一个项目，而非全部可见项目。可从 `search_projects` 获取其 ID。 |
| `limit` | `integer` | 否 | 限制结果数量，最多 100 条 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `entries` | `array` | 匹配的日志条目，最新的在前 |
| `entries[].id` | `number` | 条目 ID，可传给 `expand_instance_activity` |
| `entries[].at` | `string` | 条目的 ISO 时间戳 |
| `entries[].category` | `string` | 条目对应的资源类型：`"workflow"` 或 `"credential"` |
| `entries[].action` | `string` | 发生的操作，例如创建、保存、发布、删除或归档 |
| `entries[].resourceType` | `string` | `resourceId` 指向的内容 |
| `entries[].resourceId` | `string` | 资源 ID，可传给 `search_workflows` 或 `get_workflow_details` 等工具 |
| `entries[].resourceName` | `string` | 资源在当时的名称 |
| `entries[].byCurrentUser` | `boolean` | 操作是否由当前已验证身份的用户执行 |
| `entries[].detail` | `object` | 条目携带的额外字段 |
| `count` | `integer` | 返回的条目数量 |
| `hasMore` | `boolean` | 本页之后是否还有更多日志条目 |
| `nextBeforeId` | `number` | 将此值作为 `beforeId` 传回可读取下一页。只要 `hasMore` 为 `true` 就包含，即使本页未返回条目。 |

#### 说明 <a href="#notes" id="notes"></a>

* 结果数量上限为 100。
* 条目是日志记录，不是实时资源记录。工作流条目的实时记录可通过 `search_workflows` 或 `get_workflow_details` 获取，凭据条目则使用 `list_credentials`。条目提到的资源可能已被删除。
* 返回数量较少或为空的页面，后面仍可能有更多条目。在认定没有发生任何活动前，请检查 `hasMore`，并使用 `nextBeforeId` 分页。页面较短可能是因为工具隐藏了未标记为 **Available in MCP**（可在 MCP 中访问）的工作流条目。
* 工作流被删除后，只有它的 `deleted` 条目仍可读取，其余历史会消失，因为已没有工作流可供检查 **Available in MCP**（可在 MCP 中访问）状态。

***

### expand\_instance\_activity <a href="#expandinstanceactivity" id="expandinstanceactivity"></a>

读取一个活动日志条目，以及日志中有关同一资源的全部其他内容。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ----------- | --------- | -------- | ----------------------------------------------------------------- |
| `id` | `integer` | 是 | 条目 ID，由 `get_instance_activity` 返回 |
| `projectId` | `string` | 否 | 仅在单个项目内查找。可从 `search_projects` 获取项目 ID。 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ----------------- | --------- | ----------------------------------------------------------------------------------------------- |
| `entry` | `object` | 条目，使用与 `get_instance_activity` 相同的字段；ID 无法解析时不包含 |
| `resourceHistory` | `array` | 日志中有关同一资源的全部其他条目，最新的在前 |
| `liveRecordHint` | `string` | 适用时，用于获取实时资源记录的工具调用 |
| `notFound` | `boolean` | ID 已无法解析时设置 |

#### 说明 <a href="#notes" id="notes"></a>

* `notFound` 是正常结果，不是错误；可在不使用该条目的情况下继续。
* 条目未找到可能有三个原因：被 n8n 按保留窗口清理、属于你无权读取的项目，或指向未标记为 **Available in MCP**（可在 MCP 中访问）的工作流。三种情况特意返回相同响应，避免确认你无权看到的资源是否存在。

***

### get\_node\_usage <a href="#getnodeusage" id="getnodeusage"></a>

报告此实例已使用哪些节点类型，以及使用范围。在等效节点间选择前调用，使新工作流符合实例已有的构建习惯，例如通常使用 HTTP Request 节点还是专用集成节点。不提供 `nodeType` 时返回节点类型使用频次统计，提供时则返回使用该类型的工作流。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ----------- | --------- | -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `nodeType` | `string` | 否 | 完整限定节点类型，例如 `"n8n-nodes-base.httpRequest"`。省略时，获取全部已用节点类型的频次统计。 |
| `projectId` | `string` | 否 | 读取一个项目，而非全部可见工作流。可从 `search_projects` 获取项目 ID。 |
| `limit` | `integer` | 否 | 限制结果数量，最多 100 条 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| --------------------------- | --------- | -------------------------------------------------------------------------------------------------- |
| `workflowsInScope` | `number` | 作为统计依据的已索引、未归档工作流数量，即理解各项计数所需的分母 |
| `nodeTypes` | `array` | 节点类型频次统计，未指定 `nodeType` 时返回，最常用的在前 |
| `nodeTypes[].nodeType` | `string` | 完整限定节点类型 |
| `nodeTypes[].workflowCount` | `number` | 访问范围内使用该类型的工作流数量 |
| `workflows` | `array` | 提供 `nodeType` 时，返回使用指定节点类型的工作流 |
| `workflows[].workflowId` | `string` | 工作流 ID |
| `workflows[].name` | `string` | 工作流名称 |
| `workflows[].updatedAt` | `string` | 最后更改时的 ISO 时间戳 |
| `truncated` | `boolean` | 列表是否因数量限制被截断 |

#### 说明 <a href="#notes" id="notes"></a>

* 结果数量上限为 100。小于 1 或大于 100 的值会被限制到该范围内。
* 结果来自依赖索引，因此只统计节点类型，不统计参数值或凭据。
* **重要：**此工具统计你访问范围内全部已索引、未归档的工作流，不受 `Available in MCP` 设置限制。本节其他工具只报告由该设置开放的工作流。
* 频次统计中的 `truncated` 为 `true` 时，响应未列出的节点类型仍可能正在使用，不要将未出现视为未使用的证据。

***

### 实例上下文资源 <a href="#instance-context-resource" id="instance-context-resource"></a>

对于支持资源的 MCP 客户端，n8n 还将实例上下文作为资源提供；不支持资源的客户端可使用 [get_instance_context](mcp-server-tools-reference.md#getinstancecontext) 工具。

| 属性 | 值 |
| --------- | --------------------------------------------------------------------------------- |
| URI | `n8n://instance/context` |
| MIME 类型 | `text/plain` |
| 内容 | 与 `get_instance_context` 返回的自然语言说明相同，覆盖所有你可读取的项目 |

服务器说明同时介绍这两种方式，因此读取说明的客户端会知道应读取资源，或在不读取资源时调用工具。

读取资源时无需参数。要读取单个项目，请调用 `get_instance_context` 并传入 `projectId`。

资源遵循与工具相同的访问规则，无法调用 `get_instance_context` 的授权，也无法读取此资源。

响应包含各用户各自的数据，n8n 不会缓存它。两个用户读取同一 URI，会获得不同内容。

***

## 工作流构建器 <a href="#workflow-builder" id="workflow-builder"></a>

### get\_workflow\_sdk\_reference <a href="#getsdkreference" id="getsdkreference"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.12.0 起提供 `get_workflow_sdk_reference`。
{% endhint %}

获取 n8n Workflow SDK 参考文档，包括模式、表达式语法、函数、规则、导入语法、指南和设计建议。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 默认值 | 说明 |
| --------- | -------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `section` | `string` | 否 | `"all"` | 要获取的文档章节。可选：`"patterns"`、`"patterns_detailed"`、`"expressions"`、`"functions"`、`"rules"`、`"import"`、`"guidelines"`、`"design"`、`"groups"`（自 n8n 2.41.0 起提供）、`"all"` |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ----------- | -------- | ------------------------------------------------------------- |
| `reference` | `string` | 所请求章节的 SDK 参考文档内容 |

#### 说明 <a href="#notes" id="notes"></a>

* 构建任何工作流前，都应先调用此工具。
* 省略 `section`，或将其设为 `"all"`，可获取完整参考。
* 使用 `"patterns_detailed"` 获取更详细的工作流模式示例。
* 使用 `"groups"` 获取节点组必须遵循的规则，完整参考也包含这些内容。
* 在 n8n 2.34.0 中由 `get_sdk_reference` 更名。

***

### search\_nodes <a href="#searchnodes" id="searchnodes"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.12.0 起提供 `search_nodes`。
{% endhint %}

按服务名称、触发器类型或工具功能搜索 n8n 节点。将 `usage` 设为 `"agentTool"`，可仅返回与智能体兼容的工具节点。返回 `get_node_types` 工具所需的节点 ID、区分项（资源/操作/模式）及相关节点。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 默认值 | 说明 |
| --------- | --------------------------- | ----------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `queries` | `string[]` | 是（至少 1 个） |  | 搜索查询，可使用服务名（例如 `"gmail"`、`"slack"`）、触发器类型（例如 `"schedule trigger"`、`"webhook"`）或实用节点（例如 `"set"`、`"if"`、`"merge"`、`"code"`） |
| `usage` | `"workflow" \| "agentTool"` | 否 | `"workflow"` | 设为 `"agentTool"` 时，仅返回可配置为智能体工具的节点 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| --------- | -------- | ------------------------------------------------------------------------ |
| `results` | `string` | 搜索结果，包含匹配的节点 ID、区分项和相关节点 |

#### 说明 <a href="#notes" id="notes"></a>

* 自 n8n 2.34.0 起提供 `usage`。
* 搜索要作为工具附加到智能体的节点时，使用 `usage="agentTool"`，例如与 `mutate_agent` 或 `create_agent` 配合。这样会排除无法作为智能体工具运行的节点，如需要人工参与的节点和 MCP 客户端节点。

***

### get\_node\_types <a href="#getnodetypes" id="getnodetypes"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.12.0 起提供 `get_node_types`。
{% endhint %}

获取 n8n 节点的 TypeScript 类型定义，返回准确的参数名称和结构。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| --------- | ------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nodeIds` | `array` | 是（至少 1 个） | 节点类型请求对象数组。始终传入对象，即使只请求一个节点，例如 `{ "nodeId": "n8n-nodes-base.gmail" }`。如果 `search_nodes` 结果提供了区分项，也应包含。 |

**节点 ID 对象格式：**

| 字段 | 类型 | 必填 | 说明 |
| ----------- | -------- | -------- | ------------------------------------------------------- |
| `nodeId` | `string` | 是 | 节点类型 ID，例如 `"n8n-nodes-base.gmail"` |
| `version` | `string` | 否 | 特定版本，例如 `"2.1"` |
| `resource` | `string` | 否 | 资源区分项，例如 `"message"` |
| `operation` | `string` | 否 | 操作区分项，例如 `"send"` |
| `mode` | `string` | 否 | 模式区分项 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------- | -------- | --------------------------------------------------- |
| `definitions` | `string` | 所请求节点的 TypeScript 类型定义 |

#### 说明 <a href="#notes" id="notes"></a>

* 对正确配置节点至关重要：MCP 客户端编写工作流代码前，应始终调用此工具。
* 自 n8n 2.27.0 起，每个 `nodeIds` 条目都必须是对象。不再接受纯字符串节点 ID，请将其包装为 `{ "nodeId": "..." }`。
* 对于具有多种变体的节点，请使用 `resource`、`operation` 和 `mode` 区分项。

***

### get\_workflow\_best\_practices <a href="#getworkflowbestpractices" id="getworkflowbestpractices"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.26.0 起提供 `get_workflow_best_practices`。
{% endhint %}

获取某种工作流技术的最佳实践指南，适合在搜索节点或编写工作流代码前使用。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ----------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `technique` | `string` | 是 | 要获取指南的工作流技术键。传入 `"list"` 可发现全部可用技术。可选值包括：`"scheduling"`、`"chatbot"`、`"form_input"`、`"scraping_and_research"`、`"monitoring"`、`"enrichment"`、`"triage"`、`"content_generation"`、`"document_processing"`、`"data_extraction"`、`"data_analysis"`、`"data_transformation"`、`"data_persistence"`、`"notification"`、`"knowledge_base"`、`"human_in_the_loop"`、`"web_app"` |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ---------------------------------------- | --------- | ------------------------------------------------------------------------------ |
| `technique` | `string` | 所请求的技术键；列出全部可用技术时为 `"list"` |
| `message` | `string` | 便于阅读的响应摘要 |
| `documentation` | `string` | 所请求技术的最佳实践文档（如果可用） |
| `availableTechniques` | `array` | 可用技术列表，`technique` 为 `"list"` 时返回 |
| `availableTechniques[].technique` | `string` | 技术键 |
| `availableTechniques[].description` | `string` | 技术描述 |
| `availableTechniques[].hasDocumentation` | `boolean` | 此技术是否有详细的最佳实践文档 |

#### 说明 <a href="#notes" id="notes"></a>

* 使用 `technique: "list"` 调用时，列出全部可用技术。
* 自 n8n 2.41.0 起，`"list"` 响应末尾还会提供何时应将工作流组织为节点组的指南。
* 某些已知技术可能尚无详细文档，此时工具会返回一条消息，不包含 `documentation`。
* 此工具替代了原先的 `get_suggested_nodes` 工作流规划指南。

***

### explore\_node\_resources <a href="#explorenoderesources" id="explorenoderesources"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.27.0 起提供 `explore_node_resources`。
{% endhint %}

解析节点资源定位器或动态加载选项下拉框背后的真实值，例如 Slack 频道、Google Sheets 标签页或可用 AI 模型。需要为目标服务设置凭据。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ----------------------- | ------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nodeType` | `string` | 是 | 完整限定的节点类型 ID，来自 `search_nodes` / `get_node_types`，例如 `"n8n-nodes-base.slack"` |
| `version` | `number` | 是 | 节点版本，例如 `4.7`，必须与 `search_nodes` 返回的版本匹配 |
| `methodName` | `string` | 是 | 类型定义中节点 `@searchListMethod` 或 `@loadOptionsMethod` 注解提供的准确方法名。先调用 `get_node_types` 读取真实方法名，不要猜测。 |
| `methodType` | `"listSearch" \| "loadOptions"` | 是 | `"listSearch"` 用于 `@searchListMethod` 注解（支持筛选和分页）；`"loadOptions"` 用于 `@loadOptionsMethod` 注解。 |
| `credentialType` | `string` | 是 | 节点的凭据类型键，例如 `"slackApi"` 或 `"googleSheetsOAuth2Api"` |
| `credentialId` | `string` | 是 | 用户可访问的凭据 ID，由 `list_credentials` 获取 |
| `filter` | `string` | 否 | 可选的搜索或筛选文本，用于缩小结果范围 |
| `paginationToken` | `string` | 否 | 用于获取下一页的前次调用分页令牌，仅适用于 `listSearch` |
| `currentNodeParameters` | `object` | 否 | 用于依赖项查找的当前节点参数。某些方法要求先作出选择，例如列出电子表格中的工作表时，需要 `{ documentId: { __rl: true, mode: "id", value: "<spreadsheetId>" } }`。可查看类型定义的 `displayOptions`，了解方法依赖哪些参数。 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ----------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `results` | `array` | 节点方法返回的资源 |
| `results[].name` | `string` | 资源的显示标签 |
| `results[].value` | `string \| number \| boolean` | 工作流代码中应使用的 ID |
| `results[].url` | `string` | 资源 URL（如果可用） |
| `results[].description` | `string` | 资源描述（如果可用） |
| `paginationToken` | `string` | 将其作为 `paginationToken` 传回可获取下一页；没有更多结果时不包含。 |
| `builderHint` | `string` | 节点 `@builderHint` 注解提供的选择指引（如果存在） |
| `error` | `string` | 查找失败时的错误消息 |
| `httpCode` | `string` | 查找因 API 调用失败时，上游 API 返回的 HTTP 状态码 |
| `errorDescription` | `string` | 查找因 API 调用失败时，上游 API 自身的错误文本，可用于区分权限不足与凭据无效。n8n 将其截断为最多 4,000 个字符。 |

#### 说明 <a href="#notes" id="notes"></a>

* 需要提供 `credentialId`，可从 `list_credentials` 获取。查找以当前用户身份、使用该凭据执行。
* `listSearch` 方法支持 `filter`，并通过 `paginationToken` 分页；`loadOptions` 方法则不支持。
* 与多数其他只读工具不同，此工具会访问外部服务。
* 自 n8n 2.43.0 起，查找失败会返回错误结果，包含空的 `results` 数组和 `error` 字段。如果由上游 API 调用失败导致，还会在可用时包含 `httpCode` 和 `errorDescription`。较早版本仅返回错误消息，API 失败时通常只是通用的状态说明。
* 返回前，n8n 会从 `error` 和 `errorDescription` 中移除密钥。

***

### validate\_workflow <a href="#validateworkflow" id="validateworkflow"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.12.0 起提供 `validate_workflow`。
{% endhint %}

验证 n8n Workflow SDK 代码。将代码解析为工作流并检查错误。创建或更新工作流前，应始终验证。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------ | -------- | -------- | ------------------------------------------------------------------------------------------------------ |
| `code` | `string` | 是 | 使用 n8n Workflow SDK 的完整 TypeScript/JavaScript 工作流代码，必须包含工作流导出 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| -------------------------- | ---------- | ------------------------------------------------------------ |
| `valid` | `boolean` | 工作流代码是否有效 |
| `nodeCount` | `number` | 工作流节点数量，仅在有效时包含 |
| `warnings` | `array` | 验证警告（如果有） |
| `warnings[].code` | `string` | 标识警告类型的警告代码 |
| `warnings[].message` | `string` | 警告消息 |
| `warnings[].nodeName` | `string` | 触发警告的节点（如果适用） |
| `warnings[].parameterPath` | `string` | 触发警告的参数路径（如果适用） |
| `errors` | `string[]` | 验证错误，仅在无效时包含 |
| `hint` | `string` | 可操作的恢复提示（如果可用） |

#### 说明 <a href="#notes" id="notes"></a>

* 必须在 `create_workflow_from_code` 或 `update_workflow` 之前调用。
* 即使代码有效，也可能存在警告。
* 自 n8n 2.41.0 起，如果代码定义节点组，工具会按节点组规则检查。违反规则会将 `valid` 设为 `false`，随后 `errors` 数组会包含与保存时因节点组被拒绝而返回的相同消息。
* 如果 `valid` 为 `false` 且包含 `hint`，请先按提示处理再重试。

***

### validate\_node\_config <a href="#validatenodeconfig" id="validatenodeconfig"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.25.1 起提供 `validate_node_config`。
{% endhint %}

根据生成的节点 Schema，独立验证一个或多个节点配置。适合在组合节点时使用，先于组装工作流代码或调用 `update_workflow`。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| --------------------- | --------- | ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `nodes` | `array` | 是（至少 1 个，最多 50 个） | 要独立验证的一个或多个节点配置 |
| `nodes[].name` | `string` | 否 | 可选的节点名称，在结果中返回以便对应响应 |
| `nodes[].type` | `string` | 是 | 完整节点类型，例如 `"n8n-nodes-base.set"` 或 `"@n8n/n8n-nodes-langchain.agent"` |
| `nodes[].typeVersion` | `number` | 否 | 节点类型版本，默认为 `1` |
| `nodes[].parameters` | `object` | 否 | 节点参数对象，结构与工作流 JSON 相同，默认为 `{}` |
| `nodes[].subnodes` | `unknown` | 否 | 可选的 AI 父节点子节点配置，例如 LangChain 智能体的模型、记忆或工具引用 |
| `nodes[].isToolNode` | `boolean` | 否 | 设为 `true`，用于验证通过 `ai_tool` 连接作为 AI 工具子节点接入的节点 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ---------------------------- | --------- | --------------------------------------------------------------- |
| `valid` | `boolean` | 是否所有节点配置都有效 |
| `results` | `array` | 逐节点验证结果，顺序与输入一致 |
| `results[].index` | `number` | 此节点在输入数组中的位置 |
| `results[].name` | `string` | 回显输入的节点名称（如果提供） |
| `results[].type` | `string` | 回显输入的节点类型 |
| `results[].valid` | `boolean` | 此节点配置是否有效 |
| `results[].errors` | `array` | 此节点的验证错误，节点有效时省略 |
| `results[].errors[].path` | `string` | 错误参数路径 |
| `results[].errors[].message` | `string` | 便于阅读的错误消息 |
| `error` | `string` | 无法执行验证时的顶层错误消息 |

#### 说明 <a href="#notes" id="notes"></a>

* 仅验证节点参数 Schema。
* 不检查工作流级别的问题，例如连接、必需输入、触发器、未连接节点或凭据是否存在。
* 对于 LangChain 或 AI 工具子节点，将 `isToolNode` 设为 `true`，使 Schema 计算正确的显示选项分支。

***

### create\_workflow\_from\_code <a href="#createworkflowfromcode" id="createworkflowfromcode"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.12.0 起提供 `create_workflow_from_code`。
{% endhint %}

根据已验证的 SDK 代码，在 n8n 中创建工作流。工具将代码解析为工作流并保存。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------------- | ---------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `code` | `string` | 是 | 使用 n8n Workflow SDK 的完整 TypeScript/JavaScript 工作流代码，必须先通过 `validate_workflow` 验证 |
| `skillsUsed` | `string[]` | 否 | MCP 客户端生成此工作流时使用的 n8n 技能名称，服务器端会标准化这些值 |
| `name` | `string` | 否 | 可选的工作流名称，最多 128 个字符。未提供时，使用代码中的名称。 |
| `description` | `string` | 否 | 工作流描述，超过 255 个字符的文本会在保存前缩短为 255 个字符 |
| `projectId` | `string` | 否 | 用于创建工作流的项目 ID，默认使用用户的个人项目。用户指定项目名称时，先调用 `search_projects`。 |
| `folderId` | `string` | 否 | 用于创建工作流的文件夹 ID，要求设置 `projectId`。使用 `search_folders` 可按名称查找项目内的文件夹。 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------------------------------------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `workflowId` | `string` | 新建工作流 ID |
| `name` | `string` | 新建工作流名称 |
| `nodeCount` | `number` | 工作流节点数量 |
| `url` | `string` | 在 n8n 中打开工作流的 URL |
| `autoAssignedCredentials` | `array` | 自动分配给节点的凭据列表 |
| `autoAssignedCredentials[].nodeName` | `string` | 被自动分配凭据的节点名称 |
| `autoAssignedCredentials[].credentialName` | `string` | 自动分配的凭据名称 |
| `autoAssignedCredentials[].credentialType` | `string` | 自动分配的凭据类型 |
| `skippedGroups` | `array` | 因违反节点组规则而被工具丢弃的节点组；全部保留时不包含 |
| `skippedGroups[].groupName` | `string` | 被丢弃的组名称 |
| `skippedGroups[].reason` | `string` | 工具丢弃该组的原因 |
| `warnings` | `array` | 有关新建工作流的警告，包含 SDK 代码解析警告；画布顶层项目过多时的 `TOP_LEVEL_ITEMS_OVER_CEILING` 警告；以及各节点类型来自已验证社区软件包、但实例未安装该软件包时的 `UNINSTALLED_COMMUNITY_NODE` 警告。没有警告时不包含。 |
| `warnings[].code` | `string` | 标识警告类型的警告代码 |
| `warnings[].message` | `string` | 警告消息 |
| `warnings[].nodeName` | `string` | 可选的警告关联节点 |
| `warnings[].parameterPath` | `string` | 可选的警告关联参数路径 |
| `targetProject` | `object` | 工作流创建所在的项目 |
| `targetProject.id` | `string` | 项目 ID |
| `targetProject.name` | `string` | 项目显示名称 |
| `targetProject.type` | `"personal" \| "team"` | 工作流是在个人项目还是团队项目中创建 |
| `targetFolder` | `object` | 工作流所在的文件夹，包含 `id` 和 `name`；位于项目根目录时省略 |
| `note` | `string` | 有关工作流创建的附加说明，例如自动分配凭据时跳过的节点、被缩短为 255 个字符的描述，或 n8n 保存工作流后失败的后续步骤 |
| `hint` | `string` | 错误后可供操作的恢复提示（如果可用） |
| `errorCode` | `string` | 机器可读的错误代码，仅在失败时包含 |

#### 说明 <a href="#notes" id="notes"></a>

* 自动向节点分配可用凭据。
* 自动分配凭据时会跳过 HTTP Request 节点，必须手动配置。
* 将新建工作流的 `availableInMCP` 标志设为 true。
* 为工作流添加 `aiBuilderAssisted` 元数据和 `builderVariant: mcp`。
* 自动解析 Webhook 节点 ID。
* 自 n8n 2.41.0 起，工具会保存 SDK 代码定义的节点组。如果某个组违反节点组规则，工具会丢弃该组，在 `skippedGroups` 中报告，并继续创建工作流的其他部分。无效节点组不会使创建失败，可使用 `update_workflow` 修复。
* 提供 `folderId` 时，还必须提供 `projectId`。
* 如果用户指定目标项目名称，请先调用 `search_projects`，并传入解析后的 `projectId`，不要猜测。
* 创建后，使用 `targetProject` 字段告知用户工作流创建在哪个项目中。
* 自 n8n 2.27.0 起，超过 255 个字符的 `description` 会被截断，而不是被拒绝；发生时，响应的 `note` 会说明。
* 如果 n8n 已保存工作流，但后续步骤失败，工具会确认工作流已保存，并在 `note` 中解释失败步骤，不会将整个调用报告为错误。
* `errorCode` 的值为 `HTTP_` 加上错误携带的 HTTP 状态码（如果有），或错误自身的错误代码（如果有），否则为 `UNKNOWN_ERROR`。

***

### update\_workflow <a href="#updateworkflow" id="updateworkflow"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.12.0 起提供 `update_workflow`。自 n8n 2.20.0 起，此工具改为执行部分更新，不再每次重写整个工作流。
{% endhint %}

按顺序批量应用针对性的部分更新，修改 n8n 中的已有工作流。批次是原子的：任一操作失败，就不保存任何更改。自 n8n 2.41.0 起，节点组操作例外；n8n 会跳过失败的节点组操作，在 `skippedOperations` 中报告，并应用批次中的其他操作。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------------ | ---------- | -------- | -------------------------------------------------------------------------------------------------------------- |
| `workflowId` | `string` | 是 | 要更新的工作流 ID |
| `skillsUsed` | `string[]` | 否 | MCP 客户端生成本次工作流更新时使用的 n8n 技能名称，服务器端会标准化这些值 |
| `operations` | `array` | 是 | 按顺序应用的操作列表，必须包含 1 到 100 个操作 |

#### 支持的操作 <a href="#supported-operations" id="supported-operations"></a>

| 操作 | 必填字段 | 可选字段 | 说明 |
| ---------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `updateNodeParameters` | `nodeName`, `parameters` | `replace` | 将 `parameters` 深度合并到已有节点的参数中。如果 `replace` 为 `true`，则替换整个参数对象。 |
| `setNodeParameter` | `nodeName`, `path`, `value` |  | 通过 RFC 6901 JSON Pointer 路径设置单个参数，例如 `/jsonSchema` 或 `/options/systemMessage`。按需创建中间对象。不支持数组索引，应设置整个数组。 |
| `addNode` | `node.name`, `node.type`, `node.typeVersion` | `node.id`, `node.parameters`, `node.position`, `node.credentials`, `node.disabled`, `node.notes` | 添加节点。`position` 为 `[x, y]`。省略 `id` 时会自动生成。节点名称必须唯一。 |
| `removeNode` | `nodeName` |  | 移除节点及其全部传入、传出连接。连接的子节点会保留在工作流中，但变为未连接状态。 |
| `renameNode` | `oldName`, `newName` |  | 重命名节点，并重写连接引用。新名称必须唯一。 |
| `addConnection` | `source`, `target` | `sourceIndex`, `targetIndex`, `connectionType` | 添加连接。`sourceIndex` 和 `targetIndex` 默认为 `0`；`connectionType` 默认为 `main`。不会重复添加已有的相同连接。 |
| `removeConnection` | `source`, `target` | `sourceIndex`, `targetIndex`, `connectionType` | 移除匹配的连接。`sourceIndex` 和 `targetIndex` 默认为 `0`；`connectionType` 默认为 `main`。 |
| `setNodeCredential` | `nodeName`, `credentialKey`, `credentialId`, `credentialName` |  | 设置或替换节点凭据引用。凭据必须可访问，且匹配节点类型接受的凭据键。 |
| `setNodePosition` | `nodeName`, `position` |  | 将节点画布位置更新为 `[x, y]` |
| `setNodeDisabled` | `nodeName`, `disabled` |  | 启用或禁用节点 |
| `setNodeSettings` | `nodeName`, `settings` |  | 更新节点级执行设置，`settings` 必须至少包含一个受支持的设置 |
| `setWorkflowMetadata` |  | `name`, `description` | 更新工作流元数据。`name` 最多 128 个字符，`description` 最多 255 个字符。 |
| `setNodeGroups` | `nodeGroups` |  | 替换全部节点组，传入 `[]` 可清空。每个组都有 `name` 和 `nodeNames`，以及可选的 `id` 和 `description`。组成员为节点名称，不是 ID。自 n8n 2.41.0 起提供。 |
| `addNodeGroup` | `name`, `nodeNames` | `description`, `id` | 添加一个节点组。`name` 必须唯一，`nodeNames` 必须列出至少一个已有节点。省略 `id` 时会自动生成。自 n8n 2.41.0 起提供。 |
| `removeNodeGroup` | `groupName` |  | 移除一个节点组，组内节点保留在工作流中。自 n8n 2.41.0 起提供。 |
| `updateNodeGroup` | `groupName` | `newName`, `nodeNames`, `description` | 更新一个节点组。至少传入 `newName`、`nodeNames` 或 `description` 之一。`nodeNames` 替换组成员，`description` 传入空字符串可将其清空。自 n8n 2.41.0 起提供。 |

#### `setNodeSettings` 字段 <a href="#setnodesettings-fields" id="setnodesettings-fields"></a>

| 字段 | 类型 | 必填 | 说明 |
| ------------------ | -------------------------------------------------------------------- | -------- | ----------------------------------------------------------- |
| `onError` | `"stopWorkflow" \| "continueRegularOutput" \| "continueErrorOutput"` | 否 | 节点出错时的行为 |
| `retryOnFail` | `boolean` | 否 | 节点失败时是否重试 |
| `maxTries` | `integer` | 否 | `retryOnFail` 为 true 时的尝试次数，必须为 2 到 5 次 |
| `waitBetweenTries` | `integer` | 否 | 两次重试之间等待的毫秒数，必须为 0 到 5000 |
| `alwaysOutputData` | `boolean` | 否 | 节点是否始终输出数据 |
| `executeOnce` | `boolean` | 否 | 节点是否仅执行一次 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------------------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------- |
| `workflowId` | `string` | 更新后的工作流 ID |
| `name` | `string` | 更新后的工作流名称 |
| `nodeCount` | `number` | 工作流节点数量 |
| `url` | `string` | 在 n8n 中打开工作流的 URL |
| `appliedOperations` | `number` | 已应用的操作数量 |
| `skippedOperations` | `array` | 被 n8n 跳过、而未导致批次失败的节点组操作 |
| `skippedOperations[].opIndex` | `number` | 被跳过操作在 `operations` 数组中的位置 |
| `skippedOperations[].type` | `string` | 被跳过操作的类型 |
| `skippedOperations[].reason` | `string` | n8n 跳过该操作的原因 |
| `removedGroups` | `array` | 因本次更新而失效、被 n8n 移除的已有节点组；没有移除组时不包含 |
| `removedGroups[].groupName` | `string` | 被移除的组名称 |
| `removedGroups[].reason` | `string` | n8n 移除该组的原因 |
| `autoAssignedCredentials` | `array` | 自动分配给本次更新新增节点的凭据 |
| `autoAssignedCredentials[].nodeName` | `string` | 被自动分配凭据的节点 |
| `autoAssignedCredentials[].credentialName` | `string` | 自动分配的凭据 |
| `autoAssignedCredentials[].credentialType` | `string` | 自动分配的凭据类型 |
| `validationWarnings` | `array` | 生成工作流的图与 JSON 验证警告，不会阻止保存 |
| `validationWarnings[].code` | `string` | 警告代码 |
| `validationWarnings[].message` | `string` | 警告消息 |
| `validationWarnings[].nodeName` | `string` | 可选的警告关联节点 |
| `note` | `string` | 有关工作流更新的附加说明，例如自动分配凭据时跳过的 HTTP Request 节点 |
| `error` | `string` | 更新失败时的错误消息 |
| `errorCode` | `string` | 机器可读的错误代码，仅在失败时包含 |

#### 说明 <a href="#notes" id="notes"></a>

* 操作按顺序应用并原子保存，节点组操作除外，n8n 会跳过这些操作并在 `skippedOperations` 中报告。
* 节点组操作必须形成有效、连通且不含触发器的图子区域，n8n 会在保存时检查。组的 `description` 最长为 145 个字符。
* 批次中的其他操作可能使已有节点组失效，n8n 会移除该组，并在 `removedGroups` 中报告，批次的其余部分仍会保存。
* 调用后读取 `skippedOperations` 和 `removedGroups`，修复更新时跳过或移除的节点组。
* 已有凭据保持不变，除非显式修改。
* 仅对本次调用新增的节点执行凭据自动分配。
* 自动分配凭据时会跳过 HTTP Request 节点，必须手动配置。
* 保存前会验证生成的工作流，验证警告在 `validationWarnings` 中返回。
* 为工作流添加 `aiBuilderAssisted` 元数据和 `builderVariant: mcp`。
* `errorCode` 的值为 `HTTP_` 加上错误携带的 HTTP 状态码（如果有），或错误自身的错误代码（如果有），否则为 `UNKNOWN_ERROR`。

***

### archive\_workflow <a href="#archiveworkflow" id="archiveworkflow"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.12.0 起提供 `archive_workflow`。
{% endhint %}

按 ID 归档 n8n 中的工作流。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------------ | -------- | -------- | --------------------------------- |
| `workflowId` | `string` | 是 | 要归档的工作流 ID |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------ | --------- | --------------------------------- |
| `archived` | `boolean` | 工作流是否已归档 |
| `workflowId` | `string` | 已归档工作流的 ID |
| `name` | `string` | 已归档工作流的名称 |

#### 说明 <a href="#notes" id="notes"></a>

* 幂等操作：跳过已归档的工作流。

***

### restore\_workflow\_version <a href="#restoreworkflowversion" id="restoreworkflowversion"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.29.0 起提供 `restore_workflow_version`。自 n8n 2.31.0 起，恢复生成的历史条目会按恢复内容自动命名并添加描述。
{% endhint %}

将工作流恢复到历史版本，把该版本重新应用为当前草稿，并记录新的历史条目。使用 `get_workflow_history` 查找 `versionId`。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------------ | -------- | -------- | ---------------------------------------------------------------- |
| `workflowId` | `string` | 是 | 要恢复的工作流 ID |
| `versionId` | `string` | 是 | 要恢复的版本 ID，由 `get_workflow_history` 返回 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ----------------------- | ---------------- | ---------------------------------------------------------------- |
| `success` | `boolean` | 恢复是否成功 |
| `workflowId` | `string` | 工作流 ID |
| `restoredFromVersionId` | `string` | 恢复所使用的版本 ID |
| `newVersionId` | `string \| null` | 恢复成功时，由恢复操作创建的新当前版本 ID |
| `error` | `string` | 恢复失败时的错误消息 |

#### 说明 <a href="#notes" id="notes"></a>

* 获取 `versionId` 请调用 `get_workflow_history`。
* 恢复会将版本中的节点、连接和节点组重新应用为当前草稿，不会修改作为恢复来源的版本。
* 恢复操作自身会保存为新的历史条目，不会覆盖当前草稿的历史。
* 使用与 n8n 编辑器恢复版本相同的更新路径，因此遵循相同的权限和共享检查。

***

## 智能体管理 <a href="#agent-management" id="agent-management"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.34.0 起，当实例同时启用工作流构建器和智能体模块时，可使用智能体管理工具。详情请参阅[构建和管理智能体](../../build/build-and-manage-agents/README.md)。
{% endhint %}

{% hint style="info" %}
**预览状态**

智能体处于预览阶段，未来版本可能更改，请避免在生产工作流中依赖此功能。
{% endhint %}

这些工具用于创建、配置、发布和管理 n8n 智能体。智能体是可持久化的独立对话助手资源，拥有自己的模型、工具、技能、任务和渠道集成。即使工作流可包含 AI Agent 节点，智能体也仍是独立于工作流的资源。

接受 `agentId` 的工具会从智能体解析项目，无需调用者单独传入项目 ID。除 `search_agents` 外，所有工具仅操作 `availableInMCP` 为 true 的智能体；`search_agents` 仍返回当前用户有权访问的全部智能体，使客户端能告知用户已有内容，并在需要时提示启用 MCP 访问。

### search\_agents <a href="#searchagents" id="searchagents"></a>

搜索当前用户有权访问的智能体，可使用 `publishedOnly` 和 `excludeAgentId` 发现候选子智能体。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 默认值 | 说明 |
| ---------------- | --------- | -------- | ------- | --------------------------------------------------------- |
| `projectId` | `string` | 否 |  | 仅返回一个项目的结果 |
| `query` | `string` | 否 |  | 按智能体名称筛选 |
| `publishedOnly` | `boolean` | 否 | `false` | 仅返回具有已发布活跃版本的智能体 |
| `excludeAgentId` | `string` | 否 |  | 要排除的智能体 ID，适用于子智能体搜索 |
| `limit` | `integer` | 否 | `50` | 限制结果数量，最多 100 条 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ----------------------- | --------- | -------------------------------------------------- |
| `data` | `array` | 匹配的智能体列表 |
| `data[].id` | `string` | 智能体唯一标识符 |
| `data[].name` | `string` | 智能体名称 |
| `data[].projectId` | `string` | 智能体所属项目 |
| `data[].published` | `boolean` | 智能体是否具有已发布的活跃版本 |
| `data[].availableInMCP` | `boolean` | 智能体是否可供 MCP 工具访问 |
| `data[].updatedAt` | `string` | 智能体最后更新时的 ISO 时间戳 |
| `count` | `integer` | 返回的智能体数量 |

#### 说明 <a href="#notes" id="notes"></a>

* 结果数量上限为 100。
* `search_agents` 与其他智能体工具不同，无论 `availableInMCP` 设置如何都会返回智能体。
* 要查找可用于 `subAgents` 配置字段的候选子智能体，请使用 `publishedOnly: true` 调用，并将当前智能体 ID 作为 `excludeAgentId` 传入。

***

### get\_agent <a href="#getagent" id="getagent"></a>

读取智能体草稿、技能、任务、自定义工具、可运行状态和 `configHash`。在 `mutate_agent` 之前调用。传入 `versionId` 可检查已发布版本快照，而非草稿。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ----------- | -------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agentId` | `string` | 是 | 要获取的智能体 ID |
| `versionId` | `string` | 否 | 读取已发布版本快照，而非草稿，例如智能体的 `activeVersionId`。快照只读，因此响应不含 `configHash`。 |

#### 返回值 <a href="#output" id="output"></a>

省略 `versionId` 时，响应描述当前草稿：

| 字段 | 类型 | 说明 |
| ----------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent` | `object` | 智能体元数据 |
| `agent.id` | `string` | 智能体 ID |
| `agent.name` | `string` | 智能体名称 |
| `agent.projectId` | `string` | 智能体所属项目 |
| `agent.published` | `boolean` | 智能体是否具有已发布的活跃版本 |
| `agent.versionId` | `string` | 草稿的内部版本指针 |
| `agent.activeVersionId` | `string \| null` | 已发布版本 ID，未发布时为 null |
| `agent.createdAt` | `string` | 智能体创建时的 ISO 时间戳 |
| `agent.updatedAt` | `string` | 智能体最后更新时的 ISO 时间戳 |
| `config` | `object` | 可编辑的智能体配置，包括模型、凭据、指令、工具等；不包含 `integrations`，该信息在下方单独返回。 |
| `configHash` | `string` | 完整持久化配置的哈希，请将其作为 `baseConfigHash` 传给 `mutate_agent` |
| `isRunnable` | `boolean` | 智能体是否具备运行所需的全部条件 |
| `missing` | `string[]` | 智能体可运行前仍需补齐的配置路径 |
| `skills` | `object` | 技能 ID 到技能内容的映射，包含 `name`、`description`、`instructions`，以及可选的 `allowedTools`、`references` |
| `tasks` | `array` | 计划任务，每个任务包含 `id`、`name`、`objective`、`cronExpression` 和 `enabled` |
| `customTools` | `array` | 自定义工具，每个工具包含 `id` 和 `descriptor`，后者包括 `name`、`description`、`inputSchema`、`outputSchema` 及相关元数据 |
| `integrations` | `array` | 已配置的 Slack、Telegram 或 Linear 集成，此处只读；请使用 `update_agent_integration` 管理。 |

提供 `versionId` 时，响应改为描述该已发布快照：

| 字段 | 类型 | 说明 |
| ------------------- | --------- | --------------------------------------------------------------------------------------- |
| `agent` | `object` | 智能体元数据，结构与上文相同 |
| `version` | `object` | 版本元数据 |
| `version.versionId` | `string` | 版本 ID |
| `version.author` | `string` | 发布此版本的用户 |
| `version.createdAt` | `string` | 此版本发布时的 ISO 时间戳 |
| `version.isActive` | `boolean` | 此版本是否为当前已发布版本 |
| `config` | `object` | 该版本的可编辑智能体配置 |
| `skills` | `object` | 该版本的技能 |
| `tasks` | `array` | 该版本的任务，每个任务包含 `id`、`name`、`objective`、`cronExpression`、`enabled` |
| `customTools` | `array` | 该版本的自定义工具 |

#### 说明 <a href="#notes" id="notes"></a>

* 版本快照响应不含 `configHash`，不能作为 `mutate_agent` 的基线；修改始终仅应用于草稿。
* 使用 `list_agent_versions` 查找可检查的 `versionId`。

***

### get\_agent\_builder\_reference <a href="#getagentbuilderreference" id="getagentbuilderreference"></a>

返回智能体配置及 `mutate_agent` 操作所需的参考，包括权威的智能体配置 JSON Schema。构建智能体前请先阅读。

#### 参数 <a href="#parameters" id="parameters"></a>

此工具不接受参数。

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| -------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `uri` | `string` | 包含相同内容的 `n8n://agents/reference` 资源 URI |
| `guide` | `string` | Markdown 指南，涵盖构建顺序、`mutate_agent` 操作、自定义工具编写、集成和 MCP 服务器验证 |
| `configSchema` | `object` | 权威的智能体配置 JSON Schema |

#### 说明 <a href="#notes" id="notes"></a>

* 支持资源的 MCP 客户端，也可从 `n8n://agents/reference` 资源读取相同内容。请参阅[智能体构建器参考资源](mcp-server-tools-reference.md#agent-builder-reference-resource)。
* 在 `create_agent` 或 `mutate_agent` 之前调用，确保配置符合当前 Schema，而不是凭猜测构造。

***

### discover\_agent\_assets <a href="#discoveragentassets" id="discoveragentassets"></a>

发现模型目录、聊天集成、可附加的工作流、已发布子智能体或 MCP 注册表服务器，为智能体配置提供实际依据。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ---------------- | -------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `projectId` | `string` | 是 | 要在其中发现资源的项目 |
| `kind` | `"models" \| "integrations" \| "workflows" \| "subagents" \| "mcpServers"` | 是 | 要发现的资源种类 |
| `query` | `string` | 否 | 用于模型 ID、`workflows`、`subagents` 或 `mcpServers` 的筛选条件。自 n8n 2.43.0 起，使用 `kind=models` 并提供 `provider` 时，`query` 仅保留 ID 包含该文本的模型，不区分大小写。较早版本对模型会忽略 `query`。 |
| `provider` | `string` | 否 | `kind=models` 的模型提供方，例如 `"openai"`、`"anthropic"`。省略时，返回不含模型列表的提供方摘要。 |
| `credentialId` | `string` | 否 | 可访问的凭据，用于向所选提供方验证实时模型列表 |
| `excludeAgentId` | `string` | 否 | `kind=subagents` 时要排除的智能体 |

#### 返回值 <a href="#output" id="output"></a>

`data` 字段的结构取决于 `kind`：

| `kind` | `data` 结构 |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `models`（无 `provider`） | `{ providers: [{ provider, name, modelCount }], hint }`，即提供方摘要。传入 `provider` 可列出其模型。 |
| `models`（有 `provider`） | `{ provider, verified, models: [{ id, name, toolCall, releaseDate?, reasoning?, cost?, limits? }], truncated, hint? }`。`verified` 为 true 时，表示列表已使用 `credentialId` 通过提供方自身 API 确认。自 n8n 2.43.0 起，`models` 最多包含 50 个条目；有更多模型匹配时，`truncated` 为 `true`，`hint` 会要求传入 `query` 按模型 ID 筛选。较早版本返回完整模型列表，不含 `truncated` 或 `hint`。 |
| `integrations` | `{ type, label, icon, credentialTypes, settingsRequired, settingsSchema?, settingsGuidance?, setupGuidance? }` 数组。Telegram 条目包含 `settingsSchema` 和 `settingsGuidance`；Slack 条目包含 `setupGuidance`，用于说明托管设置流程。 |
| `workflows` | `{ name, active, triggerType }` 数组，包含具有受支持触发器、可附加为 `type: "workflow"` 工具的工作流。 |
| `subagents` | `{ agentId, name }` 数组，包含项目中已发布的智能体，排除 `excludeAgentId`。 |
| `mcpServers` | MCP 注册表服务器数组，每个条目包含 `name`、`title`、`description`、`url`、`transport`、`authentication`、`credentialType`、`tools`、`metadata`。 |

顶层响应：`{ ok, kind, data }`。

#### 说明 <a href="#notes" id="notes"></a>

* 省略 `provider` 时，针对 `kind=models` 仅返回摘要，因为完整模型目录对多数 MCP 客户端的令牌限制而言过大。
* 对于 `kind=models`，提供 `provider` 时，n8n 最多返回 50 个模型。如果 `truncated` 为 `true`，请再次调用，将 `query` 设为所需模型 ID 的一部分。`truncated` 和 `hint` 字段自 n8n 2.43.0 起提供。
* 对于 `kind=mcpServers`，省略 `query` 可列出最多 20 个注册表服务器；传入 `query` 可按名称搜索。
* 要附加已发现的资源（工作流、子智能体或 MCP 服务器），仍须使用 `mutate_agent` 将其加入智能体配置。
* Slack 条目的 `setupGuidance` 字段自 n8n 2.43.0 起提供。

***

### create\_agent <a href="#createagent" id="createagent"></a>

创建智能体草稿，可选填初始模型、凭据、指令和常规工具配置。随后使用 `mutate_agent` 添加技能、任务和自定义工具。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ----------- | -------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `projectId` | `string` | 是 | 创建智能体的目标项目 |
| `name` | `string` | 是 | 智能体名称，最多 128 个字符 |
| `config` | `object` | 否 | 可选的初始智能体配置。必须省略 `name`、`skills`、`tasks`、`integrations`，以及所有 `tools` 中含 `type: "custom"` 的条目；顶层 `name` 会自动注入。提供 `credential` 时还必须设置 `model`。 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------ | -------- | --------------------------------------------------------------------------------------------- |
| `agent`      | `object` | `{ id, name, projectId, published: false, versionId, activeVersionId }`                       |
| `configHash` | `string` | 新建配置的哈希，请将其作为 `baseConfigHash` 传给第一次 `mutate_agent` 调用 |
| `url` | `string` | 在 n8n 编辑器中打开智能体的 URL |

#### 说明 <a href="#notes" id="notes"></a>

* 通过 MCP 创建的智能体会自动向 MCP 工具开放（`availableInMCP: true`）。
* 请先获取 [get_agent_builder_reference](mcp-server-tools-reference.md#getagentbuilderreference)，确认当前配置 Schema。
* 技能、任务和自定义工具需要服务器生成 ID，因此应在创建后使用 `mutate_agent` 添加。
* 如果初始 `config` 未通过验证，或引用了用户无权访问的凭据，则不会创建智能体。

***

### mutate\_agent <a href="#mutateagent" id="mutateagent"></a>

对智能体草稿应用一次配置、技能、任务或自定义工具修改，并返回后续修改所需的下一份 `configHash`。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ---------------- | -------- | -------- | --------------------------------------------------------------------------------------------------- |
| `agentId` | `string` | 是 | 要修改的智能体 ID |
| `baseConfigHash` | `string` | 是 | 最新 `configHash`，由 `get_agent` 或上一次成功修改返回 |
| `operation` | `object` | 是 | 要应用的修改，其字段直接位于对象中，不使用 `value` 包装，并与 `type` 同级 |

**`operation` 的变体（由 `type` 区分）：**

| `type` | 字段 | 说明 |
| ------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `config.replace` | `config: object` | 替换完整的可编辑智能体配置，不能包含 `integrations` |
| `config.patch` | `patch: array`（至少 1 个） | 应用 RFC 6902 JSON Patch 操作数组，可用操作为 `add`、`remove`、`replace`、`move`、`copy`、`test`。不接受 `/integrations` 下的路径。 |
| `skill.upsert` | `skill: object`, `skillId?: string` | 省略 `skillId` 可创建并附加新技能，提供时则替换已有技能内容 |
| `skill.delete` | `skillId: string` | 删除技能，并移除其配置引用 |
| `task.upsert` | `task: object`, `taskId?: string`, `enabled?: boolean` | 省略 `taskId` 可创建新的计划任务，提供时则替换已有任务。`task` 包含 `name`、`objective` 和 `cronExpression`，其中最后一项为标准五字段 cron 表达式。 |
| `task.delete` | `taskId: string` | 删除任务，并移除其配置引用 |
| `customTool.upsert` | `code: string` | 从源代码编译、验证、存储并附加自定义工具 |
| `customTool.delete` | `toolId: string` | 删除自定义工具，并移除其配置引用 |

#### 返回值 <a href="#output" id="output"></a>

成功时：

| 字段 | 类型 | 说明 |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------ |
| `agentId` | `string` | 智能体 ID |
| `operation` | `string` | 已应用操作的 `type` |
| `configHash` | `string` | 此次修改后的配置哈希，供下一次 `mutate_agent` 调用使用 |
| `resource` | `object` | 在技能、任务和自定义工具操作中包含：`{ type: "skill" \| "task" \| "customTool", id }` |

配置已过时时：

| 字段 | 类型 | 说明 |
| ------------ | --------- | ------------------------------------------------ |
| `ok`         | `boolean` | `false`                                          |
| `code`       | `string`  | `"stale_config"`                                 |
| `agentId` | `string` | 智能体 ID |
| `configHash` | `string` | 当前正确的配置哈希 |
| `message`    | `string`  | `"Call get_agent before retrying the mutation."` |

#### 说明 <a href="#notes" id="notes"></a>

* 每次修改都需要 `baseConfigHash`，来自 `get_agent` 或上一次成功修改。如果读取该哈希后智能体已更改，调用会返回 `stale_config`，而不应用修改；请调用 `get_agent`，再针对返回的 `configHash` 重试。
* 不能通过 `config.replace` 或 `config.patch` 更改集成（Slack、Telegram、Linear），请使用 [update_agent_integration](mcp-server-tools-reference.md#updateagentintegration)。
* 自定义工具代码只能导入 `@n8n/agents` 和 `zod`。默认导出必须是 `Tool` 构建器链，包含 `description`、`input`（Zod Schema）和 `handler`；`output` 可选。
* 调用 `config.replace` 或 `config.patch` 之前，请获取 [get_agent_builder_reference](mcp-server-tools-reference.md#getagentbuilderreference)，阅读完整配置 Schema 和示例。

***

### validate\_agent <a href="#validateagent" id="validateagent"></a>

验证智能体草稿、其附属资源引用，以及用户有权访问的凭据。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| --------- | -------- | -------- | ------------------------------- |
| `agentId` | `string` | 是 | 要验证的智能体 ID |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| --------- | ---------- | ------------------------------------------------------ |
| `valid` | `boolean` | 智能体是否有效且可运行 |
| `errors` | `string[]` | 配置 Schema 错误 |
| `missing` | `string[]` | 智能体可运行前仍需补齐的配置路径 |
| `url` | `string` | 在 n8n 编辑器中打开智能体的 URL |

#### 说明 <a href="#notes" id="notes"></a>

* 执行与 `publish_agent` 强制要求相同的验证流程，因此验证通过的结果与发布所接受的内容一致。
* 不会执行实时 MCP 服务器握手，如需握手请使用 `verify_agent_mcp_server`。
* 有效的智能体是一份已完善的草稿，验证通过并不意味着应当发布。

***

### call\_agent <a href="#callagent" id="callagent"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.35.0 起提供 `call_agent`。
{% endhint %}

通过内置 Preview（预览）聊天测试智能体草稿。使用消息请求开始或继续对话，也可在人工作出决定后恢复返回的审批。

{% hint style="warning" %}
**此工具会产生真实影响**

`call_agent` 使用真实凭据运行智能体的实际工具，因此可能修改已连接系统的数据，并向真实收件人发送消息。这不是模拟运行，请仅测试你允许与外部系统实际交互的智能体草稿。
{% endhint %}

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| --------- | -------- | -------- | -------------------------------------------------------------------------- |
| `agentId` | `string` | 是 | 要测试的智能体 ID |
| `request` | `object` | 是 | 要执行的操作，可以是 `message` 请求或 `approval` 请求，见下文 |

要开始或继续对话，请传入 `message` 请求：

| 字段 | 类型 | 必填 | 说明 |
| ----------- | ----------- | -------- | -------------------------------------------------------------------------------------------------------- |
| `type` | `"message"` | 是 | 标识请求类型 |
| `message` | `string` | 是 | 发送给智能体的消息 |
| `sessionId` | `string` | 否 | 省略时开始新会话，传入前次响应的 `sessionId` 可继续该对话 |

要恢复待处理审批，请传入 `approval` 请求：

| 字段 | 类型 | 必填 | 说明 |
| -------------- | ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type` | `"approval"` | 是 | 标识请求类型 |
| `approved` | `boolean` | 是 | 人工是否批准了待处理的工具调用 |
| `continuation` | `object` | 是 | 标识要恢复的审批。根据上一响应构建：`runId` 和 `toolCallId` 来自 `suspensions` 中的条目，`sessionId` 和 `response` 来自同一响应的顶层。 |

#### 返回值 <a href="#output" id="output"></a>

响应随 `status` 而变化，并非每次响应都包含所有字段。

| 字段 | 类型 | 说明 |
| ------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------- |
| `ok` | `boolean` | 调用是否成功 |
| `status` | `string` | 取值为 `"completed"`、`"suspended"`、`"approval_required"` 或 `"error"` |
| `response` | `string` | 智能体回复 |
| `sessionId` | `string` | 会话 ID，传回可继续对话 |
| `executionId` | `string` | 执行 ID（如果可用） |
| `suspensions` | `array` | 待处理审批，每项包含 `runId`、`toolCallId` 和 `toolName`，在 `status` 为 `"approval_required"` 时返回 |
| `approvals` | `array` | 智能体正在等待的审批，在 `status` 为 `"suspended"` 时返回 |
| `previewUrl` | `string` | 打开智能体 Preview 聊天的 URL |
| `previewAccessNote` | `string` | 说明有权运行智能体但无法打开 Preview 时应如何处理 |
| `code` | `string` | `status` 为 `"error"` 时的错误代码，例如 `session_not_found` 或 `agent_misconfigured` |
| `message` | `string` | `status` 为 `"error"` 时的错误消息 |
| `missing` | `string[]` | `code` 为 `agent_misconfigured` 时，仍需补齐的配置路径 |

#### 说明 <a href="#notes" id="notes"></a>

* 需要智能体所属项目的 `agent:execute` 作用域。
* 仅在启用智能体功能，且智能体已向 MCP 开放时可用。
* 返回的每项审批都需要人工决定，不要自动批准。
* 测试的是智能体行为，不是聊天渠道集成。
* 测试不会发布智能体，经过测试的草稿仍是草稿。

***

### verify\_agent\_mcp\_server <a href="#verifyagentmcpserver" id="verifyagentmcpserver"></a>

使用用户可访问的凭据测试 MCP 服务器，并返回可用工具。编写 `mcpServers` 配置条目前请先调用。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 默认值 | 说明 |
| --------------------- | --------------------------- | -------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `projectId` | `string` | 是 |  | 智能体所属项目 |
| `name` | `string` | 是 |  | 服务器名称，最多 64 个字符，仅允许字母、数字、`_` 和 `-` |
| `url` | `string` | 是 |  | HTTP(S) MCP 服务器端点 |
| `transport` | `"sse" \| "streamableHttp"` | 否 | `"streamableHttp"` | 要使用的 MCP 传输方式 |
| `authentication` | `string` | 否 | `"none"` | 身份验证方式：`"none"`、`"bearerAuth"`、`"headerAuth"`、`"multipleHeadersAuth"`、`"mcpOAuth2Api"`，或任何以 `McpOAuth2Api` 结尾的凭据类型名称。除 `"none"` 外，其他值均要求提供 `credential`。 |
| `credential` | `string` | 否 |  | 可访问的凭据 ID，`authentication` 不为 `"none"` 时必填 |
| `connectionTimeoutMs` | `integer` | 否 |  | 连接超时，单位毫秒，范围为 1–120,000 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------- | --------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `ok` | `boolean` | n8n 成功连接服务器并列出工具时为 `true`。自 n8n 2.44.0 起，无法连接服务器时为 `false`。 |
| `tools` | `array` | 服务器提供的工具，每项包含 `name` 和 `description` |
| `error` | `string` | 连接错误消息，在 `ok` 为 `false` 时包含。`error` 自 n8n 2.44.0 起提供。 |

#### 说明 <a href="#notes" id="notes"></a>

* 打开临时连接来验证服务器，无需先将其附加到智能体。
* `validate_agent` 不执行这项实时检查，因此未验证的 `mcpServers` 条目可能通过配置验证，却在运行时失败。
* 使用返回的工具名称填写 `toolFilter`，该字段位于智能体的 `mcpServers` 配置条目中，不要猜测名称。
* 自 n8n 2.44.0 起，无法连接服务器时，工具会返回 `ok: false`，并在 `error` 中说明原因，而不是使调用失败。请先检查 `ok`，再使用 `tools`。

***

### publish\_agent <a href="#publishagent" id="publishagent"></a>

发布有效的智能体草稿，并激活其任务和集成。传入 `versionId` 则改为重新发布一个以前发布过的版本。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ----------- | -------- | -------- | --------------------------------------------------------------------------------------------------- |
| `agentId` | `string` | 是 | 要发布的智能体 ID |
| `versionId` | `string` | 否 | 重新发布以前发布过的版本，而非当前草稿，草稿保持不变 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ----------------- | --------- | ------------------------------------------- |
| `agentId` | `string` | 智能体 ID |
| `published`       | `boolean` | `true`                                      |
| `versionId` | `string` | 已发布版本的 ID |
| `activeVersionId` | `string` | 活跃（已发布）版本 ID |
| `url` | `string` | 在 n8n 编辑器中打开智能体的 URL |

#### 说明 <a href="#notes" id="notes"></a>

* 发布草稿（未提供 `versionId`）时，会先验证草稿，不可运行则失败。重新发布版本（设置 `versionId`）时，跳过草稿验证，因为实际上线的不是该草稿。
* 仅在用户明确请求或确认发布、激活或部署后调用。完成构建不意味着获准发布。
* 激活智能体的计划任务和已配置的全部集成。

***

### unpublish\_agent <a href="#unpublishagent" id="unpublishagent"></a>

取消发布智能体，并停止其正在使用的任务和集成。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| --------- | -------- | -------- | -------------------------------- |
| `agentId` | `string` | 是 | 要取消发布的智能体 ID |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ----------------- | ---------------- | ------------------------------------ |
| `agentId` | `string` | 智能体 ID |
| `published`       | `boolean`        | `false`                              |
| `versionId` | `string` | 草稿内部版本指针 |
| `activeVersionId` | `string \| null` | 取消发布后为 `null` |

#### 说明 <a href="#notes" id="notes"></a>

* 停止计划任务和渠道集成，直到智能体重新发布。
* 草稿不变，仍可编辑。

***

### revert\_agent <a href="#revertagent" id="revertagent"></a>

从已发布版本恢复智能体草稿，覆盖草稿的配置、技能、任务和自定义工具，不会发布。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ----------- | -------- | -------- | --------------------------------------------------------------------------------------------- |
| `agentId` | `string` | 是 | 要恢复的智能体 ID |
| `versionId` | `string` | 否 | 用于恢复草稿的已发布版本，默认使用当前已发布版本 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ----------------- | ---------------- | ------------------------------------------------------------------------------------------------- |
| `agentId` | `string` | 智能体 ID |
| `versionId` | `string` | 恢复后的草稿内部版本指针 |
| `activeVersionId` | `string \| null` | 当前已发布版本 ID，此调用不改变它 |
| `configHash` | `string` | 恢复后的配置哈希，作为 `baseConfigHash` 传给下一次 `mutate_agent` 调用 |
| `url` | `string` | 在 n8n 编辑器中打开智能体的 URL |

#### 说明 <a href="#notes" id="notes"></a>

* 覆盖当前草稿，上次发布以来尚未发布的更改将丢失。
* 不会发布恢复后的草稿，如有需要请单独调用 `publish_agent`。
* 恢复前，先使用 `get_agent` 并传入 `versionId` 检查该版本。

***

### list\_agent\_versions <a href="#listagentversions" id="listagentversions"></a>

列出智能体发布历史，最新的在前。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 默认值 | 说明 |
| --------- | --------- | -------- | ------- | ------------------------------------------ |
| `agentId` | `string` | 是 |  | 智能体 ID |
| `limit` | `integer` | 否 | `20` | 限制结果数量，最多 100 条 |
| `offset` | `integer` | 否 | `0` | 分页时跳过的版本数量 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------------ | --------- | --------------------------------------------------- |
| `data` | `array` | 发布历史，最新的在前 |
| `data[].versionId` | `string` | 版本 ID |
| `data[].agentId` | `string` | 智能体 ID |
| `data[].createdAt` | `string` | 此版本发布时的 ISO 时间戳 |
| `data[].updatedAt` | `string` | 此版本最后更新时的 ISO 时间戳 |
| `data[].author` | `string` | 发布此版本的用户 |
| `data[].isActive` | `boolean` | 此版本是否为当前已发布版本 |
| `count` | `integer` | 返回的版本数量 |

#### 说明 <a href="#notes" id="notes"></a>

* 将此列表中的 `versionId` 传给 `get_agent`，在 `revert_agent` 或 `publish_agent` 前检查版本。

***

### update\_agent\_integration <a href="#updateagentintegration" id="updateagentintegration"></a>

配置或断开 Slack、Telegram 或 Linear 对话集成。这是管理集成的唯一方式，`config.replace` 和 `config.patch`（属于 `mutate_agent`）无法更改集成。对于 Slack，n8n 建议首次连接不传 `credentialId`，让 n8n 为智能体创建 Slack 应用。也可连接已有的 `slackApi` 凭据。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ---------------------- | --------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agentId` | `string` | 是 | 智能体 ID |
| `action` | `"connect" \| "disconnect"` | 是 | 连接还是断开集成 |
| `type` | `string` | 是 | 由 `discover_agent_assets` 返回的集成类型：`"slack"`、`"telegram"` 或 `"linear"` |
| `credentialId` | `string` | 否 | 此集成可访问的凭据。`disconnect` 时必填，Slack 之外的全部类型在 `connect` 时也必填。省略可通过托管设置连接 Slack。 |
| `managerCredentialId` | `string` | 否 | 仅用于 Slack 托管设置：`managerCredentialId`，由未提供 `credentialId` 的 Slack 连接调用返回 |
| `workspaceId` | `string` | 否 | 仅用于 Slack 托管设置：`workspaceId`，由未提供 `credentialId` 的 Slack 连接调用返回 |
| `replacesCredentialId` | `string` | 否 | `connect` 时，此凭据要替换的同类型凭据。一次操作完成两者切换，无需单独执行 `disconnect`。 |
| `settings` | `object` | 否 | 集成设置。Telegram `connect` 操作必填，其中 `accessMode` 可为 `"public"` 并带 `allowedUsers: []`，或为 `"private"` 并至少指定一个允许的 Telegram 用户。 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ----------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agentId` | `string` | 智能体 ID |
| `integration`     | `object`           | `{ type, credentialId }`                                                                                                                                                                                                                                                                                                                                               |
| `configured` | `boolean` | 在 `connect` 时包含。n8n 已保存渠道时为 `true`；返回设置步骤、等待安装批准或无法安装时为 `false`。 |
| `connected` | `boolean` | 渠道目前是否正在运行 |
| `published` | `boolean` | 智能体是否具有已发布的活跃版本 |
| `activeVersionId` | `string \| null` | 已发布版本 ID，未发布时为 null |
| `configHash` | `string` | 此次更改后的配置哈希 |
| `warning` | `string \| object` | 显式提供凭据的 Slack `connect`：返回字符串，说明 n8n 无法确认 Slack 应用，因此智能体可能收不到事件。`disconnect`：如果 n8n 无法删除外部资源，返回包含 `integrationType`、`code` 及可选 `action` URL 的对象。例如，无法删除 Slack 应用时返回 `code: "app_not_deleted"`。 |

每次调用还可返回 `ok`；失败的调用返回 `ok: false`，其中含 `code` 和 `error`。Slack `connect` 调用还可包含以下字段：

| 字段 | 类型 | 说明 |
| --------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ok` | `boolean` | 调用是否成功 |
| `status` | `string` | n8n 需要选择工作区时为 `"workspace_selection_required"`，需要人工批准 Slack 应用安装时为 `"install_approval_required"` |
| `code` | `string` | Slack 错误代码：`"slack_workspace_not_connected"`、`"slack_manager_reconnect_required"`、`"slack_managed_setup_unavailable"` 或 `"slack_app_built_for_another_agent"` |
| `error` | `string` | 发生的问题 |
| `managerCredentials` | `array` | 项目中的 Slack 工作区凭据，每项含 `managerCredentialId` 和 `name`。对于 `status: "workspace_selection_required"`，仅列出可直接使用的凭据及其 `workspaces`；对于 `code: "slack_manager_reconnect_required"`，列出需要重新连接的凭据。 |
| `managerCredentials[].workspaces` | `array` | 凭据涵盖的工作区，每项含 `workspaceId`、`name` 和 `connected`。`connected: true` 表示智能体已有该工作区的机器人凭据，此时条目还包含该 `credentialId`。 |
| `appId` | `string` | Slack 应用 ID，托管安装后及 `status` 为 `"install_approval_required"` 时包含 |
| `installUrl` | `string` | 用户打开以批准 Slack 应用安装的 URL，在 `status` 为 `"install_approval_required"` 时包含 |
| `agentUrl` | `string` | 在 n8n 中打开智能体的 URL，用户可在其中使用 **Add channel**（添加渠道） |
| `nextStep` | `string` | 下一步应执行的操作 |
| `slackApp.requestUrl` | `string` | Slack 应用必须发送 Event Subscriptions 和 Interactivity 请求的目标 URL |
| `slackApp.manifest` | `object` | 用于手动设置的 Slack 应用清单 |
| `slackApp.configuredForAgent` | `boolean` | 仅当凭据背后的 Slack 应用由 n8n 为此智能体创建时，才为 `true` |

#### 说明 <a href="#notes" id="notes"></a>

* 配置集成绝不会发布智能体。如果智能体已发布，连接会立即启用渠道；否则渠道保持停用，直到调用 `publish_agent`。
* 断开连接会立即关闭正在使用的渠道，无论智能体是否已发布。
* 为已发布智能体连接渠道前，请先与用户确认，因为连接会立即生效。
* Slack 托管设置自 n8n 2.43.0 起提供，包括 `managerCredentialId` 和 `workspaceId` 参数，以及 `status`、`code`、`managerCredentials`、`appId`、`installUrl`、`agentUrl`、`nextStep`、`slackApp` 字段。自 n8n 2.43.0 起，`credentialId` 对 Slack `connect` 可选；较早版本每次调用都要求 `credentialId`，会返回 `configured: true`（适用于任何可访问的 `slackApi` 凭据），不会检查 Slack 应用。
* Slack 应用只会将事件发送到其自身配置的请求 URL，因此 Slack 渠道仅能与指向此智能体的 Slack 应用配合。为 Slack Trigger 或其他智能体等用途创建的 `slackApi` 凭据，可能通过全部凭据检查，但此智能体仍收不到事件。
* 连接 Slack 时，首次调用传入 `action: "connect"`、`type: "slack"`，不传 `credentialId`。此时不会更改任何内容，n8n 会返回可为智能体创建 Slack 应用的工作区，或用户需要在 n8n 中完成的步骤。
* 首次调用返回 `status: "workspace_selection_required"` 时，请询问用户使用哪个工作区，并确认允许 n8n 在该处创建 Slack 应用。随后携带该 `managerCredentialId` 和 `workspaceId` 再次调用。n8n 会创建并安装 Slack 应用，再连接渠道。
* 第二次调用返回 `status: "install_approval_required"` 时，请将 `installUrl` 提供给用户。用户批准安装后，n8n 会连接渠道；调用 `get_agent` 进行确认。
* `code: "slack_app_built_for_another_agent"` 表示智能体已使用另一个 Slack 应用的机器人凭据。请先断开 `integration.credentialId`，再重新安装。
* `code: "slack_workspace_not_connected"` 表示尚无 Slack 工作区连接到 n8n。请向用户提供 `agentUrl`，让其通过 **Add channel**（添加渠道）连接一次工作区，再重试。
* `code: "slack_manager_reconnect_required"` 表示用户必须通过 **Add channel**（添加渠道）重新连接列出的 Slack 工作区凭据。请提供 `agentUrl`，然后重试。
* `code: "slack_managed_setup_unavailable"` 表示此实例无法创建 Slack 应用。请转告 `slackApp.requestUrl` 和 `slackApp.manifest`，让用户自行配置 Slack 应用，然后使用该应用的 `slackApi` 凭据连接。
* 显式使用 `slackApi` 凭据连接时，请检查 `slackApp.configuredForAgent`。如果为 `false`，请将警告及 `slackApp.requestUrl` 转告用户，不要报告渠道已就绪。
* Slack 托管安装会创建凭据，因此用户需要项目内创建凭据的权限。
* 托管设置会创建自己的凭据，不要将 `credentialId`、`replacesCredentialId` 或 `settings` 与 `managerCredentialId` 和 `workspaceId` 一起传入。
* 断开连接必须提供 `credentialId`。`managerCredentialId` 和 `workspaceId` 仅适用于 `connect`。

***

### delete\_agent <a href="#deleteagent" id="deleteagent"></a>

永久删除智能体及其关联资源。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| --------- | -------- | -------- | ----------------------------- |
| `agentId` | `string` | 是 | 要删除的智能体 ID |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| --------- | --------- | ---------------------- |
| `deleted` | `boolean` | `true`                 |
| `agentId` | `string` | 已删除智能体的 ID |

#### 说明 <a href="#notes" id="notes"></a>

* 此操作无法撤销。

***

### 智能体构建器参考资源 <a href="#agent-builder-reference-resource" id="agent-builder-reference-resource"></a>

对于支持资源的 MCP 客户端，n8n 还将智能体构建器参考作为资源提供；不支持资源的客户端可使用 [get_agent_builder_reference](mcp-server-tools-reference.md#getagentbuilderreference) 工具。

| 属性 | 值 |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URI | `n8n://agents/reference` |
| MIME 类型 | `text/markdown` |
| 内容 | 相同的构建顺序指南、`mutate_agent` 操作目录及权威的智能体配置 JSON Schema，与 `get_agent_builder_reference` 返回的内容一致 |

***

## 用户偏好 <a id="user-preferences"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.41.0 起提供 `get_user_preferences`，自 n8n 2.42.0 起提供 `save_user_preference`、`update_user_preference` 和 `undo_user_preference`。
{% endhint %}

{% hint style="info" %}
**预览状态**

偏好属于智能体上下文管理的一部分，处于预览阶段，未来版本可能更改。&#x20;
{% endhint %}

{% hint style="info" %}
**配置**

偏好工具默认开启。如果自托管实例关闭遥测（`N8N_DIAGNOSTICS_ENABLED=false`），或无法访问 n8n 功能标志服务，工具会保持关闭。要开启，请将 `N8N_FEATURE_FLAG_OVERRIDES` 设为 `{"111_context_preferences":"variant"}`，保留 JSON 对象中的其他条目，然后重启 n8n。值必须是字符串 `"variant"`，而不是 `true`。

偏好功能关闭时，n8n 不注册这些工具，也不会在授权页面提供它们的 OAuth 作用域。
{% endhint %}

[偏好](../../build/agentic-context-management/preferences.md)是用户希望所有 AI 工具在 n8n 中工作时遵循的简短指令，例如“用英文命名节点”。这些工具让 MCP 客户端读取适用于当前用户的偏好，并保存、更改或移除偏好。

这些工具使用两个 OAuth 作用域：

| OAuth 作用域 | 授权页面标签 | 工具 |
| -------------------- | ---------------------------------------- | ------------------------------------------------------------------------ |
| `aiPreference:read` | **Read AI preferences**（读取 AI 偏好） | `get_user_preferences` |
| `aiPreference:write` | **Save, update and undo AI preferences**（保存、更新和撤销 AI 偏好） | `save_user_preference`、`update_user_preference`、`undo_user_preference` |

获得 `aiPreference:write` 的客户端也应请求 `aiPreference:read`，因为保存偏好前需要先读取。

每项偏好属于以下三个作用域之一：

| 作用域 | 适用范围 |
| ---------- | ---------------------------------------------------------------------------------------------- |
| `instance` | 实例中的所有人，仅实例所有者和管理员可写入。 |
| `user` | 当前用户，适用于所有项目，也包含保存在用户个人项目上的偏好。 |
| `project` | 某个团队项目中的所有人，项目管理员和编辑者可写入。 |

偏好具有以下限制：

* 每项偏好最多 2,000 个字符。
* 每个作用域最多保存 50 项偏好。
* 同一作用域不能有两项文本相同的偏好。

### get\_user\_preferences <a id="get_user_preferences"></a>

读取此实例、当前用户及其项目保存的偏好。n8n MCP 服务器会要求客户端在 n8n 中创建或更改任何内容（例如工作流、智能体、数据表或文件夹）之前调用此工具，并在任务后续过程中应用返回的偏好。如果偏好与用户直接提出的要求冲突，客户端应遵循用户要求，并说明搁置了哪项偏好。

#### 参数 <a id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ----------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `projectId` | `string` | 否 | 读取单个项目的偏好，而非全部项目。始终包含实例和个人偏好。项目 ID 可从 `search_projects` 获取。 |

#### 返回值 <a id="output"></a>

| 字段 | 类型 | 说明 |
| ----------------------- | --------- | --------------------------------------------------------------------------------------------------------- |
| `hasPreferences` | `boolean` | 为 `true` 表示 `preferences` 至少包含一项；为 `false` 表示未保存任何内容，或设置了 `error`。 |
| `preferences` | `array` | 所有适用偏好，依次为实例、个人、项目偏好 |
| `preferences[].id` | `string` | 偏好的稳定 ID，可传给 `update_user_preference` 或 `undo_user_preference` |
| `preferences[].scope` | `string` | 取值为 `"instance"`、`"user"`、`"project"` 之一 |
| `preferences[].project` | `string` | 团队项目名称，仅在 `scope` 为 `"project"` 时设置 |
| `preferences[].text` | `string` | 用户原样编写的偏好文本 |
| `error` | `string` | 读取失败时设置，表示偏好未知，不代表不存在 |

#### 说明 <a id="notes"></a>

* 工具每次调用都会读取已保存偏好，因此编辑后无需重新连接客户端即可生效。
* 未保存任何偏好时，文本结果会明确说明，避免客户端再次调用以查找偏好。

***

### save\_user\_preference <a id="save_user_preference"></a>

为当前用户保存新偏好，作用域为 `user`。用于用户提出的长期工作规则，例如“始终添加错误工作流”；不要用于仅针对当前任务的要求，例如“这次使用 POST 请求”。

#### 参数 <a id="parameters-1"></a>

| 名称 | 类型 | 必填 | 说明 |
| --------- | -------- | -------- | ------------------------------------------------ |
| `content` | `string` | 是 | 偏好文本，长度为 1 到 2,000 个字符 |

#### 返回值 <a id="output-1"></a>

| 字段 | 类型 | 说明 |
| ------------------ | --------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `saved` | `boolean` | 调用返回时已保存偏好，则为 `true` |
| `preference` | `object` | 已保存的偏好，`saved` 为 `false` 时不包含 |
| `preference.id` | `string` | 稳定 ID，可传给 `update_user_preference` 或 `undo_user_preference` |
| `preference.scope` | `string` | 偏好适用的人群，默认为 `"user"`，除非用户在复核表单中更改 |
| `preference.text` | `string` | 已保存的偏好文本 |
| `preference.url` | `string` | 用户可用于查看、编辑或删除偏好的设置页面 |
| `removed` | `boolean` | 用户拒绝复核表单、导致偏好被移除时，为 `true` |
| `error` | `string` | 保存或复核失败时设置 |
| `reason` | `string` | 拒绝保存的原因。`"duplicate"`：相同文本已保存；`"scope_full"`：用户需先移除一项偏好。 |

#### 说明 <a id="notes-1"></a>

* n8n 会立即保存偏好，无需确认步骤。客户端应告知用户实际保存的准确文本，并提供 `preference.url`。
* 如果客户端支持 MCP elicitation（信息征询），n8n 会在保存后显示复核表单，呈现已保存文本。用户可接受、编辑或拒绝；拒绝会移除偏好，取消表单则保留。实例所有者和管理员还可在表单中将偏好移到 **Everyone on this n8n instance**（此 n8n 实例中的所有人）。
* 如果已有偏好涵盖同一规则，请携带其 ID 调用 `update_user_preference`，而不是保存近似重复的偏好。

***

### update\_user\_preference <a id="update_user_preference"></a>

更改已保存偏好的文本、作用域或两者。用户调整已有偏好时，应使用此工具，避免重复保存。

#### 参数 <a id="parameters-2"></a>

| 名称 | 类型 | 必填 | 说明 |
| ----------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `id` | `string` | 是 | 待更改偏好的 ID，来自 `get_user_preferences` 或 `save_user_preference` |
| `content` | `string` | 否 | 新文本，最多 2,000 个字符。省略则保留文本，仅移动偏好。 |
| `scope` | `string` | 否 | 更改后偏好适用的人群，可选：`"user"`、`"project"`、`"instance"`。省略则保留当前作用域。 |
| `projectId` | `string` | 否 | 偏好要移入的项目，`scope` 为 `"project"` 时必填，可从 `search_projects` 获取项目 ID |

传入 `content`、`scope` 或两者。

#### 返回值 <a id="output-2"></a>

| 字段 | 类型 | 说明 |
| ------------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `saved` | `boolean` | 偏好现已应用更改时为 `true` |
| `preference` | `object` | 更改后的偏好，包含 `id`、`scope`、`text` 和 `url` 字段 |
| `error` | `string` | 更改被拒绝或失败时设置 |
| `reason` | `string` | 拒绝更改的原因。`"not_found"`：用户看不到此 ID 的偏好；`"duplicate"`：同一作用域中另有偏好使用此文本；`"not_permitted"`：用户无权将偏好移到所请求作用域。 |

#### 说明 <a id="notes-2"></a>

* 仅在用户要求移动偏好时，才传入 `scope`。
* 移动需要拥有从当前作用域删除偏好、并在新作用域创建偏好的权限。
* 不提供 `scope` 时，工具仅更改当前用户自己的 `user` 偏好。项目、实例或其他用户的偏好会返回 `"not_found"`。

***

### undo\_user\_preference <a id="undo_user_preference"></a>

移除 MCP 客户端为当前用户保存的偏好。适用于用户撤回刚保存的偏好，或要求忘记 MCP 客户端此前保存的偏好。

#### 参数 <a id="parameters-3"></a>

| 名称 | 类型 | 必填 | 说明 |
| ---- | -------- | -------- | ----------------------------------------------------------- |
| `id` | `string` | 是 | 待移除偏好的 ID，来自 `save_user_preference` |

#### 返回值 <a id="output-3"></a>

| 字段 | 类型 | 说明 |
| --------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `removed` | `boolean` | 偏好已移除时为 `true` |
| `id` | `string` | 调用所请求的 ID |
| `error` | `string` | 移除被拒绝或失败时设置 |
| `reason` | `string` | 取值为 `"not_found"`、`"not_permitted"`、`"failed"` 之一。`"not_found"` 表示此 ID 的偏好并非由 MCP 客户端为此用户保存。 |

#### 说明 <a id="notes-3"></a>

* 仅移除 MCP 客户端为此用户保存、且仍位于 `user` 作用域的偏好。用户在设置中手动编写、n8n Assistant 保存，以及项目或实例级别的偏好都会被拒绝；这些偏好由用户在 **Settings**（设置）> **Context**（上下文）> **Preferences**（偏好）中移除。

***

## 数据表 <a href="#data-tables" id="data-tables"></a>

### search\_data\_tables <a href="#searchdatatables" id="searchdatatables"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.16.0 起提供 `search_data_tables`。
{% endhint %}

搜索当前用户有权访问的数据表。在修改数据表或向其中添加数据前，可使用此工具查找数据表 ID。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ----------- | --------- | -------- | ----------------------------------------------------------- |
| `query` | `string` | 否 | 按数据表名称筛选，不区分大小写的部分匹配 |
| `projectId` | `string` | 否 | 按项目 ID 筛选 |
| `limit` | `integer` | 否 | 限制结果数量，最多 100 条 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------------------ | --------- | ----------------------------------------------------------------------- |
| `data` | `array` | 符合查询的数据表列表 |
| `data[].id` | `string` | 数据表唯一标识符 |
| `data[].name` | `string` | 数据表名称 |
| `data[].projectId` | `string` | 此数据表所属项目 |
| `data[].createdAt` | `string` | 数据表创建时的 ISO 时间戳 |
| `data[].updatedAt` | `string` | 数据表最后更新时的 ISO 时间戳 |
| `data[].columns` | `array` | 此数据表定义的列 |
| `data[].columns[].id` | `string` | 列唯一标识符 |
| `data[].columns[].name` | `string` | 列名 |
| `data[].columns[].type` | `string` | 列数据类型，可选：`"string"`、`"number"`、`"boolean"`、`"date"` |
| `data[].columns[].index` | `integer` | 列在表中的位置 |
| `count` | `integer` | 匹配数据表总数 |

#### 说明 <a href="#notes" id="notes"></a>

* 结果数量上限为 100。

***

### create\_data\_table <a href="#createdatatable" id="createdatatable"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.16.0 起提供 `create_data_table`。
{% endhint %}

使用指定列创建新数据表。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ---------------- | -------- | ----------- | ----------------------------------------------------------------------------------------------------- |
| `projectId` | `string` | 是 | 创建数据表的目标项目 ID |
| `name` | `string` | 是 | 数据表名称，1 到 128 个字符，必须在项目内唯一 |
| `columns` | `array` | 是（至少 1 个） | 要在数据表中创建的列 |
| `columns[].name` | `string` | 是 | 列名，必须以字母开头，仅包含字母、数字和下划线，最多 63 个字符 |
| `columns[].type` | `string` | 是 | 列数据类型，可选：`"string"`、`"number"`、`"boolean"`、`"date"` |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ----------- | -------- | ----------------------------------------------- |
| `id` | `string` | 新建数据表的唯一标识符 |
| `name` | `string` | 新建数据表的名称 |
| `projectId` | `string` | 新建数据表的项目 ID |

#### 说明 <a href="#notes" id="notes"></a>

* 至少需要一列。
* 表名必须在项目内唯一。
* 列名必须符合模式 `^[a-zA-Z][a-zA-Z0-9_]*$`，最多 63 个字符。

***

### add\_data\_table\_column <a href="#adddatatablecolumn" id="adddatatablecolumn"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.16.0 起提供 `add_data_table_column`。
{% endhint %}

向已有数据表添加新列。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------------- | -------- | -------- | ----------------------------------------------------------------------------------------------------- |
| `dataTableId` | `string` | 是 | 要添加列的数据表 ID |
| `projectId` | `string` | 是 | 数据表所属项目 ID |
| `name` | `string` | 是 | 列名，必须以字母开头，仅包含字母、数字和下划线，最多 63 个字符 |
| `type` | `string` | 是 | 新列的数据类型，可选：`"string"`、`"number"`、`"boolean"`、`"date"` |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------- | --------- | ------------------------------- |
| `success` | `boolean` | 操作是否成功 |
| `message` | `string` | 结果说明 |
| `column` | `object` | 新建的列 |
| `column.id` | `string` | 列唯一标识符 |
| `column.name` | `string` | 列名 |
| `column.type` | `string` | 列数据类型 |

#### 说明 <a href="#notes" id="notes"></a>

* 列名必须符合模式 `^[a-zA-Z][a-zA-Z0-9_]*$`，最多 63 个字符。
* 创建后，不能通过 MCP 更改列类型。

***

### rename\_data\_table\_column <a href="#renamedatatablecolumn" id="renamedatatablecolumn"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.16.0 起提供 `rename_data_table_column`。
{% endhint %}

重命名数据表中的列。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------------- | -------- | -------- | ----------------------------------------------------- |
| `dataTableId` | `string` | 是 | 包含此列的数据表 ID |
| `projectId` | `string` | 是 | 数据表所属项目 ID |
| `columnId` | `string` | 是 | 要重命名的列 ID |
| `name` | `string` | 是 | 新列名，必须遵循列命名规则 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| ------------- | --------- | ------------------------------- |
| `success` | `boolean` | 操作是否成功 |
| `message` | `string` | 结果说明 |
| `column` | `object` | 重命名后的列 |
| `column.id` | `string` | 列唯一标识符 |
| `column.name` | `string` | 新列名 |
| `column.type` | `string` | 列数据类型 |

#### 说明 <a href="#notes" id="notes"></a>

* 新名称必须遵循列命名规则：`^[a-zA-Z][a-zA-Z0-9_]*$`，最多 63 个字符。

***

### delete\_data\_table\_column <a href="#deletedatatablecolumn" id="deletedatatablecolumn"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.16.0 起提供 `delete_data_table_column`。
{% endhint %}

从数据表删除一列，会永久移除该列及其全部数据。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------------- | -------- | -------- | ---------------------------------------------- |
| `dataTableId` | `string` | 是 | 包含此列的数据表 ID |
| `projectId` | `string` | 是 | 数据表所属项目 ID |
| `columnId` | `string` | 是 | 要删除的列 ID |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| --------- | --------- | ------------------------------- |
| `success` | `boolean` | 操作是否成功 |
| `message` | `string` | 结果说明 |

#### 说明 <a href="#notes" id="notes"></a>

* 通过 MCP 删除列后无法撤销。

***

### rename\_data\_table <a href="#renamedatatable" id="renamedatatable"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.16.0 起提供 `rename_data_table`。
{% endhint %}

重命名已有数据表。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------------- | -------- | -------- | ------------------------------------------------------ |
| `dataTableId` | `string` | 是 | 要重命名的数据表 ID |
| `projectId` | `string` | 是 | 数据表所属项目 ID |
| `name` | `string` | 是 | 数据表的新名称，1 到 128 个字符 |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| --------- | --------- | ------------------------------- |
| `success` | `boolean` | 操作是否成功 |
| `message` | `string` | 结果说明 |

#### 说明 <a href="#notes" id="notes"></a>

* 名称必须在项目内唯一。

***

### add\_data\_table\_rows <a href="#adddatatablerows" id="adddatatablerows"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.16.0 起提供 `add_data_table_rows`。
{% endhint %}

向已有数据表插入行，每行是将列名映射到值的对象。

#### 参数 <a href="#parameters" id="parameters"></a>

| 名称 | 类型 | 必填 | 说明 |
| ------------- | -------- | --------------------- | --------------------------------------------------------------------------------------------------------- |
| `dataTableId` | `string` | 是 | 要插入行的数据表 ID |
| `projectId` | `string` | 是 | 数据表所属项目 ID |
| `rows` | `array` | 是（至少 1 个，最多 1000 个） | 行对象数组，每个对象将列名映射到值（`string`、`number`、`boolean` 或 `null`） |

#### 返回值 <a href="#output" id="output"></a>

| 字段 | 类型 | 说明 |
| --------------- | --------- | -------------------------------------- |
| `success` | `boolean` | 插入操作是否成功 |
| `insertedCount` | `integer` | 成功插入的行数 |

#### 说明 <a href="#notes" id="notes"></a>

* 每次调用最多 1000 行。
* 行值必须为 `string`、`number`、`boolean` 或 `null`。
* 行对象中的列名必须与数据表中已有列名匹配。

## 相关资源 <a id="related-resources"></a>

* [连接 n8n MCP 服务器](../connect-to-n8n-mcp-server.md)
* [MCP 客户端连接示例](mcp-client-examples.md)
