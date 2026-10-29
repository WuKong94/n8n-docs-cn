---
title: 设置 SAML
description: 在 n8n 中使用 SAML SSO 的通用设置说明。
contentType: howto
nodeTitle: 设置 SAML
originalFilePath: user-management/saml/setup.md
originalUrl: https://docs.n8n.io/user-management/saml/setup
url: https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-saml
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 设置 SAML <a href="#set-up-saml" id="set-up-saml"></a>

{% include "../../../../reusable-content/.gitbook/includes/user-management/sso-saml-availability.md" %}

{% hint style="info" %}
**使用环境变量配置**

自 n8n 2.18.0 起，可以通过环境变量配置 SAML，无需使用界面。请参阅 [SSO 环境变量](../../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso.md)。
{% endhint %}

## 启用 SAML <a href="#enable-saml" id="enable-saml"></a>

1. 在 n8n 中，前往 **Settings**（设置）> **SSO**。
1. 记下 n8n 的 **Redirect URL**（重定向 URL）和 **Entity ID**（实体 ID）。
	* **可选**：如果 IdP 支持通过导入元数据设置 SAML，请访问 **Entity ID** URL 并保存 XML。
	* **可选**：如果 n8n 部署在负载均衡器之后，请确保已配置 `N8N_EDITOR_BASE_URL`。
1. 在身份提供方（IdP）中设置 SAML。你需要 **Redirect URL**（重定向 URL）和 **Entity ID**（实体 ID），可能还需要 IdP 用户的邮箱地址和姓名。
1. 在 IdP 中完成设置后，将元数据 XML 加载到 n8n。可以使用元数据 URL 或原始 XML：
	* **Metadata URL**（元数据 URL）：将 IdP 的元数据 URL 复制到 n8n 的 **Identity Provider Settings**（身份提供方设置）字段。
	* **Raw XML**（原始 XML）：从 IdP 下载元数据 XML，将 **Identiy Provider Settings**（身份提供方设置）切换为 **XML**，再将原始 XML 复制到 **Identity Provider Settings**（身份提供方设置）。
1. 选择 **Save settings**（保存设置）。
1. 选择 **Test settings**（测试设置），检查 SAML 设置是否正常。
1. 将 SAML 2.0 设为 **Activated**（已启用）。

{% hint style="info" %}
**SAML 请求类型**

n8n 不支持 `POST` 绑定，请将 IdP 配置为使用 `HTTP` 请求绑定。
{% endhint %}

## 通用 IdP 设置 <a href="#generic-idp-setup" id="generic-idp-setup"></a>

IdP 的配置步骤取决于所选提供方，以下是一些常见设置任务：

* 在 IdP 中为 n8n 创建应用。
* 将 n8n 属性映射到 IdP 属性：

