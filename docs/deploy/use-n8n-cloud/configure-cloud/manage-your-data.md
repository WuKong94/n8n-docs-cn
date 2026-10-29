---
contentType: howto
nodeTitle: 管理数据
originalFilePath: manage-cloud/cloud-data-management.md
originalUrl: https://docs.n8n.io/manage-cloud/cloud-data-management
url: https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/manage-your-data
description: 如何管理 n8n Cloud 上的数据。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 管理数据 <a id="manage-your-data"></a>

在 n8n Cloud 上管理数据时，需要关注两个方面：

* 内存使用：复杂工作流处理大量数据时，可能超出 n8n 的内存限制，导致实例崩溃并无法访问。
* 数据存储：受执行设置和执行数量影响，n8n 数据库可能持续增大，最终耗尽存储空间。

为避免这些问题，n8n 建议在构建工作流时考虑内存效率，并且不要保存不必要的数据。

## 各 n8n Cloud 套餐的内存限制 <a href="#memory-limits-on-each-cloud-plan" id="memory-limits-on-each-cloud-plan"></a>

当前套餐：

* 试用：640MiB RAM，10 毫核 CPU，支持突发
* Starter：640MiB RAM，10 毫核 CPU，支持突发
* Pro-1（10,000 次执行）：640MiB RAM，20 毫核 CPU，支持突发
* Pro-2（50,000 次执行）：1280MiB RAM，80 毫核 CPU，支持突发
* Enterprise：4096MiB RAM，80 毫核 CPU，支持突发

旧套餐：

* Start：320MiB RAM，10 毫核 CPU，支持突发
* Power：1280MiB RAM，80 毫核 CPU，支持突发

n8n 为每个实例提供最多 100GB 的数据存储空间。

## 如何减少工作流的内存消耗 <a href="#how-to-reduce-memory-consumption-in-your-workflow" id="how-to-reduce-memory-consumption-in-your-workflow"></a>

工作流的构建方式会影响执行时的数据和内存消耗。虽然以下建议不适用于所有情况，但可作为避免超出实例内存限制的基础最佳实践。

{% include "../../../reusable-content/.gitbook/includes/self-hosting/scaling/reduce-memory-consumption.md" %}

注意，n8n 自身运行也会消耗内存。仅软件本身平均就需要约 180MiB RAM。

与界面交互同样会消耗内存。在工作流进行高负载执行时操作其界面，也可能使内存使用超出限制。

## 如何管理 n8n Cloud 的执行数据 <a href="#how-to-manage-execution-data-on-cloud" id="how-to-manage-execution-data-on-cloud"></a>

执行数据包括节点数据、参数、变量、执行上下文和二进制数据引用，以文本形式保存。

二进制数据是 n8n 无法用纯文本表示的非文本数据，例如图片、文档、音频和视频等文件及媒体。它通常远大于文本数据。

如果工作流处理的数据量很大，且已结束测试阶段，可以考虑停止保存成功执行的数据。

你可以通过以下两种方式，控制 n8n 在数据库中保存的执行数据量：

在 n8n Cloud 控制台中：

1. 打开 [Cloud 控制台](../use-the-cloud-console.md)，选择 **Instance settings（实例设置）**。
2. 在 **Runtime（运行时）** 部分的 **Executions to save（要保存的执行）** 下，取消勾选不想记录的执行类型：**Manual（手动）**、**Failed（失败）** 或 **Successful（成功）**。
3. 在页面底部的操作栏中选择 **Save and restart（保存并重启）**。实例会重启以应用修改。

在工作流设置中：

1. 选择 **Options（选项）** <img src="../../.gitbook/assets/three-dot-options-menu (1).png" alt="选项菜单" data-size="line"> 菜单。
2. 选择 **Settings（设置）**。n8n 会打开 **Workflow settings（工作流设置）** 弹窗。
3. 将 **Save successful production executions（保存成功的生产执行）** 改为 **Do not save（不保存）**。

## n8n Cloud 数据清理与内存不足事件预防 <a href="#cloud-data-pruning-and-out-of-memory-incident-prevention" id="cloud-data-pruning-and-out-of-memory-incident-prevention"></a>

### 自动数据清理 <a href="#automatic-data-pruning" id="automatic-data-pruning"></a>

达到保留期限或存储上限时，n8n 会自动清理执行日志，以先达到的条件为准。清理始终从最旧的数据开始，具体限制取决于 n8n Cloud 套餐：

* Start 和 Starter 套餐：最多保存 2,500 次执行，执行日志保留 7 天；
* Pro 套餐：最多保存 25,000 次执行，执行日志保留 30 天；
* Enterprise 套餐：最多保存 50,000 次执行，执行日志保留时间不限。

超过可保存的执行数量，或达到实例数据库存储大小限制，都可能触及上限。如果是数据库达到存储限制，n8n 只会删除执行数据，保留执行记录；如果基于执行数量或保留期限进行清理，则会彻底删除记录。

### 手动数据清理 <a href="#manual-data-pruning" id="manual-data-pruning"></a>

即使启用了自动清理，高负载执行或某些使用场景仍可能超出数据库容量。此时，n8n 会手动清理数据，以保护实例稳定性。

1. 实例磁盘使用率达到 85% 时，告警系统会通知 n8n。
2. n8n 清理执行数据：先备份实例（包含工作流、用户、凭据和执行数据），再恢复备份，但不恢复执行数据。

由于流程需要人工操作，告警机制并非万无一失。如果告警发生在非工作时间，或数据增长过快，剩余磁盘空间可能在来得及清理之前就被占满。

## 相关资源 <a id="related-resources"></a>

* [配置 Cloud](./)
* [设置时区](set-your-timezone.md)
* [查找 IP 地址](find-your-ip-addresses.md)
* [更改实例所有者或用户名](change-instance-ownership-or-username.md)
