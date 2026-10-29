---
title: SSO 的启用
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_SSO_MANAGED_BY_ENV` | Boolean | `false` | 设为 `true`，通过环境变量管理 SSO。当值为 `true` 时，n8n 会在每次启动时应用 SSO 变量，并锁定对应的界面控件。 |
| `N8N_SSO_USER_ROLE_PROVISIONING` | 枚举字符串：`disabled`、`instance_role`、`instance_and_project_roles` | `disabled` | n8n 为通过 SSO 登录的用户配置角色的方式。`disabled` 不配置任何角色；`instance_role` 仅配置实例级角色；`instance_and_project_roles` 同时配置实例角色和项目角色。 |
