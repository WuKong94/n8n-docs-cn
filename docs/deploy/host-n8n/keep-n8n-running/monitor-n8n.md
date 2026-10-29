---
description: 获取健康检查指标。
contentType: howto
nodeTitle: 监控 n8n
originalFilePath: hosting/logging-monitoring/monitoring.md
originalUrl: https://docs.n8n.io/hosting/logging-monitoring/monitoring
url: https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/monitor-n8n
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 监控 <a href="#monitoring" id="monitoring"></a>

可以调用三个 API 端点，检查实例状态：`/healthz`、`healthz/readiness` 和 `/metrics`。


## healthz 和 healthz/readiness <a href="#healthz-and-healthzreadiness" id="healthz-and-healthzreadiness"></a>

`/healthz` 端点返回标准 HTTP 状态码。200 表示实例可访问，不表示数据库状态。自托管和 Cloud 用户均可使用。

访问端点：

```
<your-instance-url>/healthz
```

`/healthz/readiness` 端点与 `/healthz` 端点类似，但仅在数据库已连接并完成迁移，即实例已准备好接收流量时，返回 HTTP 状态码 200。

访问端点：

```
<your-instance-url>/healthz/readiness
```

{% hint style="info" %}
**自定义健康检查端点**

可以通过 [`N8N_ENDPOINT_HEALTH`](../configure-n8n/basic-configuration/use-environment-variables/endpoints.md) 环境变量自定义健康检查端点路径。
{% endhint %}

## metrics <a href="#metrics" id="metrics"></a>

`/metrics` 端点提供更详细的实例当前状态信息。

访问端点：

```
<your-instance-url>/metrics
```

{% hint style="info" %}
**功能可用范围**

`/metrics` 端点可用于：

- **自托管：**所有版本。

n8n Cloud 不提供此端点。
{% endhint %}


## 如何启用指标和健康检查？ <a href="#enable-metrics-and-health-checks-for-self-hosted-n8n" id="enable-metrics-and-health-checks-for-self-hosted-n8n"></a>

`/metrics` 端点默认禁用。n8n 主服务器始终启用健康检查端点；[队列模式](../configure-n8n/scaling/enable-queue-mode.md)下的工作进程服务器默认禁用健康检查端点。

要启用，请配置 n8n 实例：

```shell
# metrics <a href="#metrics" id="metrics"></a>
N8N_METRICS=true
# healthz <a href="#healthz" id="healthz"></a>
QUEUE_HEALTH_CHECK_ACTIVE=true
```

使用环境变量配置实例的更多信息，请参阅[配置方式](../configure-n8n/basic-configuration.md)。

## 相关资源 <a id="related-resources"></a>

* [保持 n8n 运行](./)
* [设置日志](set-up-logging.md)
* [使用 Grafana 可视化指标](visualize-metrics-with-grafana.md)
* [备份与恢复](backup-and-restore.md)
* [更新 n8n](update-n8n.md)
* [使用 OpenTelemetry 跟踪执行](trace-executions-with-opentelemetry.md)
