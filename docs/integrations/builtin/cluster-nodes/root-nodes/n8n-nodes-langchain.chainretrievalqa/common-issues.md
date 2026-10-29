---
title: Question and Answer Chain 节点常见问题
contentType:
- integration
- reference
priority: high
nodeTitle: Question and Answer Chain 节点常见问题
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/common-issues
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/common-issues
description: 工作流自动化平台 n8n 中 Question and Answer Chain 节点的常见错误和问题，包括问题详情及建议的解决办法。
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


# 常见问题 <a id="common-issues"></a>

以下列出 [Question and Answer Chain 节点](./README.md)的常见错误和问题，以及解决或排查步骤。

## 未指定提示词错误 <a href="#no-prompt-specified-error" id="no-prompt-specified-error"></a>

**Prompt**（提示词）为空或无效时，会显示此错误。

以下两种情况之一可能导致此问题：

1. **Prompt**（提示词）设为 **Define below**（在下方定义），但 **Text**（文本）中的表达式未生成值。
   * 解决方法是在 **Text**（文本）字段中输入有效提示词。
   * 请确保表达式引用有效字段，并解析为有效输入，而非 null。
2. **Prompt**（提示词）设为 **Connected Chat Trigger Node**（已连接的聊天触发器节点），但传入数据包含 null 值。
   * 解决方法是确保输入包含 `chatInput` 字段。添加 [Edit Fields (Set)](../../../core-nodes/n8n-nodes-base.set.md) 节点，将传入字段名称改为 `chatInput`。
   * 请从输入节点的 `chatInput` 字段移除 null 值。

## A Retriever sub-node must be connected（必须连接检索器子节点）错误 <a href="#a-retriever-sub-node-must-be-connected-error" id="a-retriever-sub-node-must-be-connected-error"></a>

n8n 尝试执行未连接 Retriever 的节点时，会显示此错误。

解决方法是：节点打开时，点击屏幕底部的 + Retriever 按钮；节点关闭时，点击 Retriever + 连接器。n8n 随后会打开可用检索器列表供你选择。

## 无法生成更长的响应 <a href="#cant-produce-longer-responses" id="cant-produce-longer-responses"></a>

如果需要生成比 Question and Answer Chain 节点默认响应更长的内容，可尝试以下一种或多种方法：

* **连接输出更详尽的模型**：有些 AI 模型的输出比其他模型简短。换用上下文窗口更大、输出更详尽的模型，可增加响应长度。
* **增加最大 token 数**：许多模型节点（例如 [OpenAI Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatopenai/README.md#maximum-number-of-tokens)）提供 **Maximum Number of Tokens**（最大 token 数）选项。可通过此设置增加模型生成响应时可用的最大 token 数。
* **分阶段构建较长的响应**：需要更详细的答案时，可以使用多种 AI 节点分阶段构建回复。可用 AI 将一个问题拆分为多个提示词，并分别生成响应，再将这些响应组合为最终回复。虽然具体实现不同，但这个[使用 AI 撰写 WordPress 文章的模板](https://n8n.io/workflows/2187-write-a-wordpress-post-with-ai-starting-from-a-few-keywords/)很好地展示了总体思路。
