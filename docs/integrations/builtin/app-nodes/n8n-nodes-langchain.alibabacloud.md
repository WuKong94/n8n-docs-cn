---
title: Qwen Cloud 节点
contentType:
- integration
- reference
nodeTitle: Qwen Cloud 节点
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.alibabacloud.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.alibabacloud
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.alibabacloud
description: 在 n8n 工作流中调用 Qwen Cloud 提供的模型，生成文本、分析或生成图片，以及根据文本创建视频。
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


# Qwen Cloud <a id="qwen-cloud"></a>

{% hint style="info" %}
在 n8n Cloud 中，可以使用 [Gateway 额度](../../../deploy/use-n8n-cloud/gateway-credits/README.md)运行 Qwen Cloud 节点，无需提供自己的 Qwen Cloud API 密钥。在节点的凭据字段中选择 **Use Gateway credits**（使用 Gateway 额度），即可在没有 Qwen Cloud 账户的情况下运行节点。
{% endhint %}

Qwen Cloud 节点让你能够在 n8n 中调用 Qwen Cloud 提供的模型。使用它生成补全文本、分析或创建图片，以及根据文本或图片生成短视频。

{% hint style="info" %}
**凭据**

有关此节点的身份验证信息，请参阅 [Qwen Cloud 凭据文档](../credentials/alibaba.md)。
{% endhint %}

## 资源与操作 <a href="#resources-and-operations" id="resources-and-operations"></a>

* **Text**（文本）：向模型发送消息，生成文本补全和类似智能体的响应。
* **Image**（图片）：使用视觉语言模型分析图片，或根据提示词生成图片。
* **Video**（视频）：根据文本或一张或多张图片生成短视频。

### Message a model（向模型发送消息） <a href="#message-a-model" id="message-a-model"></a>

使用 Qwen 模型生成补全响应。

**参数**

* **Model**（模型；类型：options；字段：`modelId`）：用于生成内容的模型，例如 Qwen3.5 Flash、Qwen3 Max。
* **Messages**（消息；类型：fixedCollection；字段：`messages`）：组成对话的一条或多条消息。
  * 消息值：
    * **Content**（内容；类型：string；字段：`content`）：消息内容。
    * **Role**（角色；类型：options；字段：`role`）：消息发送者的角色：User（用户）或 Assistant（助手）。
* **Simplify Output**（简化输出；类型：boolean；字段：`simplify`）：返回简化响应，而不是完整的原始 API 输出。

**选项**

* **Enable Search**（启用搜索；类型：boolean；字段：`enableSearch`）：启用网页搜索以获取最新信息。
* **Max Tokens**（最大 token 数；类型：number；字段：`maxTokens`）：最多生成的 token 数。
* **Max Tools Iterations**（最大工具迭代次数；类型：number；字段：`maxToolsIterations`）：停止前最多执行的工具调用迭代次数。设为零表示不限制。
* **Repetition Penalty**（重复惩罚；类型：number；字段：`repetitionPenalty`）：对重复 token 的惩罚，值越高，重复越少。
* **Seed**（随机种子；类型：number；字段：`seed`）：用于复现输出的随机种子。
* **Stop Sequences**（停止序列；类型：string；字段：`stop`）：以逗号分隔的序列列表；API 遇到这些序列时停止生成。
* **System Message**（系统消息；类型：string；字段：`system`）：提供给模型的系统指令。
* **Temperature**（温度；类型：number；字段：`temperature`）：控制随机性。值越低，输出越确定。
* **Top K**（Top K；类型：number；字段：`topK`）：将采样候选集限制为概率最高的 K 个 token。
* **Top P**（Top P；类型：number；字段：`topP`）：核采样参数。

### Analyze image（分析图片） <a href="#analyze-image" id="analyze-image"></a>

输入图片，并针对图片提出视觉语言问题。

**参数**

* **Model**（模型；类型：options；字段：`modelId`）：要使用的视觉语言模型，例如 Qwen-VL Flash。
* **Input Type**（输入类型；类型：options；字段：`inputType`）：图片的提供方式：URL 或二进制数据。
* **Image URL**（图片 URL；类型：string；字段：`imageUrl`）：要分析的图片 URL，使用 URL 输入时必填。
* **Input Data Field Name**（输入数据字段名称；类型：string；字段：`binaryPropertyName`）：使用二进制输入时，从中读取图片的二进制字段名称。
* **Question**（问题；类型：string；字段：`question`）：针对图片的问题或指令。
* **Simplify Output**（简化输出；类型：boolean；字段：`simplify`）：返回简化响应。

**选项**

* **Temperature**（温度；类型：number；字段：`temperature`）：控制视觉模型的随机性。
* **Max Tokens**（最大 token 数；类型：number；字段：`maxTokens`）：视觉模型输出的最大 token 数。

### Generate an image（生成图片） <a href="#generate-an-image" id="generate-an-image"></a>

根据文本提示词创建图片。

**参数**

