---
title: 安全策略
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_SECURITY_POLICY_MANAGED_BY_ENV` | Boolean | `false` | 设为 `true`，通过环境变量管理安全策略。当值为 `true` 时，n8n 会在每次启动时应用安全策略变量，并锁定对应的界面控件。 |
| `N8N_MFA_ENFORCED_ENABLED` | Boolean | `false` | 是否强制所有用户使用双因素身份验证：`true` 表示强制，`false` 表示不强制。 |
| `N8N_PERSONAL_SPACE_PUBLISHING_ENABLED` | Boolean | `true` | 是否允许用户从个人空间发布：`true` 表示允许，`false` 表示不允许。 |
| `N8N_PERSONAL_SPACE_SHARING_ENABLED` | Boolean | `true` | 是否允许用户从个人空间共享资源：`true` 表示允许，`false` 表示不允许。 |
