---
description: 在 terraform-aws-n8n 模块中配置多主实例、工作进程自动扩缩容和 Redis 高可用。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 在 AWS 上扩缩容并实现高可用 <a id="scale-and-run-at-high-availability-on-aws"></a>

[terraform-aws-n8n](https://github.com/n8n-io/terraform-aws-n8n) 模块默认以[队列模式](../../../configure-n8n/scaling/enable-queue-mode.md)部署 n8n，并使用[多主实例配置](../../../configure-n8n/scaling/enable-queue-mode.md#multi-main-setup)实现高可用。本页介绍此拓扑在模块中的专属设置：多主实例许可证要求、工作进程自动扩缩容和 Redis 高可用。

## 多主实例配置 <a id="multi-main-setup"></a>

模块默认运行多个主 Pod，需要 Enterprise 许可证。设置 `n8n_main_hpa_min_replicas = 1` 后，改为运行单个主 Pod，只需要 Business 套餐许可证，因为此模式禁用了 n8n 的多主实例领导者选举功能。

{% hint style="warning" %}
**单主实例模式在升级时会停机**

设置 `n8n_main_hpa_min_replicas = 1` 后，主 Pod 的自动扩缩容上限固定为一个，升级使用 `Recreate` 策略，Pod 中断预算允许驱逐唯一的主 Pod。升级和维护期间，编辑器、REST API 和定时触发器会停机，请安排维护窗口。
{% endhint %}

主 Pod 前方的负载均衡器或 Ingress 都需要启用会话保持（粘性会话），让浏览器始终连接同一个主 Pod。模块自身的 Ingress 默认已设置。如果自行提供 Ingress，请参阅[自定义 AWS 基础设施](customize-the-infrastructure.md#customer-managed-ingress)。

## 工作进程自动扩缩容 <a id="worker-autoscaling"></a>

工作进程 Pod 使用模块自动安装的 [KEDA](https://keda.sh/)，根据 Redis 队列深度扩缩容。要检查工作进程的自动扩缩容组件能否连接 Redis：

```bash
kubectl -n n8n get scaledobject
```

健康的扩缩容组件会报告 `READY=True`。如果报告 `READY=False`，请检查 KEDA Operator 日志中的原因：

```bash
kubectl -n keda logs -l app=keda-operator | grep -i 'connection to redis'
```

{% hint style="info" %}
**工作进程 HPA 的 TARGETS 列可能造成误解**

对于由 KEDA 驱动的工作进程 HPA，即使自动扩缩容正常，`kubectl get hpa` 的 TARGETS 列也经常显示 `<unknown>`。请改用 `kubectl get scaledobject` 检查扩缩容组件健康状态。
{% endhint %}

如果启用 [Redis 传输中加密](#redis-in-transit-encryption-and-auth)，KEDA 的队列深度触发器会自动使用与工作进程相同的加密、认证连接。

## Redis 高可用 <a id="redis-high-availability"></a>

默认情况下，模块将 Redis 创建为单节点 `aws_elasticache_cluster`，这会成为工作队列和多主实例领导者选举的单点故障。设置 `redis_high_availability_enabled = true` 后，会改为创建跨两个可用区、支持自动故障转移的复制组（一个主节点和一个副本）：

```hcl
module "n8n" {
  # ...
  redis_high_availability_enabled = true
  redis_node_type                 = "cache.r6g.large"
}
```

两个节点都使用 `redis_node_type`，因此启用高可用会使 Redis 成本大致翻倍。

{% hint style="warning" %}
**高可用不会阻止 Pod 重启**

Redis 故障转移约需二十秒即可将副本提升为主节点，但 Redis 复制是异步的，如果副本尚未收到近期队列写入，这些写入可能丢失。同时，每个主 Pod、工作进程 Pod 和 Webhook Pod 仍会重启：Redis 不可达时间超过 `QUEUE_BULL_REDIS_TIMEOUT_THRESHOLD`（默认十秒）后，n8n 的 Redis 客户端会退出进程。这是快速失败设计，不是崩溃循环。Kubernetes 会立即重新启动各 Pod；如果 Redis 可用，通常一分钟内可以恢复。
{% endhint %}

### 避免故障转移期间重启 <a id="avoid-restarts-during-a-failover"></a>

设置 `n8n_redis_timeout_threshold`，延长 n8n 退出前等待 Redis 的时间。实际等待预算的粒度比设置值更粗，因为每次失败的连接尝试约需 11.1 秒（1 秒重试间隔加 10 秒连接超时）：

| 设置值 | 实际等待预算 | 退出前的重连尝试次数 |
|---|---|---|
| `10000`（默认） | 11.1 秒 | 1 |
| `30000` | 33.2 秒 | 3 |
| `60000` | 66.4 秒 | 6 |

由于 DNS 缓存，故障转移后解析过时的 Redis 端点可能比故障转移本身耗时更长。实践中，将阈值设为 `60000` 可以应对此情况，Pod 会记录 `Recovered Redis connection`，而不是重启：

```hcl
module "n8n" {
  # ...
  redis_high_availability_enabled = true
  n8n_redis_timeout_threshold     = 60000
}
```

这一调整有取舍：同一阈值也决定了 Redis 确实不可用时，Pod 在重启前等待多久。对于工作进程，这通常可以接受，因为 Redis 不可达时，重启本来也无法解决问题。

### 切换拓扑 <a id="switching-topologies"></a>

在运行中的部署上切换 `redis_high_availability_enabled` 会销毁现有缓存并创建新缓存，当时所有排队中或运行中的任务都会丢失。请将其作为维护窗口操作：停止新任务进入 n8n，等待工作进程处理完队列，并在应用配置前确认 Redis 中的 `bull:jobs:wait`、`bull:jobs:active` 和 `bull:jobs:delayed` 均为空。

## Redis 淘汰策略 <a id="redis-eviction-policy"></a>

模块将 Redis 的 `maxmemory-policy` 设为 `noeviction`（`redis_maxmemory_policy`），而不是 ElastiCache 默认的 `volatile-lru`。在内存压力下，采用 `noeviction` 的 Redis 会以内存不足错误拒绝新写入，而不是静默淘汰任务锁等队列键。因此，Redis 满载会表现为写入失败和任务锁续期失败，而不是队列数据无故消失。请将队列与 n8n 缓存一并纳入 Redis 内存规划，因为两者共享同一实例。

## Redis 传输中加密与 AUTH <a id="redis-in-transit-encryption-and-auth"></a>

默认情况下，Redis 位于私有子网中，由仅允许 VPC 流量的安全组保护，不启用 TLS，也不设置密码。设置 `redis_transit_encryption_enabled = true` 后可同时启用两者：模块开启 TLS、生成 AUTH 令牌，并将其配置到每个 n8n 容器。

```bash
terraform output -raw redis_auth_token
```

## 相关资源 <a id="related-resources"></a>

* [使用 Terraform 部署到 AWS](./)
* [在 AWS 上部署首个 n8n 实例](deploy-your-first-instance.md)
* [在 AWS 上配置企业功能](use-enterprise-features-on-aws.md)
* [自定义 AWS 基础设施](customize-the-infrastructure.md)
* [维护和拆除 AWS 部署](maintain-and-tear-down.md)
* [启用队列模式](../../../configure-n8n/scaling/enable-queue-mode.md)
