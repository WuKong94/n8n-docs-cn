---
title: Google Drive 触发器节点文档
description: 了解如何在 n8n 中使用 Google Drive 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: n8n-nodes-base.googledrivetrigger
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Drive 触发器节点 <a href="#google-drive-trigger-node" id="google-drive-trigger-node"></a>

[Google Drive](https://drive.google.com) 是 Google 开发的文件存储与同步服务，允许用户在服务器上存储文件、跨设备同步文件，以及共享文件。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Google 凭据文档](../../credentials/google/README.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Google Drive Trigger 集成](https://n8n.io/integrations/google-drive-trigger/)页面。
{% endhint %}

{% hint style="info" %}
**手动执行与启用**

手动执行时，此节点会返回符合搜索条件的最近一个事件。如果没有匹配事件，例如正在监控新建文件但尚未创建任何文件，则会抛出错误。保存并发布后，节点会定期检查匹配事件，并为找到的每个事件触发工作流。
{% endhint %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见问题及建议的解决办法，请参阅[常见问题](common-issues.md)。
