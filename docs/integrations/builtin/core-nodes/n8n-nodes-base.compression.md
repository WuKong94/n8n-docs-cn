---
title: Compression（压缩）
description: 工作流自动化平台 n8n 中的 Compression（压缩） 节点文档，包括使用说明和示例链接。
contentType:
- integration
- reference
priority: medium
nodeTitle: n8n-nodes-base.compression
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.compression.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.compression
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.compression
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Compression（压缩） <a href="#compression" id="compression"></a>

使用 Compression 节点压缩和解压缩文件。支持 Zip、Gzip、Tar 和 Tar.gz 格式。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

节点参数取决于所选 **Operation**（操作）。可选择：

* **Compress**（压缩）：使用输入数据创建压缩文件。
* **Decompress**（解压缩）：解压缩已有压缩文件。

各 **Operation**（操作）的专用参数，请参阅下方各节。

### Compress（压缩） <a href="#compress" id="compress"></a>

- **Input Binary Field(s)**（输入二进制字段）：输入包含待压缩二进制文件的输入数据字段名称。要压缩多个文件，请以逗号分隔字段名称。
- **Output Format**（输出格式）：选择将压缩输出保存为 **Zip**、**Gzip**、**Tar** 或 **Tar (Gzip)** 格式。
- **File Name**（文件名称）：输入节点创建的压缩文件名称。
- **Put Output File in Field**（输出文件存入字段）：输入用于存放文件的输出数据字段名称。

### Decompress（解压缩） <a href="#decompress" id="decompress"></a>

Decompress 操作根据文件扩展名识别归档格式，支持以下格式：

- `.zip`
- `.gz` 和 `.gzip`
- `.tar`
- `.tar.gz` 和 `.tgz`

解压缩 `.tar.gz` 或 `.tgz` 归档时，节点会一次提取其中的所有文件，无需单独解压 gzip 层。

- **Input Binary Field(s)**（输入二进制字段）：输入包含待解压二进制文件的输入数据字段名称。要解压多个文件，请以逗号分隔字段名称。
- **Output Prefix**（输出前缀）：输入要添加到输出文件名称的前缀。节点以该前缀加上递增索引，为每个提取的文件命名。

{% hint style="warning" %}
#### 不支持的格式 <a id="unsupported-formats"></a>

如果传入文件的扩展名不受支持，节点会抛出错误，而不会无提示地产生空输出。支持的格式为 `zip`、`gzip`、`tar`、`tar.gz` 和 `tgz`。
{% endhint %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Compression（压缩）集成模板](https://n8n.io/integrations/compression)，或[搜索所有模板](https://n8n.io/workflows/)
