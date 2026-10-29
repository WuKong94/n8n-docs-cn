---
title: 二进制数据
description: 了解并使用 n8n 中的二进制数据。
contentType: overview
tags:
- binary data
hide:
- tags
nodeTitle: 处理文件和图片
originalFilePath: data/specific-data-types/binary-data.md
originalUrl: https://docs.n8n.io/data/specific-data-types/binary-data
url: https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-files-and-images
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 二进制数据 <a href="#binary-data" id="binary-data"></a>

二进制数据是指各种文件类型的数据，例如图片文件或文档。

本页汇总了 n8n 中与二进制数据相关的资源。

## 在工作流中处理二进制数据 <a href="#working-with-binary-data-in-your-workflows" id="working-with-binary-data-in-your-workflows"></a>

你可以在 n8n 工作流中处理二进制数据。n8n 提供了专门的节点，也支持使用代码进行处理。

### 节点 <a href="#nodes" id="nodes"></a>

以下三个主要节点专门用于处理二进制数据文件：

- [Convert to File](../../../integrations/builtin/core-nodes/n8n-nodes-base.converttofile.md)：接收输入数据，并将其输出为文件。
- [Extract From File](../../../integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile.md)：从二进制格式中提取数据并转换为 JSON。
- [Read/Write Files from Disk](../../../integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md)：在运行 n8n 的计算机上读取和写入文件。

XML 和 HTML 数据分别由以下节点处理：

* [HTML](../../../integrations/builtin/core-nodes/n8n-nodes-base.html.md)
* [XML](../../../integrations/builtin/core-nodes/n8n-nodes-base.xml.md)

以下节点用于执行常见任务：

* [Compression（压缩）](../../../integrations/builtin/core-nodes/n8n-nodes-base.compression.md)
* [Edit Image（编辑图片）](../../../integrations/builtin/core-nodes/n8n-nodes-base.editimage.md)
* [FTP](../../../integrations/builtin/core-nodes/n8n-nodes-base.ftp.md)

你可以使用 [Local File 触发器](../../../integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger.md)，在本地文件发生变化时触发工作流。

要拆分或拼接二进制数据项，请使用[数据转换节点](../expressions-versus-data-nodes.md#other-data-transformation-nodes)。

### 代码 <a href="#code" id="code"></a>

你可以使用 [Code 节点](../../code-in-n8n/using-the-code-node.md)处理工作流中的二进制数据。例如，[获取二进制数据缓冲区](../../code-in-n8n/cookbook/code-node/get-the-binary-data-buffer.md)介绍了如何获取工作流中可用的二进制数据。


## 在自托管环境中配置二进制数据模式 <a href="#configure-binary-data-mode-when-self-hosting" id="configure-binary-data-mode-when-self-hosting"></a>

你可以通过[二进制数据环境变量](../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/binary-data.md)，配置自托管 n8n 实例处理二进制数据的方式，例如设置存储路径和选择存储方式。

这些配置会影响 n8n 的扩展能力，详见[扩展 | 二进制数据文件系统模式](../../../deploy/host-n8n/configure-n8n/scaling/handle-binary-data.md)。

读写二进制文件可能涉及安全问题。如果要禁用二进制数据的读取和写入，请使用 `NODES_EXCLUDE` 环境变量。更多信息请参阅[环境变量 | 节点](../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes.md)。

## 相关资源 <a id="related-resources"></a>

* [处理特殊数据类型](./)
* [处理日期和时间](work-with-dates-and-times.md)
* [查询 JSON 数据](query-json-data.md)
