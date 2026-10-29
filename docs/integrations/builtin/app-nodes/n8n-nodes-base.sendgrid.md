---
title: SendGrid 节点文档
description: 了解如何在 n8n 中使用 SendGrid 节点，并按照技术文档将 SendGrid 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: SendGrid 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.sendgrid.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sendgrid
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sendgrid
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# SendGrid 节点 <a href="#sendgrid-node" id="sendgrid-node"></a>

使用 SendGrid 节点自动处理 SendGrid 中的工作，并将其与其他应用集成。n8n 内置支持多种 SendGrid 功能，包括创建、更新、删除和获取联系人及列表，以及发送电子邮件。

本页列出了 SendGrid 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [SendGrid 凭据](../credentials/sendgrid.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Contact（联系人）
    * Create/update a contact（创建或更新联系人）
    * Delete a contact（删除联系人）
    * Get a contact by ID（按 ID 获取联系人）
    * Get all contacts（获取全部联系人）
* List（列出）
    * Create a list（创建列表）
    * Delete a list（删除列表）
    * Get a list（获取列表）
    * Get all lists（获取全部列表）
    * Update a list（更新列表）
* Mail（邮件）
    * Send an email.（发送电子邮件）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 SendGrid 集成模板](https://n8n.io/integrations/sendgrid)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
