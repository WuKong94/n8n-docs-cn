---
title: 启用 SAML 时管理用户
description: 启用 SAML 后如何管理用户及其登录。
contentType: howto
nodeTitle: 启用 SAML 时管理用户
originalFilePath: user-management/saml/managing.md
originalUrl: https://docs.n8n.io/user-management/saml/managing
url: https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/manage-users-with-saml
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 启用 SAML 时管理用户 <a href="#manage-users-with-saml" id="manage-users-with-saml"></a>

{% include "../../../../reusable-content/.gitbook/includes/user-management/sso-saml-availability.md" %}

SAML 会影响一些用户管理任务。

## 允许用户不使用 SAML 登录 <a href="#exempt-users-from-saml" id="exempt-users-from-saml"></a>

你可以允许用户不通过 SAML 登录，操作如下：

1. 前往 **Settings**（设置）> **Users**（用户）。
2. 选择要豁免 SAML 登录的用户旁边的菜单图标。
3. 选择 **Allow Manual Login**（允许手动登录）。

## 删除用户 <a href="#deleting-users" id="deleting-users"></a>

从 IdP 移除用户后，该用户在 n8n 中仍保持登录。你还需要手动从 n8n 中移除该用户。删除用户的方法请参阅[管理用户](../../add-and-remove-users.md)。

## 相关资源 <a id="related-resources"></a>

* [使用 SAML](./)
* [设置 SAML](set-up-saml.md)
* [设置 Okta Workforce Identity SAML](set-up-okta-workforce-identity-saml.md)
* [设置 Azure AD SAML](set-up-azure-ad-saml.md)
* [排查 SAML 问题](troubleshoot-saml.md)
