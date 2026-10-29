---
title: 使用 n8n Assistant
status: preview
description: 通过聊天使用 n8n Assistant 创建、编辑、测试和排查 n8n 工作流。
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
- tag: preview
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 使用 n8n Assistant <a id="use-n8n-assistant"></a>

n8n Assistant 是 n8n 中基于聊天的智能体，可以根据自然语言帮助你创建、编辑、测试和排查工作流。它也可以构建智能体，并协助处理重命名或发布工作流等实例任务。

描述想要自动化的任务后，n8n Assistant 可以规划工作流，在所选项目中构建、测试，并帮助修复错误。

生成的结果是普通 n8n 工作流。可以像其他工作流一样打开、检查、编辑、测试和发布。

{% hint style="info" %}
**功能可用范围**

以下套餐提供 n8n Assistant：

* **n8n Cloud：** Starter、Pro
* **自托管：** Community、已注册的 Community、Business

此功能尚未适用于 n8n Cloud Enterprise 或自托管 Enterprise。Enterprise 客户可以联系客户成功经理，了解预览访问资格。
{% endhint %}

{% hint style="info" %}
**预览状态**

n8n Assistant 处于预览阶段，可能出错，开发期间行为也可能变化。用于生产环境前，请务必检查生成的工作流。
{% endhint %}

## n8n Assistant 可以提供哪些帮助 <a id="what-n8n-assistant-can-help-with"></a>

通过聊天与 n8n Assistant 交互。它可以使用 n8n 内的工具，帮助创建和调试工作流。

可以要求 n8n Assistant：

