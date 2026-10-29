---
contentType: explanation
nodeTitle: 解决内存问题
originalFilePath: hosting/scaling/memory-errors.md
originalUrl: https://docs.n8n.io/hosting/scaling/memory-errors
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/fix-memory-issues
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 内存相关错误 <a href="#memory-related-errors" id="memory-related-errors"></a>

n8n 不限制各节点可获取和处理的数据量。这提供了灵活性，但当工作流执行所需内存超过可用内存时，可能导致错误。本页介绍如何识别并避免这些错误。

{% hint style="info" %}
**仅适用于自托管 n8n**

本页介绍[自托管 n8n](../../README.md)时的内存相关错误。[n8n Cloud](../../../use-n8n-cloud/README.md) 的内存限制请参阅 [Cloud 数据管理](../../../use-n8n-cloud/configure-cloud/manage-your-data.md)。
{% endhint %}

## 识别内存不足的情况 <a href="#identifying-out-of-memory-situations" id="identifying-out-of-memory-situations"></a>

部分内存不足情况会由 n8n 错误消息提示，例如 **Execution stopped at this node (n8n may have run out of memory while executing it)**（执行在此节点停止，n8n 可能在执行时内存不足）。

**Problem running workflow**（运行工作流时出现问题）、**Connection Lost**（连接丢失）或 **503 Service Temporarily Unavailable**（服务暂时不可用）等错误消息，表明 n8n 实例可能已不可用。

自托管 n8n 时，服务器日志还可能出现 **Allocation failed - JavaScript heap out of memory**（分配失败，JavaScript 堆内存不足）等错误消息。

在 n8n Cloud 或使用 n8n Docker 镜像时，遇到此类问题后 n8n 会自动重启。但通过 npm 运行时，可能需要手动重启。

## 常见原因 <a href="#typical-causes" id="typical-causes"></a>

当工作流执行所需内存超过 n8n 实例的可用内存时，就会出现此类问题。增加工作流执行内存用量的因素包括：

- [JSON 数据](../../../../build/work-with-data/understand-n8ns-data-structure.md)的数量。
- 二进制数据的大小。
- 工作流中的节点数量。
- 部分节点的内存开销较大：[Code](../../../../integrations/builtin/core-nodes/n8n-nodes-base.code/README.md) 节点和旧版 Function 节点可能显著增加内存消耗。
- 工作流是手动执行还是自动执行：手动执行时，n8n 会为前端复制一份数据，因此内存消耗更高。
- 同时运行的其他工作流。

## 避免内存不足 <a href="#avoiding-out-of-memory-situations" id="avoiding-out-of-memory-situations"></a>

遇到内存不足时有两种选择：增加 n8n 可用内存，或减少内存消耗。

### 增加可用内存 <a href="#increase-available-memory" id="increase-available-memory"></a>

自托管 n8n 时，增加可用内存意味着为实例分配更多内存，可能产生额外的托管费用。

在 n8n Cloud 上，需要升级到更高规格的套餐。

### 减少内存消耗 <a href="#reduce-memory-consumption" id="reduce-memory-consumption"></a>

这种方法更复杂，需要重新构建导致问题的工作流。本节提供一些减少内存消耗的建议，并非所有建议都适用于每个工作流。

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/scaling/reduce-memory-consumption.md" %}

### 增加老生代内存 <a href="#increase-old-memory" id="increase-old-memory"></a>

此方法适用于自托管 n8n。遇到 **JavaScript heap out of memory**（JavaScript 堆内存不足）错误时，为 V8 JavaScript 引擎的老生代区域分配更多内存通常有帮助。请通过 CLI 设置相应的 [V8 选项](https://nodejs.org/api/cli.html#--max-old-space-sizesize-in-megabytes) `--max-old-space-size=SIZE`，或通过 `NODE_OPTIONS` [环境变量](https://nodejs.org/api/cli.html#node_optionsoptions)设置。

## 相关资源 <a id="related-resources"></a>

* [扩展](../scaling.md)
* [衡量性能](measure-performance.md)
* [启用队列模式](enable-queue-mode.md)
* [控制并发](control-concurrency.md)
* [管理执行数据](manage-execution-data.md)
* [处理二进制数据](handle-binary-data.md)
* [使用外部存储](use-external-storage.md)
