---
title: Mailchimp 节点文档
description: 了解如何在 n8n 中使用 Mailchimp 节点，并按照技术文档将 Mailchimp 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Mailchimp 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.mailchimp.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mailchimp
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mailchimp
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Mailchimp 节点 <a href="#mailchimp-node" id="mailchimp-node"></a>

使用 Mailchimp 节点自动处理 Mailchimp 中的工作，并将其与其他应用集成。n8n 内置支持多种 Mailchimp 功能，包括创建、更新和删除营销活动，以及获取列表分组。

本页列出了 Mailchimp 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Mailchimp 凭据](../credentials/mailchimp.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Campaign（营销活动）
    * Delete a campaign（删除营销活动）
    * Get a campaign（获取营销活动）
    * Get all the campaigns（获取全部营销活动）
    * Replicate a campaign（复制营销活动）
    * Creates a Resend to Non-Openers version of this campaign（创建向未打开邮件者重发的活动版本）
    * Send a campaign（发送营销活动）
* List Group（列出群组）
    * Get all groups（获取全部群组）
* Member（成员）
    * Create a new member on list（在列表中创建成员）
    * Delete a member on list（删除列表中的成员）
    * Get a member on list（获取列表中的成员）
    * Get all members on list（获取列表中的全部成员）
    * Update a new member on list（更新列表中的新成员）
* Member Tag（成员标签）
    * Add tags from a list member（为列表成员添加标签）
    * Remove tags from a list member（从列表成员移除标签）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Mailchimp 集成模板](https://n8n.io/integrations/mailchimp)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
