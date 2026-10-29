---
title: Kafka 触发器节点文档
description: 了解如何在 n8n 中使用 Kafka 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Kafka 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.kafkatrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.kafkatrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.kafkatrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Kafka 触发器节点 <a href="#kafka-trigger-node" id="kafka-trigger-node"></a>

[Kafka](https://kafka.apache.org/) 是开源的分布式事件流平台，可用于高性能数据管道、流式分析、数据集成和关键业务应用。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Kafka 凭据文档](../credentials/kafka.md)。
{% endhint %}

{% hint style="info" %}
**Schema Registry（架构注册表）**

要通过需要身份验证的 Confluent Schema Registry（例如 Confluent Cloud）解码消息，请在节点中启用 **Use Schema Registry**（使用架构注册表），并添加 [Schema Registry 凭据](../credentials/schemaregistry.md)。
{% endhint %}

{% hint style="warning" %}
**版本 1 的消息压缩支持**

Kafka Trigger 版本 1 可消费未压缩的消息和使用 **GZIP** 压缩的消息，但无法解码使用 **LZ4**、**Snappy** 或 **Zstd** 压缩的消息（这些格式是 Confluent 和 JVM 生产者的常见默认格式）。消费此类主题时，会报不支持压缩格式的错误。要消费该主题，请将生产者配置为使用 GZIP 或不压缩，或切换至可解码全部四种格式的 [Kafka Trigger 版本 2](#kafka-trigger-version-2)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Kafka Trigger 集成](https://n8n.io/integrations/kafka-trigger/)页面。
{% endhint %}

## Kafka Trigger 版本 2 <a id="kafka-trigger-version-2"></a>

{% hint style="info" %}
**功能可用性**

从 n8n 2.45.0 起，Kafka Trigger 的默认版本为 2：通过节点面板添加的触发器使用版本 2。从 n8n 2.36.0 起，工作流便可选择使用版本 2。现有工作流在主动切换前，仍保持创建时使用的版本。
{% endhint %}

版本 2 使用全新的、持续维护的 Kafka 引擎。触发器保留了版本 1 的字段和凭据，但有以下差异：

- 可解码使用 **GZIP**、**LZ4**、**Snappy** 或 **Zstd** 压缩的消息。版本 1 仅支持未压缩和 GZIP 消息。
- 发布工作流时会检查主题和消费组。如果以确切名称指定的主题不存在，或代理拒绝该消费组，发布会失败并报错，而不会出现触发器不消费任何消息却没有提示的情况。
- 手动执行（选择 **Listen for test event**，即监听测试事件时）会加入名为 `<group-id>-n8n-manual-<uuid>` 的临时消费组，即使启用了 **Read Messages From Beginning**（从头读取消息），也不会重放主题。手动执行不再取走已发布工作流的消息。如果集群配置了访问控制列表（ACL），请为 `<group-id>-n8n-manual-` 授予前缀匹配的消费组 ACL；或者跳过测试，直接发布工作流并查看执行记录。
- 如果 Schema Registry 无法解码消息，版本 2 会将其保留为未读，并在 **Retry Delay on Error**（出错后重试延迟）指定的时间后重试，因此注册表不可用时也不会丢失消息。版本 1 会将原始消息传给工作流并提交偏移量。

### Kafka Trigger 版本 2 中移除或变更的选项 <a id="options-removed-or-changed-in-kafka-trigger-version-2"></a>

版本 2 不再提供版本 1 中的以下三个选项：

- **Auto Commit Threshold**（自动提交阈值）：新引擎没有对应设置。
- **Each Batch Auto Resolve**（每批自动解析）：该选项会将未经任何执行处理的消息标记为已读。
- **Allow Topic Creation**（允许创建主题）：该选项在版本 1 中未生效。

其他所有选项保留原名称和默认值，其中三个选项的行为有所变化：

- **Rebalance Timeout**（再均衡超时）现在规定单批消息可处理多长时间，超过后消费组将移除此消费者。n8n 仅在工作流未设置自身执行超时时使用该值；工作流的超时设置优先。
- 如果 **Heartbeat Interval**（心跳间隔）超过 **Session Timeout**（会话超时）的三分之一，n8n 会自动降低心跳间隔，以免代理移除该消费者。
- **Retry Delay on Error**（出错后重试延迟）也用于控制 Schema Registry 无法解码的消息的重试间隔。版本 1 仅在偏移量解析失败后使用该选项。

### 将工作流切换至 Kafka Trigger 版本 2 <a id="switch-a-workflow-to-kafka-trigger-version-2"></a>

通过节点面板添加的触发器已经使用版本 2。编辑器没有版本选择器，因此迁移现有版本 1 工作流时，请按以下步骤操作：

1. 下载工作流（**Workflow menu** > **Download**，即工作流菜单 > 下载），保留该文件不作修改，作为回滚时的恢复点。
2. 在该文件的副本中，将 Kafka Trigger 节点设置为 `"typeVersion": 2`，并按[选择消费组 ID](#choose-the-consumer-group-id)中的说明设置消费组 ID。
3. 将副本导入一个新的空工作流（**Workflow menu** > **Import from File**，即工作流菜单 > 从文件导入）。导入会将节点添加到画布现有节点旁边，因此不要导入仍包含版本 1 触发器的工作流。
4. 如果导入后节点的 Kafka 凭据被清空，请重新选择。如果使用相同的消费组 ID 迁移，请先取消发布版本 1 工作流，再发布版本 2 工作流。

有关菜单的详细信息，请参阅[导出和导入工作流](../../../build/manage-workflows/export-and-import.md)。

n8n 在每次构建时，都会检查版本 2 的原生组件能否在 amd64 和 arm64 架构的官方 n8n Docker 镜像中加载。npm 或自定义镜像等其他安装方式不在此检查范围内。

### 选择消费组 ID <a id="choose-the-consumer-group-id"></a>

版本 1 和版本 2 使用不同的客户端库，无法共同组成消费组，因此请根据目标设置消费组 ID：

- **同时运行两个触发器时**，为版本 2 触发器指定独立的消费组 ID。这适合对比两个版本，或在版本 1 继续工作的同时试用版本 2。此时两者完全独立：分别接收主题中的每条消息，各自保存读取位置，启动新触发器不会干扰已运行的触发器。
- **从版本 1 迁移至版本 2 时**，保留相同的消费组 ID，但每次仅运行一个触发器：先取消发布版本 1 工作流，再发布版本 2 工作流。新触发器会从旧触发器停止的位置继续，不会跳过任何消息，包括两个触发器都未运行期间到达的消息。只有在取消发布版本 1 时执行仍未完成的消息，才可能再次执行。此时不要使用新的消费组 ID：新消费组没有已保存的位置，会根据 **Read Messages From Beginning**（从头读取消息）的设置，跳过积压消息或重放整个主题。
- **不要使用相同的消费组 ID 同时发布两个触发器。** 两者无法组成消费组。无论哪种情况，现有触发器都会继续工作；配置错误的后果是新触发器始终不触发，而不是破坏生产工作流。如果后发布的是版本 2 触发器，会发布失败并显示错误；如果后发布的是版本 1 触发器，代理会拒绝它，直到你取消发布其中一个触发器，它才会收到消息。请在发布前设置好消费组 ID，不要依赖报错来发现问题。

### 回滚至 Kafka Trigger 版本 1.3 <a id="roll-back-to-kafka-trigger-version-13"></a>

回滚不会丢失读取位置：取消发布版本 2 工作流时，其消费者会退出消费组，后台也不再运行任何相关任务。已提交的读取位置仍保存在代理上，并关联消费组 ID，保留时间取决于代理对空消费组偏移量的保留期限（默认为七天）。

编辑器没有修改现有节点版本的控件。如果原来的版本 1 工作流仍然存在，先取消发布版本 2 工作流，再重新发布原工作流。否则，请选择以下一种方式。如果仍保留切换步骤 1 中的导出文件，优先选择第一种；如果工作流最初就使用版本 2，没有版本 1 的导出文件，则使用第二种。

- **恢复导出文件：**取消发布版本 2 工作流。然后将切换步骤 1 中的文件导入一个新的空工作流（**Workflow menu** > **Import from File**，即工作流菜单 > 从文件导入），或者在你的套餐保留相应记录的情况下，通过[工作流历史记录](../../../build/manage-workflows/view-change-history.md)恢复先前版本。如果导入后 Kafka 凭据被清空，请重新选择，再发布恢复后的工作流。
- **编辑工作流 JSON：**取消发布版本 2 工作流并下载（**Workflow menu** > **Download**，即工作流菜单 > 下载）。在文件副本中，将 Kafka Trigger 节点设置为 `"typeVersion": 1.3`，保留相同的消费组 ID，再将副本导入一个新的空工作流。如果导入后 Kafka 凭据被清空，请重新选择，再发布恢复后的工作流。通过节点面板添加的触发器为版本 2，因此添加新触发器无法完成回滚。

之后消费组的行为取决于你之前如何运行版本 2：

- 如果两个触发器使用不同的消费组 ID 并行运行，无需使用上述任一种恢复方式：取消发布或删除版本 2 工作流即可，原触发器从未受到影响。
- 如果迁移时共用消费组 ID，回滚后的触发器会重新加入消费组，从已提交的位置继续读取，包括切换期间到达的消息。
- 如果切换时使用了新的消费组 ID，回滚后的触发器会再次投递版本 2 已处理的消息，因为版本 2 运行期间，旧消费组的读取位置并未前移。
