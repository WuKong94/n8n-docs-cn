---
title: AI 工具调用中的人工审核
description: 了解如何要求 AI Agent 在 n8n 中执行特定工具前获得人工批准。
contentType: explanation
nodeTitle: 为工具添加人工审核
originalFilePath: advanced-ai/human-in-the-loop-tools.md
originalUrl: https://docs.n8n.io/advanced-ai/human-in-the-loop-tools
url: https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# AI 工具调用中的人工审核 <a href="#human-in-the-loop-for-ai-tool-calls" id="human-in-the-loop-for-ai-tool-calls"></a>

可以要求 AI Agent 在执行特定工具前获得人工批准。当工具需要人工审核时，工作流会暂停，等待审核者执行以下操作之一：

- **Approve（批准）**：工具使用 AI 指定的输入执行。
- **Deny（拒绝）**：取消操作，不执行工具。

此功能允许有选择地监督 AI 工作流中的工具使用，便于对发送消息、修改记录或删除数据等风险较高的工具增加审核。

## 何时使用人工审核 <a href="#when-to-use-human-review" id="when-to-use-human-review"></a>

以下情况适合使用人工参与（HITL）审核：

- **工具执行不可逆操作**：例如删除数据、对外发送消息或购买商品。
- **存在合规要求**：受监管行业可能要求某些自动化操作获得人工批准。
- **涉及重要决策**：对业务影响较大的操作适合增加人工监督。
- **正在建立对 AI 工作流的信任**：先启用人工审核，随着信心增强，再逐步减少监督。

可以对 AI Agent 节点连接的所有工具启用人工审核，也可以只对指定工具启用。相较于统一审核输出，这种方式提供更精确的控制。

## 工作原理 <a href="#how-it-works" id="how-it-works"></a>

1. AI Agent 判断需要使用一个已启用人工审核的工具。
2. 工作流暂停，并通过配置的渠道发送审批请求，例如 Slack、Telegram 或 n8n Chat 界面。
3. 人工审核者收到请求，查看 AI 想使用的工具及其参数。
4. 审核者批准或拒绝请求。
5. 批准后，工具使用 AI 指定的输入执行。拒绝后，操作取消，并告知 AI 请求已被拒绝。

{% hint style="info" %}
**使用不同的审批渠道**

审核步骤可以使用与主要交互不同的渠道。例如，用户通过 n8n Chat 界面与 AI 智能体交互，而审批请求发送给 Slack 中的指定人员。
{% endhint %}

## 为工具设置人工审核 <a href="#setting-up-human-review-for-tools" id="setting-up-human-review-for-tools"></a>

### 第 1 步：打开工具面板 <a href="#step-1-open-the-tools-panel" id="step-1-open-the-tools-panel"></a>

在工作流中，点击 AI Agent 节点的 **Tools（工具）**连接端，打开工具面板。

### 第 2 步：添加人工审核步骤 <a href="#step-2-add-a-human-review-step" id="step-2-add-a-human-review-step"></a>

1. 在工具面板中找到 **Human review（人工审核）**部分。
2. 从可用选项中选择所需的审批渠道。
3. 为审批渠道配置相应凭据和设置。

### 第 3 步：将工具连接到审核步骤 <a href="#step-3-connect-tools-to-the-review-step" id="step-3-connect-tools-to-the-review-step"></a>

1. 将需要审批的工具添加到人工审核步骤的工具连接端。
2. 按通常方式配置每个工具。



## 可用审批渠道 <a href="#available-approval-channels" id="available-approval-channels"></a>

可以使用以下任意服务作为人工审核渠道：

