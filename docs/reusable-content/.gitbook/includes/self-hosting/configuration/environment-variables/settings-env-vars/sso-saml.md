---
title: SSO 的 SAML 配置
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_SSO_SAML_LOGIN_ENABLED` | Boolean | `false` | 是否启用 SAML 登录。 |
| `N8N_SSO_SAML_METADATA` | String | - | 以 XML 字符串提供的 SAML 身份提供商元数据。与 `N8N_SSO_SAML_METADATA_URL` 互斥，不要同时设置。 |
| `N8N_SSO_SAML_METADATA_URL` | String | - | 用于获取 SAML 身份提供商元数据的 URL。与 `N8N_SSO_SAML_METADATA` 互斥，不要同时设置。 |
