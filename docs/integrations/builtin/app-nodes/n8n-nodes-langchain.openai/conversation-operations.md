---
title: OpenAI 会话操作
contentType:
- integration
- reference
priority: critical
nodeTitle: OpenAI 会话操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.openai/conversation-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/conversation-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/conversation-operations
description: 了解 n8n 工作流自动化平台中 OpenAI 节点的会话操作，包括操作及配置详情，以及示例和凭据信息链接。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 会话操作 <a id="conversation-operations"></a>

这些操作用于在 OpenAI 中创建、获取、更新或移除会话。有关 OpenAI 节点本身的更多信息，请参阅 [OpenAI](./README.md)。

## Create a Conversation（创建会话） <a href="#create-a-conversation" id="create-a-conversation"></a>

此操作用于创建新会话。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
* **Resource**（资源）：选择 **Conversation**（会话）。
* **Operation**（操作）：选择 **Create a Conversation**（创建会话）。
* **Messages**（消息）：输入给模型的消息。`system` 角色的消息优先于 `user` 角色给出的指令；`assistant` 角色的消息会被视为模型在此前交互中生成的内容。

### 选项 <a href="#options" id="options"></a>

* **Metadata**（元数据）：用于存储结构化信息的键值对集合。每个对象最多可附加 16 对，适合添加可通过 API 或控制台搜索的自定义数据。

更多信息，请参阅[会话 | OpenAI](https://platform.openai.com/docs/api-reference/conversations/create) 文档。

## Get a Conversation（获取会话） <a href="#get-a-conversation" id="get-a-conversation"></a>

此操作用于获取已有会话。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
* **Resource**（资源）：选择 **Conversation**（会话）。
* **Operation**（操作）：选择 **Get Conversation**（获取会话）。
* **Conversation ID**（会话 ID）：要获取的会话的 ID。

更多信息，请参阅[会话 | OpenAI](https://platform.openai.com/docs/api-reference/conversations/create) 文档。

## Remove a Conversation（移除会话） <a href="#remove-a-conversation" id="remove-a-conversation"></a>

此操作用于移除已有会话。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
* **Resource**（资源）：选择 **Conversation**（会话）。
* **Operation**（操作）：选择 **Remove Conversation**（移除会话）。
* **Conversation ID**（会话 ID）：要移除的会话的 ID。

更多信息，请参阅[会话 | OpenAI](https://platform.openai.com/docs/api-reference/conversations/create) 文档。

## Update a Conversation（更新会话） <a href="#update-a-conversation" id="update-a-conversation"></a>

此操作用于更新已有会话。

填写以下参数：

* **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
* **Resource**（资源）：选择 **Conversation**（会话）。
* **Operation**（操作）：选择 **Update a Conversation**（更新会话）。
* **Conversation ID**（会话 ID）：要更新的会话的 ID。

### 选项 <a href="#options" id="options"></a>

* **Metadata**（元数据）：用于存储结构化信息的键值对集合。每个对象最多可附加 16 对，适合添加可通过 API 或控制台搜索的自定义数据。

更多信息，请参阅[会话 | OpenAI](https://platform.openai.com/docs/api-reference/conversations/create) 文档。
