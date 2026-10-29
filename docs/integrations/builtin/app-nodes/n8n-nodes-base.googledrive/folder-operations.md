---
title: Google Drive 文件夹操作
contentType:
- integration
- reference
priority: high
nodeTitle: Google Drive 文件夹操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googledrive/folder-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/folder-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/folder-operations
description: 了解 n8n 工作流自动化平台中 Google Drive 节点的文件夹操作，包括操作及配置详情，以及示例和凭据信息链接。
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


# 文件夹操作 <a id="folder-operations"></a>

使用这些操作在 Google Drive 中创建、删除和共享文件夹。有关 Google Drive 节点本身的更多信息，请参阅 [Google Drive](./README.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 创建文件夹 <a href="#create-a-folder" id="create-a-folder"></a>

此操作用于在云端硬盘中创建新文件夹。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Folder**（文件夹）。
* **Operation**（操作）：选择 **Create**（创建）。
* **Folder Name**（文件夹名称）：新文件夹使用的名称。
* **Parent Drive**（父级云端硬盘）：选择 **From list**（从列表）可在下拉列表中选择云端硬盘，选择 **By URL**（按 URL）可输入其 URL，选择 **By ID**（按 ID）可输入 `driveId`。
* **Parent Folder**（父文件夹）：选择 **From list**（从列表）可在下拉列表中选择文件夹，选择 **By URL**（按 URL）可输入其 URL，选择 **By ID**（按 ID）可输入 `folderId`。

在浏览器中打开共享云端硬盘或文件夹，复制 URL 的最后一部分，即可找到 `driveId` 和 `folderID`：`https://drive.google.com/drive/u/1/folders/driveId`。

### 选项 <a href="#options" id="options"></a>

* **Simplify Output**（简化输出）：是否返回简化后的响应，而非包含所有字段。
* **Folder Color**（文件夹颜色）：文件夹颜色，使用 RGB 十六进制字符串表示。

更多信息，请参阅 [Method: files.insert | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/insert) API 文档。

## 删除文件夹 <a href="#delete-a-folder" id="delete-a-folder"></a>

此操作用于从云端硬盘删除文件夹。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Folder**（文件夹）。
* **Operation**（操作）：选择 **Delete**（删除）。
* **Folder**（文件夹）：选择要删除的文件夹。
  * 选择 **From list**（从列表）可在下拉列表中选择文件夹，选择 **By URL**（按 URL）可输入文件夹 URL，选择 **By ID**（按 ID）可输入 `folderId`。
  * 可在 Google Drive 文件夹 URL 中找到 `folderId`：`https://drive.google.com/drive/u/0/folders/folderID`。

### 选项 <a href="#options" id="options"></a>

* **Delete Permanently**（永久删除）：是否立即删除文件夹，而非将其移至垃圾箱。

更多信息，请参阅 [Method: files.delete | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/delete) API 文档。

## 共享文件夹 <a href="#share-a-folder" id="share-a-folder"></a>

此操作用于为文件夹添加共享权限。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Folder**（文件夹）。
* **Operation**（操作）：选择 **Share**（共享）。
* **Folder**（文件夹）：选择要共享的文件夹。
  * 选择 **From list**（从列表）可在下拉列表中选择文件夹，选择 **By URL**（按 URL）可输入文件夹 URL，选择 **By ID**（按 ID）可输入 `folderId`。
  * 可在 Google Drive 文件夹 URL 中找到 `folderId`：`https://drive.google.com/drive/u/0/folders/folderID`。
* **Permissions**（权限）：要添加到文件夹的权限：
  * **Role**（角色）：选择用户可以对文件夹执行的操作，可选 **Commenter**（评论者）、**File Organizer**（文件整理者）、**Organizer**（管理者）、**Owner**（所有者）、**Reader**（读取者）或 **Writer**（写入者）。
  * **Type**（类型）：选择新权限的授予范围：
    * **User**（用户）：授予指定用户权限，通过 **Email Address**（邮箱地址）指定用户。
    * **Group**（群组）：授予指定群组权限，通过 **Email Address**（邮箱地址）指定群组。
    * **Domain**（网域）：授予整个网域权限，通过 **Domain**（网域）指定。
    * **Anyone**（任何人）：授予任何人权限。可选择启用 **Allow File Discovery**（允许发现文件），使文件能通过搜索被发现。

### 选项 <a href="#options" id="options"></a>

* **Email Message**（邮件消息）：通知邮件中包含的纯文本自定义消息。
* **Move to New Owners Root**（移至新所有者的根目录）：共享不属于共享云端硬盘的项目，且尝试转移所有权时可用。开启后，将文件夹移至新所有者的 My Drive（我的云端硬盘）根文件夹。
* **Send Notification Email**（发送通知邮件）：向用户或群组共享时，是否发送通知邮件。
* **Transfer Ownership**（转移所有权）：是否将所有权转移给指定用户，并将当前所有者降为写入者权限。
* **Use Domain Admin Access**（使用网域管理员权限）：是否以网域管理员身份执行操作。

更多信息，请参阅 [REST Resources: files | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files) API 文档。
