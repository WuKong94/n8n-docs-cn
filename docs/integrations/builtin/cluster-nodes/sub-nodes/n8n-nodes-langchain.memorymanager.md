---
title: Chat Memory Manager（聊天记忆管理器） 节点文档
description: 了解如何在 n8n 中使用 Chat Memory Manager（聊天记忆管理器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Chat Memory Manager（聊天记忆管理器） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Chat Memory Manager（聊天记忆管理器） 节点 <a href="#chat-memory-manager-node" id="chat-memory-manager-node"></a>

Chat Memory Manager 节点管理工作流中的聊天消息记忆[^1]。使用此节点加载、插入和删除内存[向量存储](#user-content-fn-2)[^2]中的聊天消息。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-sub-nodes/chat-memory-manager-purpose.md" %}

本页列出了 Chat Memory Manager 节点支持的操作，并提供更多资源的链接。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Operation Mode**（操作模式）：选择 **Get Many Messages**（获取多条消息）、**Insert Messages**（插入消息）或 **Delete Messages**（删除消息）。
* **Insert Mode**（插入模式）：适用于 **Insert Messages**（插入消息）模式，可选：
    * **Insert Messages**（插入消息）：在现有消息之外插入新消息。
    * **Override All Messages**（覆盖全部消息）：替换当前记忆。
* **Delete Mode**（删除模式）：适用于 **Delete Messages**（删除消息）模式，可选：
    * **Last N**（最后 N 条）：删除最后 N 条消息。
    * **All Messages**（全部消息）：从记忆中删除消息。
* **Chat Messages**（聊天消息）：适用于 **Insert Messages**（插入消息）模式。定义要插入记忆的聊天消息，包括：
    * **Type Name or ID**（类型名称或 ID）：设置消息类型，可选择：
        * **AI**：用于来自 AI 的消息。
        * **System**（系统）：添加包含 AI 指令的消息。
        * **User**（用户）：用于来自用户的消息。其他 AI 工具和指南有时将此类型称为“human”消息。
    * **Message**（消息）：输入消息内容。
    * **Hide Message in Chat**（在聊天中隐藏消息）：关闭时，n8n 在聊天界面向用户显示消息；开启时不显示。
* **Messages Count**（消息数量）：在 **Delete Messages**（删除消息）模式中选择 **Last N**（最后 N 条）时可用，输入要删除的最新消息数量。
* **Simplify Output**（简化输出）：适用于 **Get Many Messages**（获取多条消息）模式。开启后，输出仅包含发件方（AI、用户或系统）及文本。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Chat Memory Manager（聊天记忆管理器） 集成模板](https://n8n.io/integrations/chat-memory-manager)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 记忆文档](https://langchain-ai.github.io/langgraphjs/concepts/memory/)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: 在 AI 场景中，记忆让 AI 工具能够在多次交互之间保存消息上下文。例如，与 AI 智能体持续对话时，无需在每条消息中重复提交上下文。在 n8n 中，AI 智能体节点可以使用记忆，而 AI 链不能。
<a id="user-content-fn-2"></a>
[^2]: 向量存储或向量数据库用于存储信息的数学表示。将其与嵌入模型和检索器配合使用，可创建供 AI 在回答问题时访问的数据库。
