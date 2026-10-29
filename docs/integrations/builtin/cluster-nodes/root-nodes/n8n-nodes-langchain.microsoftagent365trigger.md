---
title: Microsoft Agent 365 Trigger（Microsoft Agent 365 触发器） 节点文档
description: 了解如何在 n8n 中使用 Microsoft Agent 365 Trigger（Microsoft Agent 365 触发器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: 根节点
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.microsoftagent365trigger/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.microsoftagent365trigger
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.microsoftagent365trigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Agent 365 Trigger（Microsoft Agent 365 触发器） 节点 <a href="#microsoft-agent-365-trigger-node" id="microsoft-agent-365-trigger-node"></a>

{% hint style="info" %}
**预览状态**

这是使用 Microsoft Agent 365 和 n8n 构建智能体的早期预览。你需要加入 [Frontier 预览计划](https://adoption.microsoft.com/copilot/frontier-program/)，才能提前使用 Microsoft Agent 365。
{% endhint %}

使用 Microsoft Agent 365 Trigger 节点，接收来自 Microsoft Agent 365 的消息，并通过 AI 智能体能力响应。此节点让 n8n 能够充当 Agent 365 智能体的后端。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Microsoft Agent 365 凭据文档](../../credentials/microsoftagent365.md)。
{% endhint %}

## 节点连接器 <a href="#node-connectors" id="node-connectors"></a>

Microsoft Agent 365 Trigger 节点可连接以下子节点：

- **Model**（模型）：连接语言模型（Chat model 子节点），处理传入消息
- **Memory**（记忆）：连接记忆子节点，保留对话上下文。单个 n8n 工作流为 Microsoft 端的多个 Agent 实例提供服务，因此多个用户会与同一工作流交互。请谨慎选择会话 ID 键，将对话限定到各自的 Agent 实例，防止对话历史在实例之间串用。
- **Tool**（工具）：连接工具子节点，为智能体提供额外能力

## 节点选项 <a href="#node-options" id="node-options"></a>

### Enable Microsoft Work IQ Tools for A365（为 A365 启用 Microsoft Work IQ 工具） <a href="#enable-microsoft-work-iq-tools-for-a365" id="enable-microsoft-work-iq-tools-for-a365"></a>

开启此选项，让智能体通过模型上下文协议（MCP）访问 Microsoft 365 工具。默认关闭。

启用后，选择以下一项：

- **All**（全部）：启用所有可用的 Microsoft MCP 工具
- **Selected**（指定工具）：从列表中选择具体工具：
    - Calendar（日历）
    - Mail（邮件）
    - SharePoint
    - Teams
    - Word
    - 以及更多工具

## Webhook 身份验证 <a href="#webhook-authentication" id="webhook-authentication"></a>

{% hint style="info" %}
**功能可用性**

从 n8n 2.25.7 和 n8n 2.26.2 起，Microsoft Agent 365 Trigger 节点会在运行工作流之前验证每个传入请求。节点检查 Microsoft 随请求发送的 Bot Framework token，确认它由 Microsoft 为你的智能体签发。节点会拒绝任何不含有效 token 的请求，因此即使其他人知道 webhook URL，也无法注入伪造的活动。
{% endhint %}

此验证使用 [Microsoft Agent 365 凭据](../../credentials/microsoftagent365.md)中的 **Client ID**（客户端 ID）。Client ID 必须与智能体应用注册的应用程序（客户端）ID 匹配，否则节点会拒绝来自 Microsoft 的合法请求。

## 入门 <a href="#getting-started" id="getting-started"></a>

建议按照以下资源设置 Agent 365 集成：

1. [Microsoft Agent 365 开发者文档](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/)：使用 Microsoft Agent 365 构建智能体的官方文档
2. [Agent 365 CLI 文档](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/agent-365-cli)：用于在 Azure 上部署和管理 Agent 365 应用的跨平台命令行工具

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Microsoft Agent 365 开发者文档](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}
