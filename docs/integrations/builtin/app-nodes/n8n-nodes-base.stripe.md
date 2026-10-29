---
title: Stripe 节点文档
description: 了解如何在 n8n 中使用 Stripe 节点，并按照技术文档将 Stripe 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Stripe 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.stripe.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.stripe
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.stripe
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Stripe 节点 <a href="#stripe-node" id="stripe-node"></a>

使用 Stripe 节点自动处理 Stripe 中的工作，并将其与其他应用集成。n8n 内置支持多种 Stripe 功能，包括获取余额、创建收款和计量事件，以及删除客户。

本页列出了 Stripe 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Stripe 凭据](../credentials/stripe.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Balance（余额）
    * Get a balance（获取余额）
* Charge（收款）
    * Create a charge（创建收款）
    * Get a charge（获取收款）
    * Get all charges（获取全部收款）
    * Update a charge（更新收款）
* Coupon（优惠券）
    * Create a coupon（创建优惠券）
    * Get all coupons（获取全部优惠券）
* Customer（客户）
    * Create a customer（创建客户）
    * Delete a customer（删除客户）
    * Get a customer（获取客户）
    * Get all customers（获取全部客户）
    * Update a customer（更新客户）
* Customer Card（客户银行卡）
    * Add a customer card（添加客户银行卡）
    * Get a customer card（获取客户银行卡）
    * Remove a customer card（移除客户银行卡）
* Meter Event（计量事件）
    * Create a meter event（创建计量事件）
* Source（支付来源）
    * Create a source（创建支付来源）
    * Delete a source（删除支付来源）
    * Get a source（获取支付来源）
* Token（令牌）
    * Create a token（创建令牌）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Stripe 集成模板](https://n8n.io/integrations/stripe)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