| 值（IdP 端） | 名称格式 | 名称 |
| ---------------- | ----------- | ---- |
| 用户邮箱 | URI Reference | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` |
| 用户名字 | URI Reference | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/firstname` |
| 用户姓氏 | URI Reference | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/lastname` |
| 用户主体名称（每个用户唯一） | URI Reference | `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn` |

{% hint style="warning" %}
**userPrincipalName 必须对每个用户保持唯一**

n8n 使用 `upn` 声明值作为将 SAML 身份关联到 n8n 账号的键。请为每个用户提供不同的值，例如登录名或邮箱。如果 IdP 为多个人发送相同的值，他们就会登录到同一个 n8n 账号。不要将声明名称（`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn`）作为每个用户的值。
{% endhint %}

### 实例与项目访问权限预配 <a href="#instance-and-project-access-provisioning" id="instance-and-project-access-provisioning"></a>

n8n 支持通过 SSO 预配实例角色和项目角色。用户通过 SAML 登录时，n8n 可以根据 SAML 响应中的属性，自动分配其实例角色和项目访问权限。

自 n8n 1.122.2 起支持角色预配。

#### 选择角色分配方式 <a href="#choose-how-roles-are-assigned" id="choose-how-roles-are-assigned"></a>

在 n8n 中，前往 **Settings**（设置）> **SSO**。使用 **Role assignment**（角色分配）下拉菜单，选择如何为通过 SSO 登录的用户分配角色。默认值为 **Assigned manually in n8n**（在 n8n 中手动分配）。

可选项如下：

- **Assigned manually in n8n**（在 n8n 中手动分配）：管理员直接在 n8n 中分配所有角色，不自动映射 IdP 中的角色。
- **Instance roles via SSO**（通过 SSO 分配实例角色）：n8n 在用户登录时从 IdP 读取其实例角色，项目访问权限仍在 n8n 中手动管理。
- **Instance and project roles via SSO**（通过 SSO 分配实例与项目角色）：n8n 在用户登录时从 IdP 读取实例角色和项目访问权限。

每次登录都会重新计算角色，因此 IdP 中的更改会在用户下次登录时生效。

{% hint style="warning" %}
**现有访问权限将被覆盖**

启用任一 SSO 预配模式后，对于在 n8n 中授予、但未体现在 IdP 响应中的访问权限，n8n 会在用户下次登录时将其移除。

保存此更改前，n8n 会要求你下载两个包含当前访问设置的 CSV 文件。请保留以供参考。
{% endhint %}

#### 选择角色映射方法 <a href="#choose-a-role-mapping-method" id="choose-a-role-mapping-method"></a>

将 **Role assignment**（角色分配）设为 **Instance roles via SSO**（通过 SSO 分配实例角色）或 **Instance and project roles via SSO**（通过 SSO 分配实例与项目角色）后，会显示 **Role mapping method**（角色映射方法）下拉菜单，可选择：

- **Map rules on your IdP**（在 IdP 中映射规则）：n8n 直接从 SAML 响应读取 n8n 专用属性（`n8n_instance_role` 和 `n8n_projects`）。IdP 管理员配置每个用户或组应获得的 n8n 角色或项目。
- **Map rules inside n8n**（在 n8n 中映射规则）：在 n8n 中定义表达式，根据用户的 SAML 属性计算并返回角色。如果 IdP 无法表达 n8n 专用的角色逻辑，或 IT 管理流程导致 IdP 端更改较慢，可使用此选项。

#### 在 IdP 中映射规则 <a href="#map-rules-on-your-idp" id="map-rules-on-your-idp"></a>

在 IdP 中为组或单个用户配置以下属性：

| 值（IdP 端） | 数据类型 | 名称 |
| ---------------- | ----------- | ---- |
| `n8n_instance_role` | 字符串 | `n8n_instance_role` |
| `n8n_projects` | 数组 | `n8n_projects` |

**配置 `n8n_instance_role` 属性**

`n8n_instance_role` 是在 IdP 中为组或用户配置的字符串。如果未设置值，n8n 会回退到 `global:member`。

支持的实例角色：

- `global:member`
- `global:admin`
- `global:chatUser`

**配置 `n8n_projects` 属性**

`n8n_projects` 是在 IdP 中为组或用户配置的字符串数组，每个元素都必须符合 `<project-id>:<role>` 格式。

例如：

- `bHsykgeFirmIhezz:viewer`
- `4K3zrg3DvlMFFTB7:editor`
- `dCjnYuEpYOUBVaNe:admin`

对于启用项目预配时已存在的访问权限，可以在下载的 CSV 文件中查找项目 ID。

对于新项目，可在浏览器中查看项目时，从 URL 获取项目 ID。在 URL `<your-domain>/projects/VVRWZaq5DRxaf9O1/workflows` 中，项目 ID 为 `VVRWZaq5DRxaf9O1`。

#### 在 n8n 中映射规则 <a href="#map-rules-inside-n8n" id="map-rules-inside-n8n"></a>

自 n8n 2.19.0 起支持 **Map rules inside n8n**（在 n8n 中映射规则）。

使用此选项可在 n8n 中定义从组到角色的映射，而不必在 IdP 中定义。每条规则都是一个表达式，由 n8n 根据 IdP 响应中的 SAML 属性进行计算。

**表达式的工作方式**

- 表达式通过 `$claims` 对象访问 IdP 响应中的全部 SAML 属性。
- 如果表达式返回 `true`，n8n 会分配你在该规则中选择的角色。
- 规则按从上到下的顺序计算，采用首个匹配的规则。
- 每次登录都会重新计算规则，因此角色更改会在用户下次会话时生效。
- `$claims` 提供原始 SAML 属性，n8n 不会对其进行标准化处理，因此应按照 IdP 实际发送的结构编写表达式。SAML 组成员信息通常以多值属性传递，但具体形式取决于 IdP。

{% hint style="info" %}
**检查 SAML 响应结构**

不同 IdP 序列化组及其他属性的方式不同。编写规则前，请使用 SAML Chrome Panel 等浏览器工具（或 IdP 的测试工具）检查 SAML 响应，确认属性名称和结构。
{% endhint %}

**实例角色规则**

在 **Instance role rules**（实例角色规则）下，选择 **Add rule**（添加规则）来创建规则。输入条件表达式，并选择在条件返回 `true` 时要分配的实例角色。

例如，要向 IdP 中 `admin` 组内的任意用户分配 **Admin**（管理员）角色：

```
{{ $claims.groups.includes('admin') }}
```

**Default condition**（默认条件）行设置在没有任何规则匹配时授予用户的角色，默认是 **Member**（成员）。

**项目角色规则**

在 **Project role rules**（项目角色规则）下，选择 **Add rule**（添加规则），创建在一个或多个项目中分配项目角色的规则。

例如，要向 `operations` 组中的用户授予 **Operations** 项目的 **Project Editor**（项目编辑者）角色，请将表达式设为：

```
{{ $claims.groups.includes('operations') }}
```

在 **assign**（分配）字段选择角色，在 **in**（所在项目）字段选择目标项目。不匹配任何项目规则的用户不会获得项目访问权限。

{% hint style="warning" %}
**手动角色管理已禁用**

启用 **Map rules inside n8n**（在 n8n 中映射规则）时，界面中手动分配用户角色的控件会被禁用。所有角色分配均通过映射规则完成。
{% endhint %}

{% hint style="warning" %}
**切换映射方法**

从 **Map rules inside n8n**（在 n8n 中映射规则）切回 **Map rules on your IdP**（在 IdP 中映射规则）会移除 n8n 内的所有映射。如果未在 IdP 中设置等效映射，用户下次登录时可能失去当前分配的角色。n8n 会在应用此更改前要求确认。
{% endhint %}


## 常用 IdP 的设置资源 <a href="#setup-resources-for-common-idps" id="setup-resources-for-common-idps"></a>

常用 IdP 的文档链接。

| IdP | 文档 |
| --- | ------------- |
| Auth0 | [将 Auth0 配置为 SAML 身份提供方：手动配置 SSO 集成](https://auth0.com/docs/authenticate/single-sign-on/outbound-single-sign-on/configure-auth0-saml-identity-provider#manually-configure-sso-integrations) |
| Authentik | [应用](https://goauthentik.io/docs/applications)与 [SAML 提供方](https://docs.goauthentik.io/add-secure-apps/providers/saml/) |
| Azure AD | [使用 Azure Active Directory 进行 SAML 身份验证](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/auth-saml) |
| JumpCloud | [如何使用 JumpCloud 设置 SAML（SSO）应用](https://jumpcloud.com/support/integrate-with-zoom#configuring-the-sso-integration)（以 `Zoom` 为例） |
| Keycloak | 根据托管方式选择[入门指南](https://www.keycloak.org/guides#getting-started)。 |
| Okta | n8n 提供 [Workforce Identity 设置指南](set-up-okta-workforce-identity-saml.md)，其中包含分步 PDF 指南。 |
| PingIdentity | [PingOne SSO](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_p1sso_start.html) |

## 相关资源 <a id="related-resources"></a>

* [使用 SAML](./)
* [设置 Okta Workforce Identity SAML](set-up-okta-workforce-identity-saml.md)
* [设置 Azure AD SAML](set-up-azure-ad-saml.md)
* [排查 SAML 问题](troubleshoot-saml.md)
* [启用 SAML 时管理用户](manage-users-with-saml.md)
