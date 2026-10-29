---
title: Microsoft Teams 节点文档
description: 了解如何在 n8n 中使用 Microsoft Teams 节点，并按照技术文档将 Microsoft Teams 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Microsoft Teams 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.microsoftteams.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftteams
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftteams
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Teams 节点 <a href="#microsoft-teams-node" id="microsoft-teams-node"></a>

使用 Microsoft Teams 节点自动处理 Microsoft Teams 中的工作，并将其与其他应用集成。n8n 内置支持多种 Microsoft Teams 功能，包括频道、聊天、频道消息和聊天消息、聊天成员、联机会议及任务。

本页列出了 Microsoft Teams 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

从节点第 2 版起，**Authentication**（身份验证）下拉菜单提供三个选项：

- **Teams OAuth2**：Microsoft Teams 专用的 OAuth2 凭据，默认选项。默认作用域覆盖本页全部资源，包括从 n8n 2.39.0 起用于聊天成员和聊天消息的 `Chat.ReadWrite`、用于联机会议的 `OnlineMeetings.ReadWrite`，以及从 n8n 2.41.0 起用于提及团队标签的 `TeamworkTag.Read`。
- **Microsoft OAuth2 (Graph)**：可在其他 Microsoft 节点中复用的通用 Microsoft Graph 凭据。选择此选项时，请为凭据授予本节点所需作用域，完整列表请参阅 [Microsoft Teams 默认作用域](../credentials/microsoft.md#default-scopes-for-microsoft-teams)。
- **Service Principal (App-Only)**（服务主体，仅应用）：通过 Microsoft Entra 应用注册实现仅应用访问，无需用户登录。部分资源要求有已登录用户，因此不适用于此凭据。请参阅本页的[服务主体凭据支持范围](#service-principal-credential-support)；设置方式及所需应用程序权限，请参阅 [Microsoft Entra 服务主体凭据](../credentials/microsoftentraserviceprincipal.md)。

如果在 n8n 2.39.0 之前连接了 Teams OAuth2 凭据，请重新连接以获得 `OnlineMeetings.ReadWrite`。如果凭据使用 **Custom Scopes**（自定义作用域），请改为将该作用域添加到 **Enabled Scopes**（已启用的作用域）。

在 n8n Cloud 中，托管的 **Teams OAuth2** 凭据需要 Microsoft Entra 管理员先为组织批准权限，非管理员用户才能连接或重新连接。n8n 新增需要管理员同意的作用域时，也需再次批准。操作步骤以及仅重新连接仍会失败的原因，请参阅[云端 Microsoft Teams：管理员批准](../credentials/microsoft.md#microsoft-teams-on-cloud-admin-approval)。

有关身份验证设置，请参阅 [Microsoft 凭据](../credentials/microsoft.md)。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果使用政府云租户（美国政府、美国国防部或中国），请确保在 Microsoft 凭据配置中选择正确的 **Microsoft Graph API Base URL（Microsoft Graph API 基础 URL）**。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/hitl-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

{% hint style="info" %}
**功能可用范围**

- Chat Member（聊天成员）和 Online Meeting（联机会议）资源，以及 Channel Message（频道消息）的 **Get**（获取）、**Get Many Replies**（获取多条回复）和 **Reply**（回复）操作，从 n8n 2.39.0 起可用。
- Chat Member（聊天成员）的 **Add**（添加）和 **Remove**（移除）操作，Channel Message（频道消息）和 Chat Message（聊天消息）的 **Delete**（删除）及 **Undo Delete**（撤销删除）操作，Online Meeting（联机会议）的 **Create or Get**（创建或获取）、**Delete**（删除）及 **Update**（更新）操作，以及 Online Meeting 对 **Service Principal (App-Only)**（服务主体，仅应用）凭据的支持，从 n8n 2.40.0 起可用。
- Chat（聊天）资源从 n8n 2.41.0 起可用。
- Activity Notification（活动通知）资源从 n8n 2.42.0 起可用。
{% endhint %}

* Activity Notification（活动通知）
    * Send（发送）
* Channel（频道）
    * Create（创建）
    * Delete（删除）
    * Get（获取）
    * Get Many（获取多条）
    * Update（更新）
* Channel Message（频道消息）
    * Create（创建）
    * Delete（删除）
    * Get（获取）
    * Get Many（获取多条）
    * Get Many Replies（获取多条回复）
    * Reply（回复）
    * Undo Delete（撤销删除）
* Chat（聊天）
    * Create（创建）
    * Get（获取）
    * Get Many（获取多条）
* Chat Member（聊天成员）
    * Add（添加）
    * Get Many（获取多条）
    * Remove（移除）
* Chat Message（聊天消息）
    * Create（创建）
    * Delete（删除）
    * Get（获取）
    * Get Many（获取多条）
    * Send and Wait for Response（发送并等待回复）
    * Undo Delete（撤销删除）
* Online Meeting（联机会议）
    * Create（创建）
    * Create or Get（创建或获取）
    * Delete（删除）
    * Get（获取）
    * Update（更新）
* Task（任务）
    * Create（创建）
    * Delete（删除）
    * Get（获取）
    * Get Many（获取多条）
    * Update（更新）

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/send-and-wait-operation.md" %}

## 提及 <a id="mentions"></a>

{% hint style="info" %}
**功能可用范围**

Microsoft Teams 节点从 n8n 2.41.0 起支持提及功能。
{% endhint %}

Channel Message（频道消息）的 **Create**（创建）和 **Reply**（回复）操作，以及 Chat Message（聊天消息）的 **Create** 操作，都提供 **Mentions**（提及）字段。每一行可 @提及一名用户或一个团队标签，n8n 会为你将提及添加到消息中。频道消息需先将 **Mention Type**（提及类型）设为 **User**（用户）或 **Team Tag**（团队标签）。聊天消息仅能提及用户，因为团队标签属于团队。Microsoft Teams 如何保存提及，请参阅 Microsoft 的 [`chatMessageMention` 资源类型](https://learn.microsoft.com/en-us/graph/api/resources/chatmessagemention)。

不要再将该名称填入 **Message**（消息）中，否则名称会显示两次。

操作的 **Options**（选项）集合中的 **Mention Placement**（提及位置）控制提及出现的位置。默认值 **Start of Message**（消息开头）会生成 `@Jane please review this`；**End of Message**（消息末尾）会生成 `please review this @Jane`。

{% hint style="warning" %}
**提及会让消息以 HTML 显示**

包含提及时，即使 **Content Type**（内容类型）为 **Text**（文本），Microsoft Teams 仍会将消息渲染为 HTML。在 **Message**（消息）中输入的换行将不再显示为换行，请改用 `<br>`。
{% endhint %}

### 提及用户 <a id="mention-a-user"></a>

在 Channel Message（频道消息）**Create**（创建）或 **Reply**（回复）的 **Mentions**（提及）行中，将 **Mention Type**（提及类型）设为 **User**（用户）。Chat Message（聊天消息）**Create** 没有 **Mention Type**，因为其中每行本身都是用户。然后填写 **User** 字段：

* **From List**（从列表）：搜索 Microsoft Entra 目录，选择用户。每个条目都显示名称及用户主体名称（UPN），例如 `Jane Smith (jane@contoso.com)`，因为租户内的显示名称并不唯一。此处也支持来宾用户。
* **By ID**（按 ID）：输入用户对象 ID，例如 `7e2f1174-e8ee-4859-b8b1-a8d1cc63d276`，或 UPN/邮箱地址，例如 `jacob@contoso.com`。来宾用户请使用对象 ID：来宾的 UPN 含有 `#EXT#`，该字段不接受此形式。

n8n 会在发送消息前到 Microsoft Entra 中查找用户，因此提及显示的是目录中的显示名称，而非你输入的文本。

### 提及团队标签 <a id="mention-a-team-tag"></a>

团队标签属于某个团队，因此只能在频道消息中提及标签。先将操作的 **Team**（团队）设为标签所属团队，再添加一行 **Mentions**（提及），将 **Mention Type**（提及类型）设为 **Team Tag**（团队标签），填写 **Team Tag** 字段：

* **From List**（从列表）：选择团队标签。每个条目会显示该标签关联的成员数，例如 `Engineering (4 members)`。
* **By ID**（按 ID）：输入 `GET /v1.0/teams/<team-id>/tags` 返回的标签 ID。标签必须属于所选团队，否则节点查找标签时会失败。

提及标签会通知所有关联成员。Microsoft Teams 节点只能提及团队已有标签，不能创建新标签。

### 提及权限 <a id="mention-permissions"></a>

提及用户需要 `User.Read.All` 权限，提及团队标签需要 `TeamworkTag.Read`。**Teams OAuth2** 凭据默认请求两者。如果凭据使用 **Custom Scopes**（自定义作用域），或通过 **Microsoft OAuth2 (Graph)** 身份验证，请手动添加这些权限，并由 Microsoft Entra 管理员授予同意。

如果在 n8n 2.41.0 之前连接了 Teams OAuth2 凭据，请重新连接以获得 `TeamworkTag.Read`。没有该作用域，提及团队标签会因权限错误而失败。

**Service Principal (App-Only)**（服务主体，仅应用）凭据不支持提及，因为支持提及的三个操作均无法使用该凭据运行。请参阅[服务主体凭据支持范围](#service-principal-credential-support)。

## 删除和恢复消息 <a id="delete-and-restore-messages"></a>

Channel Message（频道消息）和 Chat Message（聊天消息）的 **Delete**（删除）操作会软删除消息：Microsoft Teams 将其从频道或聊天中隐藏，但仍保留消息，同一资源的 **Undo Delete**（撤销删除）操作可恢复它。两种操作都以已登录用户的身份执行，可以删除和恢复自己的消息。能否删除他人的消息，取决于团队角色及组织的 Microsoft Teams 消息策略；不允许时，操作会因权限错误而失败。

两种操作都需要 **Message ID**（消息 ID）。在 Microsoft Teams 中复制消息链接即可找到：链接路径末尾、`?` 之前的数字就是消息 ID。聊天消息还需 **Chat**（聊天），频道消息还需 **Team**（团队）和 **Channel**（频道）。要删除或恢复频道中的回复，请添加 **Parent Message ID**（父消息 ID）选项，填入回复所属消息的 ID，即回复链接中的 `parentMessageId` 参数。

删除和恢复频道消息需要 `ChannelMessage.ReadWrite` 作用域，**Teams OAuth2** 凭据从 n8n 2.40.0 起默认请求它。此前连接的凭据没有此作用域，**Delete**（删除）和 **Undo Delete**（撤销删除）会因 403 错误而失败，直到重新连接。如果使用 **Custom Scopes**（自定义作用域），请在重新连接前，将作用域添加到 **Enabled Scopes**（已启用的作用域）。

`ChannelMessage.ReadWrite` 需要管理员同意。如果你不是 Microsoft Entra 管理员，请先让管理员为应用新增权限授予同意，例如由管理员亲自重新连接凭据并选择 **Consent on behalf of your organization**（代表组织同意）。如果未获同意就重新连接，Microsoft 会停留在 **Approval required**（需要批准）页面，凭据将没有令牌，导致所有操作失败，而不只是删除操作失败。

聊天消息使用凭据已包含的 `Chat.ReadWrite` 作用域。如果使用 **Microsoft OAuth2 (Graph)** 凭据，请自行添加作用域。

**Service Principal (App-Only)**（服务主体，仅应用）凭据不支持 **Delete**（删除）和 **Undo Delete**（撤销删除），因为 Microsoft Graph 仅向已登录用户提供这两个操作。请参阅[服务主体凭据支持范围](#service-principal-credential-support)。

## 聊天和聊天成员 <a id="chats-and-chat-members"></a>

Chat（聊天）资源从 n8n 2.41.0 起可用，用于处理已登录用户的聊天。**Get Many**（获取多项）列出聊天，**Get**（获取）返回从列表选择或按 ID 指定的聊天，**Create**（创建）开始新聊天。聊天 ID 以 `19:` 开头，可在 Teams Web 应用地址栏的 `conversations/` 后，或 Chat **Get Many** 结果的 `id` 字段中找到。n8n 会自动将你加入新聊天，因此 **Other Participants**（其他参与者）只需列出其他人。**Chat Type**（聊天类型）决定创建哪种聊天：

* **One-on-One**（一对一）：你与另一人的聊天。如果已与对方有聊天，Microsoft Teams 会返回已有聊天，而不会新建。
* **Group**（群组）：你与一名或多名其他人的聊天。可设置 **Topic**（主题），之后使用 Chat Member（聊天成员）操作添加或移除成员。

对每位参与者，可从列表选择用户，或输入 UPN/对象 ID。租户中的来宾账户应将 **Role**（角色）设为 **Guest**（来宾），因为 Microsoft Teams 不允许来宾作为所有者。对于其他组织的人员，请输入其对象 ID 和所属组织的 **Tenant ID**（租户 ID）。

Chat Member（聊天成员）**Remove**（移除）操作需要成员关系 ID，而非用户 ID。可从列表选择成员，或使用 Chat Member **Get Many**（获取多项）结果中的 `id` 字段。Microsoft Teams 不允许移除一对一聊天的成员，也不允许移除群组聊天的最后一名所有者。

**Service Principal (App-Only)**（服务主体，仅应用）凭据不支持 Chat（聊天）和 Chat Member（聊天成员）资源。请参阅[服务主体凭据支持范围](#service-principal-credential-support)。

## 服务主体凭据支持范围 <a id="service-principal-credential-support"></a>

**Service Principal (App-Only)**（服务主体，仅应用）凭据没有已登录用户，因此 Microsoft Teams 节点无法运行需要代表该用户执行的操作。下方列表说明各资源的支持情况。选择此凭据时，节点会隐藏不可用资源和操作的字段，并显示提示。如果工作流仍使用其中某项操作，会在发送任何请求前报错。

- **Activity Notification**（活动通知）：Send（发送）。需要 `TeamsActivity.Send` 应用程序权限，且接收者已安装配套 Teams 应用。请参阅[发送活动通知](#send-an-activity-notification)。
- **Channel**（频道）：全部操作。
- **Channel Message**（频道消息）：Get（获取）、Get Many（获取多项）和 Get Many Replies（获取多条回复）。Create（创建）和 Reply（回复）不可用，因为仅应用 Microsoft Graph 对频道消息只支持迁移导入。Delete（删除）和 Undo Delete（撤销删除）也不可用，因为 Microsoft Graph 仅向已登录用户提供这些操作。需要这四项操作时，请使用 OAuth2 凭据。
- **Chat**（聊天）：不可用。仅应用 Microsoft Graph 没有可用于列出、获取或创建聊天的已登录用户。
- **Chat Member**（聊天成员）：不可用。节点的聊天选择器列出已登录用户的聊天，仅应用访问无法执行此操作，因此节点会阻止整个资源，包括按 ID 指定的聊天。
- **Chat Message**（聊天消息）：不可用。节点以已登录用户的身份发送和读取聊天消息。
- **Online Meeting**（联机会议）：全部操作，以 **Organizer**（组织者）字段所选用户的身份执行；选择此凭据后，节点会显示该字段。可从列表选择组织者，或输入其 UPN/对象 ID。应用注册需要 `OnlineMeetings.ReadWrite.All` 应用程序权限，Get（获取）操作使用 `OnlineMeetings.Read.All` 即可；从列表或按 UPN 选择组织者还需要 `User.Read.All`；另需 Microsoft Teams 应用程序访问策略，允许应用代表组织者管理会议。没有该策略，操作会因 403 错误而失败。设置方法请参阅[允许仅应用联机会议](../credentials/microsoftentraserviceprincipal.md#allow-app-only-online-meetings)。
- **Task**（任务）：全部操作。Get Many（获取多项）始终列出某个计划的任务：节点会隐藏 **Tasks For**（任务所属对象）选项，因此 **Group Member**（组成员）不可用。节点还会隐藏 **Team**（团队）选择器，**Plan**（计划）、**Bucket**（存储桶）和 **Assigned To**（分配给）字段仅接受 ID。

各操作所需的应用程序权限，请参阅 [Microsoft Entra 服务主体凭据](../credentials/microsoftentraserviceprincipal.md)。

## 发送活动通知 <a id="send-an-activity-notification"></a>

{% hint style="info" %}
**功能可用范围**

Activity Notification（活动通知）资源从 n8n 2.42.0 起可用。
{% endhint %}

Activity Notification（活动通知）的 **Send**（发送）操作向单个用户的活动源，即 Microsoft Teams 的 **Activity**（活动）选项卡，发布通知。它不会发送聊天消息或频道消息，因此也适用于不能发送消息的 **Service Principal (App-Only)**（服务主体，仅应用）凭据。可通过无人值守工作流提醒某个人，例如提醒待处理审批。

只有接收者安装了声明你所用凭据客户端 ID 的配套 Teams 应用，Microsoft Teams 才会显示通知。否则，Microsoft Graph 会以 HTTP 403 错误拒绝请求。管理员为每个租户设置一次此应用，再为每位接收者安装。请参阅[设置配套 Teams 应用](#set-up-the-companion-teams-app)。

### 字段 <a id="fields"></a>

| 字段 | 说明 |
|---|---|
| **Recipient**（接收者） | 接收通知的用户。**From List**（从列表）搜索 Microsoft Entra 目录。**By ID**（按 ID）接受用户对象 ID 或 UPN，例如 `jacob@contoso.com`。来宾用户需使用对象 ID：来宾 UPN 含有 `#EXT#`，该字段不接受此形式。 |
| **Headline**（标题） | 通知首行，以粗体显示。请保持简短，以便在一行内显示。 |
| **Preview Text**（预览文本） | 第二行。Teams 显示前 150 个字符。 |
| **Topic**（主题） | 第三行，以灰色显示。请说明通知涉及的对象，例如工作流或订单。 |
| **Topic Link**（主题链接） | 用户选择通知后打开的 Microsoft Teams 链接。必须为 Microsoft Teams 域名上的 `https` 链接，例如 `https://teams.microsoft.com/l/chat/0/0?users=someone@contoso.com`。请参阅[主题链接](#topic-link)。 |
| **Chain ID**（链 ID，可选） | 用于关联相关通知的数字。新通知使用相同 Chain ID 时，会替换活动源中的旧通知。保留 `0` 可发送不带链的通知。 |

节点为该用户调用 Microsoft Graph 的 [`sendActivityNotification`](https://learn.microsoft.com/en-us/graph/api/userteamwork-sendactivitynotification?view=graph-rest-1.0)，使用 `systemDefault` 活动类型。成功后返回 `{ "success": true }`。不支持团队或聊天接收者，也不支持自定义活动类型。

### 设置配套 Teams 应用 <a id="set-up-the-companion-teams-app"></a>

每个租户完成一次以下步骤。Microsoft Entra 管理员授予权限，Teams 管理员发布并安装应用。

配套应用必须声明凭据用于身份验证的应用注册的客户端 ID。对于 **Service Principal (App-Only)**（服务主体，仅应用）凭据，这是 **Application (Client) ID**（应用程序，客户端 ID）。对于 **Teams OAuth2** 或 **Microsoft OAuth2 (Graph)** 凭据，这是你自己的应用注册的 **Client ID**（客户端 ID）。在 n8n Cloud 中，Teams OAuth2 凭据可通过 n8n 管理的应用注册连接，该客户端 ID 不会显示，因此请改用服务主体凭据，或使用自己的应用注册的凭据。

#### 授予 Microsoft Graph 权限 <a id="grant-the-microsoft-graph-permission"></a>

<!-- vale off -->

- **Service Principal (App-Only)**（服务主体，仅应用）：在 [Microsoft Entra 管理中心](https://entra.microsoft.com/)打开应用注册，选择 **API permissions**（API 权限）> **Add a permission**（添加权限）> **Microsoft Graph** > **Application permissions**（应用程序权限），添加 `TeamsActivity.Send`，授予管理员同意。请参阅[添加应用程序权限](../credentials/microsoftentraserviceprincipal.md#add-application-permissions)。要通过 **From List**（从列表）选择接收者，还需添加 `User.Read.All`。
- **Teams OAuth2**：凭据从 n8n 2.42.0 起默认请求委派的 `TeamsActivity.Send` 作用域。此前连接的凭据需重新连接以获得该作用域。如果使用 **Custom Scopes**（自定义作用域），请先将 `TeamsActivity.Send` 添加到 **Enabled Scopes**（已启用的作用域）。
- **Microsoft OAuth2 (Graph)**：将 `TeamsActivity.Send` 添加到凭据的 **Scope**（作用域）字段，再重新连接。

<!-- vale on -->

#### 构建应用包 <a id="build-the-app-package"></a>

应用包是直接包含三个文件的 zip 文件：`manifest.json`、名为 `color.png` 的 192x192 PNG，以及名为 `outline.png` 的 32x32 PNG。对 Microsoft Graph 起作用的部分只有 `webApplicationInfo.id`，必须是你的客户端 ID。应用无需机器人、选项卡或其他能力。

{% code title="manifest.json" %}
```json
{
	"$schema": "https://developer.microsoft.com/en-us/json-schemas/teams/v1.17/MicrosoftTeams.schema.json",
	"manifestVersion": "1.17",
	"version": "1.0.0",
	"id": "<new-guid>",
	"developer": {
		"name": "Contoso",
		"websiteUrl": "https://www.contoso.com",
		"privacyUrl": "https://www.contoso.com/privacy",
		"termsOfUseUrl": "https://www.contoso.com/terms"
	},
	"name": {
		"short": "n8n Notifications"
	},
	"description": {
		"short": "Lets n8n workflows post to your Teams activity feed.",
		"full": "Companion app that lets an n8n Microsoft Teams credential send activity feed notifications."
	},
	"icons": {
		"color": "color.png",
		"outline": "outline.png"
	},
	"accentColor": "#FF6D5A",
	"webApplicationInfo": {
		"id": "<application-client-id>",
		"resource": "api://<application-client-id>"
	}
}
```
{% endcode %}

将 `<new-guid>` 替换为新生成的应用 GUID，例如通过 `uuidgen` 生成；将两处 `<application-client-id>` 都替换为你的客户端 ID。然后直接压缩这三个文件，不要包含文件夹：

```bash
zip -j n8n-notifications.zip manifest.json color.png outline.png
```

#### 将应用发布到组织目录 <a id="publish-the-app-to-your-organizations-catalog"></a>

在 [Teams 管理中心](https://admin.teams.microsoft.com/)进入 **Teams apps**（Teams 应用）> **Manage apps**（管理应用），选择 **Actions**（操作）> **Upload new app**（上传新应用），上传 zip 文件。只有管理员能执行此操作：仅应用访问无法发布到目录，因此 n8n 无法代你设置该应用。

#### 为每位接收者安装应用 <a id="install-the-app-for-each-recipient"></a>

通过 Microsoft Graph，在接收者的个人范围内安装应用。可从 [Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer) 发送请求：打开 **Modify permissions**（修改权限），发送前同意授予 `AppCatalog.Read.All` 和 `TeamsAppInstallation.ReadWriteForUser`。任何以你的应用注册身份调用 Microsoft Graph 的工具也可使用，但需要 `TeamsAppInstallation.ReadWriteForUser.All` 应用程序权限。

先查找应用的目录 ID。它与 manifest 中的 `id` 不同，Microsoft Graph 将后者称为 `externalId`：

```http
GET https://graph.microsoft.com/v1.0/appCatalogs/teamsApps?$filter=externalId eq '<manifest-id>'
```

然后为接收者安装应用，将响应中的 `id` 用作 `<catalog-app-id>`：

```http
POST https://graph.microsoft.com/v1.0/users/<user-id>/teamwork/installedApps
Content-Type: application/json

{
	"teamsApp@odata.bind": "https://graph.microsoft.com/v1.0/appCatalogs/teamsApps/<catalog-app-id>"
}
```

HTTP 409 响应表示该用户已安装此应用。请为每位需要接收通知的用户重复安装步骤。

#### 等待安装生效 <a id="allow-time-for-the-install-to-propagate"></a>

安装需要时间传播。在生效前，Microsoft Graph 会持续返回“not installed”（未安装）的 HTTP 403 错误。在 n8n 的测试中，首条通知在安装约五分钟后才成功发出。刚安装后出现 403，并不意味着安装失败。

### 主题链接 <a id="topic-link"></a>

用户选择通知后，Teams 会打开 **Topic Link**（主题链接）。Microsoft Graph 仅接受 Microsoft Teams 链接，因此通知不能链接到 n8n 执行或其他网站。节点会在发送请求前检查链接。主权云的 Teams 域名链接也适用，例如 `teams.microsoft.us`。

链接还必须打开真实存在的内容，否则用户选择通知时 Teams 会报错。请使用以下任一种：

- 聊天链接，例如 `https://teams.microsoft.com/l/chat/0/0?users=someone@contoso.com`，用于打开与该用户的聊天。
- 从 Teams 复制的频道、消息或会议链接，用于打开相应对象。

链接格式请参阅 Microsoft 的 [Teams 聊天、频道和消息深层链接](https://learn.microsoft.com/en-us/microsoftteams/platform/concepts/build-and-test/deep-link-teams)文档。

### 常见错误 <a id="common-errors"></a>

| 错误 | 原因 | 解决方法 |
|---|---|---|
| `The companion Teams app is not installed for this recipient` | Microsoft Graph 返回 HTTP 403。接收者未安装在 `webApplicationInfo.id` 下声明你所用客户端 ID 的应用，或安装尚未生效。 | 完成[设置配套 Teams 应用](#set-up-the-companion-teams-app)。检查 `webApplicationInfo.id` 是否与凭据的客户端 ID 一致。同 ID 的机器人应用不算配套应用。安装后等待约五分钟。 |
| `The app registration is missing the TeamsActivity.Send application permission` | Microsoft Graph 向服务主体凭据返回 HTTP 403。应用注册缺少 `TeamsActivity.Send` 应用程序权限，或未获得相应管理员同意。 | 添加权限并授予管理员同意。也可改为向配套应用 manifest 添加资源特定的 `TeamsActivity.Send.User` 权限，再为接收者安装更新后的应用。 |
| `The credential is missing the TeamsActivity.Send permission` | Microsoft Graph 返回 HTTP 403，所用凭据为 OAuth2。令牌缺少委派的 `TeamsActivity.Send` 作用域。 | 重新连接凭据。使用 **Custom Scopes**（自定义作用域）时，先将作用域添加到 **Enabled Scopes**（已启用的作用域）。使用 **Microsoft OAuth2 (Graph)** 凭据时，将其添加到 **Scope**（作用域）。 |
| `The Topic Link is required`、`The Topic Link must be a Microsoft Teams link` | 节点在发送前检查链接，发现其为空、不符合 `https`，或不属于 Microsoft Teams 域名。 | 输入 Teams 深层链接。请参阅[主题链接](#topic-link)。 |
| `The recipient was not found` | Microsoft Graph 针对该用户 ID 或 UPN 返回 HTTP 404。 | 检查该值，或通过 **From List**（从列表）选择用户。来宾用户请使用对象 ID。 |

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Microsoft Teams 集成模板](https://n8n.io/integrations/microsoft-teams)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Microsoft Teams API 文档](https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
