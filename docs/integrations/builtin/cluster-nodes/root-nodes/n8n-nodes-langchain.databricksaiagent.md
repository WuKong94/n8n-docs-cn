---
description: 了解如何在 n8n 中使用 Databricks AI Agent 节点，运行 AI 智能体，并将每次运行导出到 Databricks 工作区的
  MLflow Tracing。
status: preview
tags:
- tag: preview
  primary: true
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Databricks AI Agent（Databricks AI 智能体） 节点 <a id="databricks-ai-agent-node"></a>

使用 Databricks AI Agent 节点，构建运行记录可在 Databricks 工作区的 [MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) 中查看的 AI 智能体[^1]。此节点运行的智能体与 [AI Agent](n8n-nodes-langchain.agent/README.md) 节点相同：接受相同的聊天模型、记忆、工具[^2]和输出解析器子节点，并提供相同的选项。它额外提供 **Export Traces to MLflow**（将追踪导出到 MLflow）功能。开启后，每次运行都会在 MLflow 实验中创建一条追踪，并为每次模型调用和工具调用创建一个跨度（span），方便 Databricks 工作区运维团队将 n8n 智能体与其他 AI 系统一并检查。

本页介绍前置条件、设置步骤、节点参数、追踪包含的内容，以及发生故障时的导出行为。

{% hint style="info" %}
**凭据**

身份验证设置指南，请参阅 [Databricks 凭据](../../credentials/databricks.md)。此节点的凭据为可选项。智能体使用所连接聊天模型子节点的凭据运行；此节点自己的 **Databricks OAuth2 API** 凭据仅用于导出追踪，因此开启 **Export Traces to MLflow**（将追踪导出到 MLflow）时需要选择此凭据。
{% endhint %}

{% hint style="info" %}
**预览状态**

Databricks AI Agent 节点从 n8n 2.45.0 起处于预览阶段，未来版本中可能发生变化。请避免在生产工作流中依赖此节点。
{% endhint %}

## 前置条件 <a id="prerequisites"></a>

运行智能体需要一个具有自身凭据的聊天模型子节点，例如 [Databricks Chat Model](../sub-nodes/n8n-nodes-langchain.lmchatdatabricks.md) 节点。导出追踪还需要：

