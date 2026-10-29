---
title: OpenAI 节点
description: 了解如何在 n8n 中使用 OpenAI 节点，并将其集成到工作流。
contentType:
- integration
- reference
priority: critical
search:
  boost: 3
nodeTitle: n8n-nodes-langchain.openai
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.openai/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# OpenAI 节点 <a href="#openai-node" id="openai-node"></a>

{% hint style="info" %}
在 n8n Cloud 中，可以使用 [Gateway 额度](../../../../deploy/use-n8n-cloud/gateway-credits/README.md)运行 OpenAI 节点，无需提供自己的 OpenAI API 密钥。在节点的凭据字段中选择 **Use Gateway credits**（使用 Gateway 额度），即可在没有 OpenAI 账户的情况下运行节点。
{% endhint %}

使用 OpenAI 节点自动处理 OpenAI 中的工作，并将其与其他应用集成。n8n 内置支持多种 OpenAI 功能，包括创建图片和助手，以及与模型对话。

本页列出了 OpenAI 节点支持的操作，并提供更多资源的链接。

{% hint style="warning" %}
**功能可用性**

从 n8n 1.117.0 起可使用 OpenAI 节点 V2。它支持 OpenAI Responses API，并移除了对 [Assistants API](https://platform.openai.com/docs/assistants/migration) 的支持，原文将后者描述为 OpenAI 已宣布计划退役的接口。译注：核对时，OpenAI 官方文档已明确 Assistants API 于 2026 年 8 月 26 日停用；本文保留的助手内容属于旧版节点说明。

从 n8n 1.29.0 起，OpenAI 节点取代 OpenAI assistant 节点。
{% endhint %}

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [OpenAI 凭据](../../credentials/openai.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

- **Text**（文本）
    - [**Generate a Chat Completion**](text-operations.md#generate-a-chat-completion)（生成聊天补全）
    - [**Generate a Model Response**](text-operations.md#generate-a-model-response)（生成模型响应）
    - [**Classify Text for Violations**](text-operations.md#classify-text-for-violations)（对文本进行违规分类）
- **Image**（图片）
    - [**Analyze Image**](image-operations.md#analyze-image)（分析图片）
    - [**Generate an Image**](image-operations.md#generate-an-image)（生成图片）
    - [**Edit an Image**](image-operations.md#edit-an-image)（编辑图片）
- **Audio**（音频）
    - [**Generate Audio**](audio-operations.md#generate-audio)（生成音频）
    - [**Transcribe a Recording**](audio-operations.md#transcribe-a-recording)（转写录音）
    - [**Translate a Recording**](audio-operations.md#translate-a-recording)（翻译录音）
- **File**（文件）
    - [**Delete a File**](file-operations.md#delete-a-file)（删除文件）
    - [**List Files**](file-operations.md#list-files)（列出文件）
    - [**Upload a File**](file-operations.md#upload-a-file)（上传文件）
- **Video**（视频）
    - [**Generate a Video**](video-operations.md#generate-video)（生成视频）
- **Conversation**（会话）
    - [**Create a Conversation**](conversation-operations.md#create-a-conversation)（创建会话）
    - [**Get a Conversation**](conversation-operations.md#get-a-conversation)（获取会话）
    - [**Update a Conversation**](conversation-operations.md#update-a-conversation)（更新会话）
    - [**Remove a Conversation**](conversation-operations.md#remove-a-conversation)（移除会话）


## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-langchain.openai 集成模板](https://n8n.io/integrations/openai)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [OpenAI 文档](https://beta.openai.com/docs/introduction)。

有关助手工作方式的更多信息，请参阅 [OpenAI 助手文档](https://platform.openai.com/docs/assistants/how-it-works/objects)。

有关速率限制的处理方法，请参阅[处理速率限制](../../handle-rate-limits.md)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

## 为 OpenAI 助手使用工具 <a href="#using-tools-with-openai-assistants" id="using-tools-with-openai-assistants"></a>

部分操作允许连接工具。[工具](../../../../build/integrate-ai/understand-ai-components/how-tools-work.md)类似于扩展组件，可供 AI 访问额外的上下文或资源。

选择 **Tools**（工具）连接器，可浏览可用工具并添加。

添加工具连接后，OpenAI 节点会成为[根节点](#user-content-fn-1)[^1]，从而与工具子节点[^3]组成一个[集群节点](#user-content-fn-2)[^2]。有关集群节点和根节点的更多信息，请参阅[节点类型](../../node-types.md#cluster-nodes)。

### 支持工具连接器的操作 <a href="#operations-that-support-tool-connectors" id="operations-that-support-tool-connectors"></a>

- **Text**（文本）
    - [**Generate a Chat Completion**](text-operations.md#generate-a-chat-completion)（生成聊天补全）
    - [**Generate a Model Response**](text-operations.md#generate-a-model-response)（生成模型响应）

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见疑问或问题及建议的解决方法，请参阅[常见问题](common-issues.md)。

<a id="user-content-fn-1"></a>
[^1]: 每个 n8n 集群节点包含一个根节点，用于定义集群的主要功能。一个或多个子节点连接到根节点，以扩展其功能。
<a id="user-content-fn-2"></a>
[^2]: 在 n8n 中，集群节点是协同为工作流提供功能的一组节点，由根节点和一个或多个扩展其功能的子节点组成。
[^3]: n8n 集群节点由根节点及连接到它的一个或多个子节点组成。子节点扩展根节点的功能，可用于访问特定服务或资源，或提供计算器等专用处理能力。
