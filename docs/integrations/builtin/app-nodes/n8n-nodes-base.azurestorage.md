---
title: Azure Storage 节点文档
description: 了解如何在 n8n 中使用 Azure Storage 节点，并按照技术文档将 Azure Storage 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Azure Storage 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.azurestorage.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurestorage
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurestorage
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Azure Storage 节点 <a href="#azure-storage-node" id="azure-storage-node"></a>

Azure Storage 节点内置支持多种功能，包括创建、获取和删除 Blob 与容器。可以使用此节点自动处理 Azure Storage 服务中的工作，或将其与工作流中的其他服务集成。

本页列出了 Azure Storage 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

该节点的身份验证信息，请参阅 [Azure Storage 凭据文档](../credentials/azurestorage.md)。
{% endhint %}


## 操作 <a href="#operations" id="operations"></a>

* **Blob**（二进制大对象）
	* **Create blob**（创建 Blob）：创建新的 Blob，或替换已有 Blob。
	* **Delete blob**（删除 Blob）：删除已有 Blob。
	* **Get blob**（获取 Blob）：获取指定 Blob 的数据。
	* **Get many blobs**（获取多个 Blob）：获取 Blob 列表。
* **Container**（容器）
	* **Create container**（创建容器）：创建新容器。
	* **Delete container**（删除容器）：删除已有容器。
	* **Get container**（获取容器）：获取指定容器的数据。
	* **Get many containers**（获取多个容器）：获取容器列表。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Azure Storage 集成模板](https://n8n.io/integrations/azure-storage)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>


该服务的更多信息，请参阅 [Microsoft 的 Azure Storage 文档](https://learn.microsoft.com/en-us/rest/api/storageservices/)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
