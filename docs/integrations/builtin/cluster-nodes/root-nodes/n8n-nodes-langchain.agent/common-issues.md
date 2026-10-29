---
title: AI Agent 节点常见问题
contentType:
- integration
- reference
priority: critical
nodeTitle: AI Agent 节点常见问题
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues
description: 工作流自动化平台 n8n 中 AI Agent 节点的常见错误和问题，包括问题详情及建议的解决办法。
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

以下列出 [AI Agent 节点](./README.md)的常见错误和问题，以及解决或排查步骤。

## Internal error: 400 Invalid value for 'content'（内部错误：content 值无效） <a href="#internal-error-400-invalid-value-for-content" id="internal-error-400-invalid-value-for-content"></a>

完整错误消息可能如下所示：

```
Internal error
Error: 400 Invalid value for 'content': expected a string, got null.
<stack-trace>
```

**Prompt**（提示词）输入包含 null 值时，可能出现此错误。

以下两种情况之一可能导致此问题：

1. **Prompt**（提示词）设为 **Define below**（在下方定义），但 **Text**（文本）中的表达式未生成值。
   * 请确保表达式引用有效字段，并解析为有效输入，而非 null。
2. **Prompt**（提示词）设为 **Connected Chat Trigger Node**（已连接的聊天触发器节点），但传入数据包含 null 值。
   * 请从输入节点的 `chatInput` 字段移除 null 值。

## Error in sub-node Simple Memory（Simple Memory 子节点错误） <a href="#error-in-sub-node-simple-memory" id="error-in-sub-node-simple-memory"></a>

n8n 在 [Simple Memory](../../sub-nodes/n8n-nodes-langchain.memorybufferwindow/README.md) 子节点中遇到问题时，会显示此错误。

最常见的原因是工作流或复制的模板使用了旧版 Simple Memory 节点，该节点此前名为“Window Buffer Memory”。

可尝试从工作流移除 Simple Memory 节点后重新添加，确保使用最新节点版本。

## A Chat Model sub-node must be connected（必须连接聊天模型子节点）错误 <a href="#a-chat-model-sub-node-must-be-connected-error" id="a-chat-model-sub-node-must-be-connected-error"></a>

n8n 尝试执行未连接 Chat Model 的节点时，会显示此错误。

节点打开时，点击屏幕底部的 + Chat Model 按钮；节点关闭时，点击 Chat Model + 连接器。n8n 随后会打开可用聊天模型列表供你选择。

## 未指定提示词错误 <a href="#no-prompt-specified-error" id="no-prompt-specified-error"></a>

智能体期望从上一个节点自动获取提示词时，会出现此错误，通常发生在使用 [Chat Trigger 节点](../../../core-nodes/n8n-nodes-langchain.chattrigger/README.md)时。

解决方法是找到 AI Agent 节点的 **Prompt**（提示词）参数，将其从 **Connected Chat Trigger Node**（已连接的聊天触发器节点）改为 **Define below**（在下方定义），以便通过引用其他节点的输出数据或添加静态文本，手动构建提示词。
