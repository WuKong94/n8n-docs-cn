---
title: ConvertKit 触发器节点文档
description: 了解如何在 n8n 中使用 ConvertKit 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: ConvertKit 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.convertkittrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.convertkittrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.convertkittrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# ConvertKit 触发器节点 <a href="#convertkit-trigger-node" id="convertkit-trigger-node"></a>

[ConvertKit](https://www.convertkit.com/) 是功能完整的电子邮件营销平台，可用于建立邮件列表、发送群发邮件、自动执行邮件序列、创建细分群组和构建落地页。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [ConvertKit 凭据文档](../credentials/convertkit.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [ConvertKit Trigger 集成](https://n8n.io/integrations/convertkit-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* Form subscribe（表单订阅）
* Link click（链接点击）
* Product purchase（产品购买）
* Purchase created（购买记录已创建）
* Purchase complete（购买已完成）
* Sequence complete（邮件序列已完成）
* Sequence subscribe（订阅邮件序列）
* Subscriber activated（订阅者已激活）
* Subscriber unsubscribe（订阅者退订）
* Tag add（标签已添加）
* Tag Remove（标签已移除）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 ConvertKit 提供应用节点。更多信息请参阅 [ConvertKit 节点文档](../app-nodes/n8n-nodes-base.convertkit.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/convertkit-trigger/)。

API 的详细信息，请参阅 [ConvertKit 文档](https://developers.kit.com/v4#introduction)。
