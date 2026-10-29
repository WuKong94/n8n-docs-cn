---
description: 在 n8n 中使用 LDAP。
contentType: howto
nodeTitle: 连接 LDAP
originalFilePath: user-management/ldap.md
originalUrl: https://docs.n8n.io/user-management/ldap
url: https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/connect-ldap
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 轻量级目录访问协议（LDAP） <a href="#lightweight-directory-access-protocol-ldap" id="lightweight-directory-access-protocol-ldap"></a>

{% hint style="info" %}
**功能可用范围**

LDAP 可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**Business、Enterprise。

你需要能访问 n8n 实例所有者账号。
{% endhint %}

本页说明如何在 n8n 中启用 LDAP，假定你已熟悉 LDAP，并且已设置好 LDAP 服务器。

LDAP 允许用户使用组织的凭据登录 n8n，无需使用独立的 n8n 登录凭据。

## 启用 LDAP <a href="#enable-ldap" id="enable-ldap"></a>

1. 以实例所有者身份登录 n8n。
2. 选择 **Settings**（设置）<img src="../../.gitbook/assets/settings.png" alt="设置图标" data-size="line"> > **LDAP**。
3. 打开 **Enable LDAP Login**（启用 LDAP 登录）开关。
4. 填写 LDAP 服务器的详细信息，请参阅[连接设置](#connection-settings)。
5. 选择 **Test connection**（测试连接）检查连接设置，或选择 **Save connection**（保存连接）创建连接。

启用 LDAP 后，LDAP 服务器上的任何用户都可以登录 n8n 实例，除非使用 **User Filter**（用户筛选器）将其排除。

你仍然可以在 **Settings**（设置）> **Users**（用户）页面创建非 LDAP 用户（邮箱用户）。

## 连接设置 <a id="connection-settings"></a>

打开 **Enable LDAP Login**（启用 LDAP 登录）后，会显示以下字段。

| 字段 | 填写内容 |
| -- | -- |
| **LDAP Login**（LDAP 登录） | n8n 登录页上用户名字段的标签，用于替代 **Email**（邮箱）。 |
| **LDAP Server Address**（LDAP 服务器地址） | LDAP 服务器的 IP 地址或域名。 |
| **LDAP Server Port**（LDAP 服务器端口） | n8n 连接的端口，预填为标准 LDAP 端口 `389`。如果选择 **TLS**，请改为服务器的 LDAPS 端口，默认为 `636`。 |
| **Connection Security**（连接安全性） | 可选 **None**（无）、**TLS** 或 **STARTTLS**。**TLS** 使用 `ldaps://` 连接；**None** 和 **STARTTLS** 使用 `ldap://` 连接，**STARTTLS** 随后会将连接升级为 TLS。 |
| **Ignore SSL/TLS Issues**（忽略 SSL/TLS 问题） | 即使证书检查失败也进行连接。此字段仅在 **Connection Security** 不为 **None** 时显示。 |
| **Base DN**（基础 DN） | n8n 在目录树中开始查找用户的位置，例如 `o=acme,dc=example,dc=com`。 |
| **Binding as**（绑定身份） | **Admin**（管理员）或 **Anonymous**（匿名）。请参阅[绑定方法](#bind-methods)。 |
| **Binding DN**（绑定 DN） | n8n 用于搜索目录的账号，例如 `uid=2da2de69435c,ou=Users,o=Acme,dc=com`。此字段仅在 **Binding as** 为 **Admin** 时显示。 |
| **Binding Password**（绑定密码） | **Binding DN** 用户的密码。此字段仅在 **Binding as** 为 **Admin** 时显示。 |
| **User Filter**（用户筛选器） | 用于限制哪些用户可以登录的 LDAP 查询，例如 `(ObjectClass=user)`。只有该查询返回的用户才能登录。 |

接下来是 **Attribute mapping**（属性映射）字段，告诉 n8n 应读取哪些 LDAP 属性来获取用户 ID、登录 ID、邮箱、名字和姓氏。正确的值取决于你的目录，n8n 在这些字段中显示的示例并不适用于所有服务器。请使用 `ldapsearch` 等工具查询 LDAP 服务器，查看输出中的一个用户条目，记下分别包含这五项值的属性名，并将属性名填入映射字段。

最后是同步字段，仅在打开 **Enable periodic LDAP synchronization**（启用定期 LDAP 同步）时显示。

**Enforce Email Uniqueness**（强制邮箱唯一）位于表单底部、同步字段下方。如果多个 LDAP 账号使用相同的邮箱地址，此选项会阻止登录。

## 绑定方法 <a id="bind-methods"></a>

n8n 使用简单绑定连接 LDAP 服务器。**Binding as**（绑定身份）决定具体方式：

- **Admin**（管理员）：n8n 使用你填写的 **Binding DN**（绑定 DN）和 **Binding Password**（绑定密码）进行绑定。
- **Anonymous**（匿名）：n8n 发送空的 DN 和密码，因此服务器必须允许匿名搜索。

n8n 不支持 SASL 绑定，包括 GSSAPI 和 Kerberos。界面没有用于设置 SASL 机制、keytab 或 Kerberos 票据缓存的字段。如果你的目录要求基于 Kerberos 的绑定（常见于 Active Directory），则无法使用 LDAP 登录。n8n 还支持通过 [SAML](use-saml/README.md) 和 [OIDC](use-oidc/README.md) 进行单点登录。

## 合并 n8n 与 LDAP 账号 <a href="#merging-n8n-and-ldap-accounts" id="merging-n8n-and-ldap-accounts"></a>

如果 n8n 发现邮箱用户与 LDAP 用户的账号匹配（邮箱相同），用户就必须使用 LDAP 账号登录。n8n 实例所有者账号不受此规则影响：n8n 绝不会将所有者账号转换为 LDAP 用户。

## n8n 中的 LDAP 用户账号 <a href="#ldap-user-accounts-in-n8n" id="ldap-user-accounts-in-n8n"></a>

首次登录时，n8n 会为 LDAP 用户创建一个 n8n 用户账号。

用户资料必须在 LDAP 服务器上管理，而不是在 n8n 中管理。如果在 LDAP 服务器上更新或删除用户，n8n 账号会在下次计划同步或用户下次尝试登录时更新，以先发生者为准。

{% hint style="info" %}
**删除用户**

从 LDAP 服务器移除用户后，该用户将在下次同步时失去 n8n 访问权限。
{% endhint %}

## 关闭 LDAP <a href="#turn-ldap-off" id="turn-ldap-off"></a>

要关闭 LDAP：

1. 以实例所有者身份登录 n8n。
2. 选择 **Settings**（设置）<img src="../../.gitbook/assets/settings.png" alt="设置图标" data-size="line"> > **LDAP**。
3. 关闭 **Enable LDAP Login**（启用 LDAP 登录）开关。

关闭 LDAP 后，n8n 会在现有 LDAP 用户下次登录时将其转换为邮箱用户。这些用户必须重置密码。

## 相关资源 <a id="related-resources"></a>

* [验证用户身份](./)
* [要求双因素身份验证](require-two-factor-auth.md)
* [使用 SAML](use-saml/README.md)
* [使用 OIDC](use-oidc/README.md)
