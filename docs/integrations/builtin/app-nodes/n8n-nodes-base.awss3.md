---
title: AWS S3 节点文档
description: 了解如何在 n8n 中使用 AWS S3 节点，并按照技术文档将 AWS S3 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: AWS S3 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.awss3.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awss3
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awss3
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# AWS S3 节点 <a href="#aws-s3-node" id="aws-s3-node"></a>

使用 AWS S3 节点自动处理 AWS S3 中的工作，并将其与其他应用集成。n8n 内置支持多种 AWS S3 功能，包括创建和删除存储桶、复制和下载文件，以及获取文件夹。

本页列出了 AWS S3 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [AWS 凭据](../credentials/aws.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Bucket（存储桶）
    * Create a bucket（创建存储桶）
    * Delete a bucket（删除存储桶）
    * Get all buckets（获取全部存储桶）
    * Search within a bucket（在存储桶中搜索）
* File（文件）
    * Copy a file（复制文件）
    * Delete a file（删除文件）
    * Download a file（下载文件）
    * Get all files（获取全部文件）
    * Upload a file（上传文件）
* Folder（文件夹）
    * Create a folder（创建文件夹）
    * Delete a folder（删除文件夹）
    * Get all folders（获取全部文件夹）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 AWS S3 集成模板](https://n8n.io/integrations/aws-s3)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

