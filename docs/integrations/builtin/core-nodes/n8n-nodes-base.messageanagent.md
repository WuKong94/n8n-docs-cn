---
title: Message an Agent 节点
description: 了解如何在 n8n 工作流中配置和使用 Message an Agent 节点。
contentType:
- integration
- reference
nodeTitle: Message an Agent 节点
layout:
  description:
    visible: false
status: preview
tags:
- tag: preview
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Message an Agent（向智能体发送消息）节点 <a id="message-an-agent-node"></a>

使用 Message an Agent 节点，从工作流向智能体发送消息，再在后续节点中使用其回复。智能体会执行自己的推理循环，调用自身的工具与技能，并将响应返回给工作流。

可以向已构建的智能体发送消息，也可以直接在节点内定义智能体。

{% hint style="info" %}
智能体功能处于预览阶段。关于构建、发布和管理智能体，请参阅[构建和管理智能体](../../../build/build-and-manage-agents/README.md)。
{% endhint %}

每条发送的消息均计为一次执行，与其他工作流执行相同。

{% hint style="info" %}
**节点版本**

本页介绍版本 3.1，部分控件在早期版本中不可用：

* 版本 1 使用列表和 ID 选择智能体，版本 2 引入智能体选择器。
* **Require Specific Output Format**（要求特定输出格式）在版本 3 中加入。
* **Session**（会话）设置在版本 3.1 中加入。

可在节点设置面板底部查看节点版本。
{% endhint %}

## 节点参数 <a id="node-parameters"></a>

### Agent（智能体） <a id="agent"></a>

选择要发送消息的智能体。

列表只显示与工作流属于同一项目的智能体。列表为空表示该项目尚无智能体；可在项目中创建一个，或将工作流移到目标智能体所在的项目。

运行哪个智能体版本，取决于工作流的执行方式：

- 手动执行和聊天执行使用智能体的当前草稿，因此测试会采用最新更改。
- 生产执行使用智能体已发布的版本。

更改智能体后，请发布它，否则生产执行仍会使用旧版本。

### Message（消息） <a id="message"></a>

输入要发送给智能体的消息，如同向他人提出请求一样描述，并使用表达式包含前置节点的数据。

例如：

```
处理订单 {{ $json.order_id }} 的退款，然后向客户确认退款已获批准。
```

### Require Specific Output Format（要求特定输出格式） <a id="require-specific-output-format"></a>

后续节点需要确定的数据结构而不是自由文本时，开启此选项。智能体会在 `structuredOutput` 字段返回符合所定义 schema 的对象。

通过 **Schema Type**（schema 类型）选择定义方式：

