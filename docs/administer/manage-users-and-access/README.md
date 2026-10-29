---
description: n8n 用户管理。
contentType: overview
nodeTitle: 管理用户与访问
originalFilePath: user-management/index.md
originalUrl: https://docs.n8n.io/user-management
url: https://docs.n8n.io/administer/
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 用户管理 <a href="#user-management" id="user-management"></a>

n8n 用户管理允许邀请其他人在你的实例中协作，包含：

* 登录和密码管理。
* 添加和移除用户。
* 四个内置[实例角色](understand-instance-roles.md)：**Owner**（所有者）、**Admin**（管理员）、**Member**（成员）和 **Chat user**（聊天用户），以及自定义实例角色。**Admin** 和 **Chat user** 可用于 n8n Cloud Pro、Enterprise 和自托管 Enterprise。

{% hint style="info" %}
**隐私**

用户管理功能不会向 n8n 发送邮箱、用户名等个人信息。
{% endhint %}

## 设置指南 <a href="#setup-guides" id="setup-guides"></a>

本节包含大多数用户管理使用说明，以及 [Cloud 设置指南](set-up-for-cloud.md)。自托管 n8n 需要额外步骤配置实例，请参阅[自托管指南](../../deploy/host-n8n/configure-n8n/user-management.md)。

本节还介绍如何在 n8n 中配置 [LDAP](verify-user-identity/connect-ldap.md) 和 [SAML](verify-user-identity/use-saml/README.md)。

## 本节内容 <a id="in-this-section"></a>

* [设置 Cloud 用户管理](set-up-for-cloud.md)：在 n8n Cloud 上设置用户管理。
* [添加和移除用户](add-and-remove-users.md)：删除用户，以及重新发送待接受的邀请。
* [理解实例角色](understand-instance-roles.md)：内置的 Owner、Admin、Member 和 Chat user 角色。
* [控制节点可用性](control-node-availability.md)：为实例或项目阻止或允许节点。
* [设置权限与角色（RBAC）](set-permissions-and-roles-rbac/README.md)：在实例和项目级别控制访问。
* [验证用户身份](verify-user-identity/README.md)：要求双因素身份验证，或连接 LDAP、SAML、OIDC。
* [遵循最佳实践](follow-best-practices.md)：用户管理最佳实践。

## 相关资源 <a id="related-resources"></a>

* [管理](../)
* [使用源代码管理与环境](../use-source-control-and-environments/README.md)
* [管理凭据](../manage-credentials/README.md)
* [观测与日志](../observe-and-log/README.md)
