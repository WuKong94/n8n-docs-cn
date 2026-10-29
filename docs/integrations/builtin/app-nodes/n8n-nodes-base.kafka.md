---
title: Kafka 节点文档
description: 了解如何在 n8n 中使用 Kafka 节点，并按照技术文档将 Kafka 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Kafka 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.kafka.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kafka
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kafka
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Kafka 节点 <a href="#kafka-node" id="kafka-node"></a>

使用 Kafka 节点自动处理 Kafka 中的工作，并将其与其他应用集成。n8n 内置支持多种 Kafka 功能，包括发送消息。

本页列出了 Kafka 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Kafka 凭据](../credentials/kafka.md)。
{% endhint %}

{% hint style="info" %}
**Schema Registry（架构注册表）**

要通过需要身份验证的 Confluent Schema Registry（例如 Confluent Cloud）编码消息，请在节点中启用 **Use Schema Registry**（使用架构注册表），并添加 [Schema Registry 凭据](../credentials/schemaregistry.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

- Send message（发送消息）

## Kafka 节点版本 2 <a id="kafka-node-version-2"></a>

{% hint style="info" %}
**功能可用范围**

从 n8n 2.45.0 起，Kafka 节点的默认版本为 2：通过节点面板添加的节点使用版本 2。从 n8n 2.36.0 起，工作流便可选择使用版本 2。现有工作流在主动切换前，仍保持创建时使用的版本。
{% endhint %}

版本 2 使用全新的、持续维护的 Kafka 引擎。节点保留了版本 1 的操作、字段和凭据，有以下两处变化：

- **Compression**（压缩）改为下拉菜单，提供 **GZIP**、**LZ4**、**Snappy**、**Zstd** 和 **None**（无压缩，默认）选项。版本 1 仅提供 GZIP 开关。版本 1 的 Kafka Trigger 无法解码 **LZ4**、**Snappy** 或 **Zstd**，因此如果仍有版本 1 触发器消费该主题，请继续使用 **GZIP** 或 **None**。
- 开启 **Acks**（确认）后，版本 2 会按该选项描述，等待所有同步副本的确认。版本 1 只等待主题主副本的确认。关闭 **Acks** 时（默认），两个版本都不会等待。

### 将工作流切换至 Kafka 节点版本 2 <a id="switch-a-workflow-to-kafka-node-version-2"></a>

通过节点面板添加的节点已经使用版本 2。编辑器没有版本选择器，因此迁移现有版本 1 工作流时，请按以下步骤操作：

1. 下载工作流（**Workflow menu** > **Download**，即工作流菜单 > 下载），保留该文件不作修改，作为回滚时的恢复点。
2. 在该文件的副本中，将 Kafka 节点设置为 `"typeVersion": 2`。
3. 将副本导入一个新的空工作流（**Workflow menu** > **Import from File**，即工作流菜单 > 从文件导入）。导入会将节点添加到画布现有节点旁边，因此不要导入仍包含版本 1 节点的工作流。
4. 如果导入后节点的 Kafka 凭据被清空，请重新选择。要将生产环境迁至版本 2，请取消发布版本 1 工作流，再发布版本 2 工作流。

有关菜单的详细信息，请参阅[导出和导入工作流](../../../build/manage-workflows/export-and-import.md)。

n8n 在每次构建时，都会检查版本 2 的原生组件能否在 amd64 和 arm64 架构的官方 n8n Docker 镜像中加载。npm 或自定义镜像等其他安装方式不在此检查范围内。

### 回滚至 Kafka 节点版本 1 <a id="roll-back-to-kafka-node-version-1"></a>

编辑器没有修改现有节点版本的控件。如果原来的版本 1 工作流仍然存在，先取消发布版本 2 工作流，再重新发布原工作流。否则，请选择以下一种方式。如果仍保留切换步骤 1 中的导出文件，优先选择第一种；如果工作流最初就使用版本 2，没有版本 1 的导出文件，则使用第二种。

- **恢复导出文件：**取消发布版本 2 工作流。然后将切换步骤 1 中的文件导入一个新的空工作流（**Workflow menu** > **Import from File**，即工作流菜单 > 从文件导入），或者在你的套餐保留相应记录的情况下，通过[工作流历史记录](../../../build/manage-workflows/view-change-history.md)恢复先前版本。如果导入后 Kafka 凭据被清空，请重新选择，再发布恢复后的工作流。
- **编辑工作流 JSON：**取消发布版本 2 工作流并下载（**Workflow menu** > **Download**，即工作流菜单 > 下载）。在文件副本中，将 Kafka 节点设置为 `"typeVersion": 1`，再将副本导入一个新的空工作流。如果导入后 Kafka 凭据被清空，请重新选择，再发布恢复后的工作流。通过节点面板添加的节点为版本 2，因此添加新节点无法完成回滚。

使用版本 2 消费消息的方法，包括如何选择消费组 ID，请参阅 [Kafka Trigger 版本 2](../trigger-nodes/n8n-nodes-base.kafkatrigger.md#kafka-trigger-version-2)。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Kafka 集成模板](https://n8n.io/integrations/kafka)，或[搜索所有模板](https://n8n.io/workflows/)
