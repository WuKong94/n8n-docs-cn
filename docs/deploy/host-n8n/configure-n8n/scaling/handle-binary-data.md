---
title: 扩展 n8n 的二进制数据处理
description: 处理大文件，同时避免降低 n8n 性能。
contentType: howto
nodeTitle: 处理二进制数据
originalFilePath: hosting/scaling/binary-data.md
originalUrl: https://docs.n8n.io/hosting/scaling/binary-data
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/handle-binary-data
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 二进制数据 <a href="#binary-data" id="binary-data"></a>

二进制数据是任何文件类型的数据，例如工作流执行期间生成或处理的图片文件、文档。

在队列模式下，二进制数据存储也用于承载过大、无法通过队列发送的 webhook 响应。详情请参阅[大型 webhook 响应](enable-queue-mode.md#large-webhook-responses)。

## 启用文件系统模式 <a href="#enable-filesystem-mode" id="enable-filesystem-mode"></a>

处理二进制数据时，n8n 默认将数据保存在内存中，处理大文件可能因此崩溃。

为避免此问题，将 `N8N_DEFAULT_BINARY_DATA_MODE` [环境变量](../basic-configuration/use-environment-variables/binary-data.md)改为 `filesystem`，使 n8n 将数据保存到磁盘，而非使用内存。

如果使用队列模式，请将其改为 `database`。n8n 不支持在队列模式下使用 `filesystem` 模式。

## 二进制数据清理 <a href="#binary-data-pruning" id="binary-data-pruning"></a>

n8n 将二进制数据清理作为执行数据清理的一部分。详情请参阅[执行数据 | 启用执行清理](manage-execution-data.md#enable-executions-pruning)。

如果配置了多种二进制数据模式，清理仅作用于当前启用的模式。例如，实例此前在 S3 中存储数据，后来切换为文件系统模式，n8n 就仅清理文件系统中的二进制数据。详情请参阅[外部存储](use-external-storage.md#usage)。

## 相关资源 <a id="related-resources"></a>

* [扩展](../scaling.md)
* [衡量性能](measure-performance.md)
* [启用队列模式](enable-queue-mode.md)
* [控制并发](control-concurrency.md)
* [管理执行数据](manage-execution-data.md)
* [使用外部存储](use-external-storage.md)
* [解决内存问题](fix-memory-issues.md)
