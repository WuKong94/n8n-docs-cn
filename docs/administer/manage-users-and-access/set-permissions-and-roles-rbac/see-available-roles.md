---
title: RBAC 角色类型
description: 了解 n8n 可用的 RBAC 角色及其访问权限。
contentType: reference
nodeTitle: 查看可用角色
originalFilePath: user-management/rbac/role-types.md
originalUrl: https://docs.n8n.io/user-management/rbac/role-types
url: https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# RBAC 角色类型 <a href="#rbac-role-types" id="rbac-role-types"></a>

{% hint style="info" %}
**功能可用范围**

**Project Editor**（项目编辑者）角色可用于：

- **n8n Cloud：**Pro。
- **自托管：**企业版。

**Project Viewer**（项目查看者）角色可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**企业版。
{% endhint %}

项目内有三个用户角色：Admin（管理员）、Editor（编辑者）和 Viewer（查看者），控制用户在项目中能执行的操作。同一用户可在不同项目中拥有不同角色。

## 项目管理员 <a href="#project-admin" id="project-admin"></a>

Project Admin 具有最高级别权限，可以：

* 管理项目设置：更改名称、删除项目。
* 管理项目成员：邀请和移除成员，更改成员角色。
* 查看、创建、更新和删除项目内的任意工作流、凭据或执行。
* 创建[最终用户凭据](../../manage-credentials/end-user-credentials.md)。默认只有项目管理员可以创建此凭据类型，但可通过自定义角色将权限授予其他用户。

## 项目编辑者 <a href="#project-editor" id="project-editor"></a>

Project Editor 可以查看、创建、更新和删除项目内的任意工作流、凭据或执行。**Project Editor** 角色可用于 n8n Cloud Pro 和自托管 Enterprise。

## 项目查看者 <a href="#project-viewer" id="project-viewer"></a>

Project Viewer 实际上是 `read-only` 角色，可访问项目内的全部工作流、凭据和执行。

查看者无法手动执行项目中的任何工作流。

**Project Viewer** 角色可用于 n8n Cloud Enterprise 和自托管 Enterprise。

{% hint style="info" %}
**项目角色与实例角色**

n8n 有两个级别的角色。[实例角色](../understand-instance-roles.md)控制用户在整个实例中能执行的操作；项目角色控制用户在特定[项目](organize-work-in-projects.md)中的操作，同一用户可在不同项目中拥有不同项目角色。
{% endhint %}

| 权限 | Admin，管理员 | Editor，编辑者 | Viewer，查看者 |
| ---------- |------ | ------ | ------ | 
| 查看项目中的工作流 | ✅ | ✅ | ✅ |
| 查看项目中的凭据 | ✅ | ✅ | ✅ |
| 查看执行 | ✅ | ✅ | ✅ |
| 编辑凭据和工作流 | ✅ | ✅ | ❌ |
| 添加工作流和凭据 | ✅ | ✅ | ❌ |
| 执行工作流 | ✅ | ✅ | ❌ |
| 管理成员 | ✅ | ❌ | ❌ |
| 修改项目 | ✅ | ❌ | ❌ |
| 在凭据中使用外部密钥 | ✅* | ✅* | ❌ |
| 管理项目密钥保管库 | ✅* | ❌ | ❌ |

\* 需要实例所有者或管理员启用 **Enable external secrets for project roles**（为项目角色启用外部密钥）。参阅[项目角色的访问权限](../../manage-credentials/use-external-secret-stores.md#access-for-project-roles)。此设置自 n8n 2.13.0 起提供。

项目角色适用于项目持有的凭据，不代表你可以在项目工作流中使用其他成员的个人凭据。只有凭据所有者或其直接共享的对象，才能使用该凭据运行或发布。参阅[在项目中使用个人凭据](../../manage-credentials/use-personal-credentials-in-projects.md)。

[变量](../../../build/code-in-n8n/define-custom-variables.md)和[标签](../../../build/manage-workflows/tag-workflows.md)不受 RBAC 影响，它们在整个 n8n 实例中全局可用。

译注：本页原文把变量全部描述为实例全局资源，但同一版本的“自定义变量”文档说明，自 n8n 1.118.0 起还支持项目变量；“自定义项目角色”也列出项目变量权限。此处保留原文并提示差异，不把全局描述套用于所有变量。

## 相关资源 <a id="related-resources"></a>

* [设置权限与角色（RBAC）](./)
* [使用项目组织工作](organize-work-in-projects.md)
* [自定义角色](create-custom-roles.md)
