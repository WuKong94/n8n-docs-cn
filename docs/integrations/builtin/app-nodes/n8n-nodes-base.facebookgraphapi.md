---
title: Facebook Graph API 节点文档
description: 了解如何在 n8n 中使用 Facebook Graph API 节点，并按照技术文档将 Facebook Graph API 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Facebook Graph API 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Facebook Graph API 节点 <a href="#facebook-graph-api-node" id="facebook-graph-api-node"></a>

使用 Facebook Graph API 节点自动处理 Facebook Graph API 中的工作，并将其与其他应用集成。n8n 内置支持多种 Facebook Graph API 功能，包括使用 GET、POST、DELETE 查询，以及配置主机 URL、请求方法等参数。

本页列出了 Facebook Graph API 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Facebook Graph API 凭据](../credentials/facebookgraph.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* **Default**（默认）
    * GET（获取）
    * POST（帖子）
    * DELETE（删除）
* **Video Uploads**（视频上传）
    * GET（获取）
    * POST（帖子）
    * DELETE（删除）


### 参数 <a href="#parameters" id="parameters"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

* **Host URL**（主机 URL）：请求的主机 URL，可选：
    * **Default**（默认）：请求发送至 `graph.facebook.com` 主机 URL，用于大多数请求。
    * **Video**（视频）：请求发送至 `graph-video.facebook.com` 主机 URL，仅用于视频上传请求。
* **HTTP Request Method**（HTTP 请求方法）：用于此请求的方法，可选：
    * **GET**（获取）
    * **POST**（提交）
    * **DELETE**（删除）
* **Graph API Version**（Graph API 版本）：用于此请求的 [Facebook Graph API](https://developers.facebook.com/docs/graph-api/changelog) 版本。
* **Node**（节点）：要操作的节点，例如 `/<page-id>/feed`。更多信息请参阅 [Facebook 官方开发者文档](https://developers.facebook.com/docs/graph-api/using-graph-api)。
* **Edge**（边）：要操作的节点的边。边表示关联到该节点的对象集合。
* **Ignore SSL Issues**（忽略 SSL 问题）：开启后，即使无法验证 SSL 证书，仍会下载响应。
* **Send Binary File**（发送二进制文件）：适用于 `POST` 操作。启用后，以二进制数据作为请求体发送，需要设置以下字段：
    * **Input Binary Field**（输入二进制字段）：包含待上传文件数据的二进制属性名称。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Facebook Graph API 集成模板](https://n8n.io/integrations/facebook-graph-api)，或[搜索所有模板](https://n8n.io/workflows/)
