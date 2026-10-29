---
description: 在 Databricks 作业运行或管道更新开始、成功或失败时启动 n8n 工作流。配置轮询触发器，或使用 Webhook 替代方案。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Databricks 触发器节点 <a id="databricks-trigger-node"></a>

使用 Databricks Trigger 节点响应 [Databricks](https://www.databricks.com/) 中的事件，并将 Databricks 与其他应用集成。Databricks 作业的一次运行或管道的一次更新开始、成功或失败时，节点会启动工作流。

{% hint style="info" %}
**凭据**

身份验证设置方法，请参阅 [Databricks 凭据](../credentials/databricks.md)。此节点接受 **Databricks**（访问令牌）和 **Databricks OAuth2 API** 凭据。
{% endhint %}

## 配置触发器 <a id="set-up-the-trigger"></a>

1. 向工作流添加 **Databricks Trigger** 节点。在节点选择器中搜索 `Databricks`，打开 **Databricks** 条目。它会将作业事件列为触发器；选择其中任意一个，然后在节点中设置 **Resource**（资源）和 **Events**（事件）。
2. 将 **Authentication**（身份验证）设为 **Access Token**（访问令牌）或 **OAuth2**，并选择凭据。对于 **OAuth2** 凭据，如果使用服务主体，将 **Grant Type**（授权类型）设为 **Client Credentials (Service Principal)**；如果使用登录用户，则设为 **Authorization Code (User)**。请参阅[使用服务主体](#use-a-service-principal)。
3. 将 **Resource**（资源）设为 **Job**（作业）以监控作业运行，或设为 **Pipeline**（管道）以监控 Databricks 管道更新。
4. 在 **Job**（作业）中选择作业，或在 **Pipeline**（管道）中选择管道。每个字段都提供三种模式：
    * **From List**（从列表选择）：从工作区中选择，输入文字可按名称筛选。管道列表也支持匹配 ID。Databricks 仅列出凭据所用身份具有 **CAN VIEW**（可查看）权限的作业。
    * **By ID**（按 ID）：输入 ID。作业 ID 是整数，例如 `281874479417551`；管道 ID 是 UUID，例如 `8199cd89-e2f5-4169-a6aa-656a24c8886d`。
    * **By URL**（按 URL）：粘贴 Databricks 中的页面 URL，例如 `https://<your-workspace>/jobs/<job-id>` 或 `https://<your-workspace>/pipelines/<pipeline-id>`。节点也接受两种页面的哈希形式，例如 `https://<your-workspace>/?o=<workspace-id>#job/<job-id>` 和 `https://<your-workspace>/?o=<workspace-id>#joblist/pipelines/<pipeline-id>`。
5. 选择用于启动工作流的 **Events**（事件）。请参阅[事件](#events)。
6. 保持 **Simplify**（简化）开启，以获得[输出](#output)中描述的结果。关闭此项则获取 Databricks 原始对象。
7. 在 **Poll Times**（轮询时间）下，选择轮询 **Mode**（模式），设置触发器检查 Databricks 的频率。默认为 **Every Minute**（每分钟）。请参阅[触发器如何轮询](#how-the-trigger-polls)。
8. 选择 **Fetch Test Event**（获取测试事件）检查配置。请参阅[测试触发器](#test-the-trigger)。
9. 发布工作流。

## 事件 <a id="events"></a>

对于每次运行或更新的每个事件，触发器都会启动一次工作流。一旦已将某次运行或更新报告为结束，就不会再次报告它，例如修复作业运行后也不会再次报告。

### 作业事件 <a id="job-events"></a>

**Resource**（资源）为 **Job**（作业）时可用，默认选择 **Run Failed**（运行失败）和 **Run Succeeded**（运行成功）。

* **Run Failed**（运行失败）：运行结束，且结果不是完全成功。包括已取消、已跳过和部分失败的运行（`SUCCESS_WITH_FAILURES`）。
* **Run Started**（运行已开始）：触发器发现作业的新运行。
* **Run Succeeded**（运行成功）：运行结束，且所有任务均成功。终止代码为 `SUCCESS`。

如果一次运行在两次轮询之间开始并结束，且你同时选择了 **Run Started**（运行已开始）及对应的最终事件，同一次执行中会产生两个数据项。此时两个数据项都携带相同的结束时间信息。

### 管道事件 <a id="pipeline-events"></a>

**Resource**（资源）为 **Pipeline**（管道）时可用，默认选择 **Update Completed**（更新已完成）和 **Update Failed**（更新失败）。

* **Update Completed**（更新已完成）：一次更新运行至完成。
* **Update Failed**（更新失败）：更新失败，或被 Databricks 取消。停止管道会取消正在运行的更新，因此停止操作会产生此事件。
* **Update Started**（更新已开始）：触发器发现管道的新更新。

{% hint style="info" %}
**连续管道**

连续管道会持续运行一次更新，直到你将其停止，因此不会发生 **Update Completed**（更新已完成）事件。管道启动或重启时发生 **Update Started**（更新已开始）；更新失败或你停止管道时发生 **Update Failed**（更新失败）。获取完成信号的方法，请参阅[通过作业监控管道](#watch-a-pipeline-through-a-job)。
{% endhint %}

## 输出 <a id="output"></a>

开启 **Simplify**（简化）后，两种资源的每个数据项都有相同的顶层键：`event`、被监控的对象（`job` 或 `pipeline`）、运行或更新、`result` 和 `timing`。**Run Started**（运行已开始）和 **Update Started**（更新已开始）中不包含 `result`。节点会移除没有值的键。

### 作业输出 <a id="job-output"></a>

| 字段 | 值 |
|-------|-------|
| `event` | `runStarted`、`runSucceeded` 或 `runFailed`。 |
| `job.id` | 作业 ID。 |
| `run.id` | 运行 ID。可将其传给 Databricks 节点的 **Get Run**（获取运行）或 **Get Run Output**（获取运行输出）操作，具体见[示例：作业运行失败时发送通知](../app-nodes/n8n-nodes-base.databricks.md#example-notify-when-a-job-run-fails)。 |
| `run.name` | 运行名称。 |
| `run.url` | Databricks 中的运行页面 URL。 |
| `run.trigger` | 启动运行的来源，例如 `ONE_TIME`。 |
| `run.creator` | 创建运行的用户或服务主体。 |
| `run.parameters` | 运行的作业参数，以名称和值的键值对表示。未设置值的参数显示其默认值。 |
| `result.state` | 生命周期状态。已结束的运行对应 `TERMINATED`。 |
| `result.code` | 终止代码，例如 `SUCCESS`、`SUCCESS_WITH_FAILURES`、`USER_CANCELED` 或 `RUN_EXECUTION_ERROR`。用户取消的运行对应 `USER_CANCELED`。`CANCELED` 表示 Databricks 取消了运行，例如运行超过最长持续时间。完整列表请参阅 [Databricks API 参考](https://docs.databricks.com/api/workspace/jobs/getrun)中的 `termination_details.code`。 |
| `result.type` | 终止类型，例如 `SUCCESS` 或 `CLIENT_ERROR`。 |
| `result.message` | 终止消息。Databricks 未提供时不存在此字段。 |
| `timing.startedAt` | UTC 开始时间。 |
| `timing.endedAt` | UTC 结束时间。运行尚未结束时不存在此字段。 |
| `timing.durationMs` | 运行时长，单位为毫秒。对于 **Run Started**（运行已开始）数据项，此值表示触发器轮询时该运行已持续的时间。 |
| `timing.queuedMs` | 运行在队列中等待的时间，单位为毫秒。 |

**Run Failed**（运行失败）数据项示例如下：

```json
{
	"event": "runFailed",
	"job": { "id": 281874479417551 },
	"run": {
		"id": 41847992357943,
		"name": "nightly-etl",
		"url": "https://adb-example.cloud.databricks.com/?o=1234567890#job/281874479417551/run/41847992357943",
		"trigger": "ONE_TIME",
		"creator": "service-principal@example.com",
		"parameters": { "fail": "true" }
	},
	"result": {
		"state": "TERMINATED",
		"code": "RUN_EXECUTION_ERROR",
		"type": "CLIENT_ERROR",
		"message": "Task main failed with message: Workload failed, see run output for details."
	},
	"timing": {
		"startedAt": "2026-09-01T13:37:18.171Z",
		"endedAt": "2026-09-01T13:37:58.640Z",
		"durationMs": 40469,
		"queuedMs": 14111
	}
}
```

### 管道输出 <a id="pipeline-output"></a>

| 字段 | 值 |
|-------|-------|
| `event` | `updateStarted`、`updateCompleted` 或 `updateFailed`。 |
| `pipeline.id` | 管道 ID。 |
| `pipeline.name` | 管道名称。Databricks 事件未携带名称时不存在此字段。 |
| `pipeline.url` | Databricks 中的管道页面 URL。 |
| `update.id` | 更新 ID。 |
| `update.url` | Databricks 中的更新页面 URL。 |
| `result.state` | `COMPLETED`、`FAILED` 或 `CANCELED`。 |
| `result.message` | Databricks 事件的消息，例如 `Update 01ee1d is COMPLETED.`。 |
| `result.errors` | 失败更新的异常。每个条目包含 `type`、`code`、`sqlState`、`message` 和 `stack`，其中 `stack` 为每个栈帧列出 `class`、`method`、`file` 和 `line`。事件没有异常时不存在此字段。 |
| `timing.startedAt` | 触发器为此更新观察到的首个进行中事件的时间。如果触发器只观察到最终事件，例如发布工作流时更新已经在运行，则不存在此字段。 |
| `timing.runningAt` | 更新进入 `RUNNING` 状态的时间。如果触发器未观察到该事件，则不存在此字段。 |
| `timing.endedAt` | 最终事件的时间。**Update Started**（更新已开始）中不存在此字段。 |
| `timing.durationMs` | `endedAt` 减去 `runningAt`，单位为毫秒。如果没有 `runningAt`，则不存在此字段。 |

**Update Completed**（更新已完成）数据项示例如下：

```json
{
	"event": "updateCompleted",
	"pipeline": {
		"id": "8199cd89-e2f5-4169-a6aa-656a24c8886d",
		"name": "orders-ingest",
		"url": "https://adb-example.cloud.databricks.com/pipelines/8199cd89-e2f5-4169-a6aa-656a24c8886d"
	},
	"update": {
		"id": "01ee1dae-da54-415a-aba8-0c8b0de503f1",
		"url": "https://adb-example.cloud.databricks.com/pipelines/8199cd89-e2f5-4169-a6aa-656a24c8886d/updates/01ee1dae-da54-415a-aba8-0c8b0de503f1"
	},
	"result": {
		"state": "COMPLETED",
		"message": "Update 01ee1d is COMPLETED."
	},
	"timing": {
		"startedAt": "2026-09-01T14:20:31.066Z",
		"runningAt": "2026-09-01T14:20:31.066Z",
		"endedAt": "2026-09-01T14:20:35.738Z",
		"durationMs": 4672
	}
}
```

### 原始输出 <a id="raw-output"></a>

关闭 **Simplify**（简化）后，每个数据项都是 Databricks 返回的对象，额外添加 `event` 键。对于作业，这是 Jobs API 列出的运行；对于管道，这是 Pipelines API 列出的 `update_progress` 事件。请参阅 Databricks API 参考中的[列出运行](https://docs.databricks.com/api/jobs/v2/list-runs)和[列出管道事件](https://docs.databricks.com/api/pipelines/v2/events)。

## 触发器如何轮询 <a id="how-the-trigger-polls"></a>

节点按 **Poll Times**（轮询时间）中的计划检查 Databricks。事件发生后，最多延迟一个轮询间隔到达工作流。如果这太慢，请参阅[通过 Webhook 在数秒内获取事件](#get-events-in-seconds-with-a-webhook)。

* 首次发布工作流时，触发器从该时刻开始监控。对于作业，不会报告此前已开始的运行。对于管道，仍会报告发布时已经在进行的更新的结束事件，但不会包含 `timing.startedAt`、`timing.runningAt` 或 `timing.durationMs`。
* 取消发布后再重新发布，触发器会从停止的位置继续，并报告未发布期间发生的事件。更改作业或管道，或切换 **Resource**（资源）时，会从当前时刻重新开始。
* Databricks 延迟列出的运行或更新仍会被触发器报告，且只报告一次。无论一次运行持续多久，触发器都会在其结束时报告。
* 如果作业在两次轮询之间启动超过 1,000 次运行，触发器会报告最近的 1,000 次，并向 n8n 日志写入警告。
* 每次轮询至少向 Databricks 发出一个请求，因此 **Every Minute**（每分钟）意味着每个触发器节点每天至少 1,440 个请求。未发现事件的轮询不会创建执行。对于每天只运行几次的作业，选择 **Every X**（每隔指定时间）并设置 10 或 15 分钟即可。管道轮询会读取其时间窗口内的所有事件，而不仅是更新事件，因此繁忙管道每次轮询的开销高于作业。

## 测试触发器 <a id="test-the-trigger"></a>

选择 **Fetch Test Event**（获取测试事件），手动运行触发器一次。对于作业，节点读取最近 25 次运行，每次运行产生一个数据项：运行进行中时为 **Run Started**（运行已开始），结束后为对应的最终事件。对于管道，节点读取最近 100 个事件，并返回其中的更新事件，一次更新可能同时返回开始和结束事件。节点按从旧到新的顺序列出数据项，仅保留 **Events**（事件）中所选的事件。如果没有匹配的运行或更新，测试不返回任何内容；例如仅选择 **Run Started** 且当前没有运行进行中时。测试不会改变已发布工作流此后报告的内容。

## 使用服务主体 <a id="use-a-service-principal"></a>

只要工作流保持发布状态，触发器就会无人值守运行，因此应使用属于服务主体的凭据，即 **Grant Type**（授权类型）设为 **Client Credentials (Service Principal)** 的 **OAuth2** 凭据。关联个人的凭据会在该人员离职或撤销同意后失效。设置步骤请参阅[使用 OAuth2（服务主体）](../credentials/databricks.md#using-oauth2-service-principal)。请跟踪密钥的到期日期，密钥过期时触发器会停止工作。

### 授予 CAN VIEW 权限 <a id="grant-can-view"></a>

凭据所用身份需要对每个被监控的作业或管道具有 **CAN VIEW**（可查看）权限，这是两种资源的最低权限级别。为作业授权时，在 Databricks 中打开作业，在 **Job details**（作业详情）面板中选择 **Edit permissions**（编辑权限）。选择用户或服务主体，将权限设为 **Can View**，再选择 **Add**（添加）和 **Save**（保存）。管道权限在管道的权限设置中授予。请参阅 Databricks 文档中的[作业权限](https://docs.databricks.com/aws/en/jobs/privileges)和[管道访问控制列表](https://docs.databricks.com/aws/en/security/auth/access-control/#lakeflow-pipelines-acls)。[所需 Databricks 权限](../credentials/databricks.md#required-databricks-privileges)表列出了凭据需要的其他权限。

## 通过 Webhook 在数秒内获取事件 <a id="get-events-in-seconds-with-a-webhook"></a>

此触发器采用轮询，因此事件发生后，最多延迟一个轮询间隔到达工作流。如果需要在数秒内收到作业事件，请让 Databricks 将事件推送到 [Webhook](../core-nodes/n8n-nodes-base.webhook/README.md) 节点。Databricks 作业通知可在运行开始、成功或失败时调用 Webhook。管道无法发送 Webhook，请参阅[通过作业监控管道](#watch-a-pipeline-through-a-job)。

开始之前：

* 必须由 Databricks 工作区管理员创建通知目标。Databricks 不对载荷签名，因此 Webhook 节点上的 Basic Auth 用户名和密码是唯一的校验方式。
* 载荷仅包含 ID，因此工作流需要使用 Databricks 节点读取运行。
* Databricks 文档未说明会重试，因此请保留 Databricks Trigger 节点，作为漏收事件的后备方案。
* Databricks 不保证调用顺序。同一次运行的 `jobs.on_success` 调用可能早于 `jobs.on_start` 调用到达，添加目标后的首次运行也可能跳过 `jobs.on_start`。请根据 `$json.body.event_type` 分支处理，而非依据调用到达顺序。
* Databricks 必须能够通过 HTTPS 访问你的 n8n 实例。如果实例为自行托管且位于防火墙后，请允许[通知目标](https://docs.databricks.com/aws/en/admin/workspace-settings/notification-destinations)页面 **Networking requirements**（网络要求）中列出的 Databricks 出站 IP 范围。

配置步骤：

1. 在 n8n 中添加 **Webhook** 节点。将 **HTTP Method**（HTTP 方法）设为 **POST**，将 **Authentication**（身份验证）设为 **Basic Auth**（基本身份验证），并创建包含 **User**（用户名）和 **Password**（密码）的 **Basic Auth** 凭据。保持 **Respond**（响应）为 **Immediately**（立即）。复制 **Production URL**（生产 URL）。
2. 在 Webhook 节点后添加 **Databricks** 节点。将 **Resource**（资源）设为 **Job**（作业），**Operation**（操作）设为 **Get Run**（获取运行）。将 **Run**（运行）设为 **By ID**（按 ID），输入表达式 `{{ $json.body.run.run_id }}`。节点会返回完整运行，包含 `run_state`、`run_result` 和 `run_error_message`。请参阅 [Get Run](../app-nodes/n8n-nodes-base.databricks.md#get-run)。
3. 发布工作流。
4. 在 Databricks 中，由工作区管理员创建目标。在顶栏中选择用户名，再选择 **Settings**（设置）。在 **Workspace admin**（工作区管理员）部分打开 **Notifications**（通知）标签页，选择 **Manage**（管理）。选择 **Add destination**（添加目标），选择 **Webhook**，输入生产 URL，以及步骤 1 中的 **User**（用户名）和 **Password**（密码），再选择 **Create**（创建）。请参阅[管理通知目标](https://docs.databricks.com/aws/en/admin/workspace-settings/notification-destinations)。
5. 在作业中打开 **Job details**（作业详情）面板，在 **Job notifications**（作业通知）下选择 **Edit notifications**（编辑通知）。选择 **Add notification**（添加通知），在 **Destination**（目标）中选择目标，勾选 **Start**（开始）、**Success**（成功）或 **Failure**（失败），再选择 **Save**（保存）。请参阅[为作业添加通知](https://docs.databricks.com/aws/en/jobs/notifications)。

随后 Databricks 会为每个事件发送一次 POST 请求，请求体位于 `$json.body`：

```json
{
	"event_type": "jobs.on_failure",
	"workspace_id": 1234567890,
	"run": { "run_id": 41847992357943 },
	"job": { "job_id": 281874479417551, "name": "nightly-etl" }
}
```

`event_type` 为 `jobs.on_start`、`jobs.on_success`、`jobs.on_failure` 或 `jobs.on_duration_warning_threshold_exceeded`。仅勾选 Databricks 中所需的选项，或使用 [If](../core-nodes/n8n-nodes-base.if.md) 节点根据 `$json.body.event_type` 分支处理。每种事件类型最多可向三个目标发送作业通知。

## 通过作业监控管道 <a id="watch-a-pipeline-through-a-job"></a>

**Pipeline**（管道）资源会监控 Databricks 管道的每次更新，无论它由什么启动。在以下三种情况下，应改为监控作业。

### 管道作为作业中的任务运行 <a id="the-pipeline-runs-as-a-task-in-a-job"></a>

当你关心整个作业时，例如管道任务后还有其他任务，请监控作业。作业只能看到由其启动的更新。若需要在 `result.errors` 中获取失败更新的异常和堆栈，请监控管道。

### 管道是连续管道 <a id="the-pipeline-is-continuous"></a>

连续管道不会产生 **Update Completed**（更新已完成）。要获取完成信号，请通过含有管道任务的触发式作业运行它。作业会将管道作为一次可完成的更新运行，因此作业的 **Run Succeeded**（运行成功）和管道的 **Update Completed**（更新已完成）事件都会发生。此时，管道会在作业运行时处理数据，而不再连续处理。

### 需要在数秒内收到事件 <a id="you-need-the-event-within-seconds"></a>

作业可发送 Webhook，管道则不行。含有管道任务的作业可让管道使用[通过 Webhook 在数秒内获取事件](#get-events-in-seconds-with-a-webhook)中的 Webhook 方式。

更多信息请参阅[作业的管道任务](https://docs.databricks.com/aws/en/jobs/tasks/pipeline)和[触发式与连续管道模式](https://docs.databricks.com/aws/en/ldp/concepts/pipeline-mode)。

## 常见问题 <a id="common-issues"></a>

### 触发器不启动工作流 <a id="the-trigger-doesnt-start-the-workflow"></a>

* 首次发布工作流时，触发器从该时刻开始监控，不会重放旧运行。请启动新的运行或更新进行测试。
* 打开 **Executions**（执行记录）列表，失败的轮询会显示在其中，并附有 Databricks 错误。
* 对于作业，缺少 **CAN VIEW**（可查看）权限不会产生错误。触发器会持续轮询且不报错，但始终不触发。请参阅[权限错误](#permission-errors)。
* 检查 **Events**（事件）的选择，默认未选择 **Run Started**（运行已开始）和 **Update Started**（更新已开始）。
* 连续管道不会产生 **Update Completed**（更新已完成），请参阅[通过作业监控管道](#watch-a-pipeline-through-a-job)。
* 尚在进行的运行只会产生 **Run Started**（运行已开始）。Databricks 报告运行结束后，才会产生对应的最终事件。
* 凭据已过期。服务主体密钥的有效期最多为 730 天，用户登录连接会在刷新令牌过期时结束。请参阅 [OAuth 密钥会过期](../credentials/databricks.md#create-a-service-principal-and-oauth-secret)和[配置令牌有效期](../credentials/databricks.md#configure-token-lifetimes)。

### 作业或管道未出现在列表中 <a id="the-job-or-pipeline-isnt-in-the-list"></a>

Databricks 仅列出凭据所用身份具有 **CAN VIEW**（可查看）权限的作业。搜索最多扫描工作区中的前 1,000 个作业或管道。可改用 **By ID**（按 ID）或 **By URL**（按 URL），或先授予 **CAN VIEW** 权限。

### 权限错误 <a id="permission-errors"></a>

凭据所用身份缺少 **CAN VIEW**（可查看）权限时，Databricks 会以 `PERMISSION_DENIED` 拒绝请求。n8n 将 Databricks 消息作为错误显示，并在描述中添加以下某条提示：

```text
Grant Can View on the job to the user or service principal of the credential, then retry.
```

```text
Grant Can View on the pipeline to the user or service principal of the credential, then retry.
```

选择 **Fetch Test Event**（获取测试事件）时，会在节点中看到此错误。在已发布的工作流中，每次失败轮询都作为失败执行出现在 **Executions**（执行记录）列表中。请参阅[授予 CAN VIEW 权限](#grant-can-view)。

对于作业，身份缺少 **CAN VIEW**（可查看）权限时，Databricks 对运行列表返回空结果，而非 `PERMISSION_DENIED`。此时 **Fetch Test Event**（获取测试事件）不返回任何内容，已发布的触发器会持续轮询且不报错，但始终不触发。唯一可见的迹象是作业不出现在 **From List**（从列表选择）选择器中。请为该作业授予 **CAN VIEW** 权限，再次选择 **Fetch Test Event**。触发器将在下次轮询中报告授权前五分钟内发生的运行。

### 作业或管道 ID 无效 <a id="invalid-job-or-pipeline-id"></a>

节点会在调用 Databricks 前检查 ID：

* `Job ID must be a whole number`：使用 Databricks 作业 URL 中显示的数字 ID。
* `Job ID is too large to send exactly`：大于 `9007199254740991` 的 ID 在 JavaScript 中会丢失精度，因此节点无法监控此作业。
* `Pipeline ID must be a UUID`：使用 Databricks 管道 URL 中显示的 ID，例如 `8199cd89-e2f5-4169-a6aa-656a24c8886d`。

### 非预期响应 <a id="unexpected-response"></a>

凭据中的 **Host**（主机）不是 Databricks 工作区 URL 时，n8n 会显示 `Databricks did not return a JSON list of job runs` 或 `Databricks did not return a JSON list of pipeline events`。请检查 **Host** 并重试。

## 相关资源 <a id="related-resources"></a>

* [Databricks 节点](../app-nodes/n8n-nodes-base.databricks.md)
* [Databricks 凭据](../credentials/databricks.md)
* [Jobs API：列出运行](https://docs.databricks.com/api/jobs/v2/list-runs)
* [Pipelines API：列出管道事件](https://docs.databricks.com/api/pipelines/v2/events)
* [Databricks 访问控制列表](https://docs.databricks.com/aws/en/security/auth/access-control/)
