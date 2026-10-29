---
contentType: overview
title: 基于角色的访问控制（RBAC）
description: 在 n8n 中设置和使用基于角色的访问控制（RBAC）。
nodeTitle: 设置权限与角色（RBAC）
originalFilePath: user-management/rbac/index.md
originalUrl: https://docs.n8n.io/user-management/rbac
url: https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 基于角色的访问控制（RBAC）<a href="#role-based-access-control-rbac" id="role-based-access-control-rbac"></a>

{% hint style="info" %}
**功能可用范围**

项目角色可用于：

- **n8n Cloud：**所有套餐。
- **自托管：**Registered Community、Business、Enterprise。

自定义角色，包括实例和项目角色，可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**企业版。
{% endhint %}

n8n 中的 RBAC 允许在两个级别控制访问：

* **实例角色**：决定用户在整个实例中能执行的操作。内置实例角色为 Owner、Admin、Member 和 Chat user，也可以创建自定义实例角色进行更细致的控制。参阅[实例角色](../understand-instance-roles.md)。
* **项目角色**：决定用户在特定项目中能执行的操作。将工作流和凭据归入项目后，同一用户可以在不同项目中具有不同项目角色。参阅[查看可用角色](see-available-roles.md)。

本节介绍如何在 n8n 中设置和使用 RBAC。

## 本节内容 <a id="in-this-section"></a>

* [查看可用角色](see-available-roles.md)：了解 n8n 可用的 RBAC 角色及其访问权限。
* [使用项目组织工作](organize-work-in-projects.md)：了解 n8n 如何通过项目实现 RBAC。
* [自定义角色](create-custom-roles.md)：在内置角色之外定义细粒度权限。

## 相关资源 <a id="related-resources"></a>

* [管理用户与访问](../)
* [设置 Cloud 用户管理](../set-up-for-cloud.md)
* [添加和移除用户](../add-and-remove-users.md)
* [理解实例角色](../understand-instance-roles.md)
* [验证用户身份](../verify-user-identity/README.md)
* [遵循最佳实践](../follow-best-practices.md)
