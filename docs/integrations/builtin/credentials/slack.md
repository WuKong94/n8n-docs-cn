---
title: Slack 凭据
description: Slack 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Slack 的身份验证。
contentType:
- integration
- reference
priority: high
nodeTitle: Slack 凭据
originalFilePath: integrations/builtin/credentials/slack.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/slack
url: https://docs.n8n.io/integrations/builtin/credentials/slack
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Slack 凭据 <a href="#slack-credentials" id="slack-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Slack](../app-nodes/n8n-nodes-base.slack/README.md)
- [Slack Trigger（触发器）](../trigger-nodes/n8n-nodes-base.slacktrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）：
    - [Slack Trigger（触发器）](../trigger-nodes/n8n-nodes-base.slacktrigger.md)节点必须使用此方式。
    - 可用于 [Slack](../app-nodes/n8n-nodes-base.slack/README.md) 节点，但不推荐。
- OAuth2：
    - [Slack](../app-nodes/n8n-nodes-base.slack/README.md) 节点推荐使用此方式。
    - 不适用于 [Slack Trigger（触发器）](../trigger-nodes/n8n-nodes-base.slacktrigger.md)节点。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Slack API 文档](https://api.slack.com/apis)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要一个 [Slack](https://slack.com/) 账号，以及：

- 一个 **Access Token（访问令牌）**

生成访问令牌需要创建 Slack 应用。n8n 建议通过清单创建，一步即可配置全部作用域：

### 为 API 访问令牌通过清单创建应用 <a id="create-the-app-from-a-manifest-for-api-access-token"></a>

1. 打开 [Slack API Apps](https://api.slack.com/apps) 页面。
2. 选择 **Create New App > From a manifest**（创建新应用 > 从清单创建）。
3. 选择开发应用所用的 **Workspace**（工作区），再选择 **Next**（下一步）。
4. 选择 **JSON** 选项卡，用下方 JSON 替换默认清单，并按需调整[作用域](#scopes)。
5. 选择 **Next**（下一步）。
6. 查看摘要，选择 **Create**（创建），随后打开应用详情。

```json
{
	"display_information": {
		"name": "n8n integration"
	},
	"features": {
		"bot_user": {
			"display_name": "n8n integration"
		}
	},
	"oauth_config": {
		"scopes": {
			"bot": [
				"channels:read",
				"channels:history",
				"chat:write",
				"files:read",
				"files:write",
				"groups:read",
				"groups:history",
				"im:read",
				"im:history",
				"mpim:read",
				"mpim:history",
				"reactions:read",
				"reactions:write",
				"usergroups:read",
				"usergroups:write",
				"users.profile:read",
				"users:read"
			]
		}
	},
	"settings": {
		"org_deploy_enabled": false,
		"socket_mode_enabled": false,
		"token_rotation_enabled": false
	}
}
```

### 为 API 访问令牌从头创建应用 <a id="create-the-app-from-scratch-for-api-access-token"></a>

1. 打开 [Slack API Apps](https://api.slack.com/apps) 页面。
2. 选择 **Create New App > From scratch**（创建新应用 > 从头创建）。
3. 输入 **App Name**（应用名称）。
4. 选择开发应用所用的 **Workspace**（工作区）。
5. 选择 **Create App**（创建应用），随后打开应用详情。
6. 在左侧菜单的 **Features**（功能）下，选择 **OAuth & Permissions**（OAuth 与权限）。
7. 在 **Scopes**（作用域）部分，为应用选择适当作用域。建议列表，请参阅[作用域](#scopes)。

然后安装应用并复制令牌：

1. 在左侧菜单的 **Features**（功能）下，选择 **OAuth & Permissions**（OAuth 与权限）。
2. 在 **OAuth Tokens**（OAuth 令牌）部分，选择 **Install to Workspace**（安装到工作区）。此操作必须由 Slack 工作区管理员完成。
3. 选择 **Allow**（允许）。
4. 复制 **Bot User OAuth Token**（机器人用户 OAuth 令牌），填入 n8n 凭据的 **Access Token**（访问令牌）。
5. 如果此凭据用于 [Slack Trigger（触发器）](../trigger-nodes/n8n-nodes-base.slacktrigger.md)，请按照 [Slack Trigger 配置](#slack-trigger-configuration)中的步骤完成应用设置。

更多信息，请参阅 Slack API 的[快速入门](https://api.slack.com/quickstart)。

### Slack Trigger 配置 <a href="#slack-trigger-configuration" id="slack-trigger-configuration"></a>

将 Slack 应用用于 [Slack Trigger（触发器）](../trigger-nodes/n8n-nodes-base.slacktrigger.md)节点的步骤如下：

1. 在 Slack 中打开 [Your Apps（你的应用）](https://api.slack.com/apps/)，选择要使用的应用。
2. 进入 **Features**（功能）> **Event Subscriptions**（事件订阅）。
3. 开启 **Enable Events**（启用事件）控件。
4. 在 n8n 中复制 **Webhook URL**，填入 Slack 应用的 **Request URL**（请求 URL）。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Request URL（请求 URL）</strong></p><p>Slack 每个应用只允许一个请求 URL。测试工作流时，需要选择以下一种方式：</p><ul><li>先使用 <strong>Test URL（测试 URL）</strong>测试，确认全部正常后，再将 Slack 应用改为使用 <strong>Production URL（生产 URL）</strong></li><li>使用 <strong>Production URL（生产 URL）</strong>并启用执行日志。</li></ul></div>

5. 验证通过后，选择要订阅的机器人事件，使用 n8n 的 **Trigger on**（触发条件）字段过滤这些请求。
    - 如需使用列表中没有的事件，将其添加为机器人事件，再在 n8n 节点中选择 **Any Event**（任意事件）。

更多信息，请参阅[快速入门 | 配置应用监听事件](https://api.slack.com/quickstart#listening)。

{% hint style="info" %}
Slack 验证 **Request URL**（请求 URL）后，也可在应用清单中管理事件订阅：进入 **Settings**（设置）> **App Manifest**（应用清单），编辑 `settings.event_subscriptions` 块。
{% endhint %}

n8n 建议为 Slack Trigger 启用请求签名验证，增强安全性：

1. 在 Slack 中打开 [Your Apps（你的应用）](https://api.slack.com/apps/)，选择要使用的应用。
2. 进入 **Settings**（设置）> **Basic Information**（基本信息）。
3. 复制 **Signing Secret**（签名密钥）的值。
4. 在 n8n 中，将该值粘贴到凭据的 **Signature Secret**（签名密钥）字段。

[在 Slack 中进行审批](../app-nodes/n8n-nodes-base.slack/approvals.md)也需要 **Signature Secret**（签名密钥）字段。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果[自托管 n8n](../../../deploy/host-n8n/README.md)且需要从头配置 OAuth2，则需要 [Slack](https://slack.com/) 账户，以及：

- 一个 **Client ID（客户端 ID）**
- 一个 **Client Secret（客户端密钥）**

如需获取这两项，请创建 Slack 应用。n8n 建议通过清单创建，一步配置作用域及重定向 URL：

### 为 OAuth2 通过清单创建应用 <a id="create-the-app-from-a-manifest-for-oauth2"></a>

1. 在 n8n 中，从 Slack 凭据复制 **OAuth Callback URL**（OAuth 回调 URL）。
2. 打开 [Slack API Apps](https://api.slack.com/apps) 页面。
3. 选择 **Create New App > From a manifest**（创建新应用 > 从清单创建）。
4. 选择开发应用所用的 **Workspace**（工作区），再选择 **Next**（下一步）。
5. 选择 **JSON** 选项卡，用下方 JSON 替换默认清单。将 `<your-oauth-callback-url>` 替换为从 n8n 复制的 URL，并按需调整[作用域](#scopes)。
6. 选择 **Next**（下一步）。
7. 查看摘要，选择 **Create**（创建），随后打开应用详情。

```json
{
	"display_information": {
		"name": "n8n integration"
	},
	"features": {
		"bot_user": {
			"display_name": "n8n integration"
		}
	},
	"oauth_config": {
		"redirect_urls": [
			"<your-oauth-callback-url>"
		],
		"scopes": {
			"bot": [
				"channels:read",
				"channels:history",
				"chat:write",
				"files:read",
				"files:write",
				"groups:read",
				"groups:history",
				"im:read",
				"im:history",
				"mpim:read",
				"mpim:history",
				"reactions:read",
				"reactions:write",
				"usergroups:read",
				"usergroups:write",
				"users.profile:read",
				"users:read"
			],
			"user": [
				"channels:write",
				"groups:write",
				"search:read",
				"search:read.public",
				"search:read.private",
				"search:read.im",
				"search:read.mpim",
				"stars:read",
				"stars:write",
				"users.profile:write"
			]
		}
	},
	"settings": {
		"org_deploy_enabled": false,
		"socket_mode_enabled": false,
		"token_rotation_enabled": false
	}
}
```

<details>

<summary>仅包含用户作用域的清单</summary>

部分 Slack API 端点（包括 Slack MCP 端点）仅支持用户令牌，不支持机器人令牌。如需用户令牌，请改用此清单，它将全部作用域作为用户作用域请求：

```json
{
	"display_information": {
		"name": "n8n integration"
	},
	"oauth_config": {
		"redirect_urls": [
			"<your-oauth-callback-url>"
		],
		"scopes": {
			"user": [
				"channels:read",
				"channels:write",
				"channels:history",
				"chat:write",
				"files:read",
				"files:write",
				"groups:read",
				"groups:write",
				"groups:history",
				"im:read",
				"im:history",
				"mpim:read",
				"mpim:history",
				"reactions:read",
				"reactions:write",
				"stars:read",
				"stars:write",
				"usergroups:read",
				"usergroups:write",
				"users.profile:read",
				"users.profile:write",
				"users:read",
				"search:read",
				"search:read.public",
				"search:read.private",
				"search:read.im",
				"search:read.mpim"
			]
		}
	},
	"settings": {
		"org_deploy_enabled": false,
		"socket_mode_enabled": false,
		"token_rotation_enabled": false
	}
}
```

</details>

### 为 OAuth2 从头创建应用 <a id="create-the-app-from-scratch-for-oauth2"></a>

1. 打开 [Slack API Apps](https://api.slack.com/apps) 页面。
2. 选择 **Create New App > From scratch**（创建新应用 > 从头创建）。
3. 输入 **App Name**（应用名称）。
4. 选择开发应用所用的 **Workspace**（工作区）。
5. 选择 **Create App**（创建应用），随后打开应用详情。
6. 在左侧菜单的 **Features**（功能）下，选择 **OAuth & Permissions**（OAuth 与权限）。
7. 在 **Redirect URLs**（重定向 URL）部分，选择 **Add New Redirect URL**（添加新重定向 URL）。
8. 从 n8n 复制 **OAuth Callback URL**（OAuth 回调 URL），填入 Slack 的新重定向 URL。
9. 选择 **Add**（添加）。
10. 选择 **Save URLs**（保存 URL）。
11. 在 **Scopes**（作用域）部分，为应用选择适当作用域。作用域列表，请参阅[作用域](#scopes)。

然后完成应用与 n8n 的连接：

1. 在 **Settings > Basic Information**（设置 > 基本信息）中，打开 **App Credentials**（应用凭据）部分。
2. 复制 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥），粘贴到 n8n 的对应字段。
3. 在左侧菜单的 **Features**（功能）下，选择 **OAuth & Permissions**（OAuth 与权限）。
4. 在 **OAuth Tokens**（OAuth 令牌）部分，选择 **Install to Workspace**（安装到工作区）。此操作必须由 Slack 工作区管理员完成。
5. 选择 **Allow**（允许）。
6. 此时应可点击 n8n 凭据中的 OAuth 按钮进行连接。

更多信息，请参阅 Slack API 的[快速入门](https://api.slack.com/quickstart)；OAuth 流程本身的更多详情，请参阅 Slack 的[通过 OAuth 安装](https://api.slack.com/authentication/oauth-v2)文档。

## 作用域 <a href="#scopes" id="scopes"></a>

作用域决定应用具有哪些权限。

* 如需应用代表授权用户执行操作，在 **User Token Scopes**（用户令牌作用域）部分添加所需作用域。
* 构建机器人时，在 **Bot Token Scopes**（机器人令牌作用域）部分添加所需作用域。

以下列出 OAuth 凭据要求的作用域，可作为起点。上方应用清单已包含这些作用域：

| **作用域名称** | **说明** |
|-----------------------| -- |
| `channels:read`       | |
| `channels:write` | 不可用作机器人令牌作用域 |
| `channels:history`    | |
| `chat:write`          | |
| `files:read`          | |
| `files:write`         | |
| `groups:read`         | |
| `groups:write` | 用于私密频道管理操作 |
| `groups:history`      | |
| `im:read`             | |
| `im:history`          | |
| `mpim:read`           | |
| `mpim:history`        | |
| `reactions:read`      | |
| `reactions:write`     | |
| `stars:read` | 不可用作机器人令牌作用域 |
| `stars:write` | 不可用作机器人令牌作用域 |
| `usergroups:read`     | |
| `usergroups:write`    | | 
| `users.profile:read`  | |
| `users.profile:write` | 不可用作机器人令牌作用域 |
| `users:read`          | |
| `search:read` | 已被 Slack 弃用，为节点版本 <= 2.6 保留 |
| `search:read.public` | 用于公开频道消息搜索 |
| `search:read.private` | 不可用作机器人令牌作用域 |
| `search:read.im` | 不可用作机器人令牌作用域 |
| `search:read.mpim` | 不可用作机器人令牌作用域 |

## 常见问题 <a href="#common-issues" id="common-issues"></a>

### 令牌过期 <a href="#token-expired" id="token-expired"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/slack/token-rotation.md" %}
