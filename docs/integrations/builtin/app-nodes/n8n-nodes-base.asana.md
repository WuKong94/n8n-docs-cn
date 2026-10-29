---
title: Asana 节点文档
description: 了解如何在 n8n 中使用 Asana 节点，并按照技术文档将 Asana 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Asana 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.asana.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.asana
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.asana
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Asana 节点 <a href="#asana-node" id="asana-node"></a>

使用 Asana 节点自动处理 Asana 中的工作，并将其与其他应用集成。n8n 内置支持多种 Asana 功能，包括创建、更新、删除和获取用户、任务、项目和子任务。

本页列出了 Asana 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Asana 凭据](../credentials/asana.md)。
{% endhint %}

{% hint style="info" %}
**功能可用范围**

由于 Asana API 发生变化，此节点的部分操作自 2023 年 1 月 17 日起失效。Asana 节点需要 n8n 1.22.2 才能支持这些操作。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Project（项目）
    * Create a new project（创建新项目）
    * Delete a project（删除项目）
    * Get a project（获取项目）
    * Get all projects（获取全部项目）
    * Update a project（更新项目）
* Subtask（子任务）
    * Create a subtask（创建子任务）
    * Get all subtasks（获取全部子任务）
* Task（任务）
    * Create a task（创建任务）
    * Delete a task（删除任务）
    * Get a task（获取任务）
    * Get all tasks（获取全部任务）
    * Move a task（移动任务）
    * Search for tasks（搜索任务）
    * Update a task（更新任务）
* Task Comment（任务评论）
    * Add a comment to a task（为任务添加评论）
    * Remove a comment from a task（从任务移除评论）
* Task Tag（任务标签）
    * Add a tag to a task（为任务添加标签）
    * Remove a tag from a task（从任务移除标签）
* Task Project（任务项目）
    * Add a task to a project（将任务添加到项目）
    * Remove a task from a project（从项目移除任务）
* User（用户）
    * Get a user（获取用户）
    * Get all users（获取全部用户）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Asana 集成模板](https://n8n.io/integrations/asana)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
