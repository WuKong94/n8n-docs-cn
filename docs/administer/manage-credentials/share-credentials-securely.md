---
title: 凭据共享
contentType: howto
nodeTitle: 安全共享凭据
originalFilePath: credentials/credential-sharing.md
originalUrl: https://docs.n8n.io/credentials/credential-sharing
url: https://docs.n8n.io/administer/manage-credentials/share-credentials-securely
description: 在组织内共享凭据。
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


# 安全共享凭据 <a id="share-credentials-securely"></a>

{% hint style="info" %}
**功能可用范围**

凭据共享可用于：

- **n8n Cloud：**所有套餐。
- **自托管：**商业版、企业版。
{% endhint %}

可以将凭据直接共享给其他用户，供其工作流使用；也可以共享到项目[^1]，供项目全部成员使用。使用共享凭据的用户无法查看或编辑凭据详情。

在所属团队项目中使用自己的凭据，无需共享。只有其他人需要用它运行或发布工作流时，才需共享。个人凭据在团队项目中的行为，以及工作流运行代表谁操作，请参阅[在项目中使用个人凭据](use-personal-credentials-in-projects.md)。

用户可以共享自己创建并拥有的凭据。对于在项目内创建且由项目拥有的凭据，只有项目管理员可以共享。实例所有者和管理员可以查看和共享实例上的全部凭据。**Sharing**（共享）选项卡中，只有凭据所有者，或具有凭据共享权限的用户，才能更改共享对象。

所有者和管理员的更多信息请参阅[实例角色](../manage-users-and-access/understand-instance-roles.md)。

在[项目](../manage-users-and-access/set-permissions-and-roles-rbac/README.md)中，用户角色控制其与所属项目的工作流和凭据如何交互。

{% hint style="info" %}
**共享最终用户凭据**

共享[最终用户凭据](end-user-credentials.md)时，共享的是凭据本身，而非连接。共享对象连接自己的账号，不会使用你的账号。
{% endhint %}

## 共享凭据 <a href="#share-a-credential" id="share-a-credential"></a>

要共享凭据：

1. 从左侧菜单选择 **Overview**（概览）或某个项目。
2. 选择 **Credentials**（凭据），查看凭据列表。
3. 选择要共享的凭据。
4. 选择 **Sharing**（共享）。
5. 在 **Share with projects or users**（与项目或用户共享）下拉菜单中，浏览或搜索共享对象。
6. 选择用户或项目。
7. 选择 **Save**（保存）应用更改。

共享对象获得 **Can use**（可使用）角色，可以使用凭据运行和发布工作流，但无法查看或编辑详情。

## 理解 Sharing 选项卡 <a id="understand-the-sharing-tab"></a>

**Sharing**（共享）选项卡列出所有有权访问凭据的人，以及使用凭据的项目：

* **已共享项目**：成员根据[项目角色](../manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles.md)使用凭据。
* **使用凭据但未获共享的项目**：某成员将个人凭据添加到项目的某个工作流中。项目带有 **Can view**（可查看）标签，成员可在工作流中看到凭据，但无法使用或编辑。你直接共享的成员仍可使用。要向整个项目授予访问权限，请选择 **Share**（共享）。

团队项目中，所有者和管理员遵循与其他人相同的共享规则：只有你将凭据共享给他们后，才能使用。实例角色带来的额外使用权限仅适用于他们自己的个人空间。

## 移除凭据访问权限 <a href="#remove-access-to-a-credential" id="remove-access-to-a-credential"></a>

要取消共享凭据：

1. 从左侧菜单选择 **Overview**（概览）或某个项目。
2. 选择 **Credentials**（凭据），查看凭据列表。
3. 选择要取消共享的凭据。
4. 选择 **Sharing**（共享）。
5. 在共享用户和项目列表中，选择待移除对象上的**垃圾桶图标**<img src="../.gitbook/assets/delete-node (1).png" alt="垃圾桶图标" data-size="line">。
6. 选择 **Save**（保存）应用更改。

[^1]: n8n 项目将工作流、变量和凭据分成不同组，便于管理。通过共享和划分相关资源，项目让团队协作更方便。

## 相关资源 <a id="related-resources"></a>

* [管理凭据](./)
* [在项目中使用个人凭据](use-personal-credentials-in-projects.md)
* [最终用户凭据](end-user-credentials.md)
* [凭据覆盖](credential-overwrites.md)
* [使用外部密钥存储](use-external-secret-stores.md)
