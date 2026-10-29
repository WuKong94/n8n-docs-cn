---
title: 端点环境变量
description: 通过环境变量自定义自托管 n8n 实例的 API 和 Webhook 端点。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 端点
originalFilePath: hosting/configuration/environment-variables/endpoints.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/endpoints
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 端点环境变量 <a href="#endpoints-environment-variables" id="endpoints-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

本页列出用于自定义 n8n 端点的环境变量。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_PAYLOAD_SIZE_MAX` | Number | `16` | 请求负载大小上限，单位为 MiB。默认为 16 MiB，可通过增大此变量提高上限。需要重启 n8n 实例才能应用新设置。增加负载上限会需要更多内存和 CPU 资源，可能影响性能，请确认基础设施能够处理更大的负载。 |
| `N8N_FORMDATA_FILE_SIZE_MAX` | Number | `200` | form-data Webhook 负载中文件的大小上限，单位为 MiB。 |
| `N8N_METRICS` | Boolean | `false` | 是否启用 `/metrics` 端点。 |
| `N8N_METRICS_PREFIX` | String | `n8n_` | n8n 专有指标名称的可选前缀。 |
| `N8N_METRICS_INCLUDE_DEFAULT_METRICS` | Boolean | `true` | 是否提供默认的系统和 Node.js 指标。 |
| `N8N_METRICS_INCLUDE_CACHE_METRICS` | Boolean | false | 是否包含缓存命中和未命中的指标，true 表示包含，false 表示不包含。 |
| `N8N_METRICS_INCLUDE_MESSAGE_EVENT_BUS_METRICS` | Boolean | `false` | 是否包含事件指标，true 表示包含，false 表示不包含。 |
| `N8N_METRICS_INCLUDE_WORKFLOW_ID_LABEL` | Boolean | `false` | 是否在工作流指标中包含工作流 ID 标签。 |
| `N8N_METRICS_INCLUDE_NODE_TYPE_LABEL` | Boolean | `false` | 是否在节点指标中包含节点类型标签。 |
| `N8N_METRICS_INCLUDE_CREDENTIAL_TYPE_LABEL` | Boolean | `false` | 是否在凭据指标中包含凭据类型标签。 |
| `N8N_METRICS_INCLUDE_API_ENDPOINTS` | Boolean | `false` | 是否提供 API 端点指标。 |
| `N8N_METRICS_INCLUDE_API_PATH_LABEL` | Boolean | `false` | 是否包含 API 调用路径标签。 |
| `N8N_METRICS_INCLUDE_API_METHOD_LABEL` | Boolean | `false` | 是否包含 API 调用的 HTTP 方法标签，例如 GET、POST。 |
| `N8N_METRICS_INCLUDE_API_STATUS_CODE_LABEL` | Boolean | `false` | 是否包含 API 调用的 HTTP 状态码标签，例如 200、404。 |
| `N8N_METRICS_INCLUDE_QUEUE_METRICS` | Boolean | `false` | 是否包含扩展模式下的任务指标。 |
| `N8N_METRICS_QUEUE_METRICS_INTERVAL` | Integer | `20` | 更新队列指标的频率，单位为秒。 |
| `N8N_METRICS_INCLUDE_SCHEDULER_METRICS` | Boolean | `false` | 是否包含持久调度器指标，例如队列深度、调度延迟、分发吞吐量、重试和死信。仅适用于主实例。各指标含义请参阅[持久调度器可观测性](../../durable-scheduler.md#observability)。 |
| `N8N_METRICS_SCHEDULER_INTERVAL` | Integer | `20` | 刷新持久调度器队列健康仪表指标的频率，单位为秒。参阅[持久调度器可观测性](../../durable-scheduler.md#observability)。 |
| `N8N_METRICS_INCLUDE_POLL_TRIGGER_METRICS` | Boolean | `false` | 是否包含轮询触发器指标，例如轮询耗时、轮询错误、重叠轮询和游标提交。仅适用于主实例。各指标含义请参阅[轮询触发器指标](../../durable-scheduler.md#poll-trigger-metrics)。 |
| `N8N_METRICS_INCLUDE_SYSTEM_TASK_METRICS` | Boolean | `false` | 是否包含 n8n 内部维护任务指标，例如运行时长、最近成功时间、跳过次数和定时器延迟。仅适用于主实例。各指标含义请参阅[系统任务可观测性](../../system-tasks.md#observability)。 |
| `N8N_METRICS_INCLUDE_SSRF_METRICS` | Boolean | `false` | 是否包含 SSRF 防护检查指标。 |
| `N8N_METRICS_INCLUDE_DNS_CACHE_METRICS` | Boolean | `false` | 是否包含 DNS 缓存指标，目前仅 SSRF 防护使用该缓存。 |
| `N8N_ENDPOINT_REST` | String | `rest` | REST 端点路径。 |
| `N8N_ENDPOINT_WEBHOOK` | String | `webhook` | Webhook 端点路径。 |
| `N8N_ENDPOINT_WEBHOOK_TEST` | String | `webhook-test` | 测试 Webhook 端点路径。 |
| `N8N_ENDPOINT_WEBHOOK_WAIT` | String | `webhook-waiting` | 等待 Webhook 端点路径。 |
| `N8N_ENDPOINT_HEALTH` | String | `healthz` | 健康检查端点路径。 |
| `N8N_WEBHOOK_URL` | String | - | 在反向代理后运行 n8n 时，设置测试及生产 Webhook 的基础 URL。请使用此变量，而非上方仅设置端点*路径*的 `N8N_ENDPOINT_*` 变量，后者不是 URL。参阅[配置反向代理下的 Webhook URL](../configuration-examples/configure-webhook-urls-with-reverse-proxy.md)。 |
| `WEBHOOK_URL` | String | - | 自 n8n 2.35.0 起弃用，是 `N8N_WEBHOOK_URL` 的别名。仍然有效，但 n8n 启动时会记录弃用警告。 |
| `N8N_DISABLE_PRODUCTION_MAIN_PROCESS` | Boolean | `false` | 禁用主进程中的生产 Webhook。使用专用 Webhook 进程时，可避免 HTTP 流量给主进程带来负载。 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
