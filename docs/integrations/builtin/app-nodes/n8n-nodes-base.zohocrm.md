---
title: Zoho CRM 节点文档
description: 了解如何在 n8n 中使用 Zoho CRM 节点，并按照技术文档将 Zoho CRM 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Zoho CRM 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.zohocrm.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zohocrm
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zohocrm
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Zoho CRM 节点 <a href="#zoho-crm-node" id="zoho-crm-node"></a>

使用 Zoho CRM 节点自动处理 Zoho CRM 中的工作，并将其与其他应用集成。n8n 内置支持多种 Zoho CRM 功能，包括创建和删除账户、联系人及商机。

本页列出了 Zoho CRM 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Zoho CRM 凭据](../credentials/zoho.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Account（账户）
    * Create an account（创建账户）
    * Create a new record, or update the current one if it already exists (upsert)（创建新记录；如果已存在则更新现有记录（upsert））
    * Delete an account（删除账户）
    * Get an account（获取账户）
    * Get all accounts（获取全部账户）
    * Update an account（更新账户）
* Contact（联系人）
    * Create a contact（创建联系人）
    * Create a new record, or update the current one if it already exists (upsert)（创建新记录；如果已存在则更新现有记录（upsert））
    * Delete a contact（删除联系人）
    * Get a contact（获取联系人）
    * Get all contacts（获取全部联系人）
    * Update a contact（更新联系人）
* Deal（商机）
    * Create a deal（创建商机）
    * Create a new record, or update the current one if it already exists (upsert)（创建新记录；如果已存在则更新现有记录（upsert））
    * Delete a contact（删除联系人）
    * Get a contact（获取联系人）
    * Get all contacts（获取全部联系人）
    * Update a contact（更新联系人）
* Invoice（发票）
    * Create an invoice（创建发票）
    * Create a new record, or update the current one if it already exists (upsert)（创建新记录；如果已存在则更新现有记录（upsert））
    * Delete an invoice（删除发票）
    * Get an invoice（获取发票）
    * Get all invoices（获取全部发票）
    * Update an invoice（更新发票）
* Lead（销售线索）
    * Create a lead（创建销售线索）
    * Create a new record, or update the current one if it already exists (upsert)（创建新记录；如果已存在则更新现有记录（upsert））
    * Delete a lead（删除销售线索）
    * Get a lead（获取销售线索）
    * Get all leads（获取全部销售线索）
    * Get lead fields（获取销售线索字段）
    * Update a lead（更新销售线索）
* Product（产品）
    * Create a product（创建产品）
    * Create a new record, or update the current one if it already exists (upsert)（创建新记录；如果已存在则更新现有记录（upsert））
    * Delete a product（删除产品）
    * Get a product（获取产品）
    * Get all products（获取全部产品）
    * Update a product（更新产品）
* Purchase Order（采购订单）
    * Create a purchase order（创建采购订单）
    * Create a new record, or update the current one if it already exists (upsert)（创建新记录；如果已存在则更新现有记录（upsert））
    * Delete a purchase order（删除采购订单）
    * Get a purchase order（获取采购订单）
    * Get all purchase orders（获取所有采购订单）
    * Update a purchase order（更新采购订单）
* Quote（报价单）
    * Create a quote（创建报价单）
    * Create a new record, or update the current one if it already exists (upsert)（创建新记录；如果已存在则更新现有记录（upsert））
    * Delete a quote（删除报价单）
    * Get a quote（获取报价单）
    * Get all quotes（获取所有报价单）
    * Update a quote（更新报价单）
* Sales Order（销售订单）
    * Create a sales order（创建销售订单）
    * Create a new record, or update the current one if it already exists (upsert)（创建新记录；如果已存在则更新现有记录（upsert））
    * Delete a sales order（删除销售订单）
    * Get a sales order（获取销售订单）
    * Get all sales orders（获取全部销售订单）
    * Update a sales order（更新销售订单）
* Vendor（供应商）
    * Create a vendor（创建供应商）
    * Create a new record, or update the current one if it already exists (upsert)（创建新记录；如果已存在则更新现有记录（upsert））
    * Delete a vendor（删除供应商）
    * Get a vendor（获取供应商）
    * Get all vendors（获取所有供应商）
    * Update a vendor（更新供应商）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Zoho CRM 集成模板](https://n8n.io/integrations/zoho-crm)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
