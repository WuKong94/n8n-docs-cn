---
description: n8n 实例角色。
contentType: reference
nodeTitle: 理解实例角色
originalFilePath: user-management/account-types.md
originalUrl: https://docs.n8n.io/user-management/account-types
url: https://docs.n8n.io/administer/manage-users-and-access/understand-instance-roles
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 实例角色 <a href="#instance-roles" id="instance-roles"></a>

每个用户都有一个实例角色，决定其在整个 n8n 实例中的权限和访问范围。

四个内置实例角色为 Owner（所有者）、Admin（管理员）、Member（成员）和 Chat user（聊天用户）。如果不满足需求，可以创建具有细粒度权限的[自定义实例角色](set-permissions-and-roles-rbac/create-custom-instance-roles.md)。

{% hint style="info" %}
**功能可用范围**

**Admin**（管理员）角色可用于：

- **n8n Cloud：**Pro、Enterprise。
- **自托管：**企业版。
{% endhint %}

{% hint style="info" %}
**功能可用范围**

**Chat user**（聊天用户）角色可用于：

- **n8n Cloud：**Pro、Enterprise。
- **自托管：**企业版。

Chat user 角色需要启用 Chat 功能。
{% endhint %}

{% hint style="info" %}
**实例角色与项目角色**

n8n 有两个级别的角色。实例角色控制用户在整个实例中能执行的操作；项目角色属于 [RBAC](set-permissions-and-roles-rbac/README.md)，控制用户在特定项目中的操作，同一用户可在不同项目中拥有不同项目角色。
{% endhint %}

{% hint style="info" %}
**为所有者创建 Member 角色账号**

n8n 建议所有者为自己创建第二个账号，使用 **Member**（成员）角色。所有者可以查看和编辑所有工作流、凭据和项目，但无法查看特定工作流的创建者，因此以所有者身份构建和编辑工作流，可能覆盖其他人的工作。
{% endhint %}


| 权限 | Owner，所有者 | Admin，管理员 | Member，成员 | Chat user，聊天用户 |
| ---------- |------ | ----- | ------ | --------- |
| 管理自己的邮箱和密码 | ✅ | ✅ | ✅ | ✅ |
| 管理自己的工作流 | ✅ | ✅ | ✅ | ❌ |
| 查看、创建和使用标签 | ✅ | ✅ | ✅ | ❌ |
| 删除标签 | ✅ | ✅ | ❌ | ❌ |
| 查看和共享所有工作流 | ✅ | ✅ | ❌ | ❌ |
| 查看、编辑和共享所有凭据 | ✅ | ✅ | ❌ | ❌ |
| 设置和使用[源代码管理](../use-source-control-and-environments/README.md) | ✅ | ✅ | ❌ | ❌ |
| 创建[项目](set-permissions-and-roles-rbac/organize-work-in-projects.md) | ✅ | ✅ | ❌ | ❌ |
| 查看所有项目 | ✅ | ✅ | ❌ | ❌ |
| 添加和移除用户 | ✅ | ✅ | ❌ | ❌ |
| 访问 n8n Cloud 控制台 | ✅ | ❌ | ❌ | ❌ |

## Chat user 角色 <a id="chat-user-role"></a>
Chat user 角色适合只需要通过 Chat 使用 n8n 的用户，不能构建工作流或访问其他 n8n 功能。

**Chat user 可以：**

- 在 Chat 中发送消息。
- 创建、编辑和删除自己的聊天智能体。
- 在 Chat 中运行共享给他们的工作流和智能体。

**Chat user 不可以：**

- 创建、查看或编辑工作流或凭据。
- 创建项目，或查看自己不属于的项目。
- 创建 API 密钥。
- 使用部分 Chat 工具类型，详情请参阅 Chat 文档。

启用 Chat 功能后，Chat user 登录时，n8n 会为其打开 Chat。

**将用户角色改为 Chat user，或从 Chat user 改为其他角色**

将用户角色更改为 Chat user，会产生以下影响：

- n8n 将该用户从所有与他人共享的项目中移除。如果用户是某项目唯一的管理员，n8n 会阻止更改，请先为项目分配另一名管理员。
- 用户的个人项目变为只读。
- n8n 删除该用户的全部 API 密钥。
- 将 Chat user 改为其他角色后，用户重新获得个人项目所有权，但 n8n 不会恢复其成为 Chat user 时失去的项目成员资格或 API 密钥。

## 自定义实例角色 <a href="#custom-instance-roles" id="custom-instance-roles"></a>

内置角色不符合访问需求时，可以创建细粒度权限的自定义实例角色，授予特定实例级能力，例如管理用户、标签或 API 密钥，无需提供完整 Admin 权限。

创建和管理方式请参阅[创建自定义实例角色](set-permissions-and-roles-rbac/create-custom-instance-roles.md)。

## 相关资源 <a id="related-resources"></a>

* [管理用户与访问](./)
* [设置 Cloud 用户管理](set-up-for-cloud.md)
* [添加和移除用户](add-and-remove-users.md)
* [设置权限与角色（RBAC）](set-permissions-and-roles-rbac/README.md)
* [验证用户身份](verify-user-identity/README.md)
* [遵循最佳实践](follow-best-practices.md)
