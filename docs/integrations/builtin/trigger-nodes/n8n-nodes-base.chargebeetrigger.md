---
title: Chargebee 触发器节点文档
description: 了解如何在 n8n 中使用 Chargebee 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Chargebee 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.chargebeetrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.chargebeetrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.chargebeetrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Chargebee 触发器节点 <a href="#chargebee-trigger-node" id="chargebee-trigger-node"></a>

[Chargebee](https://www.chargebee.com/) 是面向订阅式 SaaS 和电子商务企业的计费平台。它与支付网关集成，可自动收取周期性付款，并处理发票、税费、会计、邮件通知、SaaS 指标和客户管理。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Chargebee 凭据文档](../credentials/chargebee.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Chargebee Trigger 集成](https://n8n.io/integrations/chargebee-trigger/)页面。
{% endhint %}

## 在 Chargebee 中添加 Webhook URL <a href="#add-webhook-url-in-chargebee" id="add-webhook-url-in-chargebee"></a>

在 Chargebee 中添加 Webhook URL：

1. 打开 Chargebee 控制台。
2. 进入 **Settings**（设置）> **Configure Chargebee**（配置 Chargebee）。
4. 向下滚动，选择 **Webhooks**。
5. 选择 **Add Webhook**（添加 Webhook）按钮。
6. 输入 **Webhook Name**（Webhook 名称）和 **Webhook URL**。
7. 选择 **Create**（创建）。
