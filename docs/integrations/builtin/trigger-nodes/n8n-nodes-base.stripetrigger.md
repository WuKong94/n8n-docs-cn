---
title: Stripe 触发器节点文档
description: 了解如何在 n8n 中使用 Stripe 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Stripe 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.stripetrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.stripetrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.stripetrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Stripe 触发器节点 <a href="#stripe-trigger-node" id="stripe-trigger-node"></a>

[Stripe](https://stripe.com/) 是一组支付 API，为在线企业的商业交易提供支持。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Stripe 凭据文档](../credentials/stripe.md)。
{% endhint %}

## Webhook 身份验证 <a href="#webhook-authentication" id="webhook-authentication"></a>

{% hint style="info" %}
**功能可用范围**

从 n8n 2.25.7 和 n8n 2.26.2 起，可以验证传入请求。
{% endhint %}

Stripe Trigger 节点可以验证传入 Webhook 请求是否确实来自 Stripe。

在 [Stripe 凭据](../credentials/stripe.md)中设置 **Signature Secret**（签名密钥）后，节点会检查每个请求的 `Stripe-Signature` 请求头，并对未签名、伪造或超过五分钟的请求返回 `401 Unauthorized` 响应。n8n 不会为被拒绝的请求运行工作流。

未设置 **Signature Secret** 时，节点不会验证传入请求，知道 Webhook URL 的任何人都可能发送伪造事件。n8n 强烈建议设置签名密钥。配置步骤请参阅[验证传入请求](../credentials/stripe.md#verify-incoming-requests)。

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Stripe Trigger 集成](https://n8n.io/integrations/stripe-trigger/)页面。
{% endhint %}
