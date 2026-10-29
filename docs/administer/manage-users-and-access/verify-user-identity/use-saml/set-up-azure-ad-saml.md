---
title: 设置 Azure AD SAML
description: 在 n8n 中使用 Azure AD。
contentType: tutorial
nodeTitle: 设置 Azure AD SAML
originalFilePath: user-management/saml/azuread.md
originalUrl: https://docs.n8n.io/user-management/saml/azuread
url: https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-azure-ad-saml
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 设置 Azure AD SAML <a href="#azure-ad-saml-setup" id="azure-ad-saml-setup"></a>

本文介绍如何配置 Azure AD，通过 SAML 属性向 n8n 发送角色信息，从而根据 Azure AD 组成员关系自动分配角色。

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

你需要能访问 Enterprise Applications（企业应用）的 Azure AD 账号，以及 n8n SAML 设置中的重定向 URL 和实体 ID。

请先阅读[设置 SAML](set-up-saml.md)指南。

## n8n 的要求 <a href="#what-n8n-requires" id="what-n8n-requires"></a>

n8n 要求 SAML 断言中包含以下自定义 SAML 属性：

| **属性名称** | **数据类型** | **用途** |
| ------------------- | ------------- | ----------- |
| n8n_instance_role | 字符串 | 控制用户在 n8n 中的全局角色 |

`n8n_instance_role` 的有效值：

| **值** | **说明** |
| --------- | --------------- |
| `global:owner` | 完整的实例所有者访问权限 |
| `global:admin` | 管理员访问权限 |
| `global:member` | 普通成员访问权限（未指定时的默认值） |
| `global:chatUser` | n8n 中权限受限、面向非技术用户的角色，用于通过 Chat Hub 界面安全地与 AI 智能体交互 |

## 设置 <a href="#setup" id="setup"></a>

**第一步：配置标准 SAML 属性**

1. 在 Azure AD 门户中，进入 n8n 企业应用。
2. 前往 **Single sign-on**（单点登录）> **Attributes & Claims**（属性与声明）。
3. 确保已配置以下标准属性：

	| **声明名称** | **源属性** |
	| -------------- | ------------------- |
	| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` | user.mail |
	| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/firstname` | user.givenname |
	| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/lastname` | user.surname |
	| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn` | user.userprincipalname |


**第二步：添加 n8n_instance_role 声明**

此声明使用条件逻辑，根据 Azure AD 组成员关系输出不同的角色值。

1. 在 **Attributes & Claims**（属性与声明）中，点击 **Add new claim**（添加新声明）。
2. 配置基本设置：
	* **Name**（名称）：`n8n_instance_role`
	* **Namespace**（命名空间）：留空。
	* **Source**（来源）：`Attribute`
3. 展开 **Claim conditions**（声明条件），点击 **Add condition**（添加条件）。
4. 为每个 Azure AD 组添加条件（按优先顺序）：

	| **User Type（用户类型）** | **Scoped Groups（限定组）** | **Source（来源）** | **Value（值）** |
	| ------------- | ----------------- | ---------- | --------- |
	| Members | n8n-chatusers | Attribute | `global:chatUser` |
	| Members | n8n-users | Attribute | `global:member` |
	| Members | n8n-admins | Attribute | `global:admin` |
	| Members | n8n-owners | Attribute | `global:owner` |

{% hint style="info" %}
**条件顺序**

条件按顺序计算。请将权限最高的组（owners）放在最后。
{% endhint %}

5. 点击 **Save**（保存）。

### 测试配置 <a href="#testing-the-configuration" id="testing-the-configuration"></a>

1. 在 n8n 中，前往 **Settings**（设置）> **SSO**。
1. 将 **Role assignment**（角色分配）设为 **Instance roles via SSO**（通过 SSO 分配实例角色）。
1. 将 **Role mapping method**（角色映射方法）设为 **Map rules on your IdP**（在 IdP 中映射规则）。
1. 点击 **Test settings**（测试设置）。
1. 确认 SAML 响应显示了正确的 `n8n_instance_role` 值。

### 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

**SAML 响应中没有出现声明**

* 确认用户至少属于一个已配置的组。
* 检查这些组是否已分配给企业应用。
* 确保条件配置使用 `Attribute` 作为来源。
* 使用 SAML Chrome Panel 等浏览器扩展查看应用的 SAML 响应。

**用户获得的角色不正确**

* 检查条件顺序（权限最高的组应放在最后）。

## 使用应用角色代替基于组的声明，分配多个项目角色 <a href="#assigning-multiple-project-roles-using-app-roles-instead-of-group-based-claims" id="assigning-multiple-project-roles-using-app-roles-instead-of-group-based-claims"></a>

使用 Azure AD 基于组的声明条件，为用户分配多个项目角色时，往往只有首个匹配的组声明会发送到 SAML 断言中。这意味着，即使用户属于多个组，也可能只获得一个项目的访问权限。

要可靠地分配多个项目及其各自的角色，请使用在 App Registration（应用注册）中定义的 **App Roles**（应用角色），代替基于组的声明：

1. 在 n8n SAML 应用的 **App Registration**（应用注册）中，定义代表各个项目与权限组合的应用角色（例如 `<projectId>:<role>`）。
2. 保存更新后的应用清单。
3. 在 **Enterprise Application**（企业应用）的 **Users and groups**（用户和组）下，将这些应用角色分配给用户或组。
4. 在 **Single sign-on > Attributes & Claims**（单点登录 > 属性与声明）中，将 `n8n_projects` SAML 声明的来源更新为 `user.assignedroles`。这样会将全部已分配角色以数组形式输出到 SAML 响应中。

此设置可确保 n8n 正确接收所有项目分配，让用户在多个项目中获得相应访问权限。虽然定义应用角色会增加初始管理工作量，但能简化后续的用户角色管理，并确保完整同步项目角色。

从基于组的声明迁移到应用角色时，请相应调整角色定义和声明映射，以免项目访问权限不完整。

## 参考资料 <a href="#references" id="references"></a>

* [n8n SAML 设置](set-up-saml.md)
* [n8n Okta 指南（参考）](set-up-okta-workforce-identity-saml.md)
* [Azure AD 声明自定义](https://learn.microsoft.com/en-us/entra/identity-platform/saml-claims-customization)

## 相关资源 <a id="related-resources"></a>

* [使用 SAML](./)
* [设置 SAML](set-up-saml.md)
* [设置 Okta Workforce Identity SAML](set-up-okta-workforce-identity-saml.md)
* [排查 SAML 问题](troubleshoot-saml.md)
* [启用 SAML 时管理用户](manage-users-with-saml.md)
