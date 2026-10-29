---
title: 自定义实例角色
description: 在 n8n 中创建和管理具有细粒度权限的自定义实例角色。
contentType: howto
nodeTitle: 创建自定义实例角色
url: https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-instance-roles
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 自定义实例角色 <a href="#custom-instance-roles" id="custom-instance-roles"></a>

{% hint style="info" %}
**功能可用范围**

自定义实例角色可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**企业版。

自 n8n 2.30.0 起提供，该版本于 2026 年 7 月 7 日发布。
{% endhint %}

{% hint style="info" %}
**实例角色与项目角色**

n8n 有两类自定义角色：

**自定义实例角色**：与用户在实例级别所需的管理能力相关的角色。

**自定义项目角色**：适用于特定项目内的角色。参阅[创建自定义项目角色](create-custom-project-roles.md)。
{% endhint %}

自定义实例角色允许授予用户特定实例级能力，无需提供完整 Admin 权限。不同于 Owner、Admin、Member、Chat user 等内置角色，自定义实例角色可以为实例设置、用户管理和其他实例级管理定义细粒度权限。

## 创建自定义实例角色 <a href="#create-a-custom-instance-role" id="create-a-custom-instance-role"></a>

实例所有者和实例管理员可以创建自定义实例角色。

要创建自定义实例角色：

1. 前往 **Settings**（设置）> **Roles**（角色）> **Instance roles**（实例角色）。
2. 选择 **Create role**（创建角色）。
3. 输入角色名称，以及可选描述。
4. 可选择 **Preset**（预设），包括 **Admin**、**Member**，按内置角色预填权限，再按需调整。
5. 选择此角色的权限：
   * **Instance settings**（实例设置）> **Manage**（管理）：查看和更改实例级设置。
   * **Members**（成员）> **Manage**（管理）：在整个实例中邀请、移除和更新用户。
   * **Roles**（角色）> **Manage project roles**（管理项目角色）：仅创建、编辑和删除自定义项目角色。
   * **Roles**（角色）> **Manage all roles**（管理所有角色）：创建、编辑和删除全部自定义角色，包括实例和项目角色。选择后自动包含 **Manage project roles**。
   * **API keys**（API 密钥）> **Manage own**（管理自己的）：创建和删除用户自己的 API 密钥。
   * **API keys**（API 密钥）> **Manage others**（管理他人的）：查看和删除其他用户的 API 密钥，自动包含 **Manage own**。
   * **Tags**（标签）> **View**（查看）：查看全部标签。
   * **Tags**（标签）> **Manage**（管理）：创建、编辑和删除标签。
   * **Projects**（项目）> **Create**（创建）：创建新项目。
   * **Insights**（洞察）> **View**（查看）：查看实例级洞察。
6. 选择 **Save**（保存）。

## 将自定义实例角色分配给用户 <a href="#assign-a-custom-instance-role-to-users" id="assign-a-custom-instance-role-to-users"></a>

具有 **Roles: Manage all roles**（角色：管理所有角色）权限的用户，可以分配自定义实例角色。

要分配自定义实例角色：

1. 前往 **Settings**（设置）> **Users**（用户）。
2. 找到要更新的用户。
3. 选择用户当前角色，打开角色下拉菜单。
4. 在 **Custom roles**（自定义角色）下，选择要分配的角色。

## 编辑自定义实例角色 <a href="#edit-a-custom-instance-role" id="edit-a-custom-instance-role"></a>

要更新现有自定义实例角色：

1. 前往 **Settings**（设置）> **Roles**（角色）> **Instance roles**（实例角色）。
2. 找到要编辑的自定义角色。
3. 选择**三点菜单** > **Edit**（编辑）。
4. 更新角色名称、描述或权限。
5. 选择 **Save changes**（保存更改）。

{% hint style="warning" %}
**编辑会影响所有已分配此角色的用户**

更改自定义实例角色，会对整个实例中所有具有该角色的用户生效。
{% endhint %}

## 复制自定义实例角色 <a href="#duplicate-a-custom-instance-role" id="duplicate-a-custom-instance-role"></a>

要基于现有角色创建新角色：

1. 前往 **Settings**（设置）> **Roles**（角色）> **Instance roles**（实例角色）。
2. 找到要复制的角色。
3. 选择**三点菜单** > **Duplicate**（复制）。
4. 按需更新角色名称和权限。
5. 选择 **Create role**（创建角色）。

## 删除自定义实例角色 <a href="#delete-a-custom-instance-role" id="delete-a-custom-instance-role"></a>

要删除自定义实例角色：

1. 前往 **Settings**（设置）> **Roles**（角色）> **Instance roles**（实例角色）。
2. 找到要删除的角色。
3. 选择**三点菜单** > **Delete**（删除）。
4. 确认删除。

{% hint style="info" %}
**删除前请重新分配用户角色**

如果有用户使用此角色，请先为其重新分配其他角色，再删除。
{% endhint %}

## 权限参考 <a href="#permissions-reference" id="permissions-reference"></a>

下表按 **Instance roles**（实例角色）编辑器中的显示方式，说明各权限组及其复选框。

| 分组 | 复选框 | 允许的操作 |
| ----- | -------- | -------------- |
| Instance settings（实例设置） | Manage（管理） | 查看和更改实例级设置。 |
| Members（成员） | Manage（管理） | 在整个实例中邀请、移除和更新用户。 |
| Roles（角色） | Manage project roles（管理项目角色） | 仅创建、编辑、复制、删除和分配自定义项目角色。 |
| Roles（角色） | Manage all roles（管理所有角色） | 创建、编辑、复制、删除和分配全部自定义角色，包括实例和项目角色。自动包含 **Manage project roles**。 |
| API keys（API 密钥） | Manage own（管理自己的） | 创建和删除用户自己的 API 密钥。 |
| API keys（API 密钥） | Manage others（管理他人的） | 查看和删除其他用户的 API 密钥。自动包含 **Manage own**。 |
| Tags（标签） | View（查看） | 查看全部标签。 |
| Tags（标签） | Manage（管理） | 创建、编辑和删除标签。 |
| Projects（项目） | Create（创建） | 创建新项目。 |
| Insights（洞察） | View（查看） | 查看实例级洞察和使用数据。 |

{% hint style="warning" %}
**权限提升风险**

某些权限组合会带来权限提升风险：

* 拥有 **Roles: Manage all roles**（角色：管理所有角色）的用户，可以编辑自己的自定义角色，添加原本未被授予的权限。
* 拥有 **Members: Manage**（成员：管理）的用户，可以邀请其控制的用户，再授予该用户管理员级权限。
* 拥有 **Roles: Manage project roles**（角色：管理项目角色）的用户，可以编辑自己持有的自定义项目角色，给自己添加在该项目中原本未被授予的权限。

仅将这些权限分配给完全可信的用户，非必要时避免组合使用。
{% endhint %}

## 相关资源 <a id="related-resources"></a>

* [自定义角色](create-custom-roles.md)
* [创建自定义项目角色](create-custom-project-roles.md)

