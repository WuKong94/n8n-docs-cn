---
title: RBAC 项目
contentType: howto
nodeTitle: 使用项目组织工作
originalFilePath: user-management/rbac/projects.md
originalUrl: https://docs.n8n.io/user-management/rbac/projects
url: https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects
description: 了解 n8n 如何通过项目实现 RBAC，以及如何创建和管理项目。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 使用项目组织工作 <a id="organize-work-in-projects"></a>

{% hint style="info" %}
**功能可用范围**

RBAC 可用于：

- **n8n Cloud：**所有套餐。
- **自托管：**Registered Community、Business、Enterprise。

不同套餐支持的项目和角色数量不同。
{% endhint %}

n8n 使用项目归类工作流和凭据[^1]，并为每个项目中的用户分配[角色](see-available-roles.md)。同一用户可在不同项目中具有不同角色，从而获得不同访问权限。

### 创建项目 <a href="#create-a-project" id="create-a-project"></a>

实例所有者和实例管理员可以创建项目。

要创建项目：

1. 选择 <img src="../../.gitbook/assets/plus.png" alt="加号图标" data-size="line"> **Add project**（添加项目）。
2. 填写项目设置。
3. 选择 **Save**（保存）。

### 在项目中添加和移除用户 <a href="#add-and-remove-users-in-a-project" id="add-and-remove-users-in-a-project"></a>

项目管理员可以添加和移除用户。

要向项目添加用户：

1. 选择项目。
2. 选择 **Project settings**（项目设置）。
3. 在 **Project members**（项目成员）下浏览用户，或按用户名、邮箱搜索。
4. 选择要添加的用户。
5. 检查[角色类型](see-available-roles.md)，按需更改。
6. 选择 **Save**（保存）。

要从项目移除用户：

1. 选择项目。
2. 选择 **Project settings**（项目设置）。
3. 在待移除用户的**三点菜单**中，选择 **Remove user**（移除用户）。
4. 选择 **Save**（保存）。

### 删除项目 <a href="#delete-a-project" id="delete-a-project"></a>

要删除项目：

1. 选择项目。
2. 选择 **Project settings**（项目设置）。
3. 选择 **Delete project**（删除项目）。
4. 选择如何处理工作流和凭据：
   * **Transfer its workflows and credentials to another project**（将其工作流和凭据转移到其他项目）：n8n 提示选择接收数据的项目。
   * **Delete its workflows and credentials**（删除其工作流和凭据）：n8n 提示确认删除项目中的所有数据。

### 收藏项目 <a href="#favorite-a-project" id="favorite-a-project"></a>

可以收藏团队项目，将其固定以便快速访问。打开项目，选择项目标题中的星形图标，或打开**三点菜单**并选择 **Favorite**（收藏）。详情请参阅[收藏项目](../../../build/manage-workflows/favorite-items.md)，其中也说明如何以相同方式收藏工作流、文件夹和数据表。

### 在项目或用户之间移动工作流和凭据 <a href="#move-workflows-and-credentials-between-projects-or-users" id="move-workflows-and-credentials-between-projects-or-users"></a>

工作流和凭据所有者可以将其移动到自己有权访问的其他用户或项目，更改所有权。

{% hint style="warning" %}
**移动会撤销共享**

移动工作流或凭据会移除所有现有共享，可能影响当前共享这些资源的其他工作流。
{% endhint %}

1.  选择 **Workflow menu**（工作流菜单）<img src="../../.gitbook/assets/three-dot-options-menu (1).png" alt="工作流菜单图标" data-size="line"> 或 **Credential menu**（凭据菜单）<img src="../../.gitbook/assets/three-dot-options-menu (1).png" alt="工作流菜单图标" data-size="line"> > **Move**（移动）。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>移动带凭据的工作流</strong></p><p>移动工作流时，如果其中凭据是你有权共享的，可以选择同时共享凭据，确保工作流继续拥有执行所需的凭据访问权限。n8n 会指出无法移动的凭据，即你无权共享的凭据。</p></div>
2. 选择目标项目或用户。
3. 选择 **Next**（下一步）。
4. 确认理解移动的影响：目标项目中缺少所需凭据时，工作流可能无法运行，n8n 也会移除当前所有针对个人的共享。
5. 选择 **Confirm move to new project**（确认移动到新项目）。

### 在团队项目中使用个人凭据 <a id="use-personal-credentials-in-team-projects"></a>

项目成员可以在所属团队项目的任意工作流中，选择自己的个人凭据，无需将凭据共享给项目。凭据选择器将凭据分组为 **Available to you**（你可用的个人凭据）和 **Available in** _项目名称_（项目中可用的凭据）。

只有凭据所有者及其直接共享的对象，才能使用该凭据运行或发布工作流。要让每位项目成员都能使用，请将凭据共享给项目。参阅[在项目中使用个人凭据](../../manage-credentials/use-personal-credentials-in-projects.md)。

[^1]: 在 n8n 中，凭据保存连接特定应用和服务所需的身份验证信息。使用用户名和密码、API 密钥、OAuth 密钥等信息创建凭据后，就可以通过相应应用节点与服务交互。

## 相关资源 <a id="related-resources"></a>

* [设置权限与角色（RBAC）](./)
* [查看可用角色](see-available-roles.md)
* [自定义角色](create-custom-roles.md)
