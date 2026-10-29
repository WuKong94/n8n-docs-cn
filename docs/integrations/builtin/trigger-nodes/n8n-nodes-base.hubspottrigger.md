---
title: HubSpot 触发器节点文档
description: 了解如何在 n8n 中使用 HubSpot 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: HubSpot 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.hubspottrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.hubspottrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.hubspottrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# HubSpot 触发器节点 <a href="#hubspot-trigger-node" id="hubspot-trigger-node"></a>

[HubSpot](https://www.hubspot.com/) 提供社交媒体营销、内容管理、网站分析、落地页、客户支持和搜索引擎优化工具。

{% hint style="warning" %}
**Webhook**

启用第二个触发器后，之前的触发器会停止工作，因为触发器启用时会向 HubSpot 注册新的 Webhook，而 HubSpot 同时只允许一个 Webhook。
{% endhint %}

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [HubSpot 凭据文档](../credentials/hubspot.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [HubSpot Trigger 集成](https://n8n.io/integrations/hubspot-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* Company（公司）
    * Created（已创建）
    * Deleted（已删除）
    * Property changed（属性已变更）
* Contact（联系人）
    * Created（已创建）
    * Deleted（已删除）
    * Privacy deleted（隐私删除）
    * Property changed（属性已变更）
* Conversation（会话）
    * Created（已创建）
    * Deleted（已删除）
    * New message（新消息）
    * Privacy deletion（隐私删除）
    * Property changed（属性已变更）
* Deal（交易）
    * Created（已创建）
    * Deleted（已删除）
    * Property changed（属性已变更）
* Ticket（工单）
    * Created（已创建）
    * Deleted（已删除）
    * Property changed（属性已变更）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 HubSpot 提供应用节点。更多信息请参阅 [HubSpot 节点文档](../app-nodes/n8n-nodes-base.hubspot.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/hubspot-trigger/)。

API 的详细信息，请参阅 [HubSpot 文档](https://developers.hubspot.com/docs/api/overview)。

