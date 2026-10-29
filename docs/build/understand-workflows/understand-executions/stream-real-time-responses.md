---
title: 流式响应
contentType: howto
nodeTitle: 流式传输实时响应
originalFilePath: workflows/streaming.md
originalUrl: https://docs.n8n.io/workflows/streaming
url: https://docs.n8n.io/build/understand-workflows/understand-executions/stream-real-time-responses
description: 构建支持流式响应的工作流。
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


# 流式传输实时响应 <a id="stream-real-time-responses"></a>

{% hint style="info" %}
**功能可用范围**

所有套餐均可用。
{% endhint %}

流式响应可以在 AI Agent 节点生成数据的同时，将数据返回给用户。这对聊天机器人很有用：可以在答案生成时逐步展示，从而提供更好的用户体验。

可以通过以下任意节点启用流式传输：

* [Chat Trigger（聊天触发器）](../../../integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/README.md)
* [Webhook 节点](../../../integrations/builtin/core-nodes/n8n-nodes-base.webhook/README.md)

两种情况下，都需要将节点的 **Response Mode（响应模式）** 设为 **Streaming（流式）**。

## 配置节点以进行流式传输 <a href="#configure-nodes-for-streaming" id="configure-nodes-for-streaming"></a>

要进行流式传输，必须向工作流添加支持流式输出的节点。并非所有节点都支持此功能。

1. 选择支持流式传输的节点，例如：
   * [AI agent（AI 智能体）](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/README.md)
   * [Respond to Webhook](../../../integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook.md)
2. 可以在这些节点的选项中禁用流式传输。默认情况下，只要已执行触发器的 `Response Mode` 设为 `Streaming response`，这些节点就会流式传输数据。

## 重要信息 <a href="#important-information" id="important-information"></a>

配置流式响应时，请注意以下细节：

* **触发器**：触发器节点必须支持流式传输，并已配置此功能。否则，工作流会按照响应模式设置运行。
* **节点配置**：即使触发器已启用流式传输，也至少需要一个配置为流式输出数据的节点，否则工作流不会发送任何数据。

## 相关资源 <a id="related-resources"></a>

* [理解执行](./)
* [手动执行、部分执行与生产执行](types-of-executions.md)
* [查看所有执行](view-all-executions.md)
* [查看单个工作流的执行](view-executions-for-a-single-workflow.md)
* [调试并重新运行以往执行](debug-executions.md)
* [自定义执行数据](customize-executions-data.md)
* [脏节点](understand-dirty-nodes.md)
