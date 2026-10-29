---
title: Postgres Chat Memory（Postgres 聊天记忆） 节点文档
description: 了解如何在 n8n 中使用 Postgres Chat Memory（Postgres 聊天记忆） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Postgres Chat Memory（Postgres 聊天记忆） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Postgres Chat Memory（Postgres 聊天记忆） 节点 <a href="#postgres-chat-memory-node" id="postgres-chat-memory-node"></a>

使用 Postgres Chat Memory 节点，将 Postgres 用作存储聊天历史的记忆[^1]服务器。

本页列出了 Postgres Chat Memory 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Postgres 凭据文档](../../credentials/postgres.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Session Key**（会话键）：输入在工作流数据中存储记忆时使用的键。
* **Table Name**（表名称）：输入存储聊天历史的表名称，表不存在时，系统会自动创建。
* **Context Window Length**（上下文窗口长度）：输入作为上下文考虑的历史交互次数。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 单个记忆实例 <a href="#single-memory-instance" id="single-memory-instance"></a>

向工作流添加多个 Postgres Chat Memory 节点时，默认情况下所有这些节点都访问同一个记忆实例。执行会覆盖现有记忆内容的破坏性操作时，请谨慎，例如 [Chat Memory Manager](./n8n-nodes-langchain.memorymanager.md) 节点中的覆盖全部消息操作。如果希望在工作流中使用多个记忆实例，请为不同记忆节点设置不同的会话 ID。

[^1]: 在 AI 场景中，记忆让 AI 工具能够在多次交互之间保存消息上下文。例如，与 AI 智能体持续对话时，无需在每条消息中重复提交上下文。在 n8n 中，AI 智能体节点可以使用记忆，而 AI 链不能。
