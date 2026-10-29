---
title: Google Drive 节点文档
description: 了解如何在 n8n 中使用 Google Drive 节点，并按照技术文档将 Google Drive 节点集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: n8n-nodes-base.googledrive
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googledrive/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Drive 节点 <a href="#google-drive-node" id="google-drive-node"></a>

使用 Google Drive 节点自动处理 Google Drive 中的工作，并将其与其他应用集成。n8n 内置支持多种 Google Drive 功能，包括创建、更新、列出、删除和获取云端硬盘、文件及文件夹。

本页列出了 Google Drive 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Google Drive 凭据](../../credentials/google/README.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* **File**（文件）
    * [**Copy**](file-operations.md#copy-a-file)（复制）文件
    * [**Create from text**](file-operations.md#create-from-text)（从文本创建）
    * [**Delete**](file-operations.md#delete-a-file)（删除）文件
    * [**Download**](file-operations.md#download-a-file)（下载）文件
    * [**Move**](file-operations.md#move-a-file)（移动）文件
    * [**Share**](file-operations.md#share-a-file)（共享）文件
    * [**Update**](file-operations.md#update-a-file)（更新）文件
    * [**Upload**](file-operations.md#upload-a-file)（上传）文件
* **File/Folder**（文件/文件夹）
    * [**Search**](file-folder-operations.md#search-files-and-folders)（搜索）文件和文件夹
* **Folder**（文件夹）
    * [**Create**](folder-operations.md#create-a-folder)（创建）文件夹
    * [**Delete**](folder-operations.md#delete-a-folder)（删除）文件夹
    * [**Share**](folder-operations.md#share-a-folder)（共享）文件夹
* **Shared Drive**（共享云端硬盘）
    * [**Create**](shared-drive-operations.md#create-a-shared-drive)（创建）共享云端硬盘
    * [**Delete**](shared-drive-operations.md#delete-a-shared-drive)（删除）共享云端硬盘
    * [**Get**](shared-drive-operations.md#get-a-shared-drive)（获取）共享云端硬盘
    * [**Get Many**](shared-drive-operations.md#get-many-shared-drives)（获取多项）：获取多个共享云端硬盘
    * [**Update**](shared-drive-operations.md#update-a-shared-drive)（更新）共享云端硬盘

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-base.googledrive 集成模板](https://n8n.io/integrations/google-drive)，或[搜索所有模板](https://n8n.io/workflows/)

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见问题及建议的解决方法，请参阅[常见问题](common-issues.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
