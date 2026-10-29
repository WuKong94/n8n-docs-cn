---
title: Jira Software 节点文档
description: 了解如何在 n8n 中使用 Jira Software 节点，并按照技术文档将 Jira Software 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Jira Software 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.jira.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jira
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jira
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Jira Software 节点 <a href="#jira-software-node" id="jira-software-node"></a>

使用 Jira Software 节点自动处理 Jira 中的工作，并将 Jira 与其他应用集成。n8n 内置支持多种 Jira 功能，包括创建、更新、删除和获取议题及用户。

本页列出了 Jira Software 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Jira 凭据](../credentials/jira.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Issue（议题）
    * Get issue changelog（获取议题变更记录）
    * Create a new issue（创建新议题）
    * Delete an issue（删除议题）
    * Get an issue（获取议题）
    * Get all issues（获取全部议题）
    * Create an email notification for an issue and add it to the mail queue（为议题创建电子邮件通知，并加入邮件队列）
    * Return either all transitions or a transition that can be performed by the user on an issue, based on the issue's status（根据议题状态，返回用户可对议题执行的所有状态转换或某个状态转换）
    * Update an issue（更新议题）
* Issue Attachment（议题附件）
    * Add attachment to issue（向议题添加附件）
    * Get an attachment（获取附件）
    * Get all attachments（获取所有附件）
    * Remove an attachment（移除附件）
* Issue Comment（议题评论）
    * Add comment to issue（向议题添加评论）
    * Get a comment（获取评论）
    * Get all comments（获取全部评论）
    * Remove a comment（移除评论）
    * Update a comment（更新评论）
* User（用户）
    * Create a new user.（创建新用户）
    * Delete a user.（删除用户）
    * Retrieve a user.（获取用户）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Jira Software 集成模板](https://n8n.io/integrations/jira-software)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

要进一步了解 Jira Query Language（JQL，Jira 查询语言），请参阅 [JQL 官方文档](https://www.atlassian.com/software/jira/guides/expand-jira/jql)。

## 获取指定项目的议题 <a href="#fetch-issues-for-a-specific-project" id="fetch-issues-for-a-specific-project"></a>

**Get All**（获取全部）操作会返回 Jira 中的所有议题。要获取某个项目的议题，需要使用 Jira Query Language（JQL）。

例如，要获取名为 `n8n` 的项目中的所有议题，可按以下步骤操作：

- 在 **Operation**（操作）下拉列表中选择 **Get All**（获取全部）。
- 将 **Return All**（返回全部）切换为 true。
- 选择 **Add Option**（添加选项），再选择 **JQL**。
- 在 **JQL** 字段中输入 `project=n8n`。

此查询会获取名为 `n8n` 的项目中的所有议题。将 `n8n` 替换为你的项目名称，即可获取该项目的所有议题。
