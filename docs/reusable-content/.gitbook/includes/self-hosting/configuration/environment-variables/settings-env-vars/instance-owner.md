---
title: 实例所有者
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_INSTANCE_OWNER_MANAGED_BY_ENV` | Boolean | `false` | 设为 `true`，通过环境变量管理实例所有者。当值为 `true` 时，n8n 会在每次启动时覆盖下方的实例所有者信息，锁定该用户的界面控件，并拒绝通过 API 修改。 |
| `N8N_INSTANCE_OWNER_EMAIL` | String | - | 实例所有者的电子邮件地址。 |
| `N8N_INSTANCE_OWNER_FIRST_NAME` | String | - | 实例所有者的名。 |
| `N8N_INSTANCE_OWNER_LAST_NAME` | String | - | 实例所有者的姓。 |
| `N8N_INSTANCE_OWNER_PASSWORD_HASH` | String | - | 实例所有者密码的 bcrypt 哈希值。设置明文密码会导致无法登录。 |

{% hint style="warning" %}
**所有者邮箱必须唯一**

`N8N_INSTANCE_OWNER_EMAIL` 不能已属于实例中的其他用户。此设置更新现有实例所有者账号，不会将所有权转移给其他现有用户，也不会合并账号。要使用已属于其他用户的邮箱，请先更改或删除该用户，释放邮箱。
{% endhint %}