- n8n 中通过服务主体或用户登录配置的 [Databricks OAuth2 凭据](../../credentials/databricks.md#supported-authentication-methods)。服务主体必须是工作区成员，并具有 **Workspace access**（工作区访问）授权。
- 对接收追踪的实验具有 **CAN EDIT** 权限。**CAN READ** 权限不足：导出会失败，并返回 `403`，说明该身份没有编辑实验的权限。
- 节点在 `/Shared` 下创建的默认实验不需要额外授权。默认情况下，Databricks 为所有工作区用户授予 `/Shared` 文件夹内对象的 **CAN MANAGE** 权限，因此该身份可以创建实验并向其写入数据。这也意味着每个工作区用户都可以打开和删除这些追踪。对于处理个人或机密数据的工作流，请将 **Experiment**（实验）设置为你控制的文件夹中的路径。也可先创建实验并设置权限，再开启导出。

权限变更需要一分钟或更长时间才能传递到追踪服务。变更后立即运行，可能仍使用旧权限。

## 设置节点 <a id="set-up-the-node"></a>

1. 向工作流添加 **Databricks AI Agent** 节点，例如放在 [Chat Trigger](../../core-nodes/n8n-nodes-langchain.chattrigger/README.md) 节点之后。
2. 点击 **Chat Model**（聊天模型）连接器上的 **+**，添加聊天模型，例如 [Databricks Chat Model](../sub-nodes/n8n-nodes-langchain.lmchatdatabricks.md) 节点。按照与 [AI Agent](n8n-nodes-langchain.agent/README.md) 节点相同的方式，添加记忆、工具和输出解析器。[Databricks Vector Store](n8n-nodes-langchain.vectorstoredatabricks/README.md) 节点和 [Databricks Genie One MCP 服务器](../sub-nodes/n8n-mcp-registry.databricksgenie.md)均可用作工具。
3. 设置 **Source for Prompt (User Message)**（提示词来源，用户消息）和[节点选项](#node-options)。
4. 如需导出追踪，在 **Credential to connect with**（连接凭据）中选择 Databricks OAuth2 凭据，并开启 **Export Traces to MLflow**（将追踪导出到 MLflow）。
5. 在 **Experiment**（实验）中，将名称留空，让节点为工作流创建实验；也可输入现有实验的路径或 ID。请参阅[节点参数](#node-parameters)。
6. 运行工作流。在 Databricks 中，打开侧边栏的 **Experiments**（实验），选择实验，再打开 **Traces**（追踪）选项卡。每次智能体运行显示为一条追踪，并提供问题和答案预览。

## 节点参数 <a id="node-parameters"></a>

- **Source for Prompt (User Message)**（提示词来源，用户消息）：用户消息的来源，可选 **Connected Chat Trigger Node**（已连接的聊天触发器节点）或 **Define below**（在下方定义）。其行为与 [AI Agent](n8n-nodes-langchain.agent/README.md) 节点的同名字段相同。此节点不提供 **Connected Guardrails Node**（已连接的 Guardrails 节点）来源。
- **Require Specific Output Format**（要求指定输出格式）：开启后可连接输出解析器子节点，规定智能体的输出格式。
- **Enable Fallback Model**（启用备用模型）：开启后可连接第二个聊天模型，主模型失败时由智能体使用。
- **Export Traces to MLflow**（将追踪导出到 MLflow）：是否将每次运行发送到此节点所选凭据对应工作区的 MLflow Tracing。默认关闭。
- **Experiment**（实验）：追踪的存储位置。开启 **Export Traces to MLflow**（将追踪导出到 MLflow）时显示。
    - **By Name**（按名称）：实验路径，例如 `/Shared/my-agent-traces`。实验不存在时，节点会创建实验。留空则使用 `/Shared/n8n-workflows-<workflow-id>`，每个工作流对应一个实验。
    - **By ID**（按 ID）：现有实验的数字 ID，可在 Databricks 中该实验的 URL 中找到。ID 不存在不会导致运行失败：智能体会作答，随后导出失败，并在 n8n 日志中记录警告。

## 节点选项 <a id="node-options"></a>

这些选项与 AI Agent 节点相同。**System Message**（系统消息）、**Max Iterations**（最大迭代次数，默认 `10`）、**Return Intermediate Steps**（返回中间步骤）、**Automatically Passthrough Binary Images**（自动透传二进制图像）、**Tracing Metadata**（追踪元数据）和 **Enable Streaming**（启用流式输出）的说明，请参阅 [Tools Agent](n8n-nodes-langchain.agent/tools-agent.md)。另有两个选项：

- **Automatically Passthrough Binary PDFs**（自动透传二进制 PDF）：是否将输入中的二进制 PDF 文档作为消息的一部分传给模型。默认关闭。请搭配支持 PDF 输入的模型使用。
- **Batch Processing**（批量处理）：**Batch Size**（批次大小）设置智能体一次处理的输入项数量（默认 `1`）；**Delay Between Batches**（批次间延迟）设置批次之间等待的毫秒数（默认 `0`）。可用此功能避免超过按 token 计费的模型服务的速率限制。

## 节点导出的内容 <a id="what-the-node-exports"></a>

节点处理的每个数据项对应一条追踪。追踪包含由跨度组成的树：

- 顶层是智能体运行，以用户消息为输入，以最终答案为输出。
- 每次模型调用对应一个跨度，包含发送给模型的完整消息列表，以及 OpenAI 格式的模型补全结果。消息列表包含系统消息、从记忆加载的对话历史，以及以 base64 传给模型的图像或 PDF。跨度还记录工具调用和本次调用的 token 用量。
- 每次工具调用对应一个跨度，包含参数和结果。向量存储工具的跨度会显示其返回的文档。
- 当 Vector Store Question Answer Tool 等工具通过检索器查询向量存储时，每次检索器调用对应一个跨度。

每个跨度都包含开始和结束时间。追踪本身包含：

- `client_request_id`：n8n 执行 ID，用于将工作区中的追踪对应到 n8n 中的一次执行。
- 标签 `n8n.source`（`n8n`）、`n8n.workflowId` 和 `n8n.node`（节点名称）。
- 请求预览和响应预览，即问题和答案的前 1,000 个字符，显示为追踪列表中的两列。
- 本次运行的总 token 用量，使追踪列表无需打开跨度即可显示每次运行的成本。
- 状态：`OK`，或运行失败时的 `ERROR`。模型调用失败时，追踪变为 `ERROR`，模型跨度中包含 Databricks 错误消息。工具抛出异常时，记录为 `ERROR` 工具跨度；如果智能体恢复并作答，追踪仍保持 `OK`。

流式运行会导出相同的跨度，并填入结束时间和 token 数。取消运行时，导出也随之停止。实验中可能没有本次运行的追踪，也可能有一条不含跨度的追踪。无论哪种情况，n8n 都会记录导出失败。模型跨度命名为 `ChatOpenAI`，而非模型服务名称，因为 Databricks Chat Model 节点通过兼容 OpenAI 的客户端调用网关。

{% hint style="warning" %}
**追踪包含你的数据**

追踪导出会将每次运行的真实提示词（包括系统消息和记忆）、模型输出、工具结果以及检索到的文档，发送到所选凭据对应的 Databricks 工作区。在跨度内，n8n 仅对已知 token 格式和 `password=...` 等带标签的秘密信息进行脱敏，不会脱敏其他内容。追踪列表中的问题和答案预览不会脱敏。导出默认关闭，数据仅发送到你自己的工作区，不会发送给 n8n 或第三方。对于处理个人或机密数据的工作流，开启此功能前，请与安全团队确认设置。
{% endhint %}

## 导出失败时的行为 <a id="how-export-failures-behave"></a>

追踪导出用于可观测性，因此不会改变运行结果：

- 因凭据不可用、实验查找失败或身份权限不足，导致节点无法准备导出时，智能体仍会运行并作答。n8n 会将 `Databricks AI Agent: could not prepare MLflow trace export` 及其原因写入日志。
- 运行结束后追踪写入失败时，运行输出仍有效，n8n 会记录 `Databricks AI Agent: MLflow trace export failed` 及 Databricks 错误。此警告仅显示在 n8n 服务器日志中，不会显示在执行中。
- 可能发生部分导出：Databricks 可以注册追踪，但拒绝上传其跨度，此时列表中会出现不含跨度的追踪。
- 唯一会直接导致失败的情况是缺少凭据。开启 **Export Traces to MLflow**（将追踪导出到 MLflow）却未选择凭据时，节点会在调用任何模型之前失败，返回 `Select a Databricks credential to export traces to MLflow`。

每条追踪的导出包含三次调用：在实验中注册追踪、请求带签名的上传 URL、将跨度上传到该 URL。上传 URL 自带短期有效的凭据，因此工作区 token 不会发送到该 URL。

## 相关资源 <a id="related-resources"></a>

- 智能体选项和常见问题，请参阅 [AI Agent](n8n-nodes-langchain.agent/README.md) 和 [Tools Agent](n8n-nodes-langchain.agent/tools-agent.md)
- [Databricks Chat Model](../sub-nodes/n8n-nodes-langchain.lmchatdatabricks.md)
- [Databricks Vector Store](n8n-nodes-langchain.vectorstoredatabricks/README.md)，包括智能体根据 Databricks 索引作答的[完整示例](n8n-nodes-langchain.vectorstoredatabricks/README.md#example-answer-questions-from-a-databricks-index-with-an-ai-agent)
- [Embeddings Databricks](../sub-nodes/n8n-nodes-langchain.embeddingsdatabricks.md)
- [Databricks Genie One MCP 服务器](../sub-nodes/n8n-mcp-registry.databricksgenie.md)
- [Databricks 凭据](../../credentials/databricks.md)
- 从社区包迁移：请参阅[从 n8n-nodes-databricks 社区包迁移](n8n-nodes-langchain.vectorstoredatabricks/migrate-from-the-community-package.md)
- Databricks 文档中的 [MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) 和 [MLflow 实验权限](https://docs.databricks.com/aws/en/security/auth/access-control/#mlflow-experiment-acls)

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 常见问题 <a id="common-issues"></a>

### Select a Databricks credential to export traces to MLflow（请选择 Databricks 凭据以将追踪导出到 MLflow） <a id="select-a-databricks-credential-to-export-traces-to-mlflow"></a>

已开启 **Export Traces to MLflow**（将追踪导出到 MLflow），但节点没有凭据。请在 **Credential to connect with**（连接凭据）中选择 Databricks OAuth2 凭据，或关闭该选项。

### 实验中未出现追踪 <a id="no-traces-appear-in-the-experiment"></a>

运行成功但实验仍为空。请检查 n8n 服务器日志中以 `Databricks AI Agent:` 开头的日志行，其中会说明原因：`403` 表示该身份没有实验的 **CAN EDIT** 权限；`404` 且包含 `RESOURCE_DOES_NOT_EXIST` 表示 **By ID**（按 ID）指定的实验不存在；token 错误则表示凭据无法访问工作区。授予权限后，请等待一分钟再运行。

### 追踪不含跨度 <a id="a-trace-has-no-spans"></a>

Databricks 注册了追踪，但拒绝上传跨度，因此追踪列表显示该运行却没有跨度树。请检查 n8n 服务器日志中的上传错误，以及该身份是否具有实验的 **CAN EDIT** 权限。

### 智能体问题 <a id="agent-issues"></a>

模型不调用工具或触发速率限制等智能体本身的问题，请参阅 Databricks Chat Model 页面的[为智能体选择模型](../sub-nodes/n8n-nodes-langchain.lmchatdatabricks.md#choose-a-model-for-agents)和 AI Agent 的[常见问题](n8n-nodes-langchain.agent/common-issues.md)。

[^1]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大语言模型（LLM）理解用户输入，利用可用的信息和资源，决定如何最好地处理请求。
[^2]: 在 AI 场景中，工具是附加资源，AI 可在响应请求时调用它获取特定信息或功能。AI 模型可以通过工具与外部系统交互，或完成具体、专门的任务。
