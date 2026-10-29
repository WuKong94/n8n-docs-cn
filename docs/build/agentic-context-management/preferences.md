---
description: 保存偏好，让 n8n Assistant 和已连接的 MCP 客户端每次为你构建工作流和智能体时应用。
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
  anchors:
    visible: true
tags:
- preview
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 偏好设置 <a id="preferences"></a>

偏好设置是只需编写一次的简短指令，例如“始终连接错误工作流”。n8n Assistant 和已连接的 MCP 客户端每次为你构建工作流和智能体时，都会应用这些指令。

{% hint style="info" %}
**功能可用范围**

以下套餐提供偏好设置：

* **n8n Cloud：** Starter、Pro
* **自托管：** Community、已注册的 Community、Business

n8n Cloud Enterprise 和自托管 Enterprise 尚不提供偏好设置。

偏好设置从 n8n 2.40.0 起可用。通过 n8n Assistant 保存偏好，以及 n8n MCP 服务器的偏好工具，从 n8n 2.42.0 起可用。
{% endhint %}

{% hint style="info" %}
**预览状态**

偏好设置属于智能体上下文管理的一部分，处于预览阶段，未来版本中可能变化。请避免在生产环境中依赖此功能。
{% endhint %}

{% include "../../reusable-content/.gitbook/includes/agent-search-endpoint.md" %}

## 偏好设置的用途 <a id="what-preferences-are-for"></a>

希望 AI 工具在每项任务中都遵循某条规则时，使用偏好设置，而不是只针对当前任务。合适的偏好包括：

* **节点和凭据选择：**“发送提醒时，使用名为 `ops-bot` 的 **Slack** 凭据。”
* **命名：**“使用英文为节点命名，并以动词开头。”
* **工作组织方式：**“将新工作流放入 `Drafts` 文件夹。”
* **需要避免的模式：**“内置节点能完成任务时，不要使用 **Code** 节点。”
* **沟通风格：**“用不超过两句话说明更改。”

当前任务的指令应放在提示词中。例如“这次使用 POST 请求”应写在聊天中，而不是保存为偏好。

## n8n 在哪里应用偏好 <a id="where-n8n-applies-preferences"></a>

两类 AI 功能会读取偏好：

| 功能 | 读取偏好的时机 |
| ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| [n8n Assistant](../ways-of-building-workflows/n8n-assistant.md) | 每条消息都会读取，因此保存或编辑的偏好从下一条消息起生效，即使对话已经开始。 |
| 连接 [n8n MCP 服务器](../../connect/connect-to-n8n-mcp-server.md)的 MCP 客户端 | 客户端调用 `get_user_preferences` 工具时读取。n8n MCP 服务器会告知客户端，在 n8n 中创建或更改任何内容前先调用该工具。 |

如果偏好与你直接提出的要求冲突，AI 工具会遵循当前要求，并告知忽略了哪条偏好。

## 偏好的作用范围 <a id="preference-scopes"></a>

偏好的作用范围决定适用于哪些人。创建或编辑偏好时，在 **Scope（作用范围）** 字段选择。

| 作用范围标签 | 适用对象 | 谁可以创建、编辑或删除 |
| -------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------- |
| **Just you · All projects（仅你 · 所有项目）** | 仅你本人，在每个项目中 | 你本人 |
| **Just you · Personal project（仅你 · 个人项目）** | 仅你本人，在个人项目中工作时 | 你本人 |
| 团队项目名称（在列表中显示为 **Project（项目）**） | 该项目中的所有人 | 项目管理员和项目编辑者。项目查看者可以查看，但不能修改。 |
| **Global（全局）** | 实例中的所有人 | 实例所有者和管理员 |

n8n 会同时应用作用范围内的全部偏好。在对话中，n8n Assistant 收到 **Global（全局）** 偏好、你的个人偏好，以及打开对话所在项目的偏好。MCP 客户端收到全局偏好、个人偏好，以及所有你有权读取项目的偏好，并按项目分组。如果客户端传入 `projectId`，则只收到该项目的偏好，而不是所有项目的偏好。

将偏好移动到其他作用范围，需要同时具有从原范围删除、在新范围创建的权限。

## 偏好限制 <a id="preference-limits"></a>

| 限制 | 值 |
| --------------------------- | --------------------------------------------------------------------------------------------- |
| 单条偏好长度 | 2,000 个字符 |
| 每个作用范围的偏好数量 | 50 |
| 同一作用范围内的重复文本 | 不允许。如果文本与同一范围内已保存偏好相同，n8n 会拒绝。 |

作用范围内的数量已满时，需先删除一条偏好，才能添加新偏好。

## 在设置中创建偏好 <a id="create-a-preference-in-settings"></a>

