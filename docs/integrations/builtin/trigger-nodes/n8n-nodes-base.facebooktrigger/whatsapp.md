---
title: Facebook 触发器 WhatsApp 商业账户对象文档
contentType:
- integration
- reference
priority: medium
nodeTitle: Facebook 触发器 WhatsApp 商业账户对象文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/whatsapp.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/whatsapp
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/whatsapp
description: 了解如何在 n8n 中使用 Facebook 触发器节点的WhatsApp 商业账户对象，并按照技术文档将其集成到工作流中。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# WhatsApp Business Account（WhatsApp 商业账户） <a id="whatsapp-business-account"></a>

你的 WhatsApp Business Account（WABA，商业账户）变更时，使用此对象接收更新。触发器本身的更多信息，请参阅 [Facebook Trigger](./README.md)。

{% hint style="warning" %}
**使用 WhatsApp 触发器**

n8n 建议使用配有 [WhatsApp 凭据](../../credentials/whatsapp.md)的 [WhatsApp Trigger 节点](../n8n-nodes-base.whatsapptrigger.md)来替代 Facebook Trigger 节点。该触发器可订阅的事件数量是 Facebook Trigger 节点的两倍。
{% endhint %}

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Facebook App 凭据文档](../../credentials/facebookapp.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Facebook Trigger 集成](https://n8n.io/integrations/facebook-trigger/)页面。
{% endhint %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

使用此对象的触发器前，需要先在应用和 WhatsApp 账户中进行一些配置：

1. 在 WhatsApp 商业账户下订阅你的应用。必须订阅由你的企业拥有的应用；共享给企业的应用无法接收 Webhook 通知。
2. 如果你以解决方案合作伙伴身份开展工作，请确保应用已完成应用审核，并申请了 `whatsapp_business_management` 权限。

## 触发器配置 <a href="#trigger-configuration" id="trigger-configuration"></a>

使用此对象配置触发器：

1. 选择 **Credential to connect with**（连接凭据），可选择现有的 [Facebook App 凭据](../../credentials/facebookapp.md)，也可创建新凭据。
2. 输入与你的凭据关联的应用的 **APP ID**（应用 ID）。更多信息请参阅 [Facebook App 凭据](../../credentials/facebookapp.md)文档。
3. 将 **Object**（对象）设为 **WhatsApp Business Account**（WhatsApp 商业账户）。
4. **Field Names or IDs**（字段名称或 ID）：默认情况下，节点使用 `*` 通配符筛选，对所有可用事件触发。要限定事件，请使用 `X` 移除星号，再通过下拉菜单或表达式选择所需的更新。可选项包括：
   * **Message Template Status Update**（消息模板状态更新）
   * **Phone Number Name Update**（电话号码名称更新）
   * **Phone Number Quality Update**（电话号码质量更新）
   * **Account Review Update**（账户审核更新）
   * **Account Update**（账户更新）
5. 在 **Options**（选项）中开启 **Include Values**（包含值）开关。未启用此选项时，此对象类型会失败。

更多信息请参阅 [WhatsApp 商业账户 Webhook](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-whatsapp) 和 Meta 的 [WhatsApp Business Account](https://developers.facebook.com/docs/graph-api/webhooks/reference/whatsapp-business-account/) Graph API 参考。
