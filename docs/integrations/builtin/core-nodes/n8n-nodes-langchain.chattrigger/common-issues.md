---
title: Chat Trigger 节点常见问题
description: 了解 n8n 中 Chat Trigger 节点的常见问题、排查步骤及建议的解决方法。
contentType:
- integration
- reference
priority: high
nodeTitle: Chat Trigger 节点常见问题
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/common-issues
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/common-issues
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Chat Trigger 节点常见问题 <a href="#chat-trigger-node-common-issues" id="chat-trigger-node-common-issues"></a>

本页介绍 [Chat Trigger 节点](README.md)的常见错误和问题，以及解决或排查步骤。

## 从网站向嵌入式 Chat Trigger 传递数据 <a href="#pass-data-from-a-website-to-an-embedded-chat-trigger-node" id="pass-data-from-a-website-to-an-embedded-chat-trigger-node"></a>

在网站中[嵌入](https://www.npmjs.com/package/@n8n/chat) Chat Trigger 时，可能需要传递额外信息，例如保存在网站 cookie 中的用户 ID。

在嵌入聊天窗口中，通过 `metadata` 字段传递额外信息，将该字段放入传给 `createChat` 函数的 JSON 对象中。译注：原文下方 JavaScript 示例在 metadata 对象后多写了分号，应移除该分号或改为逗号，否则会出现语法错误。此处保留原始代码供对照：

```javascript
createChat({
	webhookUrl: 'YOUR_PRODUCTION_WEBHOOK_URL',
	metadata: {
		'YOUR_KEY': 'YOUR_DATA'
	};
});
```

`metadata` 字段可包含任意数据，与其他输出数据一起出现在 Chat Trigger 输出中。后续节点可按通常方式，使用 n8n 的[数据处理功能](../../../../build/work-with-data/README.md)查询和处理这些数据。

## Chat Trigger 无法获取先前消息 <a href="#chat-trigger-node-doesnt-fetch-previous-messages" id="chat-trigger-node-doesnt-fetch-previous-messages"></a>

配置 Chat Trigger 时，会话加载设置不正确可能导致无法获取先前消息，通常表现为 `workflow could not be started!` 错误。

Chat Trigger 的 **Load Previous Session**（加载先前会话）通过 `sessionID` 获取先前的聊天消息。将 **Load Previous Session** 设为 **From memory**（从记忆加载）时，通常最好为 Chat Trigger 和 Agent [连接同一个记忆节点](README.md#load-previous-session)：

1. 在 **Chat Trigger** 节点中，将 **Load Previous Session**（加载先前会话）设为 **From Memory**（从记忆加载）。仅在聊天已公开时，此选项才可见。
2. 将 **Simple Memory**（简单记忆）节点连接到 **Memory**（记忆）连接口。
3. 将同一个 **Simple Memory**（简单记忆）节点连接到 **Memory**（记忆）连接口，该连接口位于 **Agent**（智能体）节点上。
4. 在 **Simple Memory**（简单记忆）节点中，将 **Session ID**（会话 ID）设为 **Connected Chat Trigger Node**（已连接的 Chat Trigger 节点）。

如果要将记忆节点的 **Session ID**（会话 ID）设为 **Define below**（在下方定义），可考虑为 Chat Trigger 和 Agent 分别连接不同的记忆节点。

如果通过表达式获取会话 ID，同一表达式必须能用于连接到该记忆节点的每个节点。如果表达式无法适用于所有需要记忆的节点，可能需要分别使用记忆节点，为每个节点自定义会话 ID 表达式。
