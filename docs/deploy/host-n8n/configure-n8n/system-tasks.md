---
title: 系统任务
description: n8n 如何运行内部维护任务，以及这些任务在自托管实例上提供的 Prometheus 指标。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 系统任务 <a id="system-tasks"></a>

系统任务是 n8n 定期为自身运行的维护作业，例如清理旧执行、压缩洞察数据、清理过期记录和续订许可证。它们不是工作流，不属于项目，也不会出现在编辑器中。某个任务停止运行时，不会立即表现为故障，但数据库可能持续增大，或洞察数据变得过时。

本页说明系统任务如何运行，以及提供哪些 Prometheus 指标，帮助你判断任务是否仍在运行、运行情况如何。

## 系统任务如何运行 <a id="how-system-tasks-run"></a>

每个系统任务都有自己的执行周期，可以是固定间隔或 cron 计划，并以三种模式之一运行。以下指标上的 `mode` 标签用于区分模式：

- **领导者定时器**，`leader_timer`。领导者主实例中的定时器运行任务。领导者退任时停止定时器，新领导者接任后启动。如果任务到期时实例不可用，该次运行就不会执行。
- **实例定时器**，`instance_timer`。任务面向的每个进程都运行自己的副本，因为任务作用于该进程的状态。自 n8n 2.42.0 起提供。
- **持久模式**，`durable`。[持久调度器](durable-scheduler.md)从数据库支持的队列中运行任务。任意主实例都能认领到期运行，重启也不会丢失。自 n8n 2.41.0 起提供。

### 在持久调度器上运行系统任务 <a id="run-system-tasks-on-the-durable-scheduler"></a>

要将系统任务迁移到持久调度器，请在每个主实例上设置以下环境变量，并重启 n8n：

```bash
export N8N_SCHEDULER_ENABLED=true
export N8N_SCHEDULER_SYSTEM_TASKS_ENABLED=true
```

两个变量在每个主实例上的值都应相同。只有支持持久模式的任务会迁移，其余继续使用定时器模式。

{% hint style="warning" %}
每个主实例都应运行相同 n8n 版本。滚动部署期间，较旧主实例可能通过领导者定时器运行任务，而较新实例通过持久调度器运行，导致同一任务运行两次。
{% endhint %}

