---
title: ClickUp 触发器节点文档
description: 了解如何在 n8n 中使用 ClickUp 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: ClickUp 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.clickuptrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.clickuptrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.clickuptrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# ClickUp 触发器节点 <a href="#clickup-trigger-node" id="clickup-trigger-node"></a>

[ClickUp](https://clickup.com/) 是基于云的协作和项目管理工具，适用于各种规模和行业的企业。功能包括沟通协作工具、任务分配和状态、提醒及任务工具栏。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [ClickUp 凭据文档](../credentials/clickup.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [ClickUp Trigger 集成](https://n8n.io/integrations/clickup-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* Key result（关键结果）
    * Created（已创建）
    * Deleted（已删除）
    * Updated（已更新）
* List（列表）
    * Created（已创建）
    * Deleted（已删除）
    * Updated（已更新）
* Space（空间）
    * Created（已创建）
    * Deleted（已删除）
    * Updated（已更新）
* Task（任务）
    * Assignee updated（受派人已更新）
    * Comment（评论）
      * Posted（已发布）
      * Updated（已更新）
    * Created（已创建）
    * Deleted（已删除）
    * Due date updated（截止日期已更新）
    * Moved（已移动）
    * Status updated（状态已更新）
    * Tag updated（标签已更新）
    * Time estimate updated（预估耗时已更新）
    * Time tracked updated（已跟踪耗时已更新）
    * Updated（已更新）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 ClickUp 提供应用节点。更多信息请参阅 [ClickUp 节点文档](../app-nodes/n8n-nodes-base.clickup.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/clickup-trigger/)。

API 的详细信息，请参阅 [ClickUp 文档](https://developer.clickup.com/docs/authentication)。
