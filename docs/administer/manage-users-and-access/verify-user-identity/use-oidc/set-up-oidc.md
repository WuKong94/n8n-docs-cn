---
title: 设置 OIDC
description: 在 n8n 中启用 OIDC SSO 的设置说明。
contentType: howto
nodeTitle: 设置 OIDC
originalFilePath: user-management/oidc/setup.md
originalUrl: https://docs.n8n.io/user-management/oidc/setup
url: https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-oidc/set-up-oidc
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 设置 OIDC <a href="#set-up-oidc" id="set-up-oidc"></a>

{% include "../../../../reusable-content/.gitbook/includes/user-management/sso-oidc-availability.md" %}

{% hint style="info" %}
**功能可用范围**

自 n8n 2.18.0 起，可以通过环境变量配置 OIDC，无需使用界面。请参阅 [SSO 环境变量](../../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso.md)。
{% endhint %}

## 设置并启用 OIDC <a href="#setting-up-and-enabling-oidc" id="setting-up-and-enabling-oidc"></a>


1. 在 n8n 中，前往 **Settings**（设置）> **SSO**。
1. 在 **Select Authentication Protocol**（选择身份验证协议）下拉菜单中选择 **OIDC**。
1. 复制显示的**重定向 URL**（例如 `https://yourworkspace.app.n8n.cloud/rest/sso/oidc/callback`）。<br>

	<div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>负载均衡器或代理的额外配置</strong></p><p>如果 n8n 部署在负载均衡器之后，请务必设置 <a href="../../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment.md"><code>N8N_EDITOR_BASE_URL</code> 环境变量</a>。</p></div>

1. 在身份提供方（IdP）中设置 OIDC。你需要：
	- 在 IdP 中创建新的 OIDC 客户端或应用。
	- 配置上一步获取的重定向 URL。
	- 记下 IdP 提供的 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）。
1. 在 IdP 中查找 **Discovery Endpoint**（发现端点，也称 well-known 配置端点）。其格式通常如下：
	```
	https://your-idp-domain/.well-known/openid-configuration
	```
1. 在 n8n 中完成 OIDC 配置：
	- **Discovery Endpoint**（发现端点）：填写 IdP 的发现端点 URL。
	- **Client ID**（客户端 ID）：填写在 IdP 中注册应用时获得的客户端 ID。
	- **Client Secret**（客户端密钥）：填写在 IdP 中注册应用时获得的客户端密钥。
1. 选择 **Save settings**（保存设置）。
1. 将 OIDC 设为 **Activated**（已启用）。

### 实例与项目访问权限预配 <a href="#instance-and-project-access-provisioning" id="instance-and-project-access-provisioning"></a>

n8n 支持通过 SSO 预配实例角色和项目角色。用户通过 OIDC 登录时，n8n 可以根据 IdP 响应中的声明，自动分配其实例角色和项目访问权限。

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

- **Map rules on your IdP**（在 IdP 中映射规则）：n8n 直接从 IdP 响应读取 n8n 专用声明（`n8n_instance_role` 和 `n8n_projects`）。IdP 管理员配置每个用户或组应获得的 n8n 角色或项目。
- **Map rules inside n8n**（在 n8n 中映射规则）：在 n8n 中定义表达式，根据用户的 OIDC 声明计算并返回角色。如果 IdP 无法表达 n8n 专用的角色逻辑，或 IT 管理流程导致 IdP 端更改较慢，可使用此选项。

#### 在 IdP 中映射规则 <a href="#map-rules-on-your-idp" id="map-rules-on-your-idp"></a>

在 OIDC 授权服务器中添加名为 `n8n` 的额外作用域，并包含以下两个声明：

| **名称** | **数据类型** | **作用域** | **令牌类型** |
| -------- | ------------- | --------- | -------------- |
| `n8n_instance_role` | 字符串 | `n8n` | ID |
| `n8n_projects` | 字符串数组 | `n8n` | ID |

授权服务器发出的 ID Token 必须始终包含这两个声明。请为 IdP 中可以访问 n8n 的用户组配置这些声明。

**配置 `n8n_instance_role` 声明**

`n8n_instance_role` 是在 IdP 中为组或用户配置的字符串。如果未设置值，n8n 会回退到 `global:member`。

支持的实例角色：

- `global:member`
- `global:admin`
- `global:chatUser`

**配置 `n8n_projects` 声明**

`n8n_projects` 是在 IdP 中为组或用户配置的字符串数组，每个元素都必须符合 `<project-id>:<role>` 格式。

例如：

- `bHsykgeFirmIhezz:viewer`
- `4K3zrg3DvlMFFTB7:editor`
- `dCjnYuEpYOUBVaNe:admin`

对于启用项目预配时已存在的访问权限，可以在下载的 CSV 文件中查找项目 ID。

对于新项目，可在浏览器中查看项目时，从 URL 获取项目 ID。在 URL `<your-domain>/projects/VVRWZaq5DRxaf9O1/workflows` 中，项目 ID 为 `VVRWZaq5DRxaf9O1`。

#### 在 n8n 中映射规则 <a href="#map-rules-inside-n8n" id="map-rules-inside-n8n"></a>

自 n8n 2.19.0 起支持 **Map rules inside n8n**（在 n8n 中映射规则）。

使用此选项可在 n8n 中定义从组到角色的映射，而不必在 IdP 中定义。每条规则都是一个表达式，由 n8n 根据 IdP 响应中的 OIDC 声明进行计算。

