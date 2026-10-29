---
contentType: overview
nodeTitle: 扩展
originalFilePath: hosting/scaling/overview.md
originalUrl: https://docs.n8n.io/hosting/scaling/overview
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 扩展 n8n <a href="#scaling-n8n" id="scaling-n8n"></a>

当 n8n 大规模运行，用户、工作流或执行数量很多时，需要调整 n8n 配置以确保良好性能。

n8n 可按需以不同[模式](scaling/enable-queue-mode.md)运行。`queue` 模式提供最佳扩展能力，配置详情请参阅[队列模式](scaling/enable-queue-mode.md)。

你可以配置数据保存和清理策略，以提高数据库性能。详情请参阅[执行数据](scaling/manage-execution-data.md)。

## 本节内容 <a id="in-this-section"></a>

* [衡量性能](scaling/measure-performance.md)：对 n8n 的性能和资源消耗进行基准测试。
* [启用队列模式](scaling/enable-queue-mode.md)：通过多个工作进程运行 n8n，获得最佳扩展能力。
* [控制并发](scaling/control-concurrency.md)：限制同时运行的执行数量。
* [管理执行数据](scaling/manage-execution-data.md)：配置数据保存和清理策略，以提高数据库性能。
* [处理二进制数据](scaling/handle-binary-data.md)：处理大文件，同时避免降低 n8n 性能。
* [使用外部存储](scaling/use-external-storage.md)：将二进制数据和执行数据存储到外部。
* [解决内存问题](scaling/fix-memory-issues.md)：识别并避免内存相关错误。

## 相关资源 <a id="related-resources"></a>

* [配置 n8n](./)