- **Generate From JSON Example**（从 JSON 示例生成）：在 **JSON Example**（JSON 示例）中粘贴示例对象，n8n 据此构建 schema。示例中的每个属性都会成为必填项。
- **Define Using JSON Schema**（使用 JSON Schema 定义）：在 **Output Schema**（输出 schema）中，使用 [JSON Schema](https://json-schema.org/) 格式自行编写。

{% hint style="warning" %}
结构化输出由模型提供方实施，支持程度有所不同。将所有属性设为必填可获得更可靠的结果。有些提供方会拒绝可选字段或高级关键字，另一些则完全不支持结构化输出。
{% endhint %}

## 节点选项 <a id="node-options"></a>

在 **Advanced**（高级）下选择 **Add Option**（添加选项）来添加这些选项。

### Enable Streaming（启用流式传输） <a id="enable-streaming"></a>

选择是否在智能体生成文本时流式返回，而不是等待完整回复。默认开启。

只有触发器配置为支持流式传输时，调用方才能收到流式响应。将连接的 [Chat Trigger](n8n-nodes-langchain.chattrigger/README.md) 或 [Webhook](n8n-nodes-base.webhook/README.md) 节点的 **Response Mode**（响应模式）设为 **Streaming**（流式传输）。使用其他响应模式时，工作流会等待完整回复，开启此选项也不会产生可见差异。

### Invoke Agent（调用智能体） <a id="invoke-agent"></a>

选择为所有输入数据项调用一次，还是为每个数据项分别调用：

- **Once for All Items**（所有数据项调用一次）：只调用智能体一次，智能体可读取所有输入数据项。此为默认选项。
- **Once Per Item**（每个数据项调用一次）：为每个输入数据项各调用一次。

此选项不适用于节点内定义的智能体。

### Session（会话） <a id="session"></a>

会话让智能体记住之前的消息。未使用会话时，每次执行都会开始新对话。

通过 **Session ID**（会话 ID）选择会话键的来源：

- **Connected Chat Trigger Node**（已连接的 Chat Trigger 节点）：复用直接连接的 Chat Trigger 会话。此为默认选项，因此 Chat Trigger 无需额外设置即可工作。
- **Define below**（在下方定义）：在 **Key**（键）中输入自定义键，可使用固定文本或表达式。可据此将多次执行归入同一对话，例如按客户 ID 分组。

会话键最多为 74 个字符。

### Allow Agent to Access Other Nodes' Data（允许智能体访问其他节点数据） <a id="allow-agent-to-access-other-nodes-data"></a>

选择是否向智能体提供读取工作流中其他节点执行数据的工具。默认关闭，因此智能体只能访问自身输入。

此选项不适用于节点内定义的智能体。

## 节点输出 <a id="node-output"></a>

每次调用智能体，节点返回一个数据项，包含以下字段：

| 字段 | 说明 |
|-------|-------------|
| `text` | 智能体的响应。 |
| `structuredOutput` | 开启 **Require Specific Output Format**（要求特定输出格式）时，返回符合 schema 的对象，否则为 `null`。 |
| `usage` | 本次调用的 token 用量。 |
| `toolCalls` | 智能体生成响应时调用的工具。 |
| `finishReason` | 智能体停止的原因。 |
| `session` | 本次调用所在的会话。 |

{% hint style="info" %}
节点版本 1 使用 `response` 字段返回响应，版本 2 将其重命名为 `text`。仍使用版本 1 的已有工作流会保留旧字段名称。
{% endhint %}

## 将节点用作工具 <a id="use-the-node-as-a-tool"></a>

此节点也提供 **Message an Agent Tool**（向智能体发送消息工具）形式，让 AI Agent 将工作交给你的智能体。将其连接到 AI Agent 节点的 **Tool**（工具）输入，并按同样方式配置。

## 相关资源 <a id="related-resources"></a>

* [构建和管理智能体](../../../build/build-and-manage-agents/README.md)
* [AI Agent 节点](../cluster-nodes/root-nodes/n8n-nodes-langchain.agent/README.md)
* [Execute Sub-workflow 节点](n8n-nodes-base.executeworkflow.md)

## 常见问题 <a id="common-issues"></a>

以下是 Message an Agent 节点的常见错误和问题，以及解决或排查步骤。

### 智能体列表为空 <a id="the-agent-list-is-empty"></a>

**Agent**（智能体）列表只显示工作流所属项目中的智能体，其他项目的智能体不会出现。

在同一项目中创建智能体，或将工作流移到智能体所在的项目。

### Agent not found or not accessible（找不到或无法访问智能体） <a id="agent-not-found-or-not-accessible"></a>

节点只能访问工作流所属项目中的智能体。如果智能体已被删除，或工作流与智能体分属不同项目，就会出现此错误。

检查智能体是否仍存在于与工作流相同的项目中。

### Session ID must be at most 74 characters（会话 ID 最多为 74 个字符） <a id="session-id-must-be-at-most-74-characters"></a>

n8n 会将项目 ID 与会话 ID 组合成键来存储会话，该存储值有固定长度限制。

缩短 **Key**（键）中的值。如果映射了前置数据中的较长 ID，请先计算哈希或截短。

### 提示词为空 <a id="the-prompt-is-empty"></a>

**Message**（消息）解析为空值或非文本内容时，节点返回 `Prompt cannot be empty`。

检查 **Message**（消息）中的表达式。返回对象或数字的表达式会被解析为空提示词，因此应先转换为文本。
