---
description: 了解如何在 n8n 中使用 Databricks Chat Model（Databricks 聊天模型） 节点，并按照技术文档将其集成到工作流中。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Databricks Chat Model（Databricks 聊天模型） 节点 <a id="databricks-chat-model-node"></a>

使用 Databricks Chat Model 节点，通过 Databricks 工作区提供的模型运行 AI 智能体和链。节点查询 [Unity AI Gateway 模型服务](https://docs.databricks.com/aws/en/ai-gateway/model-services)，因此支持 Databricks 托管的基础模型，以及通过网关路由的外部提供方。

本页介绍 Databricks Chat Model 节点的前置条件、配置步骤、参数及已知限制。

{% hint style="info" %}
**凭据**

身份验证设置方法，请参阅 [Databricks 凭据](../../credentials/databricks.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 前置条件 <a id="prerequisites"></a>

- 已启用 Unity AI Gateway 的 Databricks 工作区。
- n8n 中的 [Databricks OAuth2 凭据](../../credentials/databricks.md#supported-authentication-methods)，使用服务主体或用户登录。节点不支持个人访问令牌。
- 凭据对应的身份需要对模型服务所在的目录和架构具有 **USE CATALOG** 和 **USE SCHEMA** 权限，并对模型服务具有 **EXECUTE** 权限。Databricks 默认向所有工作区用户授予 `system.ai` 模型服务的 **EXECUTE** 权限。

## 配置节点 <a id="set-up-the-node"></a>

1. 向工作流添加 [AI Agent](../root-nodes/n8n-nodes-langchain.agent/README.md) 节点，或其他接受聊天模型的根节点。
2. 选择节点 **Chat Model**（聊天模型）连接器上的 **+**，再选择 **Databricks Chat Model**。
3. 在 **Credential to connect with**（连接凭据）下，选择现有 Databricks OAuth2 凭据或创建新凭据。按下方与你的身份验证类型对应的步骤配置。
4. 在 **Model**（模型）中打开列表，选择模型服务。n8n 加载凭据可访问、支持聊天的模型服务。要使用未列出的服务，切换为 **ID** 并输入完整名称，例如 `system.ai.databricks-meta-llama-3-3-70b-instruct`。

### 使用服务主体配置 <a id="set-up-with-a-service-principal"></a>

无人值守的工作流，例如定时或 Webhook 触发的智能体，应使用服务主体。

1. 请 Databricks 管理员[创建服务主体和 OAuth 密钥](../../credentials/databricks.md#create-a-service-principal-and-oauth-secret)，并向其授予所需模型服务的 **EXECUTE** 权限。
2. 在 n8n 凭据中，将工作区 URL 填入 **Host**（主机），保持 **Grant Type**（授权类型）为 **Client Credentials (Service Principal)**（客户端凭据，服务主体），输入 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）。
3. 保存凭据，并在节点中选择它。

### 使用用户登录配置 <a id="set-up-with-user-login"></a>

希望智能体以你自己的 Databricks 权限运行，并在 Databricks 审计日志中显示为你的身份时，使用用户登录。

1. 请 Databricks 账户管理员[创建自定义 OAuth 应用连接](../../credentials/databricks.md#create-a-custom-oauth-app-connection)，并向你提供客户端 ID 和密钥。
2. 在 n8n 凭据中，将工作区 URL 填入 **Host**（主机），将 **Grant Type**（授权类型）设为 **Authorization Code (User)**（授权码，用户），输入 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）。
3. 选择 **Connect my account**（连接我的账户），登录 Databricks。
4. 在节点中选择该凭据。长时间执行时，n8n 会刷新访问令牌，因此智能体可运行超过一小时的令牌有效期。

## 节点参数 <a id="node-parameters"></a>

- **Model**（模型）：生成补全的 Unity AI Gateway 模型服务，名称格式为 `catalog.schema.service`。
    - **From List**（从列表选择）：选择凭据可访问、支持聊天补全的模型服务。列表同时包含 `system.ai` 中 Databricks 托管的基础模型和外部提供方路由。
    - **ID**：直接输入模型服务的完整名称。适用于支持聊天、但未声明具备聊天能力的服务。

## 节点选项 <a id="node-options"></a>

- **Frequency Penalty**（频率惩罚）：根据新 token 已在文本中出现的频率施加惩罚，减少逐字重复。范围为 `-2` 至 `2`，默认值为 `0`。
- **Maximum Number of Tokens**（最大 token 数）：补全中生成的最大 token 数，默认为 `-1`，即 n8n 不设置上限。
- **Response Format**（响应格式）：**Text**（文本，默认）或 **JSON**。JSON 模式要求提示词包含 `json` 一词，且模型服务支持 JSON 模式。
- **Presence Penalty**（存在惩罚）：根据新 token 是否已在文本中出现施加惩罚，鼓励新话题。范围为 `-2` 至 `2`，默认值为 `0`。
- **Sampling Temperature**（采样温度）：控制随机性，较低值使补全更确定。范围为 0 到 2，默认为 0.7。
- **Timeout**（超时）：请求的最长耗时，单位为毫秒，默认为 360000（六分钟）。
- **Max Retries**（最大重试次数）：失败请求的重试次数，默认为 2。
- **Top P**：核采样参数。调整此项或 **Sampling Temperature**（采样温度）之一，不要同时调整。范围为 0 到 1，默认为 1。

## 为智能体选择模型 <a id="choose-a-model-for-agents"></a>

并非每个模型服务都能通过此节点作为智能体的工具调用模型。模型必须支持工具调用，而一些声称支持的端点并不返回 AI Agent 可执行的工具调用。n8n 的测试结果如下：

- **Llama 3.3 70B** 和 **Qwen 3.5** 可可靠地调用工具，是 [Databricks Genie One MCP 服务器](n8n-mcp-registry.databricksgenie.md)及其他工具的良好默认选择。
- **gpt-oss** 和 **Llama 4 Maverick** 端点不返回 AI Agent 可执行的工具调用。使用它们的智能体会持续循环，直到达到 **Max Iterations**（最大迭代次数），却未调用任何工具。

工作区可能还列出其他模型服务。测试时，向智能体提出必须调用工具才能回答的问题，再检查执行日志。不适用的模型会表现为相同症状：耗尽全部迭代次数，却没有一次工具调用。

按 token 付费的模型服务按工作区实施速率限制。三个并发智能体运行就足以达到限制，节点会在数秒内用完默认的两次重试。演示、试点和生产智能体应使用[预配吞吐量](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis)端点，或保持较低的智能体并发。

## 相关资源 <a id="related-resources"></a>

- [Databricks 凭据](../../credentials/databricks.md)
- [Databricks 节点](../../app-nodes/n8n-nodes-base.databricks.md)：用于 SQL、Unity Catalog 和 Genie Agent REST 操作。
- [Databricks Genie One MCP 服务器](n8n-mcp-registry.databricksgenie.md)：为智能体提供 Genie One 访问。
- [Databricks Vector Store](../root-nodes/n8n-nodes-langchain.vectorstoredatabricks/README.md) 和 [Embeddings Databricks](n8n-nodes-langchain.embeddingsdatabricks.md)：让智能体搜索 Databricks Vector Search 索引。
- [Databricks AI Agent](../root-nodes/n8n-nodes-langchain.databricksaiagent.md)：将智能体运行导出到 MLflow Tracing。
- Databricks 文档中的 [Unity AI Gateway 模型服务](https://docs.databricks.com/aws/en/ai-gateway/model-services)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 常见问题 <a id="common-issues"></a>

### No model services found（未找到模型服务） <a id="no-model-services-found"></a>

模型列表为空，节点报告 `No model services found`。工作区未启用 Unity AI Gateway，或凭据对应的身份无法访问任何模型服务。请检查工作区设置，再为至少一个模型服务授予 **USE CATALOG**、**USE SCHEMA** 和 **EXECUTE** 权限。

### No chat-capable model services found（未找到支持聊天的模型服务） <a id="no-chat-capable-model-services-found"></a>

凭据可以访问模型服务，但没有任何服务声明支持聊天补全。将 **Model**（模型）切换为 **ID**，直接输入服务名称。此节点不支持仅提供嵌入的服务。

### 达到速率限制 <a id="rate-limit-reached"></a>

执行以 `Rate limit reached` 或 429 状态失败。请求超过按 token 付费端点的工作区速率限制，Databricks 以 `REQUEST_LIMIT_EXCEEDED` 拒绝请求。请减少并发智能体运行，或使用预配吞吐量端点。错误文本中出现 OpenAI，是因为节点使用兼容 OpenAI 的客户端调用网关。

### 主机必须使用 HTTPS <a id="host-must-use-https"></a>

节点以 `Databricks host must use https` 失败，因为凭据的 **Host**（主机）以 `http://` 开头。每次请求都携带令牌，因此节点拒绝纯 HTTP。请将主机改为 `https://`。

### 凭据此前可用，但请求开始返回 403 <a id="requests-fail-with-403-after-the-credential-worked-before"></a>

对于用户登录凭据，刷新令牌或 OAuth 应用的绝对会话有效期已过期。在 n8n 中打开凭据，重新选择 **Connect my account**（连接我的账户）。定时工作流要避免此问题，可使用服务主体，或请管理员[延长令牌有效期](../../credentials/databricks.md#configure-token-lifetimes)。
