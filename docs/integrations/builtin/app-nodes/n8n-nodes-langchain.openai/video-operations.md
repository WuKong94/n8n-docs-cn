---
title: OpenAI 视频操作
description: 了解 n8n 工作流自动化平台中 OpenAI 节点的视频操作，包括操作及配置详情，以及示例和凭据信息链接。
contentType:
- integration
- reference
priority: critical
nodeTitle: OpenAI 视频操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.openai/video-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/video-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/video-operations
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# OpenAI 视频操作 <a href="#openai-video-operations" id="openai-video-operations"></a>

此操作用于在 OpenAI 中生成视频。有关 OpenAI 节点本身的更多信息，请参阅 [OpenAI](README.md)。

## Generate Video（生成视频） <a href="#generate-video" id="generate-video"></a>

此操作用于根据文本提示词生成视频。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **Video**（视频）。
- **Operation**（操作）：选择 **Generate Video**（生成视频）。
- **Model**（模型）：选择用于生成视频的模型。此版本支持 `sora-2` 和 `sora-2-pro`。
- **Prompt**（提示词）：用于生成视频的提示词。
- **Seconds**（秒数）：片段时长，单位为秒，原文给出的上限为 25。译注：实际请求须使用模型及其 API 支持的时长值，不能据此推断上限以内任意秒数都受支持。
- **Size**（尺寸）：输出分辨率，格式为宽度 x 高度。1024x1792 和 1792x1024 仅 Sora 2 Pro 支持。

### 选项 <a href="#options" id="options"></a>

- **Reference**（参考）：可选的图片参考，用于引导生成，必须以二进制数据项传入。
- **Wait Timeout**（等待超时）：等待视频生成的时间，单位为秒，默认值为 300。
- **Output Field Name**（输出字段名称）：用于存放二进制文件数据的输出字段名称，默认值为 `data`。

更多信息，请参阅[视频生成 | OpenAI](https://platform.openai.com/docs/guides/video-generation)。
