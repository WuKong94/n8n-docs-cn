---
title: Microsoft Teams 触发器节点文档
description: 了解如何在 n8n 中使用 Microsoft Teams 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Microsoft Teams 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftteamstrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftteamstrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftteamstrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Teams 触发器节点 <a href="#microsoft-teams-trigger-node" id="microsoft-teams-trigger-node"></a>

使用 Microsoft Teams Trigger 节点响应 [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software) 中的事件，并将其与其他应用集成。

本页列出了 Microsoft Teams Trigger 节点可响应的事件，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Microsoft 凭据文档](../credentials/microsoft.md)。此节点也支持 [Microsoft Entra 服务主体凭据](../credentials/microsoftentraserviceprincipal.md)，可在没有用户登录的情况下提供仅应用访问：在 **Authentication**（身份验证）下拉菜单中选择 **Service Principal (App-Only)**（服务主体，仅应用）。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果使用政府云租户（US Government、US Government DOD 或 China），请在 Microsoft 凭据配置中选择适当的 **Microsoft Graph API Base URL**（Microsoft Graph API 基础 URL）。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* **New Channel**（新频道）
* **New Channel Message**（新的频道消息）
* **New Chat**（新聊天）
* **New Chat Message**（新的聊天消息）
* **New Team Member**（新的团队成员）

## 所需作用域 <a id="required-scopes"></a>

每种事件都订阅一个 Microsoft Graph 资源，并需要表中列出的委托权限之一；权限按从低到高的顺序列出：

| 事件 | 委托权限 |
|---|---|
| **New Channel**（新频道） | `Channel.ReadBasic.All` |
| **New Channel Message**（新的频道消息） | `ChannelMessage.Read.All` |
| **New Chat**（新聊天） | `Chat.ReadBasic`、`Chat.Read` 或 `Chat.ReadWrite` |
| **New Chat Message**（新的聊天消息） | `Chat.Read` 或 `Chat.ReadWrite` |
| **New Team Member**（新的团队成员） | `TeamMember.Read.All` |

在节点中列出团队需要 `Team.ReadBasic.All`，列出频道需要 `Channel.ReadBasic.All`。`ChannelMessage.Read.All` 和 `TeamMember.Read.All` 需要 Microsoft Entra 管理员授予管理员同意，而 `Team`、`Channel` 和 `Chat` 权限不需要。

