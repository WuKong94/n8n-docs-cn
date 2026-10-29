---
title: Nextcloud 节点文档
description: 了解如何在 n8n 中使用 Nextcloud 节点，并按照技术文档将 Nextcloud 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Nextcloud 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.nextcloud.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.nextcloud
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.nextcloud
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Nextcloud 节点 <a href="#nextcloud-node" id="nextcloud-node"></a>

使用 Nextcloud 节点自动处理 Nextcloud 中的工作，并将其与其他应用集成。n8n 内置支持多种 Nextcloud 功能，包括创建、更新、删除和获取文件及文件夹，以及获取和邀请用户。

本页列出了 Nextcloud 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Nextcloud 凭据](../credentials/nextcloud.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* File（文件）
    * Copy a file（复制文件）
    * Delete a file（删除文件）
    * Download a file（下载文件）
    * Move a file（移动文件）
    * Share a file（共享文件）
    * Upload a file（上传文件）
* Folder（文件夹）
    * Copy a folder（复制文件夹）
    * Create a folder（创建文件夹）
    * Delete a folder（删除文件夹）
    * Return the contents of a given folder（返回指定文件夹的内容）
    * Move a folder（移动文件夹）
    * Share a folder（共享文件夹）
* User（用户）
    * 邀请用户加入 Nextcloud 组织
    * Delete a user.（删除用户）
    * Retrieve information about a single user.（获取单个用户的信息）
    * Retrieve a list of users.（获取用户列表）
    * Edit attributes related to a user.（编辑用户的属性）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Nextcloud 集成模板](https://n8n.io/integrations/nextcloud)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
