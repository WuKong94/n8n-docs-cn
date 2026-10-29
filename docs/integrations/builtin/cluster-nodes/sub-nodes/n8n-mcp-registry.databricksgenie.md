---
description: 通过 n8n MCP 服务器注册表中的 Databricks Genie One MCP 服务器，将 AI 智能体连接到 Databricks
  Genie One，并针对其轮询行为调整智能体。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Databricks Genie One MCP 服务器 <a id="databricks-genie-one-mcp-server"></a>

n8n 的 [MCP 服务器](../../../../build/integrate-ai/mcp-servers.md)注册表中的 **Databricks Genie One** 卡片，将 AI 智能体连接到 Databricks 工作区的 [Genie One MCP 服务器](https://docs.databricks.com/aws/en/agents/mcp-tools/genie-mcp)。Genie One 是面向业务用户的 Databricks 助手，会将每个问题路由到工作区中相关的 Genie Agent；没有匹配智能体时，则路由到其他受治理的数据资产，再生成并运行 SQL 来回答问题。要通过 **Agent ID** 调用特定 Genie Agent（旧称 Genie space），请改用 [Databricks 节点](../../app-nodes/n8n-nodes-base.databricks.md)。智能体会为使用了 Genie One 的回复附上 **Powered by Databricks Genie** 标签，每个答案都会链接回 Databricks 对话。哪些智能体添加标签、何时跳过，请参阅 [Genie 署名](#genie-attribution)。

本页介绍通过 n8n 智能体使用 Genie 的前置条件、配置步骤、智能体设置及已知问题。

{% hint style="info" %}
**凭据**

此卡片使用通过用户登录的 [Databricks OAuth2 凭据](../../credentials/databricks.md#using-oauth2-with-user-login)，不提供服务主体或个人访问令牌选项。
{% endhint %}

## 前置条件 <a id="prerequisites"></a>

- Databricks 账户管理员已[创建自定义 OAuth 应用连接](../../credentials/databricks.md#create-a-custom-oauth-app-connection)，其作用域覆盖卡片请求。卡片请求 `genie` 和 `offline_access` 作用域。仅包含这两个作用域的应用连接是最小权限配置；连接仅用于 Genie 时，n8n 建议采用此配置。n8n 测试中，**All APIs**（所有 API）也可覆盖请求，但仅应在同一应用连接还供需要此权限的 Databricks 节点或 Databricks Chat Model 节点使用时选择。如果连接因 `genie` 作用域错误失败，管理员需为应用连接[添加 `genie` 作用域](../../credentials/databricks.md#add-the-genie-scope-for-the-genie-mcp-server)。
- 对 Genie One 应使用的每个 Genie Agent 拥有 **CAN RUN** 权限，并对至少一个 SQL warehouse 拥有 **CAN USE** 权限。请参阅[所需 Databricks 权限](../../credentials/databricks.md#required-databricks-privileges)。
- 可可靠调用工具的聊天模型。n8n 建议通过 [Databricks Chat Model](n8n-nodes-langchain.lmchatdatabricks.md) 节点使用 Llama 3.3 70B 或 Qwen 3.5。请参阅[为智能体选择模型](n8n-nodes-langchain.lmchatdatabricks.md#choose-a-model-for-agents)。

## 将 Genie 连接到智能体 <a id="connect-genie-to-an-agent"></a>

Genie MCP 服务器仅使用用户登录这一种身份验证方式。智能体以连接凭据的 Databricks 用户身份向 Genie 提问，因此每位 n8n 用户都需要创建自己的凭据。

1. 在画布上打开 [AI Agent](../root-nodes/n8n-nodes-langchain.agent/README.md) 节点，选择 **Tool**（工具）连接器上的 **+**。
2. 搜索 `Databricks Genie One`，或打开 **MCP Servers**（MCP 服务器）部分浏览注册表。
3. 选择 **Databricks Genie One** 卡片。n8n 会向智能体添加名为 **Databricks Genie One MCP** 的节点，并打开设置。
4. 在 **Credential to connect with**（连接凭据）下选择 **Create new credential**（创建新凭据）。
5. 将工作区 URL 填入 **Host**（主机），例如 `https://adb-1234567890123456.7.azuredatabricks.net`。
6. 输入管理员创建的自定义 OAuth 应用连接的 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）。
7. 选择 **Connect my account**（连接我的账户），登录 Databricks。
8. 在 **Tools to Include**（要包含的工具）中保持 **All**（全部），以便智能体提问、轮询、获取结果及取消。请参阅[工具](#tools)。
9. 将智能体的 **Max Iterations**（最大迭代次数）设为 30 或以上。请参阅[为 Genie 配置智能体](#configure-the-agent-for-genie)。

向智能体提出数据问题，例如“trips 表中有多少条行程？”。回复会包含 Genie 的答案及 **Explore in Databricks**（在 Databricks 中探索）链接。

## 工具 <a id="tools"></a>

Genie One 提供四个工具。Databricks 将每个问题路由到某个 Genie Agent，没有匹配项时则使用其他工作区数据，因此没有智能体参数。下表列出 Databricks 的工具短名称。在 n8n 中，智能体看到的名称以节点名称为前缀；默认节点名称对应的示例为 `Databricks_Genie_One_MCP_genie_ask`。如果重命名了节点，或节点在卡片改名前已添加，会保留自身名称作为前缀，例如 `Databricks_Genie_MCP_genie_ask`。不要在提示词中引用工具短名称。

| 工具 | 作用 |
|------|--------------|
| `genie_ask` | 使用问题开始 Genie 对话，或通过 `conversation_id` 继续现有对话。无需等待答案即可返回状态。 |
| `genie_poll_response` | 检查 Genie 是否完成。Databricks 建议两次轮询之间等待 2 到 5 秒。 |
| `genie_get_query_result` | 答案摘要不足时，获取 Genie 所运行 SQL 的完整结果行。 |
| `genie_cancel_response` | 取消正在运行的 Genie 轮次。 |

## 为 Genie 配置智能体 <a id="configure-the-agent-for-genie"></a>

Genie 异步回答。智能体先调用 `genie_ask`，再调用 `genie_poll_response`，直到 Genie 报告完成。每次轮询消耗一次智能体迭代，即一次 `genie_poll_response` 调用加上决定是否继续轮询的模型轮次。Databricks 表示，Genie 轮次通常在 70 到 260 秒完成，建议两次轮询之间等待 2 到 5 秒，因此一个答案可能消耗 14 到 130 次迭代。

- **提高最大迭代次数。** AI Agent 默认的 10 次不足以处理实际问题。将 **Max Iterations**（最大迭代次数）设为 30 或以上。Databricks 耗时范围较慢一端的问题仍可能达到上限，出现截断时请进一步提高。
- **了解截断的表现。** AI Agent 节点版本 3 会以 `Max iterations (30) reached` 使执行失败。较早版本会执行成功，但回复 `Agent stopped due to max iterations.`，看似答案，实际并非答案。截断后，Genie 仍会在 Databricks 端继续运行该轮次。
- **引导模型。** 类似以下内容的系统消息，可使循环保持紧凑，并保留署名链接：

	```text
	回答数据问题时，先向 Genie 提问，再轮询直到状态为完成。
	仅在需要时获取完整结果行。
	在回复中原样包含工具结果中的任何 [Explore in Databricks](url) 链接。
	```

    不要在系统消息中写出工具名称。模型若逐字遵循提示词，就会调用工具短名称，而这些名称与 n8n 注册的名称不匹配，导致工具无法运行。

- **留意聊天模型速率限制。** n8n 测试中 Genie 本身没有限流，但按 token 付费的模型端点会限流。三个并发智能体运行就足以触发聊天模型的速率限制错误，使执行失败。请使用预配吞吐量端点，或保持较低并发。

## Genie 署名 <a id="genie-attribution"></a>

Databricks 要求由 Genie 提供支持的集成标明 Genie。在 n8n 中：

- 当运行调用过 Genie One 工具时，AI Agent 节点版本 3 及以上和 n8n Agents 会在回复后附加 **Powered by Databricks Genie** 标签。n8n 在模型回答后通过代码添加标签，系统消息无法移除。启用 **Require Specific Output Format**（要求指定输出格式）时，AI Agent 节点会跳过标签，因为结构化输出必须保持可解析。
- 每个已完成的 Genie 答案都包含 **Explore in Databricks** 链接，可打开工作区中的 Genie 对话，供用户查看 SQL 和结果。Genie 指示模型原样呈现链接，n8n 也原样传递工具结果。不要在系统消息或输出解析中移除此链接。

## 相关资源 <a id="related-resources"></a>

- [Databricks 凭据](../../credentials/databricks.md)，包括管理员设置 `genie` 作用域的方法。
- [Databricks Chat Model 节点](n8n-nodes-langchain.lmchatdatabricks.md)。
- [Databricks 节点](../../app-nodes/n8n-nodes-base.databricks.md)，用于直接调用 Genie Agent REST API，无需 AI 智能体。
- [MCP 服务器](../../../../build/integrate-ai/mcp-servers.md)，介绍注册表的工作方式。
- Databricks 文档中的 [Genie One MCP 服务器](https://docs.databricks.com/aws/en/agents/mcp-tools/genie-mcp)。

## 常见问题 <a id="common-issues"></a>

### 连接因 genie 作用域错误而失败 <a id="connect-fails-with-a-genie-scope-error"></a>

选择 **Connect my account**（连接我的账户）后报错：

```text
access_denied: Scopes 'genie' are not assigned to the client <client-id>
```

自定义 OAuth 应用连接没有 `genie` 作用域，且此 Databricks 账户中的 **All APIs**（所有 API）不能代替该作用域。Databricks 账户管理员需要在账户控制台的作用域选择器中，或通过 Databricks CLI，为应用连接[添加 `genie` 作用域](../../credentials/databricks.md#add-the-genie-scope-for-the-genie-mcp-server)。

### 达到最大迭代次数 <a id="max-iterations-reached"></a>

执行以 `Max iterations (10) reached` 失败，或智能体回复 `Agent stopped due to max iterations.`。智能体用尽迭代次数时，Genie 尚未完成。请将 AI Agent 节点的 **Max Iterations**（最大迭代次数）提高到 30 或以上。请参阅[为 Genie 配置智能体](#configure-the-agent-for-genie)。

### 智能体始终不调用 Genie <a id="the-agent-never-calls-genie"></a>

智能体用尽所有迭代次数，却没有一次工具调用。以下两种原因在执行日志中的表现相同：

- 系统消息中写出了工具名称，例如 `genie_ask`。模型调用短名称，而它们与 n8n 注册的带前缀名称不匹配，导致工具无法运行。请按[为 Genie 配置智能体](#configure-the-agent-for-genie)中的方式描述流程，不要写工具名称。
- 聊天模型未返回智能体可执行的工具调用。请通过 [Databricks Chat Model](n8n-nodes-langchain.lmchatdatabricks.md#choose-a-model-for-agents) 节点切换为可可靠调用工具的模型，例如 Llama 3.3 70B 或 Qwen 3.5。

### Genie 报告 SQL 或权限错误 <a id="genie-reports-a-sql-or-permission-error"></a>

Genie 返回自己的错误文本，例如 `[TABLE_OR_VIEW_NOT_FOUND] The table or view samples.nyctaxi.does_not_exist cannot be found`，智能体将其转达。请在 Databricks 中修复底层数据或授权问题。连接用户需要对回答问题的 Genie Agent 拥有 **CAN RUN** 权限，并具有所用表的 Unity Catalog 权限。
