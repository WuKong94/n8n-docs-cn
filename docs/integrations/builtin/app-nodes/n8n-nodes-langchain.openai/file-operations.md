---
title: OpenAI 文件操作
description: 了解 n8n 工作流自动化平台中 OpenAI 节点的文件操作，包括操作及配置详情，以及示例和凭据信息链接。
contentType:
- integration
- reference
priority: critical
nodeTitle: OpenAI 文件操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# OpenAI 文件操作 <a href="#openai-file-operations" id="openai-file-operations"></a>

这些操作用于在 OpenAI 中删除、列出和上传文件。有关 OpenAI 节点本身的更多信息，请参阅 [OpenAI](README.md)。

## Delete a File（删除文件） <a href="#delete-a-file" id="delete-a-file"></a>

此操作用于从服务器删除文件。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **File**（文件）。
- **Operation**（操作）：选择 **Delete a File**（删除文件）。
- **File**（文件）：输入要用于此操作的文件 ID，或从下拉列表中选择文件名称。

更多信息，请参阅[删除文件 | OpenAI](https://platform.openai.com/docs/api-reference/files/delete) 文档。

## List Files（列出文件） <a href="#list-files" id="list-files"></a>

此操作用于列出用户所属组织中的文件。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **File**（文件）。
- **Operation**（操作）：选择 **List Files**（列出文件）。

### 选项 <a href="#options" id="options"></a>

- **Purpose**（用途）：仅返回具有指定用途的文件。选择 **Assistants** 可仅返回与 Assistants 和 Message 操作相关的文件；选择 **Fine-Tune** 可返回与[微调](https://platform.openai.com/docs/api-reference/fine-tuning)相关的文件。

更多信息，请参阅[列出文件 | OpenAI](https://platform.openai.com/docs/api-reference/files/list) 文档。

## Upload a File（上传文件） <a href="#upload-a-file" id="upload-a-file"></a>

此操作用于上传文件，上传后的文件可用于多种操作。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **File**（文件）。
- **Operation**（操作）：选择 **Upload a File**（上传文件）。
- **Input Data Field Name**（输入数据字段名称）：默认值为 `data`。输入包含文件的二进制属性名称。单个文件最大 512 MB；对于原文所述的旧版 Assistants 用途，还需满足 200 万 token 的上限。译注：文件大小和 token 数是同时适用的不同限制，不能任选其一。

### 选项 <a href="#options" id="options"></a>

- **Purpose**（用途）：输入上传文件的预期用途。**Assistants** 用于与 Assistants 和 Message 操作相关的文件；**Fine-Tune** 用于[微调](https://platform.openai.com/docs/api-reference/fine-tuning)。

更多信息，请参阅[上传文件 | OpenAI](https://platform.openai.com/docs/api-reference/files/create) 文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误或问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。
