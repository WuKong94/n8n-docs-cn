---
title: S3 节点文档
contentType:
- integration
- reference
priority: medium
nodeTitle: S3 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.s3.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3
description: 了解如何在 n8n 中使用 S3 节点，并按照技术文档将 S3 节点集成到工作流中。
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


# S3 <a id="s3"></a>

使用 S3 节点自动处理非 AWS 的 S3 存储，并将其与其他应用集成。n8n 内置支持多种 S3 功能，包括创建、删除和获取存储桶、文件及文件夹。对于 AWS S3，请使用 [AWS S3](n8n-nodes-base.awss3.md)。

S3 节点适用于以下非 AWS 的 S3 解决方案：

* [MinIO](https://min.io/)
* [Wasabi](https://wasabi.com/)
* [DigitalOcean Spaces](https://www.digitalocean.com/products/spaces)

本页列出了 S3 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [S3 凭据](../credentials/s3.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Bucket（存储桶）
  * Create a bucket（创建存储桶）
  * Delete a bucket（删除存储桶）
  * Get all buckets（获取全部存储桶）
  * Search within a bucket（在存储桶中搜索）
*   File（文件）<br>

    * Copy a file（复制文件）
    * Delete a file（删除文件）
    * Download a file（下载文件）
    * Get all files（获取全部文件）
    * Upload a file（上传文件）

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>附加要上传的文件</strong></p><p>要附加文件进行上传，请用其他节点将文件作为数据属性传入。例如，可以使用 <a href="../core-nodes/n8n-nodes-base.readwritefile.md">Read/Write Files from Disk</a> 节点或 <a href="../core-nodes/n8n-nodes-base.httprequest/README.md">HTTP Request</a> 节点。</p></div>
* Folder（文件夹）
  * Create a folder（创建文件夹）
  * Delete a folder（删除文件夹）
  * Get all folders（获取全部文件夹）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 S3 集成模板](https://n8n.io/integrations/s3)，或[搜索所有模板](https://n8n.io/workflows/)

## 节点参考 <a href="#node-reference" id="node-reference"></a>

### 在 Wasabi 中设置文件权限 <a href="#setting-file-permissions-in-wasabi" id="setting-file-permissions-in-wasabi"></a>

向 [Wasabi](https://wasabi.com/) 上传文件时，必须通过 **ACL** 下拉菜单设置文件权限，而不是使用开关。

![通过 S3 节点使用 Wasabi 时的文件权限](../../.gitbook/assets/acl_dropdown.png)
