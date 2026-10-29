---
title: Grafana 节点文档
description: 了解如何在 n8n 中使用 Grafana 节点，并按照技术文档将 Grafana 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Grafana 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.grafana.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.grafana
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.grafana
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Grafana 节点 <a href="#grafana-node" id="grafana-node"></a>

使用 Grafana 节点自动处理 Grafana 中的工作，并将其与其他应用集成。n8n 内置支持多种 Grafana 功能，包括创建、更新、删除和获取仪表板、团队及用户。

本页列出了 Grafana 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Grafana 凭据](../credentials/grafana.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Dashboard（仪表板）
    * Create a dashboard（创建仪表板）
    * Delete a dashboard（删除仪表板）
    * Get a dashboard（获取仪表板）
    * Get all dashboards（获取全部仪表板）
    * Update a dashboard（更新仪表板）
* Team（团队）
    * Create a team（创建团队）
    * Delete a team（删除团队）
    * Get a team（获取团队）
    * Retrieve all teams（获取全部团队）
    * Update a team（更新团队）
* Team Member（团队成员）
    * Add a member to a team（向团队添加成员）
    * Retrieve all team members（获取全部团队成员）
    * Remove a member from a team（从团队移除成员）
* User（用户）
    * Delete a user from the current organization（从当前组织删除用户）
    * Retrieve all users in the current organization（获取当前组织的全部用户）
    * Update a user in the current organization（更新当前组织中的用户）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Grafana 集成模板](https://n8n.io/integrations/grafana)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
