---
title: OpenAI 文本操作
description: 了解 n8n 工作流自动化平台中 OpenAI 节点的文本操作，包括操作及配置详情，以及示例和凭据信息链接。
contentType:
- integration
- reference
priority: critical
nodeTitle: OpenAI 文本操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# OpenAI 文本操作 <a href="#openai-text-operations" id="openai-text-operations"></a>

这些操作用于向 OpenAI 模型发送消息，或对文本进行违规分类。有关 OpenAI 节点本身的更多信息，请参阅 [OpenAI](README.md)。

{% hint style="info" %}
**此前的节点版本**

n8n 1.117.0 引入了支持 OpenAI Responses API 的 OpenAI 节点 V2。它将“Message a Model”（向模型发送消息）操作重命名为“Generate a Chat Completion”（生成聊天补全），以明确其使用 Chat Completions API；同时新增独立的“Generate a Model Response”（生成模型响应）操作，使用 Responses API。
{% endhint %}

## Generate a Chat Completion（生成聊天补全） <a href="#generate-a-chat-completion" id="generate-a-chat-completion"></a>

此操作通过 Chat Completions API 向 OpenAI 模型发送消息或提示词，并接收响应。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **Text**（文本）。
- **Operation**（操作）：选择 **Generate a Chat Completion**（生成聊天补全）。
- **Model**（模型）：选择要使用的模型。按原文给出的示例，需要较高智能水平时可选 `gpt-4o`，优先考虑速度和较低成本时可选 `gpt-4o-mini`。更多信息，请参阅[模型概览 | OpenAI Platform](https://platform.openai.com/docs/models)；这些模型名按原文版本保留。
- **Messages**（消息）：输入 **Text**（文本）提示词，并指定模型生成响应时使用的 **Role**（角色）。有关如何借助这些角色编写更好的提示词，请参阅[提示词工程 | OpenAI](https://platform.openai.com/docs/guides/prompt-engineering)。可选择以下角色：
    - **User**（用户）：以用户身份发送消息，并获取模型响应。
    - **Assistant**（助手）：表示模型在此前交互中生成的消息。译注：原文将此角色描述为设置语气或个性；角色本身用于标记助手消息，整体行为应通过相应的指令角色设定。
    - **System**（系统）：默认没有系统消息。可以在用户消息中定义指令，但系统消息中的指令更有效。每个会话可设置多条系统消息，用于设定模型行为，或为下一条用户消息提供上下文。
- **Simplify Output**（简化输出）：开启后，返回简化响应，而不是原始数据。
- **Output Content as JSON**（以 JSON 输出内容）：开启后，尝试以 JSON 格式返回响应。兼容 `GPT-4 Turbo`，以及 `GPT-3.5 Turbo` 系列中晚于 `gpt-3.5-turbo-1106` 的所有模型。

### 选项 <a href="#options" id="options"></a>

- **Frequency Penalty**（频率惩罚）：施加惩罚，降低模型重复类似语句的倾向，范围为 `0.0` 到 `2.0`。
- **Maximum Number of Tokens**（最大 token 数）：设置响应的最大 token 数。在标准英文文本中，一个 token 约对应四个字符。可用此选项限制输出长度。
- **Number of Completions**（补全数量）：默认值为 1。设置每个提示词要生成的补全数量。请谨慎设置，较大的数量会快速消耗 token。
- **Presence Penalty**（存在惩罚）：施加惩罚，引导模型讨论新话题，范围为 `0.0` 到 `2.0`。
- **Output Randomness (Temperature)**（输出随机性：温度）：调整响应的随机性，范围为 `0.0`（确定性）到 `1.0`（最大随机性）。原文建议只调整此项或 **Output Randomness (Top P)**，不要同时调整两者。可从中等温度（约 `0.7`）开始，再根据观察到的输出调整。如果响应过于重复或僵硬，可提高温度；如果过于混乱或偏离主题，可降低温度。默认值为 `1.0`。
- **Output Randomness (Top P)**（输出随机性：Top P）：调整 Top P 以控制助手响应的多样性。例如，`0.5` 表示仅考虑按概率加权后累计占一半的候选项。原文建议只调整此项或 **Output Randomness (Temperature)**，不要同时调整两者。默认值为 `1.0`。

更多信息，请参阅[聊天补全 | OpenAI](https://platform.openai.com/docs/api-reference/chat) 文档。

## Generate a Model Response（生成模型响应） <a href="#generate-a-model-response" id="generate-a-model-response"></a>

此操作通过 Responses API 向 OpenAI 模型发送消息或提示词，并接收响应。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **Text**（文本）。
- **Operation**（操作）：选择 **Generate a Model Response**（生成模型响应）。
- **Model**（模型）：选择要使用的模型，概览请参阅[模型概览 | OpenAI Platform](https://platform.openai.com/docs/models)。
- **Messages**（消息）：选择以下任一种 **Message Types**（消息类型）：
    - **Text**（文本）：输入 **Text**（文本）提示词，并指定模型生成响应时使用的 **Role**（角色）。有关如何借助这些角色编写更好的提示词，请参阅[提示词工程 | OpenAI](https://platform.openai.com/docs/guides/prompt-engineering)。
    - **Image**（图片）：通过图片 URL、文件 ID（使用 [OpenAI Files API](https://platform.openai.com/docs/api-reference/files)），或工作流前序节点传入的二进制数据，提供 **Image**（图片）。
    - **File**（文件）：提供受支持格式的 **File**（文件，本页所述节点版本仅支持 PDF）。可以使用文件 URL、文件 ID（通过 [OpenAI Files API](https://platform.openai.com/docs/api-reference/files)），或工作流前序节点传入的二进制数据。
    - 对于任意消息类型，都可以选择以下角色之一：
        - **User**（用户）：以用户身份发送消息，并获取模型响应。
        - **Assistant**（助手）：表示模型在此前交互中生成的消息。译注：原文将此角色描述为设置语气或个性；角色本身用于标记助手消息，整体行为应通过相应的指令角色设定。
        - **System**（系统）：默认系统消息为 `"You are a helpful assistant"`。可以在用户消息中定义指令，但系统消息中的指令更有效。本操作中，每个会话只能设置一条系统消息，用于设定模型行为，或为下一条用户消息提供上下文。
- **Simplify Output**（简化输出）：开启后，返回简化响应，而不是原始数据。

### 内置工具 <a href="#built-in-tools" id="built-in-tools"></a>
OpenAI Responses API 提供多种[内置工具](https://platform.openai.com/docs/guides/tools)，用于丰富模型响应：

- **Web Search**（网页搜索）：允许模型在生成响应前搜索网页，获取最新信息。
- **MCP Servers**（MCP 服务器）：允许模型连接远程 MCP 服务器。更多信息，请参阅[将远程 MCP 服务器用作工具](https://platform.openai.com/docs/guides/tools-connectors-mcp)。
- **File Search**（文件搜索）：允许模型在生成响应前，从此前上传文件构成的知识库中搜索相关信息。更多信息，请参阅 [OpenAI 文档](https://platform.openai.com/docs/guides/tools-file-search)。
- **Code Interpreter**（代码解释器）：允许模型在沙盒环境中编写并运行 Python 代码。

### 选项 <a href="#options" id="options"></a>

- **Maximum Number of Tokens**（最大 token 数）：设置响应的最大 token 数。在标准英文文本中，一个 token 约对应四个字符。可用此选项限制输出长度。
- **Output Randomness (Temperature)**（输出随机性：温度）：调整响应的随机性，范围为 `0.0`（确定性）到 `1.0`（最大随机性）。原文建议只调整此项或 **Output Randomness (Top P)**，不要同时调整两者。可从中等温度（约 `0.7`）开始，再根据观察到的输出调整。如果响应过于重复或僵硬，可提高温度；如果过于混乱或偏离主题，可降低温度。默认值为 `1.0`。
- **Output Randomness (Top P)**（输出随机性：Top P）：调整 Top P 以控制助手响应的多样性。例如，`0.5` 表示仅考虑按概率加权后累计占一半的候选项。原文建议只调整此项或 **Output Randomness (Temperature)**，不要同时调整两者。默认值为 `1.0`。
- **Conversation ID**（会话 ID）：此响应所属的会话。响应完成后，其输入项和输出项会自动添加到该会话。
- **Previous Response ID**（前一个响应 ID）：要从中继续交互的前一个响应的 ID，不能与 Conversation ID 同时使用。
- **Reasoning**（推理）：模型为生成响应所投入的推理强度。可返回模型推理过程的 **Summary**（摘要），例如用于调试。
- **Store**（存储）：是否存储生成的模型响应，以便后续通过 API 获取。默认值为 `true`。
- **Output Format**（输出格式）：选择将响应返回为 **Text**（文本）、指定的 **JSON Schema**，或 **JSON Object**（JSON 对象）。
- **Background**（后台）：是否以[后台模式](https://platform.openai.com/docs/guides/background)运行模型，使长时间运行的任务能够更可靠地执行。

更多信息，请参阅[响应 | OpenAI](https://platform.openai.com/docs/api-reference/responses/create) 文档。

## Classify Text for Violations（对文本进行违规分类） <a href="#classify-text-for-violations" id="classify-text-for-violations"></a>

此操作用于识别并标记可能有害的内容。OpenAI 模型会分析文本，并返回包含以下内容的响应：

- `flagged`：布尔字段，表示内容是否可能有害。
- `categories`：各分类的违规标记列表。
- `category_scores`：各分类的分数。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **Text**（文本）。
- **Operation**（操作）：选择 **Classify Text for Violations**（对文本进行违规分类）。
- **Text Input**（文本输入）：输入要判断是否违反审核政策的文本。
- **Simplify Output**（简化输出）：开启后，返回简化响应，而不是原始数据。

### 选项 <a href="#options" id="options"></a>

- **Use Stable Model**（使用稳定模型）：开启后，使用稳定版模型，而不是最新版，准确率可能略低。

更多信息，请参阅[内容审核 | OpenAI](https://platform.openai.com/docs/api-reference/moderations) 文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误或问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。