1. 选择 **Settings（设置）** > **Context（上下文）**。
2. 选择 **Preferences（偏好设置）**。
3. 选择 **Create preference（创建偏好）**。
4. 在 **Preference（偏好）** 中编写指令，像向同事交代工作一样，例如“始终连接错误工作流，以便发生任何失败时在 Slack 上通知我”。
5. 在 **Scope（作用范围）** 中选择适用对象。各选项说明见[偏好的作用范围](preferences.md#preference-scopes)。
6. 选择 **Save（保存）**。

n8n Assistant 会从下一条消息起应用新偏好。MCP 客户端会在下次调用 `get_user_preferences` 时应用。

## 在设置中编辑或删除偏好 <a id="edit-or-delete-preferences-in-settings"></a>

**Settings（设置）** > **Context（上下文）** > **Preferences（偏好设置）** 列出所有你有权查看的偏好，并显示 **Scope（作用范围）**、**Created by（创建者）** 和 **Last updated（最后更新时间）**。**Created by** 显示创建者姓名；如果由 AI 工具保存，还会在括号中标明来源，例如“Jane Doe (MCP)”或“Jane Doe (n8n assistant)”。

* **编辑偏好：** 打开偏好的 **Options（选项）** 菜单，选择 **Edit（编辑）**，修改文本或作用范围，再选择 **Save（保存）**。
* **删除偏好：** 打开偏好的 **Options（选项）** 菜单，选择 **Delete（删除）**。
* **删除多条偏好：** 在列表中选中，再选择 **Delete selected（删除所选）**。

删除无法撤销。n8n Assistant 和 MCP 客户端会立即停止使用已删除偏好。

没有修改权限时，n8n 会以只读方式显示偏好。

## 通过 n8n Assistant 保存偏好 <a id="save-preferences-from-n8n-assistant"></a>

向 n8n Assistant 提出长期规则时，例如“从现在起，始终添加错误工作流”，它会将规则保存为 **Just you · All projects（仅你 · 所有项目）** 范围的偏好。当前任务的一次性指令不会保存。

保存偏好后，n8n Assistant 会在聊天中显示包含文本的卡片。通过卡片可以：

* 选择 **Edit（编辑）**，修改文本或作用范围。
* 在 **Edit preference（编辑偏好）** 对话框中，选择 **Remove preference（移除偏好）** 删除。

要查看助手在最近一次回复中应用了哪些偏好，打开聊天输入框中的 **+** 菜单，再选择 **Preferences（偏好设置）**。

实例所有者和管理员控制助手能否保存偏好。在 **Settings（设置）** > **Assistant** > **Permissions（权限）** 中，将 **Save preferences from chat（从聊天保存偏好）** 设为 **Allow（允许，默认）** 或 **Block（禁止）**。设为 **Block** 后，助手仍会应用已保存的偏好，但无法保存新偏好。

## 通过 MCP 客户端保存偏好 <a id="save-preferences-from-an-mcp-client"></a>

连接 n8n MCP 服务器的 MCP 客户端，可以通过四个工具读取和保存偏好：

| 工具 | 作用 |
| ------------------------ | ----------------------------------------------------------------- |
| `get_user_preferences` | 读取适用于你的偏好 |
| `save_user_preference` | 保存 **Just you · All projects（仅你 · 所有项目）** 范围的新偏好 |
| `update_user_preference` | 修改偏好文本、作用范围，或两者同时修改 |
| `undo_user_preference` | 移除 MCP 客户端为你保存的偏好 |

`undo_user_preference` 无法移除你在设置中编写的偏好，也无法移除为项目或整个实例保存的偏好。请在 **Settings（设置）** > **Context（上下文）** > **Preferences（偏好设置）** 中移除这些内容。

如果 MCP 客户端支持 MCP elicitation（信息征询），n8n 会在 `save_user_preference` 保存偏好后显示审核表单。在表单中可以：

* 接受显示的文本，或先编辑。
* 如果是实例所有者或管理员，可以将范围改为 **Everyone on this n8n instance（此 n8n 实例中的所有人）**。
* 拒绝表单，以移除该偏好。

关闭表单而不作答，会保留已保存的偏好。

### MCP 客户端的偏好权限 <a id="mcp-client-permissions-for-preferences"></a>

使用 OAuth 连接 MCP 客户端时，n8n 会请求你批准两项偏好权限：

| 同意屏幕上的权限 | OAuth 权限范围 | 工具 |
| ---------------------------------------- | -------------------- | ------------------------------------------------------------------------ |
| **Read AI preferences（读取 AI 偏好）** | `aiPreference:read` | `get_user_preferences` |
| **Save, update and undo AI preferences（保存、更新和撤销 AI 偏好）** | `aiPreference:write` | `save_user_preference`、`update_user_preference`、`undo_user_preference` |

只有实例已启用偏好设置时，n8n 才提供这些权限。如果客户端在功能启用前已连接，请重新连接以授予权限。请参阅[检查和撤销客户端访问](../../connect/connect-to-n8n-mcp-server.md#revoking-client-access)。

每个工具的参数和输出，请参阅 MCP 服务器工具参考中的[用户偏好](../../connect/connect-to-n8n-mcp-server/mcp-server-tools-reference.md#user-preferences)。

## 编写有效偏好 <a id="write-effective-preferences"></a>

AI 工具会将偏好应用于作用范围内的每项任务，因此应编写适用于所有这些任务的规则。

* **每条偏好只写一条规则。** 相比包含多条规则的段落，单条规则更便于之后编辑或删除。
* **说明应该做什么，必要时解释原因。**“客户邮件使用名为 `support-inbox` 的 **Gmail** 凭据”比“使用正确的凭据”更具体。
* **准确写出节点、凭据、文件夹和项目名称。** AI 工具会精确匹配名称。
* **避免仅适用于单个工作流的规则。** 此类指令应放入提示词。

| 不建议 | 建议 |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| “将 Webhook 路径设为 `/orders`。” | 放在提示词中，只适用于单个工作流。 |
| “注意错误处理。” | “为每个新工作流连接 `Error alerts` 错误工作流。” |
| “使用合适名称、把内容放进文件夹，并避免 Code 节点。” | 拆分为三条偏好：一条命名规则、一条文件夹规则和一条 **Code** 节点规则。 |

## 在自托管实例上启用偏好 <a id="turn-on-preferences-on-a-self-hosted-instance"></a>

偏好设置默认开启。如果实例关闭了遥测（`N8N_DIAGNOSTICS_ENABLED=false`），或无法连接 n8n 功能标志服务，偏好功能会保持关闭。

要开启偏好设置，设置 `N8N_FEATURE_FLAG_OVERRIDES`。例如，将以下值添加到 `.env` 文件，保留 JSON 对象中的其他条目。

```bash
N8N_FEATURE_FLAG_OVERRIDES='{"111_context_preferences":"variant"}'
```

重启 n8n，应用更改。

值必须是字符串 `"variant"`。`true` 等布尔值不会开启偏好功能。

关闭偏好功能后，n8n 会隐藏 **Settings（设置）** > **Context（上下文）** 中的 **Preferences（偏好设置）**；助手不会读取或保存偏好，MCP 服务器也不会提供偏好工具。此前保存的偏好会保留，重新开启后会再次应用。

## 偏好故障排查 <a id="troubleshoot-preferences"></a>

### 设置中没有显示偏好 <a id="preferences-doesnt-appear-in-settings"></a>

确认实例运行 n8n 2.40.0 或更高版本，且不是 Enterprise 套餐。关闭遥测的自托管实例，请参阅[在自托管实例上启用偏好](preferences.md#turn-on-preferences-on-a-self-hosted-instance)。

### MCP 客户端未列出偏好工具 <a id="an-mcp-client-doesnt-list-the-preferences-tools"></a>

确认实例已开启偏好功能，再检查客户端是否具有 **Read AI preferences（读取 AI 偏好）** 和 **Save, update and undo AI preferences（保存、更新和撤销 AI 偏好）** 权限。如果在功能开启前已连接客户端，请撤销访问并重新连接。

### n8n Assistant 提示禁止保存偏好 <a id="n8n-assistant-says-saving-preferences-is-blocked"></a>

实例所有者或管理员在 **Settings（设置）** > **Assistant** > **Permissions（权限）** 中，将 **Save preferences from chat（从聊天保存偏好）** 设为了 **Block（禁止）**，或实例连接到了受保护的源代码管理分支。如果有权限，可以改在 **Settings（设置）** > **Context（上下文）** > **Preferences（偏好设置）** 中创建。

### AI 工具忽略了偏好 <a id="an-ai-tool-ignores-a-preference"></a>

检查偏好的作用范围是否涵盖当前项目。在 n8n Assistant 中，团队项目偏好仅适用于在该项目中打开的对话。如果偏好与提示词冲突，AI 工具会遵循提示词。

## 相关资源 <a id="related-resources"></a>

* [智能体上下文管理](./)
* [使用 n8n Assistant](../ways-of-building-workflows/n8n-assistant.md)
* [使用 n8n MCP 服务器](../ways-of-building-workflows/connect-to-n8n-mcp-server.md)
* [连接 n8n MCP 服务器](../../connect/connect-to-n8n-mcp-server.md)
* [MCP 服务器工具参考](../../connect/connect-to-n8n-mcp-server/mcp-server-tools-reference.md)
