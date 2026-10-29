---
title: Calendly 触发器节点文档
description: 了解如何在 n8n 中使用 Calendly 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Calendly 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Calendly 触发器节点 <a href="#calendly-trigger-node" id="calendly-trigger-node"></a>

[Calendly](https://calendly.com/) 是帮助寻找会议时间的自动排程软件。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Calendly 凭据文档](../credentials/calendly.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Calendly Trigger 集成](https://n8n.io/integrations/calendly-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* Event created（事件已创建）
* Event canceled（事件已取消）

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下列出 Calendly Trigger 节点的常见错误和问题，以及解决或排查步骤。

### 仅对由 Calendly 管理的预约触发 <a href="#node-only-triggers-for-calendly-managed-bookings" id="node-only-triggers-for-calendly-managed-bookings"></a>

Calendly Webhook 仅对由 Calendly 管理的预约和取消操作触发。直接在已连接日历（例如 Google Calendar）中创建或编辑事件，不会触发 Calendly Trigger 节点。

### Webhook 回调 URL 必须是公开可访问的 HTTPS 地址 <a href="#webhook-callback-url-must-be-public-https" id="webhook-callback-url-must-be-public-https"></a>

Calendly Trigger 节点使用 Calendly Webhook，其回调 URL 必须是公开可访问的 HTTPS 地址。本地测试时，可以使用 [ngrok](https://ngrok.com/) 或 [Cloudflare Tunnel](https://www.cloudflare.com/products/tunnel/) 等隧道，并将 n8n 的 Webhook 地址配置为该公开 HTTPS URL。配置详情请参阅[配置 > Webhook URL](../../../deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-webhook-urls-with-reverse-proxy.md)。
