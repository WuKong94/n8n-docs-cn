---
title: Facebook Lead Ads 触发器节点文档
description: 了解如何在 n8n 中使用 Facebook Lead Ads 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Facebook Lead Ads 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Facebook Lead Ads 触发器节点 <a href="#facebook-lead-ads-trigger-node" id="facebook-lead-ads-trigger-node"></a>

使用 Facebook Lead Ads Trigger 节点响应 [Facebook Lead Ads](https://www.facebook.com/business/ads/lead-ads/) 中的事件，并将其与其他应用集成。n8n 内置支持响应新的销售线索。

本页列出了 Facebook Lead Ads Trigger 节点可响应的事件，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Facebook Lead Ads 凭据文档](../credentials/facebookleadads.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Facebook Lead Ads Trigger 集成](https://n8n.io/integrations/facebook-lead-ads-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* New lead（新的销售线索）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/facebook-lead-ads-trigger/)。

API 的详细信息，请参阅 [Facebook Lead Ads 文档](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下列出 Facebook Lead Ads Trigger 节点的常见错误和问题，以及解决或排查步骤。

### 工作流只能在测试或生产环境之一正常运行 <a href="#workflow-only-works-in-testing-or-production" id="workflow-only-works-in-testing-or-production"></a>

Facebook Lead Ads 每个应用只允许注册一个 Webhook。因此，每次在测试 URL 和生产 URL 之间切换，Facebook Lead Ads 都会覆盖已注册的 Webhook URL。

测试已发布的工作流时，可能因此遇到问题。Facebook Lead Ads 只会将事件发送到两个 Webhook URL 中的一个，另一个始终收不到事件通知。

一种解决办法是在测试时停用工作流：

{% hint style="warning" %}
**会中断生产流量**

此办法会暂时停用生产工作流以进行测试。取消发布期间，工作流将不再接收生产流量。
{% endhint %}

1. 进入工作流页面。
2. 在工作流设置下拉菜单中，单击 **Unpublish**（取消发布），暂时停用工作流。
3. 使用测试 Webhook URL 测试工作流。
4. 测试完成后，单击 **Publish**（发布）。生产 Webhook URL 应会恢复正常工作。
