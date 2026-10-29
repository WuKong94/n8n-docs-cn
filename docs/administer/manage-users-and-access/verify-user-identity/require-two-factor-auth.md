---
description: 如何为 n8n 账号启用 2FA。
contentType: howto
nodeTitle: 要求双因素身份验证
originalFilePath: user-management/two-factor-auth.md
originalUrl: https://docs.n8n.io/user-management/two-factor-auth
url: https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/require-two-factor-auth
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 双因素身份验证（2FA） <a href="#two-factor-authentication-2fa" id="two-factor-authentication-2fa"></a>

双因素身份验证（2FA）在用户名和密码的基础上增加第二种身份验证方式，以提高账号安全性。n8n 支持使用身份验证器应用进行 2FA。

## 启用 2FA <a href="#enable-2fa" id="enable-2fa"></a>

你需要在手机上安装身份验证器应用。

在 n8n 中启用 2FA：

1. 前往 **Settings**（设置）> **Personal**（个人）。
2. 选择 **Enable 2FA**（启用 2FA）。n8n 会打开包含二维码的弹窗。
3. 使用身份验证器应用扫描二维码。
4. 在 **Code from authenticator app**（身份验证器应用中的验证码）中输入应用生成的验证码。
5. 选择 **Continue**（继续）。n8n 会显示恢复码。
6. 保存恢复码。如果丢失身份验证器，你需要使用这些恢复码重新访问账号。

## 为实例禁用 2FA <a href="#disable-2fa-for-your-instance" id="disable-2fa-for-your-instance"></a>

自托管用户可以将 `N8N_MFA_ENABLED` 设为 false，在 n8n 实例中为所有用户禁用 2FA。注意，如果已有用户启用 2FA，n8n 会忽略此设置。使用环境变量配置 n8n 实例的更多信息，请参阅[配置方法](../../../deploy/host-n8n/configure-n8n/basic-configuration.md)。

## 相关资源 <a id="related-resources"></a>

* [验证用户身份](./)
* [连接 LDAP](connect-ldap.md)
* [使用 SAML](use-saml/README.md)
* [使用 OIDC](use-oidc/README.md)
