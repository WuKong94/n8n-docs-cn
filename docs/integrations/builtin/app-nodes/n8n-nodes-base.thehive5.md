---
title: TheHive 5 节点文档
description: 了解如何在 n8n 中使用 TheHive 5 节点，并按照技术文档将 TheHive 5 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: TheHive 5 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.thehive5.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive5
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive5
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# TheHive 5 节点 <a href="#thehive-5-node" id="thehive-5-node"></a>

使用 TheHive 5 节点自动处理 TheHive 中的工作，并将 TheHive 与其他应用集成。n8n 内置支持多种 TheHive 功能，包括创建警报，以及统计任务日志、案件和可观测项。

本页列出了 TheHive 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**TheHive 与 TheHive 5**

n8n 为 TheHive 提供两个节点。要使用 TheHive 的版本 5 API，请使用此节点（TheHive 5）；要使用版本 3 或 4，请使用 [TheHive](n8n-nodes-base.thehive.md)。
{% endhint %}
{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [TheHive 凭据](../credentials/thehive5.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Alert（告警）
    * Create（创建）
    * Delete（删除）
    * Execute Responder（执行响应器）
    * Get（获取）
    * Merge Into Case（合并到案件）
    * Promote to Case（升级为案件）
    * Search（搜索）
    * Update（更新）
    * Update Status（更新状态）
* Case（案件）
    * Add Attachment（添加附件）
    * Create（创建）
    * Delete Attachment（删除附件）
    * Delete Case（删除案件）
    * Execute Responder（执行响应器）
    * Get（获取）
    * Get Attachment（获取附件）
    * Get Timeline（获取时间线）
    * Search（搜索）
    * Update（更新）
* Comment（评论）
    * Create（创建）
    * Delete（删除）
    * Search（搜索）
    * Update（更新）
* Observable（可观测项）
    * Create（创建）
    * Delete（删除）
    * Execute Analyzer（执行分析器）
    * Execute Responder（执行响应器）
    * Get（获取）
    * Search（搜索）
    * Update（更新）
* Page（页面）
    * Create（创建）
    * Delete（删除）
    * Search（搜索）
    * Update（更新）
* Query（查询）
    * Execute Query（执行查询）
* Task（任务）
    * Create（创建）
    * Delete（删除）
    * Execute Responder（执行响应器）
    * Get（获取）
    * Search（搜索）
    * Update（更新）
* Task Log（任务日志）
    * Add Attachment（添加附件）
    * Create（创建）
    * Delete（删除）
    * Delete Attachment（删除附件）
    * Execute Responder（执行响应器）
    * Get（获取）
    * Search（搜索）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 TheHive 5 集成模板](https://n8n.io/integrations/thehive-5)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 TheHive 提供触发器节点。更多信息请参阅 [TheHive 5 Trigger 节点文档](../trigger-nodes/n8n-nodes-base.thehive5trigger.md)。

该服务的更多信息，请参阅 TheHive 的[文档](https://docs.strangebee.com/)。