持久系统任务也是调度器任务。[持久调度器指标](durable-scheduler.md#observability)用 `task_type` 标签值 `system:<task-name>` 报告，例如 `system:insights-compaction`。本页指标使用相同名称覆盖全部三种模式。

## 可观测性 <a id="observability"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.41.0 起提供系统任务指标。
{% endhint %}

通过两个环境变量启用指标：

```bash
export N8N_METRICS=true
export N8N_METRICS_INCLUDE_SYSTEM_TASK_METRICS=true
```

工作进程和 webhook 处理器也会为自身的实例定时器任务提供这些指标。端点设置请参阅[启用 Prometheus 指标](basic-configuration/configuration-examples/enable-prometheus-metrics.md)，绘制图表请参阅[使用 Grafana 可视化指标](../keep-n8n-running/visualize-metrics-with-grafana.md)。n8n 提供了[可直接使用的系统任务仪表盘](https://github.com/n8n-io/n8n-observability/tree/main/dashboards/grafana/n8n-system-tasks)，每个面板都附有建议操作。

以下所有名称都采用默认的 `n8n_` 指标前缀。如果设置了 `N8N_METRICS_PREFIX`，请替换为你的前缀。

### 标签 <a id="labels"></a>

每个序列都带有一组少量、固定的标签：

| 标签 | 值 | 含义 |
| :---- | :----- | :------------ |
| `task` | 任务名称，例如 `execution-pruning-soft-delete`、`insights-compaction` 或 `license-renewal` | 序列描述哪个系统任务。实际任务取决于版本、许可证和设置，因此应从 `n8n_system_task_info` 读取列表，而非硬编码。 |
| `mode` | `leader_timer`、`instance_timer`、`durable` | 任务运行位置。参阅[系统任务如何运行](#how-system-tasks-run)。在 n8n 2.42.0 之前，`leader_timer` 为 `in_memory`。 |
| `result` | `success`、`failure`、`aborted`、`lease_lost`、`timed_out` | 运行结束方式。`aborted` 表示实例退任或关闭时，运行仍在进行，未完成工作就停止。自 n8n 2.44.0 起提供的 `lease_lost` 和 `timed_out`，表示持久运行失去认领权或超过超时时间。 |
| `reason` | `overlap`、`provisioned_elsewhere`、`aborted`、`coalesced` | 某次计划运行未执行的原因。参阅[内存调度](#in-memory-scheduling)。 |

不包含实例标签。Prometheus 为每个抓取目标添加 `instance` 和 `job`，因此描述任务的仪表指标应使用 `max by (task)` 聚合，计数器、直方图和运行中数量仪表指标应使用 `sum by (task)` 聚合。

### 运行健康状况 <a id="run-health"></a>

以下三个序列描述运行本身，覆盖全部三种模式。

| 指标 | 类型 | 反映的情况 |
| :----- | :--- | :---------------- |
| `n8n_system_task_run_duration_seconds` | 直方图 | 每次运行耗时，按 `task`、`mode` 和 `result` 区分。`_count` 序列同时提供运行次数和失败次数，无需单独的计数器。如果时长逐渐接近任务自身周期，说明 n8n 即将因运行重叠而跳过下一次计划运行。 |
| `n8n_system_task_last_success_timestamp_seconds` | 仪表指标 | 任务在此实例上最近一次成功运行的 Unix 时间戳。这是判断任务是否已停止的最清晰信号，因为它也能反映从未运行的任务，而计数器的速率无法做到。 |
| `n8n_system_task_runs_in_flight` | 仪表指标 | 此实例上当前正在进行的任务运行数量，正常情况下为 `0` 或 `1`。数值一直停在 `1` 表示运行挂起，也会阻止实例退任或关闭。 |

### 调度健康状况 <a id="schedule-health"></a>

这些序列描述计划而非某次运行，因此首次运行之前就已存在。

| 指标 | 类型 | 反映的情况 |
| :----- | :--- | :---------------- |
| `n8n_system_task_info` | 仪表指标 | 始终为 `1`。此实例能运行的每个任务各有一个序列，并包含其 `mode`。可作为系统任务清单，与其他序列关联，找出未报告任何运行的任务。 |
| `n8n_system_task_interval_seconds` | 仪表指标 | 固定间隔任务声明的执行周期。使“延迟”可以通过查询判断，无需人工维护阈值列表。cron 计划任务不报告此指标。 |
| `n8n_system_task_next_run_timestamp_seconds` | 仪表指标 | 间隔计划和 cron 计划的下一次运行的 Unix 时间戳。对于定时器任务，这是此实例的定时器准备触发的时间点。时间戳在过去，表示定时器已停止规划。对于持久任务，这是调度器尚未规划的首个时间点，因此已规划的运行可能更早启动。每个主实例都从数据库读取并报告相同值。 |
| `n8n_system_task_scheduled` | 仪表指标 | n8n 已为任务安排计划时为 `1`，任务失去计划后为 `0`，原因可能是 n8n 无法规划其定时器周期，或没有可运行的持久作业。这里出现 `0` 表示任务已经停止，而非延迟运行。需要重启实例，或对领导者定时器任务更换领导者，才能重新安排计划。应对此告警。 |
| `n8n_system_task_provision_check_failures_total` | 计数器 | n8n 无法检查任务的持久作业是否存在，因而改由领导者定时器运行任务的次数。持续增加表示数据库存在问题，并且两条路径同时生效时，有小概率使同一任务运行两次。 |

持久任务或实例定时器任务的序列，在 n8n 启动时为任务分配执行路径后立即出现，因此重启表现为指标重置，而非缺口。领导者定时器任务的 `info`、`scheduled`、`runs_in_flight`、`last_success` 和 `next_run_timestamp_seconds` 序列，仅在此实例担任领导者时存在，退任后 n8n 会移除它们，避免原领导者继续为已不再运行的任务导出冻结值。只有 `interval_seconds` 保留，因为周期不取决于谁担任领导者。

### 内存调度 <a id="in-memory-scheduling"></a>

这些序列仅覆盖定时器运行。持久路径在[持久调度器指标](durable-scheduler.md#observability)中有对应指标：`n8n_scheduler_task_retries_total` 表示重试，`n8n_scheduler_dispatch_lag_seconds` 表示延迟。

| 指标 | 类型 | 反映的情况 |
| :----- | :--- | :---------------- |
| `n8n_system_task_runs_skipped_total` | 计数器 | 未执行的计划运行次数，按 `reason` 区分。`overlap` 表示上次运行仍在进行；`provisioned_elsewhere` 表示任务已有持久作业，领导者定时器因而让出执行；`aborted` 表示实例已经开始退任后，该次定时器才触发；`coalesced` 表示进程休眠期间错过了多次运行，定时器仅合并触发一次，计数器增加该次触发所代表的计划运行数量。 |
| `n8n_system_task_retries_total` | 计数器 | 运行失败后 n8n 安排的重试次数。只有声明了重试延迟的任务才会重试，因此任务持续失败但此计数不变，不一定是缺陷。 |
| `n8n_system_task_fire_lag_seconds` | 直方图 | 每次定时器触发的延迟，单位为秒。小值表示事件循环繁忙，大值表示进程暂停或休眠。直方图分桶最大达到一天，因为合并触发至少延迟一个完整周期。 |

## 相关资源 <a id="related-resources"></a>

* [配置 n8n](./)
