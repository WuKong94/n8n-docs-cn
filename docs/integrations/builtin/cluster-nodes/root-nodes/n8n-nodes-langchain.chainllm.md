---
title: Basic LLM Chain（基础 LLM 链） 节点文档
description: 了解如何在 n8n 中使用 Basic LLM Chain（基础 LLM 链） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: critical
nodeTitle: Basic LLM Chain（基础 LLM 链） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Basic LLM Chain（基础 LLM 链） 节点 <a href="#basic-llm-chain-node" id="basic-llm-chain-node"></a>

使用 Basic LLM Chain 节点，设置模型使用的提示词，也可为响应配置解析器。

本页列出了 Basic LLM Chain 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Basic LLM Chain 集成](https://n8n.io/integrations/basic-llm-chain/)页面。
{% endhint %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

### Prompt（提示词） <a href="#prompt" id="prompt"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/prompt.md" %}

### Require Specific Output Format（要求指定输出格式） <a href="#require-specific-output-format" id="require-specific-output-format"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/output-format.md" %}

## Chat Messages（聊天消息） <a href="#chat-messages" id="chat-messages"></a>

使用聊天模型时，可通过 **Chat Messages**（聊天消息）设置消息。

如果未连接聊天模型，n8n 会忽略这些选项。选择节点使用的 **Type Name or ID**（类型名称或 ID）：

#### AI <a href="#ai" id="ai"></a>

在 **Message**（消息）字段中输入预期响应的示例。模型将尝试以同样的方式回复消息。

#### System（系统） <a href="#system" id="system"></a>

输入随用户输入一同发送的系统 **Message**（消息），为模型应该执行的操作提供指引。

可使用此选项定义语气等，例如：`Always respond talking like a pirate`。

#### User（用户） <a href="#user" id="user"></a>

输入用户输入示例。与 AI 选项配合使用，有助于改善智能体的输出。两者共同为模型提供可遵循的输入及预期响应（**AI Message**）示例。

选择以下一种输入类型：

* **Text**（文本）：以文本 **Message**（消息）的形式输入用户输入示例。
* **Image (Binary)**（图像，二进制）：选择前一个节点的二进制输入。输入 **Image Data Field Name**（图像数据字段名称），指定前一个节点中包含图像数据的二进制字段。
* **Image (URL)**（图像，URL）：通过 URL 输入图像，填写 **Image URL**（图像 URL）。

对于这两种 **Image**（图像）类型，可选择 **Image Details**（图像细节）以控制模型如何处理图像并生成对图像的文字理解。可选：

* **Auto**（自动）：模型使用自动设置，根据输入图像的大小决定采用 Low 还是 High 设置。
* **Low**（低）：模型接收图像的 512px × 512px 低分辨率版本，并使用 65 个 token 的预算表示图像。这样 API 可更快返回响应，消耗更少的输入 token。适用于无需高细节的场景。
* **High**（高）：模型可以访问低分辨率图像，然后根据输入图像大小创建 512px 正方形的细节裁剪图。每个细节裁剪图使用两倍的 token 预算（65 个 token），总计 129 个 token。适用于需要高细节的场景。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Basic LLM Chain（基础 LLM 链） 集成模板](https://n8n.io/integrations/basic-llm-chain)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 模型文档](https://docs.langchain.com/oss/javascript/langchain/models)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}


## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下列出 Basic LLM Chain 节点的常见错误和问题，以及解决或排查步骤。

### 未指定提示词错误 <a href="#no-prompt-specified-error" id="no-prompt-specified-error"></a>

**Prompt**（提示词）为空或无效时，会显示此错误。

以下两种情况之一可能导致此错误：

1. **Prompt**（提示词）设为 **Define below**（在下方定义），但未在 **Text**（文本）字段中输入内容。
    * 解决方法是在 **Text**（文本）字段中输入有效提示词。
2. **Prompt**（提示词）设为 **Connected Chat Trigger Node**（已连接的聊天触发器节点），但传入数据中没有名为 `chatInput` 的字段。
    * 节点需要 `chatInput` 字段。如果前一个节点没有此字段，请添加 [Edit Fields (Set)](../../core-nodes/n8n-nodes-base.set.md) 节点，将传入字段名称改为 `chatInput`。
