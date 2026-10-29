---
title: MiniMax 节点
contentType:
- integration
- reference
nodeTitle: MiniMax 节点
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.minimax.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.minimax
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.minimax
description: 在 n8n 中调用 MiniMax AI 模型，了解如何将 MiniMax 集成到工作流以生成图片和将文本合成为语音。
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


# MiniMax <a id="minimax"></a>

{% hint style="info" %}
在 n8n Cloud 中，可以使用 [Gateway 额度](../../../deploy/use-n8n-cloud/gateway-credits/README.md)运行 MiniMax 节点，无需提供自己的 MiniMax API 密钥。在节点的凭据字段中选择 **Use Gateway credits**（使用 Gateway 额度），即可在没有 MiniMax 账户的情况下运行节点。
{% endhint %}

MiniMax 节点将 n8n 工作流连接到 MiniMax AI 模型。使用它根据文本提示词生成图片、合成语音、根据文本或图片创建视频，以及向 MiniMax 语言模型发送消息。

{% hint style="info" %}
**凭据**

有关此节点的身份验证信息，请参阅 [MiniMax 凭据文档](../credentials/minimax.md)。
{% endhint %}

## 资源与操作 <a href="#resources-and-operations" id="resources-and-operations"></a>

* **Audio**（音频）：使用 MiniMax 语音合成模型，将文本转换为语音。
* **Image**（图片）：根据文本提示词生成图片。
* **Text**（文本）：向 MiniMax 语言模型发送消息并接收响应。
* **Video**（视频）：根据文本提示词或首帧图片生成视频。

### Text to speech（文本转语音） <a href="#text-to-speech" id="text-to-speech"></a>

使用 MiniMax 语音合成模型，将文本转换为语音。

**参数**

