---
title: OpenAI 音频操作
description: 了解 n8n 工作流自动化平台中 OpenAI 节点的音频操作，包括操作及配置详情，以及示例和凭据信息链接。
contentType:
- integration
- reference
priority: critical
nodeTitle: OpenAI 音频操作
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# OpenAI 音频操作 <a href="#openai-audio-operations" id="openai-audio-operations"></a>

这些操作用于在 OpenAI 中生成音频，或转写、翻译录音。有关 OpenAI 节点本身的更多信息，请参阅 [OpenAI](README.md)。

## Generate Audio（生成音频） <a href="#generate-audio" id="generate-audio"></a>

此操作用于根据文本提示词创建音频。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **Audio**（音频）。
- **Operation**（操作）：选择 **Generate Audio**（生成音频）。
- **Model**（模型）：选择用于生成音频的模型。更多信息，请参阅 [TTS | OpenAI](https://platform.openai.com/docs/models/tts)。
    - **TTS-1**：优先优化速度。
    - **TTS-1-HD**：优先优化质量。
- **Text Input**（文本输入）：输入要转换为音频的文本，最多 4096 个字符。
- **Voice**（音色）：选择生成音频时使用的音色。可在[文本转语音指南 | OpenAI](https://platform.openai.com/docs/guides/text-to-speech/quickstart)中试听音色预览。

### 选项 <a href="#options" id="options"></a>

- **Response Format**（响应格式）：选择音频响应格式，可选 **MP3**（默认）、**OPUS**、**AAC**、**FLAC**、**WAV** 和 **PCM**。
- **Audio Speed**（音频速度）：输入生成音频的速度，范围为 `0.25` 到 `4.0`，默认值为 `1`。
- **Put Output in Field**（输出字段）：默认值为 `data`。输入用于存放二进制文件数据的输出字段名称。

更多信息，请参阅[创建语音 | OpenAI](https://platform.openai.com/docs/api-reference/audio/createSpeech) 文档。

## Transcribe a Recording（转写录音） <a href="#transcribe-a-recording" id="transcribe-a-recording"></a>

此操作用于将音频转写为文本。OpenAI API 限制音频文件大小为 25 MB。按原文所述的节点版本，默认使用 `whisper-1` 模型。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **Audio**（音频）。
- **Operation**（操作）：选择 **Transcribe a Recording**（转写录音）。
- **Input Data Field Name**（输入数据字段名称）：默认值为 `data`。输入包含音频文件的二进制属性名称。音频文件须采用以下格式之一：`.flac`、`.mp3`、`.mp4`、`.mpeg`、`.mpga`、`.m4a`、`.ogg`、`.wav` 或 `.webm`。

### 选项 <a href="#options" id="options"></a>

- **Language of the Audio File**（音频文件语言）：使用 [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) 代码填写输入音频的语言。此选项有助于提高准确率并减少延迟。
- **Output Randomness (Temperature)**（输出随机性：温度）：默认值为 `1.0`。调整响应的随机性，范围为 `0.0`（确定性）到 `1.0`（最大随机性）。原文建议只调整此项或 **Output Randomness (Top P)**，不要同时调整两者；但本页此音频操作的选项未列出 Top P。原文建议从中等温度（约 0.7）开始，根据输出调整：过于重复或僵硬时提高温度，过于混乱或偏离主题时降低温度。

更多信息，请参阅[创建转写 | OpenAI](https://platform.openai.com/docs/api-reference/audio/createTranscription) 文档。

## Translate a Recording（翻译录音） <a href="#translate-a-recording" id="translate-a-recording"></a>

此操作用于将音频翻译为英文。OpenAI API 限制音频文件大小为 25 MB。按原文所述的节点版本，默认使用 `whisper-1` 模型。

填写以下参数：

- **Credential to connect with**（连接所用凭据）：创建或选择已有的 [OpenAI 凭据](../../credentials/openai.md)。
- **Resource**（资源）：选择 **Audio**（音频）。
- **Operation**（操作）：选择 **Translate a Recording**（翻译录音）。
- **Input Data Field Name**（输入数据字段名称）：默认值为 `data`。输入包含音频文件的二进制属性名称。音频文件须采用以下格式之一：`.flac`、`.mp3`、`.mp4`、`.mpeg`、`.mpga`、`.m4a`、`.ogg`、`.wav` 或 `.webm`。

### 选项 <a href="#options" id="options"></a>

- **Output Randomness (Temperature)**（输出随机性：温度）：默认值为 `1.0`。调整响应的随机性，范围为 `0.0`（确定性）到 `1.0`（最大随机性）。原文建议只调整此项或 **Output Randomness (Top P)**，不要同时调整两者；但本页此音频操作的选项未列出 Top P。原文建议从中等温度（约 0.7）开始，根据输出调整：过于重复或僵硬时提高温度，过于混乱或偏离主题时降低温度。

原文在此引用[创建转写 | OpenAI](https://platform.openai.com/docs/api-reference/audio/createTranscription) 文档。译注：该链接说明转写；本节音频翻译对应的接口为 /audio/translations，返回英文文本。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误或问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。
