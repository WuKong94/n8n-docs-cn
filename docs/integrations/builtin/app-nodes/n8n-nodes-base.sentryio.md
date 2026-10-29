---
title: Sentry.io 节点文档
description: 了解如何在 n8n 中使用 Sentry.io 节点，并按照技术文档将 Sentry.io 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Sentry.io 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.sentryio.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sentryio
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sentryio
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Sentry.io 节点 <a href="#sentryio-node" id="sentryio-node"></a>

使用 Sentry.io 节点自动处理 Sentry.io 中的工作，并将其与其他应用集成。n8n 内置支持多种 Sentry.io 功能，包括创建、更新、删除和获取问题、项目及发布版本，以及获取全部事件。

本页列出了 Sentry.io 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Sentry.io 凭据](../credentials/sentryio.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Event（事件）
    * Get event by ID（按 ID 获取事件）
    * Get all events（获取全部事件）
* Issue（议题）
    * Delete an issue（删除问题）
    * Get issue by ID（按 ID 获取问题）
    * Get all issues（获取全部问题）
    * Update an issue（更新问题）
* Project（项目）
    * Create a new project（创建新项目）
    * Delete a project（删除项目）
    * Get project by ID（按 ID 获取项目）
    * Get all projects（获取全部项目）
    * Update a project（更新项目）
* Release（发布版本）
    * Create a release（创建发布版本）
    * Delete a release（删除发布版本）
    * Get release by version identifier（按版本标识符获取发布版本）
    * Get all releases（获取全部发布版本）
    * Update a release（更新发布版本）
* Organization（组织）
    * Create an organization（创建组织）
    * Get organization by slug（按 slug 获取组织）
    * Get all organizations（获取全部组织）
    * Update an organization（更新组织）
* Team（团队）
    * Create a new team（创建团队）
    * Delete a team（删除团队）
    * Get team by slug（按 slug 获取团队）
    * Get all teams（获取全部团队）
    * Update a team（更新团队）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Sentry.io 集成模板](https://n8n.io/integrations/sentryio)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Sentry.io 文档](https://docs.sentry.io/api/)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
