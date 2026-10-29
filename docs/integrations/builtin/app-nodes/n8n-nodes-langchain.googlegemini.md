---
title: Google Gemini 节点文档
description: 了解如何在 n8n 中使用 Google Gemini 节点，并按照技术文档将 Google Gemini 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Google Gemini 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.googlegemini.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.googlegemini
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.googlegemini
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Gemini 节点 <a href="#google-gemini-node" id="google-gemini-node"></a>

{% hint style="info" %}
在 n8n Cloud 上，可使用 [Gateway 额度](../../../deploy/use-n8n-cloud/gateway-credits/README.md)运行 Google Gemini 节点，代替自己的 Google API 密钥。在节点的凭据字段中选择 **Use Gateway credits**（使用 Gateway 额度），即可在没有 Google 账户的情况下运行节点。
{% endhint %}

使用 Google Gemini 节点自动处理 Google Gemini 中的工作，并将其与其他应用集成。n8n 内置支持多种 Google Gemini 功能，包括处理音频、视频、图像、文档和文件，以进行分析、生成和转写。

本页列出了 Google Gemini 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Google Gemini(PaLM) 凭据文档](../credentials/googleai.md)。
{% endhint %}


## 操作 <a href="#operations" id="operations"></a>

* Audio:（音频）
    * Analyze Audio: Take in audio and answer questions about it.（分析音频：接收音频并回答相关问题）
    * Transcribe a Recording: Transcribes audio into text.（转写录音：将音频转写为文本）
* Document:（文档）
    * Analyze Document: Take in documents and answer questions about them.（分析文档：接收文档并回答相关问题）
* File Search:（文件搜索）
    * Create File Search Store: Create a new File Search store for RAG (Retrieval Augmented Generation)（创建文件搜索存储库，用于 RAG（检索增强生成））
    * Delete File Search Store: Delete File Search Store（删除文件搜索存储库）
    * List File Search Stores: List all File Search stores owned by the user（列出用户拥有的所有文件搜索存储库）
    * Upload to File Search Store: Upload a file to a File Search store for RAG (Retrieval Augmented Generation)（将文件上传到文件搜索存储库，用于 RAG（检索增强生成））
* Image:（图像）
    * Analyze Image: Take in images and answer questions about them.（分析图像：接收图像并回答相关问题）
    * Generate an Image: Creates an image from a text prompt.（生成图像：根据文本提示词创建图像）
    * Edit Image: Upload one or more images and apply edits based on a prompt（编辑图像：上传一张或多张图像，并根据提示词修改）
* Media File:（媒体文件）
    * Upload Media File: Upload a file to the Google Gemini API for later user.（上传媒体文件：将文件上传到 Google Gemini API，供后续使用）
* Text:（文本）
    * Message a Model: Create a completion with a Google Gemini model.（向模型发送消息：通过 Google Gemini 模型生成补全）
* Video:（视频）
    * Analyze Video: Take in videos and answer questions about them.（分析视频：接收视频并回答相关问题）
    * Generate a Video: Creates a video from a text prompt.（生成视频：根据文本提示词创建视频）
    * Download Video: Download a generated video from the Google Gemini API using a URL.（下载视频：通过 URL 从 Google Gemini API 下载生成的视频）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Google Gemini 集成模板](https://n8n.io/integrations/google-gemini)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>


有关该服务的更多信息，请参阅 [Google Gemini 文档](https://ai.google.dev/gemini-api/docs)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
