---
title: ConvertKit 节点文档
description: 了解如何在 n8n 中使用 ConvertKit 节点，并按照技术文档将 ConvertKit 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: ConvertKit 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.convertkit.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.convertkit
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.convertkit
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# ConvertKit 节点 <a href="#convertkit-node" id="convertkit-node"></a>

使用 ConvertKit 节点自动处理 ConvertKit 中的工作，并将其与其他应用集成。n8n 内置支持多种 ConvertKit 功能，包括创建和删除自定义字段、获取标签和添加订阅者。

本页列出了 ConvertKit 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [ConvertKit 凭据](../credentials/convertkit.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Custom Field（自定义字段）
    * Create a field（创建字段）
    * Delete a field（删除字段）
    * Get all fields（获取全部字段）
    * Update a field（更新字段）
* Form（表单）
    * Add a subscriber（添加订阅者）
    * Get all forms（获取全部表单）
    * List subscriptions to a form including subscriber data（列出表单订阅，包含订阅者数据）
* Sequence（邮件序列）
    * Add a subscriber（添加订阅者）
    * Get all sequences（获取全部邮件序列）
    * Get all subscriptions to a sequence including subscriber data（获取邮件序列的全部订阅，包含订阅者数据）
* Tag（标签）
    * Create a tag（创建标签）
    * Get all tags（获取全部标签）
* Tag Subscriber（带标签的订阅者）
    * Add a tag to a subscriber（为订阅者添加标签）
    * List subscriptions to a tag including subscriber data（列出标签的订阅，包含订阅者数据）
    * Delete a tag from a subscriber（从订阅者移除标签）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 ConvertKit 集成模板](https://n8n.io/integrations/convertkit)，或[搜索所有模板](https://n8n.io/workflows/)