* **创建工作流：** 描述所需自动化，n8n Assistant 即可生成工作流。
* **构建智能体：** 描述所需智能体，n8n Assistant 可以建议添加哪些指令、工具和技能。自托管环境中，智能体也可以通过 `agents` 模块运行。请参阅[构建和管理智能体](../build-and-manage-agents/)及[启用智能体](../../deploy/host-n8n/configure-n8n/set-up-n8n-assistant.md#enable-agents)。
* **连接 MCP 服务器：** 将 [MCP 服务器](../integrate-ai/mcp-servers.md)注册表中的服务器直接连接到助手，既可执行任务，也可在构建工作流时收集上下文。
* **在浏览器中操作：** 连接 [Browser Use](n8n-assistant/browser-use.md)，让 n8n Assistant 浏览网站、填写表单并代为设置凭据。
* **编辑工作流：** 要求它修改工作流、添加节点、更新逻辑或调整配置。
* **测试和排查工作流：** 要求它运行检查、查看相关错误并建议修复方法。
* **协助配置凭据：** 提示你选择已有凭据或创建新凭据，无需将机密信息粘贴到聊天中。
* **使用 n8n 资源：** 按需创建或更新[数据表](../work-with-data/data-tables.md)等配套资源。
* **研究已获准访问的网站：** 启用网页访问后，n8n Assistant 会在访问域名前请求许可。
* **接续近期工作：** 询问之前构建的工作流或失败的执行，n8n Assistant 可以找到它，无需你提供名称。

## n8n Assistant 如何了解实例 <a id="what-n8n-assistant-knows-about-your-instance"></a>

{% hint style="info" %}
**预览状态**

实例上下文处于预览阶段，未来版本中可能变化。n8n 尚未为所有实例启用此功能。请避免让生产工作依赖实例上下文。
{% endhint %}

对话开始时，n8n Assistant 会收到实例上下文，即打开对话所在项目的简短摘要。这有助于它响应“查找最近一次失败执行”等提示，无需你提供工作流名称。

实例上下文来自三类信息：

| 实例上下文报告的内容 | 来源 |
| ------------------------------------------------------------------ | ------------------------- |
| 项目中存在哪些工作流，以及它们的发布状态 | 你的工作流 |
| 最近的更改及修改者 | 实例活动日志 |
| 哪些工作流运行过、失败了多少次，以及最近一次失败 | 执行历史 |

对话第一条消息会附带初始摘要，其中包含的工作流、活动条目和执行记录数量有限。n8n Assistant 可以按需获取更多详情。此后，每条消息只携带自上次以来的变化。处理不相关任务时，开启新对话，n8n Assistant 就会重新读取项目。

在 n8n Cloud 上，由 n8n 控制实例上下文的访问。在自托管实例上，实例管理员可以覆盖功能标志，启用实例上下文。请参阅[启用实例上下文](../../deploy/host-n8n/configure-n8n/set-up-n8n-assistant.md#enable-instance-context)。

### n8n Assistant 可以通过实例上下文查询什么 <a id="what-n8n-assistant-can-look-up-from-instance-context"></a>

实例上下文保存的是指向记录的引用，而非记录内容。通过它，n8n Assistant 可以：

* **进一步读取更早的近期更改。** 实例上下文涵盖近期的一段时间。n8n Assistant 可以列出更早条目、筛选工作流或凭据更改，或打开某个条目查看单个工作流的近期更改历史。
* **打开当前记录。** 每行都带有 ID，因此 n8n Assistant 可以获取其指向的工作流、执行或凭据。

活动条目遵循[活动日志保留设置](../../deploy/host-n8n/configure-n8n/set-up-n8n-assistant.md#enable-instance-context)，执行记录遵循[执行数据保留设置](../../deploy/host-n8n/configure-n8n/scaling/manage-execution-data.md)。如果某个活动条目已被清理，n8n Assistant 会在没有该条目的情况下继续。

### n8n Assistant 如何了解你使用的节点 <a id="how-n8n-assistant-learns-which-nodes-you-use"></a>

节点类型计数与实例上下文是独立设置，必须由实例管理员启用。请参阅[启用节点类型计数](../../deploy/host-n8n/configure-n8n/set-up-n8n-assistant.md#enable-node-type-counting)。

启用后，n8n Assistant 可以查询项目中使用各类节点的工作流数量，无需读取每个工作流就能了解你的惯例。此功能只报告节点类型数量，不报告参数值，因此可以得知 10 个工作流全部使用 **Slack** 节点，却无法得知具体配置。要实际遵循某种惯例，而不仅是说出惯例，n8n Assistant 会完整读取一个工作流。

### 实例上下文不包含什么 <a id="what-instance-context-doesnt-include"></a>

活动日志记录某项更改发生过，而不记录更改的具体内容。要回答工作流结构或配置的问题，n8n Assistant 会读取工作流本身。

实例上下文不包含：

* **参数值。** 更改条目会列出添加或移除的节点类型，以及修改了哪些设置，但不记录设置的值。
* **单个节点。** 保存条目记录的是添加或移除的节点类型，而非单个节点。再添加一个 **Slack** 节点会改变节点总数，但不会增加新类型。
* **大规模更改中的全部节点类型。** 一次保存超过节点类型数量限制时，条目只列出部分类型，并报告总数。
* **未打开项目中的工作。** 请参阅[实例上下文限于单个项目](n8n-assistant.md#instance-context-stays-inside-one-project)。

## n8n Assistant 如何应用偏好设置 <a id="how-n8n-assistant-applies-your-preferences"></a>

{% hint style="info" %}
**功能可用范围**

偏好设置从 n8n 2.40.0 起可用；通过 n8n Assistant 保存偏好从 n8n 2.42.0 起可用。
{% endhint %}

{% hint style="info" %}
**预览状态**

偏好设置属于智能体上下文管理的一部分，处于预览阶段，未来版本中可能变化。请避免在生产工作流中依赖它。
{% endhint %}

[偏好设置](../agentic-context-management/preferences.md)是简短指令，例如“使用英文为节点命名，并以动词开头”，n8n Assistant 每次为你构建时都会应用。它会在每条消息中读取这些偏好，因此即使对话已开始，新保存或编辑的偏好也会从下一条消息起生效。

在对话中，n8n Assistant 会应用 **Global（全局）** 偏好、你的个人偏好，以及打开对话所在项目的偏好。如果偏好与提示冲突，n8n Assistant 遵循提示。

要查看 n8n Assistant 在最近一次回复中应用了哪些偏好，打开聊天输入框中的 **+** 菜单，再选择 **Preferences（偏好设置）**。

在聊天中提出长期规则时，例如“从现在起，始终添加错误工作流”，n8n Assistant 会将其保存为适用于你本人所有项目的个人偏好，并显示包含保存文本的卡片。选择卡片上的 **Edit（编辑）**，可以修改文本、作用范围或删除偏好。实例所有者和管理员可以在 **Settings（设置）** > **Assistant** > **Permissions（权限）** 中，通过 **Save preferences from chat（从聊天保存偏好）** 权限阻止助手保存偏好。

要管理全部偏好，进入 **Settings（设置）** > **Context（上下文）** > **Preferences（偏好设置）**。

## 开始之前 <a id="before-you-start"></a>

使用 n8n Assistant，需要有权访问已启用此功能的 n8n 实例。

请确认：

* 可以访问希望 n8n Assistant 在其中工作的项目。
* 有权使用任务所需的工作流、凭据和资源。
* 清楚工作流应完成什么任务。

n8n Assistant 使用你的 n8n 用户权限，只能访问你有权使用的工作流、凭据和资源。

## 编写有效提示词 <a id="write-effective-prompts"></a>

具体的提示词有助于 n8n Assistant 以更少迭代取得更好结果。

编写提示词时，请说明：

* 什么条件触发工作流，
* 应使用哪些应用或服务，
* 应读取、发送或更新哪些数据，
* 工作流成功时应做什么，
* 工作流失败时应做什么，
* 发布工作流前是否需要向你询问。

## 提示词示例 <a id="example-prompts"></a>

### 创建工作流 <a id="create-a-workflow"></a>

```
创建一个工作流，每天早上检查 Gmail 中的发票，
将 PDF 附件保存到 Google Drive，并向数据表添加一行。
发布工作流前先询问我。
```

### 调试失败的执行 <a id="debug-a-failed-execution"></a>

```
调试此工作流最近一次失败的执行。
说明失败原因，在进行任何更改前先提出修复建议。
```

### 更新已有工作流 <a id="update-an-existing-workflow"></a>

```
更新此工作流，将失败的订单发送到 Slack，
并在 10 分钟后重试 API 请求。
```

## 检查 AI 生成的更改 <a id="review-ai-generated-changes"></a>

n8n Assistant 可以在实例中执行操作，但控制权仍在你手中。

将 AI 生成的工作流用于生产环境前：

* 检查工作流逻辑。
* 检查节点配置和凭据。
* 使用预期输入数据测试工作流。
* 检查执行结果和错误处理。
* 确认工作流不会执行非预期操作。

n8n Assistant 会在发布、删除或其他重要变更等影响较大的操作前请求确认。

## 凭据处理 <a id="credential-handling"></a>

凭据的机密信息不会发送给 AI，AI 也不会看到它们。

从 n8n 2.41.0 起，n8n Assistant 可以读取凭据说明。从 n8n 2.42.0 起，只有实例启用凭据说明功能时，助手才会读取。

n8n Assistant 使用可用的凭据说明，帮助在同类型凭据之间作出选择。例如，说明可以标明生产账号或测试账号。如果仍无法判断，助手会询问你使用哪一个。

AI 可能接收凭据说明。不要在说明中包含 API 密钥、密码或令牌。

工作流需要凭据时，n8n Assistant 会在聊天中显示凭据卡片。通过卡片可以：

* 选择项目内你有权访问的已有凭据。
* 创建新凭据。

也可以通过 [Browser Use](n8n-assistant/browser-use.md#set-up-credentials-with-browser-use)，让 n8n Assistant 在浏览器中代为创建凭据。机密值直接写入凭据，AI 不会看到。

自行创建新凭据时，在标准 n8n 凭据界面中输入机密值，而不是在聊天中输入。不要将 API 密钥、密码或令牌粘贴到对话中。

## 网页访问 <a id="web-access"></a>

启用网页访问后，n8n Assistant 会在访问外部域名前请求许可。

批准访问前，请检查所请求的域名。

## 预览阶段的限制 <a id="preview-limitations"></a>

n8n Assistant 是预览功能，可用范围、支持的操作和行为均可能变化。

预览期间：

* 部分操作可能尚不支持。
* 一些能力可能逐步推出。
* n8n Assistant 请求澄清的频率可能高于预期。
* 生成的工作流可能需要人工检查和修正。
* 界面、额度消耗方式和支持的资源可能变化。

## 数据与隐私 <a id="data-and-privacy"></a>

n8n Assistant 会处理构建和排查工作流所需的信息。

视任务而定，可能包括：

* 提示词和聊天消息，
* 工作流结构和节点配置，
* 排查问题所选用的执行及错误详情，
* 凭据名称、类型、说明或连接状态，
* 启用网页访问后，获准访问的网页或域名，
* 打开助手所在项目中的工作流名称，
* 该项目中近期工作流和凭据更改的记录，
* 这些工作流中哪些运行过，以及哪些执行失败。

n8n Assistant 不要求你将机密信息粘贴到聊天中。请通过标准 n8n 凭据界面输入 API 密钥、密码和令牌。

{% hint style="warning" %}
除非任务确实需要，否则不要将敏感数据粘贴到聊天中。AI 输出可能有误，请在用于生产环境前检查工作流和配置。
{% endhint %}

### 实例上下文限于单个项目 <a id="instance-context-stays-inside-one-project"></a>

对话使用打开它时所在的项目。自动实例上下文和活动日志搜索只读取该项目。工作流搜索和节点类型计数则可以包含其他你有权读取的项目。

n8n Assistant 使用你的权限读取实例上下文，n8n 会在每条消息上检查权限，而不是只在对话开始时检查。如果失去项目访问权限，助手会停止读取该项目。

查询对话所在项目以外的活动条目 ID，与查询不存在的条目会得到相同响应。这类请求不会泄露其他项目中是否存在某个条目。

## 额度消耗 <a id="credit-usage"></a>

在 n8n Cloud 上，n8n Assistant 根据底层 AI 模型处理的词元数量消耗 [Assistant 额度](../../deploy/use-n8n-cloud/assistant-credits/README.md)。套餐包含每月额度，于每月第一天重置。用完后，实例所有者可以购买额外额度，在下次重置前继续使用。实例上的所有人共享同一余额。

Assistant 额度与 [Gateway 额度](../understand-workflows/use-gateway-credits.md)相互独立。Assistant 额度支付你与助手的对话，而不支付工作流或智能体运行时调用 AI 模型的费用；Gateway 额度支付这些模型调用，而不支付 n8n Assistant。为其中一种充值不会增加另一种的余额。

更长的对话、更大的工作流、调试过程和反复迭代都会消耗更多额度。

减少不必要消耗的方法如下：

* 明确工作流目标和约束。
* 为不相关任务开启新对话。
* 要求构建前先检查助手的计划。
* 避免在没有新增指导的情况下，要求重新生成相同工作流。

要查看余额，打开 n8n Assistant 面板中的额度菜单。套餐的每月额度请参阅 [n8n 套餐与定价](https://n8n.io/pricing/)。

自托管 n8n 不使用 Assistant 额度。在自托管实例上，n8n Assistant 使用你自己的 AI 服务商账号运行。请参阅[设置 n8n Assistant](../../deploy/host-n8n/configure-n8n/set-up-n8n-assistant.md)。

## 相关资源 <a id="related-resources"></a>

* [构建工作流的方式](./)
* [使用 Browser Use](n8n-assistant/browser-use.md)
* [使用 n8n MCP 服务器](connect-to-n8n-mcp-server.md)
* [使用模板](use-templates.md)
* [使用 Ask n8n AI](use-the-ai-assistant.md)
* [使用 Chat Hub](chat-hub.md)
* [偏好设置](../agentic-context-management/preferences.md)
