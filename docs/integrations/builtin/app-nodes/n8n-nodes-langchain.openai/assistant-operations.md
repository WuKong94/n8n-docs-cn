---
title: OpenAI 助手操作
description: 了解 n8n 工作流自动化平台中 OpenAI 节点的助手操作，包括操作及配置详情，以及示例和凭据信息链接。
contentType:
- integration
- reference
priority: critical
nodeTitle: OpenAI 助手操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations
layout:
  description:
    visible: false
tags:
- tag: deprecated
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# OpenAI 助手操作 <a href="#openai-assistant-operations" id="openai-assistant-operations"></a>

这些操作用于在 OpenAI 中创建、删除、列出、更新助手，或向助手发送消息。有关 OpenAI 节点本身的更多信息，请参阅 [OpenAI](README.md)。

{% hint style="warning" %}
**功能可用性**

n8n 1.117.0 引入的 OpenAI 节点 V2 已弃用助手操作。V2 支持 OpenAI Responses API，并移除了对 [Assistants API](https://platform.openai.com/docs/assistants/migration) 的支持，原文将后者描述为即将弃用的接口。译注：核对时，OpenAI 官方文档已明确 Assistants API 于 2026 年 8 月 26 日停用；以下保留为旧版节点操作说明，不代表该接口仍可使用。
{% endhint %}

## Create an Assistant（创建助手） <a href="#create-an-assistant" id="create-an-assistant"></a>

此操作用于创建新助手。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **Assistant**（助手）。
- **Operation**（操作）：选择 **Create an Assistant**（创建助手）。
- **Model**（模型）：选择要使用的模型。按原文给出的示例，需要较高智能水平时可选 `gpt-4o`，优先考虑速度和较低成本时可选 `gpt-4o-mini`。更多信息，请参阅[模型概览 | OpenAI Platform](https://platform.openai.com/docs/models)；这些模型名按原文版本保留。
- **Name**（名称）：输入助手名称，最多 256 个字符。
- **Description**（描述）：输入助手描述，最多 512 个字符。
  ```
  A virtual assistant that helps users with daily tasks, including setting reminders, answering general questions, and providing quick information.
  ```
- **Instructions**（指令）：输入助手使用的系统指令，最多 32,768 个字符。可用它指定模型回复时采用的角色。
  ```
  Always respond in a friendly and engaging manner. When a user asks a question, provide a concise answer first, followed by a brief explanation or additional context if necessary. If the question is open-ended, offer a suggestion or ask a clarifying question to guide the conversation. Keep the tone positive and supportive, and avoid technical jargon unless specifically requested by the user.
  ```
- **Code Interpreter**（代码解释器）：开启后，助手可使用代码解释器，在沙盒环境中编写和执行代码。适用于需要计算、数据分析或基于逻辑进行处理的任务。
- **Knowledge Retrieval**（知识检索）：开启后，助手可检索知识，访问外部来源或已连接的知识库。更多信息，请参阅[文件搜索 | OpenAI Platform](https://platform.openai.com/docs/assistants/tools/file-search)。
    - **Files**（文件）：选择要上传到外部知识来源的文件。使用 **Upload a File**（上传文件）操作添加更多文件。

### 选项 <a href="#options" id="options"></a>

- **Output Randomness (Temperature)**（输出随机性：温度）：调整响应的随机性，范围为 `0.0`（确定性）到 `1.0`（最大随机性）。原文建议只调整此项或 **Output Randomness (Top P)**，不要同时调整两者。可从中等温度（约 0.7）开始，再根据观察到的输出调整。如果响应过于重复或僵硬，可提高温度；如果过于混乱或偏离主题，可降低温度。默认值为 `1.0`。
- **Output Randomness (Top P)**（输出随机性：Top P）：调整 Top P 以控制助手响应的多样性。例如，`0.5` 表示仅考虑按概率加权后累计占一半的候选项。原文建议只调整此项或 **Output Randomness (Temperature)**，不要同时调整两者。默认值为 `1.0`。
- **Fail if Assistant Already Exists**（助手已存在时失败）：开启后，如果已有同名助手，操作会失败。

更多信息，请参阅[创建助手 | OpenAI](https://platform.openai.com/docs/api-reference/assistants/createAssistant) 文档。

## Delete an Assistant（删除助手） <a href="#delete-an-assistant" id="delete-an-assistant"></a>

此操作用于从账户中删除已有助手。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **Assistant**（助手）。
- **Operation**（操作）：选择 **Delete an Assistant**（删除助手）。
- **Assistant**（助手）：通过 **From list**（从列表）或 **By ID**（按 ID）选择要删除的助手。

更多信息，请参阅[删除助手 | OpenAI](https://platform.openai.com/docs/api-reference/assistants/deleteAssistant) 文档。

## List Assistants（列出助手） <a href="#list-assistants" id="list-assistants"></a>

此操作用于获取组织中的助手列表。

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **Assistant**（助手）。
- **Operation**（操作）：选择 **List Assistants**（列出助手）。

### 选项 <a href="#options" id="options"></a>

- **Simplify Output**（简化输出）：开启后，返回简化响应，而不是原始数据。此选项默认开启。

更多信息，请参阅[列出助手 | OpenAI](https://platform.openai.com/docs/api-reference/assistants/listAssistants) 文档。
  
## Message an Assistant（向助手发送消息） <a href="#message-an-assistant" id="message-an-assistant"></a>

此操作用于向助手发送消息并接收响应。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **Assistant**（助手）。
- **Operation**（操作）：选择 **Message an Assistant**（向助手发送消息）。
- **Assistant**（助手）：选择要向其发送消息的助手。
- **Prompt**（提示词）：输入要发送给助手的文本提示词或消息。
    - **Connected Chat Trigger Node**（已连接的聊天触发器节点）：自动使用前序节点 `chatInput` 字段中的输入。
    - **Define Below**（在下方定义）：通过输入静态文本，或使用表达式引用前序节点的数据，手动定义提示词。

### 选项 <a href="#options" id="options"></a>

- **Base URL**（基础 URL）：输入助手发起 API 请求时使用的基础 URL。可用于将请求定向到其他提供 OpenAI 兼容 API 的大语言模型服务端点。
- **Max Retries**（最大重试次数）：指定助手在操作失败时的重试次数。
- **Timeout**（超时）：设置助手等待响应的最长时间，单位为毫秒，以避免操作期间长时间等待。
- **Preserve Original Tools**（保留原有工具）：关闭时，移除助手关联的原有工具。可用于仅在此操作中临时移除工具。

更多信息，请参阅[助手 | OpenAI](https://platform.openai.com/docs/api-reference/assistants) 文档。

## Update an Assistant（更新助手） <a href="#update-an-assistant" id="update-an-assistant"></a>

此操作用于更新已有助手的详细信息。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **Assistant**（助手）。
- **Operation**（操作）：选择 **Update an Assistant**（更新助手）。
- **Assistant**（助手）：选择要更新的助手。

### 选项 <a href="#options" id="options"></a>

- **Code Interpreter**（代码解释器）：开启后，助手可使用代码解释器，在沙盒环境中编写和执行代码。适用于需要计算、数据分析或基于逻辑进行处理的任务。
- **Description**（描述）：输入助手描述，最多 512 个字符。
  ```
  A virtual assistant that helps users with daily tasks, including setting reminders, answering general questions, and providing quick information.
  ```
- **Instructions**（指令）：输入助手使用的系统指令，最多 32,768 个字符。可用它指定模型回复时采用的角色。
  ```
  Always respond in a friendly and engaging manner. When a user asks a question, provide a concise answer first, followed by a brief explanation or additional context if necessary. If the question is open-ended, offer a suggestion or ask a clarifying question to guide the conversation. Keep the tone positive and supportive, and avoid technical jargon unless specifically requested by the user.
  ```
- **Knowledge Retrieval**（知识检索）：开启后，助手可检索知识，访问外部来源或已连接的知识库。更多信息，请参阅[文件搜索 | OpenAI Platform](https://platform.openai.com/docs/assistants/tools/file-search)。
- **Files**（文件）：选择要上传到外部知识来源的文件。使用 [**Upload a File**](file-operations.md#upload-a-file)（上传文件）操作添加更多文件。注意，此选项只更新[代码解释器](https://platform.openai.com/docs/assistants/tools/code-interpreter)工具，不更新[文件搜索](https://platform.openai.com/docs/assistants/tools/file-search)工具。
- **Model**（模型）：选择要使用的模型。按原文给出的示例，需要较高智能水平时可选 `gpt-4o`，优先考虑速度和较低成本时可选 `gpt-4o-mini`。更多信息，请参阅[模型概览 | OpenAI Platform](https://platform.openai.com/docs/models)；这些模型名按原文版本保留。
- **Name**（名称）：输入助手名称，最多 256 个字符。
- **Remove All Custom Tools (Functions)**（移除所有自定义工具／函数）：开启后，从助手中移除所有自定义工具（函数）。
- **Output Randomness (Temperature)**（输出随机性：温度）：调整响应的随机性，范围为 `0.0`（确定性）到 `1.0`（最大随机性）。原文建议只调整此项或 **Output Randomness (Top P)**，不要同时调整两者。可从中等温度（约 0.7）开始，再根据观察到的输出调整。如果响应过于重复或僵硬，可提高温度；如果过于混乱或偏离主题，可降低温度。默认值为 `1.0`。
- **Output Randomness (Top P)**（输出随机性：Top P）：调整 Top P 以控制助手响应的多样性。例如，`0.5` 表示仅考虑按概率加权后累计占一半的候选项。原文建议只调整此项或 **Output Randomness (Temperature)**，不要同时调整两者。默认值为 `1.0`。

更多信息，请参阅[修改助手 | OpenAI](https://platform.openai.com/docs/api-reference/assistants/modifyAssistant) 文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误或问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。
