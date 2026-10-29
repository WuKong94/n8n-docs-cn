---
title: Twilio 触发器节点文档
description: 了解如何在 n8n 中使用 Twilio 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Twilio 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.twiliotrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.twiliotrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.twiliotrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Twilio 触发器节点 <a href="#twilio-trigger-node" id="twilio-trigger-node"></a>

使用 Twilio Trigger 节点响应 [Twilio](https://www.twilio.com) 中的事件，并将其与其他应用集成。n8n 内置支持多种 Twilio 事件，包括新短信和新通话。

本页列出了 Twilio Trigger 节点可响应的事件，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Twilio 凭据文档](../credentials/twilio.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Twilio 集成](https://n8n.io/integrations/twilio-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* On New SMS（收到新短信时）
* On New Call（出现新通话时）

{% hint style="info" %}
**新通话延迟**

Twilio 为已结束的通话生成摘要，可能最多需要三十分钟。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Twilio 提供应用节点。更多信息请参阅 [Twilio 节点文档](../app-nodes/n8n-nodes-base.twilio.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/twilio/)。

API 的详细信息，请参阅 [Twilio 文档](https://www.twilio.com/docs)。
