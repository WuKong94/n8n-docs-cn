---
title: 未经 Google 验证的应用
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

使用 OAuth 身份验证方式时，可能会看到 **Google hasn't verified this app（Google 尚未验证此应用）** 警告。避免此警告的方法如下：

- 如果应用的 **User Type（用户类型）** 为 **Internal（内部）**，请使用要进行身份验证的同一个账号创建 OAuth 凭据。\
- 如果应用的 **User Type（用户类型）** 为 **External（外部）**，可以将邮箱地址添加到应用的测试人员列表中：进入 [**Audience（受众）**](https://console.cloud.google.com/auth/audience) 页面，将用于登录的邮箱添加至 **Test users（测试用户）** 列表。

如果需要使用其他账号（开发者或其他第三方）生成的凭据，请按照 [Google Cloud 文档中的授权错误：Google 尚未验证此应用](https://developers.google.com/nest/device-access/reference/errors/authorization#google_hasnt_verified_this_app)说明操作。
