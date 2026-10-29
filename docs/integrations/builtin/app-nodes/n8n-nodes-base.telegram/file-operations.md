---
title: Telegram 节点文件操作文档
description: 了解 n8n 工作流自动化平台中 Telegram 节点的文件操作，以及各项文件操作的配置详情。
contentType:
- integration
- reference
priority: critical
nodeTitle: Telegram 节点文件操作文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.telegram/file-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/file-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/file-operations
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Telegram 节点文件操作 <a href="#telegram-node-file-operations" id="telegram-node-file-operations"></a>

使用此操作从 Telegram 获取文件。有关 Telegram 节点本身的更多信息，请参阅 [Telegram](README.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## Get File（获取文件） <a href="#get-file" id="get-file"></a>

此操作使用 Bot API 的 [getFile](https://core.telegram.org/bots/api#getfile) 方法，从 Telegram 获取文件。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Telegram 凭据](../../credentials/telegram.md)。
* **Resource**（资源）：选择 **File**（文件）。
* **Operation**（操作）：选择 **Get**（获取）。
* **File ID**（文件 ID）：输入要获取的文件 ID。
* **Download**（下载）：选择是否让节点下载文件，开启表示下载，关闭表示不下载。

更多信息，请参阅 Telegram Bot API 的 [getFile](https://core.telegram.org/bots/api#getfile) 文档。
