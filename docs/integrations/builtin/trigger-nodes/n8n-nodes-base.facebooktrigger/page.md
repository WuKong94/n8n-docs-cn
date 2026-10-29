---
title: Facebook 触发器 主页对象文档
description: 了解如何在 n8n 中使用 Facebook 触发器节点的主页对象，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Facebook 触发器 主页对象文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/page.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/page
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/page
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Facebook 触发器 Page（主页）对象 <a href="#facebook-trigger-page-object" id="facebook-trigger-page-object"></a>

主页的资料字段或资料设置更新，或有人提及你的主页时，使用此对象接收更新。触发器本身的更多信息，请参阅 [Facebook Trigger](README.md)。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Facebook App 凭据文档](../../credentials/facebookapp.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Facebook Trigger 集成](https://n8n.io/integrations/facebook-trigger/)页面。
{% endhint %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

使用此对象的触发器前，需要先在应用和主页中进行一些配置：

1. 至少一位主页管理员需要向应用授予 `manage_pages` 权限。
1. 主页管理员至少需要具有版主权限，否则无法接收全部内容。
1. 还需要将应用添加到主页，可能需要前往 [Graph API Explorer](https://developers.facebook.com/tools/explorer/)，使用应用令牌执行以下调用：

    ```
    {page-id}/subscribed_apps?subscribed_fields=feed
    ```

## 触发器配置 <a href="#trigger-configuration" id="trigger-configuration"></a>

使用此对象配置触发器：

1. 选择 **Credential to connect with**（连接凭据），可选择现有的 [Facebook App 凭据](../../credentials/facebookapp.md)，也可创建新凭据。
1. 输入与你的凭据关联的应用的 **APP ID**（应用 ID）。更多信息请参阅 [Facebook App 凭据](../../credentials/facebookapp.md)文档。
1. 将 **Object**（对象）设为 **Page**（主页）。
1. **Field Names or IDs**（字段名称或 ID）：默认情况下，节点使用 `*` 通配符筛选，对所有可用事件触发。要限定事件，请使用 `X` 移除星号，再通过下拉菜单或表达式选择所需的更新。可选项包括各个个人资料字段，以及：
    * **Feed**（动态）：描述主页动态的大多数变更，包括帖子、点赞、分享等。
    * **Leadgen**（线索生成）：主页的线索生成设置发生变更时通知你。
    * **Live Videos**（直播视频）：主页的直播视频状态变更时通知你。
    * **Mention**（提及）：主页、评论等位置出现新的提及时通知你。
    * **Merchant Review**（商家评价）：主页的商家评价设置变更时通知你。
    * **Page Change Proposal**（主页变更提案）：Facebook 对你的 Facebook 主页提出变更建议时通知你。
    * **Page Upcoming Change**（主页即将发生的变更）：通知你 Facebook 主页即将发生的变更。这些变更由 Facebook 提出，可能设有接受或拒绝的截止时间，逾期后自动生效。
    * **Product Review**（产品评价）：主页的产品评价设置变更时通知你。
    * **Ratings**（评分）：主页的评分发生变更时通知你，包括新增评分，以及用户对评分发表评论或表情回应。
    * **Videos**（视频）：主页上视频的编码状态变更时通知你。
1. 在 **Options**（选项）中开启 **Include Values**（包含值）开关。未启用此选项时，此对象类型会失败。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

更多信息请参阅[主页 Webhook](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-pages) 和 Meta 的 [Page](https://developers.facebook.com/docs/graph-api/webhooks/reference/page/) Graph API 参考。
