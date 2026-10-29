---
title: Read/Write Files from Disk 节点
contentType:
- integration
- reference
priority: critical
nodeTitle: Read/Write Files from Disk 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile
description: 了解 n8n 中 Read/Write Files from Disk 节点的用法，并查看相关示例。
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


# Read/Write Files from Disk（读写磁盘文件） <a id="readwrite-files-from-disk"></a>

使用 Read/Write Files from Disk 节点，在运行 n8n 的机器上读取和写入文件。

节点可访问的路径取决于 n8n 的部署方式，详见[文件位置](n8n-nodes-base.readwritefile.md#file-locations)。

## 操作 <a href="#operations" id="operations"></a>

* [**Read File(s) From Disk**](n8n-nodes-base.readwritefile.md#read-files-from-disk)（从磁盘读取文件）：从运行 n8n 的计算机检索一个或多个文件。
* [**Write File to Disk**](n8n-nodes-base.readwritefile.md#write-file-to-disk)（向磁盘写入文件）：在运行 n8n 的计算机上创建二进制文件。

各操作的节点配置说明见下文。

## Read File(s) From Disk（从磁盘读取文件） <a href="#read-files-from-disk" id="read-files-from-disk"></a>

使用以下参数配置此操作：

* **File(s) Selector**（文件选择器）：输入要读取的文件路径。
  * 要读取多个文件，输入路径匹配模式，可使用以下字符：
    * `*`：匹配零个或多个任意字符，不包含路径分隔符。
    * `**`：匹配零个或多个任意字符，包含路径分隔符。
    * `?`：匹配一个任意字符，不包含路径分隔符。
    * `[]`：匹配方括号中的任一字符。例如，`[abc]` 仅匹配 `a`、`b` 或 `c`。

有关这些字符及其预期行为的更多信息，请参阅 [Picomatch 的基本 glob 匹配](https://github.com/micromatch/picomatch#basic-globbing)文档。

### Read File(s) From Disk（从磁盘读取文件）选项 <a href="#read-files-from-disk-options" id="read-files-from-disk-options"></a>

还可通过以下 **Options**（选项）配置此操作：

* **File Extension**（文件扩展名）：输入节点输出中的文件扩展名。
* **File Name**（文件名称）：输入节点输出中的文件名称。
* **MIME Type**（MIME 类型）：输入节点输出中的文件 MIME 类型。扩展名及其 MIME 类型列表，请参阅[常见 MIME 类型](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types)。
* **Put Output File in Field**（输出文件字段）：输入用于存放文件的输出数据字段名称。

## Write File to Disk（向磁盘写入文件） <a href="#write-file-to-disk" id="write-file-to-disk"></a>

使用以下参数配置此操作：

* **File Path and Name**（文件路径与名称）：输入文件的目标位置、名称和扩展名。
* **Input Binary Field**（输入二进制字段）：输入节点输入数据中包含二进制文件的字段名称。

### Write File to Disk（向磁盘写入文件）选项 <a href="#write-file-to-disk-options" id="write-file-to-disk-options"></a>

还可通过以下 **Options**（选项）配置此操作：

此操作只有一个 **Append**（追加）选项：开启时，将数据追加到现有文件，而不是创建新文件；关闭时，创建新文件，而不向现有文件追加。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Read/Write Files from Disk 集成模板](https://n8n.io/integrations/readwrite-files-from-disk)，或[搜索所有模板](https://n8n.io/workflows/)

## 文件位置 <a href="#file-locations" id="file-locations"></a>

节点可读写的路径取决于 n8n 的部署方式。

### n8n Cloud <a href="#n8n-cloud" id="n8n-cloud"></a>

在 n8n Cloud 上，节点只能访问 `/home/node/` 下的路径。访问此目录之外的路径，例如 `/tmp/` 或 `/data/`，会出现访问错误。

{% hint style="info" %}
**Cloud 上的字段占位符**

节点 **File(s) Selector**（文件选择器）和 **File Path and Name**（文件路径与名称）中的默认占位符，例如 `/home/user/Pictures/**/*.png` 和 `/data/example.jpg`，只是示例。在 Cloud 上，应将其替换为 `/home/node/` 下的路径。
{% endhint %}

{% hint style="warning" %}
**Cloud 文件系统是临时的**

此节点在 Cloud 上写入的文件，不保证能在工作流多次执行、工作进程重启或实例重新部署后保留。不要用此节点保存需要长期保留的文件。

n8n 将 `/home/node/.n8n/` 目录保留给内部状态使用，不要在该目录写入自己的文件。

要在 Cloud 上持久保存文件，请使用 [AWS S3](../app-nodes/n8n-nodes-base.awss3.md)、[Google Drive](../app-nodes/n8n-nodes-base.googledrive/README.md) 或 [FTP](n8n-nodes-base.ftp.md) 等云存储节点。
{% endhint %}

### 自托管 n8n <a href="#self-hosted-n8n" id="self-hosted-n8n"></a>

在自托管 n8n 中，可访问路径同时受 n8n 进程权限及文件访问限制约束。可将 [`N8N_RESTRICT_FILE_ACCESS_TO`](../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/security.md) 环境变量设为一个或多个允许访问的目录，以分号分隔；n8n 2.0 起的默认限制见下文。

{% hint style="info" %}
**功能可用性**

从 n8n 2.0 起，`N8N_RESTRICT_FILE_ACCESS_TO` 默认为 `~/.n8n-files`。要在其他位置操作文件，请显式设置此变量。详见 [n8n 2.0 破坏性变更](../../../changelog/v20-breaking-changes.md#set-default-value-for-n8n_restrict_file_access_to)。
{% endhint %}

如果使用 Docker 运行 n8n，路径指向 n8n 容器的文件系统，而不是 Docker 宿主机。要让节点访问宿主机目录，请将其作为卷挂载到容器中。

n8n 建议使用绝对文件路径，以避免错误。
