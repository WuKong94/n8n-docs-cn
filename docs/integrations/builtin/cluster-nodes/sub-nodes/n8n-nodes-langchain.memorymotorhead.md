---
title: Motorhead（记忆） 节点文档
description: 了解如何在 n8n 中使用 Motorhead（记忆） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Motorhead（记忆） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead
layout:
  description:
    visible: false
tags:
- tag: deprecated
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Motorhead（记忆） 节点 <a href="#motorhead-node" id="motorhead-node"></a>

{% hint style="warning" %}
**功能可用性**

Motorhead 项目已停止维护。Motorhead 节点从 n8n 2.8.0 起弃用。更多信息请参阅[已弃用和具有版本的节点](../../deprecated-nodes.md)。
{% endhint %}

使用 Motorhead 节点，将 Motorhead 用作记忆[^1]服务器。

本页列出了 Motorhead 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Motorhead 凭据文档](../../credentials/motorhead.md)。
{% endhint %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Session ID**（会话 ID）：输入在工作流数据中存储记忆时使用的 ID。

## 节点参考 <a href="#node-reference" id="node-reference"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Motorhead（记忆） 集成模板](https://n8n.io/integrations/motorhead)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 单个记忆实例 <a href="#single-memory-instance" id="single-memory-instance"></a>

向工作流添加多个 Motorhead 节点时，默认情况下所有这些节点都访问同一个记忆实例。执行会覆盖现有记忆内容的破坏性操作时，请谨慎，例如 [Chat Memory Manager](./n8n-nodes-langchain.memorymanager.md) 节点中的覆盖全部消息操作。如果希望在工作流中使用多个记忆实例，请为不同记忆节点设置不同的会话 ID。

[^1]: 在 AI 场景中，记忆让 AI 工具能够在多次交互之间保存消息上下文。例如，与 AI 智能体持续对话时，无需在每条消息中重复提交上下文。在 n8n 中，AI 智能体节点可以使用记忆，而 AI 链不能。
