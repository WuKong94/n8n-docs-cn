---
title: Clockify 触发器节点文档
description: 了解如何在 n8n 中使用 Clockify 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Clockify 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.clockifytrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.clockifytrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.clockifytrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Clockify 触发器节点 <a href="#clockify-trigger-node" id="clockify-trigger-node"></a>

[Clockify](https://clockify.me/) 是免费的工时跟踪与时间表应用，用于跨项目记录工作时长。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Clockify 凭据文档](../credentials/clockify.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Clockify Trigger 集成](https://n8n.io/integrations/clockify-trigger/)页面。
{% endhint %}

此节点使用工作流的时区设置，确定时间记录开始时间的查询范围。要让触发器获取正确的时间记录，请在[工作流设置](../../../build/manage-workflows/configure-workflow-settings.md)中配置时区。
