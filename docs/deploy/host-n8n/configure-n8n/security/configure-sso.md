---
title: 设置单点登录（SSO）
description: 为自托管 n8n 实例设置 SAML 或 OIDC 单点登录。
contentType: howto
nodeTitle: 配置 SSO
originalFilePath: hosting/securing/set-up-sso.md
originalUrl: https://docs.n8n.io/hosting/securing/set-up-sso
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/configure-sso
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 设置单点登录（SSO） <a href="#set-up-single-sign-on-sso" id="set-up-single-sign-on-sso"></a>

{% hint style="info" %}
**功能可用范围**

单点登录可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**商业版、企业版。

需要实例所有者或管理员身份，才能启用和配置 SAML 或 OIDC。
{% endhint %}

n8n 支持通过 SAML 和 OIDC 协议实现单点登录（SSO）。两种协议的一般介绍、区别及各自优势，请参阅 [OIDC 与 SAML 对比](https://www.onelogin.com/learn/oidc-vs-saml)。

* [设置 SAML](../../../../administer/manage-users-and-access/verify-user-identity/use-saml/set-up-saml.md)：在 n8n 中设置 SAML 的通用指南，以及常见身份提供商（IdP）的相关资源。
* [设置 OIDC](../../../../administer/manage-users-and-access/verify-user-identity/use-oidc/set-up-oidc.md)：在 n8n 中设置 OpenID Connect（OIDC）SSO 的通用指南。

## 通过环境变量配置 SSO <a href="#configure-sso-with-environment-variables" id="configure-sso-with-environment-variables"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.18.0 起，支持通过环境变量配置 SSO。
{% endhint %}

也可以通过环境变量配置 SSO，而非通过界面。完整变量列表请参阅 [SSO 环境变量](../basic-configuration/use-environment-variables/sso.md)，启用机制请参阅[通过环境变量管理实例设置](../manage-settings-using-environment-variables.md)。

## 相关资源 <a id="related-resources"></a>

* [安全](../security.md)
