---
title: Google Chat 节点文档
description: 了解如何在 n8n 中使用 Google Chat 节点，并按照技术文档将 Google Chat 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Google Chat 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googlechat.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Chat 节点 <a href="#google-chat-node" id="google-chat-node"></a>

使用 Google Chat 节点自动处理 Google Chat 中的工作，并将其与其他应用集成。n8n 内置支持多种 Google Chat 功能，包括获取成员关系和空间，以及创建和删除消息。

本页列出了 Google Chat 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Google 凭据](../credentials/google/README.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/hitl-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Member（成员）
    * Get a membership（获取成员关系）
    * Get all memberships in a space（获取空间中的全部成员关系）
* Message（消息）
    * Create a message（创建消息）
    * Delete a message（删除消息）
    * Get a message（获取消息）
	* Send and Wait for Response（发送并等待回复）
    * Update a message（更新消息）
* Space（空间）
    * Get a space（获取空间）
    * Get all spaces the caller is a member of（获取调用者所属的全部空间）

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/send-and-wait-operation.md" %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Google Chat 集成模板](https://n8n.io/integrations/google-chat)，或[搜索所有模板](https://n8n.io/workflows/)
