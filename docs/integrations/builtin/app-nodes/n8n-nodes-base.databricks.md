---
title: Databricks 节点文档
description: 了解如何在 n8n 中使用 Databricks 节点，并按照技术文档将 Databricks 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Databricks 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.databricks.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.databricks
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.databricks
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Databricks 节点 <a href="#databricks-node" id="databricks-node"></a>

使用 Databricks 节点自动处理 Databricks 中的工作，并将其与其他应用集成。n8n 内置支持多种 Databricks 功能，包括运行作业、执行 SQL 查询、管理 Unity Catalog 对象、查询机器学习模型服务端点和使用向量搜索索引。

本页列出了 Databricks 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Databricks 凭据](../credentials/databricks.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Databricks SQL（SQL 操作）
    * Execute Query（执行查询）
* File（文件）
    * Create Directory（创建目录）
    * Delete Directory（删除目录）
    * Delete File（删除文件）
    * Download File（下载文件）
    * Get File Metadata（获取文件元数据）
    * List Directory（列出目录内容）
    * Upload File（上传文件）
* Genie Agent（Genie 智能体）
    * Create Conversation Message（创建对话消息）
    * Execute Message SQL Query（执行消息 SQL 查询）
    * Get Conversation Message（获取对话消息）
    * Get Genie Agent（获取 Genie 智能体）
    * Get Query Results（获取查询结果）
    * Start Conversation（开始对话）
* Job（作业）
    * Get（获取）
    * Get Run（获取运行）
    * Get Run Output（获取运行输出）
    * Run（运行）
* Lakebase（数据库操作）
    * Delete（删除）
    * Execute Function（执行函数）
    * Get Many（获取多行）
    * Insert（插入）
    * Insert or Update（插入或更新）
    * Update（更新）
* Model Serving（模型服务）
    * Query Endpoint（查询端点）
* Unity Catalog（统一目录）
    * Create Catalog（创建目录）
    * Create Function（创建函数）
    * Create Volume（创建卷）
    * Delete Catalog（删除目录）
    * Delete Function（删除函数）
    * Delete Volume（删除卷）
    * Get Catalog（获取目录）
    * Get Function（获取函数）
    * Get Table（获取表）
    * Get Volume（获取卷）
    * List Catalogs（列出目录）
    * List Functions（列出函数）
    * List Tables（列出表）
    * List Volumes（列出卷）
    * Update Catalog（更新目录）
* Vector Search（向量搜索）
    * Create Index（创建索引）
    * Get Index（获取索引）
    * List Indexes（列出索引）
    * Query Index（查询索引）

## Job（作业）操作 <a id="job-operations"></a>

使用 **Job**（作业）资源启动已有作业的一次运行、读取运行状态和输出，以及读取作业定义。所有操作均调用 Databricks Jobs API 2.2。

### 作业、运行和任务 <a id="jobs-runs-and-tasks"></a>

Databricks 区分作业及其运行，也区分运行及其中的任务：

* **作业（job）**是定义，包括名称、任务、集群和计划。每个作业有一个作业 ID。**Get**（获取）和 **Run**（运行）操作接收作业。
* **运行（run）**是作业的一次执行。每次运行有独立的运行 ID 和 Databricks 运行页面。**Get Run**（获取运行）和 **Get Run Output**（获取运行输出）接收运行。**Run**（运行）返回其启动的运行 ID。
* **任务（task）**是运行中的一个步骤。每个任务有任务键及独立的任务运行 ID。**Get Run Output**（获取运行输出）读取运行中的所有任务，每个任务返回一个数据项。

### 选择作业或运行 <a id="select-a-job-or-run"></a>

**Job**（作业）字段用于 **Get**（获取）和 **Run**（运行），**Run**（运行）字段用于 **Get Run**（获取运行）和 **Get Run Output**（获取运行输出）。两种字段均提供三种模式：

* **From list**（从列表）：从工作区选择作业，或从所有作业的近期运行中选择一次运行。输入文字可筛选列表。运行列表显示运行名称（或 `Job <job-id>`）、结果或尚未完成运行的当前状态、UTC 开始时间以及运行 ID。
* **By ID**（按 ID）：输入数字 ID。节点拒绝任何非整数值。
* **By URL**（按 URL）：粘贴 Databricks 页面 URL。节点接受作业 URL `https://<your-workspace>/jobs/<job-id>` 和运行 URL `https://<your-workspace>/jobs/<job-id>/runs/<run-id>`，也接受这两种页面的哈希形式 `https://<your-workspace>/?o=<workspace-id>#job/<job-id>` 和 `https://<your-workspace>/?o=<workspace-id>#job/<job-id>/run/<run-id>`，可包含或省略 `?o=<workspace-id>`。

### Get（获取） <a id="get"></a>

**Get**（获取）读取 **Job**（作业）字段中所选作业的定义，返回一个数据项，其中保留 Databricks 返回的作业内容，包括 `job_id`、`creator_user_name`、`run_as_user_name`、`created_time`、`settings`，以及作业有触发器时的 `trigger_state`。节点最多读取一个作业中的 2,000 个任务、作业集群、环境或参数，超过上限则报错 `Job <job-id> has more settings entries than the node can read`。

### Get Run（获取运行） <a id="get-run"></a>

**Get Run**（获取运行）读取 **Run**（运行）字段中所选的运行，返回 Databricks 运行对象，并附加五个字段：

| 字段 | 值 |
|-------|-------|
| `run_state` | 生命周期状态，例如 `RUNNING` 或 `TERMINATED`。 |
| `run_finished` | 运行达到最终状态时为 `true`。 |
| `run_result` | 终止代码，例如 `SUCCESS`、`SUCCESS_WITH_FAILURES`、`USER_CANCELED` 或 `RUN_EXECUTION_ERROR`。运行完成前为 `null`。完整列表请参阅 [Databricks API 参考](https://docs.databricks.com/api/workspace/jobs/getrun)中的 `termination_details.code`。 |
| `run_succeeded` | 值为 `true` 表示 `run_result` 为 `SUCCESS`；其他结果均为 `false`。运行完成前为 `null`。 |
| `run_error_message` | 未成功运行的终止消息，截取至 500 个字符；其他情况为 `null`。 |

在 [If](../core-nodes/n8n-nodes-base.if.md) 节点中使用这些字段，即可根据结果分支，无需读取嵌套的 `status` 对象。

### Get Run Output（获取运行输出） <a id="get-run-output"></a>

**Get Run Output**（获取运行输出）读取一次运行中各任务产生的输出。将 **Run**（运行）设为作业运行，可获取其中所有任务；使用任务运行 ID 时，仅返回该任务的一个数据项。节点读取运行中的任务，获取每个任务的输出，每个任务返回一个数据项：

| 字段 | 值 |
|-------|-------|
| `run_id` | 请求的运行。 |
| `job_id` | 该运行所属的作业。 |
| `task_key` | 作业定义中的任务键。 |
| `task_run_id` | 此任务的运行 ID。 |
| `truncated` | Databricks 截断笔记本输出或日志时为 `true`。 |
| `notebook_output`、`sql_output`、`dbt_output`、`run_job_output`、`clean_rooms_notebook_output`、`logs`、`logs_truncated`、`error`、`error_trace`、`info`、`metadata` | 保留 Databricks 返回的任务输出。具体字段取决于任务类型。`notebook_output.result` 保存笔记本通过 `dbutils.notebook.exit()` 返回的值。`error` 说明任务失败或输出不可用的原因。 |

没有任务的运行会为运行本身返回一个数据项。Databricks 重试任务时，节点为每次尝试返回一个数据项，这些数据项的 `task_key` 相同，`task_run_id` 不同。也可读取尚未完成的运行，但仍在执行的任务还没有输出。节点最多读取一次运行中的 2,000 个任务，超过上限则报错 `Run <run-id> has more tasks than the node can read`。

### Run（运行） <a id="run"></a>

**Run**（运行）启动作业的一次运行，相当于 Databricks 中的 **Run now**（立即运行）。

| 字段 | 说明 |
|-------|-------------|
| **Job**（作业） | 要运行的作业。 |
| **Job Parameters**（作业参数） | 本次运行的作业级参数。选择 **Add Parameter**（添加参数），为每个参数输入 **Name**（名称）和 **Value**（值）。这些参数会覆盖作业定义中的默认值。节点将所有值作为字符串发送。Databricks 也接受作业中未定义的参数，并将其记录在运行中。 |
| **Wait for Completion**（等待完成） | 是否等待运行完成并返回最终运行。默认关闭。 |
| **Timeout**（超时，位于 **Options**，选项中） | 等待运行完成的最长时间，单位为秒。默认 `600`，最小 `1`。仅在启用 **Wait for Completion**（等待完成）时显示。 |

关闭 **Wait for Completion**（等待完成）时，节点立即返回新的运行 ID，作业继续在 Databricks 中运行：

```json
{
	"run_id": 41847992357943,
	"number_in_job": 41847992357943
}
```

之后将 `run_id` 传给 **Get Run**（获取运行）或 **Get Run Output**（获取运行输出），即可读取结果。

#### 等待运行完成 <a id="wait-for-the-run-to-finish"></a>

启用 **Wait for Completion**（等待完成）时，节点每 5 秒检查一次运行，直到达到最终状态（`TERMINATED`、`SKIPPED` 或 `INTERNAL_ERROR`）或达到 **Timeout**（超时）时间。取消工作流执行会停止等待。之后：

* 运行成功时，节点返回完整的 Databricks 运行对象。
* 运行以其他任何结果结束时，包括 `SUCCESS_WITH_FAILURES` 和 `USER_CANCELED`，节点均报错，错误内容为 `Job run <run-id> failed (<code>): <message>`（Databricks 未提供消息时，再次显示代码）及运行页面 URL。
* 超时后运行仍未结束时，节点报错 `Job run <run-id> did not finish within <n> seconds`。错误中包含最后状态和运行页面 URL。节点不会取消 Databricks 中的运行。请增大 **Timeout**（超时），或关闭 **Wait for Completion**（等待完成），之后使用 **Get Run**（获取运行）读取结果。

某些作业的运行时间超出工作流适合等待的时长。对于此类作业，请关闭 **Wait for Completion**（等待完成）后启动运行，再由 **Databricks Trigger**（Databricks 触发器）节点在运行结束时启动第二个工作流。

### 所需作业权限 <a id="required-job-permissions"></a>

凭据所认证的身份需要 **Workspace access**（工作区访问）授权，以及相应的作业权限：

| 操作 | 作业权限 |
|------------|-----------------------|
| **Get**（获取）、**Get Run**（获取运行）、**Get Run Output**（获取运行输出） | **CAN VIEW**（可查看） |
| **Run**（运行） | **CAN MANAGE RUN**（可管理运行） |

**CAN MANAGE**（可管理）和 **IS OWNER**（所有者）均包含上述两种权限。Databricks 仅返回该身份具有 **CAN VIEW**（可查看）权限的作业和运行，因此 **Job**（作业）和 **Run**（运行）列表也仅提供这些选项。通过 **Run**（运行）启动的运行，以作业的运行身份执行，而非凭据身份。**Get**（获取）通过 `run_as_user_name` 返回此身份，默认为作业所有者。节点中其他资源所需权限，请参阅[所需 Databricks 权限](../credentials/databricks.md#required-databricks-privileges)。

缺少权限时，Databricks 以 `PERMISSION_DENIED` 拒绝请求。n8n 将 Databricks 消息显示为错误，其中会指出缺少的权限。n8n 还会在错误说明中添加以下某条提示：

```text
Grant at least Can View on the job to the signed-in user or service principal in Databricks, then retry.
```

```text
Grant at least Can Manage Run on the job to the signed-in user or service principal in Databricks, then retry.
```

### 示例：作业运行失败时通知 <a id="example-notify-when-a-job-run-fails"></a>

此工作流为失败运行中的每个任务发送一条 Slack 消息。

1. 添加 **Databricks Trigger**（Databricks 触发器）节点。将 **Resource**（资源）设为 **Job**（作业），在 **Job**（作业）中选择作业，将 **Events**（事件）仅设为 **Run Failed**（运行失败），保持 **Simplify**（简化）开启。任何以完全成功之外的结果结束的运行，包括取消和跳过的运行，都会触发一次。输出中的 `run.id` 为运行 ID，`run.url` 为运行页面 URL，`result.code` 和 `result.message` 分别为终止代码和消息。
2. 添加 **Databricks** 节点，将 **Resource**（资源）设为 **Job**（作业），**Operation**（操作）设为 **Get Run Output**（获取运行输出）。将 **Run**（运行）设为 **By ID**（按 ID），输入表达式 `{{ $json.run.id }}`。节点会为失败运行中的每个任务返回一个数据项。
3. 添加 [Slack](n8n-nodes-base.slack/README.md) 节点，将 **Resource**（资源）设为 **Message**（消息），**Operation**（操作）设为 **Send**（发送），选择频道。可使用如下消息文本：

	```text
	Databricks run {{ $('Databricks Trigger').item.json.run.name }} failed ({{ $('Databricks Trigger').item.json.result.code }}).
	Task {{ $json.task_key }}: {{ $json.error ?? 'no error text' }}
	{{ $('Databricks Trigger').item.json.run.url }}
	```

两个 Databricks 节点可共用一个凭据。该凭据需要作业的 **CAN VIEW**（可查看）权限。请使用属于服务主体的凭据，以便人员离职或撤销同意后，触发器仍能继续工作。

若希望整个运行只发送一条消息，而非每个任务一条，请在 Slack 节点前添加 [Aggregate](../core-nodes/n8n-nodes-base.aggregate.md)（聚合）节点，或在 Slack 节点设置中开启 **Execute Once**（仅执行一次）。

## Genie Agent（Genie 智能体）操作 <a id="genie-agent-operations"></a>

所有 **Genie Agent**（Genie 智能体）操作均返回 `deep_link` 字段，内容为 Databricks 工作区中的 Genie 智能体或对话 URL。使用此字段可让用户在 Databricks 中检查 SQL 和结果。

Databricks 节点作为 [AI Agent](../cluster-nodes/root-nodes/n8n-nodes-langchain.agent/README.md)（AI 智能体）节点（第 3 版及以上版本）的工具运行时，智能体会在回复末尾添加 **Powered by Databricks Genie**（由 Databricks Genie 提供支持）标签。启用 **Require Specific Output Format**（要求特定输出格式）时会跳过此标签。Databricks 要求基于 Genie 的集成使用该标签。若希望回复链接回 Databricks，请在系统消息中指示模型在回复末尾添加 Markdown 链接，链接文字为 **Explore in Databricks**（在 Databricks 中探索），URL 为 `deep_link` 字段的值，例如 `[Explore in Databricks](<deep_link value>)`。

## Lakebase 操作 <a id="lakebase-operations"></a>

使用 **Lakebase** 资源读写 Lakebase 数据库中的行。Lakebase 是 Databricks 内的托管 Postgres 服务。所有操作均通过 HTTPS 调用 [Lakebase Data API](https://docs.databricks.com/aws/en/oltp/projects/data-api)，因此节点无需连接字符串或数据库驱动。

{% hint style="info" %}
**在 Databricks 中完成一次性设置**

Data API 默认关闭，且凭据所认证的身份需要在节点读写的每个分支上拥有 Postgres 角色。使用这些操作前，请按照[为 Data API 设置 Lakebase](../credentials/databricks.md#set-up-lakebase-for-the-data-api)完成配置。Data API 拒绝个人访问令牌，因此请将节点的 **Authentication**（身份验证）设为 **OAuth2**，并选择 Databricks OAuth2 凭据。**Authentication**（身份验证）默认为 **Access Token**（访问令牌）。
{% endhint %}

### 选择表 <a id="select-a-table"></a>

所有操作均以相同的五个字段开头，每个字段都提供 **From list**（从列表）和 **By ID**（按 ID）两种模式。

| 字段 | 值 |
|-------|-------|
| **Project**（项目） | Lakebase 项目。 |
| **Branch**（分支） | 项目的分支，例如 `production`。Lakebase 为数据库创建分支的方式，与 Git 为代码创建分支类似。 |
| **Database**（数据库） | 分支上的 Postgres 数据库，例如 `databricks_postgres`。 |
| **Schema**（模式） | 表所在的模式，默认为 `public`。列表仅提供 `public`，因为 Databricks 没有列出 Postgres 模式的端点。要使用其他模式，请选择 **By ID**（按 ID）并输入名称。Data API 必须公开该模式。 |
| **Table**（表） | 要操作的表。**Execute Function**（执行函数）改为使用 **Function**（函数）。 |

表、列和函数列表，以及 **Columns**（列）和 **Arguments**（参数）映射器，均读取项目的 OpenAPI 文档。在开启 Data API 的 **OpenAPI specification**（OpenAPI 规范）设置前，**Table**（表）、**Function**（函数）和列列表会显示错误，映射器则为空并显示提示。此时可选择 **By ID**（按 ID）并输入表名或函数名；在 **Select Rows**（选择行）、**Sort**（排序）和 **Output Columns**（输出列）中通过表达式输入列名；将 **Specify Arguments**（指定参数）设为 **Using JSON**（使用 JSON）。

节点读写已有表中的行，不会创建表。请先在 Lakebase SQL 编辑器中创建表，并授予凭据所用 Postgres 角色访问权限。

下方示例中的 `orders` 表包含 `id` 主键，以及 `status` 和 `created_at` 列。

### Get Many（获取多行） <a id="get-many"></a>

**Get Many**（获取多行）读取表中的行，每行返回一个数据项。

| 字段 | 说明 |
|-------|-------------|
| **Return All**（返回全部） | 是否返回所有匹配行。默认关闭。 |
| **Limit**（数量限制） | 返回的最大行数，默认为 `50`。仅在关闭 **Return All**（返回全部）时显示。 |
| **Select Rows**（选择行） | 行必须满足的条件。选择 **Add Condition**（添加条件），设置 **Column Name or ID**（列名或 ID）、**Condition**（条件）和 **Value**（值）。未设置条件时，节点返回所有行。 |
| **Combine Conditions**（组合条件） | **AND**（与）要求满足所有条件，**OR**（或）要求满足其中任意条件。默认为 **AND**。 |
| **Sort**（排序） | 用于排序的列。选择 **Add Sort Rule**（添加排序规则），设置 **Column Name or ID**（列名或 ID）和 **Direction**（方向）。 |
| **Output Columns**（输出列，位于 **Options**，选项中） | 要返回的列。为空时返回所有列。 |

**Condition**（条件）列表提供 **Equals**（等于）、**Not Equals**（不等于）、**Greater Than**（大于）、**Greater Than or Equal**（大于或等于）、**Less Than**（小于）、**Less Than or Equal**（小于或等于）、**Like**（模式匹配）、**Like (Case-Insensitive)**（模式匹配，忽略大小写）、**Is Null**（为空）和 **Is Not Null**（非空）。两种 **Like** 条件使用 `*` 代替 `%`，使用 `_` 匹配单个字符。**Is Null** 和 **Is Not Null** 不接受值。

节点每次请求最多读取 1,000 行，最多发送 100 次请求。发送 100 次请求仍未读到表末尾时，节点会报错，而非返回部分数据：

```text
The table holds more rows than one run can read (100000)
```

请通过 **Select Rows**（选择行）中的条件缩小结果范围，或关闭 **Return All**（返回全部）并设置 **Limit**（数量限制）。上限按请求次数而非行数计算，因此项目的 **Maximum rows**（最大行数）设置也会相应降低可读取的总行数。每次请求返回 500 行时，读取 50,000 行后就会出现相同错误。

分页需要确定的全序。开启 **Return All**（返回全部）或 **Limit**（数量限制）超过 1,000 时，节点会在你设置的 **Sort**（排序）规则之后追加表的主键。这样，排序字段相同的行仍会按固定顺序返回，避免重复或遗漏。没有主键的表也会分页，但顺序取决于 Postgres 的返回顺序。

#### 示例：读取今天失败的订单 <a id="example-read-todays-failed-orders"></a>

将 **Table**（表）设为 `orders`。在 **Select Rows**（选择行）中添加 `status` **Equals**（等于）`failed`，再添加 `created_at` **Greater Than or Equal**（大于或等于）`{{ $now.startOf('day') }}`。保持 **Combine Conditions**（组合条件）为 **AND**。在 **Sort**（排序）中添加 `created_at` **DESC**（降序）。将 **Limit**（数量限制）设为 `100`。

### Insert（插入） <a id="insert"></a>

**Insert**（插入）为每个输入数据项写入一行。

通过 **Mapping Column Mode**（列映射模式）选择值的来源：

* **Map Each Column Manually**（手动映射每列）：在节点中设置每列的值。留空的列不会发送，因此 Postgres 会应用默认值。
* **Map Automatically**（自动映射）：从输入数据项获取值，按字段名匹配列名。节点会丢弃表中不存在的字段，因此即使数据项携带前序节点产生的额外数据，也仍能写入。

节点返回数据库实际存储的行，包括 Postgres 自动填充的值，例如自增 ID 或 `now()` 默认值：

```json
{
	"id": 42,
	"sku": "SKU-1",
	"name": "Widget",
	"price": 9.5,
	"created_at": "2026-10-08T09:14:22.418Z"
}
```

列为 `NOT NULL` 且没有默认值时，映射器将其标为必填。

### Update（更新） <a id="update"></a>

**Update**（更新）修改与所选列匹配的行。

将 **Columns to match on**（用于匹配的列）设为标识行的列，通常为主键。节点查找这些列的值全部等于所提供值的行，再向这些行写入其他映射列。复合主键必须选中其全部列，否则更新可能影响超出预期的行。在 **Map Each Column Manually**（手动映射每列）中留空的列不会发送，因此保持当前值。

节点为每个更新的行返回一个数据项。未匹配到任何行时不返回数据项，也不视为错误。用于匹配的列缺少值时，操作会在发送请求前失败，以免更新非预期的行。

#### 示例：将订单标记为已发货 <a id="example-mark-an-order-as-shipped"></a>

将 **Table**（表）设为 `orders`，**Mapping Column Mode**（列映射模式）设为 **Map Each Column Manually**（手动映射每列）。将 **Columns to match on**（用于匹配的列）设为 `id`，将 `id` 设为 `{{ $json.order_id }}`，`status` 设为 `shipped`。其他列全部留空，这样只会修改 `status`。

### Insert or Update（插入或更新） <a id="insert-or-update"></a>

**Insert or Update**（插入或更新）写入行，已有匹配行时则更新该行。它使用与 **Insert**（插入）相同的 **Mapping Column Mode**（列映射模式）字段，因此值可来自节点或输入数据项。

将 **Columns to match on**（用于匹配的列）设为用于判断行是否已存在的列。这些列必须共同构成主键或唯一约束，因此复合键必须选中其全部列。没有此类约束时，操作会失败，节点会提示你在 Databricks 中添加约束。

与 **Update**（更新）不同，用于匹配的列会保留在写入的行中，因为 Postgres 从发送的行数据中读取它们。

用于匹配的列缺少值时，操作会失败。Postgres 将两个空值视为不同值，因此空值永远无法匹配已有行，每次运行都会插入重复行。

节点为每个写入的行返回一个数据项，无论是新插入还是更新。

#### 示例：持续更新订单表 <a id="example-keep-an-orders-table-up-to-date"></a>

将 **Table**（表）设为 `orders`，**Columns to match on**（用于匹配的列）设为表的主键 `id`。将 **Mapping Column Mode**（列映射模式）设为 **Map Automatically**（自动映射），使每个数据项的 `id`、`status` 和 `created_at` 字段写入同名列。表中已有该 `id` 时，节点更新该行；否则写入新行。

### Delete（删除） <a id="delete"></a>

**Delete**（删除）移除满足条件的行，使用与 **Get Many**（获取多行）相同的 **Select Rows**（选择行）和 **Combine Conditions**（组合条件）字段。

删除至少需要一个条件。Data API 自身不会附加筛选条件，不带筛选的请求会清空整张表，且无法撤销。因此节点拒绝发送此类请求。

节点为每个已删除的行返回一个数据项，供后续节点记录删除内容。未匹配到任何行时，会返回一个数据项 `{"success": true}`，因为空响应无法区分“没有匹配行”和“项目不返回已删除行”这两种情况。相同情况下，**Update**（更新）不返回数据项。

{% hint style="warning" %}
**已删除的行无法恢复**

通过 Data API 执行的删除不在工作流可回滚的事务中。请先用相同条件执行 **Get Many**（获取多行），检查删除将匹配哪些行。
{% endhint %}

#### 示例：移除较早的已取消订单 <a id="example-remove-old-canceled-orders"></a>

将 **Table**（表）设为 `orders`。在 **Select Rows**（选择行）中添加 `status` **Equals**（等于）`canceled`，再添加 `created_at` **Less Than**（小于）`{{ $now.minus({ days: 30 }) }}`。保持 **Combine Conditions**（组合条件）为 **AND**。

### Execute Function（执行函数） <a id="execute-function"></a>

**Execute Function**（执行函数）调用模式中的 Postgres 函数，并返回函数结果。角色需要该函数的 `EXECUTE` 权限。

通过 **Specify Arguments**（指定参数）选择参数传递方式：

* **Using Fields Below**（使用下方字段）：节点读取函数签名，为每个参数显示一个字段，并标记必填参数。可选参数留空时使用函数默认值。布尔参数始终发送开关当前值，因此无法回退到默认值。
* **Using JSON**（使用 JSON）：在 **Arguments (JSON)**（参数，JSON）中填写 JSON 对象，每个参数对应一个键，例如 `{ "a": 1, "b": 2 }`。

节点的返回内容取决于函数的返回值：

| 函数返回值 | 节点返回内容 |
|----------------------|------------------|
| 单个值 | 一个数据项，值位于 `result` 中 |
| `TABLE (...)` 或 `SETOF <table>` | 每行一个数据项，结构与 **Get Many**（获取多行）相同 |
| `void` | 一个数据项 `{"success": true}` |

#### 示例：调用返回数字的函数 <a id="example-call-a-function-that-returns-a-number"></a>

对于此函数：

```sql
CREATE FUNCTION add_numbers(a integer, b integer)
RETURNS integer
LANGUAGE sql
AS $$ SELECT a + b $$;
```

在 **Function**（函数）中选择 `add_numbers`，保持 **Specify Arguments**（指定参数）为 **Using Fields Below**（使用下方字段），将 `a` 设为 `2`，`b` 设为 `3`。节点返回：

```json
{
	"result": 5
}
```

### 行级安全 <a id="row-level-security"></a>

Lakebase 是真正的 Postgres，因此行级安全也适用于 Data API。Postgres 根据所连接的 Databricks 身份对应的角色评估策略，而非根据 n8n。

两个凭据访问同一张表时，可能返回不同的行，且两者都正确。将工作流输出与 Databricks SQL 编辑器中看到的内容进行比较时，请检查两者使用的身份。

表未返回任何行时，请注意两点：

* 启用行级安全的表会隐藏所有行，直到有策略授予访问权限。结果为空可能表示没有策略，而非没有数据。
* 具有 `bypassrls` 的角色可查看所有行。项目所有者具有 `DATABRICKS_SUPERUSER`，因此以所有者身份在 Databricks SQL 编辑器中查询时，即使没有策略也能看到所有行。节点以其他角色运行，因此访问同一张表时可能得到空结果。

### Lakebase 常见问题 <a id="common-lakebase-issues"></a>

| 现象 | 处理方法 |
|--------------|------------|
| `Lakebase requires OAuth2 authentication` | 节点的 **Authentication**（身份验证）设为了 **Access Token**（访问令牌）。节点会在调用 Data API 前检查此设置，因此 **Table**（表）和 **Function**（函数）列表也会出现相同错误。将 **Authentication**（身份验证）设为 **OAuth2**，并选择 Databricks OAuth2 凭据。 |
| `invalid token permissions`（`PGRST301`） | 此身份在该分支上没有 Postgres 角色。请使用 `databricks_create_role` 创建角色。如果凭据本身已过期，请重新连接。 |
| `permission denied to set role`（`42501`） | 角色未获准使用 Data API。请以角色创建者身份执行 `GRANT "<role>" TO authenticator`。项目所有者完全无法使用 Data API，因此请连接非所有者身份。 |
| `permission denied for table`、`for schema`、`for sequence` 或 `for function`（`42501`） | 角色可以访问 Data API，但没有该对象的授权。请按照[为 Data API 设置 Lakebase](../credentials/databricks.md#set-up-lakebase-for-the-data-api)执行数据授权。节点显示的 `authenticator` 提示对所有 `42501` 错误都相同，因此请阅读 Postgres 消息，而非提示。 |
| `new row violates row-level security policy`（`42501`） | 表上的策略拒绝该角色写入。请添加允许写入的策略，或使用策略允许的角色写入。 |
| **Table**（表）、**Function**（函数）或列列表报错 `Turn on the "OpenAPI specification" setting of the Data API`，或 **Columns**（列）映射器为空 | 项目未提供模式文档。请开启 **Data API** > **API** > **Advanced settings**（高级设置）> **OpenAPI specification**（OpenAPI 规范）。在开启前，可选择 **By ID**（按 ID）来指定 **Table**（表）和 **Function**（函数），通过表达式输入列名。 |
| **Arguments**（参数）映射器为空 | 模式文档没有列出函数参数。可能是函数不接受参数，也可能是项目未提供文档。若仍需传入参数，请将 **Specify Arguments**（指定参数）设为 **Using JSON**（使用 JSON）。 |
| `Could not find the table`（`PGRST205`） | 检查模式名和表名，并确认 Data API 公开了该模式。刚创建或修改表后，API 重新加载模式期间，同一请求可能首次失败，重试后成功。 |
| `Could not find the '<column>' column of '<table>' in the schema cache`（`PGRST204`） | 某个已映射的列不在表中。请重新打开节点，刷新列列表。 |
| 模式未公开（`PGRST106`） | 在项目的 Data API 设置中，将该模式添加到公开模式列表。 |
| `there is no unique or exclusion constraint matching the ON CONFLICT specification`（`42P10`） | **Columns to match on**（用于匹配的列）中的列未共同构成唯一约束或主键。请选择键的全部列，或在 Databricks 中添加约束。 |
| 主键或唯一键重复、`NOT NULL` 列出现空值、类型不匹配，或外键仍在使用 | 写入违反了表的约束规则。节点会显示 Postgres 消息并指出列名。请修正值或表定义。 |
| `The branch has no read-write compute endpoint` | 分支仅提供读取。请将节点指向具有读写计算资源的分支。 |
| `At least one condition is required` | **Delete**（删除）拒绝在没有条件时运行，因为 Data API 会清空表。请在 **Select Rows**（选择行）中添加条件。 |
| `The column to match on has no value: <columns>` | 某个输入 **Update**（更新）或 **Insert or Update**（插入或更新）的数据项，其用于匹配的列没有值。请检查映射器为这些列读取的字段。 |
| `Could not find the function`（`PGRST202`） | **Execute Function**（执行函数）无法找到该函数。请检查名称，以及角色是否具有其 `EXECUTE` 权限。 |
| **Table**（表）列表中缺少某张表 | 启用 **Follow privileges**（遵循权限）时，模式文档会隐藏角色未获授权的对象。请授予角色访问权限，或选择 **By ID**（按 ID）并输入名称。 |

上述消息涉及的角色与授权步骤，请参阅[为 Data API 设置 Lakebase](../credentials/databricks.md#set-up-lakebase-for-the-data-api)。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Databricks 集成模板](https://n8n.io/integrations/databricks)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关 API 的详细信息，请参阅 [Databricks REST API 文档](https://docs.databricks.com/api/)。

要将 Databricks 与 AI 智能体结合使用，请参阅 [Databricks Chat Model](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdatabricks.md)（聊天模型）、[Databricks Vector Store](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoredatabricks/README.md)（向量存储）、[Embeddings Databricks](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks.md)（嵌入）、[Databricks AI Agent](../cluster-nodes/root-nodes/n8n-nodes-langchain.databricksaiagent.md)（AI 智能体）和 [Databricks Lakebase Chat Memory](../cluster-nodes/sub-nodes/n8n-nodes-langchain.memorylakebasechat.md)（聊天记忆）节点，以及 [Databricks Genie One MCP 服务器](../cluster-nodes/sub-nodes/n8n-mcp-registry.databricksgenie.md)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
