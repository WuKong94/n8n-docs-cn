---
title: 设置 Okta Workforce Identity SAML
description: 在 n8n 中使用 Okta Workforce Identity。
contentType: tutorial
nodeTitle: 设置 Okta Workforce Identity SAML
originalFilePath: user-management/saml/okta.md
originalUrl: https://docs.n8n.io/user-management/saml/okta
url: https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-okta-workforce-identity-saml
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 设置 Okta Workforce Identity SAML <a href="#okta-workforce-identity-saml-setup" id="okta-workforce-identity-saml-setup"></a>

使用 Okta 在 n8n 中设置 SAML SSO。

{% hint style="info" %}
**Workforce Identity 与 Customer Identity**

本指南介绍如何设置 Workforce Identity，即原有的 Okta 产品。Customer Identity 是 Okta 对其收购的 Auth0 产品所使用的名称。
{% endhint %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

你需要 Okta Workforce Identity 账号，以及 n8n SAML 设置中的重定向 URL 和实体 ID。

根据你的 Okta 配置，Okta Workforce 可能会要求用户使用双因素身份验证。

请先阅读[设置 SAML](set-up-saml.md)指南。

## 设置 <a href="#setup" id="setup"></a>

除以下说明外，这份图文分步指南也展示了如何使用 Okta 在 n8n 中设置 SAML：

{% file src="../../../.gitbook/assets/n8n-saml-with-okta.pdf" %}
使用 Okta 设置 SAML 的图文分步指南
{% endfile %}

1. 在 Okta 管理面板中，选择 **Applications**（应用）> **Applications**（应用）。
1. 选择 **Create App Integration**（创建应用集成）。Okta 会打开应用创建弹窗。
1. 选择 **SAML 2.0**，然后选择 **Next**（下一步）。
1. 在 **General Settings**（常规设置）选项卡中，将 **App name**（应用名称）填写为 `n8n`。
1. 选择 **Next**（下一步）。
1. 在 **Configure SAML**（配置 SAML）选项卡中，填写以下 **General**（常规）字段：
	* **Single sign-on URL**（单点登录 URL）：n8n 的 **Redirect URL**（重定向 URL）。
	* **Audience URI (SP Entity ID)**（受众 URI，即 SP 实体 ID）：n8n 的 **Entity ID**（实体 ID）。
	* **Default RelayState**（默认 RelayState）：留空。
	* **Name ID format**（名称 ID 格式）：`EmailAddress`。
	* **Application username**（应用用户名）：`Okta username`。
	* **Update application username on**（应用用户名更新时机）：`Create and update`。
1. 创建 **Attribute Statements**（属性语句）：
	
	| **名称** | **名称格式** | **值** |
	| -------- | --------------- | --------- |
	| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/firstname` | URI Reference | user.firstName |
	| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/lastname` | URI Reference | user.lastName |
	| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn` | URI Reference | user.login |
	| `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` | URI Reference | user.email |
	
1. 选择 **Next**（下一步）。Okta 可能会要求填写营销表单，也可能直接打开新建的 n8n Okta 应用。
1. 将 n8n 应用分配给用户：
	1. 在 Okta 的 n8n 应用控制台中，选择 **Assignments**（分配）。
	1. 选择 **Assign**（分配）> **Assign to People**（分配给用户）。Okta 会显示可用用户列表弹窗。
	1. 选择待添加用户旁的 **Assign**（分配）。Okta 会提示确认用户名。
	1. 将用户名保留为邮箱地址，选择 **Save and Go Back**（保存并返回）。
	1. 选择 **Done**（完成）。
1. 获取元数据 XML：在 **Sign On**（登录）选项卡中复制 Metadata URL（元数据 URL），访问该地址并复制 XML，将其粘贴到 n8n 的 **Identity Provider Settings**（身份提供方设置）。
1. 选择 **Save settings**（保存设置）。
1. 选择 **Test settings**（测试设置）。n8n 会打开新选项卡。如果尚未登录，Okta 会提示登录，随后 n8n 显示成功消息，确认 Okta 返回的属性。

### 实例与项目访问权限预配 <a href="#instance-and-project-access-provisioning" id="instance-and-project-access-provisioning"></a>

n8n 支持通过 SSO 以两种方式预配实例与项目角色。请根据希望在哪里配置映射逻辑进行选择：

- **Map rules on your IdP**（在 IdP 中映射规则）：在 Okta 中配置 n8n 专用属性（`n8n_instance_role` 和 `n8n_projects`），n8n 直接从 SAML 响应读取这些属性。步骤见下文。
- **Map rules inside n8n**（在 n8n 中映射规则）：将 Okta 的组成员关系作为 SAML 属性发送，并在 n8n 中定义映射表达式。除组属性外，Okta 中无需配置其他 n8n 专用内容。请参阅 SAML 主设置页中的[在 n8n 中映射规则](set-up-saml.md#map-rules-inside-n8n)。

在 n8n 中，将 **Role assignment**（角色分配）设为 **Instance roles via SSO**（通过 SSO 分配实例角色）或 **Instance and project roles via SSO**（通过 SSO 分配实例与项目角色），然后选择所需的 **Role mapping method**（角色映射方法）。

#### 在 IdP 中映射规则 <a href="#map-rules-on-your-idp" id="map-rules-on-your-idp"></a>

**添加所需属性**

1. 在 Okta 管理面板中，选择 **Applications**（应用）> **Applications**（应用）。
2. 进入 n8n 应用的配置页面。
3. 在 **General**（常规）选项卡中，点击 **SAML Settings**（SAML 设置）旁的 **Edit**（编辑）。
4. 在打开的页面中，继续到第二步：**Configure SAML**（配置 SAML）。
5. 添加以下两条 **Attribute Statements**（属性语句）：

	| **名称** | **名称格式** | **值** |
	| -------- | --------------- | --------- |
	| n8n_instance_role | Basic | appuser.n8n_instance_role |
	| n8n_projects | Basic | appuser.n8n_projects |

6. 点击 **Next**（下一步）。
7. 点击 **Finish**（完成）。

**更新应用配置文件**

1. 在 Okta 管理面板中，选择 **Directory**（目录）> **Profile Editor**（配置文件编辑器）。
2. 进入 n8n 应用的配置文件。
3. 点击 **Add Attribute**（添加属性）。
4. 添加 **n8n_instance_role** 属性。
	* **Data type**（数据类型）：string（字符串）。
	* **Display name**（显示名称）：n8n_instance_role
	* **Variable name**（变量名）：n8n_instance_role
	* **Attribute type**（属性类型）：Group（组）。
4. 添加 **n8n_projects** 属性。
	* **Data type**（数据类型）：string array（字符串数组）。
	* **Display name**（显示名称）：n8n_projects
	* **Variable name**（变量名）：n8n_projects
	* **Attribute type**（属性类型）：Group（组）。
	* **Group priority**（组优先级）：Combine values across groups（合并各组的值）。

现在前往 **Directory**（目录）> **Groups**（组），编辑已分配的 n8n 应用，即可配置通过 SAML 登录时向 n8n 发送的 **n8n_instance_role** 和 **n8n_projects**。

## 相关资源 <a id="related-resources"></a>

* [使用 SAML](./)
* [设置 SAML](set-up-saml.md)
* [设置 Azure AD SAML](set-up-azure-ad-saml.md)
* [排查 SAML 问题](troubleshoot-saml.md)
* [启用 SAML 时管理用户](manage-users-with-saml.md)
