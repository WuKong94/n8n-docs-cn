---
title: Figma 触发器（Beta）节点文档
description: 了解如何在 n8n 中使用 Figma 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Figma 触发器（Beta）节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.figmatrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.figmatrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.figmatrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Figma 触发器（Beta）节点 <a href="#figma-trigger-beta-node" id="figma-trigger-beta-node"></a>

[Figma](https://www.figma.com/) 是以网页端为主的原型设计工具，其 macOS 和 Windows 桌面应用还提供更多离线功能。

{% hint style="warning" %}
**支持的 Figma 套餐**

Figma 的免费“Starter”套餐不支持 Webhook。你的团队需要使用“Professional”套餐，才能使用此节点。
{% endhint %}

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Figma 凭据文档](../credentials/figma.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Figma Trigger 集成](https://n8n.io/integrations/figma-trigger-beta/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

- **File Commented**（文件已被评论）：有人评论文件时触发。
- **File Deleted**（文件已删除）：有人删除单个文件时触发，删除包含所有文件的整个文件夹时不会触发。
- **File Updated**（文件已更新）：有人保存或删除文件时触发。修改后 30 秒内关闭文件时会发生保存。
- **File Version Updated**（文件版本已更新）：有人在文件的版本历史记录中创建命名版本时触发。
- **Library Publish**（组件库发布）：有人发布组件库文件时触发。

