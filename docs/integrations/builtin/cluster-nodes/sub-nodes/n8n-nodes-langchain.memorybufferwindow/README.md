---
title: Simple Memory（简单记忆） 节点文档
description: 了解如何在 n8n 中使用 Simple Memory（简单记忆） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: n8n-nodes-langchain.memorybufferwindow
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Simple Memory（简单记忆） 节点 <a href="#simple-memory-node" id="simple-memory-node"></a>

使用 Simple Memory 节点，在工作流中保存[^1]聊天历史记录。

本页列出了 Simple Memory 节点支持的操作，并提供更多资源的链接。

{% hint style="warning" %}
**队列模式下不要使用此节点**

如果 n8n 实例使用[队列模式](../../../../../deploy/host-n8n/configure-n8n/scaling/enable-queue-mode.md)，此节点无法在活跃的生产工作流中正常工作，因为 n8n 无法保证每次调用 Simple Memory 都由同一个工作进程处理。
{% endhint %}

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置节点：

* **Session Key**（会话键）：输入在工作流数据中存储记忆时使用的键。
* **Context Window Length**（上下文窗口长度）：输入作为上下文考虑的历史交互次数。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Simple Memory（简单记忆）集成模板](https://n8n.io/integrations/window-buffer-memory)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 短期记忆文档](https://docs.langchain.com/oss/javascript/langchain/short-term-memory)。

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见问题及建议的解决办法，请参阅[常见问题](common-issues.md)。

[^1]: 在 AI 场景中，记忆让 AI 工具能够在多次交互之间保存消息上下文。例如，与 AI 智能体持续对话时，无需在每条消息中重复提交上下文。在 n8n 中，AI 智能体节点可以使用记忆，而 AI 链不能。
