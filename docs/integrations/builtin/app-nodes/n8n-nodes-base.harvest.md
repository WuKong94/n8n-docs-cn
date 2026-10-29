---
title: Harvest 节点文档
description: 了解如何在 n8n 中使用 Harvest 节点，并按照技术文档将 Harvest 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Harvest 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.harvest.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.harvest
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.harvest
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Harvest 节点 <a href="#harvest-node" id="harvest-node"></a>

使用 Harvest 节点自动处理 Harvest 中的工作，并将其与其他应用集成。n8n 内置支持多种 Harvest 功能，包括创建、更新、删除和获取客户、联系人、发票、任务、费用、用户及项目。

本页列出了 Harvest 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Harvest 凭据](../credentials/harvest.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Client（客户）
    * Create a client（创建客户）
    * Delete a client（删除客户）
    * Get data of a client（获取客户数据）
    * Get data of all clients（获取所有客户数据）
    * Update a client（更新客户）
* Company（公司）
    * Retrieves the company for the currently authenticated user（获取当前已通过身份验证的用户所属公司）
* Contact（联系人）
    * Create a contact（创建联系人）
    * Delete a contact（删除联系人）
    * Get data of a contact（获取联系人数据）
    * Get data of all contacts（获取所有联系人数据）
    * Update a contact（更新联系人）
* Estimate（估价单）
    * Create an estimate（创建估价单）
    * Delete an estimate（删除估价单）
    * Get data of an estimate（获取估价单数据）
    * Get data of all estimates（获取所有估价单数据）
    * Update an estimate（更新估价单）
* Expense（费用）
    * Get data of an expense（获取费用数据）
    * Get data of all expenses（获取所有费用数据）
    * Create an expense（创建费用）
    * Update an expense（更新费用）
    * Delete an expense（删除费用）
* Invoice（发票）
    * Get data of an invoice（获取发票数据）
    * Get data of all invoices（获取所有发票数据）
    * Create an invoice（创建发票）
    * Update an invoice（更新发票）
    * Delete an invoice（删除发票）
* Project（项目）
    * Create a project（创建项目）
    * Delete a project（删除项目）
    * Get data of a project（获取项目数据）
    * Get data of all projects（获取所有项目数据）
    * Update a project（更新项目）
* Task（任务）
    * Create a task（创建任务）
    * Delete a task（删除任务）
    * Get data of a task（获取任务数据）
    * Get data of all tasks（获取所有任务数据）
    * Update a task（更新任务）
* Time Entries（工时记录）
    * Create a time entry using duration（按时长创建工时记录）
    * Create a time entry using start and end time（按开始和结束时间创建工时记录）
    * Delete a time entry（删除工时条目）
    * Delete a time entry's external reference.（删除工时记录的外部引用）
    * Get data of a time entry（获取工时记录数据）
    * Get data of all time entries（获取所有工时记录数据）
    * Restart a time entry（重新开始工时记录）
    * Stop a time entry（停止工时记录）
    * Update a time entry（更新工时条目）
* User（用户）
    * Create a user（创建用户）
    * Delete a user（删除用户）
    * Get data of a user（获取用户数据）
    * Get data of all users（获取所有用户数据）
    * Get data of authenticated user（获取已通过身份验证的用户数据）
    * Update a user（更新用户）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Harvest 集成模板](https://n8n.io/integrations/harvest)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
