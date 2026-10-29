---
title: SSO 环境变量
description: 通过环境变量配置自托管 n8n 的单点登录。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: SSO
originalFilePath: hosting/configuration/environment-variables/sso.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/sso
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# SSO 环境变量 <a href="#sso-environment-variables" id="sso-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

{% hint style="info" %}
**功能可用范围**

单点登录可用于：

- **自托管：**商业版、企业版。

n8n Cloud Enterprise 也支持单点登录，但不通过本页的环境变量配置。
{% endhint %}

应用内设置步骤及身份提供商指南请参阅[设置 SSO](../../security/configure-sso.md)。启用机制请参阅[通过环境变量管理实例设置](../../manage-settings-using-environment-variables.md)。

## 启用与共享设置 <a href="#activation-and-shared-settings" id="activation-and-shared-settings"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/sso-activation.md" %}

## OIDC <a href="#oidc" id="oidc"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/sso-oidc.md" %}

## SAML <a href="#saml" id="saml"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/sso-saml.md" %}

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
