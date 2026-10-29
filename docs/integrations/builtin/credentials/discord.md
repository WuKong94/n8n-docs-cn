---
title: Discord 凭据
contentType:
- integration
- reference
priority: high
nodeTitle: Discord 凭据
originalFilePath: integrations/builtin/credentials/discord.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/discord
url: https://docs.n8n.io/integrations/builtin/credentials/discord
description: Discord 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Discord 的身份验证。
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
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Discord 凭据 <a id="discord-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Discord](../app-nodes/n8n-nodes-base.discord/README.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建 [Discord](https://www.discord.com/) 账户。
* 对于 Bot 和 OAuth2 凭据：
  * [设置本地开发环境](https://discord.com/developers/docs/quick-start/getting-started#step-0-project-setup)。
  * [创建应用和机器人用户](https://discord.com/developers/docs/quick-start/getting-started#step-1-creating-an-app)。
* 对于 webhook 凭据，请[创建 webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Bot（机器人）
* OAuth2
* Webhook

不确定使用哪种方式？更多指引，请参阅[选择身份验证方式](discord.md#choose-an-authentication-method)。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Discord 开发者文档](https://discord.com/developers/docs/intro)。

## 使用机器人 <a href="#using-bot" id="using-bot"></a>

如需使用机器人令牌而非 OAuth2 将机器人添加到 Discord 服务器，请使用此方式。

配置此凭据需要：

* **Bot Token**（机器人令牌）：创建包含机器人的应用后生成。

创建包含机器人的应用并生成 **Bot Token**（机器人令牌）的步骤如下：

1. 如果尚无应用，请先在[开发者门户](https://discord.com/developers/applications?new_application=true)创建。
2. 输入应用的 **Name**（名称）。
3. 选择 **Create**（创建）。
4. 从左侧菜单选择 **Bot**（机器人）。
5. 在 **Token**（令牌）下，选择 **Reset Token**（重置令牌），生成新的机器人令牌。
6. 复制令牌，填入 n8n 凭据。
7. 在 **Bot > Privileged Gateway Intents**（机器人 > 特权网关意图）中，添加机器人需要的特权意图。更多信息，请参阅[配置机器人](https://discord.com/developers/docs/quick-start/getting-started#configuring-your-bot)。
   * n8n 建议启用 **SERVER MEMBERS INTENT**（服务器成员意图），机器人接收 GUILD\_MEMBERS 下所列事件时需要此项。
8. 在 **Installation > Installation Contexts**（安装 > 安装上下文）中，选择机器人使用的安装上下文：
   * 服务器安装的应用选择 **Guild Install**（服务器安装），这是 n8n 用户最常用的方式。
   * 用户安装的应用选择 **User Install**（用户安装），n8n 用户较少使用此方式，但测试时可能有用。
   * 这些安装上下文的更多信息，请参阅 Discord 的[选择安装上下文](https://discord.com/developers/docs/quick-start/getting-started#choosing-installation-contexts)文档。
9. 在 **Installation > Install Link**（安装 > 安装链接）中，如果尚未选中 **Discord Provided Link**（Discord 提供的链接），请选择该项。
10. 仍在 **Installation**（安装）页面，在 **Default Install Settings**（默认安装设置）部分选择 `applications.commands` 和 `bot` 作用域。更多信息，请参阅 Discord 的[作用域](https://discord.com/developers/docs/topics/oauth2#shared-resources-oauth2-scopes)文档。
11. 在 **Bot > Bot Permissions**（机器人 > 机器人权限）页面添加权限。更多信息，请参阅 Discord 的[权限](https://discord.com/developers/docs/topics/permissions)文档。n8n 建议为 [Discord](../app-nodes/n8n-nodes-base.discord/README.md) 节点选择以下权限：
    * Manage Roles（管理角色）
    * Manage Channels（管理频道）
    * Read Messages/View Channels（读取消息或查看频道）
    * Send Messages（发送消息）
    * Create Public Threads（创建公开讨论串）
    * Create Private Threads（创建私密讨论串）
    * Send Messages in Threads（在讨论串中发送消息）
    * Send TTS Messages（发送 TTS 消息）
    * Manage Messages（管理消息）
    * Manage Threads（管理讨论串）
    * Embed Links（嵌入链接）
    * Attach Files（附加文件）
    * Read Message History（读取消息历史）
    * Add Reactions（添加表情回应）
12. 将应用添加到服务器或测试服务器：
    1. 进入 **Installation > Install Link**（安装 > 安装链接），复制其中的链接。
    2. 将链接粘贴到浏览器并按回车。
    3. 在安装提示中选择 **Add to server**（添加到服务器）。
    4. 应用添加到服务器后，会显示在成员列表中。

这些步骤介绍设置 n8n 凭据所需的基本功能。创建应用的更多信息，请参阅 [Discord 创建应用指南](https://discord.com/developers/docs/quick-start/getting-started#step-1-creating-an-app)，尤其是：

* [获取凭据](https://discord.com/developers/docs/quick-start/getting-started#fetching-your-credentials)：了解如何将应用凭据放入本地开发环境。
* [处理交互](https://discord.com/developers/docs/quick-start/getting-started#step-3-handling-interactivity)：了解如何为交互式 `/slash` 命令设置公共端点。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

如需通过 OAuth2 流程将机器人添加到 Discord 服务器，请使用此方式，它可以简化用户安装应用的过程。

配置此凭据需要：

* **Client ID**（客户端 ID）
* **Client Secret**（客户端密钥）
* 选择在 **Header**（请求头）还是 **Body**（请求体）中发送 **Authentication**（身份验证信息）
* **Bot Token**（机器人令牌）

创建包含机器人的应用并生成令牌的详情，请按照上方[使用机器人](discord.md#using-bot)中的步骤操作。

然后：

1. 复制生成的 **Bot Token**（机器人令牌），填入 n8n 凭据。
2. 打开 Discord 应用的 **OAuth2** 页面，获取 **Client ID**（客户端 ID）并生成 **Client Secret**（客户端密钥），填入 n8n 凭据。
3. 从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），填入 Discord 应用的 **OAuth2 > Redirects**（OAuth2 > 重定向）。请确保保存更改。

## 使用 webhook <a href="#using-webhook" id="using-webhook"></a>

配置此凭据需要：

* **Webhook URL**：创建 webhook 后生成。

如需获取 Webhook URL，请创建 webhook，复制生成的 URL：

1. 打开 Discord 的 **Server Settings**（服务器设置），进入 **Integrations**（集成）选项卡。
2. 选择 **Create Webhook**（创建 webhook），创建新 webhook。
3. 为 webhook 设置有意义的 **Name**（名称）。
4. 选择 **Name**（名称）旁的 **avatar**（头像），编辑或上传新头像。
5. 在 **CHANNEL**（频道）下拉列表中，选择 webhook 应发送消息的频道。
6. 选择 **Copy Webhook URL**（复制 Webhook URL），将复制的 URL 填入 n8n 凭据。

更多信息，请参阅 [Discord 创建 webhook 文档](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)。

## 选择身份验证方式 <a href="#choose-an-authentication-method" id="choose-an-authentication-method"></a>

最简单的安装方式是 **webhook**。可为 Discord 服务器的单个频道创建并添加 webhook，用于向该频道发送消息，无需机器人用户或身份验证。但 webhook 无法监听或响应用户请求及命令。如果只需直接向频道发送消息，不需要交互或反馈，请使用 webhook。

**Bot**（机器人）比 webhook 提供更丰富的交互能力。可将机器人添加到 Discord 服务器（Discord API 文档中称为 `guild`）或用户账户。添加到服务器的机器人可与该服务器所有频道中的用户交互，管理频道、发送和获取消息、获取全部用户列表及更改用户角色。如需构建交互式、复杂或多步骤工作流，请使用机器人。

**OAuth2** 本质上是使用 OAuth2 流程而非仅使用机器人令牌的 **bot**（机器人）。与机器人一样，可将其添加到 Discord 服务器或用户账户。此类凭据提供与机器人相同的功能，但可以简化在服务器上安装机器人的过程。