**表达式的工作方式**

- 表达式通过 `$claims` 对象访问 IdP 响应中的全部 OIDC 声明。
- 如果表达式返回 `true`，n8n 会分配你在该规则中选择的角色。
- 规则按从上到下的顺序计算，采用首个匹配的规则。
- 每次登录都会重新计算规则，因此角色更改会在用户下次会话时生效。
- `$claims` 提供原始 IdP 响应，n8n 不会对其进行标准化处理，因此应按照 IdP 实际发送的结构编写表达式。

{% hint style="info" %}
**让 IdP 发送 groups 声明**

大多数基于组的规则都需要 OIDC 响应包含 `groups` 声明。默认情况下不会包含此声明，你需要配置 IdP 来发送它。例如，在 Okta 中添加 `groups` 作用域，或在 Azure AD 令牌配置中设置 `groups` 声明。编写规则前，请检查 IdP 响应，确认声明的准确名称和结构。
{% endhint %}

**userinfo 响应示例**

身份验证完成后，n8n 会调用 IdP 的 userinfo 端点获取用户声明。典型响应如下：

```json
{
  "sub": "00uwyqw9raWrKRJ0Q697",
  "name": "Jane Doe",
  "email": "jane.doe@example.com",
  "email_verified": true,
  "given_name": "Jane",
  "family_name": "Doe",
  "groups": [
    "Everyone",
    "n8n admins",
    "n8n members",
    "Operations"
  ]
}
```

`$claims` 反映此载荷的内容。因此，`$claims.email` 为字符串，`$claims.groups` 为字符串数组，两者都可使用标准 JavaScript 方法处理。具体组名取决于 IdP。有些提供方（例如 Azure AD）发送的是组 UUID 而不是显示名称，此时表达式需要引用 UUID。

要在 Okta 中检查自己的 userinfo 响应，请使用有效访问令牌直接调用 userinfo 端点。可以在 **Security**（安全）> **API** > **Authorization Servers**（授权服务器）> 你的服务器 > **Token Preview**（令牌预览）选项卡获取测试访问令牌，然后运行：

```
curl -H "Authorization: Bearer <access-token>" https://<your-okta-domain>/oauth2/<auth-server-id>/v1/userinfo
```

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


## 各提供方的 OIDC 设置 <a href="#provider-specific-oidc-setup" id="provider-specific-oidc-setup"></a>

### Okta <a href="#okta" id="okta"></a>

在 Okta 中设置 OIDC 的步骤与下文介绍的 Auth0 类似。

对于 Okta，你可以下载图文分步指南 PDF：

{% file src="../../../.gitbook/assets/n8n-oidc-with-okta.pdf" %}
使用 Okta 设置 OIDC 的图文分步指南
{% endfile %}

### Auth0 <a href="#auth0" id="auth0"></a>

1. **在 Auth0 中创建应用**：
	- 登录 Auth0 控制台。
	- 前往 **Applications**（应用）> **Applications**（应用）。
	- 点击 **Create Application**（创建应用）。
	- 输入名称（例如“n8n SSO”），选择 **Regular Web Applications**（常规 Web 应用）。
	- 点击 **Create**（创建）。
1. **配置应用**：
	- 前往新应用的 **Settings**（设置）选项卡。
	- **Allowed Callback URLs**（允许的回调 URL）：添加 n8n 的 **Settings**（设置）> **SSO** > **OIDC** 中的重定向 URL。
	- **Allowed Web Origins**（允许的 Web 来源）：添加 n8n 基础 URL（例如 `https://yourworkspace.app.n8n.cloud`）。
	- 点击 **Save Changes**（保存更改）。
1. **获取凭据**：
	- **Client ID**（客户端 ID）：位于 **Settings**（设置）选项卡。
	- **Client Secret**（客户端密钥）：位于 **Settings**（设置）选项卡。
	- **Discovery Endpoint**（发现端点）：`https://{your-auth0-domain}.auth0.com/.well-known/openid-configuration`。
1. **在 n8n 中完成 OIDC 配置：**
	- **Discovery Endpoint**（发现端点）：填写 Auth0 的发现端点 URL。
	- **Client ID**（客户端 ID）：填写在 Auth0 设置中找到的客户端 ID。
	- **Client Secret**（客户端密钥）：填写在 Auth0 设置中找到的客户端密钥。
1. 选择 **Save settings**（保存设置）。
1. 将 OIDC 设为 **Activated**（已启用）。

## 发现端点参考 <a href="#discovery-endpoints-reference" id="discovery-endpoints-reference"></a>

- **Google 发现端点示例**：
```
https://accounts.google.com/.well-known/openid-configuration
```
- **Microsoft Azure AD 发现端点示例**：
```
https://login.microsoftonline.com/{tenant-id}/v2.0/.well-known/openid-configuration
```
- **Auth0 发现端点示例**：
```
https://{your-domain}.auth0.com/.well-known/openid-configuration
```
- **Okta 发现端点示例**：
```
https://{your-domain}.okta.com/.well-known/openid-configuration
```
- **Amazon Cognito 发现端点示例**：
```
https://cognito-idp.{region}.amazonaws.com/{user-pool-id}/.well-known/openid-configuration
```

## 相关资源 <a id="related-resources"></a>

* [使用 OIDC](./)
* [排查 OIDC 问题](troubleshoot-oidc.md)
