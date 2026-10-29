---
title: Lemlist 节点文档
description: 了解如何在 n8n 中使用 Lemlist 节点，并按照技术文档将 Lemlist 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Lemlist 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.lemlist.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lemlist
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lemlist
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Lemlist 节点 <a href="#lemlist-node" id="lemlist-node"></a>

使用 Lemlist 节点自动处理 Lemlist 中的工作，并将其与其他应用集成。n8n 内置支持多种 Lemlist 功能，包括获取活动、团队和营销活动，以及创建、更新和删除销售线索。

本页列出了 Lemlist 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Lemlist 凭据](../credentials/lemlist.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>



* Activity（活动）
    * Get Many（获取多条）：获取多条活动记录。
* Campaign（营销活动）
    * Get Many（获取多条）：获取多个营销活动。
    * Get Stats（获取统计数据）：获取营销活动统计数据。
* Enrichment（信息补全）
    * Get（获取）：获取之前已完成的信息补全结果。
    * Enrich Lead（补全销售线索）：通过电子邮箱或 LinkedIn URL 补全销售线索信息。
    * Enrich Person（补全人员信息）：通过电子邮箱或 LinkedIn URL 补全人员信息。
* Lead（销售线索）
    * Create（创建）：创建新销售线索。
    * Delete（删除）：删除已有销售线索。
    * Get（获取）：获取已有销售线索。
    * Unsubscribe（退订）：为已有销售线索退订。
* Team（团队）
    * Get（获取）：获取已有团队。
    * Get Credits（获取额度）：获取已有团队的额度。
* Unsubscribe（退订）
    * Add（添加）：将电子邮箱添加到退订列表。
    * Delete（删除）：从退订列表中删除电子邮箱。
    * Get Many（获取多条）：获取多个已退订的电子邮箱。



## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Lemlist 集成模板](https://n8n.io/integrations/lemlist)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
