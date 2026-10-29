---
title: Google Drive 文件操作
description: 了解 n8n 工作流自动化平台中 Google Drive 节点的文件操作，包括操作及配置详情，以及示例和凭据信息链接。
contentType:
- integration
- reference
priority: high
nodeTitle: Google Drive 文件操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Drive 文件操作 <a href="#google-drive-file-operations" id="google-drive-file-operations"></a>

使用这些操作在 Google Drive 中创建、删除、修改和管理文件。有关 Google Drive 节点本身的更多信息，请参阅 [Google Drive](README.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 复制文件 <a href="#copy-a-file" id="copy-a-file"></a>

此操作用于将文件复制到云端硬盘。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
- **Resource**（资源）：选择 **File**（文件）。
- **Operation**（操作）：选择 **Copy**（复制）。
- **File**（文件）：选择要复制的文件。
    - 选择 **From list**（从列表）可在下拉列表中按标题选择，选择 **By URL**（按 URL）可输入文件 URL，选择 **By ID**（按 ID）可输入 `fileId`。
    - 可在可分享的 Google Drive 文件 URL 中找到 `fileId`：`https://docs.google.com/document/d/fileId/edit#gid=0`。在 Google Drive 中选择 **Share > Copy link**（共享 > 复制链接），即可获取可分享的文件 URL。
- **File Name**（文件名）：文件新副本使用的名称。
- **Copy In The Same Folder**（复制到同一文件夹）：是否将文件复制到同一个文件夹。关闭时，需设置：
    - **Parent Drive**（父级云端硬盘）：选择 **From list**（从列表）可在下拉列表中选择云端硬盘，选择 **By URL**（按 URL）可输入其 URL，选择 **By ID**（按 ID）可输入 `driveId`。
    - **Parent Folder**（父文件夹）：选择 **From list**（从列表）可在下拉列表中选择文件夹，选择 **By URL**（按 URL）可输入其 URL，选择 **By ID**（按 ID）可输入 `folderId`。
    - 在浏览器中打开共享云端硬盘或文件夹，复制 URL 的最后一部分，即可找到 `driveId` 和 `folderID`：`https://drive.google.com/drive/u/1/folders/driveId`。

### 选项 <a href="#options" id="options"></a>

- **Copy Requires Writer Permissions**（复制需要写入者权限）：是否禁止读取者和评论者复制、打印或下载新文件。
- **Description**（描述）：文件的简短描述。

更多信息，请参阅 [Method: files.copy | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/copy) API 文档。

## 从文本创建文件 <a href="#create-from-text" id="create-from-text"></a>

此操作用于根据提供的文本，在云端硬盘中创建新文件。

填写以下参数：
- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
- **Resource**（资源）：选择 **File**（文件）。
- **Operation**（操作）：选择 **Create From Text**（从文本创建）。
- **File Content**（文件内容）：输入创建新文件所用的内容。
- **File Name**（文件名）：新文件使用的名称。
- **Parent Drive**（父级云端硬盘）：选择 **From list**（从列表）可在下拉列表中选择云端硬盘，选择 **By URL**（按 URL）可输入其 URL，选择 **By ID**（按 ID）可输入 `driveId`。
- **Parent Folder**（父文件夹）：选择 **From list**（从列表）可在下拉列表中选择文件夹，选择 **By URL**（按 URL）可输入其 URL，选择 **By ID**（按 ID）可输入 `folderId`。

在浏览器中打开共享云端硬盘或文件夹，复制 URL 的最后一部分，即可找到 `driveId` 和 `folderID`：`https://drive.google.com/drive/u/1/folders/driveId`。

### 选项 <a href="#options" id="options"></a>

- **APP Properties**（应用属性）：仅请求应用可见的一组任意键值对。
- **Properties**（属性）：所有应用均可见的一组任意键值对。
- **Keep Revision Forever**（永久保留修订版本）：是否设置最新修订版本中的 `keepForever` 字段。仅适用于包含二进制内容的文件。最多可保留 200 个修订版本，达到上限后必须删除已固定保留的修订版本。


- **OCR Language**（OCR 语言）：用于帮助 OCR 在导入时解析内容的 [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) 语言代码。


- **Use Content As Indexable Text**（将内容用作可索引文本）：是否将上传内容标记为可索引文本。
- **Convert to Google Document**（转换为 Google 文档）：是否创建 Google 文档，而非默认的 `.txt` 格式。必须在 [Google API Console](https://console.cloud.google.com/apis/library/docs.googleapis.com)（Google API 控制台）中启用 Google Docs API，此功能才能工作。

更多信息，请参阅 [Method: files.insert | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/insert) API 文档。

## 删除文件 <a href="#delete-a-file" id="delete-a-file"></a>

此操作用于从云端硬盘删除文件。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
- **Resource**（资源）：选择 **File**（文件）。
- **Operation**（操作）：选择 **Delete**（删除）。
- **File**（文件）：选择要删除的文件。
    - 选择 **From list**（从列表）可在下拉列表中按标题选择，选择 **By URL**（按 URL）可输入文件 URL，选择 **By ID**（按 ID）可输入 `fileId`。
    - 可在可分享的 Google Drive 文件 URL 中找到 `fileId`：`https://docs.google.com/document/d/fileId/edit#gid=0`。在 Google Drive 中选择 **Share > Copy link**（共享 > 复制链接），即可获取可分享的文件 URL。

### 选项 <a href="#options" id="options"></a>

- **Delete Permanently**（永久删除）：是否立即删除文件，而非将其移至垃圾箱。

更多信息，请参阅 [Method: files.delete | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/delete) API 文档。

## 下载文件 <a href="#download-a-file" id="download-a-file"></a>

此操作用于从云端硬盘下载文件。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
- **Resource**（资源）：选择 **File**（文件）。
- **Operation**（操作）：选择 **Download**（下载）。
- **File**（文件）：选择要下载的文件。
    - 选择 **From list**（从列表）可在下拉列表中按标题选择，选择 **By URL**（按 URL）可输入文件 URL，选择 **By ID**（按 ID）可输入 `fileId`。
    - 可在可分享的 Google Drive 文件 URL 中找到 `fileId`：`https://docs.google.com/document/d/fileId/edit#gid=0`。在 Google Drive 中选择 **Share > Copy link**（共享 > 复制链接），即可获取可分享的文件 URL。

### 选项 <a href="#options" id="options"></a>

- **Put Output File in Field**（输出文件所在字段）：选择保存二进制文件内容的字段名，供后续节点使用。
- **Google File Conversion**（Google 文件转换）：选择下载 Google 文件时使用的导出格式：
    * **Google Docs**（Google 文档）：选择下载 Google 文档文件时的导出格式：**HTML**、**MS Word Document**（Word 文档）、**Open Office Document**（OpenOffice 文档）、**PDF**、**Rich Text (rtf)**（富文本）或 **Text (txt)**（纯文本）。
    * **Google Drawings**（Google 绘图）：选择下载 Google 绘图文件时的导出格式：**JPEG**、**PDF**、**PNG** 或 **SVG**。
    * **Google Slides**（Google 幻灯片）：选择下载 Google 幻灯片文件时的导出格式：**MS PowerPoint**（PowerPoint 演示文稿）、**OpenOffice Presentation**（OpenOffice 演示文稿）或 **PDF**。
    * **Google Sheets**（Google 表格）：选择下载 Google 表格文件时的导出格式：**CSV**、**MS Excel**（Excel 电子表格）、**Open Office Sheet**（OpenOffice 电子表格）或 **PDF**。
- **File Name**（文件名）：下载文件使用的名称。

更多信息，请参阅 [Method: files.get | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/get) API 文档。

## 移动文件 <a href="#move-a-file" id="move-a-file"></a>

此操作用于将文件移至云端硬盘中的其他位置。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
- **Resource**（资源）：选择 **File**（文件）。
- **Operation**（操作）：选择 **Move**（移动）。
- **File**（文件）：选择要移动的文件。
    - 选择 **From list**（从列表）可在下拉列表中按标题选择，选择 **By URL**（按 URL）可输入文件 URL，选择 **By ID**（按 ID）可输入 `fileId`。
    - 可在可分享的 Google Drive 文件 URL 中找到 `fileId`：`https://docs.google.com/document/d/fileId/edit#gid=0`。在 Google Drive 中选择 **Share > Copy link**（共享 > 复制链接），即可获取可分享的文件 URL。
- **Parent Drive**（父级云端硬盘）：选择 **From list**（从列表）可在下拉列表中选择云端硬盘，选择 **By URL**（按 URL）可输入其 URL，选择 **By ID**（按 ID）可输入 `driveId`。
- **Parent Folder**（父文件夹）：选择 **From list**（从列表）可在下拉列表中选择文件夹，选择 **By URL**（按 URL）可输入其 URL，选择 **By ID**（按 ID）可输入 `folderId`。

在浏览器中打开共享云端硬盘或文件夹，复制 URL 的最后一部分，即可找到 `driveId` 和 `folderID`：`https://drive.google.com/drive/u/1/folders/driveId`。

更多信息，请参阅 [Method: parents.insert | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/parents/insert) API 文档。

## 共享文件 <a href="#share-a-file" id="share-a-file"></a>

此操作用于为文件添加共享权限。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
- **Resource**（资源）：选择 **File**（文件）。
- **Operation**（操作）：选择 **Share**（共享）。
- **File**（文件）：选择要共享的文件。
    - 选择 **From list**（从列表）可在下拉列表中按标题选择，选择 **By URL**（按 URL）可输入文件 URL，选择 **By ID**（按 ID）可输入 `fileId`。
    - 可在可分享的 Google Drive 文件 URL 中找到 `fileId`：`https://docs.google.com/document/d/fileId/edit#gid=0`。在 Google Drive 中选择 **Share > Copy link**（共享 > 复制链接），即可获取可分享的文件 URL。
- **Permissions**（权限）：要添加到文件的权限：
    - **Role**（角色）：选择用户可以对文件执行的操作，可选 **Commenter**（评论者）、**File Organizer**（文件整理者）、**Organizer**（管理者）、**Owner**（所有者）、**Reader**（读取者）或 **Writer**（写入者）。
    - **Type**（类型）：选择新权限的授予范围：
        - **User**（用户）：授予指定用户权限，通过 **Email Address**（邮箱地址）指定用户。
        - **Group**（群组）：授予指定群组权限，通过 **Email Address**（邮箱地址）指定群组。
        - **Domain**（网域）：授予整个网域权限，通过 **Domain**（网域）指定。
        - **Anyone**（任何人）：授予任何人权限。可选择启用 **Allow File Discovery**（允许发现文件），使文件能通过搜索被发现。

### 选项 <a href="#options" id="options"></a>

- **Email Message**（邮件消息）：通知邮件中包含的纯文本自定义消息。

- **Move to New Owners Root**（移至新所有者的根目录）：共享不属于共享云端硬盘的项目，且尝试转移所有权时可用。开启后，将文件移至新所有者的 My Drive（我的云端硬盘）根文件夹。

- **Send Notification Email**（发送通知邮件）：向用户或群组共享时，是否发送通知邮件。
- **Transfer Ownership**（转移所有权）：是否将所有权转移给指定用户，并将当前所有者降为写入者权限。
- **Use Domain Admin Access**（使用网域管理员权限）：是否以网域管理员身份执行操作。

更多信息，请参阅 [REST Resources: files | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files) API 文档。

## 更新文件 <a href="#update-a-file" id="update-a-file"></a>

此操作用于更新文件。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
- **Resource**（资源）：选择 **File**（文件）。
- **Operation**（操作）：选择 **Update**（更新）。
- **File to Update**（待更新文件）：选择要更新的文件。
    - 选择 **From list**（从列表）可在下拉列表中按标题选择，选择 **By URL**（按 URL）可输入文件 URL，选择 **By ID**（按 ID）可输入 `fileId`。
    - 可在可分享的 Google Drive 文件 URL 中找到 `fileId`：`https://docs.google.com/document/d/fileId/edit#gid=0`。在 Google Drive 中选择 **Share > Copy link**（共享 > 复制链接），即可获取可分享的文件 URL。
- **Change File Content**（更改文件内容）：是否发送新的二进制数据，替换已有文件内容。开启时，需填写：
    - **Input Data Field Name**（输入数据字段名）：包含所需二进制文件数据的输入字段名称。
- **New Updated File Name**（更新后的新文件名）：如需更改文件名，填写新的名称。

### 选项 <a href="#options" id="options"></a>

- **APP Properties**（应用属性）：仅请求应用可见的一组任意键值对。
- **Properties**（属性）：所有应用均可见的一组任意键值对。
- **Keep Revision Forever**（永久保留修订版本）：是否设置最新修订版本中的 `keepForever` 字段。仅适用于包含二进制内容的文件。最多可保留 200 个修订版本，达到上限后必须删除已固定保留的修订版本。


- **OCR Language**（OCR 语言）：用于帮助 OCR 在导入时解析内容的 [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) 语言代码。


- **Use Content As Indexable Text**（将内容用作可索引文本）：是否将上传内容标记为可索引文本。
- **Move to Trash**（移至垃圾箱）：是否将文件移至垃圾箱。仅文件所有者可执行。
- **Return Fields**（返回字段）：返回文件的元数据字段，可选择以下一项或多项：**[All]**、**explicitlyTrashed**、**exportLinks**、**hasThumbnail**、**iconLink**、**ID**、**Kind**、**mimeType**、**Name**、**Permissions**、**Shared**、**Spaces**、**Starred**、**thumbnailLink**、**Trashed**、**Version** 或 **webViewLink**。

更多信息，请参阅 [Method: files.update | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/update) API 文档。

## 上传文件 <a href="#upload-a-file" id="upload-a-file"></a>

此操作用于上传文件。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
- **Resource**（资源）：选择 **File**（文件）。
- **Operation**（操作）：选择 **Upload**（上传）。
- **Input Data Field Name**（输入数据字段名）：包含所需二进制文件数据的输入字段名称。
- **File Name**（文件名）：新文件使用的名称。
- **Parent Drive**（父级云端硬盘）：选择 **From list**（从列表）可在下拉列表中选择云端硬盘，选择 **By URL**（按 URL）可输入其 URL，选择 **By ID**（按 ID）可输入 `driveId`。
- **Parent Folder**（父文件夹）：选择 **From list**（从列表）可在下拉列表中选择文件夹，选择 **By URL**（按 URL）可输入其 URL，选择 **By ID**（按 ID）可输入 `folderId`。

在浏览器中打开共享云端硬盘或文件夹，复制 URL 的最后一部分，即可找到 `driveId` 和 `folderID`：`https://drive.google.com/drive/u/1/folders/driveId`。

### 选项 <a href="#options" id="options"></a>

- **APP Properties**（应用属性）：仅请求应用可见的一组任意键值对。
- **Properties**（属性）：所有应用均可见的一组任意键值对。
- **Keep Revision Forever**（永久保留修订版本）：是否设置最新修订版本中的 `keepForever` 字段。仅适用于包含二进制内容的文件。最多可保留 200 个修订版本，达到上限后必须删除已固定保留的修订版本。


- **OCR Language**（OCR 语言）：用于帮助 OCR 在导入时解析内容的 [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) 语言代码。


- **Use Content As Indexable Text**（将内容用作可索引文本）：是否将上传内容标记为可索引文本。
- **Simplify Output**（简化输出）：是否返回简化后的响应，而非包含所有字段。

更多信息，请参阅 [Method: files.insert | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/insert) API 文档。
