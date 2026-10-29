---
title: 自定义角色
description: n8n 项目级和实例级自定义角色概览。
contentType: overview
nodeTitle: 自定义角色
url: https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 自定义角色 <a href="#custom-roles" id="custom-roles"></a>

{% hint style="info" %}
**功能可用范围**

自定义角色可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**企业版。
{% endhint %}

自定义角色允许在内置角色之外定义细粒度权限，无需授予完整 Admin 权限，可以创建仅包含用户所需能力的角色。

n8n 有两类自定义角色：限定于单个项目的项目角色，以及适用于整个 n8n 实例的实例角色。

## 本节内容 <a id="in-this-section"></a>

* [创建自定义项目角色](create-custom-project-roles.md)：定义特定项目内的权限，包括工作流、凭据、文件夹和其他项目资源的访问权限。将其分配给项目成员，控制他们在该项目中能执行的操作。

* [创建自定义实例角色](create-custom-instance-roles.md)：定义适用于整个实例的权限，例如管理用户、标签、API 密钥或自定义角色本身。分配给需要特定实例级能力、但无需完整 Admin 权限的用户。

## 相关资源 <a id="related-resources"></a>

* [设置权限与角色（RBAC）](./)
* [查看可用角色](see-available-roles.md)
* [使用项目组织工作](organize-work-in-projects.md)
