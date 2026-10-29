---
title: Webex by Cisco 凭据
description: Webex by Cisco 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Webex by Cisco 的身份验证。
contentType:
- integration
- reference
nodeTitle: Webex by Cisco 凭据
originalFilePath: integrations/builtin/credentials/ciscowebex.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/ciscowebex
url: https://docs.n8n.io/integrations/builtin/credentials/ciscowebex
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Webex by Cisco 凭据 <a href="#webex-by-cisco-credentials" id="webex-by-cisco-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Webex by Cisco](../app-nodes/n8n-nodes-base.ciscowebex.md)
- [Webex by Cisco Trigger（触发器）](../trigger-nodes/n8n-nodes-base.ciscowebextrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Webex by Cisco](https://www.webex.com/) 账户，通常会自动获得[开发者账户访问权限](https://developer.webex.com)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Webex API 文档](https://developer.webex.com/docs/getting-started)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% hint style="info" %}
**n8n Cloud 用户须知**

只需输入凭据名称，并在 OAuth 凭据中选择 **Connect my account**（连接我的账户）按钮，即可将 Webex by Cisco 账户连接到 n8n。
{% endhint %}

如果需要从头配置 OAuth2，必须先创建集成才能使用此凭据。请按照 [Webex 注册集成文档](https://developer.webex.com/docs/integrations#registering-your-integration)开始设置。

n8n 建议为集成使用以下 **Scopes**（作用域）：

* `spark:rooms_read`
* `spark:messages_write`
* `spark:messages_read`
* `spark:memberships_read`
* `spark:memberships_write`
* `meeting:recordings_write`
* `meeting:recordings_read`
* `meeting:preferences_read`
* `meeting:schedules_write`
* `meeting:schedules_read`
