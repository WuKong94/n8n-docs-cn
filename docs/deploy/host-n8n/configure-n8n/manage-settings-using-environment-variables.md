---
title: 通过环境变量管理实例设置
description: 通过环境变量配置自托管 n8n 的实例所有者、SSO、安全策略、日志流、MCP 和社区节点包。
contentType: overview
nodeTitle: 通过环境变量管理设置
originalFilePath: hosting/configuration/settings-env-vars.md
originalUrl: https://docs.n8n.io/hosting/configuration/settings-env-vars
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 通过环境变量管理实例设置 <a href="#manage-instance-settings-using-environment-variables" id="manage-instance-settings-using-environment-variables"></a>

可以通过环境变量管理部分实例设置，无需在界面中配置。自动创建 n8n 实例时，例如通过内部部署流水线，这种方式很有用。

每个支持的配置领域都有一个名为 `<AREA>_MANAGED_BY_ENV` 的专用环境变量。将其设为 `true`，即可启用该领域的环境变量管理。之后，n8n 会应用相关环境变量，并锁定对应的界面控件。

## 工作原理 <a href="#how-it-works" id="how-it-works"></a>

将 `<AREA>_MANAGED_BY_ENV` 设为 `true` 后：

* n8n 会在**每次启动时**重新应用环境变量中的设置。
* 对应的界面控件变为**只读**。

当 `<AREA>_MANAGED_BY_ENV` 为 `false`，即默认值时，即使设置了相关环境变量，n8n 也会忽略它们。

{% hint style="info" %}
**关闭 `*_MANAGED_BY_ENV` 后仍会保留原值**

将 `*_MANAGED_BY_ENV` 改回 `false`，会恢复界面的修改权限，但保留最后一次应用的值。之后如需修改，请通过界面编辑。
{% endhint %}

{% hint style="info" %}
**界面控件意外变为只读**

如果某项设置意外显示为只读，请检查环境中对应的 `*_MANAGED_BY_ENV` 变量是否为 `true`。
{% endhint %}

支持的配置领域及启用变量如下：

* 实例所有者：`N8N_INSTANCE_OWNER_MANAGED_BY_ENV`
* SSO：`N8N_SSO_MANAGED_BY_ENV`
* 安全策略：`N8N_SECURITY_POLICY_MANAGED_BY_ENV`
* 日志流：`N8N_LOG_STREAMING_MANAGED_BY_ENV`
* MCP：`N8N_MCP_MANAGED_BY_ENV`
* 社区节点包：`N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV`

{% hint style="info" %}
**设置 `<AREA>_MANAGED_BY_ENV` 以启用该组配置**

只有 `<AREA>_MANAGED_BY_ENV` 为 `true`，该领域的其他环境变量才会生效。将其设为 `true` 以启用该组配置。
{% endhint %}

## 实例所有者 <a href="#instance-owner" id="instance-owner"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.17.0 起，支持通过环境变量管理实例所有者。
{% endhint %}

通过环境变量预配置[实例所有者](user-management.md)，无需在应用内完成设置。设置后如需更改所有者邮箱，请参阅[更改自托管 n8n 的实例所有者邮箱](change-instance-owner-email.md)。

{% hint style="warning" %}
**`N8N_INSTANCE_OWNER_PASSWORD_HASH` 必须为 bcrypt 哈希值**

此变量要求提供预先生成的 bcrypt 哈希值。设置明文密码会导致无法登录。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/instance-owner.md" %}

## SSO <a href="#sso" id="sso"></a>

{% hint style="info" %}
**功能可用范围**

单点登录可用于：

- **自托管：**商业版、企业版。

n8n Cloud Enterprise 也支持单点登录，但不通过本页的环境变量配置。

自 n8n 2.18.0 起，支持通过环境变量管理 SSO。
{% endhint %}

通过环境变量配置[单点登录](security/configure-sso.md)。

### 启用与共享设置 <a href="#activation-and-shared-settings" id="activation-and-shared-settings"></a>

{% include "../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/sso-activation.md" %}

### OIDC <a href="#oidc" id="oidc"></a>

{% include "../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/sso-oidc.md" %}

### SAML <a href="#saml" id="saml"></a>

{% hint style="warning" %}
**SAML 元数据变量互斥**

设置 `N8N_SSO_SAML_METADATA`（直接提供 XML）或 `N8N_SSO_SAML_METADATA_URL`（URL）中的一个，不要同时设置。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/sso-saml.md" %}

