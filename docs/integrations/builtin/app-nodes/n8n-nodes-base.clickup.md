---
title: ClickUp 节点文档
description: 了解如何在 n8n 中使用 ClickUp 节点，并按照技术文档将 ClickUp 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: ClickUp 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.clickup.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.clickup
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.clickup
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# ClickUp 节点 <a href="#clickup-node" id="clickup-node"></a>

使用 ClickUp 节点自动处理 ClickUp 中的工作，并将其与其他应用集成。n8n 内置支持多种 ClickUp 功能，包括创建、获取、删除和更新文件夹、检查清单、标签、评论和目标。

本页列出了 ClickUp 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [ClickUp 凭据](../credentials/clickup.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Checklist（检查清单）
    * Create a checklist（创建检查清单）
    * Delete a checklist（删除检查清单）
    * Update a checklist（更新检查清单）
* Checklist Item（检查清单项）
    * Create a checklist item（创建检查清单项）
    * Delete a checklist item（删除检查清单项）
    * Update a checklist item（更新检查清单项）
* Comment（评论）
    * Create a comment（创建评论）
    * Delete a comment（删除评论）
    * Get all comments（获取全部评论）
    * Update a comment（更新评论）
* Folder（文件夹）
    * Create a folder（创建文件夹）
    * Delete a folder（删除文件夹）
    * Get a folder（获取文件夹）
    * Get all folders（获取全部文件夹）
    * Update a folder（更新文件夹）
* Goal（目标）
    * Create a goal（创建目标）
    * Delete a goal（删除目标）
    * Get a goal（获取目标）
    * Get all goals（获取所有目标）
    * Update a goal（更新目标）
* Goal Key Result（目标关键成果）
    * Create a key result（创建关键成果）
    * Delete a key result（删除关键成果）
    * Update a key result（更新关键成果）
* List（列出）
    * Create a list（创建列表）
    * Retrieve list's custom fields（获取列表的自定义字段）
    * Delete a list（删除列表）
    * Get a list（获取列表）
    * Get all lists（获取全部列表）
    * Get list members（获取列表成员）
    * Update a list（更新列表）
* Space Tag（空间标签）
    * Create a space tag（创建空间标签）
    * Delete a space tag（删除空间标签）
    * Get all space tags（获取所有空间标签）
    * Update a space tag（更新空间标签）
* Task（任务）
    * Create a task（创建任务）
    * Delete a task（删除任务）
    * Get a task（获取任务）
    * Get all tasks（获取全部任务）
    * Get task members（获取任务成员）
    * Set a custom field（设置自定义字段）
    * Update a task（更新任务）
* Task List（任务列表）
    * Add a task to a list（将任务添加到列表）
    * Remove a task from a list（从列表移除任务）
* Task Tag（任务标签）
    * Add a tag to a task（为任务添加标签）
    * Remove a tag from a task（移除任务的标签）
* Task Dependency（任务依赖关系）
    * Create a task dependency（创建任务依赖关系）
    * Delete a task dependency（删除任务依赖关系）
* Time Entry（工时条目）
    * Create a time entry（创建工时条目）
    * Delete a time entry（删除工时条目）
    * Get a time entry（获取工时记录）
    * Get all time entries（获取所有工时记录）
    * Start a time entry（开始工时记录）
    * Stop the current running timer（停止当前运行的计时器）
    * Update a time Entry（更新工时记录）
* Time Entry Tag（工时记录标签）
    * Add tag to time entry（为工时记录添加标签）
    * Get all time entry tags（获取所有工时记录标签）
    * Remove tag from time entry（移除工时记录的标签）

## 操作详情 <a href="#operation-details" id="operation-details"></a>

### 获取任务 <a href="#get-a-task" id="get-a-task"></a>

使用 **Get a task**（获取任务）操作时，可选择启用以下选项：

- **Include Subtasks**（包含子任务）：启用时，还会获取并包含指定任务的子任务。
- **Include Markdown Description**（包含 Markdown 描述）：启用时，在响应中包含 `markdown_description` 字段，保留任务描述中的链接和格式。当任务描述包含链接或丰富格式时，这很有用。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 ClickUp 集成模板](https://n8n.io/integrations/clickup)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