从 n8n 2.45.0 起，**Teams OAuth2** 凭据默认覆盖所有事件：`TeamMember.Read.All` 是其 [Microsoft Teams 默认作用域](../credentials/microsoft.md#default-scopes-for-microsoft-teams)之一。

凭据的默认作用域 `User.Read.All` 和 `Group.ReadWrite.All` 是权限更高的替代项，同样覆盖团队列表、频道列表和 **New Channel**（新频道）订阅，无需为此给凭据额外授权。`User.Read.All` 和 `Group.ReadWrite.All` 需要管理员同意。

在 n8n 2.45.0 之前连接的凭据，重新连接时会请求 `TeamMember.Read.All`。Microsoft Entra 管理员必须在重新连接前同意该作用域，否则登录会失败。管理员在 n8n Cloud 上的批准方法，请参阅 Microsoft 凭据文档的[新增作用域需要重新批准](../credentials/microsoft.md#new-scopes-need-a-new-approval)。如果凭据使用 **Custom Scopes**（自定义作用域），且 **Enabled Scopes**（已启用作用域）中尚无该作用域，请先添加，再重新连接。在 n8n 2.45.0 之前的版本中，请在凭据中开启 **Custom Scopes**（从 n8n 2.6.0 起提供），将该作用域添加到 **Enabled Scopes**，然后重新连接。

使用 **Microsoft OAuth2 (Graph)** 凭据时，请在凭据的 **Scope**（作用域）字段中输入作用域。包含 `openid offline_access`，以便凭据刷新令牌。例如，要以最低权限作用域使用所有事件：

```
openid offline_access Team.ReadBasic.All Channel.ReadBasic.All Chat.Read ChannelMessage.Read.All TeamMember.Read.All
```

**Service Principal (App-Only)**（服务主体，仅应用）凭据改用应用权限。各事件所需的权限，请参阅 Microsoft Entra 服务主体凭据文档中的[各节点所需的应用权限](../credentials/microsoftentraserviceprincipal.md#required-application-permissions-by-node)。此凭据不支持聊天事件。

## 订阅续期 <a id="subscription-renewal"></a>

{% hint style="info" %}
**功能可用性**

从 n8n 2.45.1 起，Microsoft Teams Trigger 节点支持自动续期订阅。
{% endhint %}

发布工作流时，Microsoft Teams Trigger 节点会为其监控的每个资源创建 Microsoft Graph 变更通知订阅。Microsoft Graph 的 Teams 订阅三天后过期。Microsoft Graph 发送订阅生命周期通知时，触发器会为该订阅续期，因此已发布的工作流可持续接收事件，无需你操作。

在 n8n 2.45.1 之前，触发器不会为订阅续期，因此发布工作流约三天后便停止接收事件。在这些版本上，请[取消发布工作流](../../../build/understand-workflows/save-and-publish-workflows.md#how-to-unpublish-a-workflow)，然后重新发布。此后触发器可再接收约三天的新事件。

升级后，只要订阅尚未过期，触发器也会为旧版 n8n 创建的订阅续期。如果工作流在升级前已经停止接收事件，请取消发布并重新发布。如果你曾创建定时工作流来续期订阅或重新发布触发器工作流，请在升级后先取消发布触发器工作流，再重新发布。随后即可取消发布那个定时工作流。

从 n8n 2.45.1 起，生命周期通知（`reauthorizationRequired` 和 `subscriptionRemoved`）不再作为条目进入工作流。在 n8n 2.45.1 之前，每次生命周期通知都会启动一次执行。如果你的工作流使用 [If](../core-nodes/n8n-nodes-base.if.md) 节点按 `lifecycleEvent` 筛除这些通知，升级后可移除该分支。

续期仅在你的 n8n 实例可访问时有效。如果订阅在 n8n 停机或不可访问期间过期，触发器会停止接收事件。请取消发布工作流并重新发布，以重新创建订阅。

如果工作流没有已保存的订阅密钥，例如静态数据丢失或导入工作流后，触发器不会为其订阅续期。订阅会过期，触发器也会停止接收事件。实例日志会显示 `Microsoft Teams Trigger: skipped lifecycle notifications: no stored secret, republish the workflow`。解决方法是取消发布工作流并重新发布。

续期也可能因其他原因失败，例如 Microsoft Graph 速率限制、刷新令牌过期或同意被撤销。触发器不会重试，工作流也不会显示失败执行。实例日志中会出现以下某条记录：

* `Microsoft Teams Trigger: failed to renew subscription`
* `Microsoft Teams Trigger: failed to re-create subscription`
* `Microsoft Teams Trigger: failed to list subscriptions or resolve resources, skipped re-create`

如果订阅到期前没有成功续期，触发器会停止接收事件。如果触发器重新创建订阅失败，它已经停止接收该资源的事件。

如果刷新令牌过期，请重新连接凭据。如果同意被撤销，Microsoft Entra 管理员必须先重新授予同意，你才能重新连接 OAuth2 凭据。如果凭据是在 n8n 2.45.0 之前连接的，重新连接还会请求需要管理员同意的 `TeamMember.Read.All`，详情见[所需作用域](#required-scopes)。然后取消发布工作流并重新发布，以重新创建订阅。

默认日志设置下，这些日志行不包含工作流 ID 或错误消息。如果自行托管 n8n，将 `N8N_LOG_FORMAT` 设置为 `json` 即可包含这些信息。更多信息请参阅[日志环境变量](../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/logs.md)。

如果触发器停止接收事件，而你找不到上述日志记录，请取消发布工作流并重新发布。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Microsoft Teams 提供应用节点。更多信息请参阅 [Microsoft Teams 节点文档](../app-nodes/n8n-nodes-base.microsoftteams.md)。


在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/microsoft-teams-trigger/)。


API 的详细信息，请参阅 [Microsoft Teams 文档](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0)。
