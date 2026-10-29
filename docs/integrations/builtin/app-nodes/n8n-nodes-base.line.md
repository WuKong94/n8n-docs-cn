---
title: Line 节点文档
description: 了解如何在 n8n 中使用 Line 节点，并按照技术文档将 Line 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Line 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.line.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.line
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.line
layout:
  description:
    visible: false
tags:
- tag: deprecated
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Line 节点 <a href="#line-node" id="line-node"></a>


{% hint style="warning" %}
**功能可用范围**

Line 节点从 n8n 1.64.0 开始弃用。LINE Notify 于 2025 年 4 月 1 日终止服务，此后该节点将无法使用。更多信息请参阅 LINE Notify 的[服务终止公告](https://notify-bot.line.me/closing-announce)。
{% endhint %}


使用 Line 节点自动处理 Line 中的工作，并将其与其他应用集成。n8n 内置支持多种 Line 功能，包括发送通知。

本页列出了 Line 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Line 凭据](../credentials/line.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Notification（通知）
    * Sends notifications to users or groups（向用户或群组发送通知）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Line 集成模板](https://n8n.io/integrations/line)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
