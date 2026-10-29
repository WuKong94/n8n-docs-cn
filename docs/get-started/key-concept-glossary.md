---
title: n8n 词汇表
description: 解释 n8n 在工作流、智能体、AI 和托管方面使用的术语，并提供各概念的详细说明链接。
contentType: reference
nodeTitle: 核心概念词汇表
originalFilePath: glossary.md
originalUrl: 'https://docs.n8n.io/glossary'
url: 'https://docs.n8n.io/get-started/key-concept-glossary'
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


本词汇表解释了 n8n 在构建、运行和管理工作流及智能体时使用的术语。每个条目都链接到详细说明该概念的页面。

## 工作流基本组件 <a id="workflow-building-blocks"></a>

### 画布（n8n） <a href="#canvas-n8n" id="canvas-n8n"></a>

画布是 n8n 编辑器界面中构建工作流的主要区域。你可以在画布上添加和连接节点，组成工作流。了解更多：[创建并运行工作流](../build/understand-workflows/create-and-run-workflows.md)。

### 社区节点（n8n） <a href="#community-node-n8n" id="community-node-n8n"></a>

社区节点由社区开发并共享，属于 n8n 内置节点之外的节点。你可以在实例上安装社区节点，添加 n8n 未提供的集成。了解更多：[使用社区节点](../integrations/community-nodes/using-community-nodes.md)。

### 凭据（n8n） <a href="#credential-n8n" id="credential-n8n"></a>

在 n8n 中，凭据保存连接特定应用和服务所需的身份验证信息。使用用户名和密码、API 密钥、OAuth 密钥等信息创建凭据后，即可通过对应的应用节点与服务交互。了解更多：[创建和编辑凭据](../build/understand-workflows/create-and-edit-credentials.md)。

### 编辑器（n8n） <a href="#editor-n8n" id="editor-n8n"></a>

n8n 编辑器界面用于创建和管理工作流。其主要区域是画布，你可以在这里添加、配置和连接节点来组成工作流。侧边和顶部面板提供凭据、模板、变量、执行等其他界面的入口。了解更多：[创建并运行工作流](../build/understand-workflows/create-and-run-workflows.md)。

### 表达式（n8n） <a href="#expression-n8n" id="expression-n8n"></a>

在 n8n 中，表达式通过执行 JavaScript 代码动态填充节点参数。你可以使用 n8n 表达式语法，根据先前节点、其他工作流或 n8n 环境中的数据确定值，而不是填写固定值。了解更多：[使用表达式转换数据](../build/work-with-data/transform-data/expressions-for-data-transformation.md)。

### 节点（n8n） <a href="#node-n8n" id="node-n8n"></a>

在 n8n 中，节点是组成工作流的独立组件。有些节点启动工作流，其他节点则获取、发送和处理数据，定义流程控制逻辑，或连接外部服务。了解更多：[使用节点](../build/understand-workflows/workflow-components/work-with-nodes.md)。

### 子工作流（n8n） <a id="sub-workflow-n8n"></a>

子工作流是由另一个工作流调用的工作流。使用子工作流可以将大型工作流拆分成较小、可复用的部分。了解更多：[子工作流](../build/flow-logic/break-workflows-into-smaller-parts.md)。

### 模板（n8n） <a href="#template-n8n" id="template-n8n"></a>

n8n 模板是由 n8n 和社区成员设计的预构建工作流，可以导入你的 n8n 实例。使用模板时，可能需要填写凭据，并根据自己的需求调整配置。了解更多：[工作流模板](../build/ways-of-building-workflows/use-templates.md)。

### 触发器节点（n8n） <a href="#trigger-node-n8n" id="trigger-node-n8n"></a>

触发器节点是一种特殊节点，负责在满足特定条件时触发工作流执行。所有生产工作流都至少需要一个触发器，来确定何时运行。了解更多：[触发器节点](../integrations/builtin/trigger-nodes/README.md)。

### 工作流（n8n） <a href="#workflow-n8n" id="workflow-n8n"></a>

n8n 工作流是用于自动执行某个流程的一组节点。触发条件出现、手动运行或被另一个工作流调用时，工作流便会开始执行。它逐个节点执行，并通过分支、合并和循环完成复杂任务。了解更多：[创建并运行工作流](../build/understand-workflows/create-and-run-workflows.md)。

## 数据 <a id="data"></a>

### 二进制数据（n8n） <a id="binary-data-n8n"></a>

