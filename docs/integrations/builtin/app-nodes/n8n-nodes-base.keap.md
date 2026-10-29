---
title: Keap 节点文档
description: 了解如何在 n8n 中使用 Keap 节点，并按照技术文档将 Keap 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Keap 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.keap.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.keap
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.keap
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Keap 节点 <a href="#keap-node" id="keap-node"></a>

使用 Keap 节点自动处理 Keap 中的工作，并将其与其他应用集成。n8n 内置支持多种 Keap 功能，包括创建、更新、删除和获取公司、产品、电子商务订单、邮件及文件。

本页列出了 Keap 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Keap 凭据](../credentials/keap.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Company（公司）
    * Create a company（创建公司）
    * Retrieve all companies（获取全部公司）
* Contact（联系人）
    * Create/update a contact（创建或更新联系人）
    * Delete an contact（删除联系人）
    * Retrieve an contact（获取联系人）
    * Retrieve all contacts（获取全部联系人）
* Contact Note（联系人备注）
    * Create a note（创建备注）
    * Delete a note（删除备注）
    * Get a notes（获取备注）
    * Retrieve all notes（获取全部备注）
    * Update a note（更新备注）
* Contact Tag（联系人标签）
    * Add a list of tags to a contact（为联系人添加一组标签）
    * Delete a contact's tag（删除联系人的标签）
    * Retrieve all contact's tags（获取联系人的全部标签）
* Ecommerce Order（电子商务订单）
    * Create an ecommerce order（创建电子商务订单）
    * Get an ecommerce order（获取电子商务订单）
    * Delete an ecommerce order（删除电子商务订单）
    * Retrieve all ecommerce orders（获取全部电子商务订单）
* Ecommerce Product（电子商务产品）
    * Create an ecommerce product（创建电子商务产品）
    * Delete an ecommerce product（删除电子商务产品）
    * Get an ecommerce product（获取电子商务产品）
    * Retrieve all ecommerce product（获取全部电子商务产品）
* Email（电子邮件）
    * Create a record of an email sent to a contact（创建向联系人发送邮件的记录）
    * Retrieve all sent emails（获取全部已发送邮件）
    * Send Email（发送电子邮件）
* File（文件）
    * Delete a file（删除文件）
    * Retrieve all files（获取全部文件）
    * Upload a file（上传文件）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Keap 集成模板](https://n8n.io/integrations/keap)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
