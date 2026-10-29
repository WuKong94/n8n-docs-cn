---
contentType: howto
nodeTitle: 使用 Grafana 可视化指标
originalFilePath: hosting/logging-monitoring/grafana.md
originalUrl: https://docs.n8n.io/hosting/logging-monitoring/grafana
url: https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/visualize-metrics-with-grafana
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Grafana <a href="#grafana" id="grafana"></a>

在 n8n 中启用 Prometheus 指标端点，然后让 Grafana 通过 Prometheus 实例连接，以可视化 n8n 数据。开始本指南前，请先参阅[启用 Prometheus 指标](../configure-n8n/basic-configuration/configuration-examples/enable-prometheus-metrics.md)。

{% hint style="info" %}
**功能可用范围**

`/metrics` 端点可用于：

- **自托管：**所有版本。

n8n Cloud 不提供此端点。
{% endhint %}

## 可复用仪表盘模板 <a href="#reusable-dashboard-templates" id="reusable-dashboard-templates"></a>

为 n8n 实例启用 Prometheus 指标后，你可以构建仪表盘来观察这些指标。

n8n 在以下 GitHub 项目中，为部分受支持的 Prometheus 指标提供可复用的 Grafana 仪表盘：
[n8n-observability](https://github.com/n8n-io/n8n-observability)

## 配置 Prometheus 抓取 n8n 指标 <a href="#configure-prometheus-to-scrape-n8n" id="configure-prometheus-to-scrape-n8n"></a>

Prometheus 定期抓取 n8n 的 `/metrics` 端点并保存数据，Grafana 再查询 Prometheus，展示这些数据。

在 `prometheus.yml` 中添加以 n8n 实例为目标的抓取作业：

```yaml
scrape_configs:
  - job_name: n8n
    static_configs:
      - targets:
          - <n8n-host>:<n8n-port>
    metrics_path: /metrics
```

将 `<n8n-host>` 和 `<n8n-port>` 替换为 n8n 实例地址，n8n 默认端口为 `5678`。

编辑后，重新加载或重启 Prometheus，使更改生效。

## 将 Prometheus 添加为 Grafana 数据源 <a href="#add-prometheus-as-a-grafana-data-source" id="add-prometheus-as-a-grafana-data-source"></a>

1. 在 Grafana 中前往 **Connections**（连接）> **Data sources**（数据源）。
2. 选择 **Add new data source**（添加新数据源）。
3. 选择 **Prometheus**。
4. 将 **Prometheus server URL**（Prometheus 服务器 URL）设为 Prometheus 实例地址，例如 `http://prometheus:9090`。
5. 选择 **Save & test**（保存并测试）。

Grafana 会显示成功消息，确认连接。

## Webhook 可观测性 <a href="#webhook-observability" id="webhook-observability"></a>


{% hint style="info" %}
**功能可用范围**

自 n8n 2.28.0 起提供 webhook 可观测性。
{% endhint %}

n8n 为每次 webhook 调用提供 `n8n_webhook_request_duration_seconds` 直方图。启用以下环境变量以收集此指标：

| 变量 | 默认值 | 说明 |
|----------|---------|-------------|
| `N8N_METRICS_INCLUDE_WEBHOOK_METRICS` | `false` | 提供 `n8n_webhook_request_duration_seconds` 直方图。 |
| `N8N_METRICS_INCLUDE_WORKFLOW_INFO` | `false` | 提供 `n8n_workflow_info` 仪表指标，显示便于阅读的工作流名称。参阅[工作流名称查找](#workflow-name-lookup)。 |

n8n-observability 项目为此直方图提供了[可直接使用的仪表盘](https://github.com/n8n-io/n8n-observability/tree/main/dashboards/grafana/n8n-webhook-executions)。

### 指标跟踪的内容 <a href="#what-the-metric-tracks" id="what-the-metric-tracks"></a>

`n8n_webhook_request_duration_seconds` 是一个 Prometheus 直方图。n8n 为每次 webhook 调用记录请求耗时，即从“收到请求”到“发出响应”的时长。每个标签组合提供三个时间序列：

| 序列 | 说明 |
|--------|-------------|
| `_bucket{le="<bound>"}` | 在 `<bound>` 秒内完成的请求的累计数量。 |
| `_sum` | 所有请求的总耗时，单位为秒。 |
| `_count` | 请求总数。 |

每个序列都带有以下标签：

| 标签 | 示例 | 说明 |
|-------|---------|-------------|
| `method` | `GET` | 入站请求的 HTTP 方法。 |
| `status_code` | `200` | n8n 返回的 HTTP 状态码。 |
| `webhook_path` | `294febd8-…` | 标识 webhook 端点的 UUID 路径。 |
| `workflow_id` | `KhcGg7EmAMoa7Bmv` | webhook 所属工作流的 ID。 |

### 仪表盘示例思路 <a href="#dashboard-ideas" id="dashboard-ideas"></a>

| 面板 | PromQL |
|-------|--------|
| 各工作流的请求速率 | `sum by (workflow_id) (rate(n8n_webhook_request_duration_seconds_count[5m]))` |
| 所有 webhook 的 p95 延迟 | `histogram_quantile(0.95, sum by (le) (rate(n8n_webhook_request_duration_seconds_bucket[5m])))` |
| 各工作流的 p95 延迟 | `histogram_quantile(0.95, sum by (le, workflow_id) (rate(n8n_webhook_request_duration_seconds_bucket[5m])))` |
| 错误率，非 2xx 响应 | `sum by (workflow_id) (rate(n8n_webhook_request_duration_seconds_count{status_code!="2.."}[5m]))` |
| 平均请求时长 | `rate(n8n_webhook_request_duration_seconds_sum[5m]) / rate(n8n_webhook_request_duration_seconds_count[5m])` |

## 表单提交可观测性 <a href="#form-submission-observability" id="form-submission-observability"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.28.0 起提供表单提交可观测性。
{% endhint %}

n8n 为每次表单提交提供 `n8n_form_submission_duration_seconds` 直方图。启用以下环境变量以收集此指标：

| 变量 | 默认值 | 说明 |
|----------|---------|-------------|
| `N8N_METRICS_INCLUDE_FORM_METRICS` | `false` | 提供 `n8n_form_submission_duration_seconds` 直方图。 |
| `N8N_METRICS_INCLUDE_WORKFLOW_INFO` | `false` | 提供 `n8n_workflow_info` 仪表指标，显示便于阅读的工作流名称。参阅[工作流名称查找](#workflow-name-lookup)。 |

n8n-observability 项目为此直方图提供了[可直接使用的仪表盘](https://github.com/n8n-io/n8n-observability/tree/main/dashboards/grafana/n8n-form-executions)。

### 指标跟踪的内容 <a href="#what-the-metric-tracks" id="what-the-metric-tracks"></a>

`n8n_form_submission_duration_seconds` 是一个 Prometheus 直方图。n8n 为每次表单提交记录从“用户按下提交”到“用户收到提交反馈”的时长。每个标签组合提供三个时间序列：

| 序列 | 说明 |
|--------|-------------|
| `_bucket{le="<bound>"}` | 在 `<bound>` 秒内完成的提交的累计数量。 |
| `_sum` | 所有提交的总处理时长，单位为秒。 |
| `_count` | 提交总数。 |

每个序列都带有以下标签：

| 标签 | 示例 | 说明 |
|-------|---------|-------------|
| `status_code` | `200` | n8n 返回的 HTTP 状态码。 |
| `form_path` | `b395d2e2-…` | 标识表单端点的 UUID 路径。 |
| `workflow_id` | `qTzTyGlEROwSuVlY` | 表单所属工作流的 ID。 |

{% hint style="info" %}
**不包含 method 标签**

表单提交不包含 `method` 标签，因为 n8n 仅通过 `POST` 接收表单数据。
{% endhint %}

### 仪表盘示例思路 <a href="#dashboard-ideas" id="dashboard-ideas"></a>

| 面板 | PromQL |
|-------|--------|
| 各工作流的提交速率 | `sum by (workflow_id) (rate(n8n_form_submission_duration_seconds_count[5m]))` |
| 所有表单的 p95 处理时长 | `histogram_quantile(0.95, sum by (le) (rate(n8n_form_submission_duration_seconds_bucket[5m])))` |
| 各工作流的 p95 处理时长 | `histogram_quantile(0.95, sum by (le, workflow_id) (rate(n8n_form_submission_duration_seconds_bucket[5m])))` |
| 错误率，非 2xx 响应 | `sum by (workflow_id) (rate(n8n_form_submission_duration_seconds_count{status_code!="2.."}[5m]))` |
| 平均处理时长 | `rate(n8n_form_submission_duration_seconds_sum[5m]) / rate(n8n_form_submission_duration_seconds_count[5m])` |

## 持久调度器可观测性 <a id="durable-scheduler-observability"></a>

n8n 为[持久调度器](../configure-n8n/durable-scheduler.md)提供队列深度、调度延迟、分发、重试和死信指标。使用 `N8N_METRICS_INCLUDE_SCHEDULER_METRICS` 启用，指标含义请参阅[持久调度器可观测性](../configure-n8n/durable-scheduler.md#observability)。n8n 提供了[可直接使用的仪表盘](https://github.com/n8n-io/n8n-observability/tree/main/dashboards/grafana/n8n-scheduler)。

## 轮询触发器可观测性 <a id="poll-trigger-observability"></a>

n8n 为[轮询触发器](../configure-n8n/durable-scheduler.md#poll-triggers)提供轮询时长、轮询错误、重叠和游标提交指标。使用 `N8N_METRICS_INCLUDE_POLL_TRIGGER_METRICS` 启用，指标含义请参阅[轮询触发器指标](../configure-n8n/durable-scheduler.md#poll-trigger-metrics)。n8n 提供了[可直接使用的仪表盘](https://github.com/n8n-io/n8n-observability/tree/main/dashboards/grafana/n8n-poll-triggers)。

## 系统任务可观测性 <a id="system-task-observability"></a>

n8n 为自身的[系统任务](../configure-n8n/system-tasks.md)，即清理和压缩数据的维护作业，提供运行时长、最近成功时间、运行中数量、跳过次数和定时器延迟指标。使用 `N8N_METRICS_INCLUDE_SYSTEM_TASK_METRICS` 启用，指标含义请参阅[系统任务可观测性](../configure-n8n/system-tasks.md#observability)。n8n 提供了[可直接使用的仪表盘](https://github.com/n8n-io/n8n-observability/tree/main/dashboards/grafana/n8n-system-tasks)。

## 工作流名称查找 <a href="#workflow-name-lookup" id="workflow-name-lookup"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.28.0 起提供工作流名称查找。
{% endhint %}

启用 `N8N_METRICS_INCLUDE_WORKFLOW_INFO` 后，n8n 会为每个工作流提供一个仪表指标：

```
n8n_workflow_info{workflow_id="VaQPuPmx9tPpo6BX",workflow_name="My workflow"} 1
```

通过 `workflow_id` 将其与其他任意 n8n 指标关联，即可在 Grafana 面板中，用便于阅读的名称替换不直观的 ID。例如，按工作流名称显示 webhook 请求速率：

```promql
sum by (workflow_name) (
  rate(n8n_webhook_request_duration_seconds_count[5m])
  * on(workflow_id) group_left(workflow_name)
  n8n_workflow_info
)
```

## 相关资源 <a id="related-resources"></a>

* [保持 n8n 运行](./)
* [设置日志](set-up-logging.md)
* [监控 n8n](monitor-n8n.md)
* [备份与恢复](backup-and-restore.md)
* [更新 n8n](update-n8n.md)
* [使用 OpenTelemetry 跟踪执行](trace-executions-with-opentelemetry.md)
