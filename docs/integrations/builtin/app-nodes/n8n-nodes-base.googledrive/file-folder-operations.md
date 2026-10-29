---
title: Google Drive 文件和文件夹操作
contentType:
- integration
- reference
priority: high
nodeTitle: Google Drive 文件和文件夹操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-folder-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-folder-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-folder-operations
description: 了解 n8n 工作流自动化平台中 Google Drive 节点的文件和文件夹操作，包括操作及配置详情，以及示例和凭据信息链接。
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


# 文件和文件夹操作 <a id="file-and-folder-operations"></a>

此操作用于在 Google Drive 中搜索文件和文件夹。有关 Google Drive 节点本身的更多信息，请参阅 [Google Drive](./README.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 搜索文件和文件夹 <a href="#search-files-and-folders" id="search-files-and-folders"></a>

此操作用于在云端硬盘中搜索文件和文件夹。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **File/Folder**（文件/文件夹）。
* **Operation**（操作）：选择 **Search**（搜索）。
* **Search Method**（搜索方式）：选择搜索方式：
  * **Search File/Folder Name**（按文件/文件夹名称搜索）：在 **Search Query**（搜索查询）中填写要搜索的文件或文件夹名称。也会返回名称部分匹配的文件和文件夹。
  * **Advanced Search**（高级搜索）：使用 [Google 查询字符串语法](https://developers.google.com/drive/api/guides/search-files)填写 **Query String**（查询字符串），搜索文件和文件夹。
* **Return All**（返回全部）：选择返回所有结果，或仅返回指定数量以内的结果。
* **Limit**（数量限制）：关闭 **Return All**（返回全部）时，返回的最大数据项数量。
* **Filter**（筛选）：选择是否限制搜索范围：
  * **Drive**（云端硬盘）：要搜索的云端硬盘，默认使用个人的 My Drive（我的云端硬盘）。选择 **From list**（从列表）可在下拉列表中选择，选择 **By URL**（按 URL）可输入其 URL，选择 **By ID**（按 ID）可输入 `driveId`。
    * 在浏览器中打开共享云端硬盘，复制 URL 的最后一部分，即可找到 `driveId`：`https://drive.google.com/drive/u/1/folders/driveId`。
  * **Folder**（文件夹）：要搜索的文件夹。选择 **From list**（从列表）可在下拉列表中选择文件夹，选择 **By URL**（按 URL）可输入其 URL，选择 **By ID**（按 ID）可输入 `folderId`。
    * 在浏览器中打开共享文件夹，复制 URL 的最后一部分，即可找到 `folderId`：`https://drive.google.com/drive/u/1/folders/folderId`。
  * **What to Search**（搜索对象）：选择搜索 **Files and Folders**（文件和文件夹）、**Files**（文件）或 **Folders**（文件夹）。
  * **Include Trashed Items**（包含垃圾箱内容）：是否同时返回云端硬盘垃圾箱中的内容。

### 选项 <a href="#options" id="options"></a>

* **Fields**（字段）：选择要返回的字段，可选择以下一项或多项：**\[All]**、**explicitlyTrashed**、**exportLinks**、**hasThumbnail**、**iconLink**、**ID**、**Kind**、**mimeType**、**Name**、**Permissions**、**Shared**、**Spaces**、**Starred**、**thumbnailLink**、**Trashed**、**Version** 或 **webViewLink**。

更多信息，请参阅 [Method: files.list | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/list) API 文档。
