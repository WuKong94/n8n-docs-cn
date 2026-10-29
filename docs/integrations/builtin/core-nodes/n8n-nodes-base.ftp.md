---
title: FTP 节点
contentType:
- integration
- reference
priority: medium
nodeTitle: FTP 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.ftp.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ftp
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ftp
description: 了解 n8n 中 FTP 节点的用法，并查看相关示例。
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


# FTP <a id="ftp"></a>

FTP 节点用于访问 FTP 或 SFTP 服务器中的文件，以及向服务器上传文件。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [FTP 凭据文档](../credentials/ftp.md)。
{% endhint %}

连接 SFTP 服务器时，请使用 SFTP 凭据。更多信息，请参阅 [FTP 凭据](../credentials/ftp.md)。

## 操作 <a href="#operations" id="operations"></a>

* [**Delete**](n8n-nodes-base.ftp.md#delete)（删除）文件或文件夹
* [**Download**](n8n-nodes-base.ftp.md#download)（下载）文件
* [**List**](n8n-nodes-base.ftp.md#list)（列出）文件夹内容
* [**Rename**](n8n-nodes-base.ftp.md#rename)（重命名）或移动文件及文件夹
* [**Upload**](n8n-nodes-base.ftp.md#upload)（上传）文件

{% hint style="info" %}
**上传文件**

要提供待上传的文件，需要使用 [Read/Write Files from Disk](n8n-nodes-base.readwritefile.md) 或 [HTTP Request](n8n-nodes-base.httprequest/README.md) 等额外节点，将文件作为数据属性传入。
{% endhint %}

## Delete（删除） <a href="#delete" id="delete"></a>

此操作只有一个 **Path**（路径）参数，输入要连接的远程路径。

### Delete（删除）选项 <a href="#delete-options" id="delete-options"></a>

删除操作增加 **Folder**（文件夹）选项。开启时，节点可以删除文件夹和文件，并显示另一个选项：

* **Recursive**（递归）：开启时，删除文件夹或目录会同时删除目标目录内的所有文件和目录。

## Download（下载） <a href="#download" id="download"></a>

使用以下参数配置此操作：

* **Path**（路径）：输入要连接的远程路径。
* **Put Output File in Field**（输出文件字段）：输入用于存放文件的输出二进制字段名称。

{% hint style="info" %}
**SFTP 并发读取**

使用 SFTP 时，可以启用并发读取以提高下载速度，但并非所有 SFTP 服务器都支持。
{% endhint %}

## List（列出） <a href="#list" id="list"></a>

使用以下参数配置此操作：

* **Path**（路径）：输入要连接的远程路径。
* **Recursive**（递归）：开启时，递归返回表示 FTP/SFTP 服务器中所有目录或对象的对象；关闭时，不递归返回。

## Rename（重命名） <a href="#rename" id="rename"></a>

使用以下参数配置此操作：

* **Old Path**（原路径）：输入待重命名文件的现有路径。
* **New Path**（新路径）：输入重命名后文件的新路径。

### Rename（重命名）选项 <a href="#rename-options" id="rename-options"></a>

此操作增加 **Create Directories**（创建目录）选项。开启时，重命名现有文件或文件夹会递归创建目标目录。

## Upload（上传） <a href="#upload" id="upload"></a>

使用以下参数配置此操作：

* **Path**（路径）：输入要连接的远程路径。
* **Binary File**（二进制文件）：开启时上传二进制文件，关闭时输入要上传的文本内容。其他参数取决于此选项。
  * **Input Binary Field**（输入二进制字段）：开启 **Binary File**（二进制文件）时显示，输入包含待上传文件的输入二进制字段名称。
  * **File Content**（文件内容）：关闭 **Binary File**（二进制文件）时显示，输入要上传的文件文本内容。

{% hint style="info" %}
**上传文件**

要提供待上传的文件，需要使用 [Read/Write Files from Disk](n8n-nodes-base.readwritefile.md) 或 [HTTP Request](n8n-nodes-base.httprequest/README.md) 等额外节点，将文件作为数据属性传入。
{% endhint %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 FTP 集成模板](https://n8n.io/integrations/ftp)，或[搜索所有模板](https://n8n.io/workflows/)
