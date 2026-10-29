---
title: Elastic Security 节点文档
description: 了解如何在 n8n 中使用 Elastic Security 节点，并按照技术文档将 Elastic Security 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Elastic Security 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.elasticsecurity.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.elasticsecurity
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.elasticsecurity
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Elastic Security 节点 <a href="#elastic-security-node" id="elastic-security-node"></a>

使用 Elastic Security 节点自动处理 Elastic Security 中的工作，并将其与其他应用集成。n8n 内置支持多种 Elastic Security 功能，包括创建、更新、删除和获取案件。

本页列出了 Elastic Security 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Elastic Security 凭据](../credentials/elasticsecurity.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Case（案件）
    * Create a case（创建案件）
    * Delete a case（删除案件）
    * Get a case（获取案件）
    * Retrieve all cases（获取全部案件）
    * Retrieve a summary of all case activity（获取全部案件活动的摘要）
    * Update a case（更新案件）
* Case Comment（案件评论）
    * Add a comment to a case（为案件添加评论）
    * Get a case comment（获取案件评论）
    * Retrieve all case comments（获取全部案件评论）
    * Remove a comment from a case（从案件移除评论）
    * Update a comment in a case（更新案件中的评论）
* Case Tag（案件标签）
    * Add a tag to a case（为案件添加标签）
    * Remove a tag from a case（从案件移除标签）
* Connector（连接器）
    * Create a connector（创建连接器）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Elastic Security 集成模板](https://n8n.io/integrations/elastic-security)，或[搜索所有模板](https://n8n.io/workflows/)
