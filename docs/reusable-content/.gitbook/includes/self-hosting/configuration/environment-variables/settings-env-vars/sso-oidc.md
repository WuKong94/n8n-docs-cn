---
title: SSO 的 OIDC 配置
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_SSO_OIDC_LOGIN_ENABLED` | Boolean | `false` | 是否启用 OIDC 登录。 |
| `N8N_SSO_OIDC_CLIENT_ID` | String | - | 身份提供商签发的 OIDC 客户端 ID。 |
| `N8N_SSO_OIDC_CLIENT_SECRET` | String | - | 身份提供商签发的 OIDC 客户端密钥。 |
| `N8N_SSO_OIDC_DISCOVERY_ENDPOINT` | String | - | OIDC 发现端点 URL，即身份提供商的 `.well-known/openid-configuration` URL。 |
| `N8N_SSO_OIDC_PROMPT` | String | - | 可选的 OIDC `prompt` 参数，随授权请求发送，例如 `login` 或 `consent`。 |
| `N8N_SSO_OIDC_ACR_VALUES` | String | - | 可选的 OIDC `acr_values` 参数，用于请求特定身份验证上下文，例如需要升级验证的 MFA 流程。 |
