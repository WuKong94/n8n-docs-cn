---
title: WooCommerce 触发器节点文档
description: 了解如何在 n8n 中使用 WooCommerce 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: WooCommerce 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.woocommercetrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.woocommercetrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.woocommercetrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# WooCommerce 触发器节点 <a href="#woocommerce-trigger-node" id="woocommerce-trigger-node"></a>

[WooCommerce](https://woocommerce.com/) 是可定制的开源 WordPress 电子商务插件。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [WooCommerce 凭据文档](../credentials/woocommerce.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [WooCommerce Trigger 集成](https://n8n.io/integrations/woocommerce-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

- coupon.created（优惠券已创建）
- coupon.updated（优惠券已更新）
- coupon.deleted（优惠券已删除）
- customer.created（客户已创建）
- customer.updated（客户已更新）
- customer.deleted（客户已删除）
- order.created（订单已创建）
- order.updated（订单已更新）
- order.deleted（订单已删除）
- product.created（产品已创建）
- product.updated（产品已更新）
- product.deleted（产品已删除）