二进制数据指图片、文档等文件类型的数据。数据项将二进制数据保存在 `binary` 对象中，与 `json` 数据分开。了解更多：[二进制数据](../build/work-with-data/handle-special-data-types/work-with-files-and-images.md)。

### 数据固定（n8n） <a href="#data-pinning-n8n" id="data-pinning-n8n"></a>

数据固定允许你在开发工作流时暂时冻结节点的输出数据。这样无需反复请求外部服务，就能使用可预测的数据进行开发。生产工作流会忽略固定数据，每次执行时都请求新数据。了解更多：[模拟和固定数据](../build/work-with-data/pin-and-mock-data.md)。

### 数据表（n8n） <a id="data-table-n8n"></a>

数据表在 n8n 内部保存结构化的表格数据，因此不需要外部数据库。数据表归属于某个[项目](#project-n8n)，该项目中的工作流可通过[Data Table 节点](../integrations/builtin/core-nodes/n8n-nodes-base.datatable/README.md)读写数据表。你也可以在 Data tables（数据表）标签页及通过 [n8n API](../connect/n8n-api/api-reference.md) 管理数据表。数据表适用于轻量到中等规模的数据存储。了解更多：[数据表](../build/work-with-data/data-tables.md)和[Data Table 节点](../integrations/builtin/core-nodes/n8n-nodes-base.datatable/README.md)。

### 变量（n8n） <a id="variable-n8n"></a>

自定义变量保存可在多个工作流中复用的只读字符串。变量可以是全局变量，供整个实例使用；也可以限定在单个项目内。了解更多：[自定义变量](../build/code-in-n8n/define-custom-variables.md)。

## n8n 中的智能体和 AI <a id="agents-and-ai-in-n8n"></a>

### 智能体（n8n） <a id="agent-n8n"></a>

智能体是你在 n8n 中构建的自主助手。每个智能体都包含语言模型、指令，以及你配置的工具、[技能](#skill-n8n)、记忆、[知识库](#knowledge-base-n8n)和[子智能体](#sub-agent-n8n)等能力。智能体是项目中的独立条目，不属于工作流；用户通过聊天、渠道和时间计划与之交互。智能体目前处于预览阶段。请勿将它与运行在工作流中的 [AI Agent 节点](#ai-agent-node-n8n)混淆。了解更多：[构建和管理智能体](../build/build-and-manage-agents/README.md)。

### AI 智能体 <a href="#ai-agent" id="ai-agent"></a>

AI 智能体是一种 AI 系统，使用大语言模型（LLM）理解请求，并决定调用工具等操作以完成请求。在 n8n 中，可以通过两种方式构建 AI 智能体：创建独立的[智能体](#agent-n8n)，或在工作流中使用 [AI Agent 节点](#ai-agent-node-n8n)。了解更多：[AI 中的智能体是什么？](../build/integrate-ai/understand-ai-components/what-agents-do.md)。

### AI Agent 节点（n8n） <a id="ai-agent-node-n8n"></a>

AI Agent 节点为工作流添加 AI 智能体。它是一个集群节点：以根节点为核心，通过聊天模型、工具、记忆等子节点扩展能力。它与在 Agent Builder（智能体构建器）中创建的[智能体](#agent-n8n)属于不同功能。了解更多：[AI Agent 节点](../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/README.md)。

### AI 链 <a href="#ai-chain" id="ai-chain"></a>

AI 链按固定顺序调用 LLM 和其他组件。与智能体不同，链不会自行决定执行哪些步骤。n8n 中的 AI 链不使用持久记忆，因此无法借助它引用先前的上下文（这种情况应使用 AI 智能体）。了解更多：[AI 中的链是什么？](../build/integrate-ai/understand-ai-components/what-chains-do.md)。

### AI 记忆 <a href="#ai-memory" id="ai-memory"></a>

在 AI 场景中，记忆让 AI 工具能够在多次交互之间保留消息上下文。例如，你可以持续与 AI 智能体对话，而不必每次都提交之前的上下文。在 n8n 中，独立智能体和 AI Agent 节点都能使用记忆，但 AI 链不能。了解更多：[AI 中的记忆是什么？](../build/integrate-ai/understand-ai-components/how-memory-works.md)。

### AI 工具 <a href="#ai-tool" id="ai-tool"></a>

在 AI 场景中，工具是 AI 响应请求时可使用的附加资源，用于获取特定信息或能力。AI 模型可以通过工具与外部系统交互，或完成特定且范围明确的任务。了解更多：[AI 中的工具是什么？](../build/integrate-ai/understand-ai-components/how-tools-work.md)。

### 集群节点（n8n） <a href="#cluster-node-n8n" id="cluster-node-n8n"></a>

在 n8n 中，集群节点由一组协同工作的节点组成，为工作流提供智能体、链、向量存储等 AI 功能。它包含一个根节点，以及一个或多个用于扩展能力的子节点。例如，AI Agent 根节点通过子节点获得聊天模型、记忆和工具。n8n 将大多数 LangChain 概念表示为集群节点。了解更多：[集群节点](../integrations/builtin/cluster-nodes/README.md)。

### 知识库（n8n） <a id="knowledge-base-n8n"></a>

知识库是[智能体](#agent-n8n)在回答问题时可搜索和读取的一组文件，为回答提供上下文。你可以向智能体上传 CSV、PDF、Markdown、文本等文件。知识库在 n8n Cloud 上可用，在自托管实例上处于预览阶段。了解更多：[构建和管理智能体](../build/build-and-manage-agents/README.md#upload-knowledge)。

### 模型上下文协议（MCP） <a id="model-context-protocol-mcp"></a>

模型上下文协议（MCP）是一项开放标准，让 AI 客户端能够连接外部工具和数据。n8n 同时支持协议的两端：

- **作为 MCP 客户端**：n8n 允许智能体和 AI Agent 节点使用 MCP 服务器上的工具，可通过一键式服务器注册表或 MCP Client Tool 节点连接。
- **作为 MCP 服务器**：n8n 允许 Claude 等 MCP 客户端连接你的实例。实例级 MCP 服务器让客户端可以构建、编辑、运行和测试工作流，并管理数据表和智能体。MCP Server Trigger 节点则将单个工作流的工具暴露为独立的 MCP 服务器。

了解更多：[MCP 服务器](../build/integrate-ai/mcp-servers.md)和[设置和使用 n8n MCP 服务器](../connect/connect-to-n8n-mcp-server.md)。

### n8n Assistant <a id="n8n-assistant"></a>

n8n Assistant 是 n8n 内置的聊天式智能体，可根据自然语言帮助你创建、编辑、测试工作流并排查问题。它还能构建智能体并协助处理实例相关任务。n8n Assistant 目前处于预览阶段。了解更多：[使用 n8n Assistant](../build/ways-of-building-workflows/n8n-assistant.md)。

### 根节点（n8n） <a href="#root-node-n8n" id="root-node-n8n"></a>

每个 n8n 集群节点都包含一个根节点，定义集群的主要功能，例如运行 AI 智能体或链。一个或多个子节点连接到根节点，以扩展其功能。了解更多：[集群节点](../integrations/builtin/cluster-nodes/README.md)。

### 技能（n8n） <a id="skill-n8n"></a>

技能将某项任务所需的指令和工具打包在一起。向智能体添加技能，即可复用相应行为。了解更多：[构建和管理智能体](../build/build-and-manage-agents/README.md#bundle-capabilities-with-skills)。

### 子智能体（n8n） <a id="sub-agent-n8n"></a>

子智能体是已发布的智能体，其他智能体可以将工作移交给它。当任务可以拆分为多个部分，且由专门的智能体处理每个部分更合适时，可以使用子智能体。了解更多：[构建和管理智能体](../build/build-and-manage-agents/README.md#add-sub-agents)。

### 子节点（n8n） <a href="#sub-node-n8n" id="sub-node-n8n"></a>

n8n 集群节点由一个根节点和一个或多个与之相连的子节点组成。子节点扩展根节点的功能，提供聊天模型、记忆、向量存储等特定服务或资源，也可提供计算器等专用处理能力。了解更多：[子节点](../integrations/builtin/cluster-nodes/sub-nodes/README.md)。

### 工具审批（n8n） <a id="tool-approval-n8n"></a>

工具审批是针对 AI 工具调用的人在回路检查机制。对于敏感工具，智能体会在执行前暂停，等待人员批准或拒绝调用。了解更多：[构建和管理智能体](../build/build-and-manage-agents/README.md#approve-tool-calls)和[AI 工具调用中的人在回路](../build/integrate-ai/ai-examples/human-in-the-loop-for-tools.md)。

## 组织、运行与发布 <a id="organize-run-and-publish"></a>

### 草稿（n8n） <a id="draft-n8n"></a>

草稿是工作流或智能体正在编辑的版本。n8n 会自动将修改保存到草稿中，只有发布后，草稿才会在生产环境运行。另请参阅[发布](#publish-n8n)。了解更多：[保存和发布工作流](../build/understand-workflows/save-and-publish-workflows.md)。

### 评估（n8n） <a href="#evaluation-n8n" id="evaluation-n8n"></a>

评估通过使用一组测试用例运行工作流，并将结果与预期输出或指标比较，来测试工作流。修改模型、提示词或逻辑时，可以通过评估确认 AI 工作流仍然可靠。了解更多：[评估](../build/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test.md)。

### 执行（n8n） <a id="execution-n8n"></a>

执行是工作流的一次运行。在编辑器中主动运行工作流时，会启动手动执行；已发布工作流的触发器触发时，会自动启动生产执行。了解更多：[执行](../build/understand-workflows/understand-executions/README.md)。

### 项目（n8n） <a href="#project-n8n" id="project-n8n"></a>

n8n 项目允许你将工作流、变量、凭据、数据表和智能体分组管理。通过共享和划分相关资源，项目让团队协作更加方便。你可以在各项目中为用户分配角色，因此同一个人在不同项目中可以拥有不同角色。了解更多：[RBAC 项目](../administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects.md)。

### 发布（n8n） <a id="publish-n8n"></a>

编辑工作流时，n8n 会将修改保存为草稿。准备好投入生产环境后，即可发布一个版本。触发器触发时，将运行已发布的版本。了解更多：[保存和发布工作流](../build/understand-workflows/save-and-publish-workflows.md)。

## 托管、版本与许可 <a id="hosting-editions-and-licensing"></a>

### 版本（n8n） <a href="#edition-n8n" id="edition-n8n"></a>

自托管 n8n 时，版本指你运行的软件类别：社区版、注册社区版、Business 或 Enterprise。所有版本共享相同的基础产品。免费社区版无需许可证密钥即可运行。订阅付费 Business 或 Enterprise 套餐后，你会获得一个许可证密钥，用来解锁该套餐的功能。另请参阅[套餐](#plan-n8n)和[许可](#license-n8n)。了解更多：[比较套餐和版本](../deploy/host-n8n/community-edition-features.md)。

### 授权权益（n8n） <a href="#entitlement-n8n" id="entitlement-n8n"></a>

在 n8n 中，授权权益允许 n8n 实例在一定期限内使用受套餐限制的功能。

浮动授权权益是一组可分配给多个 n8n 实例的权益。你可以重新分配某项浮动权益，将其使用权限转移到另一个 n8n 实例。另请参阅[许可](#license-n8n)和[套餐](#plan-n8n)。了解更多：[许可证密钥](../deploy/host-n8n/configure-n8n/manage-your-license.md)。

### 实例（n8n） <a id="instance-n8n"></a>

实例是单独安装的一套 n8n，可以由 n8n Cloud 托管，也可以自行托管。每个实例都有自己的工作流、用户、凭据和设置。了解更多：[选择 n8n 的使用方式](choose-how-to-use-n8n.md)。

### 许可（n8n） <a href="#license-n8n" id="license-n8n"></a>

在 n8n 中，许可有两种含义：一是分发源代码所依据的法律条款；二是解锁付费套餐功能的许可证密钥。自托管并订阅付费 Business 或 Enterprise 套餐后，需要将许可证密钥添加到实例中，才能激活该套餐的功能。另请参阅[授权权益](#entitlement-n8n)和[套餐](#plan-n8n)。了解更多：[许可证密钥](../deploy/host-n8n/configure-n8n/manage-your-license.md)。

### 套餐（n8n） <a href="#plan-n8n" id="plan-n8n"></a>

套餐是商业订阅档位，例如 Starter、Pro、Business 或 Enterprise。无论使用 n8n Cloud 还是自托管，套餐都会决定订阅包含的功能、用量限制和价格。另请参阅[版本](#edition-n8n)和[许可](#license-n8n)。了解更多：[比较套餐和版本](../deploy/host-n8n/community-edition-features.md)。

### 队列模式（n8n） <a id="queue-mode-n8n"></a>

队列模式是一种自托管扩展架构。主实例接收触发事件，并将执行任务分发给工作实例，由工作实例并行运行。了解更多：[队列模式](../deploy/host-n8n/configure-n8n/scaling/enable-queue-mode.md)。

## 相关资源 <a id="related-resources"></a>

* [n8n 文档](./)
* [选择 n8n 的使用方式](choose-how-to-use-n8n.md)
* [构建你的第一个工作流](build-your-first-workflow.md)
* [学习路径](learning-paths.md)
