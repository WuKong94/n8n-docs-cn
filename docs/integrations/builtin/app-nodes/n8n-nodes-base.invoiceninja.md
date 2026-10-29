---
title: Invoice Ninja 节点文档
description: 了解如何在 n8n 中使用 Invoice Ninja 节点，并按照技术文档将 Invoice Ninja 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Invoice Ninja 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.invoiceninja.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.invoiceninja
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.invoiceninja
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Invoice Ninja 节点 <a href="#invoice-ninja-node" id="invoice-ninja-node"></a>

使用 Invoice Ninja 节点自动处理 Invoice Ninja 中的工作，并将其与其他应用集成。n8n 内置支持多种 Invoice Ninja 功能，包括创建、更新、删除和获取客户、费用、发票、付款和报价单。

本页列出了 Invoice Ninja 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Invoice Ninja 凭据](../credentials/invoiceninja.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Client（客户）
    * Create a new client（创建新客户）
    * Delete a client（删除客户）
    * Get data of a client（获取客户数据）
    * Get data of all clients（获取所有客户数据）
* Expense（费用）
    * Create a new expense（创建新费用）
    * Delete an expense（删除费用）
    * Get data of an expense（获取费用数据）
    * Get data of all expenses（获取所有费用数据）
* Invoice（发票）
    * Create a new invoice（创建新发票）
    * Delete a invoice（删除发票）
    * Email an invoice（通过邮件发送发票）
    * Get data of a invoice（获取发票数据）
    * Get data of all invoices（获取所有发票数据）
* Payment（付款）
    * Create a new payment（创建新付款）
    * Delete a payment（删除付款）
    * Get data of a payment（获取付款数据）
    * Get data of all payments（获取所有付款数据）
* Quote（报价单）
    * Create a new quote（创建新报价单）
    * Delete a quote（删除报价单）
    * Email an quote（通过邮件发送报价单）
    * Get data of a quote（获取报价单数据）
    * Get data of all quotes（获取所有报价单数据）
* Task（任务）
    * Create a new task（创建新任务）
    * Delete a task（删除任务）
    * Get data of a task（获取任务数据）
    * Get data of all tasks（获取所有任务数据）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Invoice Ninja 集成模板](https://n8n.io/integrations/invoice-ninja)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
