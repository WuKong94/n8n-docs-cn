---
title: OpenAI 图片操作
description: 了解 n8n 工作流自动化平台中 OpenAI 节点的图片操作，包括操作及配置详情，以及示例和凭据信息链接。
contentType:
- integration
- reference
priority: critical
nodeTitle: OpenAI 图片操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# OpenAI 图片操作 <a href="#openai-image-operations" id="openai-image-operations"></a>

这些操作用于在 OpenAI 中分析或生成图片。有关 OpenAI 节点本身的更多信息，请参阅 [OpenAI](README.md)。

## Analyze Image（分析图片） <a href="#analyze-image" id="analyze-image"></a>

此操作接收图片，并回答与图片有关的问题。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **Image**（图片）。
- **Operation**（操作）：选择 **Analyze Image**（分析图片）。
- **Model**（模型）：选择要用于分析图片的模型。
- **Text Input**（文本输入）：输入针对图片的问题。
- **Input Type**（输入类型）：选择图片的输入方式，可选：
    - **Image URL(s)**（图片 URL）：输入要分析的图片的 **URL(s)**（URL），多个 URL 以逗号分隔。
    - **Binary File(s)**（二进制文件）：在 **Input Data Field Name**（输入数据字段名称）中填写包含图片的二进制属性名称。

### 选项 <a href="#options" id="options"></a>

- **Detail**（详细程度）：指定响应时间与 token 用量之间的平衡。
- **Length of Description (Max Tokens)**（描述长度：最大 token 数）：默认值为 300。token 越少，生成的图片描述越短，细节也越少。

更多信息，请参阅[图片 | OpenAI](https://platform.openai.com/docs/api-reference/images) 文档。

## Generate an Image（生成图片） <a href="#generate-an-image" id="generate-an-image"></a>

此操作用于根据文本提示词创建图片。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **Image**（图片）。
- **Operation**（操作）：选择 **Generate an Image**（生成图片）。
- **Model**（模型）：选择要用于生成图片的模型。
- **Prompt**（提示词）：输入所需图片的文本描述。对于 `dall-e-2`，最多 1000 个字符；对于 `dall-e-3`，最多 4000 个字符。

### 选项 <a href="#options" id="options"></a>

- **Quality**（质量）：生成图片的质量。**HD**（高清）可生成细节更丰富、整体一致性更高的图片，仅 `dall-e-3` 支持此选项。其他情况选择 **Standard**（标准）。
- **Resolution**（分辨率）：选择生成图片的分辨率。`dall-e-2` 选择 **1024x1024**；`dall-e-3` 模型可选择 **1024x1024**、**1792x1024** 或 **1024x1792**。
- **Style**（风格）：选择生成图片的风格，仅 `dall-e-3` 支持此选项。
    - **Natural**（自然）：生成外观更自然的图片。
    - **Vivid**（鲜明）：生成具有超写实感和戏剧效果的图片。
- **Respond with image URL(s)**（返回图片 URL）：选择是否返回图片 URL，而不是二进制文件。
- **Put Output in Field**（输出字段）：默认值为 `data`。输入用于存放二进制文件数据的输出字段名称，仅在关闭 **Respond with image URL(s)**（返回图片 URL）时可用。

更多信息，请参阅[创建图片 | OpenAI](https://platform.openai.com/docs/api-reference/images/create) 文档。

## Edit an Image（编辑图片） <a href="#edit-an-image" id="edit-an-image"></a>

此操作用于根据文本提示词编辑图片。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **Image**（图片）。
- **Operation**（操作）：选择 **Edit Image**（编辑图片）。
- **Model**（模型）：选择用于生成编辑结果的模型。支持 `dall-e-2` 和 `gpt-image-1`。
- **Prompt**（提示词）：输入希望对原始图片进行哪些编辑的文本描述。
- **Image(s)**（图片）：添加一个或多个二进制字段，将图片与提示词一起传入。每张图片必须是小于 50MB 的 png、webp 或 jpg 文件，最多可提供 16 张图片。
- **Number of Images**（图片数量）：要生成的图片数量，必须在 1 到 10 之间。
- **Size**（尺寸）：生成图片的大小和尺寸，单位为 px。
- **Quality**（质量）：生成图片的质量，可选 auto、low、medium、high、standard。仅 `gpt-image-1` 支持。
- **Output Format**（输出格式）：生成图片的返回格式，可选 png、webp 或 jpg。仅 gpt-image-1 支持。
- **Output Compression**（输出压缩）：生成图片的压缩级别（0-100%），仅 `gpt-image-1` 在使用 webp 或 jpeg 输出格式时支持。

### 选项 <a href="#options" id="options"></a>
- **Background**（背景）：设置生成图片的背景透明度，仅 `gpt-image-1` 支持。
- **Input Fidelity**（输入保真度）：控制模型为匹配输入图片的风格和特征投入多少努力，仅 `gpt-image-1` 支持。
- **Image Mask**（图片遮罩）：填写包含遮罩图片的二进制属性名称。遮罩是第二张图片，其中完全透明的区域（例如 alpha 为零的区域）表示需要编辑的位置。如果提供多张输入图片，遮罩会应用于第一张图片。遮罩必须是有效的 PNG 文件，小于 4MB，且与原图尺寸相同。
- **User**（用户）：代表最终用户的唯一标识符，可帮助 OpenAI 监控和检测滥用。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误或问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。