| 渠道 | 说明 |
|---------|-------------|
| [Chat](../../../integrations/builtin/core-nodes/n8n-nodes-langchain.chat.md) | n8n 内置聊天界面 |
| [Slack](../../../integrations/builtin/app-nodes/n8n-nodes-base.slack/README.md) | 将审批请求发送到 Slack 频道或私信 |
| [Discord](../../../integrations/builtin/app-nodes/n8n-nodes-base.discord/README.md) | 将审批请求发送到 Discord 频道 |
| [Telegram](../../../integrations/builtin/app-nodes/n8n-nodes-base.telegram/README.md) | 通过 Telegram 发送审批请求 |
| [Microsoft Teams](../../../integrations/builtin/app-nodes/n8n-nodes-base.microsoftteams.md) | 将审批请求发送到 Teams 频道或聊天 |
| [Gmail](../../../integrations/builtin/app-nodes/n8n-nodes-base.gmail/README.md) | 通过电子邮件发送审批请求 |
| [WhatsApp Business Cloud](../../../integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/README.md) | 通过 WhatsApp 发送审批请求 |
| [Google Chat](../../../integrations/builtin/app-nodes/n8n-nodes-base.googlechat.md) | 将审批请求发送到 Google Chat |
| [Microsoft Outlook](../../../integrations/builtin/app-nodes/n8n-nodes-base.microsoftoutlook.md) | 通过 Outlook 邮件发送审批请求 |

## 在人工审核工具中使用表达式 <a href="#using-expressions-in-human-review-tools" id="using-expressions-in-human-review-tools"></a>

### $tool 变量 <a href="#the-dollartool-variable" id="the-dollartool-variable"></a>

配置人工审核步骤时，可以使用 `$tool` 变量为审核者构造消息，说明 AI 想执行的操作。此变量有两个属性：

| 属性 | 说明 |
|----------|-------------|
| `$tool.name` | AI Agent 尝试调用的工具名称，即 n8n 画布上显示的节点名称。 |
| `$tool.parameters` | AI Agent 尝试在工具调用中使用的参数，包括工具输入 schema 中通过 `$fromAI()` 表达式配置的字段。 |

**消息配置示例：**

```
AI 希望使用 {{ $tool.name }}，参数如下：
{{ JSON.stringify($tool.parameters, null, 2) }}
```

这样可帮助审核者在批准或拒绝之前，准确理解 AI 想执行的操作。

### 在人工审核工具中使用 $fromAI() <a href="#using-dollarfromai-in-human-review-tools" id="using-dollarfromai-in-human-review-tools"></a>

[`$fromAI()` 函数](use-ai-for-parameters.md)适用于连接到人工审核步骤的工具。这意味着 AI 可以动态指定工具参数，人工审核者看到并批准的就是这些由 AI 决定的值。

## 系统提示词最佳实践 <a href="#system-prompt-best-practices" id="system-prompt-best-practices"></a>

要让 AI Agent 正确理解和处理被拒绝的工具调用，请在系统提示词中说明人工审核的设置。

{% hint style="warning" %}
**需要配置系统提示词**

请在系统提示词中包含工具设置和人工审核步骤，帮助 AI 理解哪些工具需要批准，以及工具调用被拒绝时应如何妥善回应。
{% endhint %}

可以包含以下内容：

- 哪些工具需要人工批准。
- 审批被拒绝后会发生什么。
- AI 应如何应对拒绝，例如告知用户、提出替代方案或请求澄清。



## 链式调用与子智能体 <a href="#chaining-and-subagents" id="chaining-and-subagents"></a>

将 AI Agent 作为另一个 AI Agent 的工具时，子智能体中的人工审核步骤仍可正常工作。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

- [AI 示例](../ai-examples.md)
- [使用 Google Sheets 作为数据源](use-google-sheets-as-a-data-source.md)
- [调用 API](call-apis.md)
- [使用网站内容](use-website-content.md)
- [为 AI 工作流设置人工兜底](set-a-human-fallback-for-ai-workflows.md)
- [使用 AI 填写参数](use-ai-for-parameters.md)
- [AI Agent 节点](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/README.md)
- [Tools Agent](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md)
- [AI 中的工具是什么？](../understand-ai-components/how-tools-work.md)
