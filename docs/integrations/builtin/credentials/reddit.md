---
title: Reddit 凭据
description: Reddit 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Reddit 的身份验证。
contentType:
- integration
- reference
nodeTitle: Reddit 凭据
originalFilePath: integrations/builtin/credentials/reddit.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/reddit
url: https://docs.n8n.io/integrations/builtin/credentials/reddit
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Reddit 凭据 <a href="#reddit-credentials" id="reddit-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Reddit](../app-nodes/n8n-nodes-base.reddit.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Reddit](https://reddit.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Reddit 开发者文档](https://support.reddithelp.com/hc/en-us/articles/14945211791892-Developer-Platform-Accessing-Reddit-Data)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- 一个 **Client ID（客户端 ID）**
- 一个 **Client Secret（客户端密钥）**

{% hint style="warning" %}
**访问 API 需要预先批准**

Reddit 在 2025 年 11 月关闭了公共数据 API 的自助访问。现在，创建新应用前需要先获得 Reddit 的人工批准。请阅读 Reddit 的[负责任的开发者政策](https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy)，并通过 [Reddit 开发者支持表单](https://support.reddithelp.com/hc/en-us/requests/new?ticket_form_id=14868593862164)提交申请。
{% endhint %}

获批后，创建[第三方应用](https://www.reddit.com/prefs/apps)。可访问该链接，或进入 **profile > Settings > Privacy > Third-party app authorizations > are you a developer? create an app**（个人资料 > 设置 > 隐私 > 第三方应用授权 > 开发者创建应用入口），并采用以下设置：

- 从 n8n 复制 **OAuth Callback URL**（OAuth 回调 URL），用作应用的 **redirect uri**。
- 应用的客户端 ID 显示在应用名称下方。复制后填入 n8n 的 **Client ID**。
- 复制应用的 **secret**，填入 n8n 的 **Client Secret**。

