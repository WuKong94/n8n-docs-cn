---
nodeTitle: BinaryFile（二进制文件）
originalFilePath: data/expression-reference/binaryfile.md
originalUrl: https://docs.n8n.io/data/expression-reference/binaryfile
url: https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# BinaryFile（二进制文件） <a href="#binaryfile" id="binaryfile"></a>

## `binaryFile`.**`directory`** <a href="#binaryfiledirectory" id="binaryfiledirectory"></a>

**说明：** 文件所在目录的路径，可用于区分不同目录中的同名文件。如果 n8n 配置为将文件存储在数据库中，则不设置此值。

**语法：** `binaryFile`.**`directory`**

**返回值：** String（字符串）

**来源：** n8n 自定义功能

## `binaryFile`.**`fileExtension`** <a href="#binaryfilefileextension" id="binaryfilefileextension"></a>

**说明：** 文件名末尾的后缀，例如 <code>txt</code>。

**语法：** `binaryFile`.**`fileExtension`**

**返回值：** String（字符串）

**来源：** n8n 自定义功能

## `binaryFile`.**`fileName`** <a href="#binaryfilefilename" id="binaryfilefilename"></a>

**说明：** 文件名，包含扩展名。

**语法：** `binaryFile`.**`fileName`**

**返回值：** String（字符串）

**来源：** n8n 自定义功能

## `binaryFile`.**`fileSize`** <a href="#binaryfilefilesize" id="binaryfilefilesize"></a>

**说明：** 表示文件大小的字符串。

**语法：** `binaryFile`.**`fileSize`**

**返回值：** String（字符串）

**来源：** n8n 自定义功能

## `binaryFile`.**`fileType`** <a href="#binaryfilefiletype" id="binaryfilefiletype"></a>

**说明：** 表示文件类型的字符串，例如 <code>image</code>。对应 MIME 类型的第一部分。

**语法：** `binaryFile`.**`fileType`**

**返回值：** String（字符串）

**来源：** n8n 自定义功能

## `binaryFile`.**`id`** <a href="#binaryfileid" id="binaryfileid"></a>

**说明：** 文件的唯一 ID。当文件存储在磁盘或 S3 等存储服务中时，用于标识该文件。

**语法：** `binaryFile`.**`id`**

**返回值：** String（字符串）

**来源：** n8n 自定义功能

## `binaryFile`.**`mimeType`** <a href="#binaryfilemimetype" id="binaryfilemimetype"></a>

**说明：** 表示文件内容格式的字符串，例如 <code>image/jpeg</code>。

**语法：** `binaryFile`.**`mimeType`**

**返回值：** String（字符串）

**来源：** n8n 自定义功能


## 相关资源 <a id="related-resources"></a>

* [表达式参考](./)
