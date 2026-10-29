---
description: 为自托管 n8n 配置用户管理。
contentType: howto
nodeTitle: 用户管理
originalFilePath: hosting/configuration/user-management-self-hosted.md
originalUrl: https://docs.n8n.io/hosting/configuration/user-management-self-hosted
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/user-management
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 为自托管 n8n 配置用户管理 <a href="#configure-self-hosted-n8n-for-user-management" id="configure-self-hosted-n8n-for-user-management"></a>

通过 n8n 用户管理，可以邀请其他人在你的 n8n 实例中工作。

本页介绍如何为实例配置用户管理，以及如何开始邀请用户。

更多使用说明请参阅主要的[用户管理](../../../administer/manage-users-and-access/README.md)指南，包括：

* [管理用户](../../../administer/manage-users-and-access/add-and-remove-users.md)
* [实例角色](../../../administer/manage-users-and-access/understand-instance-roles.md)
* [最佳实践](../../../administer/manage-users-and-access/follow-best-practices.md)

LDAP 设置说明请参阅 [LDAP](../../../administer/manage-users-and-access/verify-user-identity/connect-ldap.md)。

SAML 设置说明请参阅 [SAML](../../../administer/manage-users-and-access/verify-user-identity/use-saml/README.md)。

{% hint style="warning" %}
**功能可用范围**

自 n8n 1.0 起，已移除对基本身份验证和 JWT 身份验证的支持。

`N8N_USER_MANAGEMENT_DISABLED` 环境变量也已在 n8n 1.0 中移除。近期版本没有受支持的方式可以禁用登录页面，包括本地或开发环境。如需简化本地开发登录，可以使用密码管理器、设置简单的本地密码，或通过脚本执行标准登录流程。
{% endhint %}

## 设置 <a href="#setup" id="setup"></a>

在 n8n 中设置用户管理分为三个阶段：

1. 配置 n8n 实例使用 SMTP 服务器。
2. 启动 n8n，完成应用内设置。
3. 邀请用户。

### 第一步：SMTP <a href="#step-one-smtp" id="step-one-smtp"></a>

n8n 建议设置 SMTP 服务器，用于发送用户邀请和重置密码。

{% hint style="info" %}
**功能可用范围**

自 n8n 0.210.1 起，SMTP 为可选配置。可以不设置 SMTP，改为手动复制并发送邀请链接。但跳过此步骤后，用户将无法重置密码。
{% endhint %}
从 SMTP 提供商获取以下信息：

* 服务器名称。
* SMTP 用户名。
* SMTP 密码。
* SMTP 发件人名称。

要为 n8n 设置 SMTP，请配置实例的 SMTP 环境变量。环境变量设置方法请参阅[配置](basic-configuration.md)。

| 变量 | 类型 | 说明 | 是否必需 |
| -------- | ---- | ----------- | --------- |
| `N8N_EMAIL_MODE` | string | `smtp` | 必需 |
| `N8N_SMTP_HOST` | string | _SMTP 服务器名称_ | 必需 |
| `N8N_SMTP_PORT` | number | _SMTP 服务器端口_，默认为 `465`。 | 可选 |
| `N8N_SMTP_USER` | string | _SMTP 用户名_ | 可选 |
| `N8N_SMTP_PASS` | string | _SMTP 密码_ | 可选 |
| `N8N_SMTP_OAUTH_SERVICE_CLIENT` | string | _OAuth 服务客户端_ | 可选 |
| `N8N_SMTP_OAUTH_PRIVATE_KEY` | string | _OAuth 私钥_ | 可选 |
| `N8N_SMTP_SENDER` | string | 发件人邮箱地址，可包含发件人名称。带名称的示例：_n8n `<contact@n8n.com>`_ | 必需 |
| `N8N_SMTP_SSL` | boolean | 是否对 SMTP 使用 SSL，true 表示使用，false 表示不使用。默认为 `true`。 | 可选 |
| `N8N_UM_EMAIL_TEMPLATES_INVITE` | string | HTML 邮件模板的完整路径，用于覆盖邀请邮件的默认模板。 | 可选 |
| `N8N_UM_EMAIL_TEMPLATES_PWRESET` | string | HTML 邮件模板的完整路径，用于覆盖密码重置邮件的默认模板。 | 可选 |
| `N8N_UM_EMAIL_TEMPLATES_WORKFLOW_SHARED` | String | 覆盖通知用户工作流已共享的默认 HTML 模板。提供模板的完整路径。 | 可选 |
| `N8N_UM_EMAIL_TEMPLATES_CREDENTIALS_SHARED` | String | 覆盖通知用户凭据已共享的默认 HTML 模板。提供模板的完整路径。 | 可选 |
| `N8N_UM_EMAIL_TEMPLATES_PROJECT_SHARED` | String | 覆盖通知用户项目已共享的默认 HTML 模板。提供模板的完整路径。 | 可选 |


如果 n8n 实例已经运行，需要重启才能启用新的 SMTP 设置。

{% hint style="info" %}
**更多配置选项**

还有更多可通过环境变量设置的配置选项，清单请参阅[环境变量](basic-configuration/use-environment-variables/README.md)。例如，如果不希望用户看到标签、工作流模板或个性化调查，可以禁用这些功能。
{% endhint %}

{% hint style="info" %}
**初次接触 SMTP？**

如果不熟悉 SMTP，可以阅读 [SendGrid 的这篇博客](https://sendgrid.com/blog/what-is-an-smtp-server/)，了解简要介绍；[维基百科的简单邮件传输协议文章](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)提供了更详细的技术背景。
{% endhint %}

### 第二步：应用内设置 <a href="#step-two-in-app-setup" id="step-two-in-app-setup"></a>

{% include "../../../reusable-content/.gitbook/includes/user-management/in-app-setup.md" %}

#### 通过环境变量预配置实例所有者 <a href="#pre-provision-the-instance-owner-from-environment-variables" id="pre-provision-the-instance-owner-from-environment-variables"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.17.0 起，支持通过环境变量预配置实例所有者。
{% endhint %}

可以通过环境变量预配置实例所有者，无需完成应用内设置。将 `N8N_INSTANCE_OWNER_MANAGED_BY_ENV` 设为 `true`，并提供所有者信息。启用机制请参阅[通过环境变量管理实例设置](manage-settings-using-environment-variables.md)。

设置后如需更改所有者邮箱，请参阅[更改自托管 n8n 的实例所有者邮箱](change-instance-owner-email.md)。

{% hint style="warning" %}
**`N8N_INSTANCE_OWNER_PASSWORD_HASH` 必须为 bcrypt 哈希值**

此变量要求提供预先生成的 bcrypt 哈希值。设置明文密码会导致无法登录。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/instance-owner.md" %}

### 第三步：邀请用户 <a href="#step-three-invite-users" id="step-three-invite-users"></a>

{% include "../../../reusable-content/.gitbook/includes/user-management/invite-users.md" %}

## 相关资源 <a id="related-resources"></a>

* [配置 n8n](./)
