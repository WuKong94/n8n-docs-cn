---
title: HighLevel 节点文档
description: 了解如何在 n8n 中使用 HighLevel 节点，并按照技术文档将 HighLevel 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: HighLevel 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.highlevel.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.highlevel
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.highlevel
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# HighLevel 节点 <a href="#highlevel-node" id="highlevel-node"></a>

使用 HighLevel 节点自动处理 HighLevel 中的工作，并将其与其他应用集成。n8n 内置支持多种 HighLevel 功能，包括创建、更新、删除和获取联系人、销售机会与任务，以及预约和获取日历中的空闲时段。

本页列出了 HighLevel 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [HighLevel 凭据](../credentials/highlevel.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Contact（联系人）
	* Create or update（创建或更新）
	* Delete（删除）
	* Get（获取）
	* Get many（获取多条）
	* Update（更新）
* Opportunity（销售机会）
	* Create（创建）
	* Delete（删除）
	* Get（获取）
	* Get many（获取多条）
	* Update（更新）
* Task（任务）
	* Create（创建）
	* Delete（删除）
	* Get（获取）
	* Get many（获取多条）
	* Update（更新）
* Calendar（日历）
	* Book an appointment（预约）
	* Get free slots（获取空闲时段）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 HighLevel 集成模板](https://n8n.io/integrations/highlevel)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [HighLevel 的 API 文档和支持论坛](https://help.gohighlevel.com/support/solutions/articles/48001060529-highlevel-api)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
