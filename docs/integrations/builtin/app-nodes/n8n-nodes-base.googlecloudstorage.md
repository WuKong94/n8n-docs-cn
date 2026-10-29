---
title: Google Cloud Storage 节点文档
description: 了解如何在 n8n 中使用 Google Cloud Storage 节点，并按照技术文档将 Google Cloud Storage 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Google Cloud Storage 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Cloud Storage 节点 <a href="#google-cloud-storage-node" id="google-cloud-storage-node"></a>

使用 Google Cloud Storage 节点自动处理 Google Cloud Storage 中的工作，并将其与其他应用集成。n8n 内置支持多种 Google Cloud Storage 功能，包括创建、更新、删除和获取存储桶及对象。

本页列出了 Google Cloud Storage 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Google Cloud Storage 凭据](../credentials/google/README.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Bucket（存储桶）
	* Create（创建）
	* Delete（删除）
	* Get（获取）
	* Get Many（获取多条）
	* Update（更新）
* Object（对象）
	* Create（创建）
	* Delete（删除）
	* Get（获取）
	* Get Many（获取多条）
	* Update（更新）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Google Cloud Storage 集成模板](https://n8n.io/integrations/google-cloud-storage)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该节点所集成 API 的详细信息，请参阅 Google 的 [Cloud Storage API 文档](https://cloud.google.com/storage/docs/apis)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
