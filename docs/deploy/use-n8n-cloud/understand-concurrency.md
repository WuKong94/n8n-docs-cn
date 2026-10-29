---
contentType: explanation
nodeTitle: 理解并发
originalFilePath: manage-cloud/concurrency.md
originalUrl: https://docs.n8n.io/manage-cloud/concurrency
url: https://docs.n8n.io/deploy/use-n8n-cloud/understand-concurrency
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Cloud 并发 <a href="#cloud-concurrency" id="cloud-concurrency"></a>

{% hint style="info" %}
**仅适用于 n8n Cloud**

本文介绍 n8n Cloud 中的并发。自托管实例的并发机制，请参阅[自托管 n8n 并发控制](../host-n8n/configure-n8n/scaling/control-concurrency.md)。
{% endhint %}

并发执行过多可能导致性能下降和无响应。为避免这些问题并提高实例稳定性，n8n 会对常规模式下的生产执行设置并发限制。

超出限制的执行任务会进入队列，等待处理。它们会一直留在队列中，直到有空闲并发容量，再按照先进先出（FIFO）顺序处理。

## 并发限制 <a href="#concurrency-limits" id="concurrency-limits"></a>

n8n 根据 Cloud 实例的套餐限制并发执行数量。详情请参阅[价格页面](https://n8n.io/pricing/)。

你可以在项目或工作流的执行标签页顶部，查看活跃执行数量和套餐并发限制。

## 详细说明 <a href="#details" id="details"></a>

关于并发，还需要注意：

- 并发控制仅适用于生产执行，即由 Webhook 或触发器节点启动的执行。不适用于手动执行、子工作流执行、错误执行等其他类型。
- [测试评估](#user-content-fn-1)[^1]不计入生产并发限制。单次测试运行中可以并行执行多少测试用例，受套餐各自独立的限额控制：自托管社区版和 n8n Cloud Pro 为 1 个（顺序执行），自托管 Business 为 3 个，Enterprise（包括 n8n Cloud 和自托管）为 5 个。你可以在 **Run Test（运行测试）** 弹出面板中调整本次运行的值。详情请参阅[基于指标的评估](../../build/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality.md#run-test-cases-in-parallel)。
- 无法重试排队中的执行任务。取消或删除排队任务时，也会将其从队列中移除。
- 实例启动时，n8n 会恢复队列中的执行任务，直至达到并发限制，并将其余任务重新入队。

## 与队列模式的比较 <a href="#comparison-to-queue-mode" id="comparison-to-queue-mode"></a>

{% hint style="info" %}
**功能可用范围**

n8n Cloud Enterprise 套餐支持队列模式。如需启用，请[联系 n8n](https://n8n-community.typeform.com/to/y9X2YuGa)。
{% endhint %}

队列模式与常规模式的并发采用不同机制。队列模式的并发设置决定每个工作实例可以并行运行多少任务；常规模式的并发限制则作用于整个实例。

<a id="user-content-fn-1"></a>

[^1]: 在 n8n 中，评估让你能够为执行历史添加标签、进行组织，并与新的执行结果比较。你可以通过它了解修改工作流后，其性能表现如何随时间变化。这在开发以 AI 为核心的工作流时尤其有用。

## 相关资源 <a id="related-resources"></a>

* [使用 n8n Cloud](./)
* [免费试用并选择套餐](start-your-free-trial.md)
* [使用 Cloud 控制台](use-the-cloud-console.md)
* [更新版本](update-your-version.md)
* [配置 Cloud](configure-cloud/README.md)
* [Gateway 额度](gateway-credits/README.md)
* [Assistant 额度](assistant-credits/README.md)
* [下载工作流](download-workflows.md)
