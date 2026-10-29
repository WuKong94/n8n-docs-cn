---
title: Google Drive 共享云端硬盘操作
contentType:
- integration
- reference
priority: high
nodeTitle: Google Drive 共享云端硬盘操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations
description: 了解 n8n 工作流自动化平台中 Google Drive 节点的共享云端硬盘操作，包括操作及配置详情，以及示例和凭据信息链接。
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


# 共享云端硬盘操作 <a id="shared-drive-operations"></a>

使用这些操作在 Google Drive 中创建、删除、获取和更新共享云端硬盘。有关 Google Drive 节点本身的更多信息，请参阅 [Google Drive](./README.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 创建共享云端硬盘 <a href="#create-a-shared-drive" id="create-a-shared-drive"></a>

此操作用于创建新共享云端硬盘。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Shared Drive**（共享云端硬盘）。
* **Operation**（操作）：选择 **Create**（创建）。
* **Name**（名称）：新共享云端硬盘使用的名称。

### 选项 <a href="#options" id="options"></a>

* **Capabilities**（能力）：原文在此列出新共享云端硬盘的能力选项，详情请参阅 [REST Resources: drives | Google Drive](https://developers.google.com/drive/api/reference/rest/v3/drives)。译注：Google Drive API 将 capabilities 定义为仅输出字段，表示当前用户已有的能力，不可通过设置此对象授予权限：
  * **Can Add Children**（可添加子项）：当前用户是否可以向此共享云端硬盘的文件夹添加子项。
  * **Can Change Copy Requires Writer Permission Restriction**（可更改复制需写入者权限限制）：当前用户是否可以更改此共享云端硬盘的 `copyRequiresWriterPermission` 限制。
  * **Can Change Domain Users Only Restriction**（可更改仅网域用户限制）：当前用户是否可以更改此共享云端硬盘的 `domainUsersOnly` 限制。
  * **Can Change Drive Background**（可更改云端硬盘背景）：当前用户是否可以更改此共享云端硬盘的背景。
  * **Can Change Drive Members Only Restriction**（可更改仅成员限制）：当前用户是否可以更改此共享云端硬盘的 `driveMembersOnly` 限制。
  * **Can Comment**（可评论）：当前用户是否可以评论此共享云端硬盘中的文件。
  * **Can Copy**（可复制）：当前用户是否可以复制此共享云端硬盘中的文件。
  * **Can Delete Children**（可删除子项）：当前用户是否可以删除此共享云端硬盘文件夹中的子项。
  * **Can Delete Drive**（可删除云端硬盘）：当前用户是否可以删除此共享云端硬盘。如果其中仍有未移至垃圾箱的项目，操作仍可能失败。
  * **Can Download**（可下载）：当前用户是否可以下载此共享云端硬盘中的文件。
  * **Can Edit**（可编辑）：当前用户是否可以编辑此共享云端硬盘中的文件。
  * **Can List Children**（可列出子项）：当前用户是否可以列出此共享云端硬盘文件夹中的子项。
  * **Can Manage Members**（可管理成员）：当前用户是否可以添加、移除或更改此共享云端硬盘成员的角色。
  * **Can Read Revisions**（可读取修订版本）：当前用户是否可以读取此共享云端硬盘内文件的修订版本资源。
  * **Can Rename Drive**（可重命名云端硬盘）：当前用户是否可以重命名此共享云端硬盘。
  * **Can Share**（可共享）：当前用户是否可以共享此共享云端硬盘内的文件或文件夹。
  * **Can Trash Children**（可将子项移至垃圾箱）：当前用户是否可以将此共享云端硬盘文件夹中的子项移至垃圾箱。
* **Color RGB**（RGB 颜色）：此共享云端硬盘的颜色，使用 RGB 十六进制字符串表示。
* **Hidden**（隐藏）：是否在默认视图中隐藏此共享云端硬盘。
* **Restrictions**（限制）：要添加到此共享云端硬盘的限制，详情请参阅 [REST Resources: drives | Google Drive](https://developers.google.com/drive/api/reference/rest/v3/drives)：
  * **Admin Managed Restrictions**（由管理员管理限制）：是否要求具备此共享云端硬盘的管理权限才能修改限制。
  * **Copy Requires Writer Permission**（复制需要写入者权限）：是否禁止读取者和评论者复制、打印或下载此共享云端硬盘内的文件。
  * **Domain Users Only**（仅网域用户）：是否仅允许此共享云端硬盘所属网域的用户访问该云端硬盘及其中的内容。
  * **Drive Members Only**（仅云端硬盘成员）：是否仅允许此共享云端硬盘的成员访问其中的内容。

更多信息，请参阅 [Method: drives.insert | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/drives/insert) API 文档。

## 删除共享云端硬盘 <a href="#delete-a-shared-drive" id="delete-a-shared-drive"></a>

此操作用于删除共享云端硬盘。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Shared Drive**（共享云端硬盘）。
* **Operation**（操作）：选择 **Delete**（删除）。
* **Shared Drive**（共享云端硬盘）：选择要删除的共享云端硬盘。
  * 选择 **From list**（从列表）可在下拉列表中按标题选择，选择 **By URL**（按 URL）可输入云端硬盘 URL，选择 **By ID**（按 ID）可输入 `driveId`。
  * 可在共享 Google Drive 的 URL 中找到 `driveId`：`https://drive.google.com/drive/u/0/folders/driveID`。

更多信息，请参阅 [Method: drives.delete | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/drives/delete) API 文档。

## 获取共享云端硬盘 <a href="#get-a-shared-drive" id="get-a-shared-drive"></a>

此操作用于获取共享云端硬盘。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Shared Drive**（共享云端硬盘）。
* **Operation**（操作）：选择 **Get**（获取）。
* **Shared Drive**（共享云端硬盘）：选择要获取的共享云端硬盘。
  * 选择 **From list**（从列表）可在下拉列表中按标题选择，选择 **By URL**（按 URL）可输入云端硬盘 URL，选择 **By ID**（按 ID）可输入 `driveId`。
  * 可在共享 Google Drive 的 URL 中找到 `driveId`：`https://drive.google.com/drive/u/0/folders/driveID`。

### 选项 <a href="#options" id="options"></a>

* **Use Domain Admin Access**（使用网域管理员权限）：是否以网域管理员身份发送请求。开启后，如果请求者是该共享云端硬盘所属网域的管理员，则授予其访问权限。

更多信息，请参阅 [Method: drives.get | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/drives/get) API 文档。

## 获取多个共享云端硬盘 <a href="#get-many-shared-drives" id="get-many-shared-drives"></a>

此操作用于获取多个共享云端硬盘。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Shared Drive**（共享云端硬盘）。
* **Operation**（操作）：选择 **Get Many**（获取多项）。
* **Return All**（返回全部）：选择返回所有结果，或仅返回指定数量以内的结果。
* **Limit**（数量限制）：关闭 **Return All**（返回全部）时，返回的最大数据项数量。
* **Shared Drive**（共享云端硬盘）：选择要获取的共享云端硬盘。
  * 选择 **From list**（从列表）可在下拉列表中按标题选择，选择 **By URL**（按 URL）可输入云端硬盘 URL，选择 **By ID**（按 ID）可输入 `driveId`。
  * 可在共享 Google Drive 的 URL 中找到 `driveId`：`https://drive.google.com/drive/u/0/folders/driveID`。

### 选项 <a href="#options" id="options"></a>

* **Query**（查询）：用于搜索共享云端硬盘的查询字符串。更多信息，请参阅 [Search for shared drives | Google Drive](https://developers.google.com/drive/api/guides/search-shareddrives)（搜索共享云端硬盘）。
* **Use Domain Admin Access**（使用网域管理员权限）：是否以网域管理员身份发送请求。开启后，如果请求者是该共享云端硬盘所属网域的管理员，则授予其访问权限。

更多信息，原文引用了 [Method: drives.get | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/drives/get) API 文档。译注：该链接是单项获取接口；Google 的批量列表方法为 drives.list。

## 更新共享云端硬盘 <a href="#update-a-shared-drive" id="update-a-shared-drive"></a>

此操作用于更新共享云端硬盘。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [Google Drive 凭据](../../credentials/google/README.md)。
* **Resource**（资源）：选择 **Shared Drive**（共享云端硬盘）。
* **Operation**（操作）：选择 **Update**（更新）。
* **Shared Drive**（共享云端硬盘）：选择要更新的共享云端硬盘。
  * 选择 **From list**（从列表）可在下拉列表中选择云端硬盘，选择 **By URL**（按 URL）可输入其 URL，选择 **By ID**（按 ID）可输入 `driveId`。
  * 可在共享 Google Drive 的 URL 中找到 `driveId`：`https://drive.google.com/drive/u/0/folders/driveID`。

### 更新字段 <a href="#update-fields" id="update-fields"></a>

* **Color RGB**（RGB 颜色）：此共享云端硬盘的颜色，使用 RGB 十六进制字符串表示。
* **Name**（名称）：更新后的共享云端硬盘名称。
* **Restrictions**（限制）：此共享云端硬盘的限制，详情请参阅 [REST Resources: drives | Google Drive](https://developers.google.com/drive/api/reference/rest/v3/drives)：
  * **Admin Managed Restrictions**（由管理员管理限制）：是否要求具备此共享云端硬盘的管理权限才能修改限制。
  * **Copy Requires Writer Permission**（复制需要写入者权限）：是否禁止读取者和评论者复制、打印或下载此共享云端硬盘内的文件。
  * **Domain Users Only**（仅网域用户）：是否仅允许此共享云端硬盘所属网域的用户访问该云端硬盘及其中的内容。
  * **Drive Members Only**（仅云端硬盘成员）：是否仅允许此共享云端硬盘的成员访问其中的内容。

更多信息，请参阅 [Method: drives.update | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/drives/update) API 文档。
