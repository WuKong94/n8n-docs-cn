---
title: Salesforce 节点文档
description: 了解如何在 n8n 中使用 Salesforce 节点，并按照技术文档将 Salesforce 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Salesforce 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.salesforce.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.salesforce
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.salesforce
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Salesforce 节点 <a href="#salesforce-node" id="salesforce-node"></a>

使用 Salesforce 节点自动处理 Salesforce 中的工作，并将其与其他应用集成。n8n 内置支持多种 Salesforce 功能，包括创建、更新、删除和获取账户、附件、个案及销售线索，以及上传文档。

本页列出了 Salesforce 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Salesforce 凭据](../credentials/salesforce.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Account（账户）
    * Add note to an account（向账户添加备注）
    * Create an account（创建账户）
    * Create a new account, or update the current one if it already exists (upsert)（创建新账户；如果已存在，则更新当前账户，即 upsert）
    * Get an account（获取账户）
    * Get all accounts（获取全部账户）
    * Returns an overview of account's metadata.（返回账户元数据概览）
    * Delete an account（删除账户）
    * Update an account（更新账户）
* Attachment（附件）
    * Create a attachment（创建附件）
    * Delete a attachment（删除附件）
    * Get a attachment（获取附件）
    * Get all attachments（获取所有附件）
    * Returns an overview of attachment's metadata.（返回附件元数据概览）
    * Update a attachment（更新附件）
* Case（个案）
    * Add a comment to a case（向个案添加评论）
    * Create a case（创建个案）
    * Get a case（获取个案）
    * Get all cases（获取所有个案）
    * Returns an overview of case's metadata（返回个案元数据概览）
    * Delete a case（删除个案）
    * Update a case（更新个案）
* Contact（联系人）
    * Add lead to a campaign（向营销活动添加销售线索）
    * Add note to a contact（向联系人添加备注）
    * Create a contact（创建联系人）
    * Create a new contact, or update the current one if it already exists (upsert)（创建新联系人；如果已存在，则更新当前联系人，即 upsert）
    * Delete a contact（删除联系人）
    * Get a contact（获取联系人）
    * Returns an overview of contact's metadata（返回联系人元数据概览）
    * Get all contacts（获取全部联系人）
    * Update a contact（更新联系人）
* Custom Object（自定义对象）
    * Create a custom object record（创建自定义对象记录）
    * Create a new record, or update the current one if it already exists (upsert)（创建新记录；如果已存在则更新现有记录（upsert））
    * Get a custom object record（获取自定义对象记录）
    * Get all custom object records（获取所有自定义对象记录）
    * Delete a custom object record（删除自定义对象记录）
    * Update a custom object record（更新自定义对象记录）
* Document（文档）
    * Upload a document（上传文档）
* Flow（流程）
    * Get all flows（获取所有流程）
    * Invoke a flow（调用流程）
* Lead（销售线索）
    * Add lead to a campaign（向营销活动添加销售线索）
    * Add note to a lead（向销售线索添加备注）
    * Create a lead（创建销售线索）
    * Create a new lead, or update the current one if it already exists (upsert)（创建新销售线索；如果已存在，则更新当前销售线索，即 upsert）
    * Delete a lead（删除销售线索）
    * Get a lead（获取销售线索）
    * Get all leads（获取全部销售线索）
    * Returns an overview of Lead's metadata（返回销售线索元数据概览）
    * Update a lead（更新销售线索）
* Opportunity（销售机会）
    * Add note to an opportunity（向销售机会添加备注）
    * Create an opportunity（创建销售机会）
    * Create a new opportunity, or update the current one if it already exists (upsert)（创建新销售机会；如果已存在，则更新当前销售机会，即 upsert）
    * Delete an opportunity（删除销售机会）
    * Get an opportunity（获取销售机会）
    * Get all opportunities（获取全部销售机会）
    * Returns an overview of opportunity's metadata（返回销售机会元数据概览）
    * Update an opportunity（更新销售机会）
* Search（搜索）
    * Execute a SOQL query that returns all the results in a single response（执行 SOQL 查询，在单次响应中返回全部结果）
* Task（任务）
    * Create a task（创建任务）
    * Delete a task（删除任务）
    * Get a task（获取任务）
    * Get all tasks（获取全部任务）
    * Returns an overview of task's metadata（返回任务元数据概览）
    * Update a task（更新任务）
* User（用户）
    * Get a user（获取用户）
    * Get all users（获取全部用户）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Salesforce 集成模板](https://n8n.io/integrations/salesforce)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

## 使用 Salesforce 自定义字段 <a href="#working-with-salesforce-custom-fields" id="working-with-salesforce-custom-fields"></a>

向请求添加自定义字段的步骤如下：

1. 选择 **Additional Fields**（附加字段）> **Add Field**（添加字段）。
2. 在下拉菜单中选择 **Custom Fields**（自定义字段）。

随后即可查找并添加自定义字段。