* **Model**（模型；类型：options；字段：`modelId`）：要使用的语音合成模型。默认值：`speech-2.8-hd`。
* **Text**（文本；类型：string；字段：`text`）：要转换为语音的文本，最多 10,000 个字符，必填。
* **Voice ID**（音色 ID；类型：string；字段：`voiceId`）：合成语音使用的音色。可在 [MiniMax 文档](https://platform.minimax.io/docs/faq/system-voice-id)中浏览可用音色。默认值：`English_Graceful_Lady`。必填。
* **Download Audio**（下载音频；类型：boolean；字段：`downloadAudio`）：是否将生成的音频下载为二进制数据。关闭时，节点仅返回音频 URL。默认值：`true`。

**选项**

* **Audio Format**（音频格式；类型：options；字段：`audioFormat`）：输出音频格式，可选 MP3、PCM、FLAC、WAV。节点仅在非流式模式下支持 WAV。默认值：`mp3`。
* **Emotion**（情绪；类型：options；字段：`emotion`）：应用于合成语音的情绪。模型会自动选择最自然的情绪。默认值：`calm`。
* **Language Boost**（语言增强；类型：options；字段：`languageBoost`）：提高特定语言的识别准确率。默认值：`auto`。
* **Pitch**（音调；类型：number；字段：`pitch`）：调整语音的音调，范围为 –12 到 12。`0` 表示保持原始音调。默认值：`0`。
* **Speed**（语速；类型：number；字段：`speed`）：语速，范围为 0.5 到 2。值越高，语速越快。默认值：`1`。
* **Volume**（音量；类型：number；字段：`volume`）：音量，范围为 0.1 到 10。值越高，音量越大。默认值：`1`。

### Generate an image（生成图片） <a href="#generate-an-image" id="generate-an-image"></a>

使用 MiniMax 图片生成模型，根据文本提示词创建图片。

**参数**

* **Model**（模型；类型：options；字段：`modelId`）：要使用的图片生成模型。默认值：`image-01`。
* **Prompt**（提示词；类型：string；字段：`prompt`）：待生成图片的文本描述，最多 1500 个字符，必填。
* **Aspect Ratio**（宽高比；类型：options；字段：`aspectRatio`）：生成图片的宽高比。可选项包括 1:1、16:9、9:16、4:3、3:4、3:2、2:3 和 21:9。默认值：`1:1`。
* **Number of Images**（图片数量；类型：number；字段：`numberOfImages`）：每次请求生成的图片数量，范围为一到九张。默认值：`1`。
* **Download Image**（下载图片；类型：boolean；字段：`downloadImage`）：是否将生成的图片下载为二进制数据。关闭时，节点仅返回图片 URL。默认值：`true`。

**选项**

* **Prompt Optimizer**（提示词优化器；类型：boolean；字段：`promptOptimizer`）：是否自动优化提示词，以获得更好的结果。默认值：`false`。
* **Seed**（随机种子；类型：number；字段：`seed`）：用于复现输出的随机种子。相同种子配合相同参数会生成相同的图片。默认值：`0`。

### Message a model（向模型发送消息） <a href="#message-a-model" id="message-a-model"></a>

向 MiniMax 语言模型发送一条或多条消息，并接收其响应。

**参数**

* **Model**（模型；类型：options；字段：`modelId`）：要使用的语言模型。默认值：`MiniMax-M2.7`。
* **Messages**（消息；类型：fixedCollection；字段：`messages`）：组成对话的一条或多条消息。每条消息包含：
  * **Prompt**（提示词；类型：string；字段：`content`）：消息的文本内容。
  * **Role**（角色；类型：options；字段：`role`）：消息发送者的角色。使用 `user` 发送消息并接收响应，或使用 `assistant` 设置模型的语气或角色。
* **Simplify Output**（简化输出；类型：boolean；字段：`simplify`）：开启时，节点返回简化响应，而不是完整的原始 API 输出。默认值：`true`。

**选项**

* **Hide Thinking**（隐藏推理内容；类型：boolean；字段：`hideThinking`）：从响应中移除思维链推理内容，仅返回最终答案。默认值：`true`。
* **Maximum Number of Tokens**（最大 token 数；类型：number；字段：`maxTokens`）：最多生成的 token 数。默认值：`1024`。
* **Max Tool Calls Iterations**（最大工具调用迭代次数；类型：number；字段：`maxToolsIterations`）：模型停止前最多执行的工具迭代轮数。一轮迭代可以包含多次工具调用。设为 `0` 表示不限制。默认值：`15`。
* **Output Randomness (Temperature)**（输出随机性（温度）；类型：number；字段：`temperature`）：控制输出的随机性。值越低，输出越确定，也越容易重复。范围：0–1。默认值：`0.7`。
* **Output Randomness (Top P)**（输出随机性（Top P）；类型：number；字段：`topP`）：采样时考虑的 token 的最大累计概率。范围：0–1。默认值：`0.95`。
* **System Message**（系统消息；类型：string；字段：`system`）：用于引导模型行为和语气的系统级指令。

### Generate video from text（根据文本生成视频） <a href="#generate-video-from-text" id="generate-video-from-text"></a>

使用 MiniMax 视频生成模型，根据文本提示词生成视频。

**参数**

* **Model**（模型；类型：options；字段：`modelId`）：要使用的视频生成模型。默认值：`MiniMax-Hailuo-2.3`。
* **Prompt**（提示词；类型：string；字段：`prompt`）：视频的文本描述，最多 2000 个字符。可以使用 `[command]` 语法控制镜头运动，例如 `[Push in]` 或 `[Pan left]`。必填。
* **Duration (Seconds)**（时长（秒）；类型：options；字段：`duration`）：生成视频的时长，可选 6 秒或 10 秒。默认值：`6`。
* **Resolution**（分辨率；类型：options；字段：`resolution`）：生成视频的分辨率，可用选项取决于模型。可选项：720P、768P、1080P。默认值：`768P`。
* **Download Video**（下载视频；类型：boolean；字段：`downloadVideo`）：是否将生成的视频下载为二进制数据。关闭时，节点仅返回视频 URL。默认值：`true`。

**选项**

* **Prompt Optimizer**（提示词优化器；类型：boolean；字段：`promptOptimizer`）：是否自动优化提示词，以获得更好的结果。默认值：`true`。

### Generate video from image（根据图片生成视频） <a href="#generate-video-from-image" id="generate-video-from-image"></a>

以一张图片作为首帧生成视频。

**参数**

* **Model**（模型；类型：options；字段：`modelId`）：要使用的视频生成模型。默认值：`MiniMax-Hailuo-2.3`。
* **Image Input Type**（图片输入类型；类型：options；字段：`imageInputType`）：首帧图片的提供方式，可选 URL 或 Binary File（二进制文件）。默认值：`url`。
* **Image URL**（图片 URL；类型：string；字段：`imageUrl`）：首帧图片的公开 URL，支持最大 20MB 的 JPG、JPEG、PNG 和 WebP 文件。**Image Input Type**（图片输入类型）为 `URL` 时显示。必填。
* **Input Data Field Name**（输入数据字段名称；类型：string；字段：`binaryPropertyName`）：包含图片二进制数据的输入字段名称。**Image Input Type**（图片输入类型）为 `Binary File` 时显示。默认值：`data`。必填。
* **Prompt**（提示词；类型：string；字段：`prompt`）：可选的视频文本描述，最多 2000 个字符。可以使用 `[command]` 语法控制镜头运动，例如 `[Zoom in]`。
* **Duration (Seconds)**（时长（秒）；类型：options；字段：`duration`）：生成视频的时长，可选 6 秒或 10 秒。默认值：`6`。
* **Resolution**（分辨率；类型：options；字段：`resolution`）：生成视频的分辨率，可用选项取决于模型。可选项：512P、720P、768P、1080P。默认值：`768P`。
* **Download Video**（下载视频；类型：boolean；字段：`downloadVideo`）：是否将生成的视频下载为二进制数据。关闭时，节点仅返回视频 URL。默认值：`true`。

**选项**

* **Prompt Optimizer**（提示词优化器；类型：boolean；字段：`promptOptimizer`）：是否自动优化提示词。默认值：`true`。
* **Last Frame Image Input Type**（尾帧图片输入类型；类型：options；字段：`lastFrameInputType`）：提供尾帧图片以生成首尾帧视频。仅 MiniMax-Hailuo-2.3 和 MiniMax-Hailuo-02 支持此选项。默认值：`none`。
  * **Last Frame Image URL**（尾帧图片 URL；类型：string；字段：`lastFrameImageUrl`）：尾帧图片的公开 URL。**Last Frame Image Input Type**（尾帧图片输入类型）为 `URL` 时显示。
  * **Last Frame Data Field Name**（尾帧数据字段名称；类型：string；字段：`lastFrameBinaryPropertyName`）：包含尾帧图片的二进制字段名称。**Last Frame Image Input Type**（尾帧图片输入类型）为 `Binary File` 时显示。默认值：`lastFrame`。
* **Subject Reference Input Type**（主体参考输入类型；类型：options；字段：`subjectReferenceInputType`）：提供人脸照片，以保持生成视频中的面部一致性。仅 MiniMax-Hailuo-2.3 支持此选项。默认值：`none`。
  * **Subject Reference Image URL**（主体参考图片 URL；类型：string；字段：`subjectReferenceImageUrl`）：参考人脸图片的公开 URL。**Subject Reference Input Type**（主体参考输入类型）为 `URL` 时显示。
  * **Subject Reference Data Field Name**（主体参考数据字段名称；类型：string；字段：`subjectReferenceBinaryPropertyName`）：包含参考人脸图片的二进制字段名称。**Subject Reference Input Type**（主体参考输入类型）为 `Binary File` 时显示。默认值：`subjectReference`。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 MiniMax 集成模板](https://n8n.io/integrations/minimax)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [MiniMax 文档](https://platform.minimax.io/docs)。
