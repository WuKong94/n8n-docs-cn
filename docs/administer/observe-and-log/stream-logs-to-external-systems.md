---
description: 将 n8n 事件以流式方式发送到日志工具。
contentType: howto
nodeTitle: 向外部系统发送日志流
originalFilePath: log-streaming.md
originalUrl: https://docs.n8n.io/log-streaming
url: https://docs.n8n.io/administer/observe-and-log/stream-logs-to-external-systems
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 日志流 <a href="#log-streaming" id="log-streaming"></a>

{% hint style="info" %}
**功能可用范围**

日志流可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**Enterprise。
{% endhint %}

日志流允许将 n8n 事件发送到自己的日志工具，从而将 n8n 监控纳入现有告警和日志流程。

## 设置日志流 <a href="#set-up-log-streaming" id="set-up-log-streaming"></a>

要使用日志流，需要添加一个发送目标。

1. 前往 **Settings**（设置）> **Log Streaming**（日志流）。
2. 选择 **Add new destination**（添加新目标）。
3. 选择目标类型。n8n 会打开 **New Event Destination**（新建事件目标）弹窗。
4. 在 **New Event Destination**（新建事件目标）弹窗中填写配置，具体内容取决于所用目标类型。
5. 选择 **Events**（事件），指定要发送的事件。
6. 选择 **Save**（保存）。

{% hint style="info" %}
**自托管用户**

