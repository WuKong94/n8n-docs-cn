---
title: Bearer 身份验证
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

## 使用 Bearer 身份验证 <a href="#using-bearer-auth" id="using-bearer-auth"></a>

如果应用或服务支持 Bearer 身份验证，可以使用此通用身份验证方式。此方式本质上是请求头身份验证，其中 `Name` 设为 `Authorization`，`Value` 设为 `Bearer <token>`。

配置此凭据时，请输入：

- 需要传递给 HTTP 请求目标应用或服务的 **Bearer Token（Bearer 令牌）**

阅读更多关于 [Bearer 身份验证](https://swagger.io/docs/specification/v3_0/authentication/bearer-authentication/)的说明。
