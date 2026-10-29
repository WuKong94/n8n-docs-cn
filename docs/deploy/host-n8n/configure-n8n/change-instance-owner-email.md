---
title: 更改自托管 n8n 的实例所有者邮箱
description: 通过界面或环境变量，更改自托管 n8n 实例的所有者邮箱地址。
contentType: howto
nodeTitle: 更改实例所有者的邮箱
originalFilePath: hosting/configuration/change-instance-owner-email.md
originalUrl: https://docs.n8n.io/hosting/configuration/change-instance-owner-email
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/change-instance-owner-email
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 更改自托管 n8n 的实例所有者邮箱 <a href="#change-the-instance-owner-email-for-self-hosted-n8n" id="change-the-instance-owner-email-for-self-hosted-n8n"></a>

可以通过界面更改实例所有者邮箱；如果通过环境变量管理实例所有者，也可以使用环境变量更改。

{% hint style="info" %}
**所有者邮箱必须唯一**

所有者邮箱不能已被实例中的其他用户使用。如果目标邮箱已属于其他用户，请先更改或删除该用户，释放邮箱。
{% endhint %}

更改邮箱会更新现有实例所有者账号，不会将所有权转移给其他现有用户，也不会合并用户账号。

## 通过界面更改所有者邮箱 <a href="#change-the-owner-email-in-the-ui" id="change-the-owner-email-in-the-ui"></a>

1. 以实例所有者身份登录。
2. 进入 **Settings（设置）** > **Personal（个人）**。
3. 更新 **Email（电子邮件）**字段。
4. 选择 **Save（保存）**。

## 通过环境变量更改所有者邮箱 <a href="#change-the-owner-email-using-environment-variables" id="change-the-owner-email-using-environment-variables"></a>

如果通过环境变量管理实例所有者：

1. 将 `N8N_INSTANCE_OWNER_MANAGED_BY_ENV` 设为 `true`。
2. 将 `N8N_INSTANCE_OWNER_EMAIL` 设为新的所有者邮箱。
3. 保持 `N8N_INSTANCE_OWNER_FIRST_NAME`、`N8N_INSTANCE_OWNER_LAST_NAME` 和 `N8N_INSTANCE_OWNER_PASSWORD_HASH` 已设置。
4. 重启 n8n。

当 `N8N_INSTANCE_OWNER_MANAGED_BY_ENV` 为 `true` 时，n8n 会在每次启动时重新应用所有者信息，对应的界面控件将变为只读。

{% hint style="warning" %}
**`N8N_INSTANCE_OWNER_PASSWORD_HASH` 必须为 bcrypt 哈希值**

此变量要求提供预先生成的 bcrypt 哈希值。设置明文密码会导致无法登录。
{% endhint %}

更多信息请参阅[通过环境变量管理实例设置](manage-settings-using-environment-variables.md#instance-owner)。

## 相关资源 <a id="related-resources"></a>

* [配置 n8n](./)