如果自托管 n8n，可以通过[环境变量](../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/logs.md#log-streaming)配置额外的日志流行为。也可使用环境变量管理发送目标，请参阅[使用环境变量配置日志流目标](#configure-using-environment-variables)。
{% endhint %}

## 各进程独立的事件日志文件 <a href="#per-process-event-log-files" id="per-process-event-log-files"></a>

n8n 会先将每个发出的事件持久化到本地日志文件，再转发到日志流目标。文件在重启后仍保留，使 n8n 能重新发送尚未送达的事件。

默认情况下，n8n 将事件日志写入 `<n8n-user-folder>/n8nEventLog.log`，在相应进程中添加 `-worker` 或 `-webhook-processor` 后缀。只有单个 n8n 进程使用该文件时，默认方式可以正常工作。

{% hint style="warning" %}
**共享可写文件系统**

如果多个 n8n 进程共享同一可写卷，例如[队列模式](../../deploy/host-n8n/configure-n8n/scaling/enable-queue-mode.md)的工作进程使用 NFS 或 EFS 上的共享持久卷，则不得写入同一个事件日志文件。多个进程并发追加可能导致内容交错或文件损坏，进而造成恢复失败和事件丢失。
{% endhint %}

为避免此问题，请在每个进程中将 [`N8N_EVENTBUS_LOGWRITER_LOGFULLPATH`](../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/logs.md#log-streaming) 设为唯一的绝对路径，并以 `.log` 结尾。n8n 原样使用配置路径，不会添加进程类型后缀，因此需要由编排系统确保各进程路径唯一。

配套变量 [`N8N_EVENTBUS_LOGWRITER_MAXTOTALMESSAGESPERFILE`](../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/logs.md#log-streaming) 限制 n8n 在恢复期间从单个事件日志文件解析的行数，避免损坏的文件耗尽进程内存。

注意：

* 未设置 `N8N_EVENTBUS_LOGWRITER_LOGFULLPATH` 时，默认行为保持不变。
* 设置此变量后，n8n 不会自动添加路径后缀，必须为每个进程提供独立的值。
* 如果以前的部署已留下共享的 `n8nEventLog-worker.log` 文件，请在启用此配置前手动将其隔离。n8n 不会自动删除旧文件。

## 事件 <a href="#events" id="events"></a>

可用事件如下。可在 **Settings**（设置）> **Log Streaming**（日志流）> **Events**（事件）中选择要发送的事件。

* Workflow（工作流）
	* Started（已开始）
	* Success（成功）
	* Failed（失败）
	* Cancelled（已取消）
* Node executions（节点执行）
	* Started（已开始）
	* Finished（已结束）
* Audit（审计）
	* User login success（用户登录成功）
	* User login failed（用户登录失败）
	* User login email conflict（用户登录邮箱冲突）
	* User signed up（用户已注册）
	* User updated（用户已更新）
	* User deleted（用户已删除）
	* User invited（已邀请用户）
	* User invitation accepted（用户已接受邀请）
	* User re-invited（已重新邀请用户）
	* User email failed（用户邮件发送失败）
	* User reset requested（已请求重置用户）
	* User reset（用户已重置）
	* User credentials created（已创建用户凭据）
	* User credentials shared（已共享用户凭据）
	* User credentials updated（已更新用户凭据）
	* User credentials deleted（已删除用户凭据）
	* User API created（已创建用户 API）
	* User API deleted（已删除用户 API）
	* User MFA enabled（用户已启用多因素身份验证）
	* User MFA disabled（用户已禁用多因素身份验证）
	* User execution deleted（已删除用户执行记录）
	* Execution data revealed（已显示执行数据）
	* Execution data reveal failed（显示执行数据失败）
	* Package installed（软件包已安装）
	* Package updated（软件包已更新）
	* Package deleted（软件包已删除）
	* n8n package import success（n8n 软件包导入成功）
	* n8n package export success（n8n 软件包导出成功）
	* n8n package export failed（n8n 软件包导出失败）
	* n8n package import failed（n8n 软件包导入失败）
	* Workflow created（工作流已创建）
	* Workflow deleted（工作流已删除）
	* Workflow updated（工作流已更新）
	* Workflow archived（工作流已归档）
	* Workflow unarchived（工作流已取消归档）
	* Workflow activated（工作流已激活）
	* Workflow deactivated（工作流已停用）
	* Workflow version updated（工作流版本已更新）
    * Workflow executed（工作流已执行）
	* Workflow waiting（工作流正在等待）
	* Workflow resumed（工作流已恢复执行）
	* Variable created（变量已创建）
	* Variable updated（变量已更新）
	* Variable deleted（变量已删除）
	* External secrets provider settings saved（外部密钥提供方设置已保存）
	* External secrets provider reloaded（外部密钥提供方已重新加载）
	* External secrets connection created（外部密钥连接已创建）
	* External secrets connection updated（外部密钥连接已更新）
	* External secrets connection deleted（外部密钥连接已删除）
	* External secrets connection tested（外部密钥连接已测试）
	* External secrets connection reloaded（外部密钥连接已重新加载）
	* Personal publishing restricted enabled（已启用个人发布限制）
	* Personal publishing restricted disabled（已禁用个人发布限制）
	* Personal sharing restricted enabled（已启用个人共享限制）
	* Personal sharing restricted disabled（已禁用个人共享限制）
	* 2FA enforcement enabled（已启用强制双因素身份验证）
	* 2FA enforcement disabled（已禁用强制双因素身份验证）
	* Token exchange succeeded（令牌交换成功）
	* Token exchange failed（令牌交换失败）
	* Token exchange embed login（通过令牌交换进行嵌入登录）
	* Token exchange embed login failed（通过令牌交换进行嵌入登录失败）
	* Token exchange identity linked（令牌交换已关联身份）
	* Token exchange user provisioned（令牌交换已预配用户）
	* Token exchange role updated（令牌交换已更新角色）
	* Role mapping roles resolved（角色映射已解析角色）
	* Role mapping rule created（角色映射规则已创建）
	* Role mapping rule updated（角色映射规则已更新）
	* Role mapping rule deleted（角色映射规则已删除）
	* Role mapping rules bulk deleted（角色映射规则已批量删除）
	* MCP OAuth completed（MCP OAuth 授权已完成）
	* MCP tool called（MCP 工具已调用）
	* MCP access updated（MCP 访问设置已更新）
* Worker（工作进程）
	* Started（已开始）
	* Stopped（已停止）
* AI node logs（AI 节点日志）
	* Memory get messages（记忆组件获取消息）
	* Memory added message（记忆组件已添加消息）
	* Output parser parsed（输出解析器已完成解析）
	* Retriever get relevant documents（检索器获取相关文档）
	* Embeddings embedded document（已为文档生成嵌入）
	* Embeddings embedded query（已为查询生成嵌入）
	* Document processed（文档已处理）
	* Text splitter split（文本分割器已完成分割）
	* Tool called（工具已调用）
	* Vector store searched（向量存储已搜索）
	* LLM generated（LLM 已生成输出）
	* LLM error（LLM 出错）
	* Vector store populated（向量存储已填充）
	* Vector store updated（向量存储已更新）
* Runner（任务运行器）
	* Task requested（已请求任务）
	* Response received（已收到响应）
* Queue（队列）
	* Job enqueued（作业已入队）
	* Job dequeued（作业已出队）
	* Job completed（作业已完成）
	* Job failed（作业失败）
	* Job stalled（作业停滞）

有两组审计事件提到软件包，但两者无关。**Package installed**（软件包已安装）、**Package updated**（软件包已更新）和 **Package deleted**（软件包已删除）针对实例中安装的[社区节点](../../integrations/community-nodes/installation-and-management/README.md)；**n8n package** 事件则针对 [n8n 软件包](../../build/manage-workflows/n8n-packages/README.md)，即在实例间迁移工作流使用的可移植归档文件。

### 工作流事件 <a id="workflow-events"></a>

四种 **Workflow**（工作流）事件涵盖单次工作流执行的生命周期。

| 事件名称 | 发送时机 |
|---|---|
| `n8n.workflow.started` | 工作流执行开始。 |
| `n8n.workflow.success` | 工作流执行结束且未出错。 |
| `n8n.workflow.failed` | 工作流执行结束并发生错误。 |
| `n8n.workflow.cancelled` | 用户或其他机制取消正在运行的执行。 |

要发送全部四种事件，请将目标订阅到 `n8n.workflow`。这些事件位于 **Settings**（设置）> **Log Streaming**（日志流）> **Events**（事件）的 **Workflow**（工作流）组中。

每个事件都携带 `executionId`、`workflowId` 和 `workflowName`。

`n8n.workflow.started`、`n8n.workflow.success` 和 `n8n.workflow.failed` 还携带：

| 字段 | 说明 |
|---|---|
| `userId` | 执行的所属用户。如果执行由 n8n 自身启动，例如由定时触发器启动，则不包含此字段。 |
| `mode` | 执行模式，例如 `trigger`、`manual`、`webhook` 或 `retry`。 |
| `isManual` | 用户从编辑器手动启动执行时为 `true`。 |
| `projectId`、`projectName` | 工作流所属的项目，仅在工作流属于某项目时包含。 |

`n8n.workflow.success` 和 `n8n.workflow.failed` 还携带布尔值 `success`：成功事件中为 `true`，失败事件中为 `false`。

`n8n.workflow.failed` 额外携带：

| 字段 | 说明 |
|---|---|
| `lastNodeExecuted` | 执行失败时正在运行的节点名称。 |
| `errorNodeType` | 该节点的类型，例如 `n8n-nodes-base.httpRequest`。 |
| `errorMessage` | 错误消息，字符串类型。 |

`n8n.workflow.cancelled` 还携带 `reason`，以字符串描述执行取消的原因。

### MCP 事件 <a id="mcp-events"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.34.0 起提供 MCP 审计事件。
{% endhint %}

三种 **MCP** 审计事件针对实例 MCP 服务器，该服务器在 **Settings**（设置）> **Instance-level MCP**（实例级 MCP）中启用，不包括使用 **MCP Server Trigger** 节点的工作流。两者区别请参阅[连接 n8n MCP 服务器](../../connect/connect-to-n8n-mcp-server.md)。

| 事件名称 | 发送时机 |
| --- | --- |
| `n8n.audit.mcp.oauth.completed` | 用户完成通过 OAuth 授权 MCP 客户端。携带 `userId`、`clientId` 和 `clientName`。 |
| `n8n.audit.mcp.tool.called` | MCP 客户端调用工具。字段见下文。 |
| `n8n.audit.mcp.access.updated` | 用户开启或关闭实例 MCP 访问。携带操作者和新的 `enabled` 值。 |

要发送全部三种事件，请将目标订阅到 `n8n.audit.mcp`。这些事件位于 **Settings**（设置）> **Log Streaming**（日志流）> **Events**（事件）的 **Audit**（审计）组中。

`n8n.audit.mcp.tool.called` 携带以下字段：

| 字段 | 说明 |
| --- | --- |
| `userId` | 客户端进行身份验证时使用其凭据的用户。 |
| `_email`、`_firstName`、`_lastName`、`globalRole` | 该用户的详细信息。 |
| `toolName` | 被调用的工具，例如 `execute_workflow`。 |
| `workflowId` | 工具操作的工作流，仅在工具针对工作流操作时包含。 |
| `status` | `success` 或 `error`。 |
| `errorMessage` | 调用失败的原因，仅在 `status` 为 `error` 时包含。 |
| `authType` | `oauth` 或 `api_key`。`api_key` 涵盖所有非 OAuth 访问令牌的 Bearer 令牌。自 n8n 2.34.0 起提供 `authType`。 |
| `clientId` | 调用时用于身份验证、且已在实例中注册的 OAuth 客户端。仅在 `authType` 为 `oauth` 时包含。自 n8n 2.34.0 起提供 `clientId`。 |
| `clientName` | 客户端自行报告的名称。 |

要按客户端衡量使用情况，请按 `clientId` 分组。它标识一次客户端注册，因此该客户端每次调用的值都相同，包括令牌刷新之后。同一产品的两个安装会分别注册并获得不同的值，因此 `clientId` 统计的是注册次数，而非产品数。`clientName` 未经验证，也不唯一，请勿用作键。

在目标上设置 `anonymizeAuditMessages` 会遮蔽用户邮箱和姓名，但不会遮蔽 `userId`、`authType` 或 `clientId`，因此仍可按这些字段分组和计数。

## 发送目标 <a href="#destinations" id="destinations"></a>

n8n 支持三种目标类型：

* syslog 服务器。
* 通用 Webhook。
* Sentry 客户端。

## 使用环境变量配置 <a href="#configure-using-environment-variables" id="configure-using-environment-variables"></a>

如果自托管 n8n，可以通过环境变量而非界面管理日志流目标，自 n8n 2.19.0 起可用。将 `N8N_LOG_STREAMING_MANAGED_BY_ENV` 设为 `true`，并在 `N8N_LOG_STREAMING_DESTINATIONS` 中以 JSON 数组提供目标。n8n 每次启动时都会重新应用这些目标，并将 **Log Streaming**（日志流）界面锁定为只读。完整方式请参阅[使用环境变量管理实例设置](../../deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables.md)。

{% include "../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/log-streaming.md" %}

### 通用字段 <a href="#common-fields" id="common-fields"></a>

无论 `type` 为何，每种目标都接受以下字段。

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `type` | `"webhook"` \| `"syslog"` \| `"sentry"` | 是 | 目标类型，决定适用哪些类型专属字段。 |
| `label` | string | 否 | 界面中显示的名称。 |
| `enabled` | boolean | 否 | 是否向目标转发事件。 |
| `subscribedEvents` | string[] | 否 | 要转发的事件名称或组前缀（例如 `n8n.audit`、`n8n.workflow`）。 |
| `anonymizeAuditMessages` | boolean | 否 | 移除 `n8n.audit.*` 事件载荷中的敏感数据。 |
| `circuitBreaker` | object | 否 | 故障保护设置，请参阅[熔断器](#circuit-breaker)。 |

### Webhook <a href="#webhook" id="webhook"></a>

| 字段 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `url` | string (URL) | 是 | - | 接收事件载荷的端点。 |
| `method` | `"GET"` \| `"POST"` \| `"PUT"` | 否 | `"POST"` | 用于发送的 HTTP 方法。 |
| `sendQuery` | boolean | 否 | `false` | 是否发送查询参数。 |
| `specifyQuery` | `"keypair"` \| `"json"` | 否 | `"keypair"` | `sendQuery` 为 `true` 时使用的查询参数格式。 |
| `queryParameters` | `{ parameters: [{ name, value }] }` | 否 | - | 以键值对提供的查询参数，在 `specifyQuery` 为 `"keypair"` 时使用。 |
| `jsonQuery` | string | 否 | `""` | JSON 字符串形式的查询参数，在 `specifyQuery` 为 `"json"` 时使用。 |
| `sendHeaders` | boolean | 否 | `false` | 是否发送请求头。 |
| `specifyHeaders` | `"keypair"` \| `"json"` | 否 | `"keypair"` | `sendHeaders` 为 `true` 时使用的请求头格式。 |
| `headerParameters` | `{ parameters: [{ name, value }] }` | 否 | - | 以键值对提供的请求头，在 `specifyHeaders` 为 `"keypair"` 时使用。 |
| `jsonHeaders` | string | 否 | `""` | JSON 字符串形式的请求头，在 `specifyHeaders` 为 `"json"` 时使用。 |
| `options` | object | 否 | `{}` | 连接级选项，请参阅 [Webhook 选项](#webhook-options)。 |

#### Webhook 选项 <a href="#webhook-options" id="webhook-options"></a>

| 字段 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `allowUnauthorizedCerts` | boolean | 否 | `false` | 忽略 SSL 证书验证。 |
| `queryParameterArrays` | `"repeat"` \| `"brackets"` \| `"indices"` | 否 | `"brackets"` | 查询参数中的数组格式，在 `sendQuery` 为 `true` 时使用。 |
| `redirect` | `{ redirect: { followRedirects, maxRedirects } }` | 否 | `{ redirect: {} }` | 跟随 HTTP 重定向。`followRedirects` 默认为 `false`；`maxRedirects` 默认为 `21`。 |
| `proxy` | `{ proxy: { protocol, host, port } }` | 否 | `{ proxy: {} }` | HTTP/HTTPS 代理。`protocol` 为 `"https"` 或 `"http"`；`host` 默认为 `"127.0.0.1"`；`port` 默认为 `9000`。 |
| `timeout` | integer ≥ 1 (ms) | 否 | `5000` | 中止前等待服务器开始响应的时间。 |
| `socket` | `{ keepAlive, maxSockets, maxFreeSockets }` | 否 | `{ keepAlive: true, maxSockets: 50, maxFreeSockets: 5 }` | 套接字池配置。`maxSockets` 和 `maxFreeSockets` 为大于等于 1 的整数。 |

```json
[
  {
    "type": "webhook",
    "label": "Audit",
    "subscribedEvents": ["n8n.audit", "n8n.workflow"],
    "anonymizeAuditMessages": true,
    "url": "https://hooks.example.com/n8n",
    "method": "POST",
    "sendHeaders": true,
    "specifyHeaders": "keypair",
    "headerParameters": {
      "parameters": [
        { "name": "Authorization", "value": "Bearer s3cret" }
      ]
    },
    "options": {
      "timeout": 5000,
      "redirect": { "redirect": { "followRedirects": true, "maxRedirects": 5 } }
    }
  }
]
```

### Syslog <a href="#syslog" id="syslog"></a>

| 字段 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `host` | string | 是 | - | Syslog 服务器主机名或 IP。 |
| `port` | number | 否 | `514` | Syslog 服务器端口。 |
| `protocol` | `"udp"` \| `"tcp"` \| `"tls"` | 否 | `"udp"` | 传输协议。 |
| `tlsCa` | string | 当 `protocol` 为 `"tls"` 时 | `""` | TLS 连接使用的 PEM 格式 CA 证书。 |
| `facility` | number | 否 | `16` | Syslog facility 代码。允许值：`0`（内核）、`1`（用户）、`3`（系统）、`13`（审计）、`14`（告警）、`16` 到 `23`（Local0 到 Local7）。 |
| `app_name` | string | 否 | `"n8n"` | 用作 Syslog `APP-NAME` 的值。 |

```json
[
  {
    "type": "syslog",
    "label": "SIEM",
    "subscribedEvents": ["n8n.audit", "n8n.workflow"],
    "host": "syslog.example.com",
    "port": 514,
    "protocol": "tls",
    "tlsCa": "-----BEGIN CERTIFICATE-----\n…\n-----END CERTIFICATE-----",
    "facility": 16,
    "app_name": "n8n"
  }
]
```

### Sentry <a href="#sentry" id="sentry"></a>

| 字段 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `dsn` | string (URL) | 是 | - | Sentry DSN 客户端密钥。 |

```json
[
  {
    "type": "sentry",
    "label": "Sentry prod",
    "subscribedEvents": ["n8n.workflow"],
    "dsn": "https://public@sentry.example.com/1"
  }
]
```

### 熔断器 <a href="#circuit-breaker" id="circuit-breaker"></a>

熔断器在重复失败后暂时停止向目标发送，避免继续给运行困难的下游服务增加负载，适用于所有目标类型。

| 字段 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `maxFailures` | integer ≥ 1 | 否 | `5` | `failureWindow` 内的失败次数达到此数值后，n8n 会停止向目标发送请求。 |
| `failureWindow` | integer ≥ 100 (ms) | 否 | `60000` | 统计失败次数的滑动窗口，早于此窗口的失败会过期。 |

```json
{ "circuitBreaker": { "maxFailures": 3, "failureWindow": 30000 } }
```

### 完整示例 <a href="#complete-example" id="complete-example"></a>

```bash
N8N_LOG_STREAMING_MANAGED_BY_ENV=true
N8N_LOG_STREAMING_DESTINATIONS='[
  {
    "type": "webhook",
    "label": "Ops webhook",
    "enabled": true,
    "subscribedEvents": ["n8n.workflow", "n8n.audit"],
    "anonymizeAuditMessages": true,
    "url": "https://hooks.example.com/n8n",
    "method": "POST",
    "sendHeaders": true,
    "specifyHeaders": "keypair",
    "headerParameters": {
      "parameters": [
        { "name": "Authorization", "value": "Bearer s3cret" }
      ]
    },
    "circuitBreaker": { "maxFailures": 5, "failureWindow": 60000 }
  },
  {
    "type": "sentry",
    "label": "Sentry prod",
    "subscribedEvents": ["n8n.workflow"],
    "dsn": "https://public@sentry.example.com/1"
  }
]'
```

## 相关资源 <a id="related-resources"></a>

* [观测与日志](./)
* [使用 Insights 跟踪使用情况](track-usage-with-insights.md)
