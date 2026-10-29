---
title: Facebook 触发器 广告账户对象文档
description: 了解如何在 n8n 中使用 Facebook 触发器节点的广告账户对象，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Facebook 触发器 广告账户对象文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/ad-account.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/ad-account
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/ad-account
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Facebook 触发器 Ad Account（广告账户）对象 <a href="#facebook-trigger-ad-account-object" id="facebook-trigger-ad-account-object"></a>

使用此对象接收广告账户中某些广告变更的更新。触发器本身的更多信息，请参阅 [Facebook Trigger](README.md)。

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
1. 输入与你的凭据关联的应用的 **APP ID**（应用 ID）。更多信息请参阅 [Facebook App 凭据](../../credentials/facebookapp.md)文档。
1. 将 **Object**（对象）设为 **Ad Account**（广告账户）。
1. **Field Names or IDs**（字段名称或 ID）：默认情况下，节点使用 `*` 通配符筛选，对所有可用的 Ad Account 事件触发。要限定事件，请使用 `X` 移除星号，再通过下拉菜单或表达式选择所需的更新。可选项包括：
    * **In Process Ad Objects**（处理中的广告对象）：当广告系列、广告组或广告退出 `IN_PROCESS` 状态时通知你。更多信息请参阅 Meta 的[广告创建和编辑后处理](https://developers.facebook.com/docs/marketing-api/using-the-api/post-processing/)。
    * **With Issues Ad Objects**（存在问题的广告对象）：当广告账户下的广告系列、广告组或广告进入 `WITH_ISSUES` 状态时通知你。
1. 在 **Options**（选项）中开启 **Include Values**（包含值）开关。未启用此选项时，此对象类型会失败。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

更多信息请参阅[广告账户 Webhook](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-ad-accounts) 和 Meta 的 [Ad Account](https://developers.facebook.com/docs/graph-api/webhooks/reference/ad-account/) Graph API 参考。