## 安全策略 <a href="#security-policy" id="security-policy"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.18.0 起，支持通过环境变量管理安全策略。
{% endhint %}

通过环境变量管理实例安全策略，包括强制多因素身份验证（MFA）和个人空间限制。

{% include "../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/security-policy.md" %}

## 日志流 <a href="#log-streaming" id="log-streaming"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.19.0 起，支持通过环境变量管理日志流。
{% endhint %}

通过环境变量管理[日志流](../../../administer/observe-and-log/stream-logs-to-external-systems.md)的目标。各类目标的 JSON 结构请参阅[通过环境变量配置](../../../administer/observe-and-log/stream-logs-to-external-systems.md#configure-using-environment-variables)。

{% include "../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/log-streaming.md" %}

## MCP <a href="#mcp" id="mcp"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.20.0 起，支持通过环境变量管理实例级 MCP 访问。
{% endhint %}

通过环境变量管理[实例级 MCP 访问](../../../connect/connect-to-n8n-mcp-server.md)。

{% include "../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/mcp.md" %}

## 社区节点包 <a href="#community-packages" id="community-packages"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.21.0 起，支持通过环境变量管理已安装的社区节点包。
{% endhint %}

通过环境变量管理已安装的[社区节点包](../../../integrations/community-nodes/installation-and-management/README.md)集合。n8n 会在每次启动时，根据列表校正已安装的包。受管理的包无法通过界面卸载或更新。

`N8N_COMMUNITY_PACKAGES_ENABLED` 也必须设为 `true`，即默认值。禁用社区节点包时，n8n 会忽略 `N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV` 并记录警告。

{% include "../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/community-packages.md" %}

## 综合示例 <a href="#combined-example" id="combined-example"></a>

以下示例将六个领域全部设置为通过环境变量管理：创建实例所有者、配置 OIDC SSO、强制启用 MFA、注册一个 Webhook 日志流目标、启用 MCP 访问，以及管理一个社区节点包。

```bash
# Instance owner <a href="#instance-owner" id="instance-owner"></a>
export N8N_INSTANCE_OWNER_MANAGED_BY_ENV=true
export N8N_INSTANCE_OWNER_EMAIL=<owner-email>
export N8N_INSTANCE_OWNER_FIRST_NAME=<first-name>
export N8N_INSTANCE_OWNER_LAST_NAME=<last-name>
export N8N_INSTANCE_OWNER_PASSWORD_HASH=<bcrypt-hash>

# SSO using OIDC <a href="#sso-using-oidc" id="sso-using-oidc"></a>
export N8N_SSO_MANAGED_BY_ENV=true
export N8N_SSO_USER_ROLE_PROVISIONING=instance_role
export N8N_SSO_OIDC_LOGIN_ENABLED=true
export N8N_SSO_OIDC_CLIENT_ID=<client-id>
export N8N_SSO_OIDC_CLIENT_SECRET=<client-secret>
export N8N_SSO_OIDC_DISCOVERY_ENDPOINT=<discovery-url>

# Security policy <a href="#security-policy" id="security-policy"></a>
export N8N_SECURITY_POLICY_MANAGED_BY_ENV=true
export N8N_MFA_ENFORCED_ENABLED=true
export N8N_PERSONAL_SPACE_PUBLISHING_ENABLED=false
export N8N_PERSONAL_SPACE_SHARING_ENABLED=false

# Log streaming <a href="#log-streaming" id="log-streaming"></a>
export N8N_LOG_STREAMING_MANAGED_BY_ENV=true
export N8N_LOG_STREAMING_DESTINATIONS='[{"type":"webhook","url":"https://logs.example.com/n8n"}]'

# MCP <a href="#mcp" id="mcp"></a>
export N8N_MCP_MANAGED_BY_ENV=true
export N8N_MCP_ACCESS_ENABLED=true

# Community packages <a href="#community-packages" id="community-packages"></a>
export N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV=true
export N8N_COMMUNITY_PACKAGES='[{"name":"n8n-nodes-foo","version":"1.2.3"}]'
```

## 设置环境变量 <a href="#set-environment-variables" id="set-environment-variables"></a>

支持的环境变量设置方式请参阅[配置方式](basic-configuration.md)。

## 相关资源 <a id="related-resources"></a>

* [配置 n8n](./)
