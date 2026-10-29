---
title: MISP 节点文档
description: 了解如何在 n8n 中使用 MISP 节点，并按照技术文档将 MISP 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: MISP 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.misp.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.misp
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.misp
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MISP 节点 <a href="#misp-node" id="misp-node"></a>

使用 MISP 节点自动处理 MISP 中的工作，并将其与其他应用集成。n8n 内置支持多种 MISP 功能，包括创建、更新、删除和获取事件、订阅源及组织。

本页列出了 MISP 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [MISP 凭据](../credentials/misp.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Attribute（属性）
    * Create（创建）
    * Delete（删除）
    * Get（获取）
    * Get All（获取全部）
	* Search（搜索）
    * Update（更新）
* Event（事件）
    * Create（创建）
    * Delete（删除）
    * Get（获取）
    * Get All（获取全部）
    * Publish（发布）
	* Search（搜索）
    * Unpublish（取消发布）
    * Update（更新）
* Event Tag（事件标签）
    * Add（添加）
    * Remove（移除）
* Feed（订阅源）
    * Create（创建）
    * Disable（禁用）
    * Enable（启用）
    * Get（获取）
    * Get All（获取全部）
    * Update（更新）
* Galaxy（Galaxy 分类体系）
    * Delete（删除）
    * Get（获取）
    * Get All（获取全部）
* Noticelist（通知列表）
    * Get（获取）
    * Get All（获取全部）
* Object（对象）
	* Search（搜索）
* Organisation（组织）
    * Create（创建）
    * Delete（删除）
    * Get（获取）
    * Get All（获取全部）
    * Update（更新）
* Tag（标签）
    * Create（创建）
    * Delete（删除）
    * Get All（获取全部）
    * Update（更新）
* User（用户）
    * Create（创建）
    * Delete（删除）
    * Get（获取）
    * Get All（获取全部）
    * Update（更新）
* Warninglist（警告列表）
    * Get（获取）
    * Get All（获取全部）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 MISP 集成模板](https://n8n.io/integrations/misp)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
