---
title: Chat Hub
status: beta
nodeTitle: Chat Hub
originalFilePath: advanced-ai/chat-hub.md
originalUrl: https://docs.n8n.io/advanced-ai/chat-hub
url: https://docs.n8n.io/build/ways-of-building-workflows/chat-hub
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


# Chat Hub <a id="chat-hub"></a>

## 概述 <a href="#overview" id="overview"></a>

Chat Hub 是集中式 AI 聊天界面，可以在其中访问多个 AI 模型、与 n8n 智能体交互，并创建自己的智能体。Chat Hub 还引入 Chat user（聊天用户）角色，让用户使用聊天界面，而无需访问 n8n 工作流。

## 使用方式 <a href="#how-to-use" id="how-to-use"></a>

在导航栏中找到 **Chat（聊天）**，选择模型，即可开始对话。

### 创建简单的个人智能体 <a href="#creating-simple-personal-agents" id="creating-simple-personal-agents"></a>

对于简单的重复任务，可以创建带有自定义指令的 Custom Agents（自定义智能体），提高 AI 的可靠性。创建简单个人智能体的步骤如下：

1. 点击 **Personal Agents（个人智能体）**，再点击 **+New Agent（新建智能体）**。
2. 设置名称、说明、系统提示词、首选模型和工具访问权限。
3. 选择 **Save（保存）**。

创建后，可以在模型选择器中选择此个人智能体。

### 使用 n8n 工作流智能体 <a href="#using-n8n-workflows-agents" id="using-n8n-workflows-agents"></a>

对于更复杂的场景，使用你或同事构建的 n8n 工作流智能体，让工作流在 Chat Hub 中可用。目前，仅支持包含 **Chat Trigger**，且 **Agent** 节点启用流式传输的工作流。设置步骤如下：

1. 打开选定的工作流。
2. 打开 **Chat Trigger**。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>仅最新版本的聊天触发器可用。要获取最新版本，请删除已有聊天触发器，再插入新触发器。</p></div>
3. 启用 **Make Available in n8n Chat（在 n8n Chat 中可用）**，并设置个人智能体的名称和说明。
4. 确保 AI Agent 节点已启用 **Enable Streaming（启用流式传输）**。
5. 发布工作流。

设置后，可以在 Chat Hub 的模型选择器中选择该工作流。同事需要有权访问工作流：可以通过共享获得权限，也可以属于工作流所在的项目，且至少具有查看权限。

## 管理权限 <a href="#managing-permissions" id="managing-permissions"></a>

可以通过 n8n 角色系统定义哪些用户有权执行哪些操作。Chat Hub 还提供更多方式，控制谁可以使用哪些功能。

### Chat user 角色 <a href="#chat-user-role" id="chat-user-role"></a>

Chat user（聊天用户）角色适合组织内需要使用工作流、但不构建工作流的人员。聊天用户只能看到聊天界面，默认无法添加凭据或工作流。

{% hint style="info" %}
**功能可用范围**

以下套餐提供 Chat user 角色：

- **n8n Cloud：** Pro、Enterprise
- **自托管：** Business、Enterprise
{% endhint %}

### 服务提供商设置 <a href="#provider-settings" id="provider-settings"></a>

管理员可以控制用户在 Chat Hub 中可访问的模型和服务提供商，包括：

* 启用或禁用特定模型和服务提供商
* 阻止用户添加自己的模型
* 为每个服务提供商设置默认凭据
* 通过 n8n 权限系统限制用户添加自己的凭据

要管理这些设置，进入 **Settings > Chat（设置 > 聊天）**，编辑服务提供商。

## 注意事项与限制 <a href="#considerations-and-limitations" id="considerations-and-limitations"></a>

1. 创建简单个人智能体时，无法添加文件知识。
2. 工具选择仅限少量选项。
3. 只有包含 [Chat Trigger 节点](../../integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/README.md)和已启用流式传输的 [AI Agent 节点](../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/README.md)的工作流，才能作为工作流智能体使用。工作流必须满足特定要求。

## 相关资源 <a id="related-resources"></a>

* [构建工作流的方式](./)
* [使用 n8n Assistant](n8n-assistant.md)
* [使用 n8n MCP 服务器](connect-to-n8n-mcp-server.md)
* [使用模板](use-templates.md)
* [使用 Ask n8n AI](use-the-ai-assistant.md)
