---
title: 构建和管理智能体
status: preview
description: 在 n8n 中构建与工作流并列的智能体，发布后让用户通过聊天、渠道和定时任务使用。
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
tags:
- tag: preview
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 构建和管理智能体 <a id="build-and-manage-agents"></a>

智能体是在 n8n 中构建的自主助手。每个智能体都拥有语言模型、指令，以及你配置的能力，例如工具、技能和知识库访问权限。智能体与工作流一样，是项目中可独立管理的对象。当任务难以用固定工作流描述，需要助手理解请求、选择合适的工具并根据响应调整行动时，可以使用智能体。

{% hint style="info" %}
**功能可用范围**

智能体可用于：

- **n8n Cloud：**所有套餐。
- **自托管：**自 n8n 2.32.3 起的所有套餐。设置详情请参阅[自托管](#self-hosted)。
{% endhint %}

{% hint style="info" %}
**预览状态**

智能体目前处于预览阶段，可能出错，行为也可能在功能开发过程中发生变化。自托管环境中的知识库也处于预览阶段。
{% endhint %}

### 启用或禁用智能体 <a id="enable-or-disable-agents"></a>

所有套餐默认启用智能体，包括企业版。实例所有者和管理员可以为整个实例更改此设置：

1. 打开 **Settings > Agents（设置 > 智能体）**。
2. 打开或关闭 **Enable Agents（启用智能体）**。

n8n 会保留你的选择，不受重启或许可证变更影响。此设置独立于 n8n Assistant 的设置。

关闭智能体后：

* 用户无法创建智能体，也无法通过预览、聊天、定时任务、渠道、MCP、评估或 **Message an Agent** 节点启动新的运行。
* 正在运行的任务可以完成，包括等待审批的任务。
* n8n 会取消为后续运行排队的消息。重新启用智能体后，这些消息也不会运行。
* n8n 会保留已保存的智能体和会话历史。重新启用智能体后，可以再次访问。

定时任务会保留。重新启用智能体后，它们可以再次触发新的运行。n8n 不会补执行智能体关闭期间错过的定时触发。

此设置不影响工作流中的 **AI Agent** 节点。

### 配置共享沙箱 <a id="configure-the-shared-sandbox"></a>

智能体与 n8n Assistant 共用同一沙箱连接，修改会同时作用于这两项功能。即使其中一项功能关闭，也可以配置连接。

在自托管实例中，实例所有者或管理员可以配置连接：

1. 打开 **Settings > Agents（设置 > 智能体）**。
2. 在 **Shared sandbox（共享沙箱）**下，选择 **Add sandbox（添加沙箱）**。要编辑已有连接，请选择 **Code sandbox（代码沙箱）**这一行。
3. 选择沙箱提供商并输入连接信息。
4. 选择 **Save（保存）**。n8n 会在保存前检查连接。

n8n Cloud 会管理沙箱连接。对于自托管环境，如果连接由环境变量配置，页面会显示 **Found in server configuration（已在服务器配置中找到）**，不提供编辑控件。如果已配置连接但沙箱处于关闭状态，请选择 **Enable sandbox（启用沙箱）**。

环境变量及模块要求请参阅[在自托管 n8n 中启用智能体](../../deploy/host-n8n/configure-n8n/set-up-n8n-assistant.md#enable-agents)。

### 视频：智能体如何与工作流及 AI 配合 <a id="video-how-agents-fit-with-workflows-and-ai"></a>

智能体、固定工作流，以及在特定步骤使用 AI 的工作流，分别适合不同类型的任务。观看视频，了解这三种方式的区别，以及它们如何在可投入生产的系统中协同工作。

{% embed url="https://www.youtube.com/embed/P5x0nsY8hCg" %}

### 可以用智能体构建什么 <a id="what-you-can-build-with-agents"></a>

智能体可以利用你上传的文件和已连接的服务回答问题，在 Slack、Google Sheets 或 Linear 等工具中执行操作，以及触发或协调工作流以完成较大的任务。智能体也可以将任务委派给其他智能体，并按计划运行。参阅下方的[子智能体](#add-sub-agents)和[定时任务](#run-agents-on-a-schedule)。

### 智能体的工作原理 <a id="how-agents-work"></a>

智能体通过推理循环运行。收到消息或被定时任务触发后，它会读取你的指令、理解请求，并决定下一步操作：调用工具、搜索知识库、交给其他智能体处理，或提出追问。它会重复这一过程，直到生成最终响应。

与智能体的每次对话都是一个**会话（session）**。n8n 会保存会话，以便你稍后继续，也让智能体能够通过记忆回想上下文。

### 智能体的组成部分 <a id="parts-of-an-agent"></a>

在 Agent Builder（智能体构建器）中配置以下部分：

| 组成部分 | 作用 |
| ------------------ | --------------------------------------------------------------------------------------------------------------- |
| **Model（模型）** | 用于推理和生成响应的语言模型。设置智能体时选择提供商和模型。 |
| **Instructions（指令）** | 描述智能体角色、语气和约束的系统提示词。 |
| **Tools（工具）** | 智能体可以执行的操作，包括工作流、自定义代码、n8n 内置集成和 [MCP 服务器](../integrate-ai/mcp-servers.md)。 |
| **Web search（网页搜索）** | 通过模型原生搜索工具或备用服务，在网上查找最新信息。 |
| **Skills（技能）** | 将指令与特定任务所需的工具打包，形成可复用的行为组合。 |
| **Channels（渠道）** | 用户可以联系智能体的地方，例如 Slack、Telegram 或 Linear。 |
| **Schedules（定时任务）** | 智能体发布后按周期运行的任务。 |
| **Sub-agents（子智能体）** | 当前智能体可以向其委派工作的其他已发布智能体。 |
| **Knowledge base（知识库）** | 智能体可搜索和读取的上下文文件。支持 n8n Cloud；自托管环境需配置沙箱，且处于预览阶段。 |
| **Memory（记忆）** | 会话记忆保留当前对话，情景记忆用于回想早期会话的上下文。 |

构建智能体时配置模型、指令、工具、技能、知识、记忆和子智能体。渠道和定时任务在发布后生效。

### 草稿版本与已发布版本 <a id="draft-and-published-versions"></a>

每个智能体都有一个**草稿**版本，准备就绪后可以发布为已发布版本。你在草稿中进行修改，n8n 会自动保存。当用户与智能体聊天、渠道触发智能体或定时任务执行时，运行的是已发布版本。

发布会为草稿创建快照，因此编辑时不会改变正在运行的智能体。每次发布都会在发布历史中新增一个版本，你可以随时恢复或回退到早期版本。

### 构建智能体 <a id="build-an-agent"></a>

在 Agent Builder 中构建智能体。先设置名称和模型，再添加指令，然后配置所需的工具、技能、知识、记忆和子智能体。n8n 会自动将修改保存到草稿。

#### 创建智能体 <a id="create-the-agent"></a>

1. 从左侧菜单选择项目，然后进入 **Agents（智能体）**标签页。
2. 选择 **Create Agent（创建智能体）**。n8n 会打开 Agent Builder，并创建空白草稿。
3. 在 **Agent（智能体）**标签页中输入名称。可以使用图标选择器更换图标。

{% hint style="info" %}
**使用 n8n Assistant**

向 [n8n Assistant](../ways-of-building-workflows/n8n-assistant.md) 描述你希望智能体完成的任务。它会建议要添加的指令、工具和技能。你可以在 Agent Builder 中逐步完善这些建议。
{% endhint %}

#### 选择模型 <a id="choose-a-model"></a>

在 **Agent（智能体）**标签页中打开 Model 字段，选择提供商和模型。如果提供商需要凭据，请按提示添加。

#### 编写指令 <a id="write-instructions"></a>

在 **Instructions（指令）**字段中描述智能体的角色、语气、响应格式、应该和不应该做的事，以及处理常见任务时优先使用的工具或技能。

指令应具体明确。如果智能体的行为不符合预期，先完善指令，再考虑添加更多工具。

#### 添加工具 <a id="add-tools"></a>

在 **Tools（工具）**部分选择 **Add tool（添加工具）**，可以选择内置工具（Slack、Google Sheets 等 n8n 集成）、同一项目中的工作流、通过 JSON schema 定义的自定义工具，或通过 [MCP 服务器](../integrate-ai/mcp-servers.md)提供的外部工具。

智能体会根据指令和任务决定使用哪个工具，并使用添加工具时关联的凭据。对于敏感工具，可以要求智能体在运行前先获得批准。参阅[批准工具调用](#approve-tool-calls)。

#### 启用网页搜索 <a id="enable-web-search"></a>

在 **Capabilities（能力）**部分启用 **Web search（网页搜索）**，让智能体查询价格、文档和新闻等最新信息，无需手动添加搜索工具。

* 如果所选模型提供原生网页搜索工具，智能体会直接使用。
* 如果模型不提供原生搜索，请选择 [Brave Search](../../integrations/builtin/credentials/bravesearch.md) 或自托管 [SearXNG](../../integrations/builtin/credentials/searxng.md) 实例作为备用服务，并添加相应凭据。

#### 使用技能组合能力 <a id="bundle-capabilities-with-skills"></a>

技能将指令与完成特定任务所需的工具打包在一起。当智能体需要处理多个不同任务，而每个任务都有各自的步骤时，可以使用技能。

添加技能的方法：

1. 打开 **Skills（技能）**部分，选择 **Add skill（添加技能）**。
2. 为技能命名，并填写简短说明。
3. 选择技能可以使用的工具。
4. 编写智能体运行该技能时应遵循的指令。

智能体会根据技能说明和当前请求选择合适的技能。

#### 上传知识 <a id="upload-knowledge"></a>

在 **Knowledge（知识）**标签页中添加智能体可以搜索和读取的文件。支持的文件类型：csv、pdf、markdown、txt。

{% hint style="info" %}
**功能可用范围**

n8n Cloud 支持知识库。自托管环境需要 Daytona 沙箱。参阅[自托管](#self-hosted)。
{% endhint %}

{% hint style="info" %}
**预览状态**

自托管环境中的知识库处于预览阶段，可能在后续版本中发生变化。
{% endhint %}

上传文件后，智能体就可以搜索知识库来回答问题和获取上下文。

#### 配置记忆 <a id="configure-memory"></a>

会话记忆保留当前对话的上下文，默认开启，无需设置。

要让智能体回想早期会话的上下文：

1. 打开 **Memory（记忆）**标签页。
2. 启用 **Episodic memory（情景记忆）**。

情景记忆需要 OpenAI 凭据来存储和检索记忆。

#### 添加子智能体 <a id="add-sub-agents"></a>

子智能体允许当前智能体将工作交给其他已发布的智能体。当任务可以清晰分成几个部分，且专门的智能体能更好地处理各部分时，可以使用子智能体。

1. 在能力列表中打开 **Agents（智能体）**部分。
2. 选择 **Add agent（添加智能体）**，从项目中选择一个已发布的智能体。
3. 在 **When should this agent be used?（何时使用此智能体？）**中，描述应调用该子智能体的场景。

你可以在智能体设置中指定并行运行子智能体的最大数量。

#### 预览智能体 <a id="preview-your-agent"></a>

选择页面顶部的 **Preview（预览）**，无需发布即可测试智能体。n8n 会使用当前草稿启动聊天会话。发布前，可以通过预览检查智能体的行为、工具选择和响应。

如果 **Preview（预览）**不可用，说明草稿存在配置错误。n8n 会列出需要解决的项目。

### 发布智能体 <a id="publish-an-agent"></a>

发布后，用户、渠道和定时任务才能使用智能体。生产环境只运行已发布版本，因此你可以继续编辑草稿，不影响用户看到的版本或定时任务使用的版本。

1. 在 Agent Builder 中打开智能体。
2. 检查错误。如果 **Publish（发布）**不可用，n8n 会列出需要解决的配置项目。
3. 选择 **Publish（发布）**。

发布会为当前草稿创建快照，并将其标记为当前生效版本。

#### 更新已发布的智能体 <a id="update-a-published-agent"></a>

智能体发布后，后续修改会进入草稿。已发布版本会继续运行，直到再次发布。

要让修改生效：

1. 在 Agent Builder 中编辑草稿。n8n 会自动保存修改。
2. 使用 **Preview（预览）**测试修改。
3. 再次选择 **Publish（发布）**，发布新版本。

要丢弃未保存的修改并恢复为已发布版本，请从发布菜单选择 **Revert changes（撤销更改）**。

#### 取消发布智能体 <a id="unpublish-an-agent"></a>

要将智能体下线，同时将草稿保留在项目中，请从发布菜单选择 **Unpublish（取消发布）**。再次发布前，用户、渠道和定时任务都无法运行该智能体。草稿仍可编辑。

### 与已发布的智能体聊天 <a id="chat-with-a-published-agent"></a>

通过 Agent Builder 的聊天面板，可以直接与智能体对话。

1. 打开聊天面板。
2. 输入并发送消息。智能体会启动会话并响应。
3. 要查看或继续之前的对话，请打开会话历史并选择相应会话。

n8n 将每次对话存储为一个会话。在 **Sessions（会话）**标签页中，可以查看消息往来、智能体使用的工具和待处理的审批。

#### 批准工具调用 <a id="approve-tool-calls"></a>

对于敏感工具，智能体会暂停并请求批准，然后才运行工具。在聊天中选择 **Approve（批准）**以允许工具运行，或选择 **Reject（拒绝）**以取消调用。智能体会根据你的决定继续处理。

### 通过其他地方使用智能体 <a id="reach-agents-from-other-places"></a>

连接渠道，让用户可以在 Agent Builder 的聊天界面以外联系智能体。

可用渠道：

* **Slack**
* **Telegram**
* **Linear**
* **Microsoft Teams**：参阅[将智能体连接到 Microsoft Teams](microsoft-teams/README.md)。

打开智能体的 **Channels（渠道）**部分，按照所需渠道的设置步骤操作。每个渠道都有自己的连接方式和权限模型。

### 通过 MCP 管理智能体 <a id="manage-agents-through-mcp"></a>

你也可以使用 n8n 的[实例级 MCP 服务器](../../connect/connect-to-n8n-mcp-server.md)，从 Claude Desktop、Claude Code 等 MCP 客户端构建和管理智能体。除了 MCP 服务器原有的工作流工具，这种方式还提供搜索、创建和配置智能体的工具。

{% hint style="info" %}
**重新连接现有 MCP 客户端**

如果在智能体功能推出之前已将 MCP 客户端连接到 n8n 实例，需要重新连接客户端才能使用智能体管理工具。进入 **Settings > Instance-level MCP（设置 > 实例级 MCP）**并重新连接客户端，获取通过 MCP 管理智能体的新权限。
{% endhint %}

### 按计划运行智能体 <a id="run-agents-on-a-schedule"></a>

定时任务让智能体能够按周期自主运行。在 **Schedules（定时任务）**部分添加计划，描述智能体应完成的任务，并选择频率：

* 每小时
* 每天
* 每周
* 每月
* 自定义 cron

定时任务只运行智能体的已发布版本。n8n 会为每个定时任务显示下次运行时间、上次运行时间和上次运行结果。

### 在工作流中使用智能体 <a id="use-agents-in-workflows"></a>

可以通过两种方式在工作流中使用智能体：

* **直接创建智能体**：直接在工作流中添加智能体节点，无需离开工作流编辑器即可构建和配置智能体。
* **向现有智能体发送消息**：从工作流向已经创建的智能体发送消息，访问已发布智能体，并将其能力整合进自动化流程。

#### Message an Agent 节点 <a id="message-an-agent-node"></a>

两种方式都使用 [Message an Agent](../../integrations/builtin/core-nodes/n8n-nodes-base.messageanagent.md) 节点。选择要联系的智能体，并编写消息。智能体会运行自己的推理循环，调用自己的工具和技能，再返回供后续节点使用的回复。

该节点还支持：

* 通过连接的 Chat 和 Webhook 触发器，流式传输智能体正在生成的回复。
* 复用会话，让智能体记住之前的消息。不提供会话时，每次执行都会开始新的对话。
* 将回复约束为 JSON schema，让后续节点收到可预期的字段。

每条消息计为一次执行，与其他工作流执行相同。

要让一个智能体向另一个智能体交接工作，请将 **Message an Agent Tool** 连接到 AI Agent 节点的 **Tool** 输入端。

### 自托管 <a id="self-hosted"></a>

在自托管 n8n 中，有两种智能体设置方式：

* **手动构建**：智能体默认启用。自行选择模型、编写指令并配置工具和技能。实例所有者或管理员可以在 **Settings > Agents（设置 > 智能体）**中启用或禁用智能体。
* **完整体验**：同时设置 [n8n Assistant](../../deploy/host-n8n/configure-n8n/set-up-n8n-assistant.md)（`instance-ai`），以支持 AI 辅助构建：描述智能体需求，由 n8n 搭建初始结构。知识库需要配置沙箱，连接渠道则需要公开可访问的 `WEBHOOK_URL`。

{% hint style="info" %}
**功能可用范围**

自 n8n 2.32.3 起，所有自托管套餐都支持智能体。
{% endhint %}

{% hint style="warning" %}
智能体暂不支持队列模式，连接 Telegram 等渠道时可能失败。目前请在常规模式下运行智能体。
{% endhint %}

环境变量和设置步骤请参阅[启用智能体](../../deploy/host-n8n/configure-n8n/set-up-n8n-assistant.md#enable-agents)。

### 智能体执行与计费 <a id="agent-executions-and-pricing"></a>

与智能体交互一轮计为一次执行。一轮指一次消息交换：你发送一条消息，智能体生成一条响应。

智能体与工作流共享执行配额。智能体和工作流的执行次数计入套餐中的同一个总量。

## 相关资源 <a id="related-resources"></a>

* [构建](../README.md)
* [理解工作流](../understand-workflows/README.md)
* [构建工作流的方式](../ways-of-building-workflows/README.md)
* [管理工作流](../manage-workflows/README.md)
* [流程逻辑](../flow-logic/README.md)
* [处理数据](../work-with-data/README.md)
* [在 n8n 中编写代码](../code-in-n8n/README.md)
* [集成 AI](../integrate-ai/README.md)
* [键盘快捷键](../keyboard-shortcuts.md)
