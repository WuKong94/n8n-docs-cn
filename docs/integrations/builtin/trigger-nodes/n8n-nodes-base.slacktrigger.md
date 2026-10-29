---
title: Slack 触发器节点文档
description: 了解如何在 n8n 中使用 Slack 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Slack 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Slack 触发器节点 <a href="#slack-trigger-node" id="slack-trigger-node"></a>

使用 Slack Trigger 节点响应 [Slack](https://slack.com/) 中的事件，并将其与其他应用集成。n8n 内置支持多种 Slack 事件，包括新消息、表情回应和新频道。

本页列出了 Slack Trigger 节点可响应的事件，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Slack 凭据文档](../credentials/slack.md)。
{% endhint %}
{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Slack 集成](https://n8n.io/integrations/slack-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* **Any Event**（任意事件）：Slack 中的任意事件都会触发节点。
* **App Home Opened**（应用主页已打开）：用户打开你的 Slack 应用的 [App Home（应用主页）](https://api.slack.com/surfaces/app-home)标签页时触发节点。
* **Bot / App Mention**（提及机器人或应用）：在应用已加入的频道中[提及](https://slack.com/help/articles/205240127-Use-mentions-in-Slack)你的机器人或应用时触发节点。
* **File Made Public**（文件设为公开）：文件[设为公开](https://slack.com/help/articles/4412651915539-Manage-public-file-sharing)时触发节点。
* **File Shared**（文件已共享）：在应用已加入的频道中[共享](https://slack.com/help/articles/201330736-Add-files-to-Slack)文件时触发节点。
* **New Message Posted to Channel**（频道中发布了新消息）：在应用已加入的频道中发布新消息时触发节点。
* **New Public Channel Created**（创建了新的公开频道）：创建新的[公开频道](https://slack.com/help/articles/360017938993-What-is-a-channel)时触发节点。
* **New User**（新用户）：向 Slack 添加新用户时触发节点。
* **Reaction Added**（添加了表情回应）：在应用所加入的消息中添加[表情回应](https://slack.com/help/articles/202931348-Use-emoji-and-reactions)时触发节点。

## 参数 <a href="#parameters" id="parameters"></a>

设置触发事件后，可使用其余参数进一步定义节点行为：

* **Watch Whole Workspace**（监控整个工作区）：是否在工作区的所有频道中监控所选 **Events**（事件）；开启则监控，关闭则不监控，默认为关闭。<br>

    <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p><strong>注意</strong></p><p>机器人或应用所在的任何频道中，每发生一个事件都会消耗一次执行。请谨慎使用！</p></div>

* **Channel to Watch**（要监控的频道）：选择节点监控所选 **Events**（事件）的频道。此参数仅在未开启 **Watch Whole Workspace**（监控整个工作区）时显示。可以通过以下方式选择频道：
    * **From list**（从列表选择）：节点使用你的凭据查询工作区中的频道列表，供你选择所需频道。
    * **By ID**（按 ID）：输入要监控的频道 ID。Slack 在频道详情底部显示频道 ID，并提供一键复制按钮。
    * **By URL**（按 URL）：输入要监控的频道 URL，格式为 `https://app.slack.com/client/<channel-address>`。
* **Download Files**（下载文件）：是否下载文件并用于节点输出；开启则下载，关闭则不下载，默认为关闭。此参数适用于 **File Made Public**（文件设为公开）和 **File Shared**（文件已共享）事件。

## 选项 <a href="#options" id="options"></a>

使用 **Add Option**（添加选项）可进一步调整节点行为：

* **Resolve IDs**（解析 ID）：是否将 ID 解析为对应名称并返回；开启则解析，关闭则不解析，默认为关闭。
* **Usernames or IDs to ignore**（要忽略的用户名或 ID）：选择用户名，或输入以逗号分隔的编码用户 ID 字符串，以忽略这些用户的事件。可从列表选择，也可使用[表达式](../../../build/work-with-data/expressions-versus-data-nodes.md)指定 ID。
* **Emoji Names to Filter**（要筛选的表情名称）：输入以逗号分隔、**不是**冒号分隔的表情名称列表（例如 `thumbsup, eyes, white_check_mark`），将 **Reaction Added**（添加了表情回应）事件限定为这些指定的表情回应。留空则任何表情回应都会触发。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Slack 提供应用节点。更多信息请参阅 [Slack 节点文档](../app-nodes/n8n-nodes-base.slack/README.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/slack-trigger/)。

API 的详细信息，请参阅 [Slack 文档](https://api.slack.com/apis/connections/events-api)。

## 所需作用域 <a href="#required-scopes" id="required-scopes"></a>

使用此节点前，需要在 Slack 中创建应用并启用事件订阅。更多信息请参阅 [Slack 凭据 | Slack Trigger 配置](../credentials/slack.md#slack-trigger-configuration)。

必须为 Slack 应用添加适当的作用域，此触发器节点才能正常工作。

节点至少需要 [conversations.list](https://api.slack.com/methods/conversations.list) 和 [users.list](https://api.slack.com/methods/users.list) 方法所需的作用域。更完整的作用域列表，请参阅[作用域 | Slack 凭据](../credentials/slack.md#scopes)。

## 验证 Webhook <a href="#verify-the-webhook" id="verify-the-webhook"></a>

{% hint style="info" %}
**功能可用性**

从 n8n 1.106.0 起，支持使用 Slack Signing Secret（签名密钥）验证传入的 Webhook 请求是否来自 Slack。
{% endhint %}

配置 [Slack 凭据](../credentials/slack.md#slack-trigger-configuration)时，可设置 [Slack Signing Secret（签名密钥）](https://api.slack.com/authentication/verifying-requests-from-slack#signing_secrets_admin_page)。设置后，Slack 触发器节点会自动验证请求是否来自 Slack 且包含可信签名。n8n 建议设置此项，确保只处理来自 Slack 的请求。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下列出 Slack Trigger 节点的常见错误和问题，以及解决或排查步骤。

### 工作流只能在测试或生产环境之一正常运行 <a href="#workflow-only-works-in-testing-or-production" id="workflow-only-works-in-testing-or-production"></a>

Slack 每个应用只允许注册一个 Webhook。这意味着，在测试 URL 和生产 URL 之间切换时，必须重新配置已注册的 Webhook URL。

测试已发布的工作流时，可能因此遇到问题。Slack 只会将事件发送到两个 Webhook URL 中的一个，另一个始终收不到事件通知。

一种解决办法是在测试时停用工作流：

{% hint style="warning" %}
**会中断生产流量**

这会为了测试暂时停用生产工作流。取消发布期间，工作流将不再接收生产流量。
{% endhint %}

1. 进入工作流页面。
2. 从工作流设置下拉菜单中点击 **Unpublish**（取消发布），暂时停用工作流。
3. 在 [Slack Trigger 配置](../credentials/slack.md#slack-trigger-configuration)中编辑 **Request URL**（请求 URL），将生产 Webhook URL 改为测试 Webhook URL。
4. 使用测试 Webhook URL 测试工作流。
5. 测试完成后，在 [Slack Trigger 配置](../credentials/slack.md#slack-trigger-configuration)中编辑 **Request URL**（请求 URL），将测试 Webhook URL 改回生产 Webhook URL。
6. 点击 **Publish**（发布）重新启用工作流。生产 Webhook URL 应恢复工作。

### 令牌过期 <a href="#token-expired" id="token-expired"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/slack/token-rotation.md" %}
