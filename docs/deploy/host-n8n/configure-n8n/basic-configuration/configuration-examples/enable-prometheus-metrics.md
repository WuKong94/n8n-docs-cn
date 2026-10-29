---
title: 启用 Prometheus 指标
description: 启用 Prometheus 指标端点。
contentType: howto
nodeTitle: 启用 Prometheus 指标
originalFilePath: hosting/configuration/configuration-examples/prometheus.md
originalUrl: https://docs.n8n.io/hosting/configuration/configuration-examples/prometheus
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/enable-prometheus-metrics
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 启用 Prometheus 指标 <a href="#enable-prometheus-metrics" id="enable-prometheus-metrics"></a>

n8n 使用 [prom-client](https://www.npmjs.com/package/prom-client) 库收集并提供指标。

`/metrics` 端点默认禁用，可以通过 `N8N_METRICS` 环境变量启用。

{% hint style="warning" %}
**不要将指标端点公开暴露**

仅向需要读取 Prometheus 数据的内部服务开放 `/metrics` 端点，不要让它可以从公共互联网访问，因为它可能泄露 n8n 实例的敏感运行数据。
{% endhint %}

```bash
export N8N_METRICS=true
```

要配置提供哪些指标和标签，请参阅对应的[环境变量](../use-environment-variables/endpoints.md)（`N8N_METRICS_INCLUDE_*`）。

`main` 和 `worker` 实例均可提供指标。

有关连接 Grafana 与 Prometheus，以可视化 n8n 指标的说明，请参阅 [Grafana](../../../keep-n8n-running/visualize-metrics-with-grafana.md)。

## 队列指标 <a href="#queue-metrics" id="queue-metrics"></a>

要启用队列指标，请将 `N8N_METRICS_INCLUDE_QUEUE_METRICS` 环境变量设为 `true`。可以通过 `N8N_METRICS_QUEUE_METRICS_INTERVAL` 调整刷新频率。

n8n 从 Bull 收集这些指标，并由主实例提供。在多主节点环境中，聚合查询时可以通过 `instance_role_leader` 仪表指标识别主节点中的领导者：领导者的值为 `1`，其他主节点为 `0`。

```
# HELP n8n_scaling_mode_queue_jobs_active Current number of jobs being processed across all workers in scaling mode. <a href="#help-n8nscalingmodequeuejobsactive-current-number-of-jobs-being-processed-across-all-workers-in-scaling-mode" id="help-n8nscalingmodequeuejobsactive-current-number-of-jobs-being-processed-across-all-workers-in-scaling-mode"></a>
# TYPE n8n_scaling_mode_queue_jobs_active gauge <a href="#type-n8nscalingmodequeuejobsactive-gauge" id="type-n8nscalingmodequeuejobsactive-gauge"></a>
n8n_scaling_mode_queue_jobs_active 0

# HELP n8n_scaling_mode_queue_jobs_completed Total number of jobs completed across all workers in scaling mode since instance start. <a href="#help-n8nscalingmodequeuejobscompleted-total-number-of-jobs-completed-across-all-workers-in-scaling-mode-since-instance-start" id="help-n8nscalingmodequeuejobscompleted-total-number-of-jobs-completed-across-all-workers-in-scaling-mode-since-instance-start"></a>
# TYPE n8n_scaling_mode_queue_jobs_completed counter <a href="#type-n8nscalingmodequeuejobscompleted-counter" id="type-n8nscalingmodequeuejobscompleted-counter"></a>
n8n_scaling_mode_queue_jobs_completed 0

# HELP n8n_scaling_mode_queue_jobs_failed Total number of jobs failed across all workers in scaling mode since instance start. <a href="#help-n8nscalingmodequeuejobsfailed-total-number-of-jobs-failed-across-all-workers-in-scaling-mode-since-instance-start" id="help-n8nscalingmodequeuejobsfailed-total-number-of-jobs-failed-across-all-workers-in-scaling-mode-since-instance-start"></a>
# TYPE n8n_scaling_mode_queue_jobs_failed counter <a href="#type-n8nscalingmodequeuejobsfailed-counter" id="type-n8nscalingmodequeuejobsfailed-counter"></a>
n8n_scaling_mode_queue_jobs_failed 0

# HELP n8n_scaling_mode_queue_jobs_waiting Current number of enqueued jobs waiting for pickup in scaling mode. <a href="#help-n8nscalingmodequeuejobswaiting-current-number-of-enqueued-jobs-waiting-for-pickup-in-scaling-mode" id="help-n8nscalingmodequeuejobswaiting-current-number-of-enqueued-jobs-waiting-for-pickup-in-scaling-mode"></a>
# TYPE n8n_scaling_mode_queue_jobs_waiting gauge <a href="#type-n8nscalingmodequeuejobswaiting-gauge" id="type-n8nscalingmodequeuejobswaiting-gauge"></a>
n8n_scaling_mode_queue_jobs_waiting 0
```

## 相关资源 <a id="related-resources"></a>

* [配置示例](./)
