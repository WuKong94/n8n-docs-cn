---
title: 用户管理 SMTP 与双因素身份验证环境变量
description: 设置用户管理和邮件的环境变量。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 用户管理与 2FA
originalFilePath: hosting/configuration/environment-variables/user-management-smtp-2fa.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/user-management-smtp-2fa
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/user-management-and-2fa
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 用户管理 SMTP 与双因素身份验证环境变量 <a href="#user-management-smtp-and-two-factor-authentication-environment-variables" id="user-management-smtp-and-two-factor-authentication-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

用户管理及邮件设置的更多信息请参阅[用户管理](../../user-management.md)。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_EMAIL_MODE` | String | `smtp` | 启用邮件。 |
| `N8N_SMTP_HOST` | String | - | _SMTP 服务器名称_。 |
| `N8N_SMTP_PORT` | Number | - | _SMTP 服务器端口_。 |
| `N8N_SMTP_USER` | String | - | _SMTP 用户名_。 |
| `N8N_SMTP_PASS` | String | - | _SMTP 密码_。 |
| `N8N_SMTP_OAUTH_SERVICE_CLIENT` | String | - | 通过服务账号使用 2LO 时，填写客户端 ID。 |
| `N8N_SMTP_OAUTH_PRIVATE_KEY` | String | - | 通过服务账号使用 2LO 时，填写私钥。 |
| `N8N_SMTP_SENDER` | String | - | 发件人邮箱地址，可以包含发件人名称。带名称的示例：_n8n `<contact@n8n.com>`_。 |
| `N8N_SMTP_SSL` | Boolean | `true` | 是否对 SMTP 使用 SSL，true 表示使用，false 表示不使用。 |
| `N8N_SMTP_STARTTLS` | Boolean | `true` | 是否对 SMTP 使用 STARTTLS，true 表示使用，false 表示不使用。 |
| `N8N_UM_EMAIL_TEMPLATES_INVITE` | String | - | HTML 邮件模板的完整路径，用于覆盖邀请邮件的默认模板。 |
| `N8N_UM_EMAIL_TEMPLATES_PWRESET` | String | - | HTML 邮件模板的完整路径，用于覆盖密码重置邮件的默认模板。 |
| `N8N_UM_EMAIL_TEMPLATES_WORKFLOW_SHARED` | String | - | 覆盖通知用户工作流已共享的默认 HTML 模板。提供模板的完整路径。 |
| `N8N_UM_EMAIL_TEMPLATES_CREDENTIALS_SHARED` | String | - | 覆盖通知用户凭据已共享的默认 HTML 模板。提供模板的完整路径。 |
| `N8N_UM_EMAIL_TEMPLATES_PROJECT_SHARED` | String | - | 覆盖通知用户项目已共享的默认 HTML 模板。提供模板的完整路径。 |
| `N8N_USER_MANAGEMENT_JWT_SECRET` | String | - | 设置指定的 JWT 密钥。默认由 n8n 在启动时生成。 |
| `N8N_USER_MANAGEMENT_JWT_DURATION_HOURS` | Number | 168 | JWT 的有效期，单位为小时。 |
| `N8N_USER_MANAGEMENT_JWT_REFRESH_TIMEOUT_HOURS` | Number | 0 | JWT 到期前多少小时自动刷新。0 表示 `N8N_USER_MANAGEMENT_JWT_DURATION_HOURS` 的 25%；-1 表示从不刷新，用户必须在 `N8N_USER_MANAGEMENT_JWT_DURATION_HOURS` 指定的时长后重新登录。 |
| `N8N_MFA_ENABLED` | Boolean | `true` | 是否启用双因素身份验证，true 表示启用，false 表示禁用。如果现有用户已经启用 2FA，n8n 会忽略此设置。 |
| `N8N_INVITE_LINKS_EMAIL_ONLY` | Boolean | `false` | 设为 true 时，n8n 只通过邮件发送邀请链接，不通过 API 暴露，避免程序或高权限用户获取邀请 URL，以提高安全性。 |


## 通过环境变量管理实例所有者 <a href="#instance-owner-using-environment-variables" id="instance-owner-using-environment-variables"></a>

将 `N8N_INSTANCE_OWNER_MANAGED_BY_ENV` 设为 `true`，通过环境变量预配置实例所有者。启用机制请参阅[通过环境变量管理实例设置](../../manage-settings-using-environment-variables.md)。

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/instance-owner.md" %}

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
