---
title: KoboToolbox 触发器节点文档
description: 了解如何在 n8n 中使用 KoboToolbox 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: KoboToolbox 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.kobotoolboxtrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.kobotoolboxtrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.kobotoolboxtrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# KoboToolbox 触发器节点 <a href="#kobotoolbox-trigger-node" id="kobotoolbox-trigger-node"></a>

[KoboToolbox](https://www.kobotoolbox.org/) 是实地调查和数据收集工具，可设计交互式表单，在移动设备上离线填写。既提供免费的云端方案，也支持自托管。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [KoboToolbox 凭据文档](../credentials/kobotoolbox.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [KoboToolbox Trigger 集成](https://n8n.io/integrations/kobotoolbox-trigger/)页面。
{% endhint %}

指定表单收到新提交时，此节点会启动工作流。触发器节点负责创建和删除钩子，无需在 KoboToolbox 中进行额外配置。

它的行为与 [KoboToolbox](../app-nodes/n8n-nodes-base.kobotoolbox.md) 节点的 Get Submission（获取提交）操作相同，也支持相同的数据重新格式化选项。
