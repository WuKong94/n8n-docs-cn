---
title: Redis Chat Memory（Redis 聊天记忆） 节点文档
description: 了解如何在 n8n 中使用 Redis Chat Memory（Redis 聊天记忆） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Redis Chat Memory（Redis 聊天记忆） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Redis Chat Memory（Redis 聊天记忆） 节点 <a href="#redis-chat-memory-node" id="redis-chat-memory-node"></a>

使用 Redis Chat Memory 节点，将 Redis 用作记忆[^1]服务器。

本页列出了 Redis Chat Memory 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Redis 凭据文档](../../credentials/redis.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Session Key**（会话键）：输入在工作流数据中存储记忆时使用的键。
* **Session Time To Live**（会话生存时间）：设置会话在指定秒数后过期。
* **Context Window Length**（上下文窗口长度）：输入作为上下文考虑的历史交互次数。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Redis Chat Memory（Redis 聊天记忆） 集成模板](https://n8n.io/integrations/redis-chat-memory)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 单个记忆实例 <a href="#single-memory-instance" id="single-memory-instance"></a>

向工作流添加多个 Redis Chat Memory 节点时，默认情况下所有这些节点都访问同一个记忆实例。执行会覆盖现有记忆内容的破坏性操作时，请谨慎，例如 [Chat Memory Manager](./n8n-nodes-langchain.memorymanager.md) 节点中的覆盖全部消息操作。如果希望在工作流中使用多个记忆实例，请为不同记忆节点设置不同的会话 ID。

[^1]: 在 AI 场景中，记忆让 AI 工具能够在多次交互之间保存消息上下文。例如，与 AI 智能体持续对话时，无需在每条消息中重复提交上下文。在 n8n 中，AI 智能体节点可以使用记忆，而 AI 链不能。
