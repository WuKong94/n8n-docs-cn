---
title: Brevo 触发器节点文档
description: 了解如何在 n8n 中使用 Brevo 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Brevo 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.brevotrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.brevotrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.brevotrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Brevo 触发器节点 <a href="#brevo-trigger-node" id="brevo-trigger-node"></a>

[Brevo](https://www.brevo.com/) 是帮助用户发展业务的数字营销平台。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Brevo 凭据文档](../credentials/brevo.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Brevo Trigger 集成](https://n8n.io/integrations/brevo-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* Email blocked（邮件已被阻止）
* Email clicked（邮件已被点击）
* Email deferred（邮件已延迟投递）
* Email delivered（邮件已送达）
* Email hard bounce（邮件硬退信）
* Email invalid（邮件无效）
* Email marked spam（邮件已被标记为垃圾邮件）
* Email opened（邮件已打开）
* Email sent（邮件已发送）
* Email soft bounce（邮件软退信）
* Email unique open（邮件唯一打开事件）
* Email unsubscribed（邮件已退订）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Brevo 提供应用节点。更多信息请参阅 [Brevo 节点文档](../app-nodes/n8n-nodes-base.brevo.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/brevo-trigger/)。

API 的详细信息，请参阅 [Brevo 文档](https://developers.brevo.com/)。
