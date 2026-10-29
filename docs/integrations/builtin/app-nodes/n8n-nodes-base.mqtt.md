---
title: MQTT 节点文档
description: 了解如何在 n8n 中使用 MQTT 节点，并按照技术文档将 MQTT 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: MQTT 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.mqtt.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mqtt
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mqtt
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MQTT 节点 <a href="#mqtt-node" id="mqtt-node"></a>

使用 MQTT 节点自动处理 MQTT 中的工作，并将其与其他应用集成。n8n 支持通过 MQTT 传输消息。

本页列出了 MQTT 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [MQTT 凭据](../credentials/mqtt.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

使用 MQTT 节点发送消息。你可以设置消息主题，并选择是否将节点输入数据作为消息的一部分发送。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 MQTT 集成模板](https://n8n.io/integrations/mqtt)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 MQTT 提供触发器节点。更多信息请参阅 [MQTT Trigger 节点文档](../trigger-nodes/n8n-nodes-base.mqtttrigger.md)。

有关该服务的更多信息，请参阅 [MQTT 文档](https://mqtt.org/getting-started/)。
