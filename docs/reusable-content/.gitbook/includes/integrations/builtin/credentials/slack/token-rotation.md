---
title: Slack 令牌轮换
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

Slack 提供 **token rotation（令牌轮换）** 功能，可以为机器人和用户令牌启用。启用后，每个令牌都会在 12 小时后过期。这在测试时可能有用，但 n8n 中使用此类令牌的凭据会在令牌过期后失效。如果要在生产环境中使用 Slack 凭据，必须**关闭**此功能。

检查 Slack 应用是否已启用令牌轮换的方法，请参阅 [Slack API 文档：令牌轮换](https://api.slack.com/authentication/rotation)。

{% hint style="info" %}
**如果应用已使用令牌轮换**

请注意，Slack 应用一旦启用令牌轮换，就无法再次关闭。需要另行创建一个禁用令牌轮换的新 Slack 应用。
{% endhint %}
