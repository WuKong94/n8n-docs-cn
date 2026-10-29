---
title: 队列模式环境变量
description: 配置自托管 n8n 实例队列模式的环境变量。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 队列模式
originalFilePath: hosting/configuration/environment-variables/queue-mode.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/queue-mode
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/queue-mode
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 队列模式环境变量 <a href="#queue-mode-environment-variables" id="queue-mode-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

可以根据需要，以不同模式运行 n8n。队列模式提供最佳扩展能力。更多信息请参阅[队列模式](../../scaling/enable-queue-mode.md)。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `OFFLOAD_MANUAL_EXECUTIONS_TO_WORKERS` | Boolean | `false` | 设为 `true`，让手动执行在工作进程中运行，而非在主实例上运行。 |
| `QUEUE_BULL_PREFIX` | String | - | 所有队列键使用的前缀。 |
| `QUEUE_BULL_REDIS_DB` | Number | `0` | 所用的 Redis 数据库。 |
| `QUEUE_BULL_REDIS_HOST` | String | `localhost` | Redis 主机。 |
| `QUEUE_BULL_REDIS_PORT` | Number | `6379` | 所用的 Redis 端口。 |
| `QUEUE_BULL_REDIS_USERNAME` | String | - | Redis 用户名，需要 Redis 6 或更高版本。为兼容 Redis 6 之前的版本，请勿设置。 |
| `QUEUE_BULL_REDIS_PASSWORD` | String | - | Redis 密码。 |
| `QUEUE_BULL_REDIS_TIMEOUT_THRESHOLD` | Number | `10000` | Redis 超时阈值，单位为毫秒。 |
| `QUEUE_BULL_REDIS_CLUSTER_NODES` | String | - | Redis 客户端初始连接的 Redis Cluster 节点列表，以逗号分隔，格式为 `host:port`。在队列模式 `EXECUTIONS_MODE = queue` 下设置此变量，会创建 Redis Cluster 客户端，而非普通 Redis 客户端，并忽略 `QUEUE_BULL_REDIS_HOST` 和 `QUEUE_BULL_REDIS_PORT`。 |
| `QUEUE_BULL_REDIS_TLS` | Boolean | `false` | 为 Redis 连接启用 TLS。 |
| `QUEUE_BULL_REDIS_DUALSTACK` | Boolean | `false` | 为 Redis 连接启用 IPv4 和 IPv6 双栈支持。 |
| `QUEUE_WORKER_TIMEOUT` （**已弃用**） | Number | `30` | 自 n8n 1.22.0 起弃用，请改用 `N8N_GRACEFUL_SHUTDOWN_TIMEOUT`。关闭工作进程时，n8n 在退出前等待正在运行的执行完成的时长，单位为秒。 |
| `QUEUE_HEALTH_CHECK_ACTIVE` | Boolean | `false` | 是否启用健康检查，true 表示启用，false 表示禁用。 |
| `QUEUE_HEALTH_CHECK_PORT` | Number | `5678` | 提供健康检查的端口。启动工作进程服务器时，如果默认端口出现冲突，请更改此值。 |
| `QUEUE_WORKER_LOCK_DURATION` | Number | `60000` | 工作进程处理一条消息的租约时长，单位为毫秒。 |
| `QUEUE_WORKER_LOCK_RENEW_TIME` | Number | `10000` | 工作进程续租的频率，单位为毫秒。 |
| `QUEUE_WORKER_STALLED_INTERVAL` | Number | `30000` | 工作进程检查停滞任务的频率，0 表示从不检查。 |
| `QUEUE_WORKER_MAX_STALLED_COUNT` （**已弃用**） | Number | `1` | **已弃用**，在 n8n 2.0 中移除，设置后无效。迁移详情请参阅[移除 QUEUE_WORKER_MAX_STALLED_COUNT](../../../../../changelog/v20-breaking-changes.md#remove-queueworkermaxstalledcount)。 |

## Webhook 响应 <a id="webhook-responses"></a>

队列模式下，工作进程通过队列消息将 Webhook 响应传回主实例。以下变量设置消息大小上限，并控制响应体过大时，是否改存到二进制数据存储，避免节点失败。详情请参阅[大型 Webhook 响应](../../scaling/enable-queue-mode.md#large-webhook-responses)。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_WEBHOOK_RESPONSE_RELAY_SIZE_MAX` | Number | `64` | 工作进程通过队列消息传回主实例的响应大小上限，单位为 MiB。Redis 会保存传输中响应的多个副本，因此每个传输中的响应应预留约此值 1.5 倍的 Redis 内存。MCP Trigger 工作流返回的工具结果也受此限制。 |
| `N8N_WEBHOOK_RESPONSE_RELAY_OFFLOAD_ENABLED` | Boolean | `false` | 当响应体超过 `N8N_WEBHOOK_RESPONSE_RELAY_SIZE_MAX` 时，工作进程是否将其存入二进制数据存储，以便主实例流式传输给客户端，而非让节点失败。需要设置可持久存储的 `N8N_DEFAULT_BINARY_DATA_MODE`，即 `filesystem`、`database`、`s3` 或 `azure`，且所有实例都能读取该存储。仅当所有主实例和 Webhook 实例均运行 n8n 2.34.0 或更高版本时，才能在工作进程上启用。 |

## 多主节点设置 <a href="#multi-main-setup" id="multi-main-setup"></a>

详情请参阅[配置多主节点部署](../../scaling/enable-queue-mode.md#configuring-multi-main-setup)。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_MULTI_MAIN_SETUP_ENABLED` | Boolean | `false` | 是否为队列模式启用多主节点部署，需要许可证。 |
| `N8N_MULTI_MAIN_SETUP_KEY_TTL` | Number | `10` | 多主节点部署中领导者键的生存时间，单位为秒。 |
| `N8N_MULTI_MAIN_SETUP_CHECK_INTERVAL` | Number | `3` | 多主节点部署中检查领导者的间隔，单位为秒。 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
