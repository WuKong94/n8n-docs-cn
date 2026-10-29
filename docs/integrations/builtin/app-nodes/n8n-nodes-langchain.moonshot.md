---
title: Moonshot Kimi 节点
contentType:
- integration
- reference
nodeTitle: Moonshot Kimi 节点
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.moonshot.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.moonshot
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.moonshot
description: 在 n8n 中调用 Moonshot Kimi AI 模型，了解如何向模型发送消息、附加图片，以及使用节点操作分析图片。
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


# Moonshot Kimi <a id="moonshot-kimi"></a>

{% hint style="info" %}
在 n8n Cloud 中，可以使用 [Gateway 额度](../../../deploy/use-n8n-cloud/gateway-credits/README.md)运行 Moonshot Kimi 节点，无需提供自己的 Moonshot API 密钥。在节点的凭据字段中选择 **Use Gateway credits**（使用 Gateway 额度），即可在没有 Moonshot 账户的情况下运行节点。
{% endhint %}

Moonshot Kimi 节点将 n8n 工作流连接到 Moonshot Kimi AI 模型。使用它发送提示词并接收模型响应、为消息附加图片，或使用图片分析模型分析图片。

{% hint style="info" %}
**凭据**

有关此节点的身份验证信息，请参阅 [Moonshot 凭据文档](../credentials/moonshot.md)。
{% endhint %}

## 资源与操作 <a href="#resources-and-operations" id="resources-and-operations"></a>

* **Analyze image**（分析图片）：分析图片并回答相关问题。
* **Message a model**（向模型发送消息）：向 Moonshot Kimi 模型发送文本消息并接收响应，支持附件、系统消息，以及思考模式、网页搜索等高级选项。

### Analyze image（分析图片） <a href="#analyze-image" id="analyze-image"></a>

分析一张图片，并回答与图片有关的问题。

**参数**

* **Model**（模型；类型：resourceLocator；字段：`modelId`）：选择用于分析的 Moonshot Kimi 模型。
* **Text Input**（文本输入；类型：string；字段：`text`）：与图片一起发送的提示词或问题。默认值：`What's in this image?`。
* **Input Data Field Name(s)**（输入数据字段名称；类型：string；字段：`binaryPropertyName`）：包含图片的一个或多个二进制字段名称。多个字段以逗号分隔。默认值：`data`。
* **Simplify Output**（简化输出；类型：boolean；字段：`simplify`）：开启时，节点返回简化响应，而不是完整的原始 API 响应。默认值：`true`。

**选项**

* **Maximum Number of Tokens**（最大 token 数；类型：number；字段：`maxTokens`）：token 越少，生成的图片描述越短，细节也越少。默认值：`1024`。

### Message a model（向模型发送消息） <a href="#message-a-model" id="message-a-model"></a>

向 Moonshot Kimi 模型发送一条或多条消息，并接收其响应。支持按角色区分的消息（user/assistant）、附件、系统消息及高级生成选项。

**参数**

* **Model**（模型；类型：resourceLocator；字段：`modelId`）：选择要向其发送消息的 Moonshot Kimi 模型。
* **Messages**（消息；类型：fixedCollection；字段：`messages`）：组成对话提示的一条或多条消息。
  * content（类型：string）：消息的文本内容。（显示名称：Prompt）
  * role（类型：options）：消息的角色，例如 `user` 或 `assistant`，用于引导模型如何响应。
* **Add Attachments**（添加附件；类型：boolean；字段：`addAttachments`）：是否为消息附加图片。默认值：`false`。
* **Attachment Input Data Field Name(s)**（附件输入数据字段名称；类型：string；字段：`binaryPropertyName`）：包含待附加图片的一个或多个二进制字段名称。多个字段以逗号分隔。默认值：`data`。
* **Simplify Output**（简化输出；类型：boolean；字段：`simplify`）：开启时，节点返回简化响应，而不是原始 API 输出。默认值：`true`。

**选项**

* **Frequency Penalty**（频率惩罚；类型：number；字段：`frequencyPenalty`）：正值会惩罚文本中已出现的 token，以减少重复。默认值：`0`。
* **Include Merged Response**（包含合并响应；类型：boolean；字段：`includeMergedResponse`）：包含一个将模型响应中所有文本部分合并后的输出字符串。默认值：`false`。
* **Maximum Number of Tokens**（最大 token 数；类型：number；字段：`maxTokens`）：补全响应最多生成的 token 数。默认值：`1024`。
* **Max Tool Calls Iterations**（最大工具调用迭代次数；类型：number；字段：`maxToolsIterations`）：大语言模型停止前最多执行的工具迭代轮数。一轮迭代可以包含多次工具调用。设为 `0` 表示不限制。默认值：`15`。
* **Output Randomness (Temperature)**（输出随机性（温度）；类型：number；字段：`temperature`）：控制输出的随机性。值越低，输出越确定。默认值：`0.7`。
* **Output Randomness (Top P)**（输出随机性（Top P）；类型：number；字段：`topP`）：采样时考虑的 token 的最大累计概率。默认值：`1`。
* **Presence Penalty**（存在惩罚；类型：number；字段：`presencePenalty`）：正值会根据 token 是否已在当前文本中出现过施加惩罚，鼓励引入新话题。默认值：`0`。
* **Response Format**（响应格式；类型：options；字段：`responseFormat`）：返回响应的格式，例如 `text`。
* **System Message**（系统消息；类型：string；字段：`system`）：用于引导模型整体行为和语气的系统级指令。
* **Thinking Mode**（思考模式；类型：boolean；字段：`thinkingMode`）：开启时，模型会以思维链形式包含推理步骤。不能与 **Web Search**（网页搜索）同时使用。默认值：`false`。
* **Web Search**（网页搜索；类型：boolean；字段：`webSearch`）：开启时，模型会执行内置网页搜索以获取最新信息。不能与 **Thinking Mode**（思考模式）同时使用。默认值：`false`。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Moonshot Kimi 集成模板](https://n8n.io/integrations/moonshot-kimi)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Moonshot Kimi 文档](https://platform.kimi.ai/docs/overview)。
