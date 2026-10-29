---
title: SSH 节点
contentType:
- integration
- reference
priority: medium
nodeTitle: SSH 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.ssh.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh
description: 了解 n8n 中 SSH 节点的用法，并查看相关示例。
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


# SSH <a id="ssh"></a>

SSH 节点通过 Secure Shell（安全外壳）协议执行命令。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [SSH 凭据文档](../credentials/ssh.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* [**Execute**（执行）命令](n8n-nodes-base.ssh.md#execute-command)
* [**Download**（下载）文件](n8n-nodes-base.ssh.md#download-file)
* [**Upload**（上传）文件](n8n-nodes-base.ssh.md#upload-file)

{% hint style="info" %}
**上传文件**

要提供待上传的文件，需要使用 [Read/Write Files from Disk](n8n-nodes-base.readwritefile.md) 或 [HTTP Request](n8n-nodes-base.httprequest/README.md) 等额外节点，将文件作为数据属性传入。
{% endhint %}

### Execute Command（执行命令） <a href="#execute-command" id="execute-command"></a>

使用以下参数配置此操作：

* **Credential to connect with**（连接凭据）：选择已有的 [SSH 凭据](../credentials/ssh.md)，或创建新凭据用于连接。
* **Command**（命令）：输入要在远程设备上执行的命令。
* **Working Directory**（工作目录）：输入 n8n 执行命令的目录。

### Download File（下载文件） <a href="#download-file" id="download-file"></a>

* **Credential to connect with**（连接凭据）：选择已有的 [SSH 凭据](../credentials/ssh.md)，或创建新凭据用于连接。
* **Path**（路径）：输入待下载文件的路径，必须包含文件名。下载文件将使用此文件名；要更改名称，使用 **File Name**（文件名称）选项。更多信息，请参阅[下载文件选项](n8n-nodes-base.ssh.md#download-file-options)。
* **File Property**（文件属性）：输入用于存放下载文件二进制数据的对象属性名称。

#### Download File（下载文件）选项 <a href="#download-file-options" id="download-file-options"></a>

还可使用 **File Name**（文件名称）选项进一步配置，将二进制数据的文件名称覆盖为指定名称。

### Upload File（上传文件） <a href="#upload-file" id="upload-file"></a>

* **Credential to connect with**（连接凭据）：选择已有的 [SSH 凭据](../credentials/ssh.md)，或创建新凭据用于连接。
* **Input Binary Field**（输入二进制字段）：输入包含待上传文件的输入二进制字段名称。
* **Target Directory**（目标目录）：要上传文件的目录。文件名取自二进制数据中的文件名；要更改名称，使用 **File Name**（文件名称）选项。更多信息，请参阅[上传文件选项](n8n-nodes-base.ssh.md#upload-file-options)。

#### Upload File（上传文件）选项 <a href="#upload-file-options" id="upload-file-options"></a>

还可使用 **File Name**（文件名称）选项进一步配置，将二进制数据的文件名称覆盖为指定名称。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 SSH 集成模板](https://n8n.io/integrations/ssh)，或[搜索所有模板](https://n8n.io/workflows/)
