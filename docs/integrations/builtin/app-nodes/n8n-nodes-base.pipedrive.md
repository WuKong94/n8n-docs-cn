---
title: Pipedrive 节点文档
description: 了解如何在 n8n 中使用 Pipedrive 节点，并按照技术文档将 Pipedrive 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Pipedrive 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.pipedrive.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pipedrive
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pipedrive
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Pipedrive 节点 <a href="#pipedrive-node" id="pipedrive-node"></a>

使用 Pipedrive 节点自动处理 Pipedrive 中的工作，并将其与其他应用集成。n8n 内置支持多种 Pipedrive 功能，包括创建、更新、删除和获取活动、文件、备注、组织及销售线索。

本页列出了 Pipedrive 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Pipedrive 凭据](../credentials/pipedrive.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Activity（活动）
    * Create an activity（创建活动）
    * Delete an activity（删除活动）
    * Get data of an activity（获取活动的数据）
    * Get data of all activities（获取全部活动的数据）
    * Update an activity（更新活动）
* Deal（商机）
    * Create a deal（创建商机）
    * Delete a deal（删除商机）
    * Duplicate a deal（复制商机）
    * Get data of a deal（获取商机的数据）
    * Get data of all deals（获取全部商机的数据）
    * Search a deal（搜索商机）
    * Update a deal（更新商机）
* Deal Activity（商机活动）
    * Get all activities of a deal（获取商机的全部活动）
* Deal Product（商机产品）
    * Add a product to a deal（为商机添加产品）
    * Get all products in a deal（获取商机中的全部产品）
    * Remove a product from a deal（从商机移除产品）
    * Update a product in a deal（更新商机中的产品）
* File（文件）
    * Create a file（创建文件）
    * Delete a file（删除文件）
    * Download a file（下载文件）
    * Get data of a file（获取文件的数据）
* Lead（销售线索）
    * Create a lead（创建销售线索）
    * Delete a lead（删除销售线索）
    * Get data of a lead（获取销售线索的数据）
    * Get data of all leads（获取全部销售线索的数据）
    * Update a lead（更新销售线索）
* Note（备注）
    * Create a note（创建备注）
    * Delete a note（删除备注）
    * Get data of a note（获取备注的数据）
    * Get data of all notes（获取全部备注的数据）
    * Update a note（更新备注）
* Organization（组织）
    * Create an organization（创建组织）
    * Delete an organization（删除组织）
    * Get data of an organization（获取组织的数据）
    * Get data of all organizations（获取全部组织的数据）
    * Update an organization（更新组织）
    * Search organizations（搜索组织）
* Person（人员）
    * Create a person（创建人员）
    * Delete a person（删除人员）
    * Get data of a person（获取人员的数据）
    * Get data of all persons（获取全部人员的数据）
    * Search all persons（搜索全部人员）
    * Update a person（更新人员）
* Product（产品）
    * Get data of all products（获取全部产品的数据）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Pipedrive 集成模板](https://n8n.io/integrations/pipedrive)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
