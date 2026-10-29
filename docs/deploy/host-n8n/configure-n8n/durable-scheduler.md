---
title: 持久调度器
description: 持久调度器如何通过数据库支持的队列，在自托管 n8n 实例中运行基于时间的工作流。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 持久调度器 <a id="durable-scheduler"></a>

持久调度器从数据库支持的队列中运行基于时间的工作流，例如以 Schedule Trigger 节点开始的工作流，而非依赖各实例内存。自 n8n 2.45.0 起默认启用。本页介绍它带来的变化、配置方式，以及如何[使用内存调度器](#use-the-in-memory-scheduler)。相关配置变量请参阅[调度器环境变量](basic-configuration/use-environment-variables/scheduler.md)。

{% hint style="info" %}
**功能可用范围**

持久调度器自 n8n 2.36.0 起提供。更早版本中，从 n8n 2.32.0 起以预览功能提供。在 n8n 2.45.0 之前默认关闭；自 n8n 2.45.0 起，新实例和现有实例都默认启用，除非显式关闭。
{% endhint %}

## 内存调度器与持久调度器的比较 <a href="#in-memory-vs-durable" id="in-memory-vs-durable"></a>

在 n8n 2.45.0 之前，默认使用内存调度器。它计算活动计划的触发时间，并将定时器保存在主实例进程中。此方式适合单实例，但有以下限制：

- **重启会丢失待运行任务。**实例停止时，内存中的定时器也会消失。停机期间到期的运行会被跳过，不会补执行。
- **多实例需要领导者。**多主实例配置中，只有领导者触发计划。如果领导者在不合适的时机更替，触发时间可能延后。

持久调度器通过将调度移入数据库解决这两个问题：

- **重启不会丢失运行。**调度器在运行到期前，将每次即将发生的运行记录在数据库中。重启不会丢弃记录。实例停机期间到期的运行，只要仍在宽限期内，就会在实例恢复后延迟触发；超过宽限期后，由触发器的[错过执行策略](#misfire-policy)决定如何处理。
- **每次运行由一个实例认领。**所有主实例共享同一队列，并从中认领运行。同一时刻每次运行仅由一个实例持有，因此任务分散在各主实例上，而不依赖单个领导者。

### 功能行为变化 <a href="#functional-changes" id="functional-changes"></a>

升级到 n8n 2.45.0 或启用持久调度器后，会应用以下行为：

- **仍然精确触发。**与内存调度器一样，运行仍会在计划的时刻触发。
- **自 n8n 2.45.0 起，默认使用固定间隔。**“每 N 秒”和“每 N 分钟”的计划，以工作流发布时间为起点，按均匀间隔运行。设置 `N8N_SCHEDULER_TRIGGER_NODE_MODE=legacy` 可保留与时钟对齐的时间安排。参阅 [Schedule Trigger 时间安排](#trigger-node-mode)。
- **错过的运行遵循错过执行策略。**调度器会提前记录运行，因此停机期间错过的运行仍有记录。宽限期内仍会延迟触发；超过宽限期后，由触发器的[错过执行策略](#misfire-policy)决定 n8n 是丢弃它，还是补执行。

## 配置持久调度器 <a href="#turn-on" id="turn-on"></a>

自 n8n 2.45.0 起，`N8N_SCHEDULER_ENABLED` 默认为 `true`，无需设置。如果升级前已设为 `false`，保留即可继续使用内存调度器；也可以移除此变量并重启 n8n，改用持久调度器。在 n8n 2.45.0 之前，请设为 `true` 来启用。

{% hint style="warning" %}
只有同时启用工作流发布服务，持久调度器才会接管 Schedule Trigger 节点。`N8N_USE_WORKFLOW_PUBLICATION_SERVICE` 默认启用。如果设为 `false`，n8n 会记录警告，Schedule Trigger 节点仍在内存调度器上运行，即使 `N8N_SCHEDULER_ENABLED` 为 `true`。
{% endhint %}

[其他变量](basic-configuration/use-environment-variables/scheduler.md)仅在调度器启用时生效。默认值适合大多数实例，仅在需要调整时间精度、存储或跨实例负载时更改。除非另有说明，所有时长都以秒为单位。

### 使用内存调度器 <a id="use-the-in-memory-scheduler"></a>

要保留或恢复内存调度，请设置以下环境变量并重启 n8n：

```bash
export N8N_SCHEDULER_ENABLED=false
```

此设置适用于实例上的所有 Schedule Trigger 和旧版 Cron 节点。多主实例配置中，每个主实例都应使用相同值。

n8n 2.45.0 弃用了内存调度器和 `N8N_SCHEDULER_ENABLED`。目前仍可作为回退方式使用，但未来版本会移除。如果设置了 `N8N_SCHEDULER_ENABLED` 或 `N8N_SCHEDULER_TRIGGER_NODE_MODE`，n8n 会在启动时记录弃用警告。如果所设值与新的默认值相同，请移除此变量。

n8n 2.45.0 还移除了 **Skip Durable Scheduler**（跳过持久调度器）节点设置和 `N8N_ENV_FEAT_SKIP_DURABLE_SCHEDULER`。现有节点设置不再使单个触发器保留在内存中。请使用 `N8N_SCHEDULER_ENABLED=false` 切换整个实例。

### 轮询触发器和系统任务 <a id="poll-triggers-and-system-tasks"></a>

轮询触发器，即带有 **Poll Times**（轮询时间）参数的触发器节点，例如 Google Sheets Trigger、Airtable Trigger，仍使用内存调度器，除非通过自 n8n 2.33.0 起提供的 [`N8N_SCHEDULER_POLL_TRIGGERS_ENABLED`](basic-configuration/use-environment-variables/scheduler.md#enable-vars) 启用持久调度。轮询触发器支持尚未完全稳定，除非准备密切观察轮询工作流，否则请不要在生产环境启用。持久调度器下的轮询行为，以及 n8n 建议与 `N8N_SCHEDULER_POLL_TRIGGERS_ENABLED` 同时启用的[持久轮询游标](#durable-poll-cursors)，请参阅[轮询触发器](#poll-triggers)。

n8n 内部维护作业也仍使用进程内定时器，除非通过自 n8n 2.45.0 起提供的 [`N8N_SCHEDULER_SYSTEM_TASKS_ENABLED`](basic-configuration/use-environment-variables/scheduler.md#enable-vars) 启用。参阅[在持久调度器上运行系统任务](system-tasks.md#run-system-tasks-on-the-durable-scheduler)。

## 持久调度器的工作原理 <a href="#how-it-works" id="how-it-works"></a>

了解以下术语，有助于理解环境变量：

- **计划（Schedule）**：重复运行规则，例如 Schedule Trigger 节点的“每 15 分钟”设置。调度器将每个计划存入数据库。
- **运行（Run）**：计划在某个具体时刻的一次触发。调度器提前将即将发生的运行逐行记录。

调度器分为五个阶段，每个阶段都有自己的[环境变量](basic-configuration/use-environment-variables/scheduler.md)：

1. **物化。**调度器扫描活动计划，并记录近期将发生的运行，即*物化窗口*内的运行，在到期前将其提交到数据库。如果物化发现某次运行已经超过[错过执行宽限期](#misfire-policy)，就由计划的错过执行策略处理，而非照原样记录。
2. **执行。**调度器最早在计划时刻前一个检查间隔认领已记录的运行，避免其他实例领取，并在计划时刻启动工作流。
3. **恢复。**如果实例认领运行后，在完成前停止，例如崩溃，*回收器（reaper）*会释放该运行，让其他实例领取。
4. **保留。**调度器将已完成运行保留一段时间，作为近期历史，然后删除，以控制表大小。
5. **归属校对。**每个计划都有归属对象，例如创建它的工作流。调度器定期检查各归属对象是否仍存在，并停用归属对象已不存在的计划。参阅[归属校对环境变量](basic-configuration/use-environment-variables/scheduler.md#owner-reconciliation)。

多实例下，每个主实例都运行全部五个阶段。认领机制保证安全：每次运行仅由一个实例认领，因此各实例都执行这些循环，可以分担负载，而不会重复工作。

## 错过执行策略 <a href="#misfire-policy" id="misfire-policy"></a>

运行延迟超过宽限期后，视为错过。宽限期默认由 `N8N_SCHEDULER_MISFIRE_GRACE` 决定，默认一分钟；自 n8n 2.36.0 起，从该版本开始新增的 Schedule Trigger 节点，可以通过 **Missed Execution Grace Period (Seconds)**（错过执行宽限期，秒）节点选项单独设置。若节点宽限期低于根据 `N8N_SCHEDULER_EXECUTOR_INTERVAL` 和 `N8N_SCHEDULER_MATERIALIZATION_WINDOW` 得出的实例级最低值，n8n 会提高到该最低值，且最长限制为 30 天。

错过的运行及其后积压的运行如何处理，取决于触发器的错过执行策略：

- **Don't Run Missed Executions**（不运行错过的执行），默认选项。n8n 完全丢弃错过的运行积压，从下一次运行继续计划。这与内存调度器一致，后者从不延迟执行已错过的运行。
- **Run the Most Recent Missed Execution**（运行最近一次错过的执行）。积压合并为该节点的一次补执行，时间取所有触发规则中最近错过的时刻，然后恢复计划。
- **Run the Most Recent Missed Execution Per Rule**（按规则运行最近一次错过的执行）。类似上一策略，但各触发规则独立补执行，因此包含多条触发规则的节点，可以按每条规则各补执行一次。

自 n8n 2.36.0 起，从该版本开始新增的 Schedule Trigger 节点，可通过 **If Execution Is Missed**（错过执行时）节点选项选择策略，参阅 [Schedule Trigger 节点文档](../../../integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/README.md#node-options)。执行轮询的触发器节点，例如 Google Sheets Trigger、Airtable Trigger，始终跳过错过的运行，并从下一次计划运行恢复轮询。

无论采用何种策略，计划时钟都会越过积压部分，没有任何策略会逐次重放积压。一次性计划没有下一次运行可继续，因此补执行策略仍会延迟运行它，跳过策略则将其永久丢弃。

{% hint style="info" %}
选择宽限期时，请先满足最低要求：使 `N8N_SCHEDULER_MISFIRE_GRACE` 大于 `N8N_SCHEDULER_EXECUTOR_INTERVAL`，并且至少为 `N8N_SCHEDULER_MATERIALIZATION_WINDOW`，否则 n8n 会在启动时警告。在此基础上，将其设为某次运行被视为错过前，所能容忍的最长延迟，例如实例重启或领导者更替所需时间。默认配置下，应为 60 秒或更长。
{% endhint %}

## Schedule Trigger 时间安排差异 <a href="#trigger-node-mode" id="trigger-node-mode"></a>

持久调度器下，大多数 Schedule Trigger 计划的触发方式与内存模式相同。上文的实例级变化仍适用：错过的运行遵循错过执行策略，每次运行由一个实例认领。此外，两类周期在特定情况下与内存调度器不同：

- **“每 N 秒”和“每 N 分钟”。**由 `N8N_SCHEDULER_TRIGGER_NODE_MODE` 控制触发方式，此设置仅影响这类周期。
- **“每 N 小时”“天”“周”或“月”。**日常使用中，两种模式下都与之前相同。持久调度器对少数日历边界情况的处理更准确，包括闰年、一年的第 53 周和夏令时切换，内存调度器在这些情况下可能偏差一个周期。

`N8N_SCHEDULER_TRIGGER_NODE_MODE` 有两个值：

- `new`，自 n8n 2.45.0 起的默认值：从工作流发布时刻开始计时，而非对齐时钟边界，运行之间保持固定秒数间隔。例如，在某分钟第 7 秒发布，“每 30 秒”将在 :37、下一分钟 :07 等时刻运行。间隔始终与设定值一致，包括跨分钟时，因此“每 7 秒”不会漂移。
- `legacy`，n8n 2.45.0 之前的默认值：与内存调度器一样，按时钟边界触发。“每 30 秒”在每分钟 :00 和 :30 触发。模式在每分钟开始时重置，因此间隔无法整除 60 时，分钟边界会出现不均匀间隔。“每 7 秒”在 :00、:07、:14 等时刻触发，直到 :56，然后跳回 :00，此时间隔为 4 秒，而非 7 秒。

要保留与时钟对齐的时间安排，请设置 `N8N_SCHEDULER_TRIGGER_NODE_MODE=legacy`。这仍会启用持久调度器。n8n 2.45.0 弃用了 `legacy` 模式和此变量，未来版本会移除。如果已将变量设为 `new`，可以移除。

{% hint style="info" %}
`N8N_SCHEDULER_TRIGGER_NODE_MODE` 仅影响“每 N 秒”和“每 N 分钟”的计划。其他所有周期，包括原始 cron 表达式，在两种值下的触发方式相同。
{% endhint %}

## 轮询触发器 <a id="poll-triggers"></a>

启用 [`N8N_SCHEDULER_POLL_TRIGGERS_ENABLED`](#turn-on) 后，轮询触发器的每个轮询时间都作为独立持久计划运行：与其他运行一样，重启不会丢失轮询，且会分散到各实例。以下三种行为特属于轮询触发器：

- **始终跳过错过的轮询。**一次轮询会获取自上次运行以来的所有新内容，因此补轮询会重复获取相同内容。参阅[错过执行策略](#misfire-policy)。
- **轮询偶尔可能运行两次。**调度器保证每次已分发的轮询至少运行一次，不保证仅运行一次。例如，实例停滞、由其他实例接管时，轮询可能重复。启用[持久轮询游标](#durable-poll-cursors)，防止重复轮询丢失或重复处理条目。
- **运行过久的轮询会被放弃。**自 n8n 2.37.0 起，运行超过 [`N8N_SCHEDULER_POLL_TIMEOUT`](basic-configuration/use-environment-variables/scheduler.md#poll-triggers) 的轮询会被放弃，默认 45 秒。n8n 停止等待，不记录任何结果，游标保持原位，下次轮询覆盖相同范围，因此不会丢失数据。这可以防止轮询卡在始终不响应的服务上。持续超时的轮询视为失败，n8n 会逐渐扩大重试轮询的间隔，避免持续冲击处理不及的服务。超时时间应低于 `N8N_SCHEDULER_LEASE_DURATION`，避免被放弃的轮询仍在运行时，其他实例已接管其运行。超时时间达到租约时长时，n8n 会在启动时警告。

### 持久轮询游标 <a id="durable-poll-cursors"></a>

每个轮询触发器节点都维护游标，用于记录已经读取到哪里，让每次轮询仅获取新内容。n8n 默认将游标保存在工作流静态数据中，并与轮询产生的执行分开保存。如果实例在两次保存之间崩溃，或两个实例同时轮询同一节点，游标与执行就会失去同步，工作流因而跳过条目或处理两次。

自 n8n 2.36.0 起，可将 `N8N_POLLER_DURABLE_CURSORS_ENABLED` 设为 `true` 来避免此问题。此时 n8n 将每个节点的游标保存在独立数据库表中，并与执行一同保存，使一轮轮询要么完整发生，要么完全未发生。n8n 建议只要轮询触发器运行在持久调度器上，就启用此功能。

自 n8n 2.37.0 起，只有 `N8N_SCHEDULER_ENABLED`、`N8N_SCHEDULER_POLL_TRIGGERS_ENABLED` 和 `N8N_USE_WORKFLOW_PUBLICATION_SERVICE` 都启用，此设置才生效。任一关闭时，n8n 都会在启动时记录警告，游标仍保存在工作流静态数据中。

启用后的预期行为：

- **切换是安全的。**节点下次轮询时，会将当前游标迁移到新表，不会重复获取或跳过内容。
- **n8n 会先检查工作流，仅限 n8n 2.36。**启动时，n8n 扫描每个活动工作流的已发布版本，检查触发器节点 ID 是否重复或缺失。发现问题或无法扫描某个工作流时，会禁用持久轮询游标，使整个实例的轮询触发器继续使用内存调度器，并记录错误，指出受影响的工作流和修复方法。
- **再次关闭并不会撤销迁移。**游标仍保留在对应表中，只是不再与执行一同保存。
- **可以观察游标保存情况。**使用 `N8N_METRICS_INCLUDE_POLL_TRIGGER_METRICS` 启用[轮询触发器指标](#poll-trigger-metrics)。

{% hint style="warning" %}
请同时启用 `N8N_POLLER_DURABLE_CURSORS_ENABLED` 和 `N8N_SCHEDULER_POLL_TRIGGERS_ENABLED`。将轮询触发器放到持久调度器上运行，但仍将游标保存在工作流静态数据中，会有丢失或重复处理条目的风险。
{% endhint %}

## 可观测性 <a id="observability"></a>

持久调度器在 `/metrics` 端点提供 Prometheus 指标，帮助判断运行是否按时启动、是否成功，以及队列是否在消化积压。通过两个环境变量启用：

```bash
export N8N_METRICS=true
export N8N_METRICS_INCLUDE_SCHEDULER_METRICS=true
```

只有主实例提供调度器指标。端点本身的设置请参阅[启用 Prometheus 指标](basic-configuration/configuration-examples/enable-prometheus-metrics.md)，绘图请参阅[使用 Grafana 可视化指标](../keep-n8n-running/visualize-metrics-with-grafana.md)。n8n 提供了[可直接使用的持久调度器仪表盘](https://github.com/n8n-io/n8n-observability/tree/main/dashboards/grafana/n8n-scheduler)，每个面板都附有建议操作。

n8n 自身的维护任务有独立指标集，由 `N8N_METRICS_INCLUDE_SYSTEM_TASK_METRICS` 控制，无论任务运行在持久调度器还是内存定时器上都适用。参阅[系统任务](system-tasks.md)。

指标名称中有两个术语需要说明。*task（任务）*是调度器已记录到数据库中的运行；*occurrence（计划触发）*是根据计划计算出的运行，在物化记录后成为任务。多数序列带有 `task_type` 标签，值为 `workflow:schedule-trigger` 或 `workflow:poll-trigger`，可区分 Schedule Trigger 节点和轮询触发器。

### 队列健康状况 <a id="queue-health"></a>

这四个仪表指标是队列快照，每次抓取时重新读取，描述整个集群，因此每个主实例报告相同值。请使用 `max` 或 `avg` 聚合，绝不要使用 `sum`。

| 指标 | 反映的情况 |
| :----- | :---------------- |
| `n8n_scheduler_tasks_pending` | 已记录、正在等待的运行数量。此值随计划数量变化，应关注趋势，而非绝对值。 |
| `n8n_scheduler_tasks_due` | 已记录、已经到期但仍未启动的运行数量，应接近零。 |
| `n8n_scheduler_tasks_running` | 集群各实例已认领且当前正在运行的数量。 |
| `n8n_scheduler_oldest_pending_age_seconds` | 最早到期运行的滞后时长。最清晰的积压信号：`0` 表示没有到期等待的运行，数值上升表示调度器处理不及。 |

每次抓取通过一次数据库查询获取全部四个仪表指标。`N8N_METRICS_SCHEDULER_INTERVAL` 缓存该查询，默认 20 秒，避免较短抓取间隔频繁查询调度器读取的表。

### 运行吞吐量与失败 <a id="run-throughput-and-failures"></a>

计数器和直方图记录各主实例自身的工作，因此应跨主实例求和，得到集群总量。

| 指标 | 类型 | 反映的情况 |
| :----- | :--- | :---------------- |
| `n8n_scheduler_tasks_dispatched_total` | 计数器 | 调度器交给处理器启动的运行数量，即调度吞吐量。 |
| `n8n_scheduler_tasks_completed_total` | 计数器 | 达到最终结果的运行数量，按 `result` 标签值 `success` 或 `failure` 区分。失败占比上升通常指向工作流或数据库问题，而非调度器问题。 |
| `n8n_scheduler_task_retries_total` | 计数器 | 调度器重新入队、准备再次尝试的失败运行数量。 |
| `n8n_scheduler_tasks_reclaimed_total` | 计数器 | 回收器从认领后停止的实例收回的运行数量。持续增加表示实例崩溃，或在运行中失去认领权。 |
| `n8n_scheduler_tasks_lease_lost_total` | 计数器 | 在另一实例已经收回认领权后才完成的运行数量，因此同一次运行可能执行了两次。按 `task_type` 区分。对轮询触发器而言，这是跨实例重叠信号，发生时由[持久轮询游标](#durable-poll-cursors)保证游标正确。 |
| `n8n_scheduler_tasks_dead_lettered_total` | 计数器 | 尝试 `N8N_SCHEDULER_MAX_ATTEMPTS` 次后 n8n 放弃的运行数量。每个都代表未能发生的运行，任何增加都应触发告警。 |
| `n8n_scheduler_dispatch_lag_seconds` | 直方图 | 每次运行从到期到启动的等待时长。应关注高百分位：p99 逐渐偏离 p50，表示部分运行停滞，而非整个队列变慢。 |

### 后台处理轮次 <a id="background-passes"></a>

这些计数器覆盖推动队列运行的[五个阶段](#how-it-works)，尤其适合判断某个阶段是否停止工作。

| 指标 | 类型 | 反映的情况 |
| :----- | :--- | :---------------- |
| `n8n_scheduler_occurrences_materialized_total` | 计数器 | 调度器写入数据库的即将发生的运行数量。如果存在已发布计划，但此值始终为零，表示物化已停止。 |
| `n8n_scheduler_jobs_deferred_total` | 计数器 | 物化无法规划、将重试的计划数量，例如包含无法解析的表达式。 |
| `n8n_scheduler_occurrences_misfired_total` | 计数器 | 被[错过执行策略](#misfire-policy)丢弃、没有记录的到期运行数量，按 `task_type` 及执行丢弃的 `policy` 区分。停机后短暂激增属于预期；持续增长表示运行经常延迟。 |
| `n8n_scheduler_occurrences_retired_total` | 计数器 | 因被补执行取代，调度器丢弃的已记录运行数量。 |
| `n8n_scheduler_occurrences_missed_total` | 计数器 | 超过截止时间仍未被认领，并由回收器标记为错过的已记录运行数量。 |
| `n8n_scheduler_tasks_pruned_total` | 计数器 | 保留阶段删除的已完成运行数量。如果从不增加，调度器表就会持续增长。 |
| `n8n_scheduler_jobs_quarantined_total` | 计数器 | 归属对象不再存在，归属校对因此停止的计划数量。自 n8n 2.39.0 起提供。 |
| `n8n_scheduler_orphaned_jobs_deleted_total` | 计数器 | 归属对象在隔离宽限期后仍不存在，归属校对因此删除的已停止计划数量。自 n8n 2.39.0 起提供。 |
| `n8n_scheduler_jobs_revived_total` | 计数器 | 归属对象实际仍存在，归属校对因此恢复的已停止计划数量。自 n8n 2.39.0 起提供。 |

### 轮询触发器指标 <a id="poll-trigger-metrics"></a>

轮询触发器有独立指标集，由单独的 `N8N_METRICS_INCLUDE_POLL_TRIGGER_METRICS` 开关控制，与上述调度器指标相互独立：

```bash
export N8N_METRICS=true
export N8N_METRICS_INCLUDE_POLL_TRIGGER_METRICS=true
```

只有主实例提供这些指标。它们来自轮询引擎本身，而非调度器，因此即使持久调度器未分发轮询也有效。与调度器计数器一样，它们记录各主实例自身的轮询，应跨主实例求和，得到集群总量。n8n 为此提供了[可直接使用的轮询触发器仪表盘](https://github.com/n8n-io/n8n-observability/tree/main/dashboards/grafana/n8n-poll-triggers)。

| 指标 | 类型 | 反映的情况 |
| :----- | :--- | :---------------- |
| `n8n_poll_trigger_duration_seconds` | 直方图 | 每次轮询耗时，按 `node_type` 和 `status` 区分。轮询耗时逐渐增加，意味着正在接近其自身间隔。一旦超过间隔，轮询就会开始重叠。 |
| `n8n_poll_trigger_errors_total` | 计数器 | 抛出错误的轮询数量，按 `node_type` 及 `kind` 标签值 `auth`、`rate_limited` 或 `thrown` 区分。`auth` 指向凭据故障，`rate_limited` 表示轮询速度超出服务允许范围。 |
| `n8n_poll_trigger_overlapping_ticks_total` | 计数器 | 同一进程中，同一节点的上次轮询尚未结束时就启动的新轮询数量。跨实例重叠由 `n8n_scheduler_tasks_lease_lost_total` 反映。 |
| `n8n_poll_trigger_timeouts_total` | 计数器 | 持久调度器因运行超过 `N8N_SCHEDULER_POLL_TIMEOUT` 而放弃的轮询数量，按 `node_type` 区分。被放弃的轮询不记录任何结果，下次轮询覆盖相同时间范围。持续增加表示被轮询服务的响应慢于超时时间。只有持久调度器会放弃轮询，因此内存调度器下此值保持为零。自 n8n 2.37.0 起提供。 |
| `n8n_poll_trigger_cursor_commits_total` | 计数器 | 已有确定结果的游标保存次数，按 `operation`（`with_execution` 或 `cursor_only`）及 `result` 区分。`result` 为 `fence_rejected`，表示过期轮询失去认领权，未获准推进游标，说明保护机制正在生效。`result` 为 `failure`，表示保存本身失败。 |
| `n8n_poll_trigger_cursor_commit_duration_seconds` | 直方图 | 每次游标保存耗时，带有相同的 `operation` 和 `result` 标签。 |

两个游标指标跟踪专用游标表。启用[持久轮询游标](#durable-poll-cursors)后，节点从首次轮询开始报告。关闭设置后仍会报告，因为游标继续保留在表中。

以上所有名称都采用默认的 `n8n_` 指标前缀。如果设置了 `N8N_METRICS_PREFIX`，请替换为你的前缀。

## 相关资源 <a id="related-resources"></a>

* [配置 n8n](./)
