---
title: 排查 SAML SSO 问题
description: 遇到 SAML 问题时需要检查的事项。
contentType: howto
nodeTitle: 排查 SAML 问题
originalFilePath: user-management/saml/troubleshooting.md
originalUrl: https://docs.n8n.io/user-management/saml/troubleshooting
url: https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/troubleshoot-saml
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 排查 SAML SSO 问题 <a href="#troubleshooting-saml-sso" id="troubleshooting-saml-sso"></a>

如果测试 SAML 设置时报错，请检查：

* 在 IdP 中创建的应用是否支持 SAML？
* 是否在 IdP 的正确字段中填写了 n8n 重定向 URL 和实体 ID？
* 元数据 XML 是否正确？检查复制到 n8n 中的元数据格式是否正确。

如需更多支持，请访问[论坛](https://community.n8n.io/)；如果购买了付费支持方案，也可以联系支持代表。

## 通过 SAML 登录后，用户进入了同一个账号 <a id="users-land-in-the-same-account-after-saml-login"></a>

n8n 通过 `userPrincipalName`（`upn`）声明，将每个 SAML 身份关联到 n8n 账号。如果 IdP 为多个人发送相同的值，他们就会登录到同一个账号。请为每个用户提供不同的值。属性映射方法请参阅[设置 SAML](set-up-saml.md)。

如果 SAML 登录匹配到已有用户，但该用户邮箱与断言中的邮箱不同，n8n 会发出 `n8n.audit.user.login.emailConflict` 审计事件。将其流式发送到日志系统，便可发现这种情况。请参阅[日志流](../../../observe-and-log/stream-logs-to-external-systems.md#events)。

## 相关资源 <a id="related-resources"></a>

* [使用 SAML](./)
* [设置 SAML](set-up-saml.md)
* [设置 Okta Workforce Identity SAML](set-up-okta-workforce-identity-saml.md)
* [设置 Azure AD SAML](set-up-azure-ad-saml.md)
* [启用 SAML 时管理用户](manage-users-with-saml.md)
