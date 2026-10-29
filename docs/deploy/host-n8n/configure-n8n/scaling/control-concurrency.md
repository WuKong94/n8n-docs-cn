---
contentType: explanation
nodeTitle: 控制并发
originalFilePath: hosting/scaling/concurrency-control.md
originalUrl: https://docs.n8n.io/hosting/scaling/concurrency-control
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/control-concurrency
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 自托管并发控制 <a href="#self-hosted-concurrency-control" id="self-hosted-concurrency-control"></a>

{% hint style="info" %}
**仅适用于自托管 n8n**

本文介绍自托管部署的并发控制。n8n Cloud 账号的并发机制，请参阅 [Cloud 并发](../../../use-n8n-cloud/understand-concurrency.md)。
{% endhint %}

在常规模式下，n8n 不限制同时运行的生产执行数量。这可能导致过多并发执行使事件循环过载，造成性能下降和无响应。

为避免这种情况，可以在常规模式下为生产执行设置并发上限，以控制同时运行的数量，并将超出上限的生产执行加入队列。这些执行会留在队列中，直到有空闲并发容量，再按先进先出（FIFO）顺序处理。

默认禁用并发控制。要启用：

```sh
export N8N_CONCURRENCY_PRODUCTION_LIMIT=20
```

请注意：

- 并发控制仅适用于生产执行，即由 webhook 或触发器[^1]节点启动的执行。不适用于手动执行、子工作流执行、错误执行或通过 CLI 启动的执行等其他类型。
- 无法重试排队中的执行。取消或删除排队中的执行，也会将其移出队列。
- 实例启动时，n8n 会在并发上限内恢复排队的执行，并将其余执行重新加入队列。

- 要监控并发控制，请查看日志中执行加入队列和移出队列的记录。未来版本会在界面中显示并发控制信息。


启用并发控制后，可以在项目或工作流的执行选项卡顶部查看活动执行数量和配置的上限。

## 与队列模式的比较 <a href="#comparison-to-queue-mode" id="comparison-to-queue-mode"></a>

在队列模式下，可以通过 [`--concurrency` 标志](enable-queue-mode.md#configure-worker-concurrency)控制单个工作进程同时运行的作业数量。

队列模式和常规模式的并发控制是独立机制，但两者都受 `N8N_CONCURRENCY_PRODUCTION_LIMIT` 环境变量控制。在队列模式下，如果此变量设为非 `-1` 的值，n8n 会将其作为上限；否则使用 `--concurrency` 标志或其默认值。

## 评估并发 <a href="#evaluation-concurrency" id="evaluation-concurrency"></a>

评估测试运行使用独立于生产执行的并发上限。默认上限取决于实例的许可证层级：Community/Pro 为 1，Business 为 3，Enterprise 为 5。可通过 [`N8N_CONCURRENCY_EVALUATION_LIMIT`](../basic-configuration/use-environment-variables/executions.md) 覆盖。界面中滑块的行为请参阅[基于指标的评估](../../../../build/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality.md#run-test-cases-in-parallel)。

[^1]: 触发器节点是一种特殊节点，用于在满足特定条件时执行工作流。所有生产工作流都至少需要一个触发器，以决定工作流何时运行。

## 相关资源 <a id="related-resources"></a>

* [扩展](../scaling.md)
* [衡量性能](measure-performance.md)
* [启用队列模式](enable-queue-mode.md)
* [管理执行数据](manage-execution-data.md)
* [处理二进制数据](handle-binary-data.md)
* [使用外部存储](use-external-storage.md)
* [解决内存问题](fix-memory-issues.md)
