---
title: Facebook 触发器 链接对象文档
description: 了解如何在 n8n 中使用 Facebook 触发器节点的链接对象，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Facebook 触发器 链接对象文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/link.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/link
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/link
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Facebook 触发器 Link（链接）对象 <a href="#facebook-trigger-link-object" id="facebook-trigger-link-object"></a>

使用此对象接收由外部提供方生成丰富预览的链接的更新。触发器本身的更多信息，请参阅 [Facebook Trigger](README.md)。

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
1. 将 **Object**（对象）设为 **Link**（链接）。
1. **Field Names or IDs**（字段名称或 ID）：默认情况下，节点使用 `*` 通配符筛选，对所有可用事件触发。要限定事件，请使用 `X` 移除星号，再通过下拉菜单或表达式选择所需的更新。
1. 在 **Options**（选项）中开启 **Include Values**（包含值）开关。未启用此选项时，此对象类型会失败。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

更多信息请参阅 Meta 的 [Links](https://developers.facebook.com/docs/workplace/reference/webhooks/#links) Workplace API 参考。
