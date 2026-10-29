---
title: Google Business Profile 节点文档
description: 了解如何在 n8n 中使用 Google Business Profile 节点，并按照技术文档将 Google Business Profile
  节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Google Business Profile 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googlebusinessprofile.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebusinessprofile
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebusinessprofile
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Business Profile 节点 <a href="#google-business-profile-node" id="google-business-profile-node"></a>

使用 Google Business Profile 节点自动处理 Google Business Profile 中的工作，并将其与其他应用集成。n8n 内置支持多种 Google Business Profile 功能，包括创建、更新和删除帖子及评价。

本页列出了 Google Business Profile 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Google 凭据文档](../credentials/google/README.md)。
{% endhint %}


## 操作 <a href="#operations" id="operations"></a>

* Post（帖子）
	* Create（创建）
	* Delete（删除）
	* Get（获取）
	* Get Many（获取多条）
	* Update（更新）
* Review（评价）
	* Delete Reply（删除回复）
	* Get（获取）
	* Get Many（获取多条）
	* Reply（回复）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Google Business Profile 集成模板](https://n8n.io/integrations/google-business-profile)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Google Business Profile 提供触发器节点。更多信息请参阅 [Google Business Profile Trigger 节点文档](../trigger-nodes/n8n-nodes-base.googlebusinessprofiletrigger.md)。

有关该服务的更多信息，请参阅 [Google Business Profile 文档](https://developers.google.com/my-business/reference/rest)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
