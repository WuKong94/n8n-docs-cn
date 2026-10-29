---
title: Pushcut 触发器节点文档
description: 了解如何在 n8n 中使用 Pushcut 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Pushcut 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.pushcuttrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.pushcuttrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.pushcuttrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Pushcut 触发器节点 <a href="#pushcut-trigger-node" id="pushcut-trigger-node"></a>

[Pushcut](https://pushcut.io) 是 iOS 应用，可创建智能通知，以启动快捷指令、URL 和在线自动化。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Pushcut 凭据文档](../credentials/pushcut.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Pushcut Trigger 集成](https://n8n.io/integrations/pushcut-trigger/)页面。
{% endhint %}

## 配置 Pushcut 操作 <a href="#configure-a-pushcut-action" id="configure-a-pushcut-action"></a>

按以下步骤，将 Pushcut Trigger 节点与 Pushcut 应用配合配置。

1. 在 Pushcut 应用的 **Notifications**（通知）页面中选择一条通知。
2. 选择 **Add Action**（添加操作）按钮。
3. 在 **Label**（标签）字段中输入操作名称。
4. 选择 **Server**（服务器）标签页。
5. 选择 **Integration**（集成）标签页。
6. 选择 **Integration Trigger**（集成触发器）。
7. 在 n8n 中输入操作名称，选择 **Execute step**（执行步骤）。
8. 在 Pushcut 应用的 **Select Integration Trigger**（选择集成触发器）页面中选择此操作。
9. 选择右上角的 **Done**（完成），保存操作。
