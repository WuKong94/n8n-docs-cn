---
description: 管理实例级安全策略，包括强制 MFA 和个人空间控制。
contentType: howto
nodeTitle: 管理安全策略
originalFilePath: security-settings.md
originalUrl: https://docs.n8n.io/security-settings
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/manage-security-policies
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 安全设置 <a href="#security-settings" id="security-settings"></a>

{% hint style="info" %}
**功能可用范围**

安全设置可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**商业版、企业版。

部分设置需要特定的许可证功能。当前套餐不支持的设置会显示 **Upgrade**（升级）标记。
{% endhint %}

安全设置允许你管理实例级安全策略。你可以为所有用户强制要求双因素身份验证，并控制用户在个人空间中能进行的操作。

要访问安全设置，请前往 **Settings**（设置）> **Security**（安全）。

## 强制双因素身份验证 <a href="#enforce-two-factor-authentication" id="enforce-two-factor-authentication"></a>

你可以要求实例上通过邮箱和密码登录的所有用户设置双因素身份验证（2FA）。

{% hint style="info" %}
**仅适用于邮箱和密码登录**

强制 2FA 适用于通过邮箱和密码验证身份的用户。通过 SSO（SAML 或 OIDC）登录的用户不受此设置影响。
{% endhint %}

要强制要求 2FA：

1. 前往 **Settings**（设置）> **Security**（安全）。
2. 在 **Enforce two-factor authentication**（强制双因素身份验证）区域打开开关。

启用此设置后：

- 所有用户必须设置 2FA 才能继续使用实例。
- 尚未配置 2FA 的用户会在下次登录时收到设置提示。

要停止强制要求 2FA，请关闭开关。已设置 2FA 的用户仍保持启用，新用户则不再需要配置。

个人用户如何设置 2FA，请参阅[双因素身份验证](../../../../administer/manage-users-and-access/verify-user-identity/require-two-factor-auth.md)。

## 个人空间策略 <a href="#personal-space-policies" id="personal-space-policies"></a>

个人空间策略允许实例管理员控制用户能否从个人空间共享工作流和凭据，以及发布工作流。

### 共享工作流和凭据 <a href="#sharing-workflows-and-credentials" id="sharing-workflows-and-credentials"></a>

控制用户能否将个人空间中的工作流和凭据共享给其他用户或项目。

要管理共享：

1. 前往 **Settings**（设置）> **Security**（安全）。
2. 在 **Personal Space**（个人空间）区域找到 **Sharing workflows and credentials**（共享工作流和凭据）。
3. 使用开关启用或禁用共享。

禁用共享后：

- 现有共享保持有效，此设置仅影响新的共享操作。
- 开关下方显示当前已共享的工作流和凭据数量。

### 发布工作流 <a href="#publishing-workflows" id="publishing-workflows"></a>

控制用户能否发布个人空间中的工作流，使其可执行。

要管理发布：

1. 前往 **Settings**（设置）> **Security**（安全）。
2. 在 **Personal Space**（个人空间）区域找到 **Publishing workflows**（发布工作流）。
3. 使用开关启用或禁用发布。

禁用发布后：

- 当前已发布的工作流保持发布状态，此设置仅影响新的发布操作。
- 开关下方显示当前已发布的个人工作流数量。

## 工作流审核 <a href="#workflow-reviews" id="workflow-reviews"></a>

{% hint style="info" %}
**预览状态**

工作流审核处于预览阶段，正式发布前可能更改。请避免在生产工作流中依赖此功能。
{% endhint %}

{% hint style="info" %}
**功能可用范围**

工作流审核可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**企业版。

自 n8n 2.37.0 起提供工作流审核。
{% endhint %}

使用工作流审核，团队可以在发布前提交工作流版本以供批准。实例管理员为整个实例启用此功能。

要启用工作流审核：

1. 前往 **Settings**（设置）> **Security & policies**（安全与策略）。
2. 在 **Workflow reviews**（工作流审核）区域打开 **Enable workflow reviews**（启用工作流审核）。

关闭此设置后，用户无法创建或管理审核。关闭功能还会解除仍有未完成审核的工作流的发布限制。启用后如何提交、批准和发布，请参阅[工作流审核](../../../../build/manage-workflows/workflow-reviews.md)。

## 强制执行数据脱敏 <a href="#enforce-execution-data-redaction" id="enforce-execution-data-redaction"></a>

你可以对实例上的所有工作流强制要求[执行数据脱敏](redact-execution-data.md)。此功能设置实例级最低脱敏策略，单个工作流的设置不能弱化此策略。

{% hint style="info" %}
**功能可用范围**

强制数据脱敏可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**企业版。

自 n8n 2.26.0 起提供。
{% endhint %}

要强制要求数据脱敏：

1. 前往 **Settings**（设置）> **Security**（安全）。
2. 在 **Data redaction**（数据脱敏）区域打开 **Enforce data redaction**（强制数据脱敏）。
3. 在 **Redact executions**（执行脱敏）下选择强制范围：
	- **Production executions (Recommended)**（生产执行，推荐）：n8n 对所有工作流的生产执行数据进行脱敏。
	- **Manual and production executions**（手动执行和生产执行）：n8n 对所有工作流的手动执行和生产执行数据进行脱敏。
4. 在对话框中确认选择。

启用强制脱敏后：

- n8n 会对所有工作流中属于所选范围的执行数据进行脱敏，包括未在自身设置中启用脱敏的工作流。
- 用户不能将工作流级脱敏设置改为比强制范围更宽松的策略。工作流仍可以采用更严格的脱敏策略，例如仅强制生产执行脱敏时，也对手动执行脱敏。
- 新工作流默认采用强制范围作为脱敏策略。

强制脱敏需要包含数据脱敏功能的 Enterprise 许可证。脱敏覆盖范围、查看原始数据及权限的详情，请参阅[执行数据脱敏](redact-execution-data.md)。

## 通过环境变量配置安全策略 <a href="#configure-security-policy-with-environment-variables" id="configure-security-policy-with-environment-variables"></a>

你也可以通过环境变量管理安全策略设置，而非通过界面。此选项自 n8n 2.18.0 起提供。将 `N8N_SECURITY_POLICY_MANAGED_BY_ENV` 设为 `true`，并提供以下变量。启用机制请参阅[通过环境变量管理实例设置](../manage-settings-using-environment-variables.md)。

当 `N8N_SECURITY_POLICY_MANAGED_BY_ENV` 为 `true` 时，本页的 **Enforce two-factor authentication**（强制双因素身份验证）和 **Personal Space**（个人空间）开关变为只读。

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/security-policy.md" %}

## 相关资源 <a id="related-resources"></a>

* [安全](../security.md)
