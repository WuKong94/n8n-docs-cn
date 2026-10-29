---
title: 调度器环境变量
description: 配置自托管 n8n 实例持久调度器的环境变量。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 调度器
originalFilePath: hosting/configuration/environment-variables/scheduler.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/scheduler
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/scheduler
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 调度器环境变量 <a href="#scheduler-environment-variables" id="scheduler-environment-variables"></a>

以下环境变量配置持久调度器。它从数据库支持的队列中运行基于时间触发的工作流，而非依赖各实例的内存。自 n8n 2.45.0 起默认启用。其行为变化、工作原理及如何使用内存调度器，请参阅[持久调度器](../../durable-scheduler.md)。

通过 `N8N_METRICS_INCLUDE_SCHEDULER_METRICS` 和 `N8N_METRICS_SCHEDULER_INTERVAL` 启用持久调度器的 Prometheus 指标，这两个变量与其他指标变量一起列在[端点](endpoints.md)页面。各指标含义请参阅[持久调度器可观测性](../../durable-scheduler.md#observability)。

{% hint style="info" %}
**功能可用范围**

持久调度器自 n8n 2.36.0 起正式可用，更早的 n8n 2.32.0 及后续版本中作为预览功能提供。
{% endhint %}

## 启用调度器 <a href="#enable-vars" id="enable-vars"></a>

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_SCHEDULER_ENABLED` | Boolean | `true` | 是否使用持久调度器。自 n8n 2.45.0 起默认为 `true`，更早版本默认为 `false`。设为 `false` 可使用内存调度器。接管 Schedule Trigger 节点还需要 `N8N_USE_WORKFLOW_PUBLICATION_SERVICE`，该设置也默认开启。自 n8n 2.45.0 起弃用，未来版本将移除此变量和内存调度器。 |
| `N8N_SCHEDULER_POLL_TRIGGERS_ENABLED` | Boolean | `false` | 持久调度器是否也接管轮询触发器，即具有 Poll Times 参数的节点。需要 `N8N_SCHEDULER_ENABLED` 和 `N8N_USE_WORKFLOW_PUBLICATION_SERVICE`。自 n8n 2.33.0 起提供。 |
| `N8N_SCHEDULER_SYSTEM_TASKS_ENABLED` | Boolean | `false` | 是否由持久调度器运行 n8n 内部维护任务，而非使用领导者主实例中的进程内定时器。需要 `N8N_SCHEDULER_ENABLED`。所有主实例的两个变量值必须一致，并运行相同 n8n 版本。任一开关关闭的主实例都会在启动时移除这些任务的持久计划。请从 n8n 2.45.0 起使用，这是首个将全部系统任务交给持久调度器的版本。参阅[系统任务](../../system-tasks.md#run-system-tasks-on-the-durable-scheduler)。 |

n8n 2.45.0 移除了 `N8N_ENV_FEAT_SKIP_DURABLE_SCHEDULER` 和节点的 **Skip Durable Scheduler（跳过持久调度器）**设置。要让所有 Schedule Trigger 节点使用内存调度器，设置 `N8N_SCHEDULER_ENABLED=false` 并重启 n8n。参阅[使用内存调度器](../../durable-scheduler.md#use-the-in-memory-scheduler)。

{% hint style="warning" %}
轮询触发器支持尚未完全稳定。生产环境中请保持 `N8N_SCHEDULER_POLL_TRIGGERS_ENABLED` 关闭，除非你准备持续监控轮询工作流：检查执行列表是否有遗漏或重复运行，并开启调度器指标，观察调度延迟、重试和死信，参阅[持久调度器可观测性](../../durable-scheduler.md#observability)。这不影响已经稳定的 Schedule Trigger 支持。
{% endhint %}

## 轮询触发器 <a id="poll-triggers"></a>

控制具有 **Poll Times（轮询时间）**参数的触发器，例如 Google Sheets Trigger 或 Airtable Trigger：包括如何存储游标，即节点已读取位置的记录，以及单次轮询允许运行多久。要让这些节点通过持久调度器运行，请启用“启用调度器”表中的 `N8N_SCHEDULER_POLL_TRIGGERS_ENABLED`。参阅[轮询触发器](../../durable-scheduler.md#poll-triggers)。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_POLLER_DURABLE_CURSORS_ENABLED` | Boolean | `false` | 是否将轮询触发器游标保存在专用数据库表中，并与本次轮询产生的执行在同一个事务中提交，避免轮询中途崩溃导致数据丢失或重复。自 n8n 2.36.0 起提供。从 n8n 2.37.0 起，需要 `N8N_SCHEDULER_ENABLED`、`N8N_SCHEDULER_POLL_TRIGGERS_ENABLED` 和 `N8N_USE_WORKFLOW_PUBLICATION_SERVICE`。参阅[持久轮询游标](../../durable-scheduler.md#durable-poll-cursors)。 |
| `N8N_SCHEDULER_POLL_TIMEOUT` | Number | `45` | 单次轮询运行多久后被放弃，单位为秒。被放弃的轮询不会记录任何内容，游标保持不变，下次轮询重新读取相同范围，避免数据遗漏。持续超时的轮询计为失败，n8n 会逐渐延长重试间隔。超时应低于 `N8N_SCHEDULER_LEASE_DURATION`：超时计时从轮询真正开始才启动，因此允许轮询占用完整租约时长，可能在其他实例接管时仍在运行。超时达到租约时长时，n8n 启动会发出警告。必须大于 0。自 n8n 2.37.0 起提供。 |

## 物化 <a href="#materialization-vars" id="materialization-vars"></a>

控制调度器提前多久，以及多频繁地将未来运行记录到数据库中。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_SCHEDULER_MATERIALIZATION_WINDOW` | Number | `60` | 调度器提前将未来多少秒内的运行记录到数据库。窗口越大，提前提交的运行越多，更能应对停机，但存储读写也略有增加。必须大于 0。 |
| `N8N_SCHEDULER_MATERIALIZATION_INTERVAL` | Number | `10` | 扫描激活计划、记录窗口内运行的频率，单位为秒。必须大于 0。 |
| `N8N_SCHEDULER_MATERIALIZATION_TIMEOUT` | Number | `60` | 单次扫描的最长运行时长，单位为秒。超时后放弃，在下个间隔重试，避免扫描因数据库缓慢而卡住。必须大于 0。 |

## 执行 <a href="#execution-vars" id="execution-vars"></a>

控制调度器启动到期运行的频率，以及如何领取每次运行，确保同一次运行只由一个实例处理。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_SCHEDULER_EXECUTOR_INTERVAL` | Number | `5` | 检查已记录运行是否即将到期的频率，单位为秒。每次检查会领取下个间隔内到期的运行，并交给精确定时器，因此运行会在计划时刻启动，而非按轮询节奏启动。此间隔也限制调度器发现新启用或修改计划所需的最长时间。必须大于 0。 |
| `N8N_SCHEDULER_EXECUTOR_TIMEOUT` | Number | `60` | 单次到期运行检查的最长时长，单位为秒。超时后放弃，在下个间隔重试。必须大于 0。 |
| `N8N_SCHEDULER_LEASE_DURATION` | Number | `60` | 实例独占已领取运行的时长，单位为秒，防止其他实例启动同一次运行。如果实例未完成就停止，领取状态会在此时长后过期，允许其他实例接管。应明显长于运行开始所需的时间：过短可能重复运行，过长则延迟崩溃恢复。必须大于 0。 |
| `N8N_SCHEDULER_CLAIM_BATCH_SIZE` | Number | `100` | 单次领取从队列获取的运行数量上限。较大批次能更快清理积压，但每轮会给单个实例分配更多工作。必须大于 0。 |

## 恢复 <a href="#recovery-vars" id="recovery-vars"></a>

控制回收器，释放已被实例领取但从未完成的运行，让其他实例能够接手。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_SCHEDULER_REAPER_INTERVAL` | Number | `30` | 检查已被实例领取但从未完成的运行，并让其重新可用的频率，单位为秒，例如崩溃或关闭后留下的运行。必须大于 0。 |
| `N8N_SCHEDULER_REAPER_BATCH_SIZE` | Number | `100` | 回收器单轮最多回收的领取过期运行数量。较大批次可以更快恢复积压，但每轮会在一个实例上处理更多工作。必须大于 0。 |
| `N8N_SCHEDULER_REAPER_TIMEOUT` | Number | `60` | 单轮恢复的最长时长，单位为秒。超时后放弃，在下个间隔重试。必须大于 0。 |
| `N8N_SCHEDULER_MAX_ATTEMPTS` | Number | `5` | 计划运行被回收，例如崩溃后，或出错后重试的最大次数。达到上限后，n8n 会放弃并将其转为死信。实例经常重启或出现临时错误时，可提高此值；降低则会更早放弃并继续其他运行。必须大于 0。 |

## 保留期限 <a href="#retention-vars" id="retention-vars"></a>

控制调度器将已完成运行保留为历史的时长，以及删除旧记录的频率。失败和漏触发的运行会比正常运行保留更久，留出发现和调试问题的时间。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_SCHEDULER_RETENTION` | Number | `86400` | 正常结束的运行，即成功或取消，删除前保留的时长，单位为秒，默认为一天。增大可保留更多历史，减小可更早释放数据库空间。必须大于 0。 |
| `N8N_SCHEDULER_FAILED_RETENTION` | Number | `604800` | 异常运行，即失败或漏触发，删除前保留的时长，单位为秒，默认为七天。应长于 `N8N_SCHEDULER_RETENTION`，留出调试时间；设得更短时，调度器会发出警告。必须大于 0。 |
| `N8N_SCHEDULER_RETENTION_INTERVAL` | Number | `3600` | 删除超过保留期限的已完成运行的频率，单位为秒，默认为一小时。必须大于 0。 |
| `N8N_SCHEDULER_RETENTION_TIMEOUT` | Number | `300` | 单轮清理的最长时长，单位为秒，默认为五分钟。超时后放弃，在下个间隔重试。必须大于 0。 |

## 所属对象校正 <a id="owner-reconciliation"></a>

控制定期扫描，停用所属对象已不存在的计划，例如已取消发布的工作流所对应的计划。扫描会立即停止这些计划，并在宽限期后删除。参阅[持久调度器的工作原理](../../durable-scheduler.md#how-it-works)。

{% hint style="info" %}
**功能可用范围**

自 n8n 2.39.0 起提供所属对象校正功能。
{% endhint %}

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_SCHEDULER_OWNER_RECONCILIATION_ENABLED` | Boolean | `true` | 调度器是否定期检查每个计划的所属对象仍然存在，并停用所属对象缺失的计划。关闭时会保留这些计划。 |
| `N8N_SCHEDULER_OWNER_RECONCILIATION_INTERVAL` | Number | `900` | 扫描频率，单位为秒，默认为十五分钟。此扫描是兜底机制，并非常规清理路径，因此较长间隔也可以。必须大于 0。 |
| `N8N_SCHEDULER_OWNER_RECONCILIATION_TIMEOUT` | Number | `300` | 单轮扫描的最长时长，单位为秒，默认为五分钟。超时后放弃，在下个间隔重试。必须大于 0。 |
| `N8N_SCHEDULER_OWNER_RECONCILIATION_BATCH_SIZE` | Number | `500` | 每次数据库查询检查的所属对象数量。较大批次可减少扫描查询次数，较小批次可降低单次查询负担。必须在 1 到 1000 之间。 |
| `N8N_SCHEDULER_OWNER_QUARANTINE_GRACE` | Number | `86400` | 已停止的计划在删除前保留的时长，单位为秒，默认为一天。扫描发现计划后会立即停止触发，此设置仅延迟删除。必须大于 0。 |
| `N8N_SCHEDULER_OWNER_SETTLE_PERIOD` | Number | `300` | 计划创建多久后才纳入扫描，单位为秒，默认为五分钟。n8n 可能先写入计划，稍后才写入其所属对象，因此此设置避免将新计划误判为无主计划。必须大于 0。 |

## 跨实例协调 <a href="#coordination-vars" id="coordination-vars"></a>

控制调度器如何让后台处理轮次重叠运行，以及如何在实例之间分散数据库负载。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_SCHEDULER_MAX_CONCURRENT_PASSES` | Number | `10` | 数据库支持重叠处理轮次时，即 PostgreSQL，单个实例上同类后台处理轮次的最大并发数。到期时如果已达到上限，n8n 会跳过该轮次。SQLite 上各轮次从不重叠，此设置不生效。必须大于 0。 |
| `N8N_SCHEDULER_JITTER_RATIO` | Number | `0.1` | 为每次定期处理加入的小幅随机时间变化，以间隔的比例表示。值为 `0.1` 时，原本每十秒运行的轮次实际每九到十一秒运行。这会分散同时启动实例的数据库查询，例如滚动部署期间。设为 `0` 可使用精确间隔，增大则更均匀地分散负载。必须大于或等于 0，且小于 1。 |

## 调度行为 <a href="#behavior-vars" id="behavior-vars"></a>

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_SCHEDULER_TRIGGER_NODE_MODE` | 枚举（`legacy`, `new`） | `new` | Schedule Trigger 节点“每 N 秒”和“每 N 分钟”计划的触发方式。`new` 从工作流发布时刻起，以固定的 N 间隔运行，自 n8n 2.45.0 起为默认值。`legacy` 按时钟对齐，与内存调度器一致，是更早版本的默认值。仅影响秒和分钟间隔。自 n8n 2.45.0 起弃用，未来版本会移除此变量和 `legacy` 模式。参阅 [Schedule Trigger 时间设置](../../durable-scheduler.md#trigger-node-mode)。 |
| `N8N_SCHEDULER_MISFIRE_GRACE` | Number | `60` | 运行可以延迟多久启动，仍被视为按时，单位为秒。超过后计为漏触发，由触发器的漏触发处理策略决定如何处理该次运行及后续积压。这是计划继承的默认值；自 n8n 2.36.0 起，Schedule Trigger 节点可以设置自己的宽限期。应大于 `N8N_SCHEDULER_EXECUTOR_INTERVAL`，且至少为 `N8N_SCHEDULER_MATERIALIZATION_WINDOW`，否则 n8n 启动时会警告。上限为三十天。参阅[漏触发处理策略](../../durable-scheduler.md#misfire-policy)。自 n8n 2.34.0 起提供。 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
