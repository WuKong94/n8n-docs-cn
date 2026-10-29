---
title: Chat 节点
description: 了解如何在 n8n 工作流中配置和使用 Chat 节点。
contentType:
- integration
- reference
priority: critical
nodeTitle: Chat 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-langchain.chat.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Chat（聊天）节点 <a href="#chat-node" id="chat-node"></a>

将 Chat 节点与 [Chat Trigger](n8n-nodes-langchain.chattrigger/README.md) 节点配合使用，向聊天发送消息，并按需等待用户响应。它支持聊天工作流中的人工参与（HITL）场景，可在一次执行内完成多轮聊天交互。Chat 节点也可用作 AI Agent 的工具。

{% hint style="info" %}
**Chat Trigger 节点**

Chat 节点要求工作流中存在 [Chat Trigger](n8n-nodes-langchain.chattrigger/README.md) 节点，并将其 [Response Mode](n8n-nodes-langchain.chattrigger/README.md#response-mode)（响应模式）设为 Using Response Nodes（使用响应节点）。
{% endhint %}

{% hint style="warning" %}
**不支持 Embedded（嵌入）模式**

Chat Trigger 节点设为 **Embedded**（嵌入）模式时，不支持 Chat 节点。嵌入模式下，请改用 [Respond to Webhook](n8n-nodes-base.respondtowebhook.md) 节点。
{% endhint %}

{% hint style="info" %}
**早期版本**

早期版本将此节点称为 Respond to Chat（响应聊天），仅使用一个 Wait for User Reply（等待用户回复）开关。现在这些功能已拆分为两种操作，并增加更多响应类型。
{% endhint %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/hitl-tools.md" %}

使用以下参数配置节点。

### Operation（操作） <a href="#operation" id="operation"></a>

Chat 节点支持以下操作：

* **Send Message**（发送消息）：向聊天发送消息，发送后工作流立即继续执行。
* **Send and Wait for Response**（发送并等待响应）：向聊天发送消息并等待用户响应，暂停工作流执行，直到用户提交响应。

选择 **Send and Wait for Response**（发送并等待响应）后，会启用[等待响应](#waiting-for-a-response)中介绍的其他参数和选项。

### Message（消息） <a href="#message" id="message"></a>

要发送到聊天的消息，两种操作都可使用此参数。

## 节点选项 <a href="#node-options" id="node-options"></a>

使用以下 **Options**（选项）进一步配置节点行为。

### Add Memory Input Connection（添加记忆输入连接） <a href="#add-memory-input-connection" id="add-memory-input-connection"></a>

选择是否将 Chat 节点的消息写入已连接的记忆。让智能体或链的[根节点](../cluster-nodes/root-nodes/README.md)与 Chat 节点共用记忆，会为这些消息附加相同的会话键，便于记录完整消息历史。

## 等待响应 <a href="#waiting-for-a-response" id="waiting-for-a-response"></a>

选择 **Send and Wait for Response**（发送并等待响应），可发送消息并暂停工作流，直到有人响应，从而在一次执行中完成多轮对话和审批流程。

### Response Type（响应类型） <a href="#response-type" id="response-type"></a>

可选择以下响应类型：

* **Free Text**（自由文本）：用户可在聊天中输入任意响应，与早期 Wait for User Reply（等待用户回复）选项行为相同。
* **Approval**（审批）：用户可使用消息内的按钮批准或拒绝，也可按需允许用户输入自定义响应。

可用参数和选项取决于所选类型。

### Free Text（自由文本）参数和选项 <a href="#free-text-parameters-and-options" id="free-text-parameters-and-options"></a>

使用 Free Text（自由文本）响应类型时，用户可输入任意消息作为响应。

**适用场景：**
- 开放式问题
- 收集详细反馈
- 请求特定信息

**选项：**
* **Limit Wait Time**（限制等待时间）：设置工作流是否在指定时间限制后自动恢复执行，可使用时间间隔或具体时间点。

### Approval（审批）参数和选项 <a href="#approval-parameters-and-options" id="approval-parameters-and-options"></a>

使用 Approval（审批）响应类型时，消息中会显示可点击的批准或拒绝按钮，与 n8n 其他人工参与（HITL）节点的模式一致。

**适用场景：**
- 简单的是／否决策
- 审批工作流
- 确认操作

使用 Approval（审批）响应类型时，可配置以下参数：

* **Type of Approval**（审批类型）：选择仅显示批准按钮，或同时显示批准和拒绝按钮。
    - **Approve Only**（仅批准）：显示一个批准按钮。
    - **Approve and Disapprove**（批准与拒绝）：显示两个按钮，为默认选项。

* **Approve Button Label**（批准按钮标签）：批准按钮显示的文本，默认为 `Approve`。

* **Disapprove Button Label**（拒绝按钮标签）：拒绝按钮显示的文本，仅在 Type of Approval（审批类型）为 Approve and Disapprove（批准与拒绝）时显示，默认为 `Disapprove`。

* **Block User Input**（阻止用户输入）：开启时阻止用户输入自定义消息；关闭时允许输入响应，默认为关闭。
    - **disabled**（关闭，默认）：用户可点击按钮或输入自定义消息；输入的文字消息会被视为附带自定义消息的拒绝。
    - **enabled**（开启）：用户只能通过按钮交互。

Approval（审批）响应类型还提供以下选项：

* **Limit Wait Time**（限制等待时间）：设置工作流是否在指定时间限制后自动恢复执行，可使用时间间隔或具体时间点。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

聊天界面的设置说明，请参阅 [Chat Trigger](n8n-nodes-langchain.chattrigger/README.md) 节点文档。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 n8n 集成模板](https://n8n.io/integrations/)，或[搜索所有模板](https://n8n.io/workflows/)

## 常见问题 <a href="#common-issues" id="common-issues"></a>

- Chat Trigger 节点的 **Mode**（模式）设为 **Embedded**（嵌入）时，不支持 Chat 节点。嵌入模式仅提供 **Respond to Webhook**（响应 Webhook）响应模式，请改用 [Respond to Webhook](n8n-nodes-base.respondtowebhook.md) 节点。
- Chat 节点不能用作子智能体的工具。
- Chat 节点不能在子工作流中使用，包括用作 AI Agent 工具的子工作流。
- 确保 Chat Trigger 节点的 Response Mode（响应模式）设为 Using Response Nodes（使用响应节点），Chat 节点才能正常工作。

Chat Trigger 节点的常见疑问或问题，请参阅 [Chat Trigger 节点常见问题](n8n-nodes-langchain.chattrigger/common-issues.md)。