* **Model**（模型；类型：options；字段：`modelId`）：要使用的图片生成模型，例如 Z-Image Turbo。
* **Prompt**（提示词；类型：string；字段：`prompt`）：描述待生成图片的文本提示词。
* **Download Image**（下载图片；类型：boolean；字段：`downloadImage`）：为 true 时，将生成的图片下载为二进制数据；否则仅返回 URL。

**选项**

* **Size**（尺寸；类型：options；字段：`size`）：生成图片的尺寸，例如 102&#x34;_&#x31;024、166&#x34;_&#x39;28。
* **Prompt Extend**（扩展提示词；类型：boolean；字段：`promptExtend`）：自动扩展和增强提示词。

### Generate video from text（根据文本生成视频） <a href="#generate-video-from-text" id="generate-video-from-text"></a>

根据文本提示词生成短视频。

**参数**

* **Model**（模型；类型：options；字段：`modelId`）：要使用的文生视频模型，例如 Wan 2.6 Text-to-Video。
* **Prompt**（提示词；类型：string；字段：`prompt`）：用于生成视频的文本提示词。
* **Resolution**（分辨率；类型：options；字段：`resolution`）：分辨率档位：720P 或 1080P。
* **Duration (Seconds)**（时长（秒）；类型：number；字段：`duration`）：生成视频的时长，单位为秒，范围为 2–15。
* **Shot Type**（镜头类型；类型：options；字段：`shotType`）：Single（单镜头）或 Multi（多镜头叙事）。
* **Download Video**（下载视频；类型：boolean；字段：`downloadVideo`）：为 true 时，将生成的视频下载为二进制数据；否则仅返回 URL。
* **Simplify Output**（简化输出；类型：boolean；字段：`simplify`）：返回简化响应。

**选项**

* **Prompt Extend**（扩展提示词；类型：boolean；字段：`promptExtend`）：自动扩展和增强提示词。
* **Audio**（音频；类型：boolean；字段：`audio`）：是否为视频生成音频。
* **Audio Input Type**（音频输入类型；类型：options；字段：`audioInputType`）：启用 **Audio**（音频）选项时必须指定，用于定义音频的提供方式：音频 URL 或二进制文件。
* **Audio URL**（音频 URL；类型：string；字段：`audioUrl`）：**Audio Input Type**（音频输入类型）设为 URL 时必须指定，表示要使用的音频文件 URL。
* **Audio Data Field Name**（音频数据字段名称；类型：string；字段：`audioBinaryPropertyName`）：**Audio Input Type**（音频输入类型）设为 **Binary File**（二进制文件）时必须指定，表示音频输入的二进制字段名称。

### Generate video from image（根据图片生成视频） <a href="#generate-video-from-image" id="generate-video-from-image"></a>

使用 Wan 模型，根据一张或多张图片生成视频。

**参数**

* **Model**（模型；类型：options；字段：`modelId`）：要使用的图生视频模型，例如 Wan 2.6 Image-to-Video Flash。
* **Input Type**（输入类型；类型：options；字段：`inputType`）：图片的提供方式：图片 URL 或二进制文件。
* **Image URL**（图片 URL；类型：string；字段：`imgUrl`）：用于生成视频的首帧图片 URL。
* **Input Data Field Name**（输入数据字段名称；类型：string；字段：`binaryPropertyName`）：使用二进制输入时，从中读取图片的二进制字段名称。
* **Prompt**（提示词；类型：string；字段：`prompt`）：可选的文本描述，用于指定所需内容和视觉特征。
* **Resolution**（分辨率；类型：options；字段：`resolution`）：分辨率档位：720P 或 1080P。
* **Duration (Seconds)**（时长（秒）；类型：number；字段：`duration`）：时长，单位为秒，范围为 2–15。
* **Shot Type**（镜头类型；类型：options；字段：`shotType`）：Single（单镜头）或多镜头叙事。
* **Download Video**（下载视频；类型：boolean；字段：`downloadVideo`）：为 true 时，将生成的视频下载为二进制数据；否则仅返回 URL。
* **Simplify Output**（简化输出；类型：boolean；字段：`simplify`）：返回简化响应。

**选项**

* **Prompt Extend**（扩展提示词；类型：boolean；字段：`promptExtend`）：自动扩展和增强提示词。
* **Audio**（音频；类型：boolean；字段：`audio`）：是否为视频生成音频。
* **Audio Input Type**（音频输入类型；类型：options；字段：`audioInputType`）：音频的提供方式：音频 URL 或二进制文件。
* **Audio URL**（音频 URL；类型：string；字段：`audioUrl`）：**Audio Input Type**（音频输入类型）设为 URL 时要使用的音频文件 URL。
* **Audio Data Field Name**（音频数据字段名称；类型：string；字段：`audioBinaryPropertyName`）：**Audio Input Type**（音频输入类型）设为二进制数据时，音频输入的二进制字段名称。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Qwen Cloud 集成模板](https://n8n.io/integrations/alibaba-cloud-model-studio)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关可用模型和 API 行为的更多信息，请参阅 [Qwen Cloud 文档](https://docs.qwencloud.com/)。
