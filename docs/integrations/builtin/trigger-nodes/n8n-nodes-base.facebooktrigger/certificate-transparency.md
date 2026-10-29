---
title: Facebook 触发器 证书透明度对象文档
contentType:
- integration
- reference
priority: medium
nodeTitle: Facebook 触发器 证书透明度对象文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/certificate-transparency.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/certificate-transparency
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/certificate-transparency
description: 了解如何在 n8n 中使用 Facebook 触发器节点的证书透明度对象，并按照技术文档将其集成到工作流中。
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


# Certificate Transparency（证书透明度） <a id="certificate-transparency"></a>

使用此对象，接收已订阅证书警报或钓鱼警报的任意域名的新签发证书更新。触发器本身的更多信息，请参阅 [Facebook Trigger](./README.md)。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Facebook App 凭据文档](../../credentials/facebookapp.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Facebook Trigger 集成](https://n8n.io/integrations/facebook-trigger/)页面。
{% endhint %}

## 触发器配置 <a href="#trigger-configuration" id="trigger-configuration"></a>

使用此对象配置触发器：

1. 选择 **Credential to connect with**（连接凭据），可选择现有的 [Facebook App 凭据](../../credentials/facebookapp.md)，也可创建新凭据。
2. 输入与你的凭据关联的应用的 **APP ID**（应用 ID）。更多信息请参阅 [Facebook App 凭据](../../credentials/facebookapp.md)文档。
3. 将 **Object**（对象）设为 **Certificate Transparency**（证书透明度）。
4. **Field Names or IDs**（字段名称或 ID）：默认情况下，节点使用 `*` 通配符筛选，对所有可用事件触发。要限定事件，请使用 `X` 移除星号，再通过下拉菜单或表达式选择所需的更新。可选项包括：
   * **Certificate**（证书）：有人为订阅的域名签发新证书时通知你。需要先为域名订阅证书警报。
   * **Phishing**（钓鱼）：有人签发的新证书可能仿冒你订阅的某个合法域名时通知你。
5. 在 **Options**（选项）中开启 **Include Values**（包含值）开关。未启用此选项时，此对象类型会失败。

要接收这些警报，需要为域名订阅相应的警报：

* 证书警报的订阅方法，请参阅[证书警报](https://developers.facebook.com/docs/certificate-transparency-api#certificate-alerts-subscribing)。
* 钓鱼警报的订阅方法，请参阅[钓鱼警报](https://developers.facebook.com/docs/certificate-transparency-api#phishing-alerts-subscribing)。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

更多信息请参阅[证书透明度 Webhook](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-certificate-transparency) 和 Meta 的 [Certificate Transparency](https://developers.facebook.com/docs/graph-api/webhooks/reference/certificate-transparency/) Graph API 参考。
